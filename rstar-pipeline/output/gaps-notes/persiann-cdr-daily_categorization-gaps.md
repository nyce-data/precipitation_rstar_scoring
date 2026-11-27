# PERSIANN-CDR Daily: what the research didn't search, by subcategory

- **Dataset:** PERSIANN-CDR Daily v01r01, a NOAA CDR (DOI 10.7289/V51V5BWQ, NCEI record C00854), made by UC Irvine's
  Center for Hydrometeorology and Remote Sensing (CHRS) from GridSat-B1 infrared, bias-adjusted to GPCP monthly.
- **Categorized:** 2026-11-27, first pass (pt1–pt6) and then a **second pass** the same day, adding
  people-production-pt7 and calibration-pt8 (see "Changes from the first pass").
- **Output:** [persiann-cdr-daily_rstar-categories.json](../categories/persiann-cdr-daily/persiann-cdr-daily_rstar-categories.json),
  built by `rstar-pipeline/processing/scripts/categorize/build_persiann-cdr-daily.py` (122 evidence items).
- **Research used:**
  - `about-datasets/persiann-cdr-daily/`: about-pt1, qc-formats-pt2, about-pt3 (funding), news-pt4, inputs-pt5,
    satellites-pt6, people-production-pt7 (people, ages, who runs and pays for the extension, code, computers) and
    calibration-pt8 (GridSat-B1's recalibration, GPCP version, substitutes, which copies are current);
  - `archives/noaa-ncei/`: the A1 threats run and the A2 resilience run (which covers PERSIANN-CDR by name);
  - `archives/uci-chrs/2026-11-27_uci-chrs-resilience` (CHRS's own data site);
  - `instruments/noaa-satellites` (GOES, DMSP, POES);
  - for NODD-wide and NCEI-wide facts only: GHCN-Daily's repository-pt7 and repository-resilience-pt9.
- **Not used:** `instruments/nasa-satellites` (about GPM and IMERG; PERSIANN-CDR uses no NASA sensor directly, and
  Aqua AIRS, which reaches it through GPCP, is covered by inputs-pt5) and `instruments/noaa-rain-gauges` (gauges reach
  it only through GPCC inside GPCP). GPCP Daily's calibration-copies-pt7, borrowed in the first pass for one inference
  on substitutes, was dropped once pt8 covered substitutes.
- **Query files:** pt7 and pt8 each had their own query file
  (`persiann-cdr-daily-gaps_Rstar_query_people-production_pt7.md` and `…_pt8.md`, in each run folder). pt8 ran in the
  parallel `Rstar_query_results_pt2` folder, first named `…_calibration-copies`, and was renamed `…_calibration-pt8`.
- **Coverage note:** `datasets-gap-queries/persiann-cdr-daily_coverage-gaps.md` (2026-11-23) listed what the gap runs
  should fill; this note replaces it for the categorization.
- **Shared people:** Braithwaite, Hsu, Nguyen and Sorooshian (CHRS) are also co-authors of IMERG's ATBD (CHRS's
  PDIR-Now is an IMERG input). GPCP V3.3 uses PERSIANN-RAW (not PERSIANN-CDR), and PERSIANN-CDR uses GPCP v2.3.

## Repositories (the JSON's `dataset` key)

| Repository | Role | Holds |
|---|---|---|
| NOAA NCEI | parent | Archive of record and distributor (HTTPS, THREDDS, ERDDAP); archived in Asheville |
| UC Irvine CHRS data site | producer site | CHRS's own copy (portal, HTTPS and FTP; raw `.bin.gz` daily files, monthly and yearly) |
| AWS, Google Cloud and Azure (NODD) | child | NCEI's copies (`s3://noaa-cdr-precip-persiann-pds/`, Google Cloud `noaa-cdr-precip-persiann`, Azure `precip-persiann`) |

Not repositories: the Data Rescue Project's April 2025 snapshot (1983–2024, 16 GB), Google Earth Engine (reformatted,
to 2026-07-31) and the IRI/LDEO Data Library (frozen at 30 September 2019, behind a sign-in). CHRS serves its own copy,
but NCEI is the archive of record, so `producer_is_repository` is false (the site would otherwise say the producer and
repository are one organization, as it does for IMERG, where Goddard is both).

