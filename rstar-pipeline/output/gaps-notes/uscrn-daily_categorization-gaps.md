# USCRN Daily: what the research didn't search, by subcategory

- **Dataset:** USCRN Daily (daily01), NCEI's daily files for the U.S. Climate Reference Network: one text file per
  station per year, from 2000 to the present, built from the stations' 5-minute data (Geonor T-200B weighing gauge
  with three wires). DOI 10.7289/V5H13007 covers all USCRN products (record C00546). NCEI ingests, quality-controls,
  produces, archives and serves the files; NOAA ARL's Atmospheric Turbulence and Diffusion Division (ATDD) in Oak
  Ridge built and maintains the 141 stations, with a non-federal field team (ORAU, then CISESS).
- **Categorized:** 2026-11-27, first pass.
- **Output:** [uscrn-daily_rstar-categories.json](../categories/uscrn-daily/uscrn-daily_rstar-categories.json), built
  by `rstar-pipeline/processing/scripts/categorize/build_uscrn-daily.py` (106 evidence items).
- **Research used:**
  - `about-datasets/uscrn-daily/`: about-pt1 (hosts, inputs, data path, organizations), qc-formats-pt2 (algorithm,
    QC, calibration, software, FAIR), people-funding-pt3 (people, ages, team, funding before 2025), threats-news-pt4
    (January 2025 – November 2026) and inputs-pt5 (stations, instruments, datalogger, GOES link, field team,
    substitutes);
  - `archives/noaa-ncei/`: the A1 threats run and the A2 resilience run (NCEI is the producer and the only repository);
  - `instruments/noaa-rain-gauges` (its USCRN row);
  - GHCN-Daily's repository-resilience run (pt9), for one NCEI-wide fact: OIG on contingency-plan testing (RRS-3), as
    GPCP and PERSIANN-CDR did.
- **Not used:** both satellite runs (USCRN uses no satellite data; the GOES satellite is only its data relay, covered
  by its own pt1, pt2 and pt5). GHCN-Daily's pt8 covers ATDD's calibration team as a GHCN-Daily source; USCRN's own
  runs cover the same ground, so nothing else was borrowed.
- **Coverage note:** none was written for USCRN Daily (its queries were planned from the templates).
- **Repository runs:** NCEI has both runs. No other repository holds daily01, so none is missing.

## Repositories (the JSON's `dataset` key)

| Repository | Role | Holds |
|---|---|---|
| NOAA NCEI (daily01 archive) | parent | The archive of record: one server serving `pub/data/uscrn/products/daily01/` by HTTPS and FTP, with weekly snapshot zips beside it, the USCRN portal in front and NCEI's tape archive behind |

`producer_is_repository` is **true**: NCEI both produces daily01 and is its archive of record (as for GHCN-Daily). The
stations are ARL's, but ARL holds no copy of the data (it says NCEI does "all the data management activities").

Not repositories: Copernicus's Climate Data Store (a reprocessed copy from 2006, NetCDF and CSV, updated yearly), the
Data Rescue Project's March 2025 snapshot, and GHCN-Daily (which takes in USCRN values as source "R", not the daily01
files). NCAR EOL dataset 100.023 may be another copy; its page could not be read.

## Scores

| Code | For | Against | Context | Score | Why |
|---|---|---|---|---|---|
| P-1 | 4 | 0 | 3 | **35** | No plan found; handover documents incomplete and old (two low items: ARL's civil-service answer, three departed team members) |
| P-2 | 3 | 1 | 3 | **NA** | Only age estimates (low): Diamond, Palecki and Meyers likely already eligible; the others unlikely |
| P-3 | 3 | 1 | 1 | **NA** | Code, QC parameters and the daily rule unpublished (for) vs a documented, peer-reviewed algorithm (against) |
| P-4 | 1 | 2 | 3 | **NA** | No deputy for the Program Manager (for) vs a field team of eight and a science team of three (against) |
| D-1 | 3 | 0 | 5 | **30** | FY2027 request closes ARL (pending); House cut to Climate Labs; NCEI's pending cut |
| D-2 | 2 | 0 | 5 | **25** | One NCEI server holds the files and snapshots; no second site named; no cloud copy |
| D-3 | 2 | 1 | 4 | **NA** | NCEI's pending cut and staff losses (for) vs daily01 current through the shutdown and the migration (against) |
| D-4 | 0 | 1 | 3 | **0** | Open fixed-width ASCII with a README; no proprietary software |
| D-5 | 1 | 1 | 2 | **NA** | Named in news about the proposed cuts (for) vs no removal or alteration found (against) |
| DIRS-1 | 1 | 1 | 4 | **0** | ATDD calibrates in house against its own NIST-traceable weights (the "for" is low) |
| DIRS-2 | 4 | 0 | 6 | **25** | Rising outages; retired datalogger; slipping visits; ARL closure proposed |
| DIRS-3 | 2 | 0 | 2 | **20** | All data through the GOES DCS, which had outages and is changing |
| DIRS-4 | 1 | 1 | 3 | **NA** | Processing on NCEI's own systems (against) vs delivery through NESDIS's GOES DCS and Wallops (for) |
| DIRS-5 | 4 | 2 | 2 | **NA** | No other relay, datalogger maker, maintainer or substitute (for) vs gauge suppliers and data-path fallbacks (against) |
| RRS-1 | 0 | 1 | 5 | **0** | One NCEI server; no second site or cloud copy |
| RRS-2 | 0 | 1 | 0 | **0** | NCEI checks checksums only on ingest and retrieval |
| RRS-3 | 0 | 1 | 1 | **0** | OIG: no contingency-plan testing at alternate sites; NCEI's plan can't be shared |
| RRS-4 | 1 | 2 | 1 | **NA** | NCEI's pending FY2027 cut and staff losses vs FY2026 enacted above the request |
| RRS-5 | 2 | 1 | 2 | **NA** | daily01 through the 2025 shutdown and NCEI's Helene recovery (for) vs Helene's 8% backlog (against) |

Category totals: P NA, D NA, DIRS NA, RRS NA, so **R* is NA** (9 of 19 subcategories NA).

## Judgment calls to double-check

- **P-1 = 35 and the documentation library.** NCEI's public library (requirements, maintenance and data-management
  plans, installation guide, ingest specification, algorithm descriptions) is filed as **context**, not "against". It
  is not a full handover package like PERSIANN-CDR's or GPCP V1.3's: there is no code, and most of it dates from
  2002–2007. The run judged it "enough to re-implement the precipitation algorithm and to read the files, but not to
  run the processing". If you count it as handover documentation (moderate "against"), P-1 goes NA.
