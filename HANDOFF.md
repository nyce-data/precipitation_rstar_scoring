# Handoff

Notes for the next session: what the project is for, where things stand, and what to do next.
Last updated 2026-11-27. Update this file before compacting a session and at the end of every session
(see CLAUDE.md).

## Status at a glance (2026-11-27, thirteenth session)

**Repo:** `develop` is at `a3f6141` ("Categorize PERSIANN-CDR Daily (first pass)") plus this HANDOFF update;
`main` and `origin/main` are still at `ea8bb0a`, so the PERSIANN work is **not merged or pushed** (command in
"Publishing"). In `Rstar_query_results`, `develop` has the ASOS `query_answers` copies (`cc94615`), not pushed.

**On the website now:** the dashboard has cards for seven datasets. Every card has an overview page and its web
research pages; four datasets are categorized (R* scores).

| Dataset | Web research pages | R* categorization |
|---|---|---|
| GHCN-Daily | 9 parts | Fourth pass (2026-11-23): 210 items, 17 of 19 NA |
| GPCP Daily | 8 parts | Second pass (2026-11-27): 134 items, 11 of 19 NA |
| IMERG Late Run | 8 parts | Third pass (2026-11-27): 149 items, 10 of 19 NA |
| PERSIANN-CDR | 6 parts | First pass (2026-11-27, before its pt7 people run): 100 items, 9 of 19 NA |
| CoCoRaHS | 5 parts | Not categorized yet |
| USCRN Daily | 5 parts | Not categorized yet |
| ASOS | 5 parts | Not categorized yet |

R* is NA for all four categorized datasets (expected: any NA subcategory makes R* NA). All 152 e2e tests pass
(Firefox and WebKit, 2026-11-27).

**All research runs are copied into `rstar-pipeline/input/web-research/`:** every dataset's Parts, plus the repository
runs for NOAA NCEI (A1, A2), NASA GES DISC + PPS (A2), UC Irvine CHRS (A2) and CoCoRaHS's data site (A2). The only
query still to run is PERSIANN-CDR's pt7 (people and production); the user has not run it yet.

## Next session (start here)

Open sessions in `/Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring`, not the old
`Rstar_precipitation-relationships`. Read `rstar-pipeline/processing/instructions/categorize-dataset-instructions.md`
before any categorizing; the user's prompts are in `categorizing-web-searches_README.md` (Prompt 1 categorizes a
dataset, Prompt 5 adds new research).

**Next steps, in order:**

