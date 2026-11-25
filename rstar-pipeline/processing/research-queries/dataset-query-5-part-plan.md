# Plan: five research queries per dataset, matched to the R* subcategories

Written 2026-11-23. This plan turns the GHCN-Daily starting query
(`notes/old/example_starting_queries/ghcn-d-about_Rstar_query_chatgpt.md`) into a general set of five queries
that any precipitation dataset can use. Together the five cover all 19 subcategories in `rstar-pipeline/input/framework/definitions/`.

## Why change the split

GHCN-Daily took **10 research sessions** (6 "about" runs, then 4 gap runs) to reach all 19 subcategories.
The other three datasets took 5 or 6 runs each, and none of them has asked about people's ages, calibration,
checksums or disaster recovery yet.

| Problem in the current split | Evidence | Fix in this plan |
|---|---|---|
| The starting query never asked some subcategories' questions | Only the GHCN-Daily gap queries mention ORCID, retirement, checksums, CoreTrustSeal or disaster recovery. Calibration appears only in the satellite algorithm sense | Each part's draft is written from the subcategories' "How to find" text, so every subcategory has a home in a part |
| Funding, threats and news were split over 2 or 3 runs that searched the same budget fights | GHCN-Daily pt3 / pt3_combined / pt4; IMERG pt4 / pt5; PERSIANN-CDR pt3 / pt4 | One threats run for the dataset and its producers (Part 4), one for its inputs (Part 5) |
| Repository questions were asked per dataset, though one repository hosts several datasets | NCEI hosts GHCN-Daily, GPCP Daily and PERSIANN-CDR Daily. GHCN-Daily's pt9 asks about NCEI's checksums and recovery plan, which are the same for all three | Repository resilience goes in a **shared run per repository**, done once and cited by every dataset it hosts |
| Threat words in a fact-finding run push it to the expensive deep tier | The research records give the tier reason "dispute" whenever cuts appear. GHCN-Daily's funding pt3 stayed standard because the query left cuts to pt4 | Parts 1–3 say "leave cuts, threats and news to Part 4" |

## What the runs actually used

From the `research-record.json` files in `rstar-pipeline/input/web-research/`. Runs stop at the research stop, about
80% of the token ceiling, and finish in 60–75% of the time limit. **The token ceiling sets the size of a run.**

| Limits given | Tier | Runs measured | Tokens used | Minutes used |
|---|---|---|---|---|
| 30 min / 240,000 | standard | 9 (about, QC and formats, people, funding route) | 141,000–197,000 | 14–23 |
| 40 min / 320,000 | deep | 4 (funding and news, inputs) | 213,000–288,000 | 26–29 |
| 50 min / 400,000 | deep | 4 (satellites, inputs, NCEI threats, NASA satellites) | 333,000–371,000 | 31–36 |

So a standard run has room for about one more sub-question than it gets now. The threat runs fill their
ceilings, as you saw.

## The five parts

| Part | Topic | Tier and limits | Subcategories it answers | Run after |
|---|---|---|---|---|
| 1 | Overview: hosts, inputs, producers | standard, 30 min / 240,000 | RRS-1 (copies and mirrors), D-2 (who serves it), DIRS-3 (input list), DIRS-4 (outside groups), P-4 (which groups) | first |
| 2 | Processing, QC, calibration, code, formats | standard, 30 min / 240,000 | D-4, P-3, DIRS-1, DIRS-4 | Part 1 |
| 3 | People, team and the funding route | standard, 40 min / 320,000 | P-1, P-2, P-4, and the funding baseline for D-1 | Part 1 |
| 4 | Threats to the dataset, its producers and its hosts | deep, 50 min / 400,000 | D-1, D-3, D-5, RRS-4, plus staff losses for P-2 and P-4 | Part 3 and the shared repository runs |
| 5 | Threats to its inputs, and alternatives | deep, 40–50 min / 320,000–400,000 | DIRS-1 (threats to calibration facilities), DIRS-2, DIRS-3, DIRS-5 | Parts 1 and 2, and the shared instrument runs |

Parts 2 and 3 can run in either order. Part 5 can run any time after Part 2. Total limits: 190–200 minutes
over 5 sessions, compared with about 380 minutes over 10 sessions for GHCN-Daily.

