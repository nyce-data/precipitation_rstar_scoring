# IMERG Late Run: what the research didn't search, by subcategory

- **Dataset:** IMERG Late Run V07 (V07B processing; "hybrid" since March 2026, the V07 algorithm ingesting GPROF V08),
  half-hourly `GPM_3IMERGHHL` (DOI 10.5067/GPM/IMERG/3B-HH-L/07) and daily `GPM_3IMERGDL`
  (DOI 10.5067/GPM/IMERGDL/DAY/07). V08 Late is due no sooner than winter 2026.
- **Categorized:** 2026-11-24 (first pass); second pass the same day added pt7 Run 1 (people and production).
  See "Changes from the first pass" at the end.
- **Output:** [imerg-late-run_rstar-categories.json](../data-rstar-categories/datasets/imerg-late-run/imerg-late-run_rstar-categories.json),
  built by `rstar-pipeline/processing/scripts/categorize/build_imerg-late-run.py` (130 evidence items).
- **Research used:**
  - `about-datasets/imerg-late-run/`: about-pt1, processing-qc-pt2, formats-people-pt3, funding-pt4, news-pt5,
    inputs-pt6 and both halves of the pt7 gap query: Run 2 `calibration-copies-pt7` and Run 1
    `people-production-pt7` (added in the second pass);
  - `instruments/nasa-satellites` (GPM, the calibrator) and `instruments/noaa-satellites` (S-NPP, NOAA-20/21, POES,
    DMSP, Metop, AMSR2, GOES);
  - for the AWS S3 integrity statement only: GHCN-Daily's repository-resilience-pt9.
- **Not used:** `instruments/noaa-rain-gauges` (the Late Run reads no gauges, only a climatology of the Final Run's
  GPCC adjustment) and both `archives/noaa-ncei` runs (no source puts an IMERG copy at NCEI).
- **No longer used:** GPCP Daily's people-production-pt7. The first pass took Huffman's, Bolvin's and Nelkin's
  estimates from it; IMERG's own people run re-checked the same people, so its items replace those three.
- **Not available:** **the NASA GES DISC + PPS A2 repository run** (written, not run), so RRS-2 and RRS-3 have no
  evidence and RRS-1, RRS-4 and RRS-5 are thin.
- **Replaces** the coverage note `imerg-late-run_coverage-gaps.md` (2026-11-23) as the list of open gaps.

## Repositories (the JSON's `dataset` key)

| Repository | Role | Holds |
|---|---|---|
| NASA GES DISC | parent | Half-hourly and daily V07 Late, 1998 to present; on-premises services ended 2026, now Earthdata Cloud only (`gesdisc-cumulus-prod-protected`, AWS us-west-2) |
| NASA PPS | producer site | Near-real-time HDF5 (`jsimpsonhttps`) and IMERG GIS GeoTIFF; keeps Late files until the next version replaces them |

Not repositories: dynamical.org's Zarr on AWS (no DOI), Google Earth Engine (mixes Late with Final), the IRI Data
Library's V06 copy (sunset October 2026), NCAR GDEX (Final Run only), Giovanni, Worldview and the PMM Publisher API
(viewers or 60-day windows). Producer: NASA Goddard (IMERG team, Code 612; PPS, Code 619), and GES DISC is also
Goddard, so `producer_is_repository` is **true** (judgment call below).

## Scores

