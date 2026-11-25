# Dataset overview pages

`app/overview.html?id=<dataset id>` shows one dataset's metadata (built
2026-11-21). Each dashboard panel links to it as "Dataset overview", just
above "Dataset web research" (NA when the dataset has no `overview_url`).

## Where the data comes from

- Master copies: `rstar-pipeline/input/dataset-metadata/<id>_dataset-metadata.json`
  (moved in from the workshop dashboard's `my_docs/`, now archived outside
  the project), made from the ChatGPT answers in its `markdown/` folder.
  Field list: the `README.md` in that folder. The user also uses these
  files in another project.
- `python3 rstar-pipeline/processing/scripts/dashboard/import_dataset_overviews.py` (run from the project folder)
  copies every one to `app/content/datasets/<id>/overview.json`, without
  the working-only keys `source`, `dashboard` and `review_notes`.
- `python3 rstar-pipeline/processing/scripts/dashboard/build_datasets.py` then rebuilds the card list
  (`app/data/datasets.json`) from each file's `dashboard` block and sets
  `overview_url` on every card whose `overview.json` exists (since
  2026-11-25; before, the overview script set it and compared the block
  with `datasets.json` by hand).

## Adding or changing a dataset's overview

1. Edit or add the master JSON file (same keys as the others; a new
   dataset's `dashboard` block is its card).
2. Run `import_dataset_overviews.py`, then `build_datasets.py` (it also
   sorts the cards).
3. Hard-reload the page (Cmd+Shift+R): browsers keep `styles.css`.

## How the page is built (`app/overview.js`)

- Sections, each an `<h2>` with an id (`#summary`, `#people`, `#time`,
  `#space`, `#instruments`, `#data-format`, `#versions`, `#archives`,
  `#access`, `#related`, `#references`), with an "On this page" list at
  the top. Empty fields and empty sections are left out.
- Label/value facts are `.facts-table` tables (row headers); lists of
  items (leads, instruments, versions, archives, endpoints) are normal
  tables with only the columns some item fills.
- Unknown text/number fields in an object are still shown, labeled from
  the key ("land_ocean" → "Land ocean"), so new metadata appears without a
  code change. New arrays or objects need code.
- Dates "YYYY-MM-DD" / "YYYY-MM" / "present" are written out
  ("1 January 1983", "January 1998", "Present").
- Access endpoints are split into "Get the data" (primary / alternative)
  and "Documentation" (role `documentation`); outside links open in a new
  tab and say so to screen readers.
- Back to dashboard and the web research link keep the search, filters
  and open cards, like the other pages.
