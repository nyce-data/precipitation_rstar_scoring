# GHCN-Daily: what it is, where it is kept, who makes it

GHCN-Daily (GHCNd) is a **compilation** of daily station records, such as rain-gauge totals, snowfall, snow depth and maximum and minimum temperatures. NCEI merges the records from more than 25 networks and national weather services into one quality-checked archive of more than 100,000 land stations in 180 countries and territories ([NCEI product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)). It doesn't blend gauges with satellites, and it isn't a single network. NOAA's National Centers for Environmental Information (NCEI, part of NESDIS) compiles, archives and serves it. NCEI's metadata names a "GHCNd Operations Team" as point of contact and Matthew Menne and Imke Durre as principal investigators. It is updated daily and rebuilt every weekend. **Confidence: high**, except where noted.

## Where it lives (high)

- **Archive:** NCEI is the holding archive. Each daily update gets its own version number and is archived at NCEI ([NCEI product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)). The developers' paper says every version is kept "in perpetuity" ([Menne et al. 2012](https://doi.org/10.1175/JTECH-D-11-00103.1)). GHCN-Daily is also the official archive for U.S. Cooperative Observer (COOP) data.
- **Identifiers:** DOI [10.7289/V5D21VHZ](https://doi.org/10.7289/V5D21VHZ). NCEI metadata record gov.noaa.ncdc:C00861, also DSI 9101_01 and "daily-summaries" in NCEI's access service ([NCEI ISO record](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html)).
- **NCEI access points:**
  - HTTPS directory [www.ncei.noaa.gov/pub/data/ghcn/daily/](https://www.ncei.noaa.gov/pub/data/ghcn/daily/): per-station files, `ghcnd_all.tar.gz` (3.8 GB, dated 2026-11-17), GSN and HCN subsets, station and inventory lists, readme, status and version files.
  - [www.ncei.noaa.gov/data/global-historical-climatology-network-daily/](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/) ("NCEI Direct Download" in the ISO record).
  - Climate Data Online, which the product page lists as an access method.
  - The readme still names the retired `ftp.ncdc.noaa.gov` address ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)).
