# Dashboard design notes

## Data file: `app/data/datasets.json` (since 2026-11-17)

Replaced the CSV (user's choice: JSON, because a dataset can have several
access links and more metadata is coming). Shape:

```json
{ "datasets": [ {
    "id": "gpcc-monitoring-noaa-psl-mirror-dwd-gpcc-source",
    "name": "...", "data_archive": "...", "precipitation_basis": "...",
    "period_of_record": "...", "formal_cdr": "...", "update_status": "...",
    "spatial_coverage": "...", "resolution": "...", "temporal_frequency": "...",
    "curator": "...", "doi": "", "notes": "...",
    "access_endpoints": [
      { "name": "DWD/GPCC archive", "url": "https://...", "role": "primary" },
      { "name": "NOAA PSL mirror",  "url": "https://...", "role": "mirror" } ]
} ] }
```

- `role` is `primary`, `alternative` or `mirror`; it's stored but not shown yet.
- `id` is a stable slug of the name and must be unique and use only
  lowercase letters, digits and hyphens. The page uses it for the `open`
  URL parameter, the `#dataset-<id>` jump, the card's `id="dataset-<id>"`
  and the panel's `id="details-<id>"`. A good key for the future dataset
  page too.
- Endpoints came from `my_docs/about_data/Data archives by dataset.md`
  (links only; archives listed there without a link were left out). Tracking
  `utm_` parameters were removed. One-time build script:
  `.work/build_json.py` (not in git).
- `curator`, `doi`, `notes` (added 2026-11-18) come from the user's
  `my_docs/about_data/master_climate_inventory_subset.json`, merged by
  `.work/merge_inventory.py` (not in git). Matching used a hand-made list of
  inventory id → dataset id, because URL matching linked only 4 of 14 and two
  wrongly. Matched datasets kept all their existing values; the inventory URL
  was added as an `alternative` endpoint when new. Four inventory entries
  became new datasets (TerraClimate, WorldClim, CMAP, CoCoRaHS) with
  blank basis/CDR/update/resolution/frequency for the user to fill in.
  DS-234 ("GPCC") was added, then dropped as a duplicate of the existing
  GPCC datasets. CHIRPS notes had "50°S-50°N land" removed (wrong for v3).
  An `email` key was there too (always blank, public site) until
  2026-11-21, when the user had it removed from the data and the panel.
  Every dataset has all three keys ("" when unknown). The panel shows
  Curator and DOI (doi.org link) in the metadata grid, and a Notes
  section after it.
- Order (since 2026-11-18): datasets are sorted by data-source tag, then
  coverage tag (both alphabetical by label), then name, so the dashboard
  opens grouped. `.work/sort_datasets.py` (not in git) re-sorts; it copies
  the tag rules from app.js, so update both if the rules change. The
  "Dataset 001" card number follows the file order; links use ids, so
  re-sorting doesn't break them (links made before 2026-11-18 used
  numbers and no longer open a card).
- New fields: add them to each dataset object; to show one in the panel, add
  it to `COL` and `METADATA_FIELDS` in app.js. Search covers every text field
  plus endpoint names and URLs.

## JSON → card mapping

| Card part | JSON field |
|---|---|
| Title | `name` |
| Label line "DATASET 007 / REANALYSIS" | position in the list + derived data-source type |
| Description | `precipitation_basis` |
| Tags | data-source type, coverage, short period (e.g. `1940–present`), `NOAA CDR` if `formal_cdr` starts with "YES" |
| Panel: Update status | `update_status` |
| Panel: metadata grid | `data_archive`, `period_of_record`, `spatial_coverage`, `resolution`, `temporal_frequency`, `formal_cdr` |
| Panel: Data access endpoints | `access_endpoints` → table (Name / Link address); links open in a new tab, link text is the URL without `https://` |

## Derived categories (`CATEGORIES`, `COVERAGES` in app.js)

(Rules below say "basis", "CDR field" etc. — the matching JSON fields.)

First matching rule wins.

- Data source: "blend"/"merged" in basis → Merged; "reanalysis" in basis or
  CDR field → Reanalysis; "satellite"/"microwave"/"IR" → Satellite; else Gauge-based.
- Coverage: "United States"/"CONUS" → CONUS; "North America"/"Canada" →
  North America; starts with "land"/"global land" and no ocean → Global land;
  "quasi"/"near-global"/a band like 60°S–60°N (not 90°S) → Quasi-global; else Global.
- Period tag: first year in the POR text, then "present" if the text says
  present/onward/most recent, else the latest year.

