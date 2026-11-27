# PERSIANN-CDR Daily: what the research didn't search, by subcategory

> **Categorized 2026-11-27 (first pass), before the pt7 run.** The categorization and what it still lacks are in
> `rstar-pipeline/output/gaps-notes/persiann-cdr-daily_categorization-gaps.md`. The UC Irvine CHRS A2 run came back
> on 2026-11-27 and is used there; pt7 (people and production) is still to rewrite and run, then add with Prompt 5.

- **Dataset:** PERSIANN-CDR Daily, a NOAA CDR (DOI 10.7289/V51V5BWQ, NCEI record C00854), made by UC Irvine's Center
  for Hydrometeorology and Remote Sensing (CHRS).
- **Checked:** 2026-11-23, by a coverage check of the six PERSIANN-CDR runs and the shared NCEI, GHCN-Daily pt7 and
  satellite runs, against the 19 subcategories. **Not a categorization:** nothing is in `rstar-pipeline/output/categories/` yet.
  Categorize once the gap runs below come back.
- **Runs read:** `2026-11-19_persiann-cdr-daily-about-pt1`, `2026-11-19_persiann-cdr-daily-qc-formats-pt2`,
  `2026-11-19_persiann-cdr-daily-about-pt3` (funding), `2026-11-19_persiann-cdr-daily-news-pt4`,
  `2026-11-19_persiann-cdr-daily-inputs-pt5`, `2026-11-19_persiann-cdr-daily-satellites` (in
  `Rstar_query_results/web_search_results/`). No earlier run was about its people.

## Hosts

| Host | Role | Repository run |
|---|---|---|
| NOAA NCEI (HTTPS, THREDDS, ERDDAP) | Archive of record and distributor | A1 done (`2026-11-17_noaa-ncei-threats`); A2 written |
| CHRS, UC Irvine (chrsdata.eng.uci.edu; persiann.eng.uci.edu HTTPS and FTP) | Producer's own data site, with its own copy | CHRS A2 written; no A1 (its funding is the producer's, in pt3 and pt4) |
| NODD on AWS (`s3://noaa-cdr-precip-persiann-pds/`), Google, Azure | Redistributors of NCEI's copy | In NCEI's A2; currency checked in pt7 |
| IRI/LDEO Data Library; Data Rescue Project | Redistributors (IRI possibly frozen at September 2019) | Copies only: checked in pt7 |

> **Update 2026-11-23: the NCEI A2 run has come back** (`rstar-pipeline/input/web-research/archives/noaa-ncei/2026-11-23_A2_Rstar_query-noaa_ncei`). It fills the NCEI side of D-2 and RRS-1, RRS-2, RRS-3 and RRS-5 below: no scheduled checksum checks (contradicts RRS-2); the CDR is archived in Asheville with an offsite tape copy only kilometres away, so RRS-1 isn't shown; no DR test is public (RRS-3); no loss reported since 2015 but 8% of Helene's ingest backlog unaccounted (RRS-5). PERSIANN-CDR v1r1's maturity review (DSMR-00012) scores Data Integrity 3.5 with checksums only at ingest and on order. Rows marked "NCEI A2" still need the other hosts' runs.

## Summary

| Subcategory | Coverage | What's missing | Filled by |
|---|---|---|---|
| P-1 Succession plan | Partly | Any succession plan; who runs production; when the director changed | pt7 |
| P-2 Retirement-eligible | **Not searched** | Everything | pt7 |
| P-3 Undocumented knowledge | Mostly covered | Code since 2014; training code | pt7 |
| P-4 Single point of failure | Partly | Who runs the quarterly extension; whether it is one person | pt7 |
| D-1 Program defunding | Covered | Who pays for the extension since 2014; a successor to NA23OAR4310443 | pt7 |
| D-2 Storage single point | Partly | Where PERSIANN-CDR sits inside NCEI; CHRS's servers and backup | NCEI A2, CHRS A2 |
| D-3 Access fragile | Partly | CHRS portal funding and staff; NCEI's pause notice | CHRS A2, pt7 |
| D-4 Format obsolescence | Covered | CHRS binary layout and licence (minor) | — |
| D-5 Political sensitivity | Covered | — | — |
| DIRS-1 Calibration | Partly | Whether months from 2024 on use the VGAC-recalibrated GridSat; who maintains GridSat's calibration | pt7 |
| DIRS-2 Observation platforms | Covered | When MTG enters ISCCP B1; DMSP after September 2026 (watch items) | — |
| DIRS-3 Upstream supply chain | Covered | Whether GPCP v2.3 will be frozen; the GPCP version per period | pt7 |
| DIRS-4 External processing | Partly | Who pays for and runs CHRS's computers; MATLAB dependence | pt7 |
| DIRS-5 No alternative supplier | Partly | Substitute datasets for PERSIANN-CDR | pt7 |
| RRS-1 Geographic redundancy | Partly | Whether copies are verified and current; CHRS backup | pt7, NCEI A2, CHRS A2 |
| RRS-2 Checksum verification | **Not searched** | NCEI and CHRS | NCEI A2, CHRS A2 |
| RRS-3 Disaster recovery plan | **Not searched** | NCEI and CHRS | NCEI A2, CHRS A2 |
| RRS-4 Stable funding | Covered (NCEI); partly (CHRS) | UC Irvine's institutional support for CHRS | CHRS A2 |
| RRS-5 Track record | Partly | Holdings before and after each event; files lost or delayed | NCEI A2, CHRS A2 |

## Notes

- **Calibration was partly searched** (GridSat's move from HIRS to VIIRS VGAC, monthly adjustment to GPCP), which
  refutes the "never searched" blind spot in part. A physical calibration lab likely doesn't apply to an IR-derived
  product (inference).
- **Already settled (the gap runs shouldn't search them again):** hosts and access points; formats, FAIR ratings and the
  code's availability; how QC is done; the processing chain and quarterly cadence; inputs and the full satellite list;
  funding history through 2014 and the grants table; the 2024–26 news sweep (nothing aimed at the dataset); NCEI-wide
  matters.