- **Cloud copies:**
  - **AWS:** S3 bucket `noaa-ghcn-pds` (us-east-1), through NOAA's Open Data Dissemination program, updated daily ([AWS Registry of Open Data](https://registry.opendata.aws/noaa-ghcn/)).
  - **Google:** BigQuery public dataset `bigquery-public-data.ghcn_d`, with an expected update frequency of daily ([Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d); [Google Cloud blog, 2016](https://cloud.google.com/blog/products/gcp/global-historical-daily-weather-data-now-available-in-bigquery)). NCEI's ISO record links both cloud copies.
  - **Microsoft:** no Planetary Computer copy was found. Only NClimGrid, a gridded product derived from GHCN-D, turned up there (low confidence: two searches).
- **Caveat:** NCEI's product page currently warns that its move to the cloud means "delayed data archival and slower update cycles for many products."

## What kind of dataset it is (high)

**A multi-network, multi-country compilation of station observations.** NCEI says it integrates "more than 25 data source components" (product page). Its metadata record says "approximately 30" (ISO record), and the 2012 paper said "20+". The figures differ because the number of sources grew over time. The sources fall into four groups:
1. **The U.S. collection:** a dozen NCEI datasets.
2. **The international collection:** about 20,000 locations in more than 100 countries, from the earlier Global Daily Climatology Network.
3. **Government exchange data:** GCOS stations and bilateral agreements. Canada gave more than 7,500 station records and Australia more than 17,000; ECA&D gave over 1,500 stations in more than 50 countries (2012).
4. **The Global Summary of the Day:** summaries derived from synoptic (SYNOP) reports sent over the Global Telecommunication System (GTS).

**Source networks and data streams.** The readme's source flags name each stream ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt), Version 3.35):
- **U.S. COOP:** 0, 6, 7 and K. These are the DSI-3200 and CDMP summaries, reports sent through WxCoder3, and forms keyed from paper.
- **U.S. NWS feeds:** CF6 summaries (1), and High Plains Regional Climate Center feeds (D, d, H).
- **ASOS:** A, B and M, plus W (WBAN/ASOS summaries from the Integrated Surface Database, ISD).
- **Other U.S. networks:** First-Order stations (X), the Climate Reference Network (R), CoCoRaHS (N), SNOTEL (T) and RAWS (U).
- **National services:** Environment Canada (C), ECA&D (E), Australia (a), and GCOS or other government data (G).
- **Other national contributions:** Mexico's CONAGUA, Russia, China, Fiji, Belarus, Ukraine and Uzbekistan.
- **The international collection (I), and GSOD (S) with its successor SSODv2 (2), which since January 2026 is derived from GHCNh** ([status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)).

**Counts by network.** NCEI publishes no current count or share of stations per source. As a stand-in, this run counted the station list ([ghcnd-stations.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt), file of 2026-11-13) by the network code in each station ID. That code is a numbering system, not the source of each value: one station can mix several sources. The list includes closed stations (**moderate**):

| ID network code | Station entries | Share |
|---|---|---|
| CoCoRaHS (`1`) | 53,167 | 40.0% |
| National met/hydro service numbers (`N`) | 30,703 | 23.1% |
| U.S. Cooperative Network (`C`) | 23,115 | 17.4% |
| Unspecified (`0`) | 13,188 | 9.9% |
| ECA&D (`E`) | 5,087 | 3.8% |
| WMO (`M`) | 3,116 | 2.3% |
| WBAN (`W`) | 2,293 | 1.7% |
| RAWS (`R`) | 1,509 | 1.1% |
| SNOTEL (`S`) | 859 | 0.6% |
| Pre-Coop (`P`) | 4 | 0.0% |
| **All entries** | **133,041** (78,570 U.S.) | |

*Source: counted by this run from NCEI's ghcnd-stations.txt (script and output in the run folder); code meanings from the readme, section IV. These are entries listed, not an official total.*

The only published per-source counts date from 2012 ([Menne et al. 2012](https://doi.org/10.1175/JTECH-D-11-00103.1), Table 2):

| Source (2012) | Stations |
|---|---|
| COOP DSI-3200 | over 20,000 |
| CDMP COOP | more than 11,000 |
| First-Order | about 1,600 |
| ASOS (2000–05) | nearly 900 |
| HPRCC real-time | "several thousand" |

The same paper says about 70% of all values came from North American stations. Version 3.00 (September 24, 2012) added SNOTEL (668 stations) and RAWS (1,453 permanent stations) ([status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)). About half the stations report precipitation only, and records run from under a year to more than 175 years (product page).

**How the sources are merged.** The product page and the 2012 paper describe the same three steps:
1. **Screening.** Stations of unknown or questionable identity are dropped. So are within-source duplicates, meaning records more than 50% identical: the longer record is kept if the two sites are within 40 km, and neither if they are farther apart.
2. **Matching.** Each station is matched to an existing GHCN-Daily station by network ID, then by cross-reference lists such as NCEI's station-history records, then by name and location. A new source joins an existing station if it matches at least 50% over the overlap and lies within 40 km.
3. **Mingling.** Values are combined day by day under a fixed source priority, highest first: "Z,R,W,D,d,1,0,6,C,X,…,N,T,U,H,2,S" ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)).
   - The most-checked sources outrank automated real-time feeds.
   - In the U.S., COOP summaries outrank other streams.
   - Abroad, government exchange data outranks the international collection.
   - GSOD is used only when nothing else exists.
   - TMAX and TMIN always come from one source per day.

## How the data are made (high, instruments moderate)

- **Direct measurements.** Every value is an observation reported by the contributing network. The five core elements are precipitation, snowfall, snow depth, TMAX and TMIN, and there are many others ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)).
  - Most U.S. values are read once a day by volunteers in COOP or CoCoRaHS; others come from automated ASOS stations ([Menne et al. 2012](https://doi.org/10.1175/JTECH-D-11-00103.1)).
  - Some elements are computed: TAXN = (TMAX+TMIN)/2. TAVG is computed in various ways; for GSOD it is an average of hourly readings.
- **Instruments.** These belong to the networks, and no NCEI document maps them to GHCN-Daily elements:
  - **COOP:** liquid-in-glass thermometers in a Cotton Region Shelter, MMTS, the standard 8-inch gauge, a plastic 4-inch gauge and Fisher-Porter gauges ([NWS, 2024](https://media.cocorahs.org/docs/WERA_2024_1_NWS_COOP_Update_McGuire_.pdf)).
  - **ASOS:** heated tipping-bucket or all-weather accumulation gauges; snow is measured by hand ([NWS Chicago](https://www.weather.gov/lot/weather_observations_faq)).
  - **SNOTEL:** snow pillows and storage gauges with pressure transducers ([NRCS](https://directives.nrcs.usda.gov/sites/default/files2/1712930525/22448.pdf)).
  - **CoCoRaHS:** a required 4-inch manual gauge ([CoCoRaHS](https://media.cocorahs.org/docs/Why%20CoCoRaHS%20requires%20manual%20measurements.pdf)).
- **Steps done by algorithm:**
  - integration (screening, matching, mingling);
  - a fully automated quality-assurance sequence of 19 tests that flags values ([Durre et al. 2010](https://doi.org/10.1175/2010JAMC2375.1)); its details are left to the separate question.
  - Values are not homogenized for changes in instruments or observing practice (product page).
- **Updates:**
  - daily updates from many streams, and a full rebuild "each weekend";
  - a version number for each update. The current version is `3.35-upd-2026111517`, built on the full reprocessing `3.35-por-2026110623` ([ghcnd-version.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt)). Version 3.35 was released October 1, 2026.
  - Real-time U.S. data are replaced by archive-quality sources 45 to 60 days after month end, and values can still change after that.
  - Not every stream is daily ([status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)):
    - Environment Canada's feed stopped on April 28, 2024 until version 3.35 resumed it with weekly re-integration.
    - ECA&D was static from September 2024 and has updated monthly since January 20, 2025.

## Who is responsible (high; division and staff: not published)

- **Organization:** NOAA NCEI, part of NESDIS, NOAA, U.S. Department of Commerce. The point of contact is the "GHCNd Operations Team" (ncdc.ghcnd@noaa.gov), and Menne and Durre are principal investigators ([ISO record](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html)).
- **Credited people:**
  - The dataset citation lists 11 people: M.J. Menne, I. Durre, B. Korzeniewski, S. McNeill, K. Thomas, X. Yin, S. Anthony, R. Ray, R.S. Vose, B.E. Gleason and T.G. Houston (2012, Version 3; [readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)).
  - The 2012 overview paper's authors are Menne, Durre, Vose, Gleason and Houston, then at NCDC, Asheville.
- **Division (low):** no page names the NCEI division or branch that runs GHCN-Daily. NCEI's February 2023 org chart names no datasets. It shows Durre heading the Products Section of the Climatic Science & Development Branch, in the Climatic Science & Services Division ([NCEI org chart](https://www.nesdis.noaa.gov/s3dl?path=/s3/2023-02/NCEI_Org_Chart_Feb_2023.pdf)).
- **Staff count:** none is published for the GHCN-Daily team. NCEI's pages give no headcount; the only NCEI-wide figure found is partial (300 employees outside Asheville, October 2024; [NCEI news](https://www.ncei.noaa.gov/news/helene-devastates-southeast-impacts-noaa-ncei-headquarters)).

## How it relates to GHCN-Monthly and GHCNh (high)

- **GHCN-Monthly:** Version 4 temperature takes GHCN-Daily as its "primary source", shares its station identifiers, and computes monthly values from it where possible ([GHCNm page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-monthly); [Menne et al. 2018](https://doi.org/10.1175/JCLI-D-18-0094.1)). Before version 4 the two were not consistent.
- **GHCN-Monthly precipitation:** version 4 grew fivefold mainly by adding GHCN-Daily, which supplies almost 85% of its roughly 40 million monthly values ([Applequist, Durre, Vose](https://repository.library.noaa.gov/view/noaa/61558/noaa_61558_DS1.pdf)).
- **GHCNh (hourly):** it replaces ISD, is "vertically aligned" with GHCN-Daily and generally uses the same station IDs ([GHCNh page](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly)). Since version 3.33, GHCN-Daily takes SSODv2, derived from GHCNh, as a source.

## Conflicting figures

- **Station counts differ by date and definition:**
  - more than 100,000 (product page, undated);
  - "well over 90,000" (ISO record, modified 2025-12-04);
  - over 80,000 (2012 paper);
  - 133,041 entries in the station file (2026), which counts every station ID, closed ones included.
- **Source counts:** "more than 25" (product page), "approximately 30" (ISO record) and "20+" (2012 paper). The paper's text layer reads "201"; the page image shows "20+".

## Gaps

- **Current station counts per source network:** not published. NCEI holds them in its processing system; ask ncdc.ghcnd@noaa.gov. The table above counts ID numbering codes, not sources.
- **The NCEI division that maintains GHCN-Daily, and team size:** not published. NCEI could answer, or a current NCEI org chart might show it.
- **Instruments outside the U.S.:** not researched.
- **Pages not read:** 3 are listed in `check-by-hand.md`. The AMS journal page was refused, but NCEI's copy of the same paper was read. DataCite's API dropped the connection; its creators match the readme.
- **Hosts the sandbox refused:** 6, listed in `sites-to-trust.md` for you to decide whether to add any to the allowed domains.

## Sources

**NCEI (maintainer)**
- [NCEI, GHCNd product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)
- [NCEI, GHCN-Daily readme.txt, Version 3.35](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)
- [NCEI, GHCN-Daily status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)
- [NCEI, ghcnd-version.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt)
- [NCEI, ghcnd-stations.txt (counted by this run)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt)
- [NCEI, /pub/data/ghcn/daily/ directory listing](https://www.ncei.noaa.gov/pub/data/ghcn/daily/)
- [NCEI, ISO metadata record C00861 (read via extraction)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html)
- [NCEI, GHCNm product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-monthly)
- [NCEI, GHCNh product page](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly)
- [NCEI, GHCN-Daily description page, saved 2020](https://web.archive.org/web/20201218051149/https://www.ncdc.noaa.gov/ghcn-daily-description)
- [NESDIS, NCEI org chart, February 2023](https://www.nesdis.noaa.gov/s3dl?path=/s3/2023-02/NCEI_Org_Chart_Feb_2023.pdf)
- [NESDIS, NCEI office page](https://www.nesdis.noaa.gov/about/our-offices/national-centers-environmental-information-ncei)
- [NCEI, Helene news post, 2024 (read via extraction)](https://www.ncei.noaa.gov/news/helene-devastates-southeast-impacts-noaa-ncei-headquarters)

**Developers' papers, NCEI-hosted copies**
- [Menne, Durre, Vose, Gleason, Houston 2012, JTECH 29: 897–910](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/menne-etal2012.pdf)
- [Durre et al. 2010, JAMC 49: 1615–1633](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf)
- [Menne et al. 2018, J. Climate 31 (GHCNm v4)](https://repository.library.noaa.gov/view/noaa/45291/noaa_45291_DS1.pdf)
- [Applequist, Durre, Vose, GHCNm precipitation v4 (read in part)](https://repository.library.noaa.gov/view/noaa/61558/noaa_61558_DS1.pdf)

**Cloud hosts**
- [AWS Registry of Open Data, noaa-ghcn (read via extraction)](https://registry.opendata.aws/noaa-ghcn/)
- [Google Cloud Marketplace, GHCN Daily](https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d)
- [Google Cloud blog, 2016 (read via extraction)](https://cloud.google.com/blog/products/gcp/global-historical-daily-weather-data-now-available-in-bigquery)

**Contributing networks**
- [NWS, COOP update slides, 2024](https://media.cocorahs.org/docs/WERA_2024_1_NWS_COOP_Update_McGuire_.pdf)
- [NWS Chicago, observations FAQ](https://www.weather.gov/lot/weather_observations_faq)
- [NRCS, National Engineering Handbook 622 ch. 8](https://directives.nrcs.usda.gov/sites/default/files2/1712930525/22448.pdf)
- [CoCoRaHS, Why CoCoRaHS requires manual measurements, 2024](https://media.cocorahs.org/docs/Why%20CoCoRaHS%20requires%20manual%20measurements.pdf)

Saved in [`web_search_results/2026-11-19_ghcn-daily-about-pt1/`](./): this answer, `research-record.json`, `method.md`, `results.csv`, `check-by-hand.md` and `sites-to-trust.md`.
