# USCRN Daily (daily01): what it is, where it lives, what goes in, who makes it

**USCRN Daily (daily01) is NCEI's file set of daily values for the U.S. Climate Reference Network.** Each station has one text file per year, with 28 fields computed from the stations' 5-minute and hourly data over the local-standard-time day. Daily01 runs from 2000 to the present and is updated daily.

**Where it is stored.** Its home and archive of record is a single NCEI server: the FTP and web copies are one and the same, and the weekly snapshots sit beside them. The only geographically independent copy found is the Copernicus Climate Data Store (CDS). That copy is reprocessed, starts in 2006 and is updated once a year. No cloud copy and no ARL copy was found.

**Who makes it.**
- ARL's Atmospheric Turbulence and Diffusion Division (ATDD), with Oak Ridge Associated Universities (ORAU) contractor staff, builds and maintains the 141 stations.
- The stations send their data hourly through NOAA's GOES satellite relay.
- NCEI does all the processing, the archive and public access.

**Confidence:** high for the hosts and inputs; moderate for the organizations (the paying office wasn't found).

## Hosts

| Host | Kind | Current? | What it holds |
|---|---|---|---|
| [NCEI `pub/data/uscrn/products/daily01/`](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/) (also `ftp.ncei.noaa.gov`) | Producer's own data site and archive of record | Yes: 2026 files modified 2026-11-25; `updates/2026` on 2026-11-26 | Yearly folders 2000–2026, plus `updates/` (real-time files also broadcast over NOAAPort) |
| [daily01 `snapshots/`](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/snapshots/) | Versioned copies on the same server | Yes: weekly zips, 2020-10-12 to 2026-11-16 (about 30–44 MB) | The whole daily01 archive as of each date |
| [NCEI USCRN portal](https://www.ncei.noaa.gov/access/crn/products.html) | Producer's site, front end to the files above | Yes | Points to the same directories |
| NCEI's tape archive (HDSS) | Archive of record (back end) | Not stated | "NCEI's data holdings are archived on a Hierarchical Data Storage System" with tape robotics ([USCRN Data Management Plan, 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN_Data_Management_Plan-August_2017.pdf), §8.4) |
| [Copernicus CDS](https://cds.climate.copernicus.eu/datasets/insitu-observations-near-surface-temperature-us-climate-reference-network?tab=overview) | Independent shared archive (Europe), reprocessed copy | Updated "Every year"; download form "temporarily closed" on 2026-11-26 | Sub-hourly to monthly values from 2006, as NetCDF and CSV, with uncertainties added |
| NODD cloud (AWS, Google, Azure) | none | — | No USCRN entry; GHCN-D and GHCN-H are listed ([NOAA NODD list](https://www.noaa.gov/nodd/datasets); [AWS registry](https://registry.opendata.aws/collab/noaa/)) |
| [GHCN-Daily](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt), [GHCNh](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf) | Other NCEI products | — | GHCN-Daily takes in USCRN values (source flag "R = NCEI Reference Network Database"), not daily01's 28 fields. GHCNh has a CRN station flag; its USCRN intake wasn't confirmed |
| ARL / ATDD pages | Operator; links only | — | ARL says NCEI does "all the data management activities … including … data archiving" and serves the data ([ARL](https://www.arl.noaa.gov/research/boundary-layer-characterization/blc-projects-climate-reference-network/)). No full copy was found |
| `ftp.atdd.noaa.gov` | Operator's transfer server, not a copy | Not checked now | NCEI picks up the datalogger files ATDD brings back from site visits "to fill data gaps" here (41 files in Jul–Sep 2017). It also held eclipse-period extracts from the 114 stations ([ARL FY17 Q4 report](https://arl.noaa.gov/wp_arl/wp-content/uploads/documents/activity/quarterly/FY17_04.pdf), p. 11–12, read via Wayback) |

**Identifier and DOI:**
- The current NCEI record is **`gov.noaa.ncdc:C00546`**, "USCRN Quality Controlled Datasets". It covers 2000-11-15 to present, is updated weekly, and gives **DOI 10.7289/V5H13007** ([NCEI metadata](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00546/html); [DataCite](https://api.datacite.org/dois/10.7289/V5H13007)). **High.**
- That DOI covers all four USCRN products. Daily01 has no DOI of its own.
- `C00466` returned no record: a 404 from NCEI's geoportal, a 502 from its landing page, and no web hits. Its meaning is unresolved.

**Against the criteria:**
- **RRS-1** ("two or more geographically independent copies"): partly supported, by the CDS copy only. That copy lags (yearly updates), is reformatted, starts in 2006 rather than 2000, and its downloads were closed on the day checked.
- **D-2** ("storage is a single point of failure"): supported for the current daily01 files. One server holds the live files and their snapshots, and NCEI's plan gives no named second site. It describes backups only as "the latest and best practices". **Moderate.**

## Inputs

**Stations** ([ARL](https://www.arl.noaa.gov/research/boundary-layer-characterization/blc-projects-climate-reference-network/); [NCEI overview](https://www.ncei.noaa.gov/access/crn/overview.html)). **High.**
- Now 141: 114 in the contiguous US, 25 in Alaska (29 planned) and 2 in Hawaii.
- The contiguous-US network was "completed in 2008" ([NCEI](https://www.ncei.noaa.gov/products/land-based-station/us-climate-reference-network)).
- Earlier: 77 commissioned stations at the end of FY2006, after NOAA "formally commissioned the network in January 2004" ([FY06 report](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY06_USCRN_Annual_Report.pdf)). Alaska grew from 2009, to 21 in August 2017 ([ARL FY17 Q4](https://arl.noaa.gov/wp_arl/wp-content/uploads/documents/activity/quarterly/FY17_04.pdf)), 22 in FY2018 ([FY18 report](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY18_USCRN_Annual_Report.pdf)) and 23 around 2021 ([ARL sheet](https://www.arl.noaa.gov/wp_arl/wp-content/uploads/2021/02/Climate-CRN2.pdf), read via Wayback). These counts are from different dates, not a conflict.
- The CDS page's undated "over 130 stations" fits with ARL's 141. The figures here rely on ARL and NCEI.
- The 141 towers got new transmitters by 25 April 2026 (from the earlier run).

**Precipitation instruments, confirmed** ([NCEI Instruments](https://www.ncei.noaa.gov/access/crn/instruments.html)). **High.**
- A Geonor T-200B weighing gauge: "inlet-heated, wind-shielded", with three load cells.
- A Vaisala DRD11A rain detector (the wetness sensor).
- A Hydrological Services America TB-3 auxiliary tipping bucket.
- A Campbell Scientific CR3000 datalogger and a TX320 GOES transmitter.
- The shield is an Alter inside a Small Double Fence (SDFIR) at the 114 contiguous-US sites. A low-porosity double fence is being evaluated as a replacement ([Kochendorfer et al., AMT 2023](https://amt.copernicus.org/articles/16/5647/2023/amt-16-5647-2023.pdf); [Diamond et al. 2013](https://mural.maynoothuniversity.ie/6481/1/PT_US%20climate.pdf)). The Alaska and Hawaii shields weren't found. **Moderate.**

**Data path** ([Diamond et al. 2013](https://mural.maynoothuniversity.ie/6481/1/PT_US%20climate.pdf); [FY19 report](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY19_USCRN_Annual_Report.pdf); [DMP 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN_Data_Management_Plan-August_2017.pdf)). **High.**
- Every hour, stations transmit through the GOES Data Collection System to NOAA's Wallops Island facility. From there the data go by commercial satellite and the Internet to NCEI, with a second path through the USGS EDDN. NOAAPort carries some records.
- In 2019, NCEI's own HRIT receiver replaced DOMSAT as the backup.
- Datalogger files collected at the yearly visits are the definitive record.
- A preliminary feed also goes to MADIS.
- The FY06 report called the network "100% dependent upon the GOES DCS systems for data delivery". No Iridium or cellular backup was found.
- **DIRS-3** ("depends on external data feeds"): supported. Delivery rests on NESDIS's GOES DCS and its ground systems, though there are several downlink paths and the on-site logger keeps a copy.

**How the daily values are made** ([daily01 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt)). **High.**
- All values cover the station's 24-hour local-standard-time day.
- Measured, then summarised: maximum and minimum temperature, precipitation, solar radiation, surface (infrared) temperature, relative humidity, and soil moisture and temperature.
- Derived:
  - `T_DAILY_MEAN` is (max + min) / 2;
  - solar energy is integrated from hourly rates;
  - soil values are averages of hourly values;
  - the official temperature and precipitation come from the three redundant sensors.
- The file has no wind field.
- The README speaks of "10-second" temperature readings, while NCEI's [Measurements page](https://www.ncei.noaa.gov/access/crn/measurements.html) says "two-second". This is unresolved.

**Processing** happens at NCEI on "LRGS, Oracle database on Linux box" (C00546 record).
- **DIRS-4** ("needs outside processing infrastructure"): contradicted. Processing is in-house; only the satellite relay is outside NCEI.

**Current version:** data version 2.1.1 and file format 03 ([readme](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/readme.txt)).
- Version 2.1.1 recalculated precipitation with algorithm OAP 2.1.1, between 2017-06-20 and 2017-06-30.
- It follows version 2.0 (2015) and version 2.1 (May 2016).
- Format 03 began on 7 January 2013, when a surface-temperature-type column was added.

**Start and updates:**
- The program began in FY2001 ([FY06 report](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY06_USCRN_Annual_Report.pdf)).
- The 2000 folder holds only two Asheville, NC test stations.
- The yearly files are "typically updated on a daily basis", and real-time files also go out over NOAAPort.

**How the other products differ:**
- Sub-hourly01 holds 5-minute data from 2006, updated hourly, with UTC and LST times ([README](https://www.ncei.noaa.gov/pub/data/uscrn/products/subhourly01/README.txt)).
- Hourly02 and monthly01 are other aggregations; their READMEs weren't read.
- The Regional network (USRCRN) stations share the daily01 files but lack the solar, surface-temperature, humidity and soil fields. Its 72 Southwest stations were dropped on 1 June 2014.
- Soil moisture appears in daily01 as daily averages. It has its own product for drought use.

## Organizations

| Organization | Role | Source |
|---|---|---|
| NCEI (NESDIS) | Produces and processes daily01, archives it, hosts it and serves it; "manages and coordinates" data access | [NCEI overview](https://www.ncei.noaa.gov/access/crn/overview.html); [ARL](https://www.arl.noaa.gov/research/boundary-layer-characterization/blc-projects-climate-reference-network/) |
| ARL ATDD (OAR, Oak Ridge, TN) | Designed, built and maintains the stations and instruments; calibrates sensors; makes yearly visits (a team of eight); sends site metadata to NCEI; wrote the 2017 DMP; the Program Manager was ATDD-affiliated in 2017 | [ARL story](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/); [DMP 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN_Data_Management_Plan-August_2017.pdf) |
| ORAU (nonprofit government contractor) | Staffs ATDD's USCRN work; installed Alaska stations in 2023 (ORAU's own account) | [ORAU blog](https://orau.org/blog/programs/video-behind-the-scenes-maintaining-the-u.s.-climate-reference-network.html); [ORAU](https://www.orau.org/blog/programs/how-orau-is-connected-to-the-atmospheric-science-work-of-noaa.html) |
| CISESS / NCICS (NC State; cooperative institute) | Ran a "USCRN Applications and Quality Assurance" task (2020–21) | [CISESS annual report 2020–21](https://ncics.org/publications/) |
| NESDIS GOES DCS; USGS EDDN; Microcom (HRIT receiver) | Carry the data, or supply the receiving equipment | [Diamond 2013](https://mural.maynoothuniversity.ie/6481/1/PT_US%20climate.pdf); [FY19 report](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY19_USCRN_Annual_Report.pdf) |
| Site hosts (39 universities, 21 NPS sites, 16 NGOs, 14 refuges and others, FY2010) | Provide land and small resets; their support is needed for "data ingest" | [FY10 report](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY10_USCRN_Annual_Report.pdf), Table 5 |
| Copernicus C3S (ECMWF) | Reprocesses and re-serves a copy | [CDS](https://cds.climate.copernicus.eu/datasets/insitu-observations-near-surface-temperature-us-climate-reference-network?tab=overview) |
| Paying office | **Not found**: no page read names NESDIS or OAR as payer | — |

## Gaps

- **C00466:** unresolved. NCEI's metadata team (ncei.info@noaa.gov) could say what it was.
- **Funding:** which office funds USCRN is in NOAA's budget justification (the "Blue Book" and Congressional Justification), which weren't read.
- **Unread:**
  - the hourly02 and monthly01 READMEs;
  - NCAR EOL dataset 100.023, "NOAA Climate Reference Network (CRN) Data", a possible third-party copy (the page is a JavaScript shell).
- **ATDD's FTP server:** I didn't list its current contents. The 2017 report describes it only as a path for gap-fill files and eclipse extracts.
- **Check by hand:** `check-by-hand.md` lists the unread pages.
- **Follow-up pass:** you approved the one call in `needs-approval.md` (ARL's FY17 Q4 report via Wayback), and it ran in a follow-up pass on 2026-11-26.
- **Sites to trust:** `sites-to-trust.md` lists 2 hosts the sandbox refused (orau.org, mural.maynoothuniversity.ie). You can check whether to add them to your sandbox's allowed domains.

## Sources

**NCEI**
- [NCEI, daily01 directory](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/), [2026 folder](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/2026/), [snapshots](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/snapshots/), [updates](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/updates/), [2000 folder](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/2000/)
- [NCEI, daily01 readme.txt (2017-07-06)](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/readme.txt); [daily01 README.txt](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt); [subhourly01 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/subhourly01/README.txt)
- [NCEI, ISO metadata gov.noaa.ncdc:C00546](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00546/html); [DataCite, DOI 10.7289/V5H13007](https://api.datacite.org/dois/10.7289/V5H13007)
- [NCEI, USCRN Program Overview](https://www.ncei.noaa.gov/access/crn/overview.html); [Instruments](https://www.ncei.noaa.gov/access/crn/instruments.html); [Measurements](https://www.ncei.noaa.gov/access/crn/measurements.html); [Products](https://www.ncei.noaa.gov/access/crn/products.html); [USCRN product page](https://www.ncei.noaa.gov/products/land-based-station/us-climate-reference-network)
- [USCRN Data Management Plan, Aug 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN_Data_Management_Plan-August_2017.pdf); [Data Ingest Functional Specification](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/CRN_Ingest_Functional_Spec.pdf)
- [USCRN annual reports: FY06](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY06_USCRN_Annual_Report.pdf), [FY10](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY10_USCRN_Annual_Report.pdf), [FY18](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY18_USCRN_Annual_Report.pdf), [FY19](https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY19_USCRN_Annual_Report.pdf)
- [NCEI, GHCN-Daily readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt); [GHCNh documentation](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf); [NCEI NODD page](https://www.ncei.noaa.gov/products/ncei-data-noaa-open-dissemination-program)

**ARL and partners**
- [ARL, US Climate Reference Network (BLC project page)](https://www.arl.noaa.gov/research/boundary-layer-characterization/blc-projects-climate-reference-network/) (read in the browser)
- [ARL, Climate-CRN2 sheet, 2021](https://www.arl.noaa.gov/wp_arl/wp-content/uploads/2021/02/Climate-CRN2.pdf) (read via a Wayback copy)
- [ARL, USCRN at ARL](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/)
- [ARL, Quarterly Activity Report FY17 Q4](https://arl.noaa.gov/wp_arl/wp-content/uploads/documents/activity/quarterly/FY17_04.pdf) (read via a Wayback copy)
- [ARL, Upgrading ARL's largest meteorological network, 2026](https://www.arl.noaa.gov/news-pubs/arl-news-stories/upgrading-arls-largest-meteorological-network/)
- [ORAU, Behind the scenes maintaining USCRN](https://orau.org/blog/programs/video-behind-the-scenes-maintaining-the-u.s.-climate-reference-network.html); [ORAU, How ORAU is connected to NOAA](https://www.orau.org/blog/programs/how-orau-is-connected-to-the-atmospheric-science-work-of-noaa.html)
- [CISESS, Annual Report 2020–21](https://ncics.org/publications/) (a landing page; the PDF was read from an earlier run's copy)

**Other**
- [Copernicus CDS, USCRN in situ dataset](https://cds.climate.copernicus.eu/datasets/insitu-observations-near-surface-temperature-us-climate-reference-network?tab=overview)
- [NOAA, NODD dataset list](https://www.noaa.gov/nodd/datasets); [Registry of Open Data on AWS, NOAA](https://registry.opendata.aws/collab/noaa/)
- [Diamond et al. 2013, BAMS (repository copy)](https://mural.maynoothuniversity.ie/6481/1/PT_US%20climate.pdf); [Kochendorfer et al. 2023, AMT](https://amt.copernicus.org/articles/16/5647/2023/amt-16-5647-2023.pdf)

Saved in [`web_search_results/2026-11-26_uscrn-daily-about-pt1/`](web_search_results/2026-11-26_uscrn-daily-about-pt1/answer.md): this answer, the research record, `check-by-hand.md`, `sites-to-trust.md`, `needs-approval.md` and `method.md`.