- **P-2 is NA, though Diamond's eligibility is close to certain.** His federal service began in 1981 (ARL's own bio),
  so with about 45 years he is past FERS's 30-year rule at any likely age. The rules make every eligibility estimate low
  confidence, so it doesn't set the score. A person may well choose 25 here (Palecki and Meyers, from publication
  years, are likely eligible too).
- **P-4 is NA; the CoCoRaHS "or" rule was not applied.** The one "for" is the Program Manager with no deputy, which
  isn't clearly one of "production, QC, or distribution". The field team of eight and the three-person Climate
  Science Team are moderate "against". If you treat the Program Manager as a production role and apply the "or" rule
  (the team items become context), P-4 = 15.
- **D-1 counts ARL's closure** because ATDD in Oak Ridge runs the stations, though the FY2027 request names only "ARL
  ... as well as a nation-wide network of soil moisture sensors", not USCRN. The House's 11% cut to Climate Labs is a
  moderate "for" (pending, not law). The rejected FY2026 closure and the Senate's flat draft are context.
- **D-3 is NA:** daily01's unbroken record through the 2025 shutdown and the 2026 migration is a high "against", set
  against NCEI's pending cut and staff losses (the host's funding and staffing). This is not the "or" rule: both sides
  bear on "at risk of going dark". NCEI's November 2026 alert is context because daily01 kept updating during it.
- **D-5 is NA:** news naming USCRN in the cuts (Tennessee Lookout, the AMS/NWA appeal, Karl et al. in Eos) is a
  moderate "for" under D-5's "What counts" (news of funding cuts or threatened termination); "no removal or
  alteration found" is a moderate "against". If the news counts only as funding news (D-1), D-5 = 0.
- **DIRS-1 = 0, although GHCN-Daily counts the same lab as "for".** For GHCN-Daily, ATDD is an outside calibration
  team behind one of its sources; for USCRN it is the group that takes the measurements, so its calibration is
  in-house ("against"). ARL's proposed closure is filed in DIRS-2 and D-1 instead.
- **DIRS-3 = 20 rests on the GOES DCS.** The relay is USCRN's only outside feed; its outages were short (1 h 16 min in
  February 2025; a GOES-19 safehold in July 2026) and its DADDS replacement is a planned change. If short, resolved
  outages shouldn't count, DIRS-3 has only the high "sole path" item left, which still gives 20.
- **DIRS-4 is NA:** the GOES DCS and Wallops are filed here too (moderate "for"), following pt2's "partly supported for
  data delivery"; processing itself is NCEI's own (high "against"). If delivery belongs only in DIRS-3, DIRS-4 = 0.
- **DIRS-5 is NA** with both sides moderate: no other relay, datalogger maker, maintainer or reference-quality
  substitute ("for"), against more than one gauge supplier and the data-path fallbacks (EDDN, NCEI's HRIT receiver,
  the logger files).
- **Repository:** NCEI is the only repository, so RRS is judged on NCEI alone. The Copernicus copy is filed as not a
  repository (reprocessed, from 2006, yearly), as ESGF obs4MIPs was for GPCP. Counting it as a child would make RRS-1
  NA (an independent site in Europe, but not current or complete).
- **RRS-1 and D-2:** NCEI's Asheville offsite tapes ("several kilometers away") are context here, not "against" as for
  GHCN-Daily, because no source says which NCEI site holds USCRN's tapes.
- **RRS-3 borrows** OIG's finding from GHCN-Daily's pt9 (moderate "against"), as GPCP and PERSIANN-CDR did.
- **RRS-5:** daily01's record through the 2025 shutdown (a lapse in funding) is a high "for"; the NCEI-wide 8% Helene
  backlog is a moderate "against" (USCRN not named), as for the other NCEI datasets.