**Use 50 min / 400,000 for Part 5** when the dataset has many inputs (GPCP Daily and IMERG, with 15 to 40
satellites). For a dataset with one or a few inputs, 40 min / 320,000 is enough.

### Shared runs (once per repository or instrument family, not per dataset)

| Shared run | Status | Subcategories | Datasets that cite it |
|---|---|---|---|
| A1: repository threats (NCEI) | Done: `archives/noaa-ncei` | RRS-4, D-1 for the host | GHCN-Daily, GPCP Daily, PERSIANN-CDR Daily |
| **A2: repository resilience (new)**, one per repository | NCEI's draft is written: `Rstar_query_results/queries/archive_queries/archive_specific_queries/A2_Rstar_query-noaa_ncei.md`. It replaces GHCN-Daily's gap pt9 and builds on the pt7 run | RRS-1, RRS-2, RRS-3, RRS-5, D-2, D-3 | every dataset the repository hosts |
| A4: instrument families | Done: NOAA rain gauges, NOAA satellites, NASA satellites | DIRS-2 | each dataset that uses them |

Other repositories that may need A1 and A2 runs: NASA GES DISC and NASA PPS (IMERG, GPCP V3), and the
cloud copies under NOAA's Open Data Dissemination program (AWS, Google). Check Part 1's host list for each
dataset before writing these. A producer's own data site, such as CHRS for PERSIANN-CDR or CoCoRaHS, gets an A2
run but no A1: its funding and threats go in the dataset's Part 4. See `rstar-pipeline/processing/research-queries/archive-query-plan.md` for the three
kinds of repository and the register of which runs exist.

## Template files

The drafts below are also template query files, in your query files' layout. They add context for the rewrite, what
the answer should give, the placeholders, and the run order. They are in
`/Users/claude/SIDE_WORK/NYCE_project/Rstar_query_results/queries/`:

| Part | Template |
|---|---|
| 1 | `dataset_queries/about_dataset_queries/templates/template-dataset-about_Rstar_query_pt1_overview.md` |
| 2 | `dataset_queries/about_dataset_queries/templates/template-dataset-about_Rstar_query_pt2_processing.md` |
| 3 | `dataset_queries/about_dataset_queries/templates/template-dataset-about_Rstar_query_pt3_people.md` |
| 4 | `dataset_queries/about_dataset_queries/templates/template-dataset-about_Rstar_query_pt4_threats.md` |
| 5 | `dataset_queries/about_dataset_queries/templates/template-dataset-about_Rstar_query_pt5_inputs.md` |
| A2 | `archive_queries/general_archive_queries/A2_Rstar_query_template-repository-resilience.md` |

Copy a template into the dataset's folder, replace the `$PLACEHOLDERS`, then rewrite it.

## Draft starting queries (to rewrite with `/my:rewrite-research-query`)

Replace the placeholders for each dataset:

- `$DATASET`: short name and full name, such as "GHCN-Daily (Global Historical Climatology Network–Daily)"
- `$RELATED`: related products to mention only to say how they differ (GHCN-Monthly; IMERG Early and Final)
- `$HOSTS`: the repositories from Part 1 (NCEI, AWS, Google BigQuery)
- `$SHARED_RUNS`: the A1, A2 and A4 run folders that apply
- `$CANDIDATES`: inputs to check in Part 5 (networks for a station dataset; satellites and sensors for a
  satellite dataset)
- `$NOW`: the month the run happens, such as November 2026

Each draft has about 5 sentences. Each ends by asking the run to tag findings with the subcategory codes they
bear on, as the GHCN-Daily gap queries did, so that sorting them into categories is quicker.

### Part 1: Overview, hosts, inputs and producers

Research the `$DATASET` dataset, current version only; mention `$RELATED` only to say how they differ. Where
is it stored and served: every repository, mirror, cloud copy and group website that holds a copy, with URLs,
and which one is the archive of record? What kind of dataset is it (one instrument or platform, a compilation
of station networks, or a blend of satellites, gauges and other datasets)? Name each input (networks,
satellites and sensors, datasets, ancillary or reanalysis fields) with its dates and share where published,
and say how the inputs are combined, which values are measured directly and which come from algorithms, and
how often it is updated. Which organizations produce, process, host and pay for it, and what does each do,
including cooperative institutes, contractors and other outside groups? Leave quality control, people,
funding amounts, and any cuts or threats to later parts. Tag findings with RRS-1, D-2, DIRS-3 or DIRS-4.

