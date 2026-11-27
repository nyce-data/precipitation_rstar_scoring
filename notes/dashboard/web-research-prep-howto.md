# Preparing new research runs for the web research pages

Written 2026-11-27. This note covers getting finished query runs from the `Rstar_query_results` project into
`rstar-pipeline/input/web-research/`, ready to become the pages linked from each dataset card's
"Dataset web research" link (`app/dataset.html?id=<id>`, and `&part=<N>` for one part).

Each part page shows a **Question** and a **Searched on** list, followed by the answer. The question text comes from
the run folder's `query_questions.txt`. This note gets every run folder to the point where that file is complete
and reads well. `notes/dashboard/dataset-about-pages-howto.md` then takes over: it covers the page list, the import
script, the card link and the browser check.

## The steps

1. Find the runs that haven't been copied yet.
2. Copy their files into `web-research/`.
3. Give each run folder a `query_questions.txt`.
4. Fill each blank `query_questions.txt` from the run's `research-record.json`.
5. Reword every line into a question, and remove references to other parts or runs.
6. Check the files.
7. Check the folders against the import script's rules, then follow the dataset pages how-to.

Never overwrite or delete anything in `web-research/`; copy only what is missing. The user edits files there by
hand (answers, question files), so a file that differs from its `query_answers` copy is usually the newer one.

## Where things are

