# Plan: bring the workshop dashboard's files into this project

Written 2026-11-25 with the user and revised the same day (second version: no big master list). Follows phase 2 of
`notes/rstar-pipeline-reorganization-plan.md`. **Steps 1–3 done 2026-11-25** (in the new `precipitation_rstar_scoring`
repo, which is private, so the "Hosting" and "Later" notes below about a public repo and `local-notes` are out of
date). `build_datasets.py`'s output was byte-identical to the old `datasets.json`. Step 4's e2e test run and commit are
the user's.

**Goal:** the dashboard and the R* scoring live in one place. Everything needed to rebuild the dashboard's cards is in
`rstar-pipeline/` (input → processing → output), and `app/` only holds what scripts write.

**From:** `/Users/claude/SIDE_WORK/NYCE_project/precip_workshop_dashboard`, its local-only `my_docs/` and `.work/`.

## Decided (user, 2026-11-25)

- **The old dashboard project stays as it is.** Its GitHub repo is now private and its app won't be shared. Claude
  only copies from it.
- **No big master list.** The 47-dataset `datasets.json`, the workshop CSV, the inventory JSON and the rest of the
  workshop list are archived by the user in a folder outside this project. The user brings a file back when its
  information is needed. This project starts from the JSON format it already has, and will hold about 15 datasets for
  a long while.
- **The card list's master is the dataset metadata JSON.** Each `rstar-pipeline/input/dataset-metadata/<id>_dataset-metadata.json`
  already has a `dashboard` block holding that dataset's card. Checked 2026-11-25: all 4 blocks equal their entries in
  `app/data/datasets.json`, apart from `overview_url`, which a script sets. So a new script builds
  `app/data/datasets.json` from those blocks, and one file per dataset is the only place to edit a card.
  - This replaces the earlier answers to questions 1 and 2: no master means no CoCoRaHS rename in it (CoCoRaHS gets
    the id `cocorahs` when its metadata file is made), and the `dashboard` block is now the master, not a copy to check.
  - Every metadata file is a card on the site (no `show_on_site` field). Add one later if a dataset should be kept off.
- **`dataset_pages.json`, `archives.json` and `archive_links.json` stay in `app/data/`** for this move.
- **Hosting:** this repo stays public for now and its GitHub Pages site is the one shared. Later the user pushes it to
  a second GitHub account as a private repo, deploys it to a DigitalOcean droplet, then makes the copy on the user's
  own account private. Both GitHub copies are kept. No GitHub Pro, so Pages stops for any private copy and the
  droplet serves the site. The user will say when the repo is private.
- **The JSON files are the user's to use** (the user was given them).

## Step 1: copy the few files this project needs

| From (`precip_workshop_dashboard/`) | To |
|---|---|
| `my_docs/about_data/dataset_metadata/markdown/*.md` (4 files: the ChatGPT answers the metadata JSON was made from) | `rstar-pipeline/input/dataset-metadata/markdown/` |
| `my_docs/about_data/dataset_metadata/new_dataset-metadata_template.md` (for the next datasets) | `rstar-pipeline/input/dataset-metadata/` |
| `my_docs/about_data/dataset_metadata/json/README.md` (the metadata JSON's keys) | `rstar-pipeline/input/dataset-metadata/README.md` (fix its `../markdown/` paths; say the `dashboard` block is now the card's master) |
| `my_docs/about_data/remove_sentence_patterns_from_pages.md` (clean-up rules for the research pages) | `rstar-pipeline/processing/instructions/` |

All four are committed (they are about public datasets, and the metadata JSON made from them is already public).
**Copied 2026-11-25 and checked with `cmp`** (not yet committed). Still to do: fix the README's `../markdown/` paths
and its `dashboard` block wording. The user archived `my_docs/` and `.work/` outside the sandbox the same day.

Everything else stays with the user's archive (see "Files for the user's archive").

## Step 2: a script writes `app/data/datasets.json`

New `rstar-pipeline/processing/scripts/dashboard/build_datasets.py`:
- reads the `dashboard` block of every `rstar-pipeline/input/dataset-metadata/*_dataset-metadata.json`;
- sets `about_url` to `dataset.html?id=<id>` for datasets listed in `app/data/dataset_pages.json`, else `""` (IMERG
  has `""` today);
