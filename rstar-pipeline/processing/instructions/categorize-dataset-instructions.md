# Instructions for Claude: categorizing a dataset's web research into R* evidence

Written 2026-11-24 from how GHCN-Daily was categorized (four passes, 2026-11-22 to 2026-11-23, commits `965c884`,
`98e4d45`, `56dfffc`, `c56e91e`), then used for GPCP Daily and IMERG Late Run. Updated 2026-11-25 to stand on its own:
everything needed to categorize a dataset is in this doc and the files it names, so `HANDOFF.md` is not needed.
The user's own how-to with prompts is `rstar-pipeline/processing/instructions/categorizing-web-searches_README.md`; this note is the working detail behind
its Prompt 1 (categorize a dataset) and Prompt 5 (add new research).

Paths here are from the repository's top folder. Everything this doc uses is in `rstar-pipeline/` (inputs in
`input/`, these instructions and the scripts in `processing/`, the results in `output/`); `rstar-pipeline/README.md`
shows the layout. The website it feeds is `app/`.

## Background: what R* is and what the output looks like

**The goal.** Score each precipitation dataset on the R* framework to show how at-risk it is. There are four groups
with 19 subcategories in all: People risk (P-1 to P-4), Data risk (D-1 to D-5), Dependent infrastructure resilience
(DIRS-1 to DIRS-5) and Repository resilience (RRS-1 to RRS-5).

1. Web research on each dataset, its repositories and its instruments is in `rstar-pipeline/input/web-research/`.
2. Claude sorts it into the 19 subcategories as evidence (`rstar-pipeline/output/categories/`). That is this doc.
3. Each subcategory gets a score from its evidence (full points, 0 or NA); a person decides the NA ones on the site.
4. The site in `app/` shows the scores, the category pages and a weighted network graph (`app/graph.html`).

**Scoring** (`rstar-pipeline/input/framework/how_to_score_rstar.md`, which both `rstar-pipeline/processing/scripts/categorize/rstar_common.py` and
`rstar-pipeline/processing/scripts/site-data/build_data.py` read):
- R* = 0.40 D + 0.30 P + 0.20 (100 − RRS) + 0.10 DIRS.
- Only high and moderate "for"/"against" items count. "For" only = full points; "against" only = 0; both, or none
  (only context, only low confidence, or no evidence) = NA.
- A category total is NA if any of its subcategories is NA; R* is NA if any category total is NA. So far every
  categorized dataset has R* NA; that is expected.
- P, D and DIRS statements are risks, so their points are risk. RRS statements are good things (resilience), which is
  why RRS enters R* as 100 − RRS.

**Dataset ids** are the same everywhere (folders, file names, metadata, the dashboard): `ghcn-daily`, `gpcp-daily`,
`imerg-late-run`, `persiann-cdr-daily`, and `cocorahs` (new, not yet researched).

**The output JSON** (format in `rstar-pipeline/processing/instructions/create_rstar_node_files.md`; its last section lists the attributes added
2026-11-23). One file per dataset: `rstar-pipeline/output/categories/<id>/<id>_rstar-categories.json`.
- **Top keys:** `people_risk`, `data_risk`, `dep_infra_resilience`, `repo_resilience`, each holding its subcategory
  keys (`P-1` … `RRS-5`), plus `dataset` (producer, `producer_is_repository`, and the repositories with roles).
- **Each subcategory value** is HTML: `<div class="p-1" data-score data-score-basis data-status>` (RRS divs also
  `data-repositories`) containing:
  - `<h4>Evidence</h4><ul class="evidence">`: each `<li>` has `data-confidence` (`high`, `moderate`, `low`),
    `data-source` (the research run folder) and `data-stance` (`for`, `against` or `context`), sorted in that order;
    RRS items also have `data-repository`;
  - then `<h4>Gaps</h4><ul class="gaps">`: each `<li>` has `data-status` (`searched-none-found`, `not-public`,
    `not-searched`).
