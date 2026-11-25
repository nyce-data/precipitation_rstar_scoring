# IMERG Late Run: what the research didn't search, by subcategory

> **Categorized 2026-11-24 (first pass).** The open gaps are now in
> [imerg-late-run_categorization-gaps.md](../rstar-pipeline/output/gaps-notes/imerg-late-run_categorization-gaps.md). This note is kept as the record of
> what the gap runs were meant to fill. Pt7's run covered only calibration, inputs, alternatives and copies; its
> people half and the NASA GES DISC + PPS A2 run are still to do.

- **Dataset:** IMERG Late Run, version V07 (V08 pending), from NASA's Precipitation Processing System (PPS), archived
  at NASA GES DISC.
- **Checked:** 2026-11-23, by a coverage check of the six IMERG runs and the NASA and NOAA satellite runs, against the
  19 subcategories. **Not a categorization:** nothing is in `rstar-pipeline/output/categories/` yet (and there is no
  `imerg-late-run/` folder). Categorize once the gap runs below come back.
- **Runs read:** `2026-11-20_imerg-late-run-about-pt1`, `2026-11-21_imerg-late-run-processing-qc-pt2`,
  `2026-11-21_imerg-late-run-formats-people-pt3`, `2026-11-21_imerg-late-run-funding-pt4`,
  `2026-11-21_imerg-late-run-news-pt5`, `2026-11-21_imerg-late-run-inputs-pt6`.
- **Rechecked 2026-11-23** after pt6 was copied into `rstar-pipeline/input/web-research/about-datasets/imerg-late-run/` (its
  answer, query and record; its `check-by-hand.md`, `left-out.md`, `sites-to-trust.md` and `method.md` are still only in
  `Rstar_query_results/web_search_results/`). Pt6's own gaps changed DIRS-1, DIRS-2, DIRS-3 and DIRS-4 below; see
  "What pt6 left open".

## Hosts

| Host | Role | Repository run |
|---|---|---|
| NASA GES DISC (Earthdata Cloud, AWS us-west-2) | Archive of record; on-premises services ended in 2026 | NASA A2 written; no A1 (NASA budget is in pt4 and pt5) |
| NASA PPS (`jsimpsonhttps.pps.eosdis.nasa.gov`, IMERG GIS) | Producer's own near-real-time site; keeps Late files until the next version | NASA A2 written |
| dynamical.org Zarr (`s3://dynamical-nasa-imerg`) | Independent third-party copy, no DOI | Copies only: checked in pt7 |
| Google Earth Engine (`NASA/GPM_L3/IMERG_V07`) | Redistributor; mixes Late with Final | Copies only: checked in pt7 |

## Summary

| Subcategory | Coverage | What's missing | Filled by |
|---|---|---|---|
| P-1 Succession plan | Partly | Any succession plan; team sizes; PPS roster | pt7 |
| P-2 Retirement-eligible | **Not searched** | ORCID iDs, earliest publication years, ages | pt7 |
| P-3 Undocumented knowledge | Partly | PPS runbooks; whether the code is shared on request; X-CAL tables | pt7 |
| P-4 Single point of failure | Partly | Who runs the Late Run day to day at PPS; departures since 2024 | pt7 |
| D-1 Program defunding | Covered | PPS funding route; the contract paying SSAI's IMERG staff | pt7 |
| D-2 Storage single point | Partly | PPS storage and failover; Earthdata Cloud single-region risk | NASA A2 |
| D-3 Access fragile | Partly | PPS distribution funding and staff; dynamical.org funding; Earthdata Login | NASA A2, pt7 |
| D-4 Format obsolescence | Covered | CF standard names (minor) | — |
| D-5 Political sensitivity | Partly | Executive orders not searched; some mission lists unread (minor) | — |
| DIRS-1 Calibration | Partly (thin) | Who maintains X-CAL, its funding and versions; the L1C ATBD version conflict; calibration after GPM; whether near-real-time MetOp-C GPROF has the MetOp-B calibration-file error PPS found on 20 Nov 2026; how GPCC's V2025 change reaches the Late Run's climatological calibration | pt7 |
| DIRS-2 Observation platforms | Covered | What PPS's near-real-time stream ingests after SSMIS (30 Sep 2026), AMSR2 (2 Sep 2026) and S-NPP ATMS (2 Nov 2026) ended, and whether the Late Run uses AMSR3; JAXA's AMSR2 end and EUMETSAT's Metop-B and Meteosat-9 end dates (hosts blocked) | pt7 (PPS notices); by hand (JAXA, EUMETSAT) |
| DIRS-3 Upstream supply chain | Covered | JMA forecast input; whether the V07 Late Run uses NOAA's new Autosnow (with AMSR3); whether GEOS FP ended on 31 May 2026 or that was FP-IT; whether CPC's merged IR switched to Meteosat-12 | pt7 |
| DIRS-4 External processing | Partly | GMU CEOSR contract; where PDIR-Now is computed; whether V08 drops PDIR-Now for GPROF-IR | pt7 |
| DIRS-5 No alternative supplier | Partly | Substitutes for CPC IR and GEOS FP; substitutes for the Late Run | pt7 |
| RRS-1 Geographic redundancy | Partly | Whether any copy is verified at a separate site now that GES DISC is cloud-only | NASA A2, pt7 |
| RRS-2 Checksum verification | **Not searched** | GES DISC, PPS, Earthdata Cloud | NASA A2 |
| RRS-3 Disaster recovery plan | **Not searched** | ESDIS, GES DISC, PPS | NASA A2 |
| RRS-4 Stable funding | Covered (GES DISC); partly (PPS) | PPS budget line; dynamical.org sustainability | pt7 |
| RRS-5 Track record | Partly | Holdings and latency before and after the 2025 shutdown and the 2026 migration | NASA A2 |