## Scores

| Subcategory | Items (for / against / context) | Score | Main reason |
|---|---|---|---|
| P-1 Succession plan | 2 / 1 / 3 | NA (was 0) | No plan found by a targeted search, and the one named producer retired with no successor, vs the public 2013–2014 handover package |
| P-2 Retirement-eligible | 1 / 1 / 5 | NA | Only low-confidence age estimates on either side; the founder and the named producer are already retired (context) |
| P-3 Undocumented knowledge | 3 / 2 / 2 | NA | QC procedure "not documented", documents name the wrong GPCP version, nothing newer than the 2014 code vs public code and C-ATBD |
| P-4 Single point of failure | 1 / 0 / 5 | **15** (was NA) | The files name one creator, now a UCI retiree, and no backup is named |
| D-1 Program defunding | 1 / 2 / 9 | NA | Pending FY2027 cut to NCEI vs no cut aimed at PERSIANN-CDR, and NESDIS's 2025–2029 plan keeping it |
| D-2 Storage single point | 3 / 1 / 1 | NA | Asheville-only archive, single-region cloud target, CHRS's servers with no backup published vs four organizations serving it |
| D-3 Access fragile | 5 / 0 / 3 | **20** | NCEI's November 2026 outage, pending NCEI cut, CHRS's one-admin site and its 2024 outage and lag, NODD with no term |
| D-4 Format obsolescence | 0 / 1 / 3 | **0** | CF netCDF-4 on NCEI's routes, rated FAIR |
| D-5 Political sensitivity | 0 / 1 / 2 | **0** | About 120 searches found nothing naming PERSIANN-CDR |
| DIRS-1 Calibration | 4 / 0 / 4 | **25** | GridSat-B1 switched from HIRS to VIIRS VGAC in October 2024, its calibration is now written by one person outside NCEI, and GPCP v2.3 is superseded |
| DIRS-2 Observation platforms | 3 / 0 / 5 | **25** | Ageing Meteosat-9/-10 with no MTG in ISCCP B1; DMSP F17 SSMIS and Aqua AIRS (through GPCP) |
| DIRS-3 Upstream supply chain | 1 / 0 / 8 | **20** | GPCP v2.3 "Version Superseded" with no freeze date and no plan to move |
| DIRS-4 External processing | 0 / 1 / 5 | **0** | CHRS produces it on its own servers (2019 paper); nothing shows outside processing |
| DIRS-5 No alternative supplier | 1 / 2 / 2 | NA | No fallback input named vs geostationary backups already used and partial substitute datasets (CMORPH-CDR, CHIRPS v3, IMERG, MSWEP) |
| RRS-1 Geographic redundancy | 2 / 4 / 1 | NA | NCEI, CHRS and the cloud copies in separate places, and the AWS copy current, vs Asheville-only archive, single-region cloud target, no check of NODD copies, no CHRS backup |
| RRS-2 Checksum verification | 0 / 3 / 2 | **0** | Checksums only at ingest and on order (DSMR-00012, CoreTrustSeal); none published at CHRS |
| RRS-3 Disaster recovery plan | 0 / 2 / 1 | **0** | NCCF can't test at alternate sites; no CHRS plan published; NCEI's plan not shareable |
| RRS-4 Stable funding | 1 / 5 / 0 | NA | FY2026 enacted vs pending FY2027 cut, NCEI staff losses, grant-funded School Center, no-term cloud copies |
| RRS-5 Track record | 3 / 2 / 2 | NA | Helene, the 2015 merger and CHRS's 2024 outage without reported loss vs 8% backlog unaccounted, 27 products retired |

9 of 19 subcategories are NA, so every group total and R* are NA. (The first-pass note called DIRS a full total of
70; that was wrong, since DIRS-5 was already NA. The four scored DIRS subcategories add to 70 of their 85 points.)

## Judgment calls to double-check

