# PERSIANN-CDR Daily: calibration today, possible replacements, current copies

PERSIANN-CDR Daily still depends on two outside inputs, NCEI's GridSat-B1 infrared record and GPCP monthly v2.3. GridSat-B1 changed its calibration reference from HIRS to VIIRS VGAC in October 2024, and its calibration is now written by its long-time author working as a one-person private contractor outside NCEI. No PERSIANN-CDR document says whether its months from October 2024 on use the new calibration. **(Moderate confidence.)** No independent dataset matches its whole profile: daily, 0.25°, 60°S–60°N, from 1983 to the present. CMORPH-CDR (from 1998) and CHIRPS v3 (land only) come closest. The current copies are NCEI's own, AWS and Google Earth Engine, all through 31 July 2026. The IRI/LDEO copy stopped at 30 September 2019, and the Data Rescue Project copy stops at the end of 2024. **(High confidence for the copies.)**

## Calibration and inputs

- **GridSat-B1 changed its calibration reference in October 2024.** NCEI's data flow diagram (Rev 2, October 2025) shows the HIRS calibration input for "1980-9/2024" and VGAC (from NOAA's NODD) for "10/2024 - present". The C-ATBD Rev 2 (03/02/26) is a "Revision to include new calibration procedures using VIIRS/VGAC in lieu of HIRS". It ties the two periods together with one fixed VGAC-to-HIRS adjustment, "to ensure temporal continuity between the HIRS intercalibration record (1980-2024) and VGAC" ([NCEI GridSat-B1 data flow diagram, 2025](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/DataFlowDiagram_01B-02.pdf); [NCEI GridSat-B1 C-ATBD Rev 2, 2026](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/AlgorithmDescription_01B-02.pdf)). **High.**
- **Whether PERSIANN-CDR uses the recalibrated data is not published.** The newest file header (30 July 2026) lists `GRIDSAT-B1.2026.07.30.*.v02r01.nc` and `gpcpv23_m2607.bin`. The GridSat version string is the same before and after the change, so the header can't show which calibration was used ([NCEI ERDDAP, PERSIANN-CDR metadata](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.html)). **Moderate.**
- **Who maintains GridSat's calibration.** The C-ATBD's revision table lists Rev 1 as "Ken Knapp, NCDC" (2015) and Rev 2 as "Ken Knapp, Knapp WeatherSat Services" (2026).
  - Search snippets (pages not opened) give Knapp's own profile saying he "was at NOAA NCEI … from 2003-2025". They also say the company was filed in North Carolina on May 22, 2025 and has one employee ([DuckDuckGo results, snippets only](https://html.duckduckgo.com/html/?q=%22Knapp+WeatherSat+Services%22)).
  - The company's GridSat page (February 2026) says GridSat "is currently being modernized" with "VIIRS-based approaches" ([Knapp WeatherSat Services, 2026](https://knappweathersat.com/gridsat-b1/)).
  - No NCEI successor or contact was found. **Moderate.**