- **Open rules this dataset hits:** whether one station closing counts as a lost source (Kingston RI, Ivotuk, and the
  three stations silent in 2026; the outage counts are filed as "for" as a network-wide trend); repeating NCEI-wide
  facts (NCEI's budget and staff appear in D-1, D-3 and RRS-4); whether D-2 and D-3 should be scoped away from the
  repository (both rest on NCEI facts here).

## What the research never searched, or couldn't find, by subcategory

### People risk
- **P-1:** a written succession plan (searched, none found); ARL's 2016 and 2022 lab-review responses (HTTP 403);
  whether the SORD reorganization changed USCRN's roles. *Ask:* ARL or NCEI's USCRN team.
- **P-2:** real ages and service dates (personnel records); publication years for French, Hall and Baker; the field
  team's employer retirement rules.
- **P-3:** the production code, QC parameter files and ISIS (internal); the daily summation rule; the datalogger
  program; the X030–X039 plans and the Site Information Handbook (not read).
- **P-4:** cover for the Program Manager and the field lead; the federal and non-federal split of the field team.

### Data risk
- **D-1:** NOAA's FY2026 spend plan for ARL; the FY2027 outcome after 11 December 2026; USCRN's own budget (never
  broken out; FOIA). The FY2011–14 and FY2016–18 budget justifications were not read.
- **D-2:** which NCEI site holds USCRN's tapes; NCAR EOL 100.023.
- **D-3:** who staffs the USCRN portal and file service; whether the November 2026 alert reached USCRN's folders.
- **D-5:** two Science articles and local Oak Ridge and Knoxville papers (not reachable).

### Dependent infrastructure resilience
- **DIRS-1:** the current calibration procedure; who certifies ATDD's weights and how often; wetness-sensor calibration.
- **DIRS-2:** the causes of the Alaska and 2026 outages and of Ivotuk's end (ARL/ATDD event notes); maintenance visits at
  the other 113 stations (ISIS pages); NOAA's datalogger replacement plan.
- **DIRS-3:** the DADDS cutover date (the 2026 GOES DCS deck could not be read).
- **DIRS-4:** whether NCEI runs the processing on its own computers or in the cloud now.
- **DIRS-5:** Canada's Reference Climate Stations as a substitute.

### Repository resilience
- **RRS-1:** where USCRN's tapes sit; NCEI's AWS regions and copy count after the move.
- **RRS-2:** NCEI's SOP 60-6-015 (not public); a stewardship maturity report for USCRN (not looked for).
- **RRS-3:** NCEI's contingency-plan test results.
- **RRS-4:** NCEI's FY2026 spend plan.
- **RRS-5:** whether USCRN's files were affected by Helene; a final Helene loss count.

Most of these are held by ARL/ATDD (outage causes, maintenance, datalogger plan, calibration) or NCEI (code, tapes,
spend plans), not published: an inquiry would settle more than another web search.

## Conflicts between runs

- **Station counts:** 137 (Eos), 139 towers (ARL 2026), 141 (ARL 2024; the metadata file), 142 (ARL newsletter 2025),
  "more than 138" (Tennessee Lookout) and 159 daily01 files (which include regional-network and test sites) (pt1, pt4,
  pt5). Not resolved; not used for a score.
- **Alaska:** ARL wrote "a total of 29" in 2023; NCEI says 25 with 29 planned; daily01 has 25 Alaska files in 2023 and
  24 in 2024–26 (pt5). pt5 reads 29 as the planned total.
- **Field crew size:** "eight technicians and engineers" (ARL, undated), four for Blue Hill (2024), five for the 2026
  transmitter swap (pt3, pt4, pt5). Likely crews of different jobs, not losses; no source says.
- **DIRS-4:** pt1 rated it contradicted (processing in house); pt2 qualified that as partly supported for data
  delivery. Both are kept (DIRS-4 NA).
- **The algorithm's start:** the daily01 README dates OAP 2.0 to 17 August 2015; NCEI's catalog dates the database
  reprocessing to 15 October 2015 (pt2). Possibly two steps; not used for a score.
- **Temperature sampling:** "10-second" (README) vs "two-second" (NCEI's Measurements page) (pt1). Not a precipitation
  matter.

## Things to check by hand (no new web search)

- The metadata file's `review_notes`: DOI 10.7289/V5H13007 and record C00546; the station counts (141 vs the figures
  above).
- Kingston RI was "scheduled to be decommissioned the summer of 2026" but still reported to 14 November 2026.
- The 2026-05-14 rewrite of 146 of the 2023 files, which has no change-log entry (worth asking NCEI).
- The pages listed in each run's `check-by-hand.md` (ARL's 2016 and 2022 review responses, the CISESS 2021–23 annual
  reports, NCAR EOL 100.023, the archive.data.noaa.gov listing).

## Evidence counts

106 items: P 25, D 30, DIRS 33, RRS 18. By stance: 34 for, 17 against, 55 context.
