# PERSIANN-CDR Daily: what the research didn't search, by subcategory

- **Dataset:** PERSIANN-CDR Daily v01r01, a NOAA CDR (DOI 10.7289/V51V5BWQ, NCEI record C00854), made by UC Irvine's
  Center for Hydrometeorology and Remote Sensing (CHRS) from GridSat-B1 infrared, bias-adjusted to GPCP monthly.
- **Categorized:** 2026-11-27 (first pass), **before its pt7 people-and-production run** (the user chose to categorize
  now and add pt7 later with Prompt 5).
- **Output:** [persiann-cdr-daily_rstar-categories.json](../categories/persiann-cdr-daily/persiann-cdr-daily_rstar-categories.json),
  built by `rstar-pipeline/processing/scripts/categorize/build_persiann-cdr-daily.py` (100 evidence items).
- **Research used:**
  - `about-datasets/persiann-cdr-daily/`: about-pt1, qc-formats-pt2, about-pt3 (funding), news-pt4, inputs-pt5 and
    satellites-pt6;
  - `archives/noaa-ncei/`: the A1 threats run and the A2 resilience run (which covers PERSIANN-CDR by name);
  - `archives/uci-chrs/2026-11-27_uci-chrs-resilience` (CHRS's own data site);
  - `instruments/noaa-satellites` (GOES, DMSP, POES);
  - for NODD-wide and NCEI-wide facts only: GHCN-Daily's repository-pt7 and repository-resilience-pt9;
  - for one low-confidence inference on substitute datasets: GPCP Daily's calibration-copies-pt7.
- **Not used:** `instruments/nasa-satellites` (about GPM and IMERG; PERSIANN-CDR uses no NASA sensor directly, and
  Aqua AIRS, which reaches it through GPCP, is covered by inputs-pt5) and `instruments/noaa-rain-gauges` (gauges reach
  it only through GPCC inside GPCP).
- **Not yet run:** the pt7 query (`datasets-gap-queries/persiann-cdr-daily_gap-queries/persiann-cdr-daily-gaps_Rstar_query_pt7_people-production.md`,
  run sheet `datasets-gap-queries/supplemental-queries-run-sheet.md`). It asks about the people (P-1, P-2, P-4), who
  runs and pays for the quarterly extension (D-1), GridSat's calibration (DIRS-1), the GPCP version (DIRS-3), CHRS's
  computers (DIRS-4), substitutes (DIRS-5) and whether the cloud copies are current (RRS-1).
- **Coverage note:** `datasets-gap-queries/persiann-cdr-daily_coverage-gaps.md` (2026-11-23) listed what the gap runs
  should fill; this note replaces it for the categorization.
- **Shared people:** Braithwaite, Hsu, Nguyen and Sorooshian (CHRS) are also co-authors of IMERG's ATBD (CHRS's
  PDIR-Now is an IMERG input). GPCP V3.3 takes PERSIANN data as an input, and PERSIANN-CDR takes GPCP v2.3.

## Repositories (the JSON's `dataset` key)

| Repository | Role | Holds |
|---|---|---|
| NOAA NCEI | parent | Archive of record and distributor (HTTPS, THREDDS, ERDDAP); archived in Asheville |
| UC Irvine CHRS data site | producer site | CHRS's own copy (portal, HTTPS and FTP; raw `.bin.gz` daily files, monthly and yearly) |
| AWS, Google Cloud and Azure (NODD) | child | NCEI's copies (`s3://noaa-cdr-precip-persiann-pds/`, Azure `precip-persiann`) |

Not repositories: the Data Rescue Project's April 2025 snapshot (16 GB), Google Earth Engine (reformatted) and the
IRI/LDEO Data Library (its own data services, now behind a sign-in, possibly frozen at September 2019). CHRS serves
its own copy, but NCEI is the archive of record, so `producer_is_repository` is false (the site would otherwise say
the producer and repository are one organization, as it does for IMERG, where Goddard is both).

## Scores

