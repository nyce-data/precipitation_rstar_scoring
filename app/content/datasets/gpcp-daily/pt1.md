GPCP Daily is a blended, satellite-based record of daily global precipitation. Gauges enter only indirectly, because each day is scaled to the GPCP monthly product, which holds the GPCC gauge analysis. It comes in two families. The 1° One-Degree Daily (1DD, now Version 1.3, October 1996 to present) is a NOAA Climate Data Record. The University of Maryland (ESSIC, PI Robert Adler) computes it and NOAA NCEI archives it. The 0.5° Version 3 daily (V3.2, then V3.3 from January 1998) was built under NASA's MEaSUREs program by a NASA Goddard–UMD–University of Arizona team. NASA GES DISC hosts it, and since 2025 NCEI also publishes a V3.3 CDR copy. V3.3 is the current version, and V1.3 is being superseded but is still extended. NCAR GDEX and Copernicus CDS only redistribute. **Confidence: high** on versions, inputs, method and roles; **moderate** on the current end dates and on V1.3's status, where the sources disagree.

## Versions and years

| Version | Grid | Period | Status | Main home |
|---|---|---|---|---|
| 1DD V1.2 | 1° | from Oct 1998 | superseded; data still at an old NCEI address | NCEI (www1.ncdc.noaa.gov/pub/data/gpcp/daily-v1.2/) |
| 1DD V1.3 (CDR 01B-35) | 1° | Oct 1996 – Aug 2026 (newest file) | still extended; NCEI's V3.3 record labels it "Version Superseded" | NOAA NCEI |
| V3.2 daily (GPCPDAY 3.2) | 0.5° | Jun 2000 – Sep 2021 | superseded by V3.3 | NASA GES DISC |
| V3.3 daily (GPCPDAY 3.3; NCEI CDR C01726) | 0.5° | Jan 1998 – Dec 2025 (newest granule) | current | NASA GES DISC; NOAA NCEI |

Sources by row: V1.2, V3.2 and V3.3 from NASA CMR's collection and granule metadata ([NASA CMR, 2026](https://cmr.earthdata.nasa.gov/search/collections.json?keyword=GPCP%20daily&page_size=50); [newest V3.3 granule](https://cmr.earthdata.nasa.gov/search/granules.json?short_name=GPCPDAY&version=3.3&sort_key=-start_date&page_size=2); [newest V3.2 granule](https://cmr.earthdata.nasa.gov/search/granules.json?short_name=GPCPDAY&version=3.2&sort_key=-start_date&page_size=1)). V1.3 from NCEI's access directory, whose newest file is `gpcp_v01r03_daily_d20260831_c20261109.nc` ([NCEI, 2026](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2026/)). The NCEI V3.3 CDR from its ISO metadata, which gives 1998-01-01 to present and was issued 2025-08-05 ([NCEI C01726](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01726)).