New or changed in the second pass:
- **P-1 is now NA.** Two moderate "for" items (pt7's targeted search found no succession plan; the files' only named
  creator, Braithwaite, is a "UCI Retiree" with no successor named) now stand against the high "against" handover
  package (C-ATBD, data flow diagram, user guide, the 2014 code). If you take the package as the plan, P-1 is 0. If
  it is too old to count (2013–2014), P-1 is 35.
- **P-2 stays NA.** Sorooshian ("Distinguished Professor Emeritus") and Braithwaite ("UCI Retiree") are already
  retired, so they are filed as context under the rule that a departure can't count in P-2 (it counts in P-1 and
  P-4). The run read Sorooshian's emeritus status as supporting P-2. He is still PI of record at NCEI and published
  in 2026. If you count him as key personnel at retirement, P-2 is 25. Hsu's estimate (56–61, probably eligible under
  UC's age-55 rule) is low, like every age estimate.
- **P-4 = 15 rests on one moderate item:** the 2026 files name one creator, now retired, and NCEI's ISO record still
  names Sorooshian. Both records may be fixed templates. If you don't take file metadata as showing who runs the
  extension, P-4 goes back to NA. Tu Thanh Ung (the one system administrator, credited with software on the 2026
  CCS-CDR V2.0 paper) is context: no source says Ung runs PERSIANN-CDR.
- **D-1:** NESDIS's 2025–2029 product plan, which keeps PERSIANN-CDR, is a new moderate "against". D-1 was already NA,
  so no score changed. NA23OAR4310443 stays context, though the run read it as supporting D-1: it funds CHRS's new
  high-resolution record (CCS-CDR v2), not PERSIANN-CDR's extension.
- **D-3:** NCEI's "pause in operations" notice moved from a high "for" to context. pt8 found the notice dated
  2025-09-08 and unchanged, while files were made again from 2026-07-09. It was a production pause, not an access
  outage, and it looks stale. D-3 stays 20 on its five other "for" items. This settles the first pass's D-3 question.
- **DIRS-1:** the Knapp item (GridSat's calibration written by a one-person firm outside NCEI) is moderate "for". The
  C-ATBD revision table was read; that he left NCEI in 2025 and that the firm has one employee come from search
  snippets only.
- **DIRS-3:** the first pass's moderate "for" ("V3.3 itself takes PERSIANN data, so the two would feed each other")
  was removed. GPCP's team says V3.3 uses PERSIANN-RAW, not PERSIANN calibrated by v2.3. DIRS-3 = 20 now rests on one
  high item (v2.3 superseded, no freeze date, no plan to move).
- **DIRS-5:** the partial substitutes (CMORPH-CDR from 1998, CHIRPS v3 over land, IMERG Final to September 2025,
  MSWEP) are one moderate "against", as GPCP's were. None matches the 1983 start at daily 0.25° over land and ocean.
  DIRS-5 stays NA.
- **RRS-1:** the AWS copy being current (to 31 July 2026, copied a day after NCEI) is a moderate "for" for NODD,
  though it is fed from NCEI and not checked independently. RRS-1 was already NA.

Still open from the first pass:
- **P-3 "for" items:** NCEI's 2020 stewardship score ("Procedure not documented or available" for QC monitoring) and
  the user guide naming GPCP v2.2 while the files use v2.3. pt7 adds a third (nothing newer than the 2014 code).
- **D-1:** the run's "no cut found aimed at PERSIANN-CDR or CHRS" is a moderate "against" for the producer side.
- **D-4:** CHRS's headerless raw binary (rated non-FAIR) is context, not "for": it needs no proprietary software, and
  NCEI's routes serve open netCDF.
- **DIRS-1:** GPCP monthly is treated as a calibration reference as well as an input (also in DIRS-3).
- **DIRS-2:** DMSP F17 and Aqua AIRS reach PERSIANN-CDR only through GPCP, so they are moderate "for" (GPCP Daily's
  precedent). GOES's 2032 spare gap is context, as for GPCP.
- **DIRS-4 = 0** comes from a 2019 statement that CHRS's servers produce it. pt7 found nothing newer (the computers
  are not named). MATLAB is context: UC Irvine's campus licence covers it.