| Subcategory | Items (for / against / context) | Score | Main reason |
|---|---|---|---|
| P-1 Succession plan | 1 / 1 / 2 | **0** | Full handover package public at NCEI (C-ATBD, data flow diagram, user guide, production code); the one "for" (Braithwaite gone) is low |
| P-2 Retirement-eligible | 0 / 0 / 2 | NA | Not searched (pt7) |
| P-3 Undocumented knowledge | 2 / 2 / 2 | NA | QC procedure "not documented" and documents name the wrong GPCP version vs public code and C-ATBD |
| P-4 Single point of failure | 0 / 0 / 4 | NA | Who runs the quarterly extension was never searched |
| D-1 Program defunding | 1 / 1 / 7 | NA | Pending FY2027 cut to NCEI vs no cut found aimed at PERSIANN-CDR or CHRS |
| D-2 Storage single point | 3 / 1 / 1 | NA | Asheville-only archive, single-region cloud target, CHRS's servers with no backup published vs four organizations serving it |
| D-3 Access fragile | 6 / 0 / 2 | **20** | NCEI's November 2026 outage, NCEI's "pause in operations" notice, pending NCEI cut, CHRS's one-admin site and its 2024 outage and lag, NODD with no term |
| D-4 Format obsolescence | 0 / 1 / 3 | **0** | CF netCDF-4 on NCEI's routes, rated FAIR |
| D-5 Political sensitivity | 0 / 1 / 2 | **0** | About 120 searches found nothing naming PERSIANN-CDR |
| DIRS-1 Calibration | 2 / 0 / 3 | **25** | GridSat-B1's HIRS calibration source ended in 2024; bias-adjusted to a superseded GPCP v2.3 |
| DIRS-2 Observation platforms | 3 / 0 / 5 | **25** | Ageing Meteosat-9/-10 with no MTG in ISCCP B1; DMSP F17 SSMIS and Aqua AIRS (through GPCP) |
| DIRS-3 Upstream supply chain | 2 / 0 / 4 | **20** | GPCP v2.3 "Version Superseded" with no plan to move; V3.3 itself uses PERSIANN data |
| DIRS-4 External processing | 0 / 1 / 3 | **0** | CHRS produces it on its own servers (2019 paper) |
| DIRS-5 No alternative supplier | 1 / 1 / 3 | NA | No fallback input named vs geostationary backups already used |
| RRS-1 Geographic redundancy | 1 / 4 / 1 | NA | NCEI, CHRS and the cloud copies in separate places vs Asheville-only archive, single-region cloud target, no check of NODD copies, no CHRS backup |
| RRS-2 Checksum verification | 0 / 3 / 2 | **0** | Checksums only at ingest and on order (DSMR-00012, CoreTrustSeal); none published at CHRS |
| RRS-3 Disaster recovery plan | 0 / 2 / 1 | **0** | NCCF can't test at alternate sites; no CHRS plan published; NCEI's plan not shareable |
| RRS-4 Stable funding | 1 / 5 / 0 | NA | FY2026 enacted vs pending FY2027 cut, NCEI staff losses, grant-funded School Center, no-term cloud copies |
| RRS-5 Track record | 3 / 2 / 2 | NA | Helene, the 2015 merger and CHRS's 2024 outage without reported loss vs 8% backlog unaccounted, 27 products retired |

People, data and repository totals are NA, so R* is NA (9 of 19 subcategories NA). DIRS is the only full total:
25 + 25 + 20 + 0 = 70 of 100.

## Judgment calls to double-check

- **P-1 = 0 rests on the handover package alone** (high "against": the C-ATBD, data flow diagram, user guide and the
  full 2014 code at NCEI), as GPCP's V1.3 package was filed. No search for a succession plan was made, and the package
  is from 2013–2014. Braithwaite's absence from the CHRS directory is filed low "for" because no one checked whether he
  still runs production or who took over. If you'd count his absence at moderate, P-1 becomes NA. pt7 will likely add
  a "for" or "against" here.
- **P-4 = NA:** "every production step is algorithmic" was filed as context, not "against", because it describes the
  algorithm, not who runs the quarterly batches (GHCN-Daily's "against" was an explicit "will continue to update
  automatically"). As "against", P-4 would be 0.
- **P-3 "for" items:** NCEI's 2020 stewardship score ("Procedure not documented or available" for QC monitoring) and
  the user guide naming GPCP v2.2 while the files use v2.3 were each filed moderate-to-high "for", which makes P-3 NA
  against the public code.
- **D-1:** the run's "no cut found aimed at PERSIANN-CDR or CHRS" is a moderate "against" for the producer side,
  which makes D-1 NA against the pending NCEI cut. CHRS's ended NOAA grant was filed as context because it paid for
  a different product (CCS-CDR v2).
- **D-3 = 20** counts NCEI's undated "pause in operations due to processing delays" notice as a high "for", though
  files kept arriving (2026-07-09, 2026-10-13).
- **D-4:** CHRS's headerless raw binary (rated non-FAIR) was filed as context, not "for": it needs no proprietary
  software, and NCEI's routes serve open netCDF.
- **DIRS-1:** GPCP monthly is treated as a calibration reference as well as an input (also in DIRS-3).
- **DIRS-2:** DMSP F17 and Aqua AIRS reach PERSIANN-CDR only through GPCP, so they are moderate "for" (GPCP Daily's
  precedent for satellites inside an input). The Meteosat item (direct input, but an "emerging" rating) is also moderate.
  GOES's 2032 spare gap is context, as for GPCP.
- **DIRS-4 = 0** comes from a 2019 statement that CHRS's servers produce it; nothing newer is published. MATLAB was filed
  as context, as GPCP's MATLAB code was not counted.
- **RRS-1 "for":** NCEI, CHRS and the NODD copies in separate places count as a moderate "for" though none is shown
  verified (the GPCP/IMERG precedent). CHRS's missing backup is a moderate "against" resting on silence.
- **RRS-4:** CHRS's ended grant counts here (the repository's own funding) though it is context in D-1.
- **Repository roles:** CHRS's site is a producer site (it serves the original data, though as raw binary rather
  than NCEI's netCDF); IRI is filed as not a repository.

