# PERSIANN-CDR Daily gaps Part 7: People and production R* Query for Claude

About dataset = PERSIANN-CDR Daily Part 7, gaps in People risk (P-1 to P-4), funding of production (D-1),
calibration (DIRS-1), inputs (DIRS-3), outside processing (DIRS-4), alternatives (DIRS-5) and copies (RRS-1)

Written 2026-11-23 from [persiann-cdr-daily_coverage-gaps.md](../persiann-cdr-daily_coverage-gaps.md), a coverage
check of PERSIANN-CDR Daily's six runs. No earlier run was about its people. Rewrite this with
`/my:rewrite-research-query` (see [supplemental-queries-run-sheet.md](../supplemental-queries-run-sheet.md)), then run
the rewritten query with `/my:broad-web-research` in its own session. Repository resilience for NCEI is in the shared
NCEI A2 run, and for UC Irvine's CHRS data site in its own A2 run.

## Query to refine

Using the earlier runs' records on PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using
Artificial Neural Networks – Climate Data Record) (2026-11-19_persiann-cdr-daily-about-pt1,
2026-11-19_persiann-cdr-daily-qc-formats-pt2, 2026-11-19_persiann-cdr-daily-about-pt3,
2026-11-19_persiann-cdr-daily-news-pt4, 2026-11-19_persiann-cdr-daily-inputs-pt5 and
2026-11-19_persiann-cdr-daily-satellites), all in web_search_results/, who are the people critical to producing
PERSIANN-CDR Daily now at UC Irvine's Center for Hydrometeorology and Remote Sensing (CHRS), how close is each to
retirement, who runs and pays for the quarterly extension, what does its calibration rest on today, and which of its
copies are current? Add to what those runs found rather than repeating it.

- **People (P-1, P-2, P-4):** start from Soroosh Sorooshian (PI, CHRS founding director), Kuolin Hsu (C-ATBD lead
  author), Phu Nguyen (associate director), Amir AghaKouchak (director by April 2026), Dan Braithwaite (`creator_name`
  in the file metadata, not on the current CHRS directory) and Mojtaba Sadeghi, confirming each by affiliation and
  PERSIANN co-authorship. For each: current role and whether still active on PERSIANN-CDR; ORCID iD; earliest
  publication year (say from which source); first year on PERSIANN; and estimated age (earliest publication year minus
  25–30). Mark estimates as estimates. Also: when the directorship changed and why; who runs the quarterly extension
  today and whether it is one person; the CHRS team's size and how long it has existed; any written succession or
  knowledge-transfer plan.
- **Paying for production (D-1):** who has paid for the quarterly extension since the CDR Program's build money ended
  in 2014; whether NA23OAR4310443 (ended August 31, 2026) has a successor; what the terminated NOAA "incoming subaward"
  at UCI was; whether Kuolin Hsu's CISESS role (funding listed as "LEO") supports the extension.
- **Production (P-3, DIRS-4):** whether CHRS's current code differs from the public 2014 package
  (SourceCode_01B-16.tar.gz) and whether the training code is published; what computers produce it, who pays for them,
  and the dependence on MATLAB, which is commercial.
- **Calibration and inputs (DIRS-1, DIRS-3):** whether the months from 2024 on use the GridSat-B1 data recalibrated
  against VIIRS VGAC (C-ATBD Rev 2, March 2026); who at NCEI maintains GridSat's calibration (K. R. Knapp is the author);
  which GPCP monthly version adjusts which years (file headers say `gpcp_m` to April 2015 and `gpcpv23_m` from July
  2015, which conflicts with a claim that 2009–2013 were replaced); whether GPCP v2.3 will be frozen, now that V3.3
  supersedes it, and whether CHRS plans to switch.
- **Alternatives (DIRS-5):** which datasets could replace PERSIANN-CDR Daily as a long daily satellite record, with
  coverage and status. Note that GPCP V3.3 takes PERSIANN as an input, so it is not an independent substitute.
- **Copies (RRS-1, D-3):** whether the AWS bucket (`s3://noaa-cdr-precip-persiann-pds/`), the Azure copy, Google Earth
  Engine (`NOAA/PERSIANN-CDR`, to July 31, 2026), the IRI/LDEO Data Library (possibly frozen at September 2019) and the
  Data Rescue Project copy (April 24, 2025) are current; the cause and current status of NCEI's "pause in operations"
  notice for PERSIANN-CDR (ncei.noaa.gov/node/8306).

For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel
retirement-eligible within 2 years", P-3 "critical knowledge undocumented", P-4 "a single person is a point of
failure", D-1 "program defunded or under threat", DIRS-1 "depends on an external calibration service that could be
disrupted", DIRS-3 "upstream data feeds vulnerable", DIRS-4 "needs outside processing infrastructure", DIRS-5 "no
alternative supplier" or RRS-1 "two or more geographically independent sites hold verified copies" (RRS-1 is a
strength, so "supports" means resilience). Say so where nothing is published. Use CHRS's, UC Irvine's and NOAA's own
pages, award databases (USAspending, NSF award search), papers, and ORCID or OpenAlex records ahead of news. With a time
limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** Cuts and news are in pt3 and pt4, which found nothing aimed at the dataset. Asking who
  pays now is a fact-finding question.
- **No federal retirement rule applies.** CHRS staff are University of California employees. Give estimated ages and
  say whether a UC retirement plan rule is published; don't apply FERS.
- **Where to find ORCID iDs and earliest publication years:** ORCID (orcid.org, pub.orcid.org), OpenAlex
  (api.openalex.org), Google Scholar, Crossref, UC Irvine faculty pages and eScholarship.
- **These people are shared with IMERG.** CHRS supplies IMERG's PDIR-Now method, so IMERG's Part 7 can cite this run.
- **Already found, don't search again (from the coverage check):**
  - no staff count is published; the CHRS directory lists 4 faculty, 4 postdocs, 1 administrator, 11 graduate students
    and 2 visitors, and calls CHRS "an informal interdisciplinary group" (pt1, pt3);
  - full documentation is public: C-ATBD CDRP-ATBD-0286 Rev 2, User Guide CDRP-GUID-1665, Data Flow Diagram
    CDRP-DIA-0351; NCEI's stewardship assessment (NOAA IR 33336, 2020) scores QC 1.5, "Procedure not documented" (pt2);
  - processing runs locally at CHRS; QC is automated at CHRS (pt1, pt2);
  - the funding history through 2014 and the CHRS grants table: NA09NES4400006 (with CICS sub-award 2009-1380-01),
    NA10DAR4310122, NA23OAR4310443, 80NSSC23K0136, 80NSSC21K1668; NSF grant 2332263 was terminated and then reinstated
    (pt3);
  - GridSat-B1's calibration moved from HIRS (ended 2024) to VIIRS VGAC; each month is bias-adjusted to GPCP (pt2, pt5);
  - the satellites, their periods and their 2024–26 status (satellites run, pt5).

### What the answer should give

- A table of people: role, active or not, ORCID iD, earliest publication year and its source, and estimated age.
- When the director changed, who runs the extension, the team size, and any succession plan.
- Who pays for the extension now, with award numbers and dates.
- Whether the code has changed since 2014, and what computers and software production needs.
- The current calibration of GridSat and the GPCP version for each period.
- Substitute datasets.
- A table of copies: last date, and whether current; and the NCEI pause notice's cause and status.
- A stance for each finding against the subcategory statements.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
