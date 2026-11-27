# PERSIANN-CDR Daily gaps Part 7: People and production R* Query for Claude

About dataset = PERSIANN-CDR Daily Part 7, gaps in People risk (P-1 to P-4), funding of production (D-1),
calibration (DIRS-1), inputs (DIRS-3), outside processing (DIRS-4), alternatives (DIRS-5) and copies (RRS-1)

Written 2026-11-23 from a coverage check of PERSIANN-CDR Daily's six runs. No earlier run was about its people. Rewrite
this with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Repository resilience for NCEI is in the shared
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

### Run 1: people, funding and production

/my:broad-web-research

Using the earlier runs' records on PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record) (2026-11-19_persiann-cdr-daily-about-pt1, 2026-11-19_persiann-cdr-daily-qc-formats-pt2, 2026-11-19_persiann-cdr-daily-about-pt3, 2026-11-19_persiann-cdr-daily-news-pt4, 2026-11-19_persiann-cdr-daily-inputs-pt5 and 2026-11-19_persiann-cdr-daily-satellites, all in web_search_results/), who are the people critical to producing PERSIANN-CDR Daily now at UC Irvine's Center for Hydrometeorology and Remote Sensing (CHRS), how close is each to retirement, and who runs and pays for the quarterly extension, on what computers? Add to what those runs found rather than repeating it.

- **People:** start from Soroosh Sorooshian (PI, CHRS founding director), Kuolin Hsu (C-ATBD lead author), Phu Nguyen (associate director), Amir AghaKouchak (director by April 2026), Dan Braithwaite (`creator_name` in the file metadata, not on the current CHRS directory) and Mojtaba Sadeghi, confirming each by affiliation and PERSIANN co-authorship. For each: current role and whether still active on PERSIANN-CDR; ORCID iD; earliest publication year and its source; first year on PERSIANN; estimated age (earliest publication year minus 25–30), marked as an estimate. CHRS staff are University of California employees: say whether a UC retirement rule is published, and don't apply federal rules.
- **Team and succession:** when and why the directorship changed; who runs the quarterly extension today and whether it is one person; how long CHRS has existed; any written succession or knowledge-transfer plan.
- **Who pays:** what has paid for the extension since the CDR Program's build money ended in 2014; whether NA23OAR4310443 (ended August 31, 2026) has a successor; what the terminated NOAA "incoming subaward" at UCI was; whether Kuolin Hsu's CISESS role (funding listed as "LEO") supports the extension; whether NOAA contract ST133017CQ0058 (Riverside) has an order for CHRS.
- **Production:** whether CHRS's current code differs from the public 2014 package (`SourceCode_01B-16.tar.gz`) and whether the training code is published; what computers produce the extension and who pays for them; its dependence on MATLAB, which is commercial.

The earlier runs already have the CHRS directory counts, the public C-ATBD, User Guide and Data Flow Diagram, NCEI's 2020 stewardship scores, local processing and automated QC at CHRS, and the grants table (NA09NES4400006, NA10DAR4310122, NA23OAR4310443, 80NSSC23K0136, 80NSSC21K1668, NSF 2332263); build on them. For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel retirement-eligible within 2 years", P-3 "critical knowledge undocumented", P-4 "a single person is a point of failure", D-1 "program defunded or under threat" or DIRS-4 "needs outside processing infrastructure", and say so where nothing is published. This asks who does and pays for the work now; cuts and news are in pt3 and pt4. Use CHRS's, UC Irvine's and NOAA's own pages, award databases (USAspending, NSF award search), papers, eScholarship and ORCID or OpenAlex records ahead of news, and check ORCID against one other source. With a time limit of 40 minutes and a token ceiling of 320,000.

### Run 2: calibration, alternatives and copies

/my:broad-web-research

Using the same earlier runs' records on PERSIANN-CDR Daily and the NCEI resilience run (2026-11-23_A2_Rstar_query-noaa_ncei), all in web_search_results/, what does PERSIANN-CDR Daily's calibration rest on today, what could replace it, and which of its copies are current? Add to what those runs found rather than repeating it.

