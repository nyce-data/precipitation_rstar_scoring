# Plan: gather everything that makes the app's data into one folder, `rstar-pipeline/`

Written 2026-11-25. Status: proposed, waiting for the user's go-ahead.

## Goal

Put everything needed to recreate the R* data that the site shows in one folder, laid out as input → processing →
output, with a README that a person or another Claude can follow, so the same steps can be reused for another project.
The website stays in `app/`. `datasets-gap-queries/` stays where it is (a one-off process). `docs/` keeps only
`ideas/`.

## New layout

```
rstar-pipeline/
  README.md                         the structure, and the processing steps in order
  input/
    framework/                      what R* is and how it is scored
      definitions/                  ← rstar_definitions/*.md
      how_to_score_rstar.md         ← docs/scoring/
      rstar-categorization-decisions.md  ← docs/claude_feedback/ (the filing rules, master copy)
      assessment-form/example_rstar_json.json  ← docs/json_output/ (the colleague's form format)
    dataset-metadata/               ← datasets_metadata/json/*.json
    web-research/                   ← data-rstar-query-results/ (about-datasets/, archives/, instruments/)
  processing/
    instructions/
      categorize-dataset-instructions.md   ← notes/ (Claude's step-by-step; now committed from here)
      categorizing-web-searches_README.md  ← docs/ (the user's prompts)
      create_rstar_node_files.md           ← docs/ (the category JSON format)
      rstar-query-templates-guide.md       ← docs/ (how the research queries are designed)
    scripts/
      categorize/                   ← scripts/categorize/ (build_<id>.py, rstar_common.py)
      site-data/build_data.py       ← app/scripts/build_data.py
      dashboard/                    ← scripts/dashboard/ (import scripts for the dashboard pages)
  output/
    categories/<id>/<id>_rstar-categories.json  ← data-rstar-categories/datasets/
    gaps-notes/<id>_categorization-gaps.md       ← datasets-gap-queries/*_categorization-gaps.md (decision 1)
```

Other moves:
- `docs/json_output/examples_from_app/` (a file saved by the site) → `app/schema/examples/`.
- Local-only discussion records in `docs/claude_feedback/` → `notes/claude_feedback/`; `docs/example_starting_queries/`
  → `notes/old/` (both stay git-ignored).
- What stays: `app/` (site; reads only its own `app/data/` and `app/content/`), `datasets-gap-queries/` (coverage
  notes, gap queries, run sheets), `docs/ideas/`, `notes/` (Claude's plans), `.work/`.
- The site still needs its own copies of generated data: `build_data.py` keeps writing `app/data/rstar-data.js`, and
  the dashboard scripts keep writing `app/data/` and `app/content/`. The README says so.

## Path updates (what would break)

- **Code:** `rstar_common.py` (scoring doc, output folder), `build_data.py` (ROOT, definitions, scoring, metadata,
  categories, form example, output to `app/data/`), the dashboard scripts (relative paths to research, metadata,
  `app/data`), the three `build_<id>.py` docstrings.
- **Site text:** the six R* pages' "Data built by …" notice, `app.js` / `graph.js` / dashboard JS comments,
  `.github/workflows/pages.yml` comment.
- **Docs:** root `README.md` (folder guide), `app/README.md`, the four instruction docs, the gaps notes, CLAUDE.md
  ("File locations"), HANDOFF.md, `.gitignore`.
- **Not edited:** research answer files (they are records); the category JSON is regenerated, not edited.

## Steps

1. `git mv` every tracked file (keeps history); plain `mv` for ignored ones.
2. Update paths in code, then docs (one sed pass per old path, checked by hand).
3. Write `rstar-pipeline/README.md`.
4. Verify: re-run the three categorize scripts and `build_data.py`; the category JSON must come out byte-identical and
   `rstar-data.js` differ only in the `file` paths. `grep` for every old path. e2e tests in the Terminal panel; open the
   site in the preview.
5. One commit on `develop`.

## Decisions for the user

1. Move the four `*_categorization-gaps.md` notes into `output/gaps-notes/` (they are step 5 of the instructions), or
   leave them in `datasets-gap-queries/`? Recommended: move them.
2. Copy the research query templates (pt1–pt5, A1, A2, A4) from the separate `Rstar_query_results` repo into
   `rstar-pipeline/processing/research-queries/`, so another project has them? They would be a second copy.
3. Folder name: `rstar-pipeline/` (alternatives: `pipeline/`, `rstar-workflow/`).

## Later (phase 2, not now): the workshop dashboard's processing

**Done 2026-11-25** (as `notes/dashboard-files-move-plan.md`, which replaced what follows): the metadata Markdown and
template are in `input/dataset-metadata/`, the workshop's other files are archived by the user outside the project, and
`app/data/datasets.json` is built by `processing/scripts/dashboard/build_datasets.py` from the metadata files'
`dashboard` blocks.

From `/Users/claude/SIDE_WORK/NYCE_project/precip_workshop_dashboard`:
- Its scripts are already here (`scripts/dashboard/` → `processing/scripts/dashboard/`).
- Its source files are the user's local-only `my_docs/about_data/`: the workshop CSV, `master_climate_inventory_subset.json`,
  the `datasets_json/` subsets, the 47-dataset backup, `Data archives by dataset.md`, the metadata Markdown and
  `new_dataset-metadata_template.md`. These would go in `input/dashboard/` (and the template and Markdown beside
  `input/dataset-metadata/`). Decide which are committed (the repo is public).
- Don't bring its `rstar_query_results/` copy or its metadata JSON: both are older than this project's copies (the
  JSON still has the old ids).
- `app/data/datasets.json` is hand-edited source data that lives in the app; decide then whether its master copy moves
  to `input/`.
