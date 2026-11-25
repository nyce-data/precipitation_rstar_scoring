# Dataset overview pages

`app/overview.html?id=<dataset id>` shows one dataset's metadata (built
2026-11-21). Each dashboard panel links to it as "Dataset overview", just
above "Dataset web research" (NA when the dataset has no `overview_url`).

## Where the data comes from

- Master copies (the user's, not in git):
  `my_docs/about_data/dataset_metadata/json/<name>_dataset-metadata.json`,
  made from ChatGPT answers in `../markdown/`. Field list: the `README.md`
  in that folder. The user also uses these files in another project.
- `python3 scripts/import_dataset_overviews.py` (run from the project
  folder) copies each one whose `id` is in `app/data/datasets.json` to
  `app/content/datasets/<id>/overview.json`, without the working-only keys
  `source`, `dashboard` and `review_notes`, and sets `overview_url` on
  that dataset. It then lists any field where a file's `dashboard` block
  differs from `datasets.json` (`about_url` / `overview_url` are not
  compared), so the two can be kept in step by hand.

## Adding or changing a dataset's overview

1. Edit or add the master JSON file (same keys as the others).
2. If it's a new dataset, add its `dashboard` block to `datasets.json`
   and re-sort (`python3 .work/sort_datasets.py`).
3. Run the import script; fix any differences it lists.
4. Hard-reload the page (Cmd+Shift+R): browsers keep `styles.css`.

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