- **RRS-1 "for":** NCEI, CHRS and the NODD copies in separate places count as a moderate "for" though none is shown
  verified (the GPCP/IMERG precedent). CHRS's missing backup is a moderate "against" resting on silence.
- **RRS-4:** CHRS's ended grant counts here (the repository's own funding) though it is context in D-1.
- **Repository roles:** CHRS's site is a producer site; IRI is not a repository.

## What the research never searched, or couldn't find, by subcategory

### People risk
- **P-1:** a written succession plan (searched, none published); why the directorship changed in 2025 and whether
  Braithwaite was recalled (not published).
- **P-2:** real ages, service dates and UC retirement tiers (personnel records); when Sorooshian became emeritus and
  when Braithwaite retired.
- **P-3:** whether CHRS's current code differs from the 2017 package; the training code. *Ask:* CHRS or
  PERSIANN_contacts@noaa.gov.
- **P-4:** who runs the quarterly extension today and whether anyone backs them up (not published).

### Data risk
- **D-1:** what pays for the extension since 2014 (not published; CHRS or NCEI's CDR contact); a successor to
  NA23OAR4310443 (USAspending's award search, which is POST-only, was not run); the FY2027 outcome; the terminated NOAA
  "incoming subaward" at UC Irvine.
- **D-2:** NCEI's AWS regions after the move; where CHRS's servers sit and whether they are backed up.
- **D-3:** the cause of the 2025–26 processing pause and of CHRS's 2024 outage and lag; how CHRS's administrator is
  paid.
- **D-4:** CHRS's binary layout and terms of use.

### Dependent infrastructure resilience
- **DIRS-1:** whether PERSIANN-CDR's months from October 2024 used the VGAC-calibrated GridSat-B1 (not in the C-ATBD
  or the headers); an NCEI successor to Knapp and how GridSat's calibration is paid for.
- **DIRS-2:** when MTG enters ISCCP B1; which DMSP satellites still deliver after 30 Sep 2026.
- **DIRS-3:** a GPCP v2.3 freeze date (NCEI's C00979 page timed out) and any plan if it is frozen; which GPCP version
  adjusts 2009–2013 at NCEI.
- **DIRS-4:** the machines that run it today and who pays for them (not published).
- **DIRS-5:** GSMaP, TAMSAT and PERSIANN-CCS-CDR as substitutes (pt8's time ran out).

### Repository resilience
- **RRS-1:** NCEI's copy count and regions after the move; whether CHRS backs up its server; whether the Google Cloud
  and Azure copies are current (pt8 checked AWS only).
- **RRS-2:** NCEI's SOP 60-6-015 (not public); any fixity practice at CHRS.
- **RRS-3:** NCEI's contingency-plan test results (FOIA); any CHRS DR plan and whether CHRS uses UCI OIT's backup.
- **RRS-4:** NCEI's FY2026 spend plan; how CHRS's site is paid for.
- **RRS-5:** the cause of CHRS's 2024 outage and whether files were lost; a final Helene loss count.

## Conflicts between runs

- **GPCP version:** the C-ATBD (2014), code README and User Guide (December 2025) say v2.2; the files name v2.3 from
  July 2015 (`gpcpv23_m`). Sadeghi et al. (2019) say v2.3 replaced v2.2 for 2009–2013 at CHRS and NCEI, but NCEI's
  2010 and 2013 files still carry 2014 creation dates (pt8), and the 2011-07-01 header still names `gpcp_m1107.bin`.
  The v2.3 2009–2013 files may exist only on CHRS's portal.
- **GPCP V3.3's pause:** NASA's page says V3.3 is "paused at September 2024" for GridSat's new calibration, but lists
  data to 2025-12-31 (pt8). Probably older text.
- **NCEI's cloud-migration alert:** November 16–30, 2026 (NCEI A2 run) or 16 November to 31 December 2026 (pt8);
  probably extended.
- **Noise threshold unit:** 0.1 mm/hr (C-ATBD, User Guide) or 0.1 mm/day (Sadeghi et al. 2019).
- **Start of record:** 1982 (product page, C-ATBD §3.4) or 1983-01-01 (User Guide, landing page, files; used).
- **CHRS's director:** AghaKouchak since mid-2025 (Wayback captures of CHRS's directory, UCI News April 2026) or
  Sorooshian (an undated UCI Office of Research listing, probably out of date).
- **Braithwaite's age estimate:** 51–56 from his PERSIANN papers (2000 on), or 61–66 if the 1990–91 biology items in
  his profile are his. He is retired either way.
- **NSF 2332263's end:** 10/31/2026 (court sheet) or 10/31/2027 (NSF API).
- **Aqua's end:** September 2027 (NASA, 2025, used) or instruments off 26 Aug 2026 (2023 deck); AIRS still running
  30 Oct 2026.
- Settled by pt8: Google Earth Engine's copy runs to 2026-07-31 (the CHRS run's 2024-09-30 snippet was out of date);
  IRI/LDEO is frozen at 30 September 2019.

## Things to check by hand (no new web search)

- Download one 2010 PERSIANN-CDR file from NCEI and read its `source` attribute (`ncdump -h`): `gpcp_m` (v2.2) or
  `gpcpv23_m`?
- NCEI's GPCP monthly v2.3 page (C00979, timed out in pt8): any freeze or retirement date.
- The Google Cloud bucket `noaa-cdr-precip-persiann` and Azure `precip-persiann`: their latest file dates.
- NCEI's pause notice ([node/8306](https://www.ncei.noaa.gov/node/8306)): still up, though processing resumed?
- An inquiry, if wanted (CHRS or `PERSIANN_contacts@noaa.gov`): who runs and pays for the quarterly extension, on
  which computers, and whether the months from October 2024 use the VGAC-calibrated GridSat-B1.

## Changes from the first pass

Second pass, 2026-11-27: 33 items added, 11 dropped (100 → 122).
- **Added from pt7** (people-production): the 2025 directorship handover with dates, Braithwaite's and Sorooshian's
  retirements, the targeted no-plan search, CHRS's age, UC's retirement rule, age estimates for Hsu, Nguyen and
  AghaKouchak, Sadeghi's departure, CHRS's two staff, the single retired named creator (P-4), no code newer than 2014,
  NA23OAR4310443's details, NESDIS's 2025–2029 plan, the other federal money checked, the unnamed computers and the
  MATLAB licence.
- **Added from pt8** (calibration): GridSat-B1's dated HIRS-to-VGAC switch, its calibration author now outside NCEI,
  the unpublished use of VGAC data, GPCP V3.3's pause note, V3.3 using PERSIANN-RAW, the GPCP-version-by-batch
  inference, CHRS's separate PERSIANN-CDR V3 project, the end of the processing pause, the partial substitutes, the AWS
  copy being current, and the IRI and Data Rescue Project copies' dates.
- **Rewritten with the newer facts (8):** CHRS's leadership change (P-1), the PI's retirement status (P-2, which said no
  retirement date was known), "no code after 2014" (P-3, now a "for" from pt7's targeted search), the pause notice (P-4
  and D-3; D-3's moved from "for" to context), IRI's frozen copy (D-3), whether VGAC data are used (DIRS-1), and the
  non-repository copies (RRS-1).
- **Dropped (3):** Braithwaite's low "for" in P-1 (replaced by pt7's moderate one); DIRS-3's "V3.3 takes PERSIANN data,
  so the two would feed each other" (wrong: V3.3 uses PERSIANN-RAW); and the substitutes inference borrowed from GPCP
  Daily's calibration-copies-pt7.
- **Scores changed:** P-1 from 0 to NA; P-4 from NA to 15. Still 9 of 19 NA, and R* NA.
- **Gaps:** every "not searched (pt7)" gap is now searched or marked not public. Two gaps are still "not searched":
  D-4's CHRS binary layout and terms (its README not read) and DIRS-5's GSMaP, TAMSAT and PERSIANN-CCS-CDR.

## Evidence counts

122 items: P 26, D 32, DIRS 36, RRS 28. By stance: 31 for, 28 against, 63 context. By confidence: 42 high, 73
moderate, 7 low.