## What the research never searched, by subcategory

### People risk (all in the pt7 query)
- **P-1:** a written succession or knowledge-transfer plan; the CHRS team's size and how long it has worked on
  PERSIANN; when and why the directorship changed.
- **P-2:** ORCID iDs, earliest publication years and estimated ages for Sorooshian, Hsu, Nguyen, AghaKouchak,
  Braithwaite and Sadeghi (FERS doesn't apply; they are university staff).
- **P-3:** whether CHRS's current code differs from the 2014 package; the training code. *Ask:* CHRS or
  PERSIANN_contacts@noaa.gov.
- **P-4:** who runs the quarterly extension and whether it is one person.

### Data risk
- **D-1:** what pays for the extension since 2014 (pt7; NCEI's CDR contact or CHRS); a successor to NA23OAR4310443;
  the FY2027 outcome.
- **D-2:** NCEI's AWS regions after the move; where CHRS's servers sit and whether they are backed up.
- **D-3:** the cause of NCEI's pause notice and CHRS's 2024 outage and lag; how CHRS's administrator is paid.
- **D-4:** CHRS's binary layout and terms of use.

### Dependent infrastructure resilience
- **DIRS-1:** whether the 2024–2026 months use the VIIRS-recalibrated GridSat-B1 (pt7); who maintains GridSat's
  calibration.
- **DIRS-2:** when MTG enters ISCCP B1; which DMSP satellites still deliver after 30 Sep 2026.
- **DIRS-3:** GPCP v2.3's retirement date and any plan for PERSIANN-CDR if it is frozen (pt7); the GPCP version per
  period.
- **DIRS-4:** the machines that run it today and who pays for them (pt7).
- **DIRS-5:** substitute datasets for PERSIANN-CDR and how much each could replace (pt7).

### Repository resilience
- **RRS-1:** NCEI's copy count and regions after the move; whether CHRS backs up its server; whether the AWS, Google
  and Azure copies are current (pt7).
- **RRS-2:** NCEI's SOP 60-6-015 (not public); any fixity practice at CHRS.
- **RRS-3:** NCEI's contingency-plan test results (FOIA); any CHRS DR plan and whether CHRS uses UCI OIT's backup.
- **RRS-4:** NCEI's FY2026 spend plan; how CHRS's site is paid for.
- **RRS-5:** the cause of CHRS's 2024 outage and whether files were lost; a final Helene loss count.

## Conflicts between runs

- **GPCP version:** the C-ATBD (2014), code README and User Guide (December 2025) say v2.2; the files name v2.3 from
  July 2015 (`gpcpv23_m`), while Sadeghi et al. (2019) say v2.3 replaced v2.2 for 2009–2013 and the 2011-07-01 header
  still names `gpcp_m1107.bin`.
- **Noise threshold unit:** 0.1 mm/hr (C-ATBD, User Guide) or 0.1 mm/day (Sadeghi et al. 2019).
- **Start of record:** 1982 (product page, C-ATBD §3.4) or 1983-01-01 (User Guide, landing page, files; used).
- **CHRS's director:** AghaKouchak (CHRS directory, UCI News April 2026) or Sorooshian (an undated UCI Office of
  Research listing).
- **Google Earth Engine's coverage:** to 2026-07-31 (pt1) or to 2024-09-30 (a snippet in the CHRS run).
- **NSF 2332263's end:** 10/31/2026 (court sheet) or 10/31/2027 (NSF API).
- **Aqua's end:** September 2027 (NASA, 2025, used) or instruments off 26 Aug 2026 (2023 deck); AIRS still running
  30 Oct 2026.

## Things to check by hand (no new web search)

- NCEI's PERSIANN-CDR pause notice ([node/8306](https://www.ncei.noaa.gov/node/8306)): is it still up, and does the
  cloud-migration page explain it?
- The CHRS portal's Info tab (contacts; the September 2020 "Latest Update").
- The NODD bucket listings for `noaa-cdr-precip-persiann-pds` and Azure `precip-persiann`: their latest file dates.

## Evidence counts

100 items: P 16, D 29, DIRS 28, RRS 27. By stance: 26 for, 25 against, 49 context. By confidence: 35 high, 61
moderate, 4 low.