| Subcategory | Items (for / against / context) | Score | Main reason |
|---|---|---|---|
| P-1 Succession plan | 1 / 2 / 8 | NA (was 0) | A targeted search found no succession plan vs detailed documentation and a documented hand-over to PPS |
| P-2 Retirement-eligible | 2 / 1 / 4 | NA | Only low estimates: Huffman (71–76) and Stocker likely eligible; Tan and Kelley younger |
| P-3 Undocumented knowledge | 3 / 2 / 4 | NA | Production code not public or shared on request; some operating details unwritten vs ATBD and published X-CAL tables |
| P-4 Single point of failure | 2 / 2 / 5 | NA (was 0) | Huffman's four roles with no deputy; Stocker the only named PPS manager vs PPS's Real Time system; work split among organizations |
| D-1 Program defunding | 4 / 1 / 6 | **30** | GPM line $0 after FY2026 pending the Senior Review; FY2027 Earth Science and ESDS cuts pending; DAACs to be replaced (the "against" is a low inference) |
| D-2 Storage single point | 2 / 1 / 2 | NA | GES DISC cloud-only in one region and only two NASA copies vs hosted at both PPS and GES DISC |
| D-3 Access fragile | 3 / 0 / 4 | **20** | GES DISC's on-premises services and subsetters gone; DAAC consolidation; ESDS cut pending |
| D-4 Format obsolescence | 0 / 1 / 3 | **0** | Open HDF5, netCDF and GeoTIFF with a public file spec |
| D-5 Political sensitivity | 0 / 1 / 2 | **0** | No news names IMERG, PPS, GES DISC or the team; GPM on no termination list read |
| DIRS-1 Calibration | 5 / 1 / 3 | NA | GMI the single reference, GPM funding, GMI anomalies, MetOp-C error, climatological CORRA vs X-CAL in-house and current |
| DIRS-2 Observation platforms | 7 / 0 / 3 | **25** | SSMIS, S-NPP ATMS, NOAA-18/19 MHS ended; AMSR2 past life; GPM, Metop-B, Meteosat-9 near end |
| DIRS-3 Upstream supply chain | 6 / 0 / 4 | **20** | Near-real-time feeds broke; CORRA frozen to climatology; Autosnow change; IR outage |
| DIRS-4 External processing | 4 / 3 / 2 | NA | GPROF (CSU), GMU job-control software (agreement ends Aug 2027), CPC IR vs common code in PPS's own system, PDIR-Now computed at PPS, PPS's own production system |
| DIRS-5 No alternative supplier | 3 / 5 / 1 | NA | No backup calibrator, PMM underfunded, no IR substitute vs MWI, overlapping sensors, GEOS FP fallback, other NRT datasets, GPROF-IR to replace PDIR-Now |
| RRS-1 Geographic redundancy | 1 / 2 / 2 | **0** | Only two NASA copies, none verified; GES DISC in one cloud region (the "for" is a low inference) |
| RRS-2 Checksum verification | 0 / 0 / 1 | NA | Not searched (NASA A2 not run) |
| RRS-3 Disaster recovery plan | 0 / 0 / 0 | NA | Not searched (NASA A2 not run) |
| RRS-4 Stable funding | 1 / 3 / 3 | NA | ESDS cut, DAAC consolidation, GPM line $0 vs Congress holding NASA's funding |
| RRS-5 Track record | 3 / 0 / 1 | **15** | Through the 2025 shutdown, Goddard staff losses and the 2026 cloud move with no data loss reported |

Totals: P NA, D NA, DIRS NA, RRS NA, so R* is NA. 11 of 19 subcategories are NA (9 after the first pass).

## Judgment calls to double-check

- **P-1 and P-4 went from 0 to NA** with the people run, as predicted. P-1: the targeted search that found no plan
  (moderate "for") now sits against the documentation items, as GPCP's did. P-4: Huffman's four roles with no deputy
  on the Code 612 org chart, and Stocker as the only named PPS manager, are moderate "for" (the run says
  "supported"); the first pass had Huffman as a low inference. If you read "no deputy named" as too weak for
  moderate, P-4 goes back to 0.
- **P-2 stays NA:** every age is an estimate (low). Huffman and Stocker are "for"; Tan and Kelley are "against", as
  the run reads them; Bolvin, Joyce and Nelkin are context (contractors, no federal rule).
- **ATMOS in D-1** is low "against": the run calls "ATMOS pays the algorithm staff" a moderate inference, but no
  record names IMERG or a task order, and an IDIQ ceiling to 2030 is a vehicle, not funding. As moderate it would
  turn D-1 from 30 to NA.
