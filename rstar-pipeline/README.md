# R* pipeline: from web research to the website's data

This folder holds everything needed to recreate the data that the R* Scores website (`../app/`) shows, laid out as
**input → processing → output**. It is written so that a person, or a new Claude Code session, can repeat the process
for more datasets or for another project. Paths below are from the repository's top folder.

```
rstar-pipeline/
├── input/                      what the process starts from
│   ├── framework/              what R* is and how it is scored (the same for every dataset)
│   │   ├── definitions/        the four groups and 19 subcategories: description, how to find, what counts as evidence
│   │   ├── how_to_score_rstar.md            point values, group weights and the scoring rule (the scripts read it)
│   │   ├── rstar-categorization-decisions.md  the filing rules for sorting evidence (master copy)
│   │   └── assessment-form/    the R* form's JSON format (the site's "Save your scores" file follows it)
│   ├── dataset-metadata/       one JSON file per dataset: names, versions, DOIs, producer, repositories, and its
│   │   │                       dashboard card (the `dashboard` block); README.md lists the keys
│   │   ├── markdown/           the ChatGPT answers the JSON files were made from
│   │   └── new_dataset-metadata_template.md  the question to ask for a new dataset's metadata
│   └── web-research/           the research runs, one folder per run (query, answer_*.md, research record)
│       ├── about-datasets/<id>/  runs about each dataset
│       ├── archives/<repository>/  runs about the repositories that hold them
│       └── instruments/<family>/   runs about the instruments and satellites they are built from
├── processing/                 how the input becomes the output
│   ├── instructions/           the steps, for people and for Claude
│   │   ├── categorizing-web-searches_README.md  the user's how-to: the cycle and a prompt for each step
│   │   ├── categorize-dataset-instructions.md   Claude's detailed steps (stands on its own)
│   │   └── create_rstar_node_files.md           the category JSON format
│   ├── research-queries/       how the web research is asked for
│   │   ├── rstar-query-templates-guide.md       start here: the query design and how to adapt it
│   │   ├── dataset-query-5-part-plan.md, archive-query-plan.md  the design notes (with the repository register)
│   │   ├── templates/          dataset/ (pt1–pt5), archive/ (A1, A2), instrument/ (A4)
│   │   └── examples/           filled-in queries (CoCoRaHS, and A2 queries for four repositories)
│   └── scripts/
│       ├── categorize/         build_<id>.py per dataset (the hand-sorted evidence) and rstar_common.py
│       ├── site-data/build_data.py  builds app/data/rstar-data.js
│       └── dashboard/          build the dashboard's card list, and copy research and metadata into its pages
└── output/                     what the process makes
    ├── categories/<id>/<id>_rstar-categories.json  each dataset's evidence, gaps and scores
    └── gaps-notes/<id>_categorization-gaps.md       what each dataset's research never searched, and judgment calls
```

**What is outside this folder.** `app/` is the website; it reads only its own `app/data/` and `app/content/`, which
the scripts here write (the server publishes `app/` alone, so those generated files are committed).
`datasets-gap-queries/` holds the one-off work of turning gaps notes into follow-up queries (coverage notes, gap query
drafts, run sheets). The research itself is run in a separate project, `Rstar_query_results`, and its finished run
folders are copied into `input/web-research/`.

## The steps

Dataset ids are the same everywhere (folder names, file names, metadata, the site): `ghcn-daily`, `gpcp-daily`,
`imerg-late-run`, `persiann-cdr-daily`.

### 1. Set up the framework (once per project)

`input/framework/` defines R*. For another kind of data, check the definitions and the filing rules first, and change
a subcategory's "How to find" text before the query templates, which follow from it. The scripts read point values
and weights from `how_to_score_rstar.md`, so change them only there.

### 2. Describe each dataset

Add `input/dataset-metadata/<id>_dataset-metadata.json` (copy an existing one; `new_dataset-metadata_template.md` is
the question that gathers the facts). The R* pages show the dataset's name from it; without it they show the id. Its
`dashboard` block is the dataset's card on the landing page: every metadata file is a card, and the block is the only
place to edit one (step 6 builds the card list from it).

### 3. Research each dataset

Follow `processing/research-queries/rstar-query-templates-guide.md`:
1. Copy the five dataset templates (`templates/dataset/`) for the dataset and fill in the placeholders; write A1 and
   A2 queries for a new shared archive, or A2 for a producer's own data site (`templates/archive/`); an instrument
   family gets an A4 query (`templates/instrument/`).
2. Rewrite them with the `/my:rewrite-research-query` skill and run each with `/my:broad-web-research`, one session
   per run.
