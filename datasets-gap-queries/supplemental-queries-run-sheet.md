# Supplemental queries: run sheet for GPCP Daily, IMERG Late Run and PERSIANN-CDR Daily

Written 2026-11-23. These queries fill what the first six runs of each dataset never asked, found by a coverage check
against the 19 subcategories (not a categorization, so each dataset is categorized only once, after these come back).
The gaps notes are [gpcp-daily_coverage-gaps.md](gpcp-daily_coverage-gaps.md),
[imerg-late-run_coverage-gaps.md](imerg-late-run_coverage-gaps.md) and
[persiann-cdr-daily_coverage-gaps.md](persiann-cdr-daily_coverage-gaps.md).

**The shape follows `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md`:** each dataset gets one "people and production" run, and the
repository questions go to shared runs, one per repository, so NCEI and GES DISC are each searched once.

## The queries

| # | File | Covers | Limits | Order |
|---|---|---|---|---|
| 1 | [persiann-cdr-daily-gaps_Rstar_query_pt7_people-production.md](persiann-cdr-daily_gap-queries/persiann-cdr-daily-gaps_Rstar_query_pt7_people-production.md) | PERSIANN-CDR: P-1 to P-4, D-1, DIRS-1, DIRS-3 to DIRS-5, copies | 40 min, 320,000 | Before IMERG's, which can cite its CHRS people |
| 2 | [imerg-late-run-gaps_Rstar_query_pt7_people-production.md](imerg-late-run_gap-queries/imerg-late-run-gaps_Rstar_query_pt7_people-production.md) | IMERG: P-1 to P-4, D-1, DIRS-1, DIRS-3 to DIRS-5, copies | 40 min, 320,000 | Any time; after 1 if possible |
| 3 | [gpcp-daily-gaps_Rstar_query_pt7_people-production.md](gpcp-daily_gap-queries/gpcp-daily-gaps_Rstar_query_pt7_people-production.md) | GPCP: P-1 to P-4, D-1, DIRS-1, DIRS-4, DIRS-5, copies | 40 min, 320,000 | Any time |
| 4 | `Rstar_query_results/queries/archive_queries/archive_specific_queries/A2_Rstar_query-nasa_gesdisc_pps.md` | NASA GES DISC and PPS: RRS-1 to RRS-3, RRS-5, D-2, D-3 | 40 min, 320,000 | Any time |
| 5 | `Rstar_query_results/queries/archive_queries/archive_specific_queries/A2_Rstar_query-uci_chrs.md` | CHRS data site: RRS-1 to RRS-5, D-2, D-3 | 30 min, 240,000 | Any time |
| — | `Rstar_query_results/queries/archive_queries/archive_specific_queries/A2_Rstar_query-noaa_ncei.md` | NCEI: RRS-1 to RRS-3, RRS-5 (also serves GHCN-Daily) | 40 min, 320,000 | Ran 2026-11-23; copied to `archives/noaa-ncei/` |

That's 5 new sessions for the three datasets, plus the NCEI A2 run (done 2026-11-23). All five are
standard-tier questions: none asks about cuts or news, which the earlier runs already covered.

## Step 1: rewrite all five in one session

Open a session in the research project (`Rstar_query_results`) and paste this as one message, with the paths adjusted
if you copy the dataset files into that project's query folders first:

```text
/my:rewrite-research-query /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/datasets-gap-queries/persiann-cdr-daily_gap-queries/persiann-cdr-daily-gaps_Rstar_query_pt7_people-production.md /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/datasets-gap-queries/imerg-late-run_gap-queries/imerg-late-run-gaps_Rstar_query_pt7_people-production.md /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/datasets-gap-queries/gpcp-daily_gap-queries/gpcp-daily-gaps_Rstar_query_pt7_people-production.md queries/archive_queries/archive_specific_queries/A2_Rstar_query-nasa_gesdisc_pps.md queries/archive_queries/archive_specific_queries/A2_Rstar_query-uci_chrs.md

Rewrite all five files in one go. In each file, read the draft from "## Query to refine", including its "Context for the rewrite" and "What the answer should give" subsections. Write the rewritten question into "## Claude web research skill query" and your notes into "## Claude comments about the rewritten query". Keep the run folder names the drafts give, keep the time and token limits unless you explain a change, and keep each question standard tier (no cuts, threats or news).
```

## Step 2: run each in its own session

In the research project, check that the run folders each question names are in `web_search_results/`, then paste the
file's `## Claude web research skill query` section.

## Step 3: copy the results back

Copy each run folder into this project's `rstar-pipeline/input/web-research/`:
- dataset runs into `about-datasets/<id>/`;
- repository runs into `archives/<repository>/` (for example `archives/nasa-gesdisc-pps/` and `archives/uci-chrs/`).

(GHCN-Daily pt6–pt9, the NCEI A2 run and IMERG inputs-pt6 are already copied.) Then categorize each dataset (Prompt 1 in
`rstar-pipeline/processing/instructions/categorizing-web-searches_README.md`), using its own runs, the shared repository runs and the instrument runs.
