# Plan: the workshop dashboard becomes the R* site's landing page

Written 2026-11-24. Not started. Two apps go into one site in this repo's `app/`:

- **The dashboard** (`/Users/claude/SIDE_WORK/NYCE_project/precip_workshop_dashboard/app`, its own git repo, clean at
  `257b125` on `develop`; `main` is one commit behind): the dataset cards with search, filters and open panels, plus
  the overview, web research and archive/instrument pages. About 3,300 lines of plain HTML/CSS/JS and 544 KB of
  `content/`.
- **The R* viewer** (this repo's `app/`): the R* score page (now `index.html`), 4 category pages and the score graph.

After the move, `index.html` is the dashboard. Each dataset card's panel has an "R* scores" link that opens that
dataset's R* score page, and the R* pages have "Back to dashboard", which brings back the search, filters and open
cards as they were.

## What the two apps have in common, and where they differ

| | Dashboard | R* viewer |
|---|---|---|
| Pages | `index.html`, `overview.html`, `dataset.html`, `archive.html` | `index.html`, 4 category pages, `graph.html` |
| Code | `app.js`, `shared.js`, `overview.js`, `dataset.js`, `dataset-search.js`, `archive.js`, `markdown.js`, `styles.css`, all at the root of `app/` | `assets/app.js`, `assets/graph.js`, `assets/styles.css` |
| Data | `data/*.json` and `content/`, **fetched** (needs a web server) | `data/rstar-data.js`, loaded with a `<script>` tag (works from disk) |
| Dataset ids | `ghcn-d`, `gpcp-daily-v3-3`, `imerg-late-run-v07`, `noaa-ncei-persiann-cdr-v1r1` | `ghcn-daily`, `gpcp-daily`, `persiann-cdr-daily` (no IMERG yet) |
| State in the URL | `q`, `category`, `coverage`, `open` | `dataset`, `evidence` |
| Look | Navy panel, IBM Plex, light only | Light and dark from the system setting |
| Tests | None (Playwright never set up) | 116 Python Playwright tests |
| Published | https://lmerchant.github.io/precip_workshop_dashboard/ | https://lmerchant.github.io/Rstar_precipitation-relationships/ |

No file names clash: the dashboard's `data/*.json` and `content/` sit next to `data/rstar-data.js`, and its
stylesheet and scripts can move into `assets/` under new names. The URL parameter names don't clash either.

**The ids differ, and both sets are hard to change.** The R* ids are the folder names in `data-rstar-categories/`, the
keys of everyone's saved choices in `localStorage` (`rstar-chosen-scores-v1`) and the ids in saved score files, so
renaming them would lose people's scores. The dashboard ids are in bookmarks, `content/datasets/<id>/` and the
research pages' URLs. So keep both and link them (step 3).

## Steps

### 1. Copy the dashboard in

- **Pages** at the root of `app/`, so their relative links keep working: the dashboard's `index.html` (replacing the
  R* one, which moves first; see step 2), `overview.html`, `dataset.html`, `archive.html`.
- **Code** into `app/assets/dashboard/`, so it can't be mixed up with the R* code: `dashboard.js` (was `app.js`),
  `dashboard.css` (was `styles.css`), `shared.js`, `overview.js`, `dataset.js`, `dataset-search.js`, `archive.js`,
  `markdown.js`. Update the `<script>` and `<link>` tags in the 4 pages.
- **Data and text:** `data/datasets.json`, `archives.json`, `archive_links.json`, `dataset_pages.json` into
  `app/data/`; `content/` into `app/content/`. Their paths in `shared.js` stay as they are (relative to the page).