- **You never write the JSON by hand.** `rstar-pipeline/processing/scripts/categorize/build_<id>.py` holds the hand-sorted evidence and calls
  `write_categories()` in `rstar-pipeline/processing/scripts/categorize/rstar_common.py`, which writes, sorts and scores it.

**Where the research comes from.** Queries and runs live in a separate git repo,
`/Users/claude/SIDE_WORK/NYCE_project/Rstar_query_results` (also on `develop`). Runs save to its `web_search_results/`,
and the user copies finished runs into this project's `rstar-pipeline/input/web-research/`. A copy of the query
templates and their design notes is in `rstar-pipeline/processing/research-queries/` (start with its
`rstar-query-templates-guide.md`); every run folder in `input/web-research/` also holds the exact query it ran.
The query design:
- **Five parts per dataset:** pt1 overview, pt2 QC/calibration/code/formats, pt3 people and funding route (standard
  tier); pt4 threats and news, pt5 threats to inputs (deep tier). Later parts (pt6, pt7, …) are gap runs written from a
  gaps note. Some datasets' part numbers differ from this plan (IMERG's pt3 is formats and people).
- **Repositories:** a shared archive gets an A1 (threats) and an A2 (resilience) run, once, saved in
  `rstar-pipeline/input/web-research/archives/<repository>/`; a producer's own data site gets A2 only (its threats are in the
  dataset's pt4); copies get no run. The register of repositories is in `rstar-pipeline/processing/research-queries/archive-query-plan.md`: keep it current
  when a new dataset names a new host.
- **Runs stop at a token ceiling** (about 80% of it), and each query asks for findings tagged with subcategory codes and
  a supports/contradicts stance.
- **Coverage notes** (`datasets-gap-queries/<id>_coverage-gaps.md`) were written before categorizing, to plan gap runs.
  They are not categorizations. Categorize a dataset once its gap runs are back, then add later runs with Prompt 5.

## Where each dataset stands (update this table when you finish a pass)

As of 2026-11-24:

| Dataset | State | Script and gaps note | Still to come |
|---|---|---|---|
| GHCN-Daily (`ghcn-daily`) | Fourth pass, 2026-11-23: 210 items, 17 of 19 NA, RRS-2 and RRS-3 at 0, R* NA | `build_ghcn-daily.py`, `ghcn-daily_categorization-gaps.md` | All gap runs (pt6–pt9) and the NCEI A2 run are in; what's left is mostly unpublished (by hand or FOIA). The user has yet to review the fourth pass's stance calls (see Precedents) |
| GPCP Daily (`gpcp-daily`) | First pass plus pt7 Run 2, 2026-11-24: 124 items, 11 of 19 NA, R* NA | `build_gpcp-daily.py`, `gpcp-daily_categorization-gaps.md` | The NASA GES DISC + PPS A2 run (fills its GES DISC RRS gaps). Its judgment calls await the user's review |
| IMERG Late Run (`imerg-late-run`) | Second pass, 2026-11-24 (both pt7 runs): 130 items, 11 of 19 NA, R* NA | `build_imerg-late-run.py`, `imerg-late-run_categorization-gaps.md` | The NASA GES DISC + PPS A2 run (written, not run; RRS-2 and RRS-3 empty). The gaps note lists what it should search. What's left for people is mostly not public |
| PERSIANN-CDR Daily (`persiann-cdr-daily`) | Research pt1–pt6 in; not categorized. Its folder in `rstar-pipeline/output/categories/` exists but has no JSON, so the site shows "Not categorized yet" | Coverage note `persiann-cdr-daily_coverage-gaps.md`; gap queries in `persiann-cdr-daily_gap-queries/`; run sheet `supplemental-queries-run-sheet.md` | pt7 (people and production) and the UC Irvine CHRS A2 run, both to rewrite and run. Categorize once they are back |
| CoCoRaHS (`cocorahs`) | Six queries written 2026-11-23 (Parts 1–5 and a data-site A2, in `Rstar_query_results/queries/dataset_queries/about_dataset_queries/cocorahs/` with `cocorahs-run-sheet.md`), none run | — | Needs a `rstar-pipeline/input/dataset-metadata/cocorahs_dataset-metadata.json` first. Part 3's names (Doesken, Reges, Schumacher) came from Claude's knowledge: confirm them from the research |

