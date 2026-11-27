# ASOS precipitation observations as one dataset: products, hosts, inputs, organizations

ASOS precipitation reaches users through four product families. NCEI is the archive of record for all of them, and each copy elsewhere is either short-lived or a copy of NCEI's holdings.
- **1-minute data:** precipitation is on page 2 (DSI 6406), not page 1.
- **5-minute data (DSI 6401):** present weather only, no amounts.
- **Hourly METAR/SPECI totals:** now in GHCNh. ISD, which held them before, was frozen in August 2025.
- **Daily and monthly summaries:** the DSM, the monthly summary message and the CF6.

For hourly data, independent copies exist:
- NCEI's archive and its offsite backup;
- the current AWS GHCNh bucket;
- IEM's own METAR archive in Iowa;
- frozen ISD copies on AWS and Azure.

The 1-minute data have fewer copies, and no outside copy of the 5-minute data was found. Every product depends on NWS and FAA communications networks and NWS-run processing upstream of NCEI. **Overall confidence: moderate to high** (high for products and hosts, moderate for counts and data path).

## Products

| Product | Precipitation content | Period of record | Updated | Status |
|---|---|---|---|---|
| 1-minute page 2 (NCEI DSI 6406_02) | precipitation type and amount, frozen-precipitation sensor frequency | 1998-06-01 to present | daily | current |
| 1-minute page 1 (DSI 6405_02) | none (visibility, wind, RVR) | 1998-06-01 to present | daily | current |
| 5-minute (DSI 6401_02) | present weather only; no amount listed | 1996-07-01 to present | daily | current |
| ISD / Global Hourly | METAR/SPECI precipitation amounts | from 1901 | none since 24 Aug 2025 | replaced by GHCNh |
| GHCNh (DSI 2074_01) | hourly precipitation plus 3–24-hour totals from FM-15/FM-16 | "1750-01-01 to Present" (all sources) | daily | current |
| DSM / monthly summary; CF6 (F-6) | daily total and hourly amounts; monthly totals, short-duration maxima | not found | daily / monthly | current; no separate NCEI archive found |
| LCD v2 (DSI 2075_02) | daily and hourly precipitation from ASOS and AWOS | "1750-02-01 to Present" | daily | replaced LCD v1, which ended 29 Aug 2025 |