0. **Publish the PERSIANN commit if wanted:** the user merges `develop` into `main` and pushes (see "Publishing").
1. **PERSIANN-CDR Daily's pt7 run, then its second pass.** Categorized 2026-11-27 (first pass, 100 items, 9 of 19 NA)
   **before** its pt7 people-and-production query was run (the user's choice). Steps:
   - The user rewrites the draft with `/my:rewrite-research-query` (prompt in
     `datasets-gap-queries/supplemental-queries-run-sheet.md`; the draft is
     `datasets-gap-queries/persiann-cdr-daily_gap-queries/persiann-cdr-daily-gaps_Rstar_query_pt7_people-production.md`,
     with a copy in `Rstar_query_results/queries/dataset_queries/about_dataset_queries/persiann-cdr-daily/`), then runs
     it with `/my:broad-web-research` in `Rstar_query_results` (or `Rstar_query_results_pt2`).
   - Copy the run into `rstar-pipeline/input/web-research/about-datasets/persiann-cdr-daily/` following
     `notes/dashboard/web-research-prep-howto.md` (question file, then the page import if it gets a web research page).
   - Add it with Prompt 5 to `rstar-pipeline/processing/scripts/categorize/build_persiann-cdr-daily.py`: it should
     fill P-1, P-2 and P-4 (people, ages, who runs the quarterly extension), D-1 (who pays for production), DIRS-1
     (recalibrated GridSat-B1 from 2024), DIRS-3 (GPCP version), DIRS-4 (CHRS's computers), DIRS-5 (substitute
     datasets) and RRS-1 (whether the cloud copies are current). Replace the "U" (not searched, pt7) gaps, and add a
     "Changes from the first pass" section to `rstar-pipeline/output/gaps-notes/persiann-cdr-daily_categorization-gaps.md`.
   - Note names shared with IMERG (Braithwaite, Hsu, Nguyen, Sorooshian are IMERG ATBD co-authors).
2. **Categorize the three new station datasets** with Prompt 1, copying `build_ghcn-daily.py` (station data):
   - **CoCoRaHS** (`cocorahs`): Parts 1–5 and its data-site A2 (`archives/cocorahs/`). Its copy at NCEI is inside
     GHCN-Daily, so the NCEI A2 run applies to that copy.
   - **USCRN Daily** (`uscrn-daily`): Parts 1–5; NCEI-hosted, so both `archives/noaa-ncei` runs apply.
   - **ASOS** (`asos`): Parts 1–5 and the Part 4 follow-up (`2026-11-26_asos-1min-gap-followup`, answer only: cite it
     as a source; it has no page). Scored as the network as a whole (user's choice). NCEI-hosted (both NCEI runs);
     IEM is an independent outside archive (Part 1): decide its repository role when categorizing (it reprocesses
     the 1-minute data, so it may not count as serving the original format).
   - Each has an empty `rstar-pipeline/output/categories/<id>/` (`.gitkeep`). After writing its JSON, re-run
     `build_data.py`; check `app/e2e/test_dashboard.py`, whose new-dataset test expects "Not categorized yet" on
     these three cards (change it to the "R* scores" link for each one categorized).
   - Station datasets also use `instruments/noaa-rain-gauges` (COOP, ASOS, USCRN and CoCoRaHS are all in it).
3. **Things for the user to check** (no new searches needed):
   - **Metadata facts flagged in `review_notes`:** CoCoRaHS (Nolan Doesken's death on 15 November 2026, from Part 4;
     Russ Schumacher as a current lead); USCRN Daily (DOI 10.7289/V5H13007 and record C00546; station counts);
     ASOS (leads Boutin and Day from Part 3, low confidence they are still in post; an undated snippet names
     Christine Smith (Schultz) as ASOS Program Manager).
   - **Judgment calls in the gaps notes:** GHCN-Daily's fourth-pass stance calls and GPCP's list are still unreviewed.
     IMERG's third-pass RRS-1 to RRS-3 calls were reviewed and kept (2026-11-27).
   - **PERSIANN-CDR's first-pass calls** (gaps note, "Judgment calls to double-check"): P-1 = 0 rests on the 2014
     handover package alone (Braithwaite's absence is low "for"; at moderate P-1 becomes NA); P-4 NA because
     "every production step is algorithmic" was filed as context; P-3's two "for" items (QC procedure "not
     documented", documents naming GPCP v2.2); D-3 counting NCEI's undated "pause in operations" notice;
     `producer_is_repository` false (CHRS serves a copy, NCEI is the archive of record).
4. **The DigitalOcean droplet:** the user is setting it up in another folder and session and will say how. Then plan
   this site's deployment there under the workshop password (see "Hosting"). Saved scores collected on the droplet:
   later, not yet.
5. **Smaller site items, when wanted:**
   - **Archive pages** for the newer repository runs: only `noaa-ncei` has one (`app/content/archives/`); GES DISC/PPS,
     UCI CHRS and CoCoRaHS's data site have none (`import_archive_page.py --record`).
   - **Cross-run links:** some pages link `../<run>/answer.md` (ASOS pt4's follow-up link, older ones in GHCN-Daily and
     IMERG), which don't resolve on the site; the importer could drop or rewrite them.
   - **An R* score badge on each card** and filling blank archive websites in `data/archive_links.json` (see "The
     dashboard").
   - Score graph and knowledge graph ideas: "Next steps" items 6–7 below.

**At the end of the session** (CLAUDE.md): update this file, then commit on `develop` when the user asks. The user
merges into `main` and pushes (command in "Publishing").

## This repo (started fresh 2026-11-25)

- **What it is:** `precipitation_rstar_scoring` is a copy of `Rstar_precipitation-relationships` (its `develop` at
  `0a8a054`, plus its local-only files and the dashboard files copied in that day), with a **new git history**.
- **Two private GitHub copies:** the agency's https://github.com/nyce-data/precipitation_rstar_scoring (the agency
  owns the code and sees everything; the user is a collaborator) and the user's own
  https://github.com/lmerchant/precipitation_rstar_scoring (stays private; not a public website). `origin` fetches
  from the user's and has both as push URLs, so `git push origin main` updates both.
- **The old folder stays as it is:** `/Users/claude/SIDE_WORK/NYCE_project/Rstar_precipitation-relationships` and its public repo
  `lmerchant/Rstar_precipitation-relationships` (with its GitHub Pages site,
  https://lmerchant.github.io/Rstar_precipitation-relationships/) stay public for the user's colleagues. Don't change
  anything there, and don't trash anything in it. Its git history and `local-notes` branch are kept in that folder.
- **What changed in the copy:** the old folder's path and name were replaced with this one's (CLAUDE.md, the docs, the
  query templates and examples, the gap-query run sheet; the originals in `Rstar_query_results/queries/` were updated
  the same way, with their old `notes/` and pre-reorganization paths fixed, so the copies still match them); `.github/workflows/pages.yml` was removed (Pages can't publish from a private repo on GitHub
  Free); `CLAUDE.md`, `HANDOFF.md` (checked 2026-11-25: nothing personal in it), `notes/`, `.claude/launch.json` and
  the gap queries are now committed; `docs/ideas/` stays git-ignored (the user's notes for Claude to read; the user
  removes it when finished); the `local-notes` branch and its snapshot script are not used here; `.work/` was not
  copied (the venv was rebuilt here, see "Tests").
- **Setup (done 2026-11-25):** the user made the repo (`main` with an empty "Initial commit", then `develop`), set the
  repo's commit email to the GitHub noreply address, rebuilt the venv (all e2e tests pass here), checked the site and
  created both GitHub repos. The first commit, `b87f55c` "Start precipitation_rstar_scoring from
  Rstar_precipitation-relationships" (308 files), is on `develop` and `main` and was pushed to both. Both commits carry
  the noreply address. (An earlier "Initial commit" with a placeholder email was amended and force-pushed away.)

## Goal

Score precipitation datasets on the R* framework and show how risky each one is. There are four groups:
People risk (P), Data risk (D), Dependent infrastructure resilience (DIRS) and Repository resilience (RRS),
with 19 subcategories in all.

1. Web research on each dataset, its repositories and its instruments is saved in `rstar-pipeline/input/web-research/`.
2. That research is sorted into the 19 subcategories as evidence (`rstar-pipeline/output/categories/`).
3. Each subcategory gets a score from its evidence (full points, 0 or NA); a person decides the NA ones.
4. The final app in `app/` shows a weighted network graph and/or knowledge graph of R* scores and dataset
   relationships. Ideas are in `docs/ideas/rstar_relationship_graph/rstar_graphs.md` and `docs/ideas/R Precip dashboard.md` (the user's notes, kept out of git); the scoring formula and point values are in
   `rstar-pipeline/input/framework/how_to_score_rstar.md` (which `rstar-pipeline/processing/scripts/site-data/build_data.py` reads):
   - R* = 0.40 D + 0.30 P + 0.20 (100 − RRS) + 0.10 DIRS;
   - each subcategory is worth 0 or a fixed number of points, or NA when the evidence doesn't settle it (then the
     category total and R* are NA too, and a person decides).

The weighted network graph of a dataset's R* scores is built (`app/graph.html`, 2026-11-24) and the user likes it;
the knowledge graph of dataset relationships is not started. GHCN-Daily, GPCP Daily and IMERG Late Run are categorized;
PERSIANN-CDR Daily is categorized (first pass, 2026-11-27) before its pt7 people run. CoCoRaHS, USCRN Daily and ASOS are new datasets whose research
runs are done and copied in but which are not categorized; all three have dashboard cards and web research pages (CoCoRaHS and USCRN Daily in `744041f`, ASOS 2026-11-27).

**Thirteenth session (2026-11-27): PERSIANN-CDR Daily categorized (first pass).** The user chose to categorize now
rather than wait for pt7 (the user asked whether pt7 had been run: it hadn't; no PERSIANN pt7 run exists in either
`Rstar_query_results` folder). New `build_persiann-cdr-daily.py` (100 items from pt1–pt6, both NCEI runs, the UCI CHRS
A2 run, the NOAA satellite run, NODD/NCEI facts from GHCN-Daily pt7/pt9 and one low inference from GPCP's pt7 Run 2),
gaps note, rebuilt `rstar-data.js`, a PERSIANN check added to `test_dashboard.py`, the instructions' state table and
precedents, the README table and the coverage note's pointer. `producer_is_repository` is false (CHRS serves a copy,
but NCEI is the archive of record; true made the site say they are one organization). Pages checked in the built-in
browser; all 152 e2e tests pass (Firefox and WebKit). Committed on `develop` as `a3f6141`; not merged or pushed.

**Twelfth session (2026-11-27): ASOS on the dashboard; NASA repository run categorized.** All merged and pushed
(`main` = `ea8bb0a`).
- **Point values settled** (`a573e08`): the user confirmed `how_to_score_rstar.md`'s P-3 25, DIRS-2 25, DIRS-4 15;
  the decisions doc's table (which said 20, 20, 20) now matches. No score changed (the site already used them).
- **ASOS** (`6df50b0`): `query_answers` copies made and committed in `Rstar_query_results` (`cc94615`); runs copied to
  `about-datasets/asos/` with reworded question files; metadata JSON (ISD links fixed from Part 1, GHCNh added, DSI
  6405/6406; `review_notes` list every change); card, overview and Parts 1–5 (same topics as CoCoRaHS and USCRN).
- **Page cleaner fix** (same commit): `import_archive_page.py`'s `_FILE_SENTENCE` lets a period inside backticks pass,
  which fixed a cut sentence on ASOS pt4 and "md\` lists …" fragments on GHCN-Daily pt3 and USCRN Daily pt5.
- **NASA GES DISC + PPS A2 run categorized** (`ea8bb0a`): IMERG third pass (130 → 149 items; RRS-1 0 → NA, RRS-2 and
  RRS-3 NA → 0; the user kept these calls) and GPCP second pass (124 → 134; no score change). The rules used (transfer-
  only checksums and a not-found DR plan are "against"; two separate holders are an RRS-1 "for") are in the
  categorizing instructions' precedents.
- **e2e:** seven cards; ASOS's overview and five parts are opened; 152 pass.

**Eleventh session (2026-11-27): research copied in; every web research part on the dashboard.**
- **`Rstar_query_results`:** merged pt2's `uscrn-runs` (USCRN Daily Parts 1–5) into its `develop`, keeping both sets
  of rows in its run index and HANDOFF.md, and copied the USCRN `work/` folders across. Committed the `query_answers`
  copies of USCRN Daily, GES DISC/PPS and UCI CHRS. Renamed GPCP's and IMERG's pt7 copies `_run1`/`_run2`, so each run
  of a two-run query is named for its run. `Rstar_query_results_pt2` is **kept for more parallel runs**; that project's
  HANDOFF.md says how to refresh and merge it.
- **Copied into `rstar-pipeline/input/web-research/`:**
  - `about-datasets/uscrn-daily/` (Parts 1–5);
  - `archives/nasa-gesdisc-pps/` and `archives/uci-chrs/`.

  Only missing files were copied. 7 files differ from their `query_answers` copies on purpose: they were cleaned when
  copied. These are PERSIANN pt1 and pt3–6, NCEI A1 and the rain-gauge A4.
- **Question files:**
  - Every run folder (50) now has a `query_questions.txt`.
  - Blank ones were filled from `research-record.json` (`question`, then each `subquestions[].question`), and all
    were reworded into questions with references to other parts or runs removed (GPCP's style).
  - GHCN-Daily pt1 and pt2 keep the user's earlier wording.
  - The rain-gauge file gained the 6 searched-on questions it was missing.
- **Importer:**
  - `import_dataset_pages.py` takes an optional `"folder"` per part. Run 2 of a two-run query is shown as the next
    part, so GPCP's and IMERG's `calibration-copies-pt7` are part 8 (the user's choice).
  - `import_archive_page.py`'s cleaner keeps a bullet's `**Label:**` when it removes a research-file sentence. It drops
    bullets that start with `` `check-by-hand.md` ``, `` `sites-to-trust.md` `` or a link to either, and bullets about
    "your allowed domains".
- **Pages:** `app/data/dataset_pages.json` now lists GHCN-Daily 1–9, GPCP 1–8, IMERG 1–8 (its first pages; its card now
  links to them) and PERSIANN-CDR 1–6. All re-imported and checked in the browser (31 pages). The new topic names
  (Threats and news, Repository, Infrastructure, Repository resilience, Processing and quality control, Formats and
  people) are Claude's, from the folder names, and can be renamed. GHCN-Daily's `about-pt3_combined` run was split
  by the user into pt3–pt5, so it has no page. Keep its folder: the categorization cites it.
- **Process note:** `notes/dashboard/web-research-prep-howto.md` covers copying new runs in through to the import,
  with the folder-name map and the checks. `notes/dashboard/dataset-about-pages-howto.md` covers the import itself.
- **Tests:** 140 e2e tests pass (Claude ran them in the Terminal panel). Committed on `develop` as `c5f42de`; the
  user pushed.

**Tenth session (2026-11-25): queries for three new datasets.** The user added metadata Markdown for ASOS (`asos`),
USCRN Daily (`uscrn-daily`) and CoCoRaHS (`cocorahs`) in `rstar-pipeline/input/dataset-metadata/markdown/` (committed
at the end of the session; no JSON yet). Wrote five draft queries and a run sheet each for ASOS (`Rstar_query_results/queries/dataset_queries/about_dataset_queries/asos/`) and
USCRN Daily (`Rstar_query_results/queries/dataset_queries/about_dataset_queries/uscrn-daily/`), from the templates, with what earlier runs already found (rain-gauge run,
GHCN-Daily pt5 and pt8). **ASOS is scored as the network as a whole** (user's choice): Part 1 lists its 1-minute,
5-minute, hourly (GHCNh; ISD ended Aug 29, 2025, so the metadata file's ISD links may be stale) and daily products.
Both are NCEI-hosted, so no new repository runs: five sessions each. USCRN's Part 3 names beyond Howard Diamond
(Palecki, Leeper, Baker) are from Claude's knowledge, to confirm. **CoCoRaHS's existing drafts were refreshed** (user's
choice) from its new metadata file: data.cocorahs.org export portal and CSV route, 2019 QA/QC document, METplus page;
its already-rewritten A2 query gained data.cocorahs.org in its host list. The CoCoRaHS copies in
`rstar-pipeline/processing/research-queries/examples/` were synced. The repository register in `archive-query-plan.md`
now lists ASOS, USCRN Daily and IEM (a copy), and marks NCEI's A2 as done. Committed on `develop`: queries in
`Rstar_query_results` as `ea7ebfc` (its IMERG pt7 answer copies separately), this repo's notes as `b259d93`, then the
metadata Markdown and this update. Not merged into `main` or pushed.

**Ninth session (2026-11-25): the card-list script.** New
`rstar-pipeline/processing/scripts/dashboard/build_datasets.py` builds `app/data/datasets.json` from each
`rstar-pipeline/input/dataset-metadata/*_dataset-metadata.json`'s `dashboard` block (the only place to edit a card), sets
`about_url` (from `app/data/dataset_pages.json`) and `overview_url` (when `app/content/datasets/<id>/overview.json`
exists) and sorts the cards (the rules from `sort_datasets.py`, now trashed). Its output was byte-identical to the old
file. `import_dataset_overviews.py` now writes an overview for every metadata file and no longer touches
`datasets.json`; `import_dataset_pages.py` no longer sets `about_url`; both print "Now run build_datasets.py". Docs
updated (metadata README's paths, `rstar-pipeline/README.md` step 6 and "The workshop's full dataset list", `app/README.md`,
both how-tos, `notes/dashboard/*`, both plans). **Found:** `import_dataset_pages.py` no longer runs on today's research
folders (GHCN-Daily's pt1 has no `query_questions.txt`, and the cleaner mangled a "Pages not read" bullet in `pt1.md`,
restored with `git restore`); that is the "web research pages" refresh in "The dashboard" below. The Python Playwright
memory was copied into this project's memory folder. Plan: `notes/dashboard-files-move-plan.md` (all steps done). Committed as `ebc9a90`; 140 e2e tests pass. Claude can
run the e2e tests itself in the Terminal panel (`run_in_terminal`), which is outside the Bash sandbox.

**Eighth session (2026-11-25): reorganized the repo around `rstar-pipeline/`.** Everything needed to rebuild the site's
data now lives in `rstar-pipeline/` as `input/` (framework: definitions, scoring, filing rules, form format;
dataset-metadata; web-research), `processing/` (instructions, research-queries, scripts: categorize, site-data,
dashboard) and `output/` (categories, gaps-notes); `rstar-pipeline/README.md` explains the layout and steps. Old →
new: `rstar_definitions/` → `input/framework/definitions/`; `docs/scoring/`, `docs/json_output/example_rstar_json.json`
and `docs/claude_feedback/rstar-categorization-decisions.md` → `input/framework/`; `datasets_metadata/json/` →
`input/dataset-metadata/`; `data-rstar-query-results/` → `input/web-research/`; the how-tos and format doc in `docs/`
and `notes/categorize-dataset-instructions.md` → `processing/instructions/`; `scripts/categorize|dashboard/` and
`app/scripts/build_data.py` → `processing/scripts/`; `data-rstar-categories/datasets/` → `output/categories/`; the
`*_categorization-gaps.md` notes → `output/gaps-notes/`. The query templates, examples and the two query design notes
(were `notes/dataset-query-5-part-plan.md`, `notes/archive-query-plan.md`) are now in `processing/research-queries/`
(templates and examples are copies from `Rstar_query_results`). `app/` and `datasets-gap-queries/` stayed; `docs/` holds
only `ideas/`. The rebuilt category JSON was byte-identical. The emptied old folders were trashed. `trash` works
from Claude's Bash only as a standalone command with absolute paths (global `excludedCommands: ["trash *"]`); chained
after `cd`/`&&` it stays sandboxed and fails. The e2e tests' "not categorized yet" cases now use a faked
uncategorized dataset (`uncategorized` fixture). Plan: `notes/rstar-pipeline-reorganization-plan.md`. 140 e2e tests
pass. Committed on `develop`: `dbca72b` (fake uncategorized dataset; standalone guide) and `0a8a054` (the
reorganization). The user merged both into `main` and pushed (`main` = `origin/main` = `0a8a054`). CLAUDE.md now
describes the `local-notes` snapshot step (snapshots `3424586`, `f4f69be`). Later the same day: wrote the plan for
bringing the workshop dashboard's files in (`notes/dashboard-files-move-plan.md`). The user answered its questions
1–4 (the repo stays public for now; a private copy on a second GitHub account and a DigitalOcean droplet come later).
The plan was then simplified (no big master list; cards built from the metadata JSON). **Next:** carry out the plan
when the user says go (see "Next steps"); the user is archiving the workshop files and will answer the droplet
questions later (see "Hosting").

**Seventh session (2026-11-24):** added IMERG pt7 Run 1 (`2026-11-24_imerg-late-run-people-production-pt7`:
people, ages, contracts, PPS processing) to `rstar-pipeline/processing/scripts/categorize/build_imerg-late-run.py` (second pass): 28 items
added, 5 dropped (the three GPCP-run people items, now covered by IMERG's own run; a low Huffman inference; pt3's Kidd
item, whose dates were wrong), 107 → 130. **P-1 0 → NA and P-4 0 → NA**; no other score changed; R* NA, 11 of 19 NA.
Judgment calls in the gaps note (ATMOS filed low "against" in D-1; P-4's "no deputy named" as moderate "for"; PDIR-Now
computed at PPS as DIRS-4 "against"). Site data rebuilt and checked in the preview; no e2e test uses IMERG scores.
Committed on `develop` as `5e5247e`. `rstar-pipeline/input/web-research/about-datasets/query_questions.txt` is the
user's untracked file; left alone.

**Sixth session (2026-11-24):** added GPCP pt7 Run 2 (`2026-11-24_gpcp-daily-calibration-copies-pt7`) to
`rstar-pipeline/processing/scripts/categorize/build_gpcp-daily.py`: 22 new items (102 → 124) in D-2, DIRS-1 to DIRS-5 and RRS-1; corrected the
RSS SSMIS CDR end to 2025-07-31; no score changed. Gaps note updated ("What pt7 Run 2 added", with the judgment
calls, e.g. ESGF obs4MIPs filed as not a repository). Site data rebuilt. Committed on `develop` as `e9645a4`.

**Fifth session (2026-11-24):** **categorized IMERG Late Run** (first pass, 107 items:
`rstar-pipeline/processing/scripts/categorize/build_imerg-late-run.py`, gaps note `rstar-pipeline/output/gaps-notes/imerg-late-run_categorization-gaps.md`
with the judgment calls). Scores: P-1 0, P-4 0, D-1 30, D-3 20, D-4 0, D-5 0, DIRS-2 25, DIRS-3 20, RRS-1 0, RRS-5 15;
the other 9 NA, so R* is NA. **The pt7 run covered only calibration, inputs, alternatives and copies** (its answer
says "Run 2"; the user ran one run), so P-1 to P-4, D-1/DIRS-4 contracts were never searched; the user will write
more queries and Claude re-categorizes (Prompt 5). The NASA GES DISC + PPS A2 run is also still to do. Site rebuilt;
`app/e2e/test_dashboard.py` changed (IMERG's card now has an R* link; no dataset is left without an R* entry, so the
"R* scores: NA" card branch has no test). All e2e tests pass (user ran them 2026-11-24). Committed on `develop` as `b64c26b`.

**Fourth session (2026-11-24):** wrote `rstar-pipeline/processing/instructions/categorize-dataset-instructions.md` (Claude's step-by-step for
categorizing a dataset, learned from GHCN-Daily) and **categorized GPCP Daily** (first pass, 102 items:
`rstar-pipeline/processing/scripts/categorize/build_gpcp-daily.py`, gaps note `rstar-pipeline/output/gaps-notes/gpcp-daily_categorization-gaps.md`, which
lists the judgment calls to review). Scores: D-3 20, D-4 0, D-5 0, DIRS-1 25, DIRS-2 25, DIRS-3 20, RRS-2 0, RRS-3 0;
the other 11 NA, so R* is NA. Site rebuilt. Committed on `develop` as `aca2bfa` (and the guide as `2ef9e52`).

**Earlier session (2026-11-24), in order:** renamed the site "R* Scores"; built the score graph page; made category lines
show their weighted share of R*; made the R* node red once it has a value; added evidence nodes behind an on/off
switch; coloured evidence green "for" and red "against"; added "Raw total" and "<Category> contribution" rows to the
category pages' score panel; made the category pages' stance tags green/red and the confidence badges purple
(high) / amber (moderate) / blue (low). All committed on `develop`.

**Third session (2026-11-24):** pinned each score box's badge to its top-right corner (`0e83931`); **moved the
workshop dashboard in as the landing page** (`8e1545c`; see "The dashboard" below; plan and the user's decisions in
`notes/dashboard-landing-merge-plan.md`); gave the R* pages the dashboard's styling (`4f285ff`); moved the "R* scores"
link onto each card's right half (`62c633d`); split the Pages workflow into build and deploy jobs (`b41d0f1`) after
two failed deploys. All committed, merged to `main` and pushed by the user; **the deploy worked and the live site is
up to date**. 140 e2e tests pass. The user is now running broad web research queries for the other datasets and will
come back to categorize them.

**Later on 2026-11-24 (a second session):** published the site on GitHub Pages, made the repo public, added a
top-level `README.md` for visitors, stopped tracking the working files (see "Publishing"), and redesigned the user's
GitHub Pages home page (https://lmerchant.github.io/). Committed on `develop` and pushed on `main`.

## Where things stand

| Piece | State |
|---|---|
| GHCN-Daily categorization | Done (fourth pass, 2026-11-23: 210 items, re-sorted under the decisions doc's rules, with scores): `rstar-pipeline/output/categories/ghcn-daily/ghcn-daily_rstar-categories.json`. 17 subcategories NA, RRS-2 and RRS-3 at 0, R* NA |
| GHCN-Daily research gaps | `rstar-pipeline/output/gaps-notes/ghcn-daily_categorization-gaps.md`. All four gap runs (pt6–pt9) and the NCEI A2 run are back and copied; the note's "After the gap runs" section says what each filled and what is left (mostly unpublished, so by hand or FOIA) |
| GPCP Daily categorization | Done (second pass, 2026-11-27, adding the NASA GES DISC + PPS A2 run; first pass and pt7 Run 2 2026-11-24): 134 items, 11 of 19 NA, R* NA; neither later run changed a score. Used its 8 runs, both NCEI runs, the NASA A2 run, both satellite runs and GHCN-Daily pt7/pt9 for NODD facts |
| IMERG Late Run categorization | Done (third pass, 2026-11-27, adding the NASA GES DISC + PPS A2 run): 149 items, 10 of 19 NA, R* NA. RRS-1 0 → NA, RRS-2 and RRS-3 NA → 0 (the user kept these calls, 2026-11-27; list in the gaps note). What's left (people, fixity schedules, DR tests) is mostly not public |
| PERSIANN-CDR Daily categorization | Done (first pass, 2026-11-27, before its pt7 people run): 100 items, 9 of 19 NA, R* NA. Used pt1–pt6, both NCEI runs and the UC Irvine CHRS A2 run. pt7 still to rewrite and run (see Research queue); its judgment calls await the user's review |
| CoCoRaHS (new dataset, id `cocorahs`) | Parts 1–5 and its data-site A2 (pt6) ran 2026-11-25/26; copied into `web-research/` (`about-datasets/cocorahs/`, `archives/cocorahs/`). Not categorized. Metadata JSON, card, overview and Parts 1–5 on the dashboard (`744041f`); its data-site run has no archive page |
| ASOS (new dataset, id `asos`) | Parts 1–5 and a Part 4 follow-up ran 2026-11-26; copied into `web-research/about-datasets/asos/` with question files (2026-11-27). Scored as the network as a whole. Not categorized. Metadata JSON, card, overview and Parts 1–5 on the dashboard (2026-11-27) |
| USCRN Daily (new dataset, id `uscrn-daily`) | Parts 1–5 ran 2026-11-26/27 (in pt2); copied into `web-research/about-datasets/uscrn-daily/`. Not categorized. Metadata JSON, card, overview and Parts 1–5 on the dashboard (`744041f`) |
| Dashboard web research pages | Current (2026-11-27): GHCN-Daily 1–9, GPCP 1–8, IMERG 1–8, PERSIANN-CDR 1–6, CoCoRaHS 1–5, USCRN Daily 1–5, ASOS 1–5 (2026-11-27). Process in `notes/dashboard/web-research-prep-howto.md` |
| Feedback on the first pass | `notes/claude_feedback/first_pass_to_categorize.md`. All answered (see Open questions) |
| Categorization rules | `rstar-pipeline/input/framework/rstar-categorization-decisions.md`, the master copy the user edits (2026-11-23). All its changes are applied. No Word copies are kept in the repo (they went out of sync); the user makes one with pandoc when needed |
| Categorization viewer | Done: static site in `app/` (landing page with R* scores and key, 4 category pages with card scores, "Your score" radios and a score panel with raw total and contribution, and the score graph page) |
| e2e tests | 152 pass (Firefox and WebKit, 2026-11-27, run by Claude in the Terminal panel, last after the NASA GES DISC + PPS run was added to IMERG and GPCP; before that after ASOS's card and pages were added: seven cards, and ASOS's overview and five parts are opened). Earlier: 116 pass (58 tests × Firefox and WebKit, 2026-11-24; score choices in `app/e2e/test_scores.py`, saving in `app/e2e/test_save.py`, the score graph in `app/e2e/test_graph.py`), Python Playwright. The empty-subcategory test now empties RRS-2 by intercepting `rstar-data.js`. Avoid `all_text_contents()`: it crashes this page in Playwright's Firefox |
| Score graph (weighted network graph) | Built 2026-11-24: `app/graph.html` + `app/assets/graph.js` (see "The score graph"), with evidence nodes behind an on/off switch. Knowledge graph not started |
| Query plans and templates | `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` (five parts per dataset) and `rstar-pipeline/processing/research-queries/archive-query-plan.md` (three kinds of repository, and a register of repositories). Templates in `Rstar_query_results/queries/` (see Research queries) |
| Guide for sharing | `rstar-pipeline/processing/research-queries/rstar-query-templates-guide.md` (2026-11-23): the query design, files, how to adapt it to other climate data, and starter prompts. Written for a friend of the user who will get the files in a new GitHub repo the user is making |


## Research queries

**Two projects.** Queries and research runs live in `/Users/claude/SIDE_WORK/NYCE_project/Rstar_query_results`
(its own git repo, also on `develop`). Runs save to its `web_search_results/`; the user copies finished runs into this
project's `rstar-pipeline/input/web-research/`.

**A second folder for parallel runs (2026-11-26):** `/Users/claude/SIDE_WORK/NYCE_project/Rstar_query_results_pt2` is
a clone of `Rstar_query_results` on branch `uscrn-runs`, so USCRN Daily can run there while ASOS runs in
`Rstar_query_results`, without the two sessions writing the same files (the run index and HANDOFF.md). It has the
skill's allowed-domains file and the saved pages (`work/`) of the five earlier runs the USCRN queries name. **Merged back
2026-11-27** into `Rstar_query_results`'s `develop`. The user is keeping pt2 for more parallel runs; that project's
HANDOFF.md says how to refresh it from `develop` first and merge it back afterwards.

**Copying runs in:** follow `notes/dashboard/web-research-prep-howto.md`. It covers which `query_answers` folders map to
which `web-research/` folders, copying only missing files, the `query_questions.txt` steps and the checks before the
page import.

**The design** (details in the two notes):
- **Five parts per dataset:** 1 overview, 2 QC/calibration/code/formats, 3 people and funding route (standard tier);
  4 threats and news, 5 threats to inputs (deep tier). Parts 1–3 keep threat words out so they stay standard.
- **Repositories:** shared archive gets A1 threats + A2 resilience, once; a producer's own data site gets A2 only (its
  threats are in the dataset's Part 4); copies get no run.
- **Runs stop at the token ceiling** (about 80% of it), not the time limit.
- **Each query tags findings** with subcategory codes and a supports/contradicts stance.

**Templates** (in `Rstar_query_results/queries/`):
- `dataset_queries/about_dataset_queries/templates/template-dataset-about_Rstar_query_pt1_overview.md` … `pt5_inputs.md`;
- `archive_queries/general_archive_queries/A1_Rstar_query_template-repository-threats.md` and
  `A2_Rstar_query_template-repository-resilience.md`.

**Research queue** (none of these is rewritten unless noted; the user runs them):

| Query | Where | State |
|---|---|---|
| GHCN-Daily pt6 (people), pt7 (repository), pt8 (infrastructure), pt9 (repository resilience) | `rstar-pipeline/input/web-research/about-datasets/ghcn-daily/` | Ran 2026-11-22 to 2026-11-23; copied |
| NCEI A2 | `rstar-pipeline/input/web-research/archives/noaa-ncei/2026-11-23_A2_Rstar_query-noaa_ncei/` | Ran 2026-11-23; copied. Serves GHCN-Daily, GPCP, PERSIANN-CDR and CoCoRaHS's copy (noted in their coverage notes) |
| GPCP pt7 (people and production) | `rstar-pipeline/input/web-research/about-datasets/gpcp-daily/2026-11-24_gpcp-daily-people-production-pt7/` | Ran 2026-11-24; copied; used in GPCP's categorization |
| GPCP pt7 Run 2 (calibration, alternatives, copies) | `rstar-pipeline/input/web-research/about-datasets/gpcp-daily/2026-11-24_gpcp-daily-calibration-copies-pt7/` | Ran 2026-11-24; copied; added to GPCP's categorization (22 items; judgment calls in the gaps note's "What pt7 Run 2 added") |
| IMERG pt7 Run 1 (people and production) | `rstar-pipeline/input/web-research/about-datasets/imerg-late-run/2026-11-24_imerg-late-run-people-production-pt7/` | Ran 2026-11-24; copied; added to IMERG's categorization (second pass) |
| PERSIANN-CDR pt7 (people and production) | `datasets-gap-queries/<id>_gap-queries/`; run sheet `datasets-gap-queries/supplemental-queries-run-sheet.md` | To rewrite and run |
| NASA GES DISC + PPS A2; UC Irvine CHRS A2 | `rstar-pipeline/input/web-research/archives/nasa-gesdisc-pps/` and `archives/uci-chrs/` | Ran 2026-11-27; copied 2026-11-27. The NASA run is in IMERG's (third pass) and GPCP's (second pass) categorizations; the UCI CHRS run is in PERSIANN-CDR's (first pass, 2026-11-27) |
| CoCoRaHS Parts 1–5 and its data-site A2 | `rstar-pipeline/input/web-research/about-datasets/cocorahs/` and `archives/cocorahs/` | Ran 2026-11-25/26; copied. Not categorized |
| ASOS Parts 1–5 (+ Part 4 follow-up) | `Rstar_query_results/web_search_results/2026-11-26_asos-*` | Ran 2026-11-26; `query_answers` copies committed there (`cc94615`) and copied into `about-datasets/asos/` (2026-11-27). NCEI-hosted: no repository run |
| USCRN Daily Parts 1–5 | `rstar-pipeline/input/web-research/about-datasets/uscrn-daily/` | Ran 2026-11-26/27 in pt2; merged into `Rstar_query_results` and copied 2026-11-27. Not categorized |
| IMERG inputs-pt6 | `rstar-pipeline/input/web-research/about-datasets/imerg-late-run/` | Copied 2026-11-23 (answer, query, record only). Rechecked: its leftover gaps were added to IMERG's coverage note and pt7 query |

The coverage notes (`datasets-gap-queries/<id>_coverage-gaps.md`) are not categorizations. Categorize each dataset once,
after its gap runs come back.

## Categorization format

Follows `rstar-pipeline/processing/instructions/create_rstar_node_files.md` (its last section lists the attributes added 2026-11-23). The filing rules
are in `rstar-pipeline/input/framework/rstar-categorization-decisions.md`; worked examples per subcategory are in the
"Counts / doesn't count" section of `rstar-pipeline/processing/instructions/categorizing-web-searches_README.md`.

- **One JSON file per dataset**, in `rstar-pipeline/output/categories/<dataset>/`.
- **Top keys:** `people_risk`, `data_risk`, `dep_infra_resilience`, `repo_resilience`, each holding its
  subcategory keys (`P-1` … `RRS-5`), plus `dataset` (producer, `producer_is_repository`, repositories with roles).
- **Each subcategory value** is HTML: `<div class="p-1" data-score data-score-basis data-status>` (RRS divs also
  `data-repositories`) containing:
  - `<h4>Evidence</h4><ul class="evidence">`: each `<li>` has `data-confidence` (high, moderate, low),
    `data-source` (the research run folder) and `data-stance` (`for`, `against` or `context`), sorted in that order;
    RRS items also `data-repository`;
  - then `<h4>Gaps</h4><ul class="gaps">`: each `<li>` has `data-status` (`searched-none-found`, `not-public`,
    `not-searched`).
- **Scores:** only high and moderate for/against items count. For only = full points, against only = 0, otherwise NA.
- **Inferences** are labelled "inference" and given low confidence (so they never set a score).
- **Source material:** any `answer_*.md` file in `rstar-pipeline/input/web-research/` that bears on the dataset (CLAUDE.md
  allows all of it): the dataset's own runs in `about-datasets/<dataset>/`, plus the relevant `archives/` and
  `instruments/` runs.
- **How the file is made:** hand-sorted evidence in `rstar-pipeline/processing/scripts/categorize/build_<id>.py`, which calls
  `write_categories()` in `rstar-pipeline/processing/scripts/categorize/rstar_common.py` (writing, sorting and scoring). Evidence tuples are
  `(confidence, run, text, stance[, repository])` with stance `"F"`, `"A"` or `"C"`; gaps are `(status, text)` with
  `"S"`, `"P"` or `"U"`. For a new dataset, copy the GHCN-Daily script, read all the answer files and write a gaps
  note in `datasets-gap-queries/`.

## Open questions for the user

**Discussion doc (2026-11-23):** `notes/claude_feedback/why-rstar-categories-are-hard-to-apply.md` (copy of the Claude
Doc at https://claude.ai/artifact/Q5rmmJHnFzAtNLHsubpZKW) sets out what makes the categories hard to apply, with
suggestions and questions the user plans to take to a colleague. It overlaps questions 2–6 below.

**Answered and applied (2026-11-23).** The user replied under `<reply>` tags in that doc and its follow-up,
`notes/claude_feedback/why-rstar-categories-are-hard-to-apply_follow-up.md`; both are records only.

**The current rules are in `rstar-pipeline/input/framework/rstar-categorization-decisions.md`.** That local file is the master
copy: the user edits only it (the Claude Doc https://claude.ai/artifact/ESJV1iYjXaoWyHjgEyZ6X6 is no longer updated)
and makes Word or other copies with pandoc when needed (no .docx files are kept in the repo, so nothing goes out of
sync). Read it before categorizing. All its changes were made on 2026-11-23:
scope sentences in the P, D and RRS definitions; the NA scoring rule in `rstar-pipeline/input/framework/how_to_score_rstar.md`;
"neutral" renamed "context"; gap statuses; repositories on RRS items; scores in the JSON; GHCN-Daily re-sorted; the
website's score section, key, producer sentence, card scores and repository labels; the "Counts / doesn't count" guide.

**Still open (for colleagues):** whether one station closing or only a whole network counts as a "source"; whether the
scoring decision table changes once users see mostly NA; repeating NCEI facts across subcategories; per-repository RRS.
First-pass questions 2 to 6 below are all answered.

From `notes/claude_feedback/first_pass_to_categorize.md`. Check whether the user has answered them before
categorizing another dataset.

1. ~~Should RRS and DIRS also use `archives/` and `instruments/`?~~ Answered yes (CLAUDE.md, 2026-11-22).
   They didn't fill RRS-2, RRS-3 or DIRS-1: those topics were never searched (see the gaps note).
2. Should `repo_resilience` be split by repository (NCEI, AWS, Google), or stay pooled?
3. Should there be a data-quality subcategory? QC and processing evidence has no home in D-1 to D-5 now.
4. Should evidence shared between subcategories be repeated, or cross-referenced ("see D-1")?
5. Is the JSON and HTML format right? That covers the file name, the Evidence and Gaps lists, the
   attributes, and keeping labelled inferences.
6. Should the 2025-to-present window in D-1 and RRS-4 be enforced strictly?

Other issues raised in the feedback:

- **Unknown scores unevenly.** Missing evidence scores 0, which reads as "no risk" for P, D and DIRS but
  "no resilience" for RRS.
- ~~**DIRS-1's "How to find" text** is about who does processing, not calibration.~~ Fixed 2026-11-23: the DIRS
  definitions now say DIRS covers only what the dataset needs to be produced (its networks, calibration, input
  feeds and processing), not the repository (that is D-2, D-3 and RRS), and each "How to find" was rewritten to
  match. GHCN-Daily's DIRS-4 lost four NCEI-wide items as a result. The viewer shows extra paragraphs of a
  "... defined" section (`definition_more`) on the category page only.
- **Decided 2026-11-23:** DIRS-5 also counts substitutes for the dataset itself (its "How to find" says so), so
  GHCN-Daily's HadISD, Berkeley Earth and ECA&D/C3S/WIS2 items stay.
- **Still to decide:** whether D-2 and D-3 should be scoped away from the repository the same way as DIRS.
- **The research never asked some questions:** succession plans, ages or ORCID, calibration, checksums,
  disaster recovery plans. Listed per subcategory, with suggested searches, in the GHCN-Daily gaps note.
- **Research file mix-ups:** two GHCN-Daily runs are both named "pt3", and the answers' cross-links point
  to `answer.md` files that don't exist.

## The dashboard (landing page, moved in 2026-11-24)

- **From** `/Users/claude/SIDE_WORK/NYCE_project/precip_workshop_dashboard` (copied at its commit `257b125`). That repo
  and its test site stay as they are (user's choice: it was a test, shown briefly); don't work in it any more.
- **Pages:** `index.html` (dashboard: cards, search, filters, detail panels), `overview.html`, `dataset.html`
  (web research parts), `archive.html` (archive and instrument threat pages). The old R* landing page is now
  `scores.html` (`data-page="scores"`).
- **Code and data:** `app/assets/dashboard/` (`dashboard.js` was `app.js`, `dashboard.css` was `styles.css`, plus
  `shared.js`, `overview.js`, `dataset.js`, `dataset-search.js`, `archive.js`, `markdown.js`); `app/data/*.json`
  (fetched, so these pages need a server) and `app/content/`. Scripts in `rstar-pipeline/processing/scripts/dashboard/` now read this repo's
  `rstar-pipeline/input/dataset-metadata/` and `rstar-pipeline/input/web-research/`; `build_datasets.py` builds and sorts the cards (2026-11-25). The old project's
  design notes and how-tos are in `notes/dashboard/` (paths in them still name the old project).
- **One set of ids** (user said saved scores can be lost): the dashboard took the R* ids `ghcn-daily`, `gpcp-daily`,
  `imerg-late-run`, `persiann-cdr-daily` (were `ghcn-d`, `gpcp-daily-v3-3`, `imerg-late-run-v07`,
  `noaa-ncei-persiann-cdr-v1r1`), in `datasets.json`, `dataset_pages.json`, `content/datasets/<id>/`, each
  `overview.json`, and `id` / `dashboard.id` / `dashboard.about_url` in `rstar-pipeline/input/dataset-metadata/*.json`.
- **Links between them:** `index.html` loads `data/rstar-data.js`; each card's header has a large "R* scores →" link
  on its right half (moved out of the panel at the user's request, 2026-11-24; "Not categorized yet" under it, or
  "R* scores: NA" for IMERG, which has no R* entry until its
  `rstar-pipeline/output/categories/imerg-late-run/` folder exists). `withDataset()` in `assets/app.js` now carries the
  dashboard's `q`, `category`, `coverage` and `open` through all R* pages, and the R* header has "← Back to dashboard"
  (`dashboardHref()`), which opens and focuses the current dataset's card (added to any already open).
- **Tests:** `e2e/test_dashboard.py` (new, 11 tests) and `test_landing.py` renamed `test_scores_page.py`; R* tests
  now open `/scores.html`.
- **Whole-site styling: done (2026-11-24)**, see `app/README.md` "One look for the whole site". R* pages are in the
  navy frame, light only; the header nav gained an "R* score" tab (current on `scores.html`).
- **Next for the dashboard:** (2) an R* score badge on each card (needs `currentScores()` moved out of `assets/app.js` into a shared
  script); (3) ~~refresh the web research pages~~ **done 2026-11-27**: all parts of the four carded datasets (see
  "Eleventh session"); CoCoRaHS and USCRN Daily added in `744041f`; ASOS added 2026-11-27; (4) fill the blank archive websites in `data/archive_links.json`. The old project's open items are in its
  `HANDOFF.md` "Next steps".

## The viewer (`app/`)

Plan: `notes/app-categorization-viewer-plan.md`. Details: `app/README.md`.

- **How it's built:** plain HTML, CSS and JavaScript, with no dependencies. `rstar-pipeline/processing/scripts/site-data/build_data.py`
  reads the definitions, the point values and weights, the dataset metadata and the categorization JSON,
  and writes `app/data/rstar-data.js`.
  - **Re-run it after changing any of those inputs:**
    `python3 rstar-pipeline/processing/scripts/site-data/build_data.py`.
  - The pages load the data with a `<script>` tag, so they also work opened from disk.
- **Title:** the site is titled "R* Scores" (header, landing h1 and page titles; renamed from "R* categorizations"
  2026-11-24). The "Score details" tables show only the person's chosen scores.
- **Pages:** `index.html` (dataset selector, dataset details with the producer-is-repository sentence, the R* score
  section with a "Score details" panel, then the key to the tags and scoring, and 4 category cards with coverage
  chips), plus one page per category. On a category page each subcategory card shows its Description,
  "What counts as evidence", why the research gives its score, "Your score" radios (starting on the research score;
  no research-score badge), its status (RRS cards: the
  repositories), and opens to show the evidence. A panel beside the category description lists the chosen scores,
  the "Raw total" (renamed from "Total", 2026-11-24) and below it the "<Category> contribution" row: what the
  category adds to R* (weight × raw total; RRS 0.20 × (100 − raw total)), with the most it can add in the Points
  column.
  - **Chosen scores (2026-11-23):** the radios offer full points, 0 or NA and start on the research score. The
    sentence above them states the implied score, for example "Both “for” and “against” web evidence (high or
    moderate): score = NA" (was "needs a decision"; the user's colleague is reviewing whether "score = NA" reads as
    the score implied by the web evidence). The panel's button is "Reset scores" and resets only that
    category; a second "Reset scores" beside "Score details" on the landing page resets all categories (it asks
    first). Notes are never reset. On-screen text says "web evidence
    score" for the research score. Each person's browser keeps their choices between visits (the user chose this over
    starting fresh each visit; the site will be on the droplet, one form per person). Choices
    are kept in `localStorage` (`rstar-chosen-scores-v1`, shaped `{"<dataset id>": {"P-1": 35, ...}}`) and the
    category panel, landing totals and R* are worked out from them in `app.js` (`currentScores()`, same rule as
    `build_data.py`). Details in `app/README.md`.
  - **Notes and saving (2026-11-23):** each card has a "Your notes" box. The landing page's "Save your scores" panel
    (name, email, role) downloads one JSON file per save in the colleague's form format
    (`rstar-pipeline/input/framework/assessment-form/example_rstar_json.json`) plus an `assessor` block; NA is `null`, notes go in
    `justification`, `scoringMethod` is `""`. Plan and the user's answers: `notes/rstar-score-json-save-plan.md`;
    changes to pass to the colleague: `notes/rstar-json-format-changes.md`; schema:
    `app/schema/rstar-assessment.schema.json`.
  - Deep links work: `people-risk.html?dataset=ghcn-daily#P-3`.
  - **"What counts as evidence" (2026-11-23):** each subcategory in `rstar-pipeline/input/framework/definitions/` now has a
    `#### What counts as evidence` section, a reader's version of `#### How to find`. The site shows it in place of
    "How to find", which stays as the search instructions for queries and categorizing. Edit both together when a
    definition changes.
  - **No research run names (2026-11-23):** evidence items no longer show the run folder ("repository-pt7"); readers
    don't know the files. It is still in each item's `data-source` in the JSON.
  - **Evidence tags (2026-11-24):** stance tags are solid green "For", solid red "Against", grey "Context". Confidence
    badges and each item's left border are purple high, amber moderate, blue low (see Colours below).
- **Header nav:** its accessible name is "Pages" (was "Categories"); it holds the 4 categories and "Score graph".
- **Viewing:** after each big change, give the user this command (CLAUDE.md):
  `cd /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/app && python3 -m http.server 3000 --bind 127.0.0.1`,
  then http://127.0.0.1:3000/.
- **Claude's own preview:** `.claude/launch.json` defines `rstar-viewer` (port 8765) and `rstar-viewer-2` (port 8766,
  for when another chat holds 8765) for the built-in browser. The built-in browser can't load the CSS and JS of a page opened from disk, so serve it.
- **Accessibility:** follows the frontend-ui-engineering skill.
  - Each card's arrow is a `<button aria-expanded>` that controls a `role="region"` panel.
  - Headings go h1, then h2 (subcategory), then h3.
  - Coverage dots have screen-reader text.

## The score graph (`app/graph.html`, built 2026-11-24)

Draws the dataset's **chosen** scores (the same as the landing page, so it changes as scores are picked) as a weighted
network graph in plain SVG. Reached from "Score graph" in the header and "See the score graph →" on the landing score
panel. Code: `app/assets/graph.js` (no libraries); `app.js` passes it its helpers through
`window.RSTAR_GRAPH.render(ctx)`. Evidence plan: `notes/score-graph-evidence-nodes-plan.md`. All design choices come
from the user's notes (`docs/ideas/...`) or were decided with the user on 2026-11-24.

- **Nodes:** R* in the middle, black while NA and red once every subcategory has a score. Four category nodes in their
  own colours (P blue, D orange, DIRS aqua, RRS violet; P and RRS sit opposite because they are the hardest pair to tell
  apart), each showing its raw total and "adds X" (its share of R*). Subcategory nodes in the parent's colour, showing
  ID and score. NA nodes are black with a ring in the category colour.
- **Line widths:** subcategory line = score ÷ 5 (35 → 7 px). Category line = its weighted share of R* ÷ 4 (the user
  chose the share over the raw total), so D's most is 10 px, P 7.5, RRS 5, DIRS 2.5. A 0 is 1 px; NA is dashed.
- **RRS switch:** "Repository resilience subcategory lines show" risk (points − score, default) or score. The RRS line to
  R* is always its share, 0.20 × (100 − raw total).
- **Evidence nodes:** the "Show evidence nodes" switch (`role="switch"`, off by default, `&evidence=on` in the URL)
  adds one dot per evidence item (210 for GHCN-Daily, 127 set a score) in a fan outside each subcategory node, joined by
  thin grey lines. Green circle = for, red diamond = against, small grey ring = context; filled = sets the score
  (high/moderate), outline = low confidence. Dots have hover tooltips (stance, confidence, repository, first 200
  characters), click through to the card, and dim while another subcategory node is hovered or focused. They are read
  from the category JSON in the browser (`build_data.py` unchanged), are not tab stops and are hidden from screen
  readers.
- **Around it:** a summary sentence (R* value and triage tier, or how many subcategories are NA), a graph key, hover/focus
  tooltips on nodes (subcategory and category nodes are links to their cards/pages), and "The graph as a table" (every
  node, score, line drawn and evidence counts). Below 660 px wide the graph scrolls sideways.

## Publishing

- **Nothing is published from this repo yet.** It is private, and GitHub Pages doesn't publish from a private repo on
  GitHub Free, so its Pages workflow was removed. The site will be served from a DigitalOcean droplet (see "Hosting").
- **The old public site** (https://lmerchant.github.io/Rstar_precipitation-relationships/) is published from the old
  repo and stays as it is. The user's home page https://lmerchant.github.io/ links to it; Claude's copy of the home
  page is in the old folder's `.work/lmerchant.github.io/`.
- **To push** (the user runs it; the sandbox blocks github.com):
  `git switch main && git merge --ff-only develop && git push origin main && git switch develop`. That one push
  updates both GitHub copies (see "This repo").
- **Commit `app/data/rstar-data.js` after rebuilding it:** no build runs on the server, so the committed `app/` is the
  site.

## Hosting (user's plan, 2026-11-25)

- **A new DigitalOcean droplet**, to buy after the private repo is set up. Set it up like the user's example
  `/Users/claude/PROGRAMMING/Claude_code_apps/ny_climate_dashboard_app/docs/digitalocean/review-site-on-digitalocean.md`
  (a different droplet; there: Ubuntu 24.04, Caddy with `basic_auth`, a sslip.io address because there's no domain,
  HTTPS from Let's Encrypt, and a publish script that rsyncs the built site from the Mac). No domain yet.
- **It will serve the output of several GitHub repos.** Some sites are public (nothing sensitive). The others are
  behind passwords: **a workshop password** for the workshop sites (workshop participants need the output of more than
  one repo, and agency people use the same password for those), and **an internal password** for the agency's
  internal sites. The agency can see everything. This project is a workshop site.
- **Still to decide then:** one shared login per group or one per person (shared is simplest; the example's notes say
  how to add per-person logins); how sites are laid out (paths on one sslip.io name, or one name each); deploying by a
  publish script from the Mac (as in the example) or from GitHub Actions.
- The sandbox can't reach github.com or the droplet, so the user runs those commands; Claude writes the config files
  and scripts.
- **Saved scores on the droplet: later, not today.** The user will want saved scores collected eventually (now each
  participant's browser downloads a JSON file). That needs a small server program on the droplet, not just static
  files; plan it when the user asks.
- **Settled (user, 2026-11-25):** the people evidence is fine to show (it comes from public web sources); the colleague
  approves the R* framework, scoring and form format; the email addresses in the old repo's commits are fine; this
  repo's commits use the noreply address.

## Colours (`app/assets/styles.css`)

Light only since 2026-11-24 (the dashboard styling; the dark theme was dropped). All text passes 4.5:1 and marks and
control edges 3:1. Green and red mean **stance only**. The R* pages also use the dashboard's own tokens from
`assets/dashboard/dashboard.css` (`--header-text`, `--mist-blue`, ...) in the header band.

| Token | Meaning |
|---|---|
| `--cat-p`, `--cat-d`, `--cat-dirs`, `--cat-rrs` | Category colours on the graph (checked with the dataviz palette validator) |
| `--ev-for` (green), `--ev-against` (red), `--ev-on` | Evidence stance: graph dots and the category pages' solid stance tags |
| `--conf-high` (purple), `--moderate` (amber), `--conf-low` (blue) | Confidence badges and evidence item borders |
| `--rstar-bg` (red) | The R* node once it has a value |
| `--na-bg` (black), `--na-border` | NA scores everywhere |
| `--card`, `--card-hover`, `--card-rule` | Dashboard card colours: category and subcategory cards, and the teal rule on section boxes |
| `--text`, `--body`, `--muted`, `--link` | Headings, body text, labels (#46606F, 4.57:1 on the hover colour) and links |
| `--accent`, `--control-border` | Deep ocean for selected things (tabs, chosen score, primary button); slate edges on inputs and buttons |
| `--high`, `--low` | Still used for coverage dots (green = 4+ items) and the save form's error text; not for confidence |

## Tests

- **Tool:** Python Playwright, not npm. It lives in `.work/venv`, with versions pinned in
  `app/requirements-dev.txt`. The tests are in `app/e2e/`, and `pytest.ini` runs Firefox and WebKit only.
- **Run them in the Terminal panel,** not the Bash tool. In the sandbox, pip can't reach PyPI and servers
  can't bind ports:
  `cd /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/app && ../.work/venv/bin/pytest`
- **The venv was rebuilt in this folder on 2026-11-25** (it was not copied from the old one).
- **Rebuild the venv** if its Python disappears (Anaconda was uninstalled on 2026-11-22): the command is in
  `app/README.md`. It uses `/opt/homebrew/bin/python3` (3.15).
- **Don't remove the DYLD fix.** `~/.zshrc` sets `DYLD_LIBRARY_PATH=/opt/homebrew/lib`, which made
  Playwright's Firefox load Homebrew's libnss3 and crash. `app/e2e/conftest.py` removes the variable.
  - The user may switch the shell line to `DYLD_FALLBACK_LIBRARY_PATH`.
  - `/usr/bin/env` hides `DYLD_*` variables, so check with `echo $DYLD_LIBRARY_PATH` instead.
- **Node** (v26, Homebrew) is now installed. The tests stay on Python unless the user asks to switch.

## Repository and working conventions

- Work on `develop`. Commit only when the user asks. The user pushes only `main` (`develop` is not on GitHub). See
  "Publishing" for the command.
- `.work/` holds the venv, logs and debug scripts, and is git-ignored. `notes/` is for Claude's plans.
  `docs/` is the user's.
- Use `trash`, never `rm`.
- `Rstar_query_results` is a separate git repo (also on `develop`) for queries and research runs. Commit query files
  there and project files here, each in its own commit.
- **Commit style:** one commit for the change (code, tests, README, notes). Messages end with the Co-Authored-By line.
- **What's committed here:** everything except `docs/ideas/` and `.work/`. There is no `local-notes` branch in this repo.

**Tips from the 2026-11-24 session:**
- **The `guard_bash` hook blocks any Bash command whose text contains `cat.key`** (it reads it as a key file). `app.js`
  and `graph.js` use `cat.key` a lot, so for edits that include it, write a Python edit script to the scratchpad with
  the Write tool and run the file, or use the Edit tool.
- **Cached CSS:** `python3 -m http.server` lets the browser reuse old CSS/JS. After a style change, hard-refresh
  (Cmd+Shift+R), or in the built-in browser run `fetch(<stylesheet href>, {cache: 'reload'})` then reload. Tell the user
  to hard-refresh too.
- **Screenshots right after a redraw** can catch the 0.15 s fade or dimming transitions and look washed out; zoom in, or
  check computed styles with JavaScript.
- **Auto mode** sometimes refuses a call sent in the same message as another; send it again on its own.

## Next steps

**How-to for Claude:** `rstar-pipeline/processing/instructions/categorize-dataset-instructions.md` (read it before categorizing). Since 2026-11-25 it
stands on its own (R* background, JSON format, a per-dataset state table, settled and open rules, precedents, viewer
and test checks), so a categorizing session doesn't need this file; update its state table after each pass. **How-to for the user:** `rstar-pipeline/processing/instructions/categorizing-web-searches_README.md` has the prompts for categorizing a dataset,
adding it to the website, writing gap queries and adding new research. Follow it for the other datasets.

**Dashboard files (plan `notes/dashboard-files-move-plan.md`, second version).** Step 1 is done: the metadata
Markdown, its template and README, and the page clean-up rules were copied in from `precip_workshop_dashboard` on
2026-11-25 (checked with `cmp`). The user archived that project's `my_docs/` and `.work/` outside the sandbox (the
47-dataset list, the workshop CSV, the inventory and the rest; brought back only when needed; about 15 datasets here for
a long while). **Steps 2–3 done 2026-11-25** (ninth session): `build_datasets.py` builds `app/data/datasets.json` from each dataset
metadata JSON's `dashboard` block, so a card is edited in one place. Step 4 done: 140 e2e tests pass; committed as
`ebc9a90`.

0. ~~**Next:** categorize PERSIANN-CDR Daily~~ **done 2026-11-27** (first pass, before pt7; its pt7 people run is
   still to rewrite and run). ~~Add the NASA GES DISC + PPS A2 run to IMERG and GPCP~~ **done 2026-11-27** (IMERG third
   pass, GPCP second pass; see their gaps notes' judgment calls).
   *Done 2026-11-24 (kept for reference): categorize IMERG Late Run (id `imerg-late-run`)* in a new session, once the user has copied in the last of
   its query results. GHCN-Daily and GPCP Daily are done and committed (`aca2bfa`, `2ef9e52`); the user is publishing
   them by merging `develop` into `main` and pushing.
   - **Read first:** `rstar-pipeline/processing/instructions/categorize-dataset-instructions.md` (Claude's step-by-step) and follow it, then
     `datasets-gap-queries/imerg-late-run_coverage-gaps.md` (hosts, versions and what each gap run was meant to fill).
   - **Check the research is all there:** `rstar-pipeline/input/web-research/about-datasets/imerg-late-run/` had pt1 to pt6 on
     2026-11-24; the gap run pt7 (people and production, query in
     `datasets-gap-queries/imerg-late-run_gap-queries/`) and the NASA GES DISC + PPS A2 run (into
     `rstar-pipeline/input/web-research/archives/`) were still to come. Use whatever is there and list anything still missing in
     the gaps note, as GPCP's note does for GES DISC.
   - **Sources beyond its own folder:** `instruments/nasa-satellites` and `instruments/noaa-satellites` apply (GPM, DMSP,
     POES, S-NPP, AMSR2, GOES); the NCEI runs only if a source puts an IMERG copy at NCEI. PERSIANN-CDR's people
     overlap with IMERG's (UC Irvine CHRS makes PDIR-Now, an IMERG input), so note any names shared with that dataset.
   - **Make:** `rstar-pipeline/processing/scripts/categorize/build_imerg-late-run.py` (copy the layout of `build_gpcp-daily.py`, the closest
     satellite example; write the evidence fresh), which creates `rstar-pipeline/output/categories/imerg-late-run/` and its
     JSON; `rstar-pipeline/output/gaps-notes/imerg-late-run_categorization-gaps.md` (follow GPCP's: scores table and judgment calls);
     then `python3 rstar-pipeline/processing/scripts/site-data/build_data.py`.
   - **Tests:** `app/e2e/test_dashboard.py` (lines 72–73) uses IMERG's card as the "R* scores: NA" example (no R* entry
     at all). Once IMERG is categorized that test fails: change it to check IMERG's card now has an "R* scores" link,
     and keep PERSIANN-CDR Daily as the "Not categorized yet" example. Run the e2e tests in the Terminal panel.
   - **Finish:** check the pages in the browser, report scores and judgment calls, update `README.md`'s dataset table and
     this file, give the server command, and commit on `develop` when the user asks. Consider refreshing the dashboard's
     web research pages from the newer runs too (see "The dashboard").
1. **Copy finished runs into `rstar-pipeline/input/web-research/`** as they come back, following
   `notes/dashboard/web-research-prep-howto.md` (dataset runs into `about-datasets/<id>/`, repository runs into
   `archives/<repository>/`, then the question files and the page import). Everything is copied, ASOS last (2026-11-27). The GES DISC/PPS run is now in GPCP's and IMERG's
   categorizations (2026-11-27); the UCI CHRS run is in PERSIANN-CDR's (2026-11-27).
2. **Review GHCN-Daily's fourth-pass stance calls** (listed in the session that made them): 15 items became
   context, including P-2's NCEI-wide retirements (P-2 is now NA), D-1's rejected FY2026 request, five D-5 items with
   no GHCN-Daily tie, and the Data Rescue snapshot. Also P-2's retirement estimates and RRS-1's single-region items.
3. **Review GPCP Daily's and IMERG's judgment calls** (lists in their gaps notes; the NASA GES DISC + PPS A2 run was
   added 2026-11-27, and the user kept IMERG's RRS-1 to RRS-3 calls from it). **Point values settled (user, 2026-11-27):** `how_to_score_rstar.md`'s DIRS-2
   25, P-3 25, DIRS-4 15 are right; the decisions doc's table (which said 20, 20, 20) was corrected to match. The site
   already used these, so no score changed.
   **Categorize PERSIANN-CDR Daily and IMERG Late Run** once their pt7 and repository runs are back, using
   their coverage notes. Each needs a folder in `rstar-pipeline/output/categories/` (`imerg-late-run/` doesn't exist
   yet) and a `rstar-pipeline/processing/scripts/categorize/build_<id>.py`. Re-run `build_data.py` afterwards.
4. **Categorize CoCoRaHS, USCRN Daily and ASOS.** All three have their research in; all three have metadata JSON
   and cards (ASOS's 2026-11-27).
5. **Keep the repository register in `rstar-pipeline/processing/research-queries/archive-query-plan.md` current** when a new dataset names a new host.
6. **Saving scores is built (download to the scorer's computer).** Still to do when wanted: "Load a saved file" to
   carry on scoring, a server that collects files (the user wants to think about this later), and
   `scripts/analyze/collect_rstar_scores.py` to turn a folder of saved files into a CSV. The user is telling the
   colleague about the format changes (`notes/rstar-json-format-changes.md`). The viewer plan also
   lists confidence filters and a side-by-side dataset view as later ideas.
7. **Score graph: next pieces** (the user likes the current version), from
   `docs/ideas/rstar_relationship_graph/rstar_graphs.md` and `docs/ideas/R Precip dashboard.md`:
   - still open from the notes: whether RRS lines should default to risk or score; whether score lines should be red
     for risk rather than the category colour (the notes say both);
   - evidence nodes: gaps as nodes (up to 3 per subcategory)? and an attribute in the categorize scripts marking
     evidence that comes from another dataset (for the thick lines the notes ask for);
   - two datasets side by side, and expert / workshop / participant versions of the same graph;
   - the separate knowledge graph (dataset, repository, people and instrument connections from the metadata files).
   - With the stance/confidence colour clash gone, the stance tags could go back to pale tints if the user prefers.
8. **Keep the e2e tests passing in both browsers** as the viewer changes.