- **Which GPCP version adjusts which years: probably production batches, not a reprocessing.**
  - NCEI's own folder listings show the 2010 and 2013 files still carry 2014 creation dates (`…20100115_c20140523.nc`, `…20130115_c20140908.nc`) ([NCEI access/2010](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2010/); [access/2013](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2013/)).
  - In 2015 the batch changes between 15 June (`c20151028`) and 15 July (`c20160324`) ([access/2015](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2015/)). That matches the header split you describe, `gpcp_m` before and `gpcpv23_m` from July 2015: files made from March 2016 on used v2.3, and older files kept the old v2.2 name.
  - Sadeghi et al. say V2.3 "has replaced V2.2 data for the 2009–2013 period on CHRS data portal and NOAA National Centers for Environmental Information" ([Sadeghi et al., 2019](https://doi.org/10.3390/rs11232755)). NCEI's files show no such replacement.
  - The 2010 and 2013 headers themselves couldn't be read (THREDDS timed out twice), so this is **low** confidence. The V2.3 2009–2013 data may exist only on CHRS's portal.
- **GPCP v2.3's future.** No freeze or end date for GPCP monthly v2.3 was found.
  - GPCP's own team says "V3.3 uses PERSIANN-RAW instead of PERSIANN calibrated by GPCP V2.3" ([Behrangi, IPWG 2026](https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf)).
  - No CHRS statement about moving PERSIANN-CDR to V3.x was found.
  - What was found is a separate CHRS project, PERSIANN-CDR V3: 0.04°, 3-hourly, 1980–2025. It uses "GridSat-B1 (1980–2000; 3-hourly) and CPC-4km (2000–present)" with "a monthly bias correction using GPCP (2.5°)" of unnamed version ([CHRS researcher's GitHub, undated](https://github.com/vndao1193/PERSIANN-CDR-V3)). That would drop GridSat after 2000, but it is an undated personal repository whose paper is "accepted", not published. **Low.**
- **The GridSat change has already stalled a product downstream.** NASA's GPCP V3.3 page says the products "are currently paused at September 2024 because the IR input dataset from NCEI requires a new calibration scheme". The same page lists data to 2025-12-31 and 516 monthly files, which is exactly January 1983 to December 2025 (my count), and is dated 2025-02-12. So the pause sentence is probably older text and V3.3 has since been extended ([NASA GES DISC, GPCPMON V3.3](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpcpmon-3.3)). **Moderate.**

## Alternatives

| Dataset | Producer | Coverage, resolution | Period, latest | Status | Independent of PERSIANN-CDR's inputs? |
|---|---|---|---|---|---|
| CMORPH-CDR V1 | NOAA NCEI/CPC | 60°S–60°N, 0.25° daily (also 8 km, 30 min) | 1 Jan 1998 to June 2026 (2026 folder) | "Ongoing"; made monthly, 3–4 months' latency | Partly: bias-corrected with CPC gauges over land and GPCP pentads over ocean |
| CHIRPS v3 | UCSB CHC, with FEWS NET and USGS | land only, 60°N–60°S, 0.05° | 1981 to near-real time | released 2025-01-01; v2 continues through 2026 | Daily values split from pentads using ERA5 or IMERG Late; IR source not named |
| IMERG Final daily V07 | NASA GPM | global, 0.1° | 1998-01-01 to 2025-09-30 | V07 record ended; V08 expected (search summary: fall 2026) | Yes (different algorithm and inputs) |
| MSWEP V3 | GloH2O (private) | global, 0.1°, hourly | 1979 to present, about 2 h delay | CC BY-NC; non-commercial download by Rclone only | Merges reanalysis and gauges; inputs not checked |
| GPCP V3.3 daily/monthly | NASA/UMD | global, 0.5° | daily from 1998 | not a substitute | No: calibrates PERSIANN-CDR IR precipitation |

Sources by row: [NCEI ISO C00948](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00948) and [NCEI CMORPH 2026 folder](https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/2026/); [CHIRPS v3 README](https://data.chc.ucsb.edu/products/CHIRPS/v3.0/README-CHIRPSv3.0.txt) and [CHC chirps3 page](https://chc.ucsb.edu/data/chirps3) (fetch extract); [GES DISC GPM_3IMERGDF V07](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDF_07/summary); [GloH2O MSWEP](https://www.gloh2o.org/mswep/) (earlier run's extract); [GPCP V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf).

None covers 1983–1997 at daily, 0.25°, ocean-inclusive scale except CDRs built on the same GridSat/ISCCP B1 record. GSMaP, TAMSAT and PERSIANN-CCS-CDR (same producer, so not independent) weren't checked.

## Copies

| Copy | Last date held | Current? | Source |
|---|---|---|---|
| NCEI `/data/precipitation-persiann/access/` | 31 Jul 2026 (file created 2026-10-13) | yes | [NCEI access/2026](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2026/) |
| AWS `noaa-cdr-precip-persiann-pds` (us-east-1, managed by NOAA NODD) | 31 Jul 2026, copied 2026-10-14 | yes, fed from NCEI | [bucket listing](https://noaa-cdr-precip-persiann-pds.s3.amazonaws.com/?list-type=2&prefix=data/2026) (fetch extract); [AWS registry](https://registry.opendata.aws/noaa-cdr-atmospheric/) |
| Google Earth Engine `NOAA/PERSIANN-CDR` | 2026-07-31 | yes, "produced quarterly, with a typical lag of three months" | [Earth Engine catalog](https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR) (fetch extract) |
| IRI/LDEO Data Library | 30 Sep 2019 (page last updated 19 May 2020) | no, frozen; live page needs sign-in | [Wayback copy, 26 Apr 2024](https://web.archive.org/web/20240426080555/https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.CDR/.PERSIANN-CDR/.v01r01/) |
| Data Rescue Project | yearly archives 1983–2024 (archived Apr 24, 2025; 16.0 GB; torrent 17.17 GB with SHA512 sums) | no, one-time snapshot | [DRP portal](https://portal.datarescueproject.org/datasets/precipitation---persiann-climate-data-record-cdr/); [Academic Torrents](https://academictorrents.com/details/448dd345e52d3a0b0953b7f2d86f75089ca61a24) (fetch extract) |

Not checked: the Google Cloud bucket `noaa-cdr-precip-persiann` that [NCEI's product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann) lists.

**NCEI's "pause in operations" notice looks out of date.**
- The page's metadata dates it 8 September 2025 ([NCEI node/8306](https://www.ncei.noaa.gov/node/8306)). Its text is unchanged in captures of 13 September 2025 and 10 June 2026 and on the live page: "a pause in operations due to processing delays. This message will be updated when processing resumes" ([Wayback, 2025-09-13](https://web.archive.org/web/20250913132027/https://www.ncei.noaa.gov/node/8306); [Wayback, 2026-06-10](https://web.archive.org/web/20260610093438/https://www.ncei.noaa.gov/node/8306)).
- It gives no cause beyond "processing delays". It falls in the same period as the GridSat calibration change, but no source links the two.
- Processing has since resumed: the first 2026 files were created on 9 July 2026.
- The product page and the [NCEI Alerts page](https://www.ncei.noaa.gov/alerts) don't mention the pause. The Alerts page does warn of "delayed data archival and slower update cycles for many products" during the cloud migration (16 Nov to 31 Dec 2026). **Moderate.**

## What this means for the four statements

| Statement | Verdict | Why |
|---|---|---|
| DIRS-1 external calibration service could be disrupted | **supports** | GridSat-B1's calibration now rests on VGAC data and on a one-person contractor outside NCEI. GPCP V3.3 was already halted once by the same "new calibration scheme". PERSIANN-CDR's own adjustment rests on superseded GPCP v2.3. |
| DIRS-3 upstream feeds vulnerable | **supports** | Two outside feeds (GridSat-B1, GPCP v2.3). A 2025–26 processing pause happened. Nothing published on a GPCP v2.3 end date or a CHRS switch. |
| DIRS-5 no alternative supplier | **partly contradicts** | CMORPH-CDR, CHIRPS v3, IMERG and MSWEP exist. None matches 1983 start, daily, 0.25°, land and ocean; GPCP V3.3 is not independent. |
| RRS-1 two or more independent sites hold verified copies | **partly supports** | Current data: NCEI, AWS and Earth Engine, all fed by NCEI (not independently made or verified). To 2024: the DRP snapshot with SHA512 checksums. IRI stopped in 2019. |

## Gaps

- **Unresolved conflict:** whether 2009–2013 were replaced at NCEI (Sadeghi 2019 against NCEI's 2014 file dates). The 2009–2013 headers are needed: download one 2010 file from NCEI and read its `source` attribute.
- **Unresolved conflict:** GPCP V3.3's pause note against its listed extent to 2025-12-31. GES DISC holds the answer: its file list.
- **Not published:**
  - whether PERSIANN-CDR months from October 2024 used VGAC-calibrated GridSat (CHRS or NCEI's CDR program would know; not in the C-ATBD or headers);
  - a GPCP v2.3 freeze date (NCEI's C00979 page timed out);
  - an NCEI successor to Knapp.
- **Not read:** the IMERG V08 schedule notice (gpm.nasa.gov, HTTP 504). One host was refused by the sandbox (the AWS S3 listing, read by WebFetch instead); it is listed in `sites-to-trust.md` if you want to consider adding it.
- **Time:** the 30-minute budget, not the evidence, ended the search for GSMaP, TAMSAT and the Google Cloud copy.

## Sources

- [NCEI, GridSat-B1 C-ATBD Rev 2, 2026](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/AlgorithmDescription_01B-02.pdf)
- [NCEI, GridSat-B1 data flow diagram Rev 2, 2025](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/DataFlowDiagram_01B-02.pdf)
- [NCEI ERDDAP, PERSIANN-CDR metadata, 2026](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.html)
- [NCEI, PERSIANN-CDR access/2010](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2010/), [access/2013](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2013/), [access/2015](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2015/), [access/2026](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2026/)
- [NCEI, PERSIANN-CDR processing delay notice (node/8306), 2025](https://www.ncei.noaa.gov/node/8306); Wayback captures [2025-09-13](https://web.archive.org/web/20250913132027/https://www.ncei.noaa.gov/node/8306) and [2026-06-10](https://web.archive.org/web/20260610093438/https://www.ncei.noaa.gov/node/8306)
- [NCEI, PERSIANN-CDR product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann); [NCEI Alerts, 2026](https://www.ncei.noaa.gov/alerts)
- [NCEI, CMORPH-CDR ISO metadata C00948](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00948); [NCEI, CMORPH daily 0.25° 2026 folder](https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/2026/)
- [NASA GES DISC, GPCP V3.3 monthly (Earthdata)](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpcpmon-3.3); [GPCP V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf); [GES DISC, IMERG Final daily V07](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDF_07/summary)
- [UCSB CHC, CHIRPS v3 README, 2025](https://data.chc.ucsb.edu/products/CHIRPS/v3.0/README-CHIRPSv3.0.txt); [UCSB CHC, CHIRPS3 page](https://chc.ucsb.edu/data/chirps3) (fetch extract)
- [AWS Open Data registry, NOAA CDR atmospheric](https://registry.opendata.aws/noaa-cdr-atmospheric/); [AWS bucket listing, 2026](https://noaa-cdr-precip-persiann-pds.s3.amazonaws.com/?list-type=2&prefix=data/2026) (fetch extract)
- [Google Earth Engine, NOAA/PERSIANN-CDR](https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR) (fetch extract)
- [IRI/LDEO Data Library, PERSIANN-CDR v01r01 (Wayback 2024-04-26)](https://web.archive.org/web/20240426080555/https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.CDR/.PERSIANN-CDR/.v01r01/)
- [Data Rescue Project portal, PERSIANN-CDR, 2025](https://portal.datarescueproject.org/datasets/precipitation---persiann-climate-data-record-cdr/); [Academic Torrents, noaa-ncei-precipitation-persiann](https://academictorrents.com/details/448dd345e52d3a0b0953b7f2d86f75089ca61a24) (fetch extract)
- [Sadeghi et al., Remote Sensing, 2019](https://doi.org/10.3390/rs11232755)
- [Behrangi, GPCP V3.3 talk, IPWG 2026](https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf)
- [Knapp WeatherSat Services, GridSat-B1 page, 2026](https://knappweathersat.com/gridsat-b1/)
- [Dao (CHRS), PERSIANN-CDR-V3 GitHub README](https://github.com/vndao1193/PERSIANN-CDR-V3)
- [GloH2O, MSWEP](https://www.gloh2o.org/mswep/) (earlier run's fetch extract)
- [DuckDuckGo results on Knapp WeatherSat Services](https://html.duckduckgo.com/html/?q=%22Knapp+WeatherSat+Services%22) (snippets only)
- [NASA GPM, IMERG V08 transition schedule](https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026) (snippet only; HTTP 504)

Saved in [`web_search_results/2026-11-27_persiann-cdr-calibration-copies/`](web_search_results/2026-11-27_persiann-cdr-calibration-copies/): this answer, the research record, `method.md`, `check-by-hand.md` and `sites-to-trust.md`.