### Part 2: Processing, quality control, calibration, code and formats

Using Part 1's record, how is `$DATASET` processed and quality-controlled: the checks, whether automated or
manual, how flags work, and who does each step, including checks done by input providers before the data
arrive? What calibration does it depend on, such as instrument calibration labs, reference standards,
calibration against a reference sensor or dataset, or intercomparison programs, and who runs each? What
software, algorithms and computing facilities produce it, who owns and runs them, and does any step need
facilities outside the producer's control? For each piece of code, is it published (where, under what
license), only described in papers, or unpublished, and is the documentation detailed enough for a newcomer
to reproduce the dataset? Rate each format and access route FAIR, partly FAIR or non-FAIR, and say whether
any needs proprietary software. Leave cuts and threats to later parts. Tag findings with D-4, P-3, DIRS-1 or
DIRS-4.

### Part 3: People, team and the funding route

Using Parts 1 and 2, who are the people critical to producing and quality-controlling `$DATASET` now (its
principal investigators, developers and maintainers), with each one's role, employer, whether still active,
ORCID iD and earliest publication year? For each, estimate age (earliest publication year minus 25–30) and
whether they are likely eligible to retire within 2 years under their employer's rules (for US federal staff,
FERS), and mark estimates as estimates. How big is the team, how long has it existed, who could step in if one
person left, and is there any written succession, workforce or knowledge-transfer plan? How is the work paid
for: each route (appropriation line, program, grant, cooperative agreement or contract), with award numbers,
amounts and years where published, and which people depend on each route? Leave cuts, layoffs and news from
2025 on to Part 4. Tag findings with P-1, P-2, P-4 or D-1.

### Part 4: Threats to the dataset, its producers and its hosts

Using Parts 1–3 and `$SHARED_RUNS`, has funding for `$DATASET`, the groups that produce it and the systems
that serve it been stable, cut or threatened between January 1, 2025 and `$NOW`, including proposed
termination or retirement of the dataset or its products and budget uncertainty? What layoffs, buyouts,
hiring freezes, reorganizations or contract changes have affected the people and groups that produce or
serve it? Has the dataset or its access systems faced outages, access limits, removal, alteration or
political pressure? What news from 2024 to `$NOW` names the dataset, its group or its people, and does each
item name them directly or only the parent agency? Rate each development imminent, emerging or no current
threat found; count agency-wide actions only where a source ties them to this dataset; and say what each
could mean for its updates and availability. Tag findings with D-1, D-3, D-5, RRS-4, P-2 or P-4.

### Part 5: Threats to its inputs, and alternatives

Using Parts 1 and 2 and `$SHARED_RUNS`, which of `$DATASET`'s inputs (networks, satellites and sensors,
input datasets, ancillary fields, calibration facilities, and the organizations that run them) faced funding
cuts, termination, end of life, operational disruptions or news about these between January 2024 and `$NOW`?
Check `$CANDIDATES` without assuming any is affected, and spend most of the time on inputs the shared runs
didn't cover. For each affected input: what happened and when; whether it is enacted, proposed or reversed;
what share of the dataset it supplies; and whether the dataset's own record shows the effect. If an input
failed, is there a replacement, a backup source or a substitute, and which datasets could replace
`$DATASET` itself? Rate each input, and the inputs overall, imminent, emerging or no current threat found.
Tag findings with DIRS-1, DIRS-2, DIRS-3 or DIRS-5.

### A2 (shared): repository resilience, one per repository

How resilient is `$REPOSITORY` as a home for data? Does it hold copies at two or more geographically
separate sites and check them against each other? How often does it run fixity or checksum checks, and is
it certified (CoreTrustSeal or ISO 16363)? Does it have a disaster recovery or continuity-of-operations
plan, when was the plan last tested, and with what results? What are its storage and backup design and its
access systems (portals, APIs, cloud copies), and who pays for and staffs them? Through which past funding,
leadership or physical disruptions has it kept or lost data, and how did its holdings and ingest delays look
before and after? Leave budget cuts and news from 2025 on to the `$REPOSITORY` threats run (A1). Tag
findings with RRS-1, RRS-2, RRS-3, RRS-5, D-2 or D-3.

## Where each subcategory is answered