- **Calibration and inputs:** whether the months from 2024 on use GridSat-B1 data recalibrated against VIIRS VGAC (C-ATBD Rev 2, March 2026), and who at NCEI maintains GridSat's calibration (K. R. Knapp is its author); which GPCP monthly version adjusts which years (file headers say `gpcp_m` to April 2015 and `gpcpv23_m` from July 2015, which conflicts with a claim that 2009–2013 were replaced; explain it); whether GPCP v2.3 will be frozen now that V3.3 supersedes it, and whether CHRS plans to switch.
- **Alternatives:** which datasets could replace PERSIANN-CDR Daily as a long daily satellite record, with coverage, resolution and status. GPCP V3.3 takes PERSIANN as an input, so don't count it as an independent substitute.
- **Copies:** for each, the last date it holds and whether it is current: the IRI/LDEO Data Library (possibly frozen at September 2019) and the Data Rescue Project copy (April 24, 2025); and the cause and current status of NCEI's "pause in operations" notice for PERSIANN-CDR (ncei.noaa.gov/node/8306). CHRS's own data site is covered by its A2 run.

For each finding, say whether it supports or contradicts DIRS-1 "depends on an external calibration service that could be disrupted", DIRS-3 "upstream data feeds vulnerable", DIRS-5 "no alternative supplier" or RRS-1 "two or more geographically independent sites hold verified copies" (RRS-1 is a strength, so "supports" means resilience), and say so where nothing is published. Use the C-ATBD, the file headers, NOAA's own pages and the hosts' own catalogs ahead of news. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:**
- **Run 1 (people, funding, production):** a row per person (role, active or not, ORCID iD, earliest publication year and its source, first PERSIANN year, estimated age, and whether a UC rule is published), when and why the director changed, who runs the extension, any succession plan, who pays for the extension now with award numbers and dates (or a plain "not published"), whether the code has changed since 2014 and what computers and software production needs, and a stance on P-1 to P-4, D-1 and DIRS-4.
- **Run 2 (calibration, alternatives, copies):** whether 2024-on months use the VGAC recalibration, the GPCP version for each period with the conflict explained, the outlook for GPCP v2.3, substitute datasets, the last date of each copy, the cause of NCEI's pause notice, and a stance on DIRS-1, DIRS-3, DIRS-5 and RRS-1.

**What I changed from your draft:**
- **Split into two runs.** People and funding live in ORCID, UC pages and award databases; calibration and copies live in the C-ATBD, file headers and catalogs. No earlier run covered CHRS's people, so Run 1 starts from less than the GPCP and IMERG people runs do. Neither run needs the other, so either order works.
- **"Already found" folded into one sentence** in Run 1, so the run builds on pt1–pt5.
- **"CHRS team size" narrowed** to how long CHRS has existed: the directory counts are already in pt1 and pt3.
- **Added one lead** to "Who pays": NOAA contract ST133017CQ0058 (Riverside), which pt3 left open as a possible route for CHRS. Drop it if you'd rather not.
- **The retirement rule** (UC, not FERS) is in the question itself, as your context asked.
- **Run 2 names the NCEI A2 run,** which already covered NCEI's own copies.
- **Copies on blocked hosts left out:** the AWS bucket, the Azure copy and Earth Engine. Their hosts aren't in `.claude/settings.local.json`.
- **Standard tier:** Run 1 says it asks who pays now, with cuts and news left to pt3 and pt4. "Terminated subaward" and D-1 are the words most likely to push the skill toward deep; if they do, the limits still hold.

**Limits:** Run 1 has 40 minutes and 320,000 tokens (6 people, plus funding questions pt3 couldn't settle). Run 2 has 30 minutes and 240,000.

**One-run version:** put all seven bullets under Run 1's opening question, with all ten statements, at 40 minutes and 320,000 tokens (your draft's limits). It gives up depth on the calibration and copies: the people and funding lookups would take most of the time.

**Hosts:** every host the questions name is allowed: IRI/LDEO (columbia.edu), UC Irvine, NSF, NOAA and USAspending under the `.edu` and `.gov` rules, plus datarescueproject.org, escholarship.org, ORCID and OpenAlex.

**Order and reuse:** run both in this project, after the six PERSIANN-CDR runs (all done). Don't add "Don't use earlier runs."; both depend on them. Run 1 before IMERG's Part 7 Run 1 if you want IMERG to cite it for PDIR-Now's method.