Result on the current CSV: Gauge 15, Satellite 12, Reanalysis 13, Merged 2;
CONUS 5, North America 2, Global land 11, Quasi-global 9, Global 15.

## Filters (multi-select, 2026-11-17)

- A click on an option button adds that option; a second click removes it.
  "All datasets" clears that group (it shows as pressed when nothing in the
  group is selected).
- Options in one group combine with OR; the two groups combine with AND
  (e.g. Satellite + Gauge-based and CONUS + Global land = datasets of either
  type that are in either coverage).
- URL: comma-separated lists, `?category=gauge,satellite&coverage=conus`.
  `FILTER_GROUPS` in app.js lists the groups.

## Differences from the design HTML in my_docs/

- The design HTML and CSS used different class names; the app uses the CSS's names.
- Card header is not a `<button>` wrapping headings (invalid HTML); the title is
  a button whose `::after` covers the whole header, so the whole header is clickable.
- Filter buttons and counts are generated from the data.
- Panel opens with a grid-rows animation; respects reduced motion.

## Layout and colors (2026-11-17, from my_docs/html_css_design/images/new_dashboard_layout_2026-11-17-6.46am.png)

Colors sampled from the image; all live as variables at the top of `app/styles.css`.

- Page (`--page-bg` `#E5EDF0`) shows at the sides; the whole `main.dashboard`
  (max 1200px) is navy `--deep-ocean` `#1F3244`, no top margin.
- Header text sits on the navy, indented 32px more than the panels below it.
  Label line `#A0B6C0`, description and meta `#C8D6DE`, rule `#5C7A8C`,
  title white bold 36px.
- Search bar: white, on the navy, 24px above the white panel.
- `.content-panel` (white) holds both the filters and the dataset index, so
  "Dataset index" and the cards sit in the same white area with dividers
  between cards. Filter headings, card labels and the "11 OF 42 DATASETS"
  counter are `--steel-blue` `#5C7A8C` (4.55:1 on white, passes AA).
- Footer is on the navy in `--on-navy-text` `#A0B6C0` (6.2:1).
- Active filter button `#1F3244`; inactive `#E3EDF0`.

### Card colors (2026-11-17, from the user)

- Page background `#D5E3EF` (`--page-bg`; was `#90A8BE` until session 4).
- Card `#E4EBF0` (`--dataset-card-bg`; was `#E3E8EC`) with a 4px `#235C70` line under each
  card (`--dataset-card-rule`); the last card has no line.
- Card header on hover and while open: `#CAD8E3` (`--dataset-card-hover`; was `#DAE4EC`).
- Open panel background white (`--dataset-details-bg`).
- Contrast fixes for the grey cards: card label line ("DATASET 008 /
  REANALYSIS") uses `--dataset-label-text` `#46606F` (steel-blue was 3.5:1; darkened from
  `#4A6575` in session 4 to pass 4.5:1 on the darker `#CAD8E3` hover);
  the plain tags (coverage, period) are white so they don't vanish into the
  card; `--muted-text` is `#5C7A8C` (4.55:1 on white).
- Data-source tags (from the user): Gauge `#79D49B`, Satellite `#B0ECFF`,
  Reanalysis `#C6B9FB`, Merged `#FFD28A`, all with text `#434343`
  (`--tag-category-text`; 5.5–7.7:1).

## Archive pages (2026-11-17, session 3)

A page about a data archive (not a dataset), shared by every dataset held
there. First one: NOAA NCEI, from the user's research answer
`answer_A1_Rstar_query_chatgpt-noaa_ncei.md` (in `my_docs/about_data/rstar_query_results/`).