| Subcategory | Part 1 | Part 2 | Part 3 | Part 4 | Part 5 | Shared |
|---|---|---|---|---|---|---|
| P-1 Succession plan | | | **main** | | | |
| P-2 Retirement-eligible | | | **main** | staff losses | | |
| P-3 Undocumented knowledge | | **main** | supports | | | |
| P-4 Single point of failure | groups | | **main** | staff losses | | |
| D-1 Defunding | | | funding route | **main** | | A1 |
| D-2 Storage single point | who serves it | | | | | **A2** |
| D-3 Access fragile | | | | **main** | | A2 |
| D-4 Format obsolescence | | **main** | | | | |
| D-5 Political sensitivity | | | | **main** | | |
| DIRS-1 Calibration | | **main** | | | threats | |
| DIRS-2 Networks and platforms | input list | | | | **main** | A4 |
| DIRS-3 Upstream supply chain | input list | | | | **main** | |
| DIRS-4 Outside processing | outside groups | **main** | | | | |
| DIRS-5 No alternative | | | | | **main** | |
| RRS-1 Geographic redundancy | copies listed | | | | | **A2** |
| RRS-2 Checksums | | | | | | **A2** |
| RRS-3 Disaster recovery | | | | | | **A2** |
| RRS-4 Stable funding | | | | **main** | | A1 |
| RRS-5 Track record | | | | | | **A2** |

## Datasets already researched

Don't rerun these. Map the existing runs to the parts, categorize, and run only what is missing.

| Dataset | Part 1 | Part 2 | Part 3 | Part 4 | Part 5 | Missing |
|---|---|---|---|---|---|---|
| GHCN-Daily | pt1 | pt2 | funding-pt3 | threats-news-pt4 | sources-pt5 | Gap runs pt7 (repository, 2026-11-22) and pt8 (infrastructure, 2026-11-23) are done. Still to run: pt6 (people) and the NCEI A2 run, which replaces pt9 |
| GPCP Daily | pt1 | qc-formats-pt2 | people-pt3 | funding-news-pt4 | inputs-pt5, satellites-pt6 | P-2 ages, DIRS-1 calibration labs, A2 runs for NCEI and GES DISC |
| PERSIANN-CDR Daily | pt1 | qc-formats-pt2 | none | pt3 (funding), news-pt4 | inputs-pt5, satellites-pt6 | A Part 3 run (people), DIRS-1, A2 for NCEI |
| IMERG Late Run | pt1 | processing-qc-pt2, formats-people-pt3 | partly in pt3 | funding-pt4, news-pt5 | inputs-pt6 | P-2 ages, A1 and A2 for NASA PPS and GES DISC |

The supplemental queries for GPCP, IMERG and PERSIANN-CDR (written 2026-11-23 from coverage checks) are listed in
`datasets-gap-queries/supplemental-queries-run-sheet.md`: one "people and production" run per dataset, plus the NASA
GES DISC and PPS and the CHRS A2 runs.

The newest runs (GHCN-Daily pt7 and pt8, IMERG inputs-pt6) are in `Rstar_query_results/web_search_results/` but not
yet in this project's `rstar-pipeline/input/web-research/`.

For the next new dataset, write the five parts from the drafts above, and the A1 and A2 runs for any
repository that doesn't have them yet.

## How to run them

1. **One session** rewrites all five drafts with `/my:rewrite-research-query`, passing the five files at once.
   This is what the GHCN-Daily gap run sheet did. The rewrite can name earlier run folders only after they
   exist, so rewrite Parts 4 and 5 again after Parts 1–3 run if you want them to build on those records.
2. **Five research sessions**: Part 1 first; then Parts 2, 3 and 5 in any order; Part 4 last.
3. Shared runs (A1, A2, A4) go once per repository or instrument family, before the dataset's Part 4 or 5.

## Open choices

- **Part 3's limits.** 40 min / 320,000 assumes that the ORCID lookups and the funding route need more room
  than a standard run has. If the first Part 3 stops well under the ceiling, drop it to 30 min / 240,000.
- **Tagging cost.** Asking for subcategory tags adds a little writing to each answer. If it crowds out
  findings, drop the tags and sort the findings by hand, as now.
- **Station versus satellite wording.** Part 5's `$CANDIDATES` and Part 2's calibration examples differ by
  dataset type. A gauge network needs calibration labs and field technicians. A satellite blend needs
  calibration against a reference sensor (such as GPM's GMI) and the groups that run that calibration.