- **GMU's agreement 80NSSC22M0109** (ends 2027-08-31) is context in D-1 (an end date with no renewal news is not a
  termination) and "for" in DIRS-4 (GMU writes PPS's job-control software).
- **PDIR-Now computed at PPS** is "against" in DIRS-4 (high, from the ATBD); GPROF (CSU code run at PPS) stays "for"
  as third-party software. The first pass's single item mixed the two.
- **GPROF-IR** (V08's replacement for PDIR-Now) is "against" in DIRS-5 as a named successor (moderate: a preprint by
  the IMERG team, abstract checked), and context in P-3 and DIRS-4 because V08 isn't running yet.
- **`producer_is_repository` = true.** The producer is NASA Goddard (PPS runs the code) and both repositories are
  Goddard units, so the site's "same organization" sentence shows. If you'd rather treat PPS and GES DISC as separate
  organizations, set it to false in the script.
- **PPS as a repository** ("producer site"), as the decisions doc's example says. Its copy lasts only until V08 Late
  replaces V07 (context in RRS-1).
- **GEOS FP running** is context in DIRS-3, not "against" (a working feed doesn't show the others safe; GPCP filed
  CPC's IR the same way). As "against" it would make DIRS-3 NA.
- **DIRS-1's "against" item** is X-CAL being done in-house at Goddard and current (v1.11, Aug 2026). DIRS-1 asks about
  an *external* calibration service; GMI as the single reference is "for". Dropping either flips the score.
- **The GPM line in D-1 and RRS-4.** NASA's 2023 Senior Review funded GPM "to support the near real-time processing
  system", so the $0 after FY2026 is read as bearing on PPS's near-real-time system (RRS-4 "against" for PPS).
- **D-4 = 0:** login and licence failures are filed as access, not format (as GPCP did), unlike GHCN-Daily's FAIR item.
- **RRS-5 = 15** rests on no data loss being reported through the 2025 shutdown and the 2026 cloud move (moderate,
  absence of reports). The NASA A2 run may change it.
- **D-1's HQ slide** ("PMM" science team eliminated) is low because "PMM" may mean the planned mission.

## What the research never searched, by subcategory

**Left after the people run (pt7 Run 1).** Most are held by NASA, not published:
- **P-1:** PPS's and the IMERG group's real headcount (not public); why Kidd left the author list (2020–2023; not
  public).
- **P-2:** real birth years and federal service dates for Huffman and Stocker (NASA HR); ages for ATBD co-authors
  Daniel Watters and B. Jason West (not searched); the PPS day-to-day operator is not named, so no age.
- **P-3:** whether PPS would share the production code if asked (ask the PPS help desk); PPS runbooks (not covered);
  the SPEEDe code statement (Tan et al. 2024, GRL).
- **P-4:** who runs the Late Run day to day at PPS and who backs them up (not named anywhere; ask PPS).
- **D-1 and P-4:** PPS's contract and funding line (GSFC procurement; a records request); ATMOS task orders and
  staffing (STC and GSFC).
- **D-1 and DIRS-4:** whether GMU's agreement 80NSSC22M0109 covers PPS, and whether it will be renewed after
  2027-08-31; where V08's GPROF-IR will run.
- **By hand:** `check-by-hand.md` in the run's folder in `Rstar_query_results/web_search_results/` lists unread
  pages (the IPWG-12 V08 slides, pages 2–5 of the staff lists); arxiv.org and ipwg12.imgw.pl were refused by the
  sandbox.

**For the NASA GES DISC + PPS A2 run (RRS, D-2, D-3):**
- **RRS-1 / D-2:** how many copies GES DISC keeps and in which AWS regions; where PPS stores its copy; whether any copy
  is verified against another.
- **RRS-2:** fixity or checksum practice at GES DISC, Earthdata Cloud and PPS, and how often.
- **RRS-3:** disaster recovery or contingency plans at ESDIS, GES DISC and PPS, and when they were last tested.
- **RRS-4:** PPS's budget line; GES DISC's place in the DAAC consolidation; ESDIS Next's award.
- **RRS-5:** holdings and latency at GES DISC and PPS before and after the 2025 shutdown and the 2026 migration.

**Other open items (from the runs' own gaps):**
- **DIRS-2 / DIRS-3:** what PPS's near-real-time stream ingests after SSMIS (30 Sep 2026), AMSR2 (2 Sep 2026) and
  S-NPP ATMS (2 Nov 2026) ended; whether the Late Run uses AMSR3; which Autosnow version it reads; whether the
  near-real-time MetOp-C GPROF has the calibration-file error; Meteosat-12 in CPC's merged IR. **By hand:** the input
  lists in Late Run file headers (free PPS sign-up) settle most of these.
- **DIRS-1:** X-CAL's funding; a backup reference if GMI or DPR stopped.
- **DIRS-5:** model substitutes for GEOS FP; GSMaP_NRT's status (JAXA pages refused).
- **D-5:** mission-list articles not read (Science, CNN, SpaceNews); executive orders not searched.
- **D-4:** CF standard names inside the files.
- **By hand (hosts refused):** JAXA's GCOM-W pages (AMSR2 end), EUMETSAT's IODC page (Meteosat-9) and Metop-B end of
  life; the 2026 Senior Review result for GPM when posted.

## Conflicts between runs

- **NOAA-18/19 MHS:** pt6 counts them as Late Run sounders lost in 2025; pt1's 2023 sensor table says NOAA-19 MHS
  ended as an input in September 2020. Both kept in DIRS-2.
- **L1C ATBD version:** pt2 cites v1.6 (2016), pt3 v1.9 (2022); pt7 settles it: v1.11 (August 2026) is current.
- **GEOS FP:** pt6's forum snippet said "GMAO-FP streams" ended 31 May 2026; pt7 shows GEOS FP running and the end was
  FP-IT.
- **Latency:** 12 h (ATBD Table 3), about 14 h (ATBD text, GES DISC), "almost 13 hr" (Tech Doc), 14–15 h (README.GIS).
  Not used for a score.
- **Licence:** CMR names none, NASA policy says CC0, the AWS Registry says CC BY 4.0. Context in D-4.
- **"PMM" on the May 2026 HQ slide:** the science team or the planned mission. Low in D-1.
- **Kidd's departure:** pt3 put it between 2023 and 2026; pt7 Run 1 shows he left the author list between 2020
  (V06.3) and 2023 (V07). The pt3 item was replaced.
- **Joyce's employer:** his staff page says STC; an August 2026 paper's metadata still gives SSAI. The run follows the
  staff page.
- **ATMOS start date:** NASA's release gives 3 November 2025; USAspending gives 2025-12-01 to 2030-12-01.

## Changes from the first pass

Second pass, 2026-11-24: added `2026-11-24_imerg-late-run-people-production-pt7` (pt7 Run 1).
- **Added 28 items:** P-1 6, P-2 6, P-3 2, P-4 5, D-1 3, DIRS-4 4, DIRS-5 1, RRS-4 1 (in P-1 to P-4, mostly context).
- **Dropped 5 items:** the three GPCP-run items (Huffman, Bolvin and Nelkin, now covered by IMERG's own run), the low
  inference on Huffman's roles in P-4 (now a moderate "for"), and pt3's Kidd item (wrong dates).
- **Rewritten:** the P-1 headcount item (no longer says no run searched for a plan); DIRS-4's GPROF/PDIR item, split
  (PDIR-Now is computed at PPS); DIRS-3's PDIR-Now item (V08 replaces it).
- **Totals:** 107 → 130 items. **Scores:** P-1 0 → NA and P-4 0 → NA; no other score changed. R* stays NA.
