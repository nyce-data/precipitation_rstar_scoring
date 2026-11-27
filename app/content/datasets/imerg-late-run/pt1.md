The IMERG Late Run is NASA's near-real-time, multi-satellite precipitation estimate. It is a 0.1° grid every 30 minutes from 1998 on (`GPM_3IMERGHHL`), with a daily product derived from it (`GPM_3IMERGDL`), and it is ready about 12–14 hours after observation. NASA's Precipitation Processing System (PPS) at Goddard makes it with the IMERG team's code. PPS and the GES DISC archive both hold and serve it; Earthdata Cloud (AWS), Google Earth Engine and the visualization tools only redistribute or display it. It is built from a constellation of passive-microwave satellites calibrated to the GPM Core Observatory's radar-radiometer product, gaps filled with NOAA CPC's geostationary infrared, motion from NASA GMAO's GEOS FP model, and a monthly gauge calibration carried over as a climatology from the Final Run. The current version is V07 (V07B on the GES DISC page), running since March 2026 in a "hybrid" mode with V08 microwave inputs; NASA expects V08 no sooner than winter 2026. **Confidence: high** on what it is and where it lives; moderate on exactly which satellites feed today's run.

## The products and the current version

| Product | Short name, version | DOI | Resolution | Latency |
|---|---|---|---|---|
| Late half-hourly | `GPM_3IMERGHHL` V07 (PPS name `3IMERGHH_LATE`) | [10.5067/GPM/IMERG/3B-HH-L/07](https://doi.org/10.5067/GPM/IMERG/3B-HH-L/07) | 0.1° × 0.1°, 30 min | about 14 h (target), 12 h achieved |
| Late daily | `GPM_3IMERGDL` V07 | [10.5067/GPM/IMERGDL/DAY/07](https://doi.org/10.5067/GPM/IMERGDL/DAY/07) | 0.1° × 0.1°, 1 day (mm/day) | a few minutes after the day's last half-hourly file |

Sources: the [GES DISC half-hourly page](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary) and [daily page](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_07/summary), and the [IMERG Technical Documentation, 2023](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf) for the PPS name.

- **The daily product** is the mean of the day's valid half-hours × 24, made from the half-hourly Late files. It "should appear no earlier than 14 hours after the closure of the UTC day" ([GES DISC daily page](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_07/summary)). The IMERG documentation counts daily averages among the value-added products the hosting sites make ([Tech Doc, 2023](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf)).
- **Version, high confidence.** GES DISC says "Version 07B is the current version" ([GES DISC](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary)).
  - **Hybrid mode.** Since March 2026 the Late and Early Runs use "the IMERG V07 algorithm but ingesting GPROF V08". The CORRA calibration has been "set to climatological values" ([GPM, V08 Transition Schedule, Apr 2026](https://gpm.nasa.gov/data/news/imerg-v08-transition-schedule)).
  - **V07C file names.** Earthdata said the minor version in Early and Late file names would change to V07C to mark the change ([Earthdata, GPM V08 Reprocessing](https://www.earthdata.nasa.gov/data/alerts-outages/gpm-version-08-reprocessing)). This run did not confirm the file names now in use.
  - **The V08 switch.** The Late switch to V08 is "no sooner than winter of 2026", after a V08 Final Run that was "more likely" in fall 2026 ([GPM, Aug 2026 update](https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026)).
  - **The Final record.** The V07 Final Run record ended September 30, 2025 ([Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/transition-gpm-imerg-products-v08)).
  - **No V08 release yet.** No V08 release notice turned up as of 2026-11-20, either in [GPM Data News](https://gpm.nasa.gov/data/news) or in a DuckDuckGo search.

## How the Late Run differs from Early and Final

| | Early | Late | Final |
|---|---|---|---|
| Latency | about 4 h | about 12–14 h | about 3.5 months |
| Microwave propagation | forward only | forward and backward | forward and backward |
| Share of microwave sensors waited for | 95% | 100% | 100% |
| GPROF and CORRA inputs | near-real-time GPROF and CORRA | near-real-time GPROF, research CORRA | climate GPROF, research CORRA |
| CORRA calibration window | trailing 45 days | trailing 45 days (climatological since Mar 2026) | centered 45 days |
| Motion vectors | GEOS FP | GEOS FP | MERRA-2 |
| Gauges | "Final Climatological" | "Final Climatological" | GPCC monthly analysis |

Sources: [IMERG ATBD V07, Table 3 (Aug 2026)](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf) and the [GES DISC pages](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary).

The Late Run waits for the next microwave overpasses, so it can interpolate backward as well as forward. It never sees gauges directly. Its estimates get "a monthly climatological concluding calibration based on averaging the concluding calibrations computed in the Final" ([GES DISC](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary)). The Final Run, by contrast, is adjusted to sum to its monthly satellite–gauge combination. **High confidence.**

The latency figure conflicts, but only in how it is defined. GES DISC gives about 14 h, the nominal target. The ATBD and the [GPM data directory](https://gpm.nasa.gov/data/directory) give 12 h ("Minimum Latency: 12 Hours"), the latency now achieved.

## What kind of dataset it is

It is a merged product from many satellites, not from one instrument. In outline ([GES DISC](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary); [ATBD V07](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf)):

1. Each passive-microwave sensor's precipitation is retrieved with GPROF2021. The estimates are gridded and intercalibrated to the GPM combined radar-radiometer product (CORRA).
2. The microwave estimates are moved in time ("morphed") along model-derived motion vectors.
3. A Kalman filter blends them with infrared estimates. The infrared matters most more than about ±90 minutes from an overpass.

**High confidence.**

## Inputs, their roles and who supplies them

| Input | Role in the Late Run | Supplied by |
|---|---|---|
| **GPM Core Observatory: GMI + DPR**, as the combined product CORRA | Calibration reference for every microwave sensor. In hybrid V07, climatological CORRA V07 values are used. No passage found has the DPR entering directly. | NASA (GMI), JAXA (DPR); combined product from the GPM team, processed at PPS |
| **Conical microwave imagers:** GMI; AMSR2 (GCOM-W1); SSMIS (DMSP F16, F17, F18; the 2023 table only estimates their end dates, Dec 2024 to Mar 2026); WSF-M1 MWI (in the Early and Late Runs since 17 Aug 2026) | Precipitation estimates. Imager estimates are preferred over sounder estimates in each grid box. | NASA; JAXA; US DoD (DMSP, WSF-M) |
| **Cross-track microwave sounders:** ATMS (SNPP, NOAA-20, NOAA-21); MHS (MetOp-B, MetOp-C). NOAA-19 MHS ended Sep 2020. | Precipitation estimates, used where no imager estimate exists | NOAA; EUMETSAT |
| SAPHIR (Megha-Tropiques); AMSR3 ("GOSAT-3" in the 2023 table) | SAPHIR: "not used in V07". AMSR3: a sensor slot in the 2026 ATBD, but no evidence found that it has entered IMERG. | CNES/ISRO; JAXA |
| **Geostationary IR:** NOAA CPC merged 4-km IR, from GOES-East/West, Meteosat, Himawari, EWS-G1 | Source of IR precipitation for gaps between overpasses (the KF "observations") | NOAA/NWS CPC assembles it and forwards it to PPS. The satellites belong to NOAA/NESDIS, EUMETSAT, JMA and DoD/NOAA. |
| **PDIR-NOW** (successor to PERSIANN-CCS) | Turns the IR into precipitation. It is recalibrated to the microwave estimates. | UC Irvine CHRS (PERSIANN family). It runs inside IMERG at PPS. |
| **GEOS FP** (MERRA-2 for Final) | Motion vectors from precipitation, liquid water and water vapour fields | NASA GMAO |
| **GPCC gauge analyses** | Final Run only. The Late Run gets a climatology of the Final's gauge adjustment. | DWD GPCC |

Sources:
- the [Tech Doc, Table 10 (2023)](https://arthurhou.pps.eosdis.nasa.gov/Documents/IMERG_TechnicalDocumentation_final.pdf), for sensors and agencies (the imager-before-sounder rule was read only through a subagent's report);
- the [ATBD V07, Tables 1 and 3, sections 3.3.3 and 3.14 (Aug 2026)](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf);
- the [V07 Release Notes (Nov 2024)](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf), for PDIR-NOW replacing PERSIANN-CCS;
- the [CPC 4-km IR satellite list (2025)](https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/CPC-4kmIR-Sats.pdf);
- the [GPM directory entry for CPC IR](https://gpm.nasa.gov/data/directory/ncepcpc-level-3-merged-infrared-brightness-temperatures-0);
- [PPS, WSF-M1 MWI NRT files](https://gpm.nasa.gov/data/news/new-wsf-m1-mwi-nrt-files-available).

Notes:
- **Satellite list.** The satellites named for the present day are those the 2023 table shows as active, plus WSF-M1. The full historical list (TRMM, AMSR-E, DMSP F11–F19, NOAA-15 to -21, MetOp-A/B/C) is in the earlier [GPCP satellites run](../2026-11-20_gpcp-daily-satellites-pt6/answer.md). This run found no published list of exactly which sensors feed today's hybrid Late Run. **Moderate confidence.**
- **PERSIANN-CCS is no longer an input.** The V07 release notes say PDIR-NOW "replaced PERSIANN-CCS", and the 2026 ATBD says CPC forwards IR to PPS "for use in the PDIR computation routines". The GES DISC description still says "PERSIANN-CCS", which is outdated wording. **High confidence.**
- **SSMIS is ending.** SSMIS "provides roughly 25% of the available PMW data in IMERG". The DMSP program was "scheduled to be retired in September 2026". That is why WSF-M1 matters ([GPM, SSMIS–MWI transition, 2025](https://gpm.nasa.gov/sites/default/files/2025-08/SSMIS-MWI_transition.pdf)).

## Producers versus hosts

- **Producers:**
  - The IMERG team at NASA GSFC writes the algorithm.
  - PPS runs it and makes the files.
  - Input producers: CPC (IR), GMAO (model fields), the GPM team and JAXA (CORRA, DPR), the satellite agencies, and UC Irvine (PDIR's method).
  - GES DISC itself derives the daily file from the half-hourly ones.
- **Official archives and servers:** the IMERG files "are hosted on both PPS and GES DISC", and "Secondary archives … exist outside of PPS and GES DISC" ([Tech Doc, 2023](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf)). The access points:
  - **GES DISC**, the long-term archive with the DOIs. Its pages link the Online Archive, Earthdata Search, OPeNDAP and Giovanni: [half-hourly](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary), [daily](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_07/summary).
  - **PPS near-real-time servers** (registration required): HDF5 at `https://jsimpsonhttps.pps.eosdis.nasa.gov/imerg/late/` and GeoTIFF at `…/imerg/gis/` ([GPM data directory](https://gpm.nasa.gov/data/directory)).
- **Cloud copy:** GES DISC's own Earthdata Cloud bucket, `gesdisc-cumulus-prod-protected/GPM_L3/GPM_3IMERGHHL.07/` in AWS us-west-2. It needs Earthdata credentials and carries a CC BY 4.0 licence ([AWS Registry of Open Data](https://registry.opendata.aws/nasa-gpm3imerghhl/)). It is NASA's copy hosted on AWS, not a third-party mirror.
- **Redistributors and viewers:**
  - **Google Earth Engine** `NASA/GPM_L3/IMERG_V07`: producer given as GES DISC, half-hourly, 1998-01-01 to 2026-11-19 ([Earth Engine catalog](https://developers.google.com/earth-engine/datasets/catalog/NASA_GPM_L3_IMERG_V07)). The page doesn't say which run it carries. Its end date, one day ago, implies near-real-time data. **Low confidence on the run.**
  - **The PMM Publisher API** keeps the last 60 days ([GPM data directory](https://gpm.nasa.gov/data/directory)).
  - **NASA Worldview** shows IMERG imagery only ([Earthdata, 2020](https://www.earthdata.nasa.gov/news/feature-articles/explore-20-years-rain-snowfall-data-from-nasas-precipitation-missions)).

## Gaps and uncertainties

- **The record's start date.** GES DISC's daily page gives a record start of 1998-01-01 in its summary, 2000-06-01 in its version table and "beginning 2000" in its text. The V07 reprocessing went back to 1998, so the 2000 figures look out of date. The Earthdata catalog entries also say "beginning 2000" while showing 1998-01-01. GES DISC is the body that can settle it. **Unresolved.**
- **V08.** No V08 release notes or V08 ATBD exist yet. NASA's GPM team will post them on [GPM Data News](https://gpm.nasa.gov/data/news) when V08 Late starts (no sooner than winter 2026).
- **Not checked:** Copernicus or other third-party mirrors, the Worldview/GIBS layer ID for the Late Run, an AWS entry for the daily product, and the exact V07B release date.
- **Sites refused:** the sandbox refused 1 host (developers.google.com).

## Sources

**IMERG team and NASA documentation**
- [NASA GES DISC, GPM_3IMERGHHL V07 dataset page](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary)
- [NASA GES DISC, GPM_3IMERGDL V07 dataset page](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_07/summary)
- [NASA Earthdata, GPM_3IMERGHHL catalog entry](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpm-3imerghhl-07)
- [IMERG Team, IMERG V07 ATBD, rev. Aug 2026](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf)
- [IMERG Team, IMERG Technical Documentation, 13 July 2023](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf)
- [IMERG Team, IMERG Technical Documentation (PPS copy)](https://arthurhou.pps.eosdis.nasa.gov/Documents/IMERG_TechnicalDocumentation_final.pdf)
- [IMERG Team, IMERG V07 Release Notes, Nov 2024](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf)
- [NASA GPM, IMERG V08 Transition Schedule, Apr 2026](https://gpm.nasa.gov/data/news/imerg-v08-transition-schedule)
- [NASA GPM, Update to the IMERG V08 Transition Schedule, Aug 2026](https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026)
- [NASA GPM, Data News](https://gpm.nasa.gov/data/news)
- [NASA GPM, Precipitation Data Directory](https://gpm.nasa.gov/data/directory)
- [NASA GPM, NCEP/CPC merged IR directory entry](https://gpm.nasa.gov/data/directory/ncepcpc-level-3-merged-infrared-brightness-temperatures-0)
- [NASA GPM, New WSF-M1 MWI NRT files available, Aug 2026](https://gpm.nasa.gov/data/news/new-wsf-m1-mwi-nrt-files-available)
- [NASA GPM, Impacts of the transition from DMSP SSMIS to WSF-M MWI on IMERG, 2025](https://gpm.nasa.gov/sites/default/files/2025-08/SSMIS-MWI_transition.pdf)
- [NASA Earthdata, Transition of GPM IMERG products to V08](https://www.earthdata.nasa.gov/data/alerts-outages/transition-gpm-imerg-products-v08)
- [NASA Earthdata, GPM Version 08 reprocessing](https://www.earthdata.nasa.gov/data/alerts-outages/gpm-version-08-reprocessing)
- [NASA GES DISC, CPC 4-km IR satellite list, 2025](https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/CPC-4kmIR-Sats.pdf)

**Hosts and redistributors**
- [AWS Registry of Open Data, NASA GPM_3IMERGHHL](https://registry.opendata.aws/nasa-gpm3imerghhl/)
- [Google Earth Engine, NASA/GPM_L3/IMERG_V07](https://developers.google.com/earth-engine/datasets/catalog/NASA_GPM_L3_IMERG_V07)
- [NASA Earthdata, Explore 20 years of rain and snowfall data, 2020](https://www.earthdata.nasa.gov/news/feature-articles/explore-20-years-rain-snowfall-data-from-nasas-precipitation-missions)