The best script to copy: `build_gpcp-daily.py` or `build_imerg-late-run.py` for a satellite product,
`build_ghcn-daily.py` for station data.

## 0. Read first (every time)

1. `rstar-pipeline/input/framework/rstar-categorization-decisions.md`: **the filing rules**. It is the master copy and the user
   edits only it (the old Claude Doc copy is no longer updated, and no Word copies are kept). Read it every time; it
   may have changed since this doc was written.
2. The "Counts / doesn't count" table in `rstar-pipeline/processing/instructions/categorizing-web-searches_README.md`: worked examples per subcategory.
3. `rstar-pipeline/input/framework/definitions/*.md`: each subcategory's Description, How to find and What counts as evidence, plus each group's
   scope paragraph.
4. `rstar-pipeline/processing/scripts/categorize/rstar_common.py`: the tuple format and scoring.
5. The dataset's coverage note, if any (`datasets-gap-queries/<id>_coverage-gaps.md`): hosts, versions, runs read, and
   what each gap run was meant to fill.
6. `rstar-pipeline/input/dataset-metadata/<id>_dataset-metadata.json`: versions, DOIs, archives, producer. A new dataset needs this
   file before categorizing, or the site shows its id instead of its name.
7. This doc's "Rules settled and still open" and "Precedents" sections below.

## Rules settled and still open

These came from the user's answers on 2026-11-23 (records in `notes/claude_feedback/first_pass_to_categorize.md`,
`why-rstar-categories-are-hard-to-apply.md` and its `_follow-up.md`; all are applied to the rules doc and the
definitions). The rules doc wins if it says otherwise.

**Settled:**
- **All of `rstar-pipeline/input/web-research/` may be used** (CLAUDE.md), including `archives/` and `instruments/` for RRS and
  DIRS.
- **Repeat shared evidence** in every subcategory it bears on, not "see D-1".
- **DIRS covers only what the dataset needs to be produced:** its networks, calibration, input feeds and processing. The
  repository is not DIRS (repository facts go in D-2, D-3 and RRS). GHCN-Daily's DIRS-4 lost four NCEI-wide items to
  this rule.
- **DIRS-5 also counts substitutes for the dataset itself** (GHCN-Daily's HadISD, Berkeley Earth and ECA&D/C3S/WIS2
  items count).
- **RRS stays pooled** across a dataset's repositories, with each item naming its repository.
- **Inferences** are labelled ("Inference:", "Estimate:") and given low confidence, so they never set a score; keep
  them.
- **"Context"** is the name for the third stance (it was "neutral").

**Still open (the user is taking them to colleagues; don't decide them, but note when a dataset hits one):**
- Whether one station closing, or only a whole network, counts as a lost "source".
- Whether D-2 and D-3 should be scoped away from the repository the way DIRS was.
- Whether the scoring table changes once users see mostly NA.
- Repeating NCEI-wide facts across subcategories, and per-repository RRS.
- Whether there should be a data-quality subcategory (QC and processing evidence has no home now; it is context unless
  it shows a risk).
- Missing evidence reads unevenly: no evidence reads as "no risk" for P, D and DIRS but "no resilience" for RRS.
- **Point values:** `how_to_score_rstar.md` (what the scripts read) gives DIRS-2 25, P-3 25, DIRS-4 15, while the
  decisions doc's table says 20, 20, 20. Ask the user which is right if it matters; don't change either file
  unasked.

## 1. Gather the source runs

- Every `answer_*.md` in `rstar-pipeline/input/web-research/about-datasets/<id>/` (read the whole file, not just the summary).
- The `archives/` runs for each repository that holds the dataset (for NOAA CDRs: both `noaa-ncei` runs, A1 threats
  and A2 resilience). The NCEI A2 run
  (`archives/noaa-ncei/2026-11-23_A2_Rstar_query-noaa_ncei/`) serves GHCN-Daily, GPCP, PERSIANN-CDR and CoCoRaHS's
  copy at NCEI. There is no NASA GES DISC + PPS run yet and no UC Irvine CHRS run: say so in the gaps note.
- The `instruments/` runs for what the dataset is built from: station data → `noaa-rain-gauges`; satellite products →
  `nasa-satellites` and `noaa-satellites` (GPM, DMSP, POES, S-NPP, AMSR2, GOES). Leave out runs that don't apply, and
  say why in the gaps note and the script's docstring (GHCN-Daily left out both satellite runs; IMERG uses the NCEI
  runs only where a source puts an IMERG copy at NCEI).