- sets `overview_url` to `overview.html?id=<id>` when the dataset's overview page exists (use the rule
  `import_dataset_overviews.py` uses now);
- sorts the cards with the logic now in `sort_datasets.py` (move it in; trash `sort_datasets.py`);
- writes `app/data/datasets.json` with 2-space indents.

**Check: the new `app/data/datasets.json` is byte-identical to today's.** If not, find why before going on.

Then change the other two scripts so nothing else writes `app/data/datasets.json`:
- `import_dataset_pages.py`: stop setting `about_url`; print "now run build_datasets.py".
- `import_dataset_overviews.py`: stop setting `overview_url` and drop its "dashboard block differs" check (the block is
  now the source); print "now run build_datasets.py".

## Step 3: update the docs

- `rstar-pipeline/README.md`: add the metadata Markdown and template to the layout; add `build_datasets.py` to the
  steps ("edit the card in the dataset's metadata JSON, then run it"); drop "Still to bring in" (say instead that the
  workshop's full list is archived outside the project); drop the `sort_datasets.py` line.
- `rstar-pipeline/processing/instructions/categorizing-web-searches_README.md` and
  `categorize-dataset-instructions.md`: where adding a dataset to the website mentions the card list, point at the
  metadata file's `dashboard` block and `build_datasets.py`.
- `app/README.md` (its "Data" line) and the top-level `README.md` folder guide.
- `notes/dashboard/*.md`: replace `my_docs/...` and old-project paths; say the workshop source files are archived
  outside the project; the design notes' "Data file" section says the cards come from the metadata JSON.
- `CLAUDE.md` "File locations" (if anything changes there), `HANDOFF.md`, and
  `notes/rstar-pipeline-reorganization-plan.md` (phase 2 done).

## Step 4: check and commit

- Rebuild: `python3 rstar-pipeline/processing/scripts/dashboard/build_datasets.py`; `git diff app/data/` shows nothing.
- Look at the dashboard in the preview (cards, filters, panels, R* links).
- The user runs the e2e tests in the Terminal panel:
  `cd /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/app && ../.work/venv/bin/pytest`
- One commit on `develop` when the user asks. Then snapshot the local notes.

## Files for the user's archive (outside this project)

From `precip_workshop_dashboard/`. None is in its git repo, so the archive is their only copy. Simplest: copy the
whole `my_docs/` and `.work/` folders. What they hold:

| File | What it is |
|---|---|
| `my_docs/data_backup_all_datasets/datasets.json` | The 47-dataset card list (old ids such as `ghcn-d`; no IMERG Late Run) |
| `my_docs/about_data/precipitation_workshop_datasets.csv` | The workshop's first list (41 datasets) |
| `my_docs/about_data/master_climate_inventory_subset.json` | The given inventory: source of `curator`, `doi`, `notes` |
| `my_docs/about_data/Data archives by dataset.md` | Source of the cards' access links |
| `my_docs/about_data/datasets_json/` | Older subsets of the card list |
| `my_docs/about_data/IMERG_dataset_overview.md` | Notes on IMERG |
| `my_docs/about_data/rstar_query_results/`, `my_docs/about_data/dataset_metadata/json/` | Older copies of research and metadata (this project has newer) |
| `my_docs/html_css_design/` | Design mock and screenshots |
| `.work/build_json.py`, `.work/merge_inventory.py`, `.work/sort_datasets.py`, `.work/removed/` | The one-time scripts that built the 47-dataset list |

The four files in Step 1 can also stay in the archive (they will be in this project too).

## Later, separately: the private copies and the droplet

- Anything committed while this repo is public stays public in its history.
- The `.gitignore` rules for `CLAUDE.md`, `HANDOFF.md`, `notes/` and the gap queries stay; tracking them in the
  private copies is a separate decision (it would replace the `local-notes` snapshot step).
- **Never push `local-notes`** to any remote, the new account included.
- The Pages workflow won't publish from a private repo on GitHub Free. The droplet needs a web server with HTTPS and
  a way to deploy new commits. Questions for the user are in HANDOFF.md ("Hosting").
