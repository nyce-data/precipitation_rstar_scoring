# R* categorization decisions

As of 2026-11-23. **This local file is the current version**: make every change here. It started as the Claude Doc
[R* categorization decisions](https://claude.ai/artifact/ESJV1iYjXaoWyHjgEyZ6X6), which is no longer updated. No Word
copy is kept in the repo; make one when needed, for example
`pandoc rstar-categorization-decisions.md -o rstar-categorization-decisions.docx` (run in this folder).

## Purpose

These are the rules agreed so far for sorting web research on precipitation datasets into the 19 R* subcategories,
and for scoring them. The R* formula and point values are fixed; these rules decide how evidence is filed and when a
subcategory gets its points. This doc is updated as decisions change.

The examples come from GHCN-Daily, the first dataset categorized (three passes, 210 evidence items). The questions and
answers behind these decisions are kept as a record in the project's `notes/claude_feedback/` folder
([why-rstar-categories-are-hard-to-apply.md](why-rstar-categories-are-hard-to-apply.md) and its
[follow-up](why-rstar-categories-are-hard-to-apply_follow-up.md)). Points still to settle are in the last section.

## The R* framework

R* combines four group totals, and each total is the sum of its subcategory scores. The formula is fixed, and no
subcategories can be added.

```latex
R^* = 0.40\,D + 0.30\,P + 0.20\,(100 - RRS) + 0.10\,DIRS
```

Each subcategory scores either 0 or its points. P, D and DIRS statements describe risks, so "for" adds risk. RRS
statements describe resilience, so "for" raises RRS, and (100 − RRS) turns that into lower risk.

| Group | Code | Statement | Points |
| --- | --- | --- | --- |
| Data risk (D) | D-1 | Active or threatened program termination or defunding | 30 |
| Data risk (D) | D-2 | Storage system end-of-life or single point of failure | 25 |
| Data risk (D) | D-3 | Access infrastructure fragile or unfunded | 20 |
| Data risk (D) | D-4 | Format obsolescence | 15 |
| Data risk (D) | D-5 | Political sensitivity | 10 |
| People risk (P) | P-1 | No documented succession plan | 35 |
| People risk (P) | P-2 | Key personnel retirement-eligible within 2 years | 25 |
| People risk (P) | P-3 | Critical undocumented knowledge | 25 |
| People risk (P) | P-4 | Single person is point of failure | 15 |
| Dependent infrastructure (DIRS) | DIRS-1 | Calibration facility dependency | 25 |
| Dependent infrastructure (DIRS) | DIRS-2 | Observation network or sensor platform at risk | 25 |
| Dependent infrastructure (DIRS) | DIRS-3 | Upstream data supply chain at risk | 20 |
| Dependent infrastructure (DIRS) | DIRS-4 | External processing infrastructure dependency | 15 |
| Dependent infrastructure (DIRS) | DIRS-5 | No alternative supplier | 15 |
| Repository resilience (RRS) | RRS-1 | At least 2 geographically independent sites hold verified copies | 25 |
| Repository resilience (RRS) | RRS-2 | Checksum checks quarterly or more often | 20 |
| Repository resilience (RRS) | RRS-3 | Disaster recovery plan tested in the past 2 years, with documented results | 20 |
| Repository resilience (RRS) | RRS-4 | Stable institutional funding | 20 |
| Repository resilience (RRS) | RRS-5 | Track record through a prior disruption without data loss | 15 |

## Scope of each group

Each group has one scope sentence that says which facts belong to it. A fact can fit more than one group and is then
filed in each.

| Group | Scope |
| --- | --- |
| People risk (P) | The people who produce this dataset: its own team, including contractors, at the producer. Staff losses at the wider agency, or at a source network, are context here unless a source names this team. Losses at a source network can still count in DIRS-2. |
| Data risk (D) | The dataset as a product and the places that serve it: the programs that produce and host it, where it is stored and how users reach it (including the repository going offline), its formats, and political pressure on it. |
| Dependent infrastructure resilience (DIRS) | What the dataset needs in order to be produced: the instruments and observing networks that make its measurements, their calibration, the data feeds it is built from, and the processing that turns them into the dataset. Not where the finished dataset is stored or served. Substitutes for the dataset itself count in DIRS-5. |
| Repository resilience (RRS) | Each repository that holds a copy of the dataset, judged as an institution: its redundancy, integrity checks, disaster recovery, funding and track record. "For" means the repository is resilient. |

D-2 and D-3 cover both the dataset and its repository, because the dataset is served by the repository. If the
repository goes offline, the data goes offline. So the same repository fact often appears in D-2 or D-3 and in RRS.

## What counts as evidence

A fact counts as "for" or "against" only if a source names the dataset, or something on its documented source list,
input list or team. A fact one step removed is kept as context: it helps a person judge the score but does not set it.

| Kind of fact | GHCN-Daily example | How it is filed |
| --- | --- | --- |
| Agency-wide loss at the producer, with no team named | NCEI's 58 staff departures in 2025; no source ties them to the GHCN-Daily team | Context |
| Loss at the agency that runs a source | NWS-wide technician losses; NWS runs COOP and ASOS, both GHCN-Daily sources | Counts (DIRS-2) |
| Fact about the repository | NCEI's offsite tape copy is 12.5 miles from Asheville | Counts in D-2, D-3 and RRS, since the repository holds the dataset |
| A source of a compilation stops | GSOD, one of GHCN-Daily's input feeds, ended in August 2025 | "For", whatever the source's size |
| Proposed cut, still pending | USCRN's maintaining lab (ARL) proposed for closure again for FY2027 | "For", the same as an enacted cut |
| Proposed cut that was rejected | ARL's closure proposed for FY2026 and rejected by Congress | Context |
| Sources that disagree | OIG-24-034-A recommendations "open" (September 2025) vs "Closed" (Oversight.gov) | Both kept; the subcategory is NA and a person decides |
| Event before the 2025-to-present window of D-1 and RRS-4 | Hurricane Helene (September 2024); FY2020–2024 budgets | Context in D-1 and RRS-4; counts in RRS-5 (track record) |
| An inference made while sorting | P-2 age estimates from earliest publication year | Kept, labelled "inference", low confidence |

**Repeating facts.** A fact goes in every subcategory it bears on, with no cross-references. For example, NCEI's
FY2027 request, 25% below its base, appears in D-1, D-3 and RRS-4. R* is a starting score for judging a dataset, not
an exact split, so this is accepted.

**Producer and repository the same.** When one organization produces and holds the dataset (NCEI for GHCN-Daily), its
facts are repeated like any others. The dataset's landing page says so in a separate sentence.

**Data quality.** R* assumes the data are of good quality, so there is no quality subcategory. QC-process facts are
filed where they show a risk: QC only one person can run goes to P-3 or P-4, QC on outside systems to DIRS-4.
Otherwise they are context. Signs of a drop in quality are filed by cause: a lost network in DIRS-2, lost calibration
in DIRS-1, an outage in D-2 or D-3.

Worked "counts / doesn't count" examples for each subcategory are in a separate guide for whoever categorizes, the
"Counts / doesn't count" section of `rstar-pipeline/processing/instructions/categorizing-web-searches_README.md`, not in the definition files.

## How evidence is tagged

Each dataset has one JSON file. Each subcategory in it holds an Evidence list and a Gaps list, plus its score and
status. Every evidence item carries the tags below.

| Tag | Values | Meaning |
| --- | --- | --- |
| Stance | for, against, context | How the item bears on the subcategory's statement. "Context" (formerly "neutral") is background that is not directly tied, or does not show the statement true or false |
| Confidence | high, moderate, low | How well the source supports the item. Inferences are always low |
| Source | research run folder | Which web research run the item came from |
| Status | found; searched and none found; not public; not searched | Every evidence item is "found". Each Gaps item gets one of the other three. Each subcategory shows a summary status |
| Repository | the repository's name | RRS items only: which repository the item is about |

A fact that exists but is withheld is both. For example, NCEI's disaster-recovery plan "cannot be shared outside the
US Government": the plan's existence is a found item (context), and whether it was tested is a "not public" gap.

## How a subcategory is scored

Only high- and moderate-confidence "for" and "against" items set a score. Low-confidence items stay in the list,
tagged low, but are left out of the score. Context items are ignored.

| High or moderate evidence | Score |
| --- | --- |
| "For" items and no "against" items | Full points |
| "Against" items and no "for" items | 0 |
| Both "for" and "against" items | NA |
| None: only context, only low confidence, or no evidence | NA |

NA means there is not enough information to decide, and a person must choose. They may know things a web search
cannot find, such as what they have been told directly. A group total is NA if any of its subcategories is NA, and R*
is NA if any group total is NA. The score is stored in each dataset's JSON file.

GHCN-Daily, re-sorted under these rules on 2026-11-23, has 17 subcategories at NA and RRS-2 and RRS-3 at 0, so its R*
is NA. P-2 is NA because its one moderate "for" item, NCEI-wide retirements, became context; the items left on either
side are low-confidence estimates.

This decision table may change once users have seen the results.

## Repositories

RRS gives one pooled verdict across all of a dataset's repositories. Each RRS item names the repository it is about.
If one repository has "for" evidence and another has "against" evidence, the subcategory is NA. Each RRS card says
whether the dataset has one repository or several.

A place counts as a repository only if it serves the dataset in its original format with its metadata.

| Kind of place | Example | Counts? | Why |
| --- | --- | --- | --- |
| Archive of record | NCEI for GHCN-Daily | Yes: the parent repository | Holds and serves the original |
| Copies and mirrors | AWS `noaa-ghcn-pds`, Google BigQuery | Yes: child repositories | Serve copies of the original |
| Producer's own site | NASA PPS's site for IMERG, next to GES DISC | Yes | Serves the original |
| Volunteer snapshot | Data Rescue Project | No | May hold only the data file, without its metadata |
| Third-party reformatted copy | dynamical.org Zarr, Google Earth Engine | No | Not the original format, and the metadata may not be kept |

Metadata matters because a dataset's landing page often carries information, as text, images and a download link,
that the data file itself may not contain.

## How the website shows it

The categorization website shows the scores alongside the evidence, with NA wherever a person must decide (built
2026-11-23; the web form and the graph are not built yet).

- **Each dataset's landing page** has an "R* categorizations" section with the total R* and the four group scores,
  each a number or NA. A "Score details" panel opens to show every subcategory's score.
- **A key at the top of each landing page** explains the tags and how scores were set, so users can suggest a
  different decision table.
- **Same producer and repository:** when one organization is both, the landing page says so in a sentence of its own.
- **Each subcategory card** shows its score clearly, not in gray.
- **Each RRS card** says whether the dataset has one repository or several.

Later, a web form will let users enter the final scores. The research fills in what it can, and NA items are marked as
needing a decision. In the planned network graph, an NA node is drawn in black with the value NA.

## Still open

These points are not settled. The current rule is used until they are.

- **What counts as a source of a compilation.** Is the unit a whole network (one of GHCN-Daily's source flags, such
  as CoCoRaHS or a national weather service), or does one station closing count? GHCN-Daily has over 100,000 stations
  and some close every year, so counting single stations would make DIRS-2 "for" for every compilation. For now, any
  source that stops counts as "for".
- **The scoring decision table.** Under the current table most subcategories of a well-researched dataset come out
  NA. It may change once users have seen the results.
- **Repeating facts when the producer is the repository.** Repeating NCEI's facts across subcategories may count the
  same evidence more than once. To be reviewed after more datasets are categorized.
- **Pooled RRS.** RRS gives one verdict for all repositories. Scoring each repository and weighting them by which copy
  users rely on is a possible later change.
