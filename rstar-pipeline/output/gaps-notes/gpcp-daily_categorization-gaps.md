# GPCP Daily: what the research didn't search, by subcategory

- **Dataset:** GPCP Daily, two families: the 1° One-Degree Daily (1DD V1.3, NOAA CDR 01B-35 at NCEI, DOI
  10.7289/V5RX998Z) and the 0.5° V3.x Daily (V3.2 and V3.3 at NASA GES DISC; V3.3 also an NCEI CDR, C01726).
- **Categorized:** 2026-11-24 (first pass); the same day, pt7 Run 2 (calibration-copies-pt7) was added.
- **Output:** [gpcp-daily_rstar-categories.json](../data-rstar-categories/datasets/gpcp-daily/gpcp-daily_rstar-categories.json),
  built by `rstar-pipeline/processing/scripts/categorize/build_gpcp-daily.py` (124 evidence items; 102 before Run 2).
- **Research used:**
  - `about-datasets/gpcp-daily/`: about-pt1, qc-formats-pt2, people-pt3, funding-news-pt4, inputs-pt5,
    satellites-pt6 and the two gap runs of the pt7 query: people-production-pt7 (Run 1) and
    calibration-copies-pt7 (Run 2: calibration, alternatives and copies);
  - `archives/noaa-ncei/`: the A1 threats run and the A2 resilience run (which covers GPCP Daily by name);
  - `instruments/nasa-satellites` and `instruments/noaa-satellites` (GPM, Aqua, DMSP, POES, Suomi NPP, GOES);
  - for NCEI-wide and NODD facts only: GHCN-Daily's repository-pt7 and repository-resilience-pt9.
- **Not used:** `instruments/noaa-rain-gauges` (GPCP's gauges come only through DWD's GPCC analysis, and no run ties
  US gauge networks to it) and the other GHCN-Daily runs.
- **Not available:** no repository run for NASA GES DISC, NCAR GDEX or Copernicus CDS. The NASA GES DISC + PPS A2
  query is written but not run (see `supplemental-queries-run-sheet.md`).
- **Replaces** the coverage note `gpcp-daily_coverage-gaps.md` (2026-11-23), which listed what the gap runs should fill.

## Repositories (the JSON's `dataset` key)

| Repository | Role | Holds |
|---|---|---|
| NOAA NCEI | parent | 1DD V1.3 (archive of record); V3.3 CDR in its `climatedatarecords` bucket |
| NASA GES DISC | parent | V3.2, V3.3 (role "ARCHIVER" in CMR) |
| AWS and Google Cloud (NODD) | child | NCEI's copies; version not confirmed |
| NSF NCAR GDEX | child | V1.3 to 2024-11, V3.2 |
| Copernicus CDS | child | v1.3 to 2024-03, V3.2, V3.3 |