Sources by row:
- **1-minute and 5-minute rows:** NCEI metadata ([page 2](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00387/html), [page 1](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00386/html), [5-minute](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00418/html)).
- **ISD row:** the [NESDIS notice](https://www.nesdis.noaa.gov/news/service-location-change-integrated-surface-data-global-hourly).
- **GHCNh row:** the [GHCNh documentation](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf) and [GHCNh metadata](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01688/html).
- **Summaries row:** [NWSI 10-1004](https://www.weather.gov/media/directives/010_pdfs/pd01010004curr.pdf) and [NWS ASOS Information Reporting](https://www.weather.gov/asos/InformationReporting.html).
- **LCD row:** the [NCEI LCD page](https://www.ncei.noaa.gov/products/land-based-station/local-climatological-data) and [LCDv2 metadata](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01689/html).

Notes on the products:
- **DSI 3285:** no NCEI page read uses this number; NCEI names the 1-minute data DSI 6405 and DSI 6406.
- **ISD end date:** the NESDIS notice says ISD had "no update beyond 08/24/2025". 29 Aug 2025 is when the legacy LCD v1 ends and the replacements take over, so the two dates mark different events (High).

## Hosts

| Host | Holds | Kind | Still updated? |
|---|---|---|---|
| NCEI `/data/automated-surface-observing-system-one-minute-pg1/`, `-pg2/`, `-five-minute/` | 1- and 5-minute data | archive of record | yes; 2026 folders modified 2026-11-26 |
| NCEI `/pub/data/asos-onemin/`, `/asos-fivemin/` | older copies, 6405/6406/6401 | NCEI legacy directories | no; last year folders dated 2022-07-05 |
| NCEI `/data/global-hourly/` | ISD | none now | redirects (301) to the AWS bucket; NCEI's own service set to retire 31 Jul 2026 |
| NCEI GHCNh object store | GHCNh | archive of record | file dates not read (built by JavaScript) |
| AWS `noaa-ghcnh-pds` (us-east-1) | GHCNh | NODD copy | yes; 2026 files modified 2026-11-26 |
| AWS `noaa-global-hourly-pds`, `noaa-isd-pds` (us-east-1) | ISD (CSV and original format) | NODD copies | no; newest prefix 2025/, 2026/ empty |
| Azure `noaaisd` blob (West Europe) | ISD | NODD copy | not checked |
| Iowa Environmental Mesonet | own global METAR archive, 1900–present; reprocessed 1-minute data | independent outside archive | yes; synced every 10 min; 1-minute data to 25 Nov 2026 |
| api.weather.gov | observations | NWS real-time feed | 7 days kept |
| aviationweather.gov | METARs | NWS AWC real-time feed | 30 days kept |
| FAA WMSCR | current METARs | FAA dissemination | current data only |

Sources by row:
- **NCEI rows:** sa1's saved listings of the [1-minute page 2 access folder](https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg2/access/), the [5-minute access folder](https://www.ncei.noaa.gov/data/automated-surface-observing-system-five-minute/access/) and [/pub/data/asos-onemin/](https://www.ncei.noaa.gov/pub/data/asos-onemin/), and the [NESDIS notice](https://www.nesdis.noaa.gov/news/service-location-change-integrated-surface-data-global-hourly).
- **AWS rows:** the bucket listings ([GHCNh 2026](https://noaa-ghcnh-pds.s3.amazonaws.com/?list-type=2&prefix=hourly/access/by-year/2026/&max-keys=8), [global-hourly](https://noaa-global-hourly-pds.s3.amazonaws.com/?list-type=2&delimiter=/&max-keys=1000), [isd](https://noaa-isd-pds.s3.amazonaws.com/?list-type=2&prefix=data/&delimiter=/&max-keys=1000)) and the AWS registry ([ISD](https://registry.opendata.aws/noaa-isd/), [GHCNh](https://registry.opendata.aws/noaa-ghcnh/)).
- **Azure row:** [Microsoft](https://microsoft.github.io/AIforEarthDataSets/data/noaa-isd.html).
- **IEM row:** [IEM METAR dataset](https://mesonet.agron.iastate.edu/info/datasets/metar.html), [IEM download](https://mesonet.agron.iastate.edu/request/download.phtml) and [IEM 1-minute](https://mesonet.agron.iastate.edu/request/asos/1min.phtml).
- **Feed rows:** [NWS API](https://www.weather.gov/documentation/services-web-api), [AWC Data API](https://aviationweather.gov/data/api/) and [FAA WMSCR FAQ](https://www.faa.gov/airports/planning_capacity/non_federal/doc/awos_wmscr_faq.pdf).

What the hosts say about their own role:
- **NCEI:** NWS says "The National Centers for Environmental Information (NCEI) is the official climatological archive of all weather observations" ([NWS ASOS FAQ](https://www.weather.gov/asos/FAQ.html)).
- **NODD:** NOAA calls its cloud holdings "copies of data", delivered to cloud providers through a data broker, and calls them authoritative ([NODD FAQ](https://www.noaa.gov/big-data-project-frequently-asked-questions)).
- **IEM:** it calls NCEI ISD "likely the most authoritative source". IEM is the only outside group found that keeps a full archive of its own (High).
- **NWS and FAA:** their feeds keep 7 days, 30 days or current data only. Neither states that it keeps a full archive (High for the feeds; the absence of an archive is a not-found).

How NCEI stores its archive:
- NCEI says "The NCEI archive and backup copy contains more than 60 petabytes" ([NCEI About](https://www.ncei.noaa.gov/about-us)).
- In 2020 it kept two tape copies, one in Asheville and a secure copy offsite ([NCEI 2020](https://www.ncei.noaa.gov/news/ncei-archives-cosmic-2-data)).
- A 2016 SOP put the off-site library about 12.5 miles from the Asheville office ([NCEI SOP via Wayback](https://web.archive.org/web/20201028083622/https://www1.ncdc.noaa.gov/pub/data/paleo/data_management/20160928-MSC_SOP_AppendixM-NCDC200-01-018_IT_Off-site_Backup_Procedures.pdf)).
- NESDIS is moving all of NCEI's data from Asheville and Boulder to AWS through Spring 2027 ([NCEI cloud migration](https://www.ncei.noaa.gov/news/cloud-migration)).
- None of these names ASOS products, and they are partly dated (Moderate).

## Inputs

**Stations.** NWS says "approximately 950 active ASOS sites" ([NWS FAQ](https://www.weather.gov/asos/FAQ.html)); NCEI says "more than 900" ([NCEI](https://www.ncei.noaa.gov/products/land-based-station/automated-surface-weather-observing-systems)). NWS's [equipment spreadsheet as of 18 Mar 2025](https://www.weather.gov/media/asos/ASOS%20Sites%20by%20Equipment%20As%20Of%203_18_2025.xlsx) can be counted by owner (these are this run's row counts, not NWS figures):
- legacy in-service rows: FAA 568, NWS 304, DOD 8, Navy 1 (881);
- AWPAG: 323 (NWS 303, FAA 20);
- heated tipping bucket: 575 (FAA 552, NWS 14, DOD 8, Navy 1);
- freezing-rain sensor: 683;
- present-weather sensor: 857.

The figures differ by scope, not error: rounded program totals, stations with 1-minute data, and units NWS maintains, which likely leaves out most DoD-run sites. Old NCDC documentation planned "approximately 1200" NWS and FAA sites when fully commissioned ([TD 6406](https://www.ncei.noaa.gov/pub/data/asos-onemin/td6406.txt)), a number never reached (Moderate). The AWPAG, made by Ott Hydrometrie, replaced the tipping bucket at NWS-sponsored sites (313 were planned; resolution 0.01 inch, capacity 40 inches of liquid equivalent) ([AWPAG plan](https://www.weather.gov/media/asos/ASOS%20Implementation/awpagimplan.pdf)). It is the NWS climate-standard gauge ([NWSI 10-1302](https://www.weather.gov/media/directives/010_pdfs/pd01013002curr.pdf)).

**Processor.** Data collection packages feed the Acquisition Control Unit, which "applies algorithms" and transmits. The ACU and DCPs are being replaced under the tri-agency Service Life Extension Program ("ASOS 2.0", Campbell Scientific as the original equipment maker) ([NWS FAQ](https://www.weather.gov/asos/FAQ.html), [ASOS Current Events](https://www.weather.gov/asos/CurrentEvents.html)) (High).

**Path to NCEI.** The pieces come from several documents, some dated (Moderate):
- Long-line transmission goes over NWS or FAA networks; many sites have used FAA ADAS since 2002 ([TIN 02-16](https://www.weather.gov/media/notification/tins/tin02-16asos_xfer.pdf)).
- It reaches the NWS Telecommunications Gateway and NCEP. NWS describes "compilation on the daily Service Records Retention System (SRRS) tape" for NCEI ([NWS Information Reporting](https://www.weather.gov/asos/InformationReporting.html)).
- 1-minute data are stored on station for 12 hours and were collected by NCDC, by modem in the old documentation ([DSI-6405 doc](https://www.ncei.noaa.gov/pub/data/asos-onemin/td6405.txt)).
- No current end-to-end description was found.

**Human observers.** The FAA's service levels set how much people add (High):
- Level D is fully automated.
- At Level C an observer, usually a controller, augments and backs up the report.
- Levels B and A add detail, "typically provided by contract weather observers, NWS observers, and, at some locations, FSS observers" ([FAA AIM 7-1](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap7_section_1.html)).
- The METAR hourly, 3-/6-hour and 24-hour precipitation groups are "Automated Only" ([FAA JO 7900.5E](https://www.faa.gov/documentLibrary/media/Order/Order_JO_7900.5E.pdf)).
- Snowfall and snow depth are measured by hand ([NWSI 10-1302](https://www.weather.gov/media/directives/010_pdfs/pd01013002curr.pdf)).

**Measured vs derived** (Moderate).
- *Measured:* the gauge's 1-minute accumulation, precipitation identification from the present-weather sensor, and the freezing-rain sensor.
- *Derived:* the 15-minute and hourly SHEF totals (sums of 1-minute accumulations; [NWS](https://www.weather.gov/asos/InformationReporting.html)); the METAR 3-, 6- and 24-hour amounts; and the DSM daily and hourly totals.
- *In GHCNh:* hourly values are running totals within the hour, and the last report gives the hourly value ([GHCNh doc](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf)).
- *IEM:* computes its own calendar-day totals, which DSM or CLI values may overwrite.

## Organizations

- **Tri-agency program:** NWS, FAA and DoD (Navy) run ASOS jointly ([ASOS home](https://www.weather.gov/asos/); [ASOS Current Events](https://www.weather.gov/asos/CurrentEvents.html)).
- **NWS:** its electronics technicians maintain both NWS- and FAA-owned units, and the tri-agency parties fund its ASOS Operations and Monitoring Center ([NWSI 30-2111](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf)).
- **FAA:** it says NWS "maintains ASOS through an interagency agreement" ([FAA ASWON](https://www.faa.gov/air_traffic/weather/aswon)).
- **Navy and Air Force:** they maintain their own units (1998 [User's Guide](https://www.weather.gov/media/asos/aum-toc.pdf)).
- **NCEI:** collects, processes and archives the data.
- **Contractors:** Vaisala makes the newer wind and temperature/humidity sensors; Campbell Scientific makes the new processor hardware.
- **Outside groups:** IEM (Iowa State) keeps and serves its own archive; cloud providers host the NODD copies.

**AWOS differs:**
- Many units are non-federal: "procured, installed, operated, and maintained by an entity other than any federal government agency" ([FAA](https://www.faa.gov/airports/planning_capacity/non_federal/faq)).
- Only some types sense precipitation: AWOS-3P has identification only, and AWOS-4 adds accumulation and freezing rain ([FAA AIM](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap7_section_1.html)).

## Against the rubric

| Statement | Verdict | Evidence |
|---|---|---|
| RRS-1 "two or more geographically independent copies" | **Supports** for hourly data. **Partly supports** for 1-minute data. **Not shown** for 5-minute data and CF6/DSM. | Hourly: NCEI and its offsite backup; AWS us-east-1 GHCNh (current); IEM in Iowa (independent); Azure West Europe ISD (frozen). 1-minute: NCEI and IEM's reprocessed copy. 5-minute: NCEI only. NCEI's backup was about 12.5 miles from the primary in 2016, which is a weak form of geographic independence. |
| D-2 "storage is a single point of failure" | **Contradicted** for hourly data. **Partly supported** for 5-minute data and the summaries. **Open** during the migration. | Only NCEI was found holding DSI 6401. ASOS keeps the DSM for 10 days. When NCEI's own archive moves onto AWS by Spring 2027, it and the NODD copies may sit with one provider; the regions of the migrated archive weren't found. |
| DIRS-3 "depends on external data feeds" | **Supports** | NCEI receives everything over NWS and FAA networks (NWSTG, FAA ADAS). IEM depends on NOAAPort, IDD, MADIS and NCEI. |
| DIRS-4 "needs outside processing infrastructure" | **Supports** | Products depend on site ACUs, the NWS AOMC, NCEP/NWSTG and FAA ADAS/WMSCR before NCEI. NCEI's own processing is moving to AWS, and NODD copies pass through the CISESS data broker. |

## Gaps

- **DSI 3285:** not matched to any product.
- **GHCNh at NCEI:** the bulk-folder dates weren't read (JavaScript explorer).
- **Azure ISD copy:** whether it is still updated wasn't checked.
- **GAO unit counts (GAO-07-650):** unread (HTTP 403). GAO holds the report; open it in a browser.
- **Path to NCEI:** no current end-to-end description of the ASOS data path; NWS's page describes the SRRS tape step.
- **Tri-agency agreement:** the text wasn't found; NWS's ASOS program office holds it.
- **CF6 and DSM at NCEI:** no separate archive was found.
- **Pages to check by hand:** 4, in [check-by-hand.md](check-by-hand.md).
- **Sandbox:** 5 refused hosts, listed in [sites-to-trust.md](sites-to-trust.md); you can decide whether to add any to your allowed domains.

## Sources

**NCEI and NESDIS**
- [NCEI, 1-Minute Page 2 metadata (C00387)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00387/html)
- [NCEI, 1-Minute Page 1 metadata (C00386)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00386/html)
- [NCEI, 5-Minute metadata (C00418)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00418/html)
- [NCEI, 1-minute page 2 access directory](https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg2/access/)
- [NCEI, 5-minute access directory](https://www.ncei.noaa.gov/data/automated-surface-observing-system-five-minute/access/)
- [NCEI, /pub/data/asos-onemin/](https://www.ncei.noaa.gov/pub/data/asos-onemin/)
- [NCEI, DSI-6405 documentation](https://www.ncei.noaa.gov/pub/data/asos-onemin/td6405.txt)
- [NCEI, TD 6406 documentation](https://www.ncei.noaa.gov/pub/data/asos-onemin/td6406.txt)
- [NCEI, GHCNh documentation v1.1.0](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf)
- [NCEI, GHCNh metadata (C01688)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01688/html)
- [NCEI, LCD product page](https://www.ncei.noaa.gov/products/land-based-station/local-climatological-data)
- [NCEI, LCDv2 metadata (C01689)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01689/html)
- [NCEI, ASOS/AWOS product page](https://www.ncei.noaa.gov/products/land-based-station/automated-surface-weather-observing-systems)
- [NCEI, About](https://www.ncei.noaa.gov/about-us)
- [NCEI, COSMIC-2 archiving news, 2020](https://www.ncei.noaa.gov/news/ncei-archives-cosmic-2-data)
- [NCEI, SOP 200-01-018, 2016 (Wayback copy)](https://web.archive.org/web/20201028083622/https://www1.ncdc.noaa.gov/pub/data/paleo/data_management/20160928-MSC_SOP_AppendixM-NCDC200-01-018_IT_Off-site_Backup_Procedures.pdf)
- [NCEI, Cloud migration](https://www.ncei.noaa.gov/news/cloud-migration)
- [NESDIS, Service location change for ISD](https://www.nesdis.noaa.gov/news/service-location-change-integrated-surface-data-global-hourly)
- [NOAA, NODD FAQ](https://www.noaa.gov/big-data-project-frequently-asked-questions)

**NWS**
- [NWS, ASOS home](https://www.weather.gov/asos/)
- [NWS, ASOS FAQ](https://www.weather.gov/asos/FAQ.html)
- [NWS, ASOS Information Reporting](https://www.weather.gov/asos/InformationReporting.html)
- [NWS, ASOS Current Events](https://www.weather.gov/asos/CurrentEvents.html)
- [NWS, ASOS Sites by Equipment, 18 Mar 2025](https://www.weather.gov/media/asos/ASOS%20Sites%20by%20Equipment%20As%20Of%203_18_2025.xlsx)
- [NWS, AWPAG implementation plan](https://www.weather.gov/media/asos/ASOS%20Implementation/awpagimplan.pdf)
- [NWS, ASOS User's Guide, 1998](https://www.weather.gov/media/asos/aum-toc.pdf)
- [NWS, NWSI 10-1004, 2025](https://www.weather.gov/media/directives/010_pdfs/pd01010004curr.pdf)
- [NWS, NWSI 10-1302](https://www.weather.gov/media/directives/010_pdfs/pd01013002curr.pdf)
- [NWS, NWSI 30-2111](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf)
- [NWS, TIN 02-16](https://www.weather.gov/media/notification/tins/tin02-16asos_xfer.pdf)
- [NWS, API documentation](https://www.weather.gov/documentation/services-web-api)
- [NWS, SCN 24-45](https://www.weather.gov/media/notification/pdf_2023_24/scn24-45_api_observation_data_removal.pdf)
- [NWS AWC, Data API](https://aviationweather.gov/data/api/)

**FAA**
- [FAA, Order JO 7900.5E](https://www.faa.gov/documentLibrary/media/Order/Order_JO_7900.5E.pdf)
- [FAA, AIM Chapter 7 Section 1](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap7_section_1.html)
- [FAA, ASWON](https://www.faa.gov/air_traffic/weather/aswon)
- [FAA, Non-federal program FAQ](https://www.faa.gov/airports/planning_capacity/non_federal/faq)
- [FAA, AWOS WMSCR FAQ](https://www.faa.gov/airports/planning_capacity/non_federal/doc/awos_wmscr_faq.pdf)

**Hosts and copies**
- [AWS Registry, NOAA ISD](https://registry.opendata.aws/noaa-isd/)
- [AWS Registry, NOAA GHCNh](https://registry.opendata.aws/noaa-ghcnh/)
- [S3 listing, noaa-ghcnh-pds 2026](https://noaa-ghcnh-pds.s3.amazonaws.com/?list-type=2&prefix=hourly/access/by-year/2026/&max-keys=8) (read via WebFetch extraction)
- [S3 listing, noaa-global-hourly-pds](https://noaa-global-hourly-pds.s3.amazonaws.com/?list-type=2&delimiter=/&max-keys=1000)
- [S3 listing, noaa-isd-pds data/](https://noaa-isd-pds.s3.amazonaws.com/?list-type=2&prefix=data/&delimiter=/&max-keys=1000) (read via WebFetch extraction)
- [Microsoft, AIforEarthDataSets: NOAA ISD](https://microsoft.github.io/AIforEarthDataSets/data/noaa-isd.html)
- [IEM, METAR dataset](https://mesonet.agron.iastate.edu/info/datasets/metar.html)
- [IEM, ASOS-AWOS-METAR download](https://mesonet.agron.iastate.edu/request/download.phtml) (read from mirror)
- [IEM, ASOS one-minute download](https://mesonet.agron.iastate.edu/request/asos/1min.phtml)

Saved in [`web_search_results/2026-11-26_asos-precip-about-pt1/`](./): this answer, `research-record.json`, `method.md`, `check-by-hand.md` and `sites-to-trust.md`.