3. Copy each finished run folder into `input/web-research/about-datasets/<id>/` (named
   `<date>_<id>-<topic>-pt<N>`), `archives/<repository>/` or `instruments/<family>/`.

### 4. Categorize each dataset

Follow `processing/instructions/categorize-dataset-instructions.md` (Prompt 1 in
`categorizing-web-searches_README.md`). In short: read every answer file that bears on the dataset, sort each finding
into the 19 subcategories as an evidence item with a confidence, a stance and its source, list the gaps, and keep it
all in `processing/scripts/categorize/build_<id>.py` (copy an existing script). Then run it:

```bash
python3 rstar-pipeline/processing/scripts/categorize/build_<id>.py
```

It writes `output/categories/<id>/<id>_rstar-categories.json` and works out each subcategory's score from the
evidence. Then write the dataset's gaps note in `output/gaps-notes/`.

### 5. Fill the gaps (repeat while worthwhile)

Turn the gaps note into new queries (Prompts 2–4 of `categorizing-web-searches_README.md`, worked in
`datasets-gap-queries/`), run them as in step 3, and add the new evidence to the dataset's script (Prompt 5). Re-run
the script.

### 6. Build the website's data

```bash
python3 rstar-pipeline/processing/scripts/site-data/build_data.py
```

It reads the framework, the metadata and every category JSON, and writes `app/data/rstar-data.js`. A dataset appears
on the site once it has a folder in `output/categories/` ("Not categorized yet" until that folder has a JSON file).

The dashboard pages (the landing page's cards, each dataset's overview and web research pages, and the archive pages)
are filled by the scripts in `processing/scripts/dashboard/`, run from the repository's top folder:
- `import_dataset_overviews.py`: dataset metadata → `app/content/datasets/<id>/overview.json`;
- `import_dataset_pages.py`: the research runs listed in `app/data/dataset_pages.json` →
  `app/content/datasets/<id>/pt<N>.md`;
- `import_archive_page.py`: one archive or instrument run → a page in `app/content/` (see its docstring);
- `build_datasets.py`, run last: the card list, `app/data/datasets.json`. It copies every metadata file's `dashboard`
  block, adds the links to the dataset's web research pages (when `dataset_pages.json` lists it) and overview page
  (when its `overview.json` exists), and sorts the cards by data source, coverage and name.

To change a card, edit the `dashboard` block in the dataset's metadata file and run `build_datasets.py`; don't edit
`app/data/datasets.json`. The page lists (`dataset_pages.json`, `archives.json`, `archive_links.json`) are edited by
hand in `app/data/`.

```bash
python3 rstar-pipeline/processing/scripts/dashboard/import_dataset_overviews.py
python3 rstar-pipeline/processing/scripts/dashboard/build_datasets.py
```

The web research pages on the site were made from older copies of the runs, and `import_dataset_pages.py` no longer
runs cleanly on today's folders (for example GHCN-Daily's pt1 run has no `query_questions.txt`); update
`dataset_pages.json` and the script for the newer runs before re-running it.

### 7. Check and publish

Serve the site (`cd app && python3 -m http.server 3000 --bind 127.0.0.1`, then http://127.0.0.1:3000/), look at the
dataset's pages, and run the end-to-end tests (`app/README.md` has the setup). Commit the script, the output, the
rebuilt `app/data/rstar-data.js` and the gaps note together. Publishing is described in `app/README.md`.

## Rebuild everything from the inputs

```bash
for f in rstar-pipeline/processing/scripts/categorize/build_*.py; do python3 "$f"; done
python3 rstar-pipeline/processing/scripts/site-data/build_data.py
```

Both are plain Python 3 with no packages to install. The category JSON comes out the same each time from the same
scripts, so a diff after a rebuild shows only real changes.

## Reusing this for another project

1. Copy this folder and `app/`.
2. Empty `input/dataset-metadata/`, `input/web-research/`, `output/` and `processing/scripts/categorize/` except
   `rstar_common.py` (keep one `build_<id>.py` as a model).
3. Adapt `input/framework/` and the query templates to the new kind of data (step 1, and the guide's "Adapting to other
   climate data").
4. Work through steps 2–7 for each dataset.

## The workshop's full dataset list

The workshop dashboard's own source files (its 47-dataset card list, the workshop CSV, the inventory JSON and the
one-off scripts that built them) are archived by the user outside this project and brought back only when needed. The
dashboard's metadata notes and scripts were moved in (`input/dataset-metadata/`, `processing/scripts/dashboard/`).