**Start dates differ by version.**
- When it was first published, the 1DD covered 1 January 1997 – 30 April 1999, with new months "appended a few months after real time" ([Huffman et al., 2001](https://ntrs.nasa.gov/api/citations/20000068519/downloads/20000068519.pdf)).
- V1.2 starts in October 1998, with "a delay of two to three months".
- The reprocessed V1.3 reaches back to October 1996.
- The V3 Daily ATBD's revision history dates the documents, not the data releases: V3.1 (9 June 2021), V3.2 (1 February 2022), V3.3 (11 February 2025) and "V3.3 completed" (12 June 2026).

**How it relates to the monthly and pentad.** Each daily version is scaled so its days sum to a companion GPCP monthly. V1.3 uses Monthly V2.3 ([NCEI C-ATBD, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)), and V3.2/V3.3 use the V3.2/V3.3 Monthly ([GES DISC V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)). The pentad is a separate product. For V3, NASA says only that a 0.5° pentad "may be added" ([NASA CMR, 2026](https://cmr.earthdata.nasa.gov/search/collections.json?keyword=GPCP%20daily&page_size=50)).

**Conflicting end dates (moderate).**
- The V3.3 release notes say production was "paused at March 2024" while NCEI recalibrates the GridSat IR input ([GPCP V3.3 Release Notes](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)). The notes are dated 11 March 2025 on the title page and 5 March 2025 in the page footers.
- NASA's catalog says "paused at September 2024" ([NASA Earthdata GPCPDAY 3.3](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpcpday-3.3)).
- Yet the newest V3.3 granule is for 2025-12-31, and a 2026 IPWG talk gives "01/1998-12/2025" ([Behrangi et al., IPWG-12, 2026](https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf)).
- The V3.3 Daily ATBD explains part of this: October–December 2025 "was computed with IMERG V07 Late instead of IMERG V07 Final", because IMERG Final ended at September 2025. So the record was extended after the pause notices were written. No dated notice of the restart was found.

V1.3 is also unsettled. NCEI's V3.3 record says the V1.3 landing page "should not be used except in rare cases", yet NCEI added V1.3 files for data to 2026-08-31 on 2026-11-10. NCEI's product page still describes only the 1° record ([NCEI product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily)).

## Where it lives

**Producers' archives:**
- **V1.3:** NOAA NCEI is the archive of record ([NCEI product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily); [NCEI C00999](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00999)). DOI [10.7289/V5RX998Z](https://doi.org/10.7289/V5RX998Z). Access:
  - HTTPS directory: https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/
  - Google Cloud: https://console.cloud.google.com/storage/browser/noaa-cdr-precip-gpcp-daily
  - AWS: https://noaa-cdr-precip-gpcp-daily-pds.s3.amazonaws.com/index.html
- **V3.3 at NASA GES DISC:**
  - Landing page: https://disc.gsfc.nasa.gov/datasets/GPCPDAY_3.3/summary
  - DOI: 10.5067/MEASURES/GPCP/DATA307
  - Downloads, S3 and OPeNDAP links listed in CMR, for example https://data.gesdisc.earthdata.nasa.gov/data/GPCP/GPCPDAY.3.3/
- **V3.2:** GES DISC, under GPCPDAY.3.2.
- **V3.3 at NOAA NCEI:** DOI [10.25921/9b5m-ka77](https://doi.org/10.25921/9b5m-ka77), served from NOAA's open-data bucket at `archive.data.noaa.gov/climatedatarecords#UMD_ESSIC/GPCP/Daily/GPCP-D-CDR_01B-35/` ([NCEI C01726](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01726); [data.gov record](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-the-global-precipitation-climatology-project-gpcp-daily-ve)). NCEI's own access directory holds only V1.3 files.

**Hosts that only redistribute:**
- **NSF NCAR GDEX:**
  - d728007 holds V1.3, 1996-10-01 to 2024-11-01, and names "DOC/NOAA/NESDIS/NCEI | UMD/ESSIC" as data contributors ([GDEX d728007](https://gdex.ucar.edu/datasets/d728007/)).
  - d728009 holds V3.2, with "roughly quarterly updates" ([GDEX d728009](https://gdex.ucar.edu/datasets/d728009/)).
- **Copernicus Climate Data Store "satellite-precipitation":**
  - v1.3 runs October 1996 to March 2024, v3.2 June 2000 to September 2021, and v3.3 January 1998 to present.
  - v1.3 is provided "on behalf of GPCP" and v3.2/v3.3 "on behalf of" GES DISC ([Copernicus CDS](https://cds.climate.copernicus.eu/datasets/satellite-precipitation?tab=overview)).
- **NOAA PSL:** no GPCP daily product was found there; it lists GPCP V2.3 monthly.

## What kind of dataset: inputs and roles

Both families are **blends of several satellites, scaled to a gauge-informed monthly**. Neither is a single-instrument record. The V1.3 C-ATBD says microwave estimates and gauge analyses "are not explicitly used". The V3 daily, in its ATBD's words, computes "no precipitation estimates" of its own.

| Input | Provider | Instruments, satellites | Role in V1.3 (1DD) | Role in V3.2/V3.3 |
|---|---|---|---|---|
| Geostationary IR, 3-hourly Tb histograms | NOAA CPC ("IR 3 hourly files"; NCEI's V3.3 lineage names "Globally Merged IR data") | GOES, Meteosat, GMS, MTSAT, with NOAA polar-orbiter IR filling gaps | main input in 40°N–40°S (TMPI) | not used directly; enters inside IMERG (GridSat-B1 before Feb 2000, CPC IR after) |
| Leo-IR GPI | (AVHRR) | AVHRR on NOAA polar orbiters | fills gaps in 40°N–S | not used |
| Passive microwave (GPROF) | RSS Tb CDRs at NCEI | SSM/I on DMSP F13 (1996–2008), SSMIS on F17 (2009–) | sets the TMPI's rain frequency (calibration) | not used directly; inside IMERG |
| IR sounders | GPCP/GSFC (TOVS); GES DISC (AIRS V6) | TOVS on NOAA satellites; AIRS on Aqua | main input poleward of 40° | main input poleward of 55° (TOVS to Aug 2002, IR-only AIRS from Sep 2002), histogram-matched to IMERG |
| IMERG Final (V06 for V3.2, V07 for V3.3) | NASA GES DISC (GPM) | GPM/TRMM constellation microwave plus geo-IR | not used | main input in 55°N–S |
| GPCP Monthly (V2.3; V3.2/V3.3) | GPCP (NCEI; GSFC) | satellite–gauge blend incl. GPCC | scales each month's total | scales each month's total (ratio capped at 0.2–4) |
| GPCC gauge analysis | DWD GPCC | rain gauges (direct measurements) | only through the monthly | only through the monthly |

Sources by row: V1.3 from the NCEI C-ATBD, Section 3.1 and Table 1 (p. 11), and its data flow diagram ([NCEI C-ATBD, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf); [NCEI data flow diagram](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/DataFlowDiagram_01B-35.pdf)). V3.x from the GES DISC Daily ATBDs, Table 1 and Section 3.4 ([V3.2 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf); [V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)). The GridSat and CPC split inside IMERG is from the [V3.3 Release Notes](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf).

The V1.3 C-ATBD conflicts with itself on AIRS: Table 1 starts it in 2003, while its text says it follows TOVS "in 2005". NCEI's V3.3 CDR metadata lineage still lists V1.3-style inputs (GPCC, CPC merged IR, RSS SSMI/SSMIS, AIRS V6) and no IMERG, against the ATBD; this is likely carried over from the V1.3 record (**low confidence**).

## How the data are made

Every step is algorithmic. Gauges, the only direct measurements, reach the daily only through the monthly scaling.
- **V1.3 (1DD):** the Threshold-Matched Precipitation Index (TMPI) is a GOES Precipitation Index-type method. Its IR threshold is set each month so IR "cold" coverage matches SSM/I rain frequency. A single rain rate then makes the month sum to the GPCP Monthly.
  - Poleward of 40°, TOVS/AIRS rain days are cut to match the TMPI at 40° and rescaled to the monthly, with smoothing across 40–50°.
  - It is updated "two months after the end of the month" ([NCEI C-ATBD, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf); [Huffman et al., 2001](https://ntrs.nasa.gov/api/citations/20000068519/downloads/20000068519.pdf)).
- **V3.2/V3.3:**
  - IMERG Final half-hourly 0.1° is averaged to 0.5° daily and thresholded at 0.24 mm/d.
  - TOVS/AIRS is histogram-matched to IMERG.
  - IMERG is used in 55°N–S and TOVS/AIRS poleward, with the seam "feathered".
  - Each day is then ratio-adjusted to the Monthly ([V3.2 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf)).
  - Updates were "roughly quarterly" ([GDEX d728009](https://gdex.ucar.edu/datasets/d728009/)); NCEI's V3.3 metadata gives a monthly maintenance frequency.
  - GPCP V4 is planned: a daily from 1983 at 0.1° with 2-week latency, targeting mid 2027 ([Behrangi et al., 2026](https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf)).

## Who is responsible

- **V1.3 producer:**
  - The University of Maryland computes it and submits it to NCEI: PI Robert Adler, processor UMD/ESSIC ([NCEI C-ATBD, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf); [NCEI C00999](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00999)).
  - NCEI's lineage calls it "a joint effort between the University of Maryland and NASA".
  - The NOAA CDR Program "formalize[s] its production". NCEI is the archive, publisher and distributor.
- **V3.2/V3.3 producer:**
  - It was developed under NASA MEaSUREs. The PI is Ali Behrangi, University of Arizona; the first V3 MEaSUREs project was led by George Huffman, SSAI ([V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf); [NASA MEaSUREs project page](https://www.earthdata.nasa.gov/about/competitive-programs/measures/next-generation-global-precipitation-climatology-project)).
  - The authors are at NASA GSFC, SSAI, UMD and the University of Arizona ([V3.3 Release Notes](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)). GES DISC hosts it.
  - NCEI's V3.3 CDR copy "is currently computed by the University of Maryland and submitted to NCEI" ([NCEI C01726](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01726)).
  - ESSIC writes that NASA MEaSUREs supports CDR development and NCEI supports the routine monthly ICDR ([ESSIC, 2026](https://essic.umd.edu/global-precipitation-summary-for-may-2026/)).
- **Umbrella program:** GPCP is a WCRP/GEWEX project under the GEWEX Data and Assessments Panel (GDAP) ([NCEI product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily)). GEWEX's current GDAP projects page did not list GPCP when read ([GEWEX GDAP projects](https://www.gewex.org/panels/gewex-data-and-analysis-panel/gdap-projects/)).
- **Earlier set-up (V2.2 era, 2013):** a consortium did the work. The merge was at NASA Goddard/UMD, gauges at DWD's GPCC, microwave at NOAA NESDIS and George Mason University, and geostationary IR and the pentad merge at NOAA CPC. Operations were moving to NCDC under the CDR Program ([Sapiano et al., AMS 2013](https://ams.confex.com/ams/93Annual/webprogram/Handout/Paper220154/Sapiano_GPCPcdr_AMS_jan13.pdf)) (**moderate**).

## Gaps

- **Which group runs routine V3.3 production for GES DISC:** not stated. The producers hold this (GES DISC help desk, or the GPCP team at ESSIC).
- **When V1.3 will stop, and when the V3.3 restart happened:** no NCEI notice was found. NCEI's V3.3 landing page returned 503 and has no Wayback copy; its ISO XML was read instead.
- **Not read:**
  - Huffman et al. 2023, *J. Climate* (AMS returns 403); the V3.2 Daily ATBD covers its method.
  - The C3S Confluence V3.3 README (the sandbox refused the host, and the browser page did not load).
  - Which CPC IR product V1.3 uses: not stated.
- **Hosts not checked:** obs4MIPs/ESGF, Google Earth Engine, gpcp.umd.edu, and the Google and AWS bucket listings.


## Sources

- [NOAA NCEI, Precipitation - GPCP Daily C-ATBD (CDRP-ATBD-0913, 01B-35), 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)
- [NOAA NCEI, GPCP Daily V1.3 Data Flow Diagram, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/DataFlowDiagram_01B-35.pdf)
- [NASA GES DISC, ATBD for GPCP V3.2 Daily](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf)
- [NASA GES DISC, ATBD for GPCP V3.3 Daily](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)
- [Huffman et al., GPCP V3.3 Release Notes, 2025](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)
- [Huffman et al., Global Precipitation at One-Degree Daily Resolution from Multi-Satellite Observations, J. Hydrometeor. 2001 (NTRS manuscript)](https://ntrs.nasa.gov/api/citations/20000068519/downloads/20000068519.pdf)
- [Huffman et al., GPCP Version 3.2 poster, NTRS 2023](https://ntrs.nasa.gov/api/citations/20230012664/downloads/20230012664%20Huffman%20G%20poster.pdf)
- [Behrangi et al., The Newly Released GPCP V3.3 Daily and Monthly Products and Efforts Towards GPCP V4.0, IPWG-12, 2026](https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf)
- [Sapiano et al., GPCP Current Status and Transfer to Operations at NCDC, AMS 2013 poster](https://ams.confex.com/ams/93Annual/webprogram/Handout/Paper220154/Sapiano_GPCPcdr_AMS_jan13.pdf)
- [NASA Earthdata, Next-Generation GPCP Data Products (MEaSUREs project page)](https://www.earthdata.nasa.gov/about/competitive-programs/measures/next-generation-global-precipitation-climatology-project)
- [ESSIC (UMD), Global Precipitation Summary for May 2026](https://essic.umd.edu/global-precipitation-summary-for-may-2026/)
- [NOAA NCEI, Precipitation - GPCP Daily CDR product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily)
- [NOAA NCEI, GPCP CDR V1.3 (Daily) landing page C00999 (Wayback copy of 2026-10-24)](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00999)
- [NOAA NCEI, NOAA CDR of GPCP Daily Version 3.3, C01726 (read as ISO XML)](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01726)
- [NOAA NCEI, GPCP Daily access directory](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/) and [its 2026 folder](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2026/)
- [data.gov, NOAA CDR of GPCP Daily Version 3.3 (catalog record)](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-the-global-precipitation-climatology-project-gpcp-daily-ve)
- [NASA CMR, GPCP daily collection metadata](https://cmr.earthdata.nasa.gov/search/collections.json?keyword=GPCP%20daily&page_size=50), [latest V3.3 granules](https://cmr.earthdata.nasa.gov/search/granules.json?short_name=GPCPDAY&version=3.3&sort_key=-start_date&page_size=2), [latest V3.2 granule](https://cmr.earthdata.nasa.gov/search/granules.json?short_name=GPCPDAY&version=3.2&sort_key=-start_date&page_size=1)
- [NASA Earthdata, GPCPDAY V3.3 catalog entry](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpcpday-3.3)
- [NSF NCAR GDEX, d728007 (GPCP CDR V1.3 Daily)](https://gdex.ucar.edu/datasets/d728007/)
- [NSF NCAR GDEX, d728009 (GPCP V3.2 Daily)](https://gdex.ucar.edu/datasets/d728009/)
- [Copernicus Climate Data Store, satellite-precipitation](https://cds.climate.copernicus.eu/datasets/satellite-precipitation?tab=overview)
- [GEWEX, GDAP Current Projects](https://www.gewex.org/panels/gewex-data-and-analysis-panel/gdap-projects/)
