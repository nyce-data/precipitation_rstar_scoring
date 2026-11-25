# GPCP Daily: what the research didn't search, by subcategory

> **Superseded 2026-11-24:** GPCP Daily is now categorized. See
> [gpcp-daily_categorization-gaps.md](../rstar-pipeline/output/gaps-notes/gpcp-daily_categorization-gaps.md) for what is still open. This note is kept as
> the record of what the pt7 and A2 gap runs were meant to fill.

- **Dataset:** GPCP Daily: 1DD V1.3 (NOAA CDR at NCEI, DOI 10.7289/V5RX998Z) and V3.x Daily (V3.3 CDR C01726 at NCEI;
  V3.2 and V3.3 at NASA GES DISC).
- **Checked:** 2026-11-23, by a coverage check of the six GPCP runs and the shared NCEI, NASA satellite and GHCN-Daily
  pt7 runs, against the 19 subcategories. **Not a categorization:** nothing is in `rstar-pipeline/output/categories/` yet.
  Categorize once the gap runs below come back.
- **Runs read:** `2026-11-19_gpcp-daily-about-pt1`, `2026-11-20_gpcp-daily-qc-formats-pt2`,
  `2026-11-20_gpcp-daily-people-pt3`, `2026-11-20_gpcp-daily-funding-news-pt4`, `2026-11-20_gpcp-daily-inputs-pt5`,
  `2026-11-20_gpcp-daily-satellites-pt6` (in `Rstar_query_results/web_search_results/`).

## Hosts

| Host | Versions | Repository run |
|---|---|---|
| NOAA NCEI (HTTPS, open-data S3) | 1DD V1.3 (archive of record); V3.3 CDR | A1 done (`2026-11-17_noaa-ncei-threats`); A2 written |
| NODD on AWS (`noaa-cdr-precip-gpcp-daily-pds`) and Google | NCEI's copies; version not confirmed | In NCEI's A2 |
| NASA GES DISC (Earthdata Cloud, AWS us-west-2) | V3.2, V3.3 | NASA A2 written; no A1 (NASA budget is in the IMERG runs) |
| NSF NCAR GDEX, Copernicus CDS, GSFC backup FTP, obs4MIPs, Earth Engine, gpcp.umd.edu | various; some not confirmed | Copies only: checked in pt7 |

> **Update 2026-11-23: the NCEI A2 run has come back** (`rstar-pipeline/input/web-research/archives/noaa-ncei/2026-11-23_A2_Rstar_query-noaa_ncei`). It fills the NCEI side of D-2 and RRS-1, RRS-2, RRS-3 and RRS-5 below: no scheduled checksum checks (contradicts RRS-2); the CDR is archived in Asheville with an offsite tape copy only kilometres away, so RRS-1 isn't shown; no DR test is public (RRS-3); no loss reported since 2015 but 8% of Helene's ingest backlog unaccounted (RRS-5). GPCP Daily v1.3's maturity review (DSMR-00163) scores Data Integrity 3.5 with checksums only at ingest and on order; GPCP Daily also has a copy in NCEI's own `climatedatarecords` cloud bucket (low confidence). Rows marked "NCEI A2" still need the other hosts' runs.

## Summary

| Subcategory | Coverage | What's missing | Filled by |
|---|---|---|---|
| P-1 Succession plan | Partly | Any succession or knowledge-transfer plan; head count | pt7 |
| P-2 Retirement-eligible | **Not searched** | ORCID iDs, earliest publication years, ages | pt7 |
| P-3 Undocumented knowledge | Partly | Whether V3.x code is shared on request; runbooks | pt7 |
| P-4 Single point of failure | Partly | Who runs V3.3 production (UMD or Goddard); named operators | pt7 |
| D-1 Program defunding | Covered | MEaSUREs award number and end date; GPCP's share of CISESS | pt7 |
| D-2 Storage single point | Partly | GES DISC storage and backup; where GPCP sits inside NCEI | NCEI A2, NASA A2 |
| D-3 Access fragile | Partly | GES DISC and CDS staffing and funding | NASA A2 |
| D-4 Format obsolescence | Covered | Which version the NODD buckets hold | pt7 |
| D-5 Political sensitivity | Covered (by absence) | — | — |
| DIRS-1 Calibration | Partly | 1DD's SSMIS feed since the RSS CDR ended in 2023; post-GPM calibration plan | pt7 |
| DIRS-2 Observation platforms | Covered | Aqua's end date; DMSP data after September 30, 2026 (watch items) | — |
| DIRS-3 Upstream supply chain | Covered | NCEI's preliminary monthly feed (watch item) | — |
| DIRS-4 External processing | Partly | NASA-side computing; PPS dependence | pt7 |
| DIRS-5 No alternative supplier | Partly | Substitutes for GPCP Daily; a 1DD contingency if F17 or AIRS stops | pt7 |
| RRS-1 Geographic redundancy | Partly | Verified copies per host; which copies are current | pt7, NCEI A2, NASA A2 |
| RRS-2 Checksum verification | **Not searched** | For every host | NCEI A2, NASA A2 |
| RRS-3 Disaster recovery plan | **Not searched** | For every host | NCEI A2, NASA A2 |
| RRS-4 Stable funding | Covered (NCEI); partly (GES DISC, GDEX); not searched (CDS) | GES DISC's own budget line | IMERG pt4 covers NASA's data systems budget |
| RRS-5 Track record | Partly (NCEI); not searched elsewhere | Holdings before and after a disruption | NCEI A2, NASA A2 |

## Notes

- **Calibration is not a blind spot here** in the satellite sense: the chain is documented (pt2, pt5). What's missing is
  the current SSMIS feed for 1DD and who maintains the intercalibration.
- **Already settled (the gap runs shouldn't search them again):** versions, grids, periods and DOIs; algorithms and
  input roles; the satellite list with dates; QC methods; formats and FAIR; funding routes and FY2026–27 figures; the
  news sweep; input threats from 2024 to 2026; NCEI's threats and storage.
- **Gauges:** GPCP's gauges come only through GPCC's global analysis. Whether US COOP or ASOS data reach GPCC is not
  stated in any run (inference), so the US rain-gauge run doesn't bear on it directly.