- **Files**
  - `app/data/archives.json` lists the archives that have pages:
    `{ "archives": [ { "id", "name", "full_name", "data_archive_names": [...],
    "pages": [ { "id", "title", "as_of", "file" } ] } ] }`.
    `data_archive_names` are the names as written in a dataset's
    `data_archive` text (split on ";").
  - `app/content/archives/<archive id>/<page>.md`: the page text, kept as
    Markdown and rendered in the browser by `app/markdown.js` (a small
    renderer, written here, no library: headings, paragraphs, bold, code,
    links, nested lists, pipe tables; escapes all text first).
  - `app/archive.html` + `app/archive.js`: one page for every archive,
    `archive.html?id=noaa-ncei[&page=threats]`.
  - `app/shared.js`: helpers both pages use (paths, escapeHtml, fetchJson,
    archive matching, `dashboardQuery`). Loaded before app.js / archive.js.
  - `scripts/import_archive_page.py SOURCE.md DEST.md` copies a research
    answer in and removes the parts that point to the research project's own
    files (the closing "Saved in ..." paragraph and the "Pages to check by
    hand" / "Sites to trust" items). With `--record research-record.json`
    it also writes `<page>.json` next to the .md with
    `{ "question", "searched_on": [each subquestion's "question"] }`.
    With `--query rstar_query.md` it copies the R* query statement the
    research started from to `<page>.query.md`.
    Then add the page to `archives.json` (`file` = .md, `record` = .json,
    `query` = .query.md).
- **Under the page title** (its first `<h2>`), above the direct answer:
  1. the R* query (from `query`), rendered from Markdown in a pale box
     with a teal left rule; its `###` heading becomes an `<h3>`, styled
     like the other h3s (18px; h2 is 24px, body 15px) but with no top rule;
  2. "**Question:** <question>" and a "Searched on" list (from `record`).
- **Dropdown links** (changed 2026-11-19, session 8): "Data archive(s)" is
  its own section under the metadata grid (no longer a grid item): a table
  styled like the endpoints table, columns "Archive" and "About", one row
  per archive name. "Archive" links to the archive's website from
  `app/data/archive_links.json` (`{ "archive_links": { "<name>": "<url>" } }`,
  one key per name used in `data_archive`; blank = `href="#"` placeholder
  that doesn't jump). "About" is an "About archive" link to the archive's
  page, or "NA" if it has none. 10 datasets link to NCEI. Add new archive
  names to `archive_links.json` when adding datasets.
- **Back to the dashboard**: "About archive" links in a dataset panel carry
  the dashboard's `q`, `category`, `coverage` and `open=<that dataset only>`
  (user's request, session 8); the "R* metadata" row links carry every open
  card. The archive page's "← Back to dashboard" sends them back. Open-card
  ids that match no dataset (old card numbers like `21`) are dropped on load.
- **Dataset block** (session 8): each panel starts with an h4 "Dataset", the
  full name (to copy) and "Dataset web research" (was "About dataset"): a link to the dataset's
  optional `about_url` field in `datasets.json`, or "Dataset web research: NA" when
  it's missing/blank (the user's dataset pages come from another project);
  "Update status" is an h5.
- **Archive page layout**: same navy header as the dashboard (archive name,
  full name, dataset and page counts); white panel with "As of <date>" and
  the Markdown text (its `#` title becomes the page's `<h2>`, so the
  archive name is the only `<h1>`); a grey "Datasets in this archive" list.
  Wide tables scroll sideways inside their own box on phones. Content is
  indented 40px on desktop (user's request), 16px on phones.
- **Dataset links on the archive page** go to
  `index.html?<saved dashboard state, with the id added to open>#dataset-<id>`. The
  dashboard opens that card, scrolls it to the top of the screen and puts
  focus on its title (`jumpToCard` in app.js). If the saved search or
  filters would hide the card, they are cleared first. Each card has
  `id="dataset-<id>"` (the dataset's `id` from datasets.json).
- **More pages**: with two or more pages in `pages`, tabs appear above the
  text (WAI-ARIA tabs: arrow keys, Home/End); the chosen tab is in the URL
  as `&page=`. Tested with a temporary second page.
- Data and page files are fetched with `cache: "no-cache"`, so an edited
  file shows after a normal reload (CSS/JS still need Cmd+Shift+R).

### R* metadata row and instrument pages (2026-11-18, session 6)

- The dashboard has an "R* metadata" row under the coverage filters: one
  link per entry in `archives.json` ("<name> — about this archive" or
  "— about this instrument"), carrying the dashboard state like the panel
  links do.
- Instruments (NOAA Satellites, NASA Satellites, NOAA Rain Gauges, from the A4 R* query)
  are entries in `archives.json` with `"kind": "instrument"` and an empty
  `data_archive_names`; their files are in `content/instruments/<id>/`.
  They use `archive.html`, labelled "Instrument", with no "Datasets" list
  (no dataset field names an instrument yet). The NCEI entry has
  `"kind": "archive"`.
- Their R* query box text is the user's ("[Dependent infrastructure
  resilience]" / "Observation network or sensor platform at risk" / the
  description), written by hand to `<page>.query.md`, since the A4
  folders have no `rstar_query.md`.
- Import script additions: drops sentences naming research-project files
  (`results.csv`, `check-by-hand.md`, `sites-to-trust.md`, ...) and the
  "- Pages to check by hand" and "- **Sandbox:**" items; `--replace OLD NEW` rewrites text, used
  to point the NASA answer's "earlier NOAA run" link at
  `archive.html?id=noaa-satellites`. Links in a page to another
  `archive.html?...` page get the dashboard state added.