| What | Path |
|---|---|
| Finished copies of each run (the source) | `/Users/claude/SIDE_WORK/NYCE_project/Rstar_query_results/query_answers/` |
| The raw run folders | `/Users/claude/SIDE_WORK/NYCE_project/Rstar_query_results/web_search_results/<date>_<name>/` |
| A second query-results folder for parallel runs | `/Users/claude/SIDE_WORK/NYCE_project/Rstar_query_results_pt2/` (merge it into `Rstar_query_results` first; see that project's HANDOFF.md) |
| The destination | `rstar-pipeline/input/web-research/` (`about-datasets/<id>/`, `archives/<repository>/`, `instruments/<family>/`) |
| The blank template | `rstar-pipeline/input/web-research/about-datasets/query_questions.txt` (keep it blank) |
| The page list and import script | `app/data/dataset_pages.json`, `rstar-pipeline/processing/scripts/dashboard/import_dataset_pages.py` |

### How `query_answers` folders map to `web-research` folders

Each run is a dated folder (`<date>_<name>`) and keeps its name. The folder above it can be named differently:

| `query_answers/…` | `web-research/…` |
|---|---|
| `dataset_answers/about_dataset_queries/<id>/` | `about-datasets/<id>/`, except `uscrn/` → `uscrn-daily/` (use the dataset id from its metadata file) |
| `archive_answers/noaa-ncei-archive/` | `archives/noaa-ncei/` |
| `archive_answers/gesdisc-pps/` | `archives/nasa-gesdisc-pps/` |
| `archive_answers/<other>/` (`cocorahs`, `uci-chrs`) | `archives/<same name>/` |
| `instrument_answers/A4_Rstar_query/<run>/` | `instruments/<family>/<run>/`: `nasa-satellite-precip-threats` → `nasa-satellites`, `noaa-rain-gauge-threats` → `noaa-rain-gauges`, `noaa-satellite-precip-threats` → `noaa-satellites` |
| PERSIANN's `2026-11-19_persiann-cdr-daily-satellites` | `2026-11-19_persiann-cdr-daily-satellites-pt6` (renamed so it ends in `-pt6`) |

For a new dataset or repository, ask the user for the folder name if the dataset id or the existing pattern doesn't
settle it.

## 1. Find the runs not yet copied

- List the run folders in `query_answers/` and, using the table above, check which don't exist in `web-research/`.
  Then compare file by file inside the run folders that do exist (a run copied earlier may be missing a file).
- Check `Rstar_query_results/web_search_results/README.md` (the run index) and its `HANDOFF.md` for finished runs
  that have **no `query_answers` copy yet**. Each copy in `query_answers` holds three files:
  - the query file (from `queries/…`, for example `uscrn-daily-about_Rstar_query_pt1.md`),
  - the answer, renamed `answer_<query file name>.md`,
  - `research-record.json`.

  Ask the user before making missing copies there. They are committed in that project.
- Leave out `work/`, `check-by-hand.md`, `sites-to-trust.md`, `method.md` and `results.csv`; the input folder doesn't
  keep them.

## 2. Copy the files

- Copy only files that don't exist at the destination (`cp -n`, or check first). Create the run folder if needed.
- If a file exists at both ends with **different content**, leave the `web-research/` one and list it for the user.
  So far these differences are deliberate: on copying, lines pointing to `check-by-hand.md` and
  `sites-to-trust.md` were taken out.
- If a `query_answers` file has the same content as a differently named file at the destination, skip it. (PERSIANN
  pt2's `answer.md` was the same file as `answer_persiann-cdr-daily-about_Rstar_query_pt2.md`.) A plain
  `answer.md` should be renamed `answer_<query file name>.md` in `query_answers` too.
- **One query file, several runs:** a query file can hold more than one run (GPCP's and IMERG's
  `…-gaps_Rstar_query_pt7_people-production.md` each hold Run 1 and Run 2). Each run has its own output folder,
  named for that run (`…-people-production-pt7` is Run 1, `…-calibration-copies-pt7` is Run 2). Inside each folder,
  the query copy and its answer get `_run<N>` before `.md`, for example
  `imerg-late-run-gaps_Rstar_query_pt7_people-production_run1.md` and
  `answer_imerg-late-run-gaps_Rstar_query_pt7_people-production_run1.md`. Use the same names in `query_answers` and
  `web-research`. Don't rename the run folders: categorization evidence, run records and the run index cite them.
- Compare with `cmp` or `diff -rq` afterwards.

## 3. Add `query_questions.txt` to each run folder

Every run folder under `about-datasets/*/`, `archives/*/` and `instruments/*/` gets one. Copy the blank template
into each run folder that has none. Don't replace an existing one, even a blank one.

## 4. Fill blank files from `research-record.json`

A file is blank when it has nothing but the `<Question>` and `<Searched on>` lines. For each blank file:

- under `<Question>`: the record's `"question"`;
- under `<Searched on>`: each `"question"` inside the record's `"subquestions"` list, in order.

The layout, with one blank line between entries:

```
<Question>

The main question?

<Searched on>

First searched-on question?

Second searched-on question?
```

Check that every record has a non-empty `question` and that every subquestion has one before writing. Stop and
report any that don't. If a file the user filled has fewer searched-on lines than its record has subquestions, ask
whether the rest were left out on purpose. The NOAA rain-gauge file had 1 of 7; the other 6 were added on
2026-11-27.

## 5. Reword the lines

The records are written as search notes, not as questions for a reader. GPCP's files (pt1 to pt6) are the model.
The rules:

- **Every line becomes a full question ending in "?"**, the main question and each searched-on line alike. Notes
  like "Hosts: every place that holds or serves a copy; archive of record; export documentation; DOI/version" become "Which places hold or
  serve a copy of the data, which is the archive of record, and is there a DOI or version?". Instructions like
  "rate each development and map it to D-1, D-3…" become "…how does each development rate, and how does it map to
  D-1, D-3…?".
- **Keep the meaning and every detail:** names, dates, versions, award numbers, URLs and criterion codes (RRS-1,
  D-2, DIRS-3, P-4…). Put criterion codes in brackets at the end of a searched-on question when the record has them
  as tags: "…and how is it paid for (D-3)?". Don't add facts that aren't in the record.
- **Remove references to other parts or runs**, because each page stands on its own. Examples taken out so far:
  - "(Part 1 overview)", "(Part 2)", "(Part 7, building on runs pt1-pt6)"
  - "Using the earlier runs' records (*_cocorahs-about-pt1 and *_cocorahs-qc-formats-pt2), …"
  - "(adding to earlier runs)", "that earlier runs did not check", "not already covered"
  - "(Adds to runs 2026-11-19_ghcn-daily-about-pt1, …)", "Builds on Part 1 (2026-11-26_uscrn-daily-about-pt1) …"
  - "beyond what the GHCN-Daily resilience run (pt9) found"
- **Keep scope notes that don't point at another run**, for example "QC and file formats out of scope" or "leaving
  out cuts, staff losses and news from 2025 on".
- Keep one searched-on line per subquestion. A very long one can become two or three short questions in the same
  paragraph (see IMERG `calibration-copies-pt7`).
- Fix plain typos ("satelite").
- Rewording applies to every file, including ones the user filled; it is the user's own file format, and the user
  asked for this on 2026-11-27.

Write the rewording into the `web-research/` files only. The `research-record.json` files stay as they are.

## 6. Check the files

From `rstar-pipeline/input/web-research/`, both of these should print nothing:

```bash
for f in */*/*/query_questions.txt; do awk 'NF && $0!~/^<(Question|Searched on)>$/ && $0!~/\?[[:space:]]*$/ {print FILENAME": "$0}' "$f"; done
```

```bash
grep -n -E "[Pp]art [0-9]|earlier run|-pt[0-9]|\(pt[0-9]|Builds on|Adds to|adding to" */*/*/query_questions.txt
```

Also check that each file's searched-on count matches its record's `subquestions`, unless the user chose otherwise.

## 7. Get the folders ready for the import script

`import_dataset_pages.py` reads `about-datasets/<research_folder>/` and, for each part in `app/data/dataset_pages.json`:

- needs exactly **one** folder ending in `-pt<N>` (the date in front doesn't matter; it stops on zero or two),
  unless the part names its run folder with `"folder"` (used when one query file held two runs; Run 2 becomes the
  next part number);
- needs exactly **one** `answer*.md` in it;
- reads `query_questions.txt` for the Question and Searched on text (lines under each heading, blank lines skipped).

Run this check (read-only) to list problems:

```bash
cd rstar-pipeline/input/web-research && python3 -I - <<'EOF'
import os, re, glob, collections
for ds in sorted(os.listdir('about-datasets')):
    p = f'about-datasets/{ds}'
    if not os.path.isdir(p): continue
    parts = collections.defaultdict(list)
    for d in sorted(os.listdir(p)):
        if not os.path.isdir(f'{p}/{d}'): continue
        m = re.search(r'-pt(\d+)$', d)
        n = len(glob.glob(f'{p}/{d}/answer*.md'))
        if not m: print(ds, d, 'has no -pt<N> ending')
        if n != 1: print(ds, d, f'has {n} answer*.md')
        if not os.path.exists(f'{p}/{d}/query_questions.txt'): print(ds, d, 'has no query_questions.txt')
        if m: parts[int(m.group(1))].append(d)
    for n, v in sorted(parts.items()):
        if len(v) > 1: print(ds, f'pt{n} has {len(v)} folders:', v)
    print(ds, 'parts:', sorted(parts))
EOF
```

Don't rename research folders to fix these without asking: the folder names match the run names in
`Rstar_query_results`.

Then follow `notes/dashboard/dataset-about-pages-howto.md`, "Adding research", from step 3:

- add the parts and their topics to `dataset_pages.json` (ask the user for new topic names);
- run `import_dataset_pages.py`, then `build_datasets.py`;
- read the `check:` lines;
- check the pages in the browser.

A **new dataset** also needs a card first: a `<id>_dataset-metadata.json` with a `dashboard` block in
`rstar-pipeline/input/dataset-metadata/`, which `build_datasets.py` turns into the card.

Archive and instrument runs don't go through `import_dataset_pages.py`. Archive pages use `import_archive_page.py
--record`, which takes the question and searched-on text straight from `research-record.json`, not from
`query_questions.txt`. So the reworded questions show on those pages only if the script is changed to read
`query_questions.txt` (ask the user).

## State on 2026-11-27 (open questions for the user)

Steps 1 to 6 are done for every run copied so far: all 50 run folders have a reworded `query_questions.txt`. Before
the next pages can be built:

- **Two pt7 folders** each in GPCP and IMERG: `people-production-pt7` (Run 1) and `calibration-copies-pt7` (Run 2) of
  one query file. Their files were renamed `_run1`/`_run2` on 2026-11-27 in both projects. The import script now
  takes a `"folder"` per part (2026-11-27), and the user chose to show Run 2 as **part 8**. So list them as
  `{ "part": 7, "topic": …, "folder": "2026-11-24_<id>-people-production-pt7" }` and
  `{ "part": 8, "topic": …, "folder": "2026-11-24_<id>-calibration-copies-pt7" }`. Topics (user, 2026-11-27):
  "People and production" (part 7) and "Calibration and copies" (part 8).
- **All four dashboard datasets were re-imported on 2026-11-27** with every part: GHCN-Daily 1–9, GPCP 1–8, IMERG
  1–8 (its first pages; its card now links to them) and PERSIANN-CDR 1–6. All 31 pages were checked in the browser.
  GHCN-Daily pt1 and pt2 keep the user's earlier question wording (restored from the committed pages into their
  `query_questions.txt`).
- The import also drops bullets that start with a link to `check-by-hand.md` or `sites-to-trust.md` (added to
  `DROP_ITEM_PREFIXES` on 2026-11-27 for GPCP pt7; CoCoRaHS pt2's answer has the same bullets).
- **GHCN-Daily pt3:** `2026-11-19_ghcn-daily-about-pt3_combined` was one query that the user later split into
  three runs (`funding-pt3`, `threats-news-pt4`, `sources-pt5`). Since 2026-11-27 the site's pt3 is `funding-pt3`
  ("Funding"); the combined run has no page, because its folder doesn't end in `-pt3`. **Keep the combined
  folder:** GHCN-Daily's categorization cites it as evidence (`build_ghcn-daily.py`,
  `ghcn-daily_rstar-categories.json`, the gaps note, `app/data/rstar-data.js`).
- **USCRN Daily, CoCoRaHS and ASOS** have metadata Markdown only, no metadata JSON, so no card yet.
- **ASOS** has runs in `Rstar_query_results/web_search_results/` (Parts 1–5 and a Part 4 follow-up) but no
  `query_answers` copies, so nothing of ASOS is in `web-research/` yet.
- **Not committed:** the copies and question files made on 2026-11-27 in `web-research/`.