## Notes

- **Already settled (the gap runs shouldn't search them again):** products, DOIs, V07B status and V08 timing; how Late
  differs from Early and Final; no QC flag; FAIR ratings and the licence conflict; NASA budget lines and the continuing
  resolution to December 11, 2026; NASA and Goddard workforce figures; no news ties cuts to IMERG, PPS or GES DISC; the
  status of every satellite input; the GPM successor picture; GES DISC's cloud migration dates.
- **Inference:** with GES DISC's on-premises services retired, its on-premises and cloud copies may no longer count as
  two independent sites. The NASA A2 run asks.
- **Shared with PERSIANN-CDR:** UC Irvine's CHRS supplies the PDIR-Now method. PERSIANN-CDR's pt7 looks up the CHRS
  people.

## What pt6 left open

Pt6 (inputs) settled what happened to each input from 2024 to November 2026. Its own gaps list, read on recheck, left
these. The first group goes into pt7; the second needs hosts the sandbox refuses.

**Added to pt7:**
- **The near-real-time stream now (DIRS-2):** no PPS or GPM notice says what the Late Run ingests after SSMIS
  (30 Sep 2026), AMSR2 (2 Sep 2026) and S-NPP ATMS (2 Nov 2026) ended, or whether it uses AMSR3. Leads: the unread
  "Details" links on the PPS home page for 30 Sep, 28 Oct and 20 Nov 2026. The input lists in Late Run file headers
  would settle it, but they need a free PPS sign-up, so check those by hand.
- **Calibration (DIRS-1):** PPS found on 20 Nov 2026 that MetOp-C GPROF used MetOp-B calibration files; it stopped
  standard processing but near-real-time continues, and no source says whether that stream has the same error. How
  GPCC's V2025 change (Full Data merged with Monitoring) reaches the Late Run's climatological calibration is unstated;
  the V07 ATBD (13 Aug 2026) may say.
- **Upstream feeds (DIRS-3):** NOAA's new Autosnow includes AMSR3, and PPS's standard V08 GPROF ignored it in Aug–Sep
  2026; whether the V07 Late Run uses it is unknown. An unread Earthdata Forum reply says "GMAO-FP streams" ended on
  31 May 2026, while GMAO's own pages show GEOS FP running on 21 Nov 2026 (it may mean FP-IT). Whether CPC's merged IR
  switched to Meteosat-12 is unknown.
- **PDIR-Now (DIRS-4, DIRS-5):** an IMERG-team preprint presents GPROF-IR as V08's IR retrieval. Whether V08 drops
  PDIR-Now, and with it the CHRS dependency, is not stated (inference).

**By hand (pt6's `check-by-hand.md`; the hosts are in its `sites-to-trust.md`):**
- JAXA's GCOM-W pages, for whether AMSR2 observing or distribution ended on 2 Sep 2026 (would move AMSR2 from emerging
  to imminent);
- EUMETSAT's IODC page and 2024 Annual Report, for Meteosat-9's end date and Metop-B's end of life.

These are input status (DIRS-2), already rated by pt6, so pt7 doesn't search them unless `jaxa.jp` and `eumetsat.int`
are added to the research project's allowed domains.