- Another dataset's runs can hold facts about this one (GPCP used GHCN-Daily pt7/pt9 for NODD facts). Use them, cited
  to that run, when they name this dataset or something on its lists. Once the dataset's own run covers the same
  ground, replace the borrowed items (IMERG's second pass dropped three GPCP-run people items this way).
- **Shared people:** PERSIANN-CDR's people overlap with IMERG's (UC Irvine CHRS makes PDIR-Now, an IMERG input). Note
  any names shared between datasets.
- Note conflicts between runs as you read (two runs disagreeing on a date or a status). Keep both items; the
  subcategory goes NA.
- The first five parts never asked about succession plans, ages or ORCID, calibration, checksums or disaster recovery
  plans; expect those gaps unless a gap run covered them.

## 2. Work out the dataset key first

Before sorting, settle:
- **Producer** (who makes it) and **whether the producer is also the repository** (`producer_is_repository`).
- **Repositories and roles:** archive of record = `parent`; mirrors and copies serving the original format with
  metadata = `child`; the producer's own data site = `producer site`. Volunteer snapshots (Data Rescue Project) and
  third-party reformatted copies (Earth Engine, Zarr stores, ESGF obs4MIPs for GPCP) are **not** repositories: their
  facts are context.
- **Its "team", "source list" and "input list"** as named in the dataset's own documentation. This decides what counts:
  a fact counts as for/against only when a source names the dataset, or something on those lists.
- Which versions are in scope (for GPCP: the 1DD V1.3 CDR and V3.x Daily; for IMERG: V07 Late). If versions differ in
  producer or host, say so in the item text.

## 3. Sort the evidence (the main work)

Copy the structure of an existing script (see the table above) into `rstar-pipeline/processing/scripts/categorize/build_<id>.py`, but write all
evidence fresh from this dataset's runs. Never reuse another dataset's items, even NCEI facts: re-read the runs and word
the item for this dataset.

**Script layout:**
- Docstring: which runs were used and left out, the pass number and date, and the run command.
- Constants for each run folder name (`PT1 = "2026-11-19_gpcp-daily-about-pt1"`): these become `data-source`. Two runs
  with the same part number (GPCP's and IMERG's two pt7 runs, GHCN-Daily's two pt3 runs) each get their own constant.
- Constants for often-cited URLs.
- One list per subcategory (`P1 = [...]`) and its gaps (`P1_GAPS = [...]`), grouped by category with a comment rule.
- `SUBCATEGORIES` dict for all 19 ids, a `DATASET` dict, then `write_categories("<id>", SUBCATEGORIES, DATASET)`.

**Each evidence item** is `(confidence, run, text, stance)`, and RRS items add a fifth field, the repository name
(matching a `DATASET` repository name, or "AWS, Google BigQuery" style when it covers several). Confidence is `"H"`,
`"M"` or `"L"`; stance is `"F"`, `"A"` or `"C"`.

- **Text:** one to three sentences in plain English, specific (numbers, dates, names), with the source as a markdown
  link `[label](url)` taken from the answer file. Quote short phrases from official pages when the wording matters
  ("cannot be shared outside the US Government"). Say when something is from a search result only or was not read.
  If the fact is about a wider body (NCEI, NASA), say whether any source names this dataset. The site doesn't show run
  names to readers (only `data-source` keeps them), so the text must make sense without them.
- **Confidence:** `H` official documentation or primary record, read; `M` reliable secondary source, or a primary
  source the run flagged as partly read / indirect; `L` search-result-only, single weak source, or **any inference
  of mine** (label it "Inference:" or "Estimate:" in the text). The run's own confidence labels are a good guide.
- **Stance** toward the subcategory's statement:
  - P, D and DIRS statements are risks: `F` = evidence the risk is present, `A` = evidence it isn't.
  - RRS statements are good things: `F` = evidence of resilience, `A` = evidence against it.
  - `C` = context: not tied to the dataset or its source/input list/team (one step removed), a rejected proposal, an
    event before 2025 in D-1 or RRS-4, or a fact that doesn't show the statement true or false.
- **Scoring is automatic** (only H/M for/against count; for only = full points, against only = 0, otherwise NA).
  So the stance and confidence calls are the score. Be deliberate: one moderate "against" item turns a "for" score NA.
- **Repeat a fact in every subcategory it bears on** (no "see D-1"). Typical repeats: a repository budget in D-1,
  D-3 and RRS-4; a repository storage fact in D-2 and RRS-1; a lost source in DIRS-2 and DIRS-5.
- **Within a list, put items in reading order** (by run); the writer sorts them for, against, context.
- **Leave out** text that fits no subcategory (version histories with no risk bearing, grid details). QC methods are
  context unless they show a risk (P-3/P-4 if only one person can run it; DIRS-4 if it runs on outside systems).

**Per-subcategory reminders (from GHCN-Daily):**
- P-1: a found succession plan or handover documentation is "against"; a targeted search that found no plan is "for".
- P-2: age estimates (earliest publication year minus 25–30, FERS rules: MRA 56–57 + 30 years, 60 + 20, 62 + 5) are
  always low; a named person's departure is context for P-2 (they can't retire again) but counts in P-1/P-4.
  Agency-wide retirements with no tie to the dataset's team are context.
- P-3: published code or a full algorithm paper is "against"; code not published is "for".
- P-4: one named person doing a step with no backup is "for"; a team or automation statement for this dataset is
  "against".
- D-1: pending cuts count like enacted ones; rejected proposals and pre-2025 budgets are context.
- D-4: open formats (NetCDF, CSV, text) with standard readers are "against"; reformatted third-party copies are context.
- D-5: needs a source naming the dataset (or the program); general politics is context.
- DIRS-2/3: any source or input that stops counts as "for", whatever its share.
- DIRS-5: a backup for a dependency or a substitute dataset is "against"; "no substitute" is "for".
- RRS-1: each copy sits in one region / both copies in one city is "against"; two independent sites is "for".
- RRS-2/3: checksums only at ingest/order, or a plan that "cannot be shared", give "against" or a "not public" gap.
- RRS-5: pre-2025 events count here.

**Gaps:** `(status, text)` with `S` searched and none found, `P` not public (exists but withheld, or personnel
records), `U` not searched. Keep each gap one line; the full list with possible searches goes in the gaps note.
A withheld fact is both a found context item and a `P` gap.

## 4. Build and check

```bash
python3 rstar-pipeline/processing/scripts/categorize/build_<id>.py      # writes rstar-pipeline/output/categories/<id>/<id>_rstar-categories.json
python3 rstar-pipeline/processing/scripts/site-data/build_data.py             # rebuilds app/data/rstar-data.js
```

- Both are plain Python scripts and run fine in the Bash tool.
- `build_data.py` reads the definitions, the point values and weights, the dataset metadata and every categorization
  JSON, and writes `app/data/rstar-data.js`. Re-run it after changing any of those. The pages load it with a
  `<script>` tag. The server runs no build, so the rebuilt `rstar-data.js` must be committed with the change.
- The script prints each subcategory's counts and score. Look over the scores: is any score set by one item you are
  unsure of? Note it for the user.
- Keep one JSON file in the dataset folder (the site loads only the first). A dataset shows on the site once it has a
  folder in `rstar-pipeline/output/categories/`; until that folder has a JSON file, its card says "Not categorized yet".
- **A new dataset's dashboard card** comes from the `dashboard` block of its metadata file, not from
  `app/data/datasets.json` (which is generated). After adding or editing the metadata file, run
  `python3 rstar-pipeline/processing/scripts/dashboard/import_dataset_overviews.py` and then
  `python3 rstar-pipeline/processing/scripts/dashboard/build_datasets.py`, and commit the changed `app/` files.
- **Check the pages in a browser.** Serve `app/` (`cd app && python3 -m http.server 3000 --bind 127.0.0.1`, run in the
  Terminal panel, since the Bash sandbox can't open ports). The built-in browser can't load a page's CSS and JS from
  disk, so always serve it; on the owner's computer the local-only `.claude/launch.json` defines `rstar-viewer`
  (port 8765) and `rstar-viewer-2` (port 8766, for when another chat holds 8765) for `preview_start`. Open:
  - `index.html` (the dashboard landing page): the dataset's card should have an "R* scores →" link and no
    "Not categorized yet";
  - `scores.html?dataset=<id>`, each category page (`people-risk.html?dataset=<id>` and the others), and
    `graph.html?dataset=<id>` (try its "Show evidence nodes" switch);
  - the console, for errors.
- **Cached files:** `http.server` lets the browser reuse old JS and CSS. After a rebuild, hard-refresh (Cmd+Shift+R),
  or in the built-in browser run `fetch(<file href>, {cache: 'reload'})` and reload. Screenshots taken right after a
  redraw can catch a 0.15 s fade and look washed out; zoom in or check computed styles instead.
- **The e2e tests** (Python Playwright, Firefox and WebKit only, in `.work/venv`, versions pinned in
  `app/requirements-dev.txt`) run in the Terminal panel, not in Bash (pip can't reach PyPI and servers can't bind in
  the sandbox):
  `cd /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/app && ../.work/venv/bin/pytest`.
  - If the venv's Python is gone, rebuild it with the command in `app/README.md` (it uses `/opt/homebrew/bin/python3`).
  - Don't remove the DYLD fix in `app/e2e/conftest.py`: `~/.zshrc` sets `DYLD_LIBRARY_PATH`, which crashes
    Playwright's Firefox.
  - Avoid `all_text_contents()` in new tests: it crashes these pages in Playwright's Firefox.
  - If a test depends on a dataset's data that changed, fix the test, not the data.

## 5. Write the gaps note

`rstar-pipeline/output/gaps-notes/<id>_categorization-gaps.md`, following `gpcp-daily_categorization-gaps.md` or
`imerg-late-run_categorization-gaps.md`:
- header bullets: dataset, date and pass, output file, script, research used, research left out and why (including
  repository runs not yet run);
- the repositories (the JSON's `dataset` key) and their roles;
- a scores table (subcategory, for / against / context counts, score, why);
- **judgment calls to double-check**;
- per subcategory: what was not searched, and possible searches;
- conflicts between runs, and things to check by hand (no new web search);
- evidence counts.
If a coverage note exists (`<id>_coverage-gaps.md`), say in it that the categorization is done and point to the
gaps note; don't delete it.

The gaps notes in `rstar-pipeline/output/gaps-notes/` are committed (the repo is public). Writing gap queries from
them (Prompts 2–4 of the user's how-to) happens in `datasets-gap-queries/`, outside the pipeline: its coverage notes
are committed, while its `*_gap-queries/` folders, the run sheets and `Rstar Precipitation Queries.md` are git-ignored
and stay on disk only.

## 6. Report to the user

- The scores per subcategory, each category total and R*.
- **The judgment calls to double-check:** items whose stance or confidence alone sets or blocks a score, items moved
  to context under the "one step removed" rule, repository roles, and conflicts between runs.
- Names or facts that came from me and not the research.
- The server command, in its own `bash` block:
  `cd /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/app && python3 -m http.server 3000 --bind 127.0.0.1`,
  then http://127.0.0.1:3000/.
- Update this doc's "Where each dataset stands" table, the top-level `README.md` dataset table (it is for visitors),
  and `HANDOFF.md` (CLAUDE.md asks for it at the end of every session; this doc doesn't depend on it).
- **Committing:** work on `develop`, and commit only when the user asks. One commit for the change (script, JSON,
  rebuilt `rstar-data.js`, gaps note, test changes, README), with the Co-Authored-By line at the end of the message.
  Query files belong to the `Rstar_query_results` repo and are committed there, in their own commit. The user
  publishes by merging `develop` into `main` and pushing; Claude doesn't push.

## Adding new research later (Prompt 5)

Add the new run constants, add items from the new answer files, and **remove items the new research makes wrong or
out of date** (and placeholders that only said "not searched"). Rewrite the Gaps lists to what is still open. Add a
"Changes from the <n>th pass" section to the gaps note with the counts added and dropped. Bump the pass number in the
script's docstring.

What the earlier second passes dropped, as a guide: items borrowed from another dataset's run once the dataset's own
run covered them, a low-confidence inference the new research made unnecessary, and an item whose dates turned out
wrong (IMERG, 2026-11-24: 28 added, 5 dropped, 107 → 130 items). Corrections to a fact go in place (GPCP's RSS SSMIS
CDR end date became 2025-07-31). Say in the report which scores changed (IMERG's P-1 and P-4 went from 0 to NA).

## Precedents (judgment calls made so far)

Follow these for consistency unless the rules doc changes them. The user has not reviewed all of them yet.

- **GHCN-Daily, fourth pass:** 15 items became context, including P-2's NCEI-wide retirements (so P-2 is NA), D-1's
  rejected FY2026 request, five D-5 items with no GHCN-Daily tie, and the Data Rescue Project snapshot. P-2's
  retirement estimates and RRS-1's single-region items were flagged for review.
- **GPCP Daily:** satellites inside an input product (IMERG's microwave constellation, GPM as IMERG's calibrator) count
  as "for" in DIRS at moderate confidence, since GPCP's own documents list them. A repository that serves only an old
  version or a stale copy goes in RRS-1 as "against" (copies not current). ESGF obs4MIPs is filed as not a repository.
- **IMERG Late Run:** ATMOS (a NASA contract the run inferred pays the algorithm staff) filed as a low "against"
  in D-1, since the link is an inference; P-4's "no deputy named" as a moderate
  "for"; PDIR-Now being computed at PPS as a DIRS-4 "against".

## Pitfalls seen

- **The "not categorized yet" tests use a faked dataset (since 2026-11-25).** They used to point at a real
  uncategorized dataset and broke each time one was categorized (GPCP Daily, 2026-11-24: 6 tests × 2 browsers). Now the
  `uncategorized` fixture in `app/e2e/conftest.py` serves `rstar-data.js` with GPCP Daily's categorization taken out
  (`UNCATEGORIZED = "gpcp-daily"`), and the five tests that need an uncategorized dataset take that fixture
  (in `test_dashboard.py`, `test_category.py`, `test_scores.py`, `test_scores_page.py` and `test_graph.py`).
  Categorizing a dataset, PERSIANN-CDR included, no longer breaks them. Other tests still name real datasets
  (`grep -n '<id>' app/e2e/*.py`), so check them when a dataset's data changes. The "R* scores: NA" card branch (a
  dataset with no R* entry at all) has no test.
- **Point values:** `rstar_common.py` reads `rstar-pipeline/input/framework/how_to_score_rstar.md`, not the decisions doc's table; the
  two disagree (see "Still open").
- Answer files cross-link to `../<run>/answer.md`, which doesn't exist here (the files are `answer_<query>.md`).
- A run's answer may say "Run 2" when only one run was made (IMERG's first pt7): check which questions it actually
  covered, and list the rest as not searched.
- The `guard_bash` hook blocks any Bash command whose text contains `cat.key`; use the Edit tool (or a Python edit
  script written with the Write tool) for `app.js`/`graph.js`.
- Auto mode sometimes refuses a call sent in the same message as another; send it again on its own.
- Use `trash`, never `rm`. Working files (venv, logs, debug scripts) go in `.work/`, which is git-ignored.
- `rstar-pipeline/input/web-research/about-datasets/query_questions.txt` is the user's untracked file; leave it alone.