- **Scripts** into `scripts/dashboard/`: `import_archive_page.py`, `import_dataset_pages.py`,
  `import_dataset_overviews.py`, `research_text.py`, and `.work/sort_datasets.py` (it is needed after every rename, so
  it should be tracked). Change their `app/` output paths. Their inputs are in the dashboard project's `my_docs/`
  (the user's own files, kept out of git); see question 3.
- **Notes:** the dashboard's `notes/*.md` (design notes and the two how-tos) into `notes/dashboard/`, and the parts of
  its `HANDOFF.md` that still matter into this `HANDOFF.md`.
- Each page keeps its own stylesheet, so the dashboard looks as it does now and the R* pages as they do now.
- One commit, whose message names the source repo and commit (`257b125`). Its history stays in the old repo (see
  question 1 for keeping it).

### 2. Move the R* score page to `scores.html`

- Rename `app/index.html` to `app/scores.html` and set `data-page="scores"` (`render()` in `assets/app.js` treats
  anything not category or graph as this page, so only the label changes).
- Point the 3 links that go to `index.html` at `scores.html`: the "R* Scores" brand in `renderHeader()`
  (`assets/app.js:374`) and "All categories" (`assets/app.js:1015`, `assets/graph.js:125`).
- In the e2e tests, change `/index.html?dataset=…` to `/scores.html?dataset=…` (`test_landing.py` → rename it
  `test_scores_page.py`, plus `test_save.py`, `test_graph.py`, `test_scores.py`).

### 3. One set of ids (changed after the user's answers)

The user said saved scores don't matter yet and the old dashboard stays as it is, so the copied dashboard takes the
R* ids (the folder names used everywhere in this repo) instead of a mapping field: `ghcn-d` → `ghcn-daily`,
`gpcp-daily-v3-3` → `gpcp-daily`, `noaa-ncei-persiann-cdr-v1r1` → `persiann-cdr-daily`, `imerg-late-run-v07` →
`imerg-late-run`. That changes `data/datasets.json` (ids and page links), `data/dataset_pages.json`, the
`content/datasets/<id>/` folder names, the `id` in each `overview.json`, and the `id` / `dashboard.id` in
`datasets_metadata/json/*.json`. The dashboard's import scripts read this repo's `datasets_metadata/json/` and
`data-rstar-query-results/` (the same files as the old `my_docs/` copies, plus newer runs) instead of `my_docs/`.

### 4. The "R* scores" link on each card

- In the panel, under "Dataset overview" and "Dataset web research", add **"R* scores"** linking to
  `scores.html?dataset=<rstar_id>` plus the dashboard state with only this card open (the same way `aboutHref()`
  adds it for the other two links, and `writeStateToUrl()` keeps it current). A dataset with no `rstar_id` shows
  "**R* scores:** NA", like the other two.
- GPCP and PERSIANN-CDR are in the R* data but not categorized: the link still goes to their R* page, which already
  says "This dataset has no categorization file yet."
- Optional (question 4): an R* score badge on the card itself, so the score shows without opening the panel.

### 5. Getting back to the dashboard from the R* pages

- `withDataset()` in `assets/app.js` keeps only `dataset`. Change it to also carry `q`, `category`, `coverage` and
  `open`, so they ride along through the category pages and the graph.
- Add "← Back to dashboard" to the R* header (before the brand), linking to
  `index.html?<those params>#dataset-<dashboard_id>`, which opens and scrolls to that card (as the overview and
  research pages already do).
- When the header's dataset picker switches dataset, set `open` to the new dataset's `dashboard_id`, so "Back"
  opens the card of the dataset being looked at.
- Header nav: "Pages" becomes "Dashboard · R* Scores · People risk · … · Score graph", or the dashboard link stays as
  the back link only (question 5).

### 6. Text and links that name the old layout

- The R* page's lede and the page `<title>`s; the dashboard's header ("Precipitation workshop / Dataset archive") and
  footer; the "R* metadata" row on the dashboard (it links the archive and instrument threat pages; keep it).
- `README.md` (top level) and `app/README.md`: the site map, the folder guide and how to run it (the dashboard pages
  need a web server; the R* pages still open from disk).
- `CLAUDE.md` and `HANDOFF.md` (local only).

### 7. Tests

- New `e2e/test_dashboard.py` (Firefox and WebKit, Python Playwright like the others):
  - the page loads 4 cards with no console errors;
  - search and a filter narrow the cards, and the URL keeps them;
  - opening the GHCN-D card shows "R* scores", which opens `scores.html?dataset=ghcn-daily`;
  - "Back to dashboard" there (and from a category page and the graph) returns with the same search, filters and the
    card open;
  - IMERG's panel shows "R* scores: NA";
  - the overview, web research and archive pages load and their back links work.
- Run the whole suite in the Terminal panel (it needs a port):
  `cd /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/app && ../.work/venv/bin/pytest`.
- Check the pages by hand in the built-in browser too, at phone width.

### 8. Publishing

- The Pages workflow already copies all of `app/` (without `e2e/`, `scripts/` and the test files), so `content/` and
  the new `data/*.json` go out with no change.
- The old dashboard site (question 1).

## Decisions (user, 2026-11-24)

- Saved scores can be lost (still testing), so the ids are unified (step 3).
- The old dashboard repo and site stay as they are (a test, shown only briefly). Plain copy, no `git subtree`.
- Use the dashboard's styling for the whole site, but as its own step **after** this move.
- The rest as recommended: the import scripts read this repo's copies of their sources (step 3), an R* badge on the
  cards after steps 1–7, a "Back to dashboard" link only, and keep the "Dataset details" strip.
- Next after this: categorize the other datasets.

## Questions for the user (with my recommendation; answered above)

1. **The old dashboard repo and site.** Recommended: leave it as it is and stop working in it; later, replace its
   `index.html` with a "moved to …" page. Alternatives: keep both going (two copies to keep in step), or delete it.
   Its git history can come along with `git subtree add` instead of a plain copy, if you want that history here.
2. **One look or two.** Recommended for now: each page keeps its own look (dashboard navy, R* pages light/dark), and
   make them match later as its own step. A single look means choosing one stylesheet and redoing the other set of
   pages.
3. **The dashboard's import scripts** read your files in `precip_workshop_dashboard/my_docs/`. Recommended: move
   them with the scripts as a local-only, git-ignored folder here (for example `docs/dashboard_sources/`), or keep
   the scripts pointing at the old folder.
4. **An R* badge on each card** (the score from that browser's choices, NA until every subcategory is scored)?
   That needs the scoring rule (`currentScores()`) moved out of `assets/app.js` into a small shared script. Recommended:
   yes, after steps 1–7 work.
5. **Header links on the R* pages:** a "Back to dashboard" link only (recommended), or "Dashboard" also in the nav.
6. **The "Dataset details" strip on the score page** repeats the card's panel (archive, curator, DOI, period,
   updates). Keep it (recommended: yes, the score page may be opened on its own) or drop it.