Not repositories: Google Earth Engine (reformatted); ESGF obs4MIPs (Run 2 found V3.3 at ORNL and NERSC, but
obs4MIPs rewrites files to CMIP conventions, so it is filed as a reformatted copy); the GSFC backup folder
(unreachable) and the UMD page (monthly summaries only). Producer: UMD/ESSIC (1DD V1.3 and
NCEI's V3.3 CDR) and NASA Goddard under MEaSUREs (V3.x), so `producer_is_repository` is false.

## Scores

| Subcategory | Items (for / against / context) | Score | Main reason |
|---|---|---|---|
| P-1 Succession plan | 1 / 2 / 4 | NA | No plan found (for) vs V1.3's CDR handover package and V3.3's ATBD (against) |
| P-2 Retirement-eligible | 2 / 1 / 3 | NA | Only estimates (low): Huffman likely eligible now; Adler about 80 |
| P-3 Undocumented knowledge | 1 / 3 / 1 | NA | V3.x code not published (for) vs V1.3 code public and V3.3 ATBD (against) |
| P-4 Single point of failure | 1 / 1 / 3 | NA | Huffman sole ATBD reviser and only federal employee vs three people on Goddard production |
| D-1 Program defunding | 3 / 2 / 5 | NA | Pending FY2027 cuts to NCEI and NASA ESDS vs MEaSUREs and CISESS awards running to 2028–2029 |
| D-2 Storage single point | 3 / 3 / 1 | NA | NCEI copies in Asheville only, single cloud region, V1.3's outside copies stale vs several organizations serving it, V3.3 current at CDS |
| D-3 Access fragile | 6 / 0 / 1 | **20** | NCEI access outage (Nov 2026), pending NCEI cut, NODD with no term, DAAC consolidation, GDEX wind-down |
| D-4 Format obsolescence | 0 / 1 / 2 | **0** | Open CF netCDF-4 on every route |
| D-5 Political sensitivity | 0 / 1 / 2 | **0** | About 40 news searches found nothing naming GPCP |
| DIRS-1 Calibration | 6 / 0 / 2 | **25** | 1DD calibrated to F17 SSMIS alone, its feed unpublished since the RSS CDR ended (2025-07-31) and disrupted by FNMOC; GridSat's HIRS calibration ended in 2024; no funded reference after GPM |
| DIRS-2 Observation platforms | 7 / 0 / 4 | **25** | DMSP SSMIS (end date in conflict), Aqua AIRS (drift advisory), lost IMERG microwave satellites, GPM's fuel and unfunded extension |
| DIRS-3 Upstream supply chain | 6 / 0 / 3 | **20** | IMERG V07 Final ended, V08 late; GridSat pause; SSMIS feed undocumented, F-17 outage March 2026; AIRS |
| DIRS-4 External processing | 3 / 1 / 2 | NA | CPC makes 1DD's IR histograms, GSFC's Sounder Research Team makes the AIRS/TOVS estimates vs producers compute on their own workstations |
| DIRS-5 No alternative supplier | 3 / 3 / 3 | NA | 1DD has one sensor of each kind, no F17/AIRS contingency vs IMERG's overlapping constellation, V3.3's stand-in inputs, partial substitute datasets |
| RRS-1 Geographic redundancy | 2 / 5 / 3 | NA | Copies at independent organizations, V3.3 current at CDS (Europe) vs none verified, NCEI's in Asheville, GDEX and CDS's V1.3 stale |
| RRS-2 Checksum verification | 0 / 2 / 1 | **0** | Checksums only at ingest and on order (DSMR-00163, CoreTrustSeal) |
| RRS-3 Disaster recovery plan | 0 / 1 / 1 | **0** | NCCF can't test at alternate sites; NCEI's plan not shareable |
| RRS-4 Stable funding | 1 / 5 / 0 | NA | FY2026 enacted vs pending FY2027 cuts and no-term cloud copies |
| RRS-5 Track record | 3 / 2 / 2 | NA | Helene and 2015 merger without reported loss vs 8% backlog unaccounted, 27 products retired |

People, data and repository totals are NA, so R* is NA (11 of 19 subcategories NA). Run 2 changed no score.

## Judgment calls to double-check

- **D-3 = 20 rests on repository facts** (NCEI's November 2026 outage, NODD contracts, DAAC consolidation, GDEX). None
  names GPCP; under the rules repository facts count in D-3.
- **D-5 = 0** comes from one moderate "against" item: a search that found nothing. GHCN-Daily had a source tying it to
  political action; GPCP has none.
- **DIRS items reached through IMERG** (GPM, POES, S-NPP, AMSR2) are counted as "for": IMERG is on V3.x's input list
  and pt6 lists those satellites as GPCP's. They were given moderate rather than high confidence.
- **DIRS-4:** CPC's GPCP IR histograms are filed as outside processing ("for"), not as a data feed (DIRS-3).
- **D-4:** the GES DISC and CDS login and licence gaps were filed as context (access, not format).
- **P-4:** "three people on Goddard production" was filed as "against", which turns the run's "P-4 supported for
  V3.x" into NA.
- **GDEX and CDS as child repositories:** both serve the original netCDF with metadata, so they count.
- **Two parents:** NCEI for V1.3 and GES DISC for V3.x.
- **Point values:** the scorer reads `rstar-pipeline/input/framework/how_to_score_rstar.md`, which gives DIRS-2 25, P-3 25 and DIRS-4 15;
  the decisions doc's table says 20, 20 and 20.

## What pt7 Run 2 added (2026-11-24)

Run 2 (`2026-11-24_gpcp-daily-calibration-copies-pt7`) answered the calibration, alternatives and copies parts of the
pt7 query: 22 items in D-2, DIRS-1 to DIRS-5 and RRS-1, and new gap statuses in DIRS-1, DIRS-2, DIRS-5, RRS-1 and
RRS-2. No score changed.

- **Corrected:** the RSS SSMIS CDR ended at **2025-07-31** (NCEI metadata C01567), not 2023 (NCEI's product page). The
  first-pass DIRS-1 and DIRS-3 items that said 2023 were rewritten from Run 2.
- **Filled:** substitute datasets for GPCP Daily (DIRS-5; CMORPH CDR, PERSIANN-CDR, MSWEP, CHIRPS, GPCC Full Data
  Daily, IMERG Final; none on GPCP's terms); a 1DD F17/AIRS contingency (searched, none found); FNMOC's October 2026
  change and the March 2026 F-17 outage; DMSP's conflicting end date; GPM's fuel and the missing Senior Review
  outcome; AIRS's drift advisory; who makes V3.x's AIRS/TOVS estimates (GSFC Sounder Research Team); which outside
  copies are current (CDS for V3.3; GDEX and CDS's V1.3 stale; ESGF for V3.3).
- **Still open from the pt7 query:** which version the NODD buckets hold (asked, not answered); Earth Engine's copy;
  which SSMIS feed 1DD uses now; who keeps 1DD's SSMIS intercalibration; ESGF V3.3's last file date; the GSFC backup.

**Judgment calls from Run 2 to double-check:**
- **ESGF obs4MIPs filed as not a repository** (context), because obs4MIPs rewrites files to CMIP conventions. The run
  called it "supports RRS-1 for V3.3". If you count it, add it to the `dataset` key as a child repository.
- **CDS's V3.3 copy filed as current** ("for" in RRS-1): it ends 2025-12-31, the same as NASA's own V3.3 record, so it
  is not behind the source even though the run called it "about a year behind".
- **Aqua continued into FY2027** filed as context in DIRS-2, not "against": a one-year extension on a drifting
  satellite doesn't show the platform is safe. As "against", DIRS-2 would become NA.
- **Substitute datasets filed as "against" DIRS-5** (moderate), though none is a full match; with V3.3's stand-in
  inputs that makes DIRS-5 3 for / 3 against.
- **AIRS/TOVS estimates from GSFC's Sounder Research Team** filed in DIRS-4 (outside processing), not DIRS-1.
- **V1.3's stale outside copies** filed as "for" in D-2 (V1.3's current data rest on NCEI and its NODD copies).

## What the research never searched, by subcategory

### People risk
- **P-1:** a written plan at Goddard, UMD or Arizona; the team's size. *Search:* "GPCP team" staff; NASA Code 612
  workforce plan; MEaSUREs project management plan.
- **P-2:** real ages and service dates (not public). Huffman's federal start date from a second source.
- **P-3:** whether V3.x code is shared on request; the contents of the 2017 tarball. *Ask:* Huffman or
  gpcp_contacts@noaa.gov.
- **P-4:** who computes each version each month; who backs up Huffman; which contract pays Bolvin and Nelkin.

### Data risk
- **D-1:** Behrangi's MEaSUREs award number and end date (USAspending under the University of Arizona; NSPIRES);
  GPCP's share of CISESS; the FY2027 outcome.
- **D-2:** GES DISC's storage and backup; NCEI's AWS regions after the move.
- **D-3:** GES DISC and CDS funding and staff; NODD contract end dates.
- **D-4:** which version the NODD buckets hold.
- **D-5:** any data rescue snapshot of GPCP Daily.

### Dependent infrastructure resilience
- **DIRS-1:** which SSMIS feed calibrates 1DD since 2025-07-31 and who keeps its intercalibration (searched in Run 2,
  not published; *ask* the GES DISC or NCEI help desk); GPM's 2026 Senior Review outcome (not yet posted).
- **DIRS-2:** DMSP's real end date (September 2026 or "no earlier than 2028"; no DoD page settles it); Aqua's real
  end-of-science date (continued into FY2027).
- **DIRS-3:** the V08 transition and V3.3's next extension; NCEI's preliminary monthly feed.
- **DIRS-4:** the machines that run each version; whether CPC still makes the IR histograms.
- **DIRS-5:** how much of GPCP Daily each substitute could replace (Run 2 listed them; IMERG, GSMaP and ERA5
  producer pages not read).

### Repository resilience
- **All five, for GES DISC, GDEX and CDS:** not searched. Run the NASA GES DISC + PPS A2 query; GDEX and CDS are
  copies and may not need a run of their own.
- **RRS-1:** copy count and regions after NCEI's move; whether NODD copies are verified; which version the NODD
  buckets hold; the GSFC backup folder (unreachable); ESGF V3.3's last file date.
- **RRS-2:** NCEI's SOP 60-6-015 (not public); GES DISC's checksum practice (GDEX and CDS pages show none).
- **RRS-3:** NCEI's contingency-plan test results (FOIA).
- **RRS-4:** NCEI's and NASA's FY2026 spend plans.
- **RRS-5:** a final Helene loss count; whether the 2026 migration delays GPCP Daily.

## Conflicts between runs

- **Who computes NCEI's V3.3 copy:** UMD (NCEI metadata, likely carried over from V1.3) or Goddard (Huffman's bio).
- **Who runs 1DD V1.3:** UMD (NCEI) or Huffman ("Produce ... One-Degree Daily", his job line).
- **V3.3's pause month:** March 2024 (release notes) or September 2024 (catalog); both out of date.
- **Aqua's end:** August 26, 2026 (2025 deck), still operating October 30, 2026, power to September 2027.
- **Bolvin and Nelkin's employer:** STC (GSFC pages) or SSAI (NCEI metadata, EGU26 abstract).
- **RSS SSMIS CDR end:** 1987–2023 (NCEI product page) or through 2025-07-31, status "Complete" (NCEI metadata
  C01567, used).
- **DMSP's end:** September 2026 (DoD via NSIDC, 2025) or "no earlier than 2028" (Air & Space Forces, Aug 2026, on
  the FY2026 NDAA); FNMOC's notice shows deliveries past September.
- **MEaSUREs award length:** "5 more years" from 2023, "(2017-2028)", against the unenacted FY2026 plan to end
  projects by CY2026.
