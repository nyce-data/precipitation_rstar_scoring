# GHCN-Daily's outside dependencies, Part 8: calibration, foreign networks, supply chain, processing, alternatives (Jan 2025 – Nov 2026)

GHCN-Daily depends on several outside services the earlier runs didn't check, and three are under threat now:
- the field staff who maintain ASOS and COOP instruments (NWS electronics technicians are down sharply);
- the eight-person NOAA ATDD team that calibrates and maintains USCRN, whose parent laboratory NOAA has asked twice to close;
- a foreign-station route that still has gaps (SSODv2's full record was promised but no NCEI note says it arrived).

The Regional Climate Centers, one possible failure point, are not at risk: NOAA re-awarded all six as five-year contracts in September 2026. Real alternatives exist for parts of the record: ECA&D, Copernicus C3S station data and WMO's WIS2 exchange. None replaces GHCN-Daily as a global, quality-controlled daily archive. Overall confidence: **moderate**.

## Findings and ratings

| Dependency | What was found | DIRS | Threat |
|---|---|---|---|
| ATDD, Oak Ridge (USCRN calibration and maintenance) | A team of 8 makes the annual visits; its parent ARL is proposed for closure in the FY26 and FY27 requests; the enacted FY26 statement doesn't name ARL | DIRS-1, DIRS-2 support | emerging |
| NWS field maintenance (ASOS, COOP) | "Critical staffing shortages", offices grouped into maintenance pods (Mar 2025); electronics technicians down ≥16% | DIRS-2 supports | imminent (staff losses) |
| Sterling Field Support Center (ASOS calibration) | Running; nothing on cuts or staffing | DIRS-1 contradicts (for now) | no current threat found |
| NRCS (SNOTEL) | Maintenance continues in Nevada; senators warn staff cuts could end snow surveys in up to a third of California's watersheds | DIRS-2 supports | emerging |
| NIST, CoCoRaHS gauge | NIST calibration staff thin but services running; no formal CoCoRaHS gauge standard found | DIRS-1: little evidence | no current threat found |
| WMO RICs (foreign calibration) | Reform proposed; "only nine" accredited RICs (the Oct 2026 list marks eight); WMO is cutting posts | DIRS-1 supports (abroad) | emerging |
| SMN Argentina | 240 (or more than 200) dismissals and closures of interior stations announced, Apr 2026 | DIRS-2 supports | emerging |
| Russia, China, Indonesia, Algeria | No national closures found; the stations still report, but NOAA's route lost them | DIRS-3 supports | imminent (route) |
| SSODv2 / GHCNh | 2025-onward data only; full record promised Jan 2026, no confirmation since; GHCNh funding unpublished | DIRS-3, DIRS-5 support | imminent |
| ECCC (Canada, Alberta) | 2024 stop unexplained, restored Oct 2026; history of 180 Alberta government stations deleted from ECCC's open data, Sept 2026 | DIRS-3 supports | imminent, small effect |
| Regional Climate Centers | Six IDIQs signed Sept 11–16, 2026, running to 2031 | DIRS-2, DIRS-3 contradict | no current threat found |
| ASOS → AWOS-C | No published list marks the climate sites | — | not published |
| Processing after the AWS move | Where it runs and who runs it is unpublished; NCEI's access-delay alert runs to Nov 30 | DIRS-4 supports | emerging |
| Alternatives | HadISD stopped; ECA&D, C3S and WIS2 are current; Berkeley Earth has no station-level daily product | DIRS-5 partly contradicts | — |

Sources: the citations in each section below.

## Calibration and maintenance (searched by no earlier run)

**USCRN.** NOAA's Atmospheric Turbulence and Diffusion Division (ATDD) in Oak Ridge designed and built the stations, and it maintains them and their instruments ([NCEI](https://www.ncei.noaa.gov/access/crn/)). "ATDD has a small team of eight technicians and engineers responsible for annual maintenance visits to each station" ([NOAA ARL](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/)). On each visit they swap one of the three platinum resistance thermometers and calibrate the rain gauges. The thermometers are traceable to NIST ([Goodge, NCDC](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/research/Goodge.pdf)).

NOAA's FY2027 request, like the FY2026 one, would "Terminate Climate Laboratories and Cooperative Institutes" (−$104,964K, −180 FTE) and close ARL ([NOAA budget](https://www.noaa.gov/organization/budget-finance-performance/budget-and-reports)). In 2025 a House panel told NOAA to "avoid closures, consolidations or eliminations" ([E&E News, 2025](https://www.eenews.net/articles/house-panel-protects-noaa-labs-research-from-trump-cuts/)). The enacted FY2026 law gave NOAA about $6.1 billion ([KGOU, 2026](https://www.kgou.org/weather-and-climate/2026-01-27/federal-funding-law-includes-money-for-oklahoma-weather-climate-institutions)). Its Joint Explanatory Statement funds OAR at $588,881,000 but never names ARL, ATDD or USCRN ([Congressional Record, H255](https://www.govinfo.gov/content/pkg/CREC-2026-01-08/html/CREC-2026-01-08-pt3-PgH255.htm)). Congress rejected the same closure for FY2018 ([Oak Ridge Today, 2017](https://web.archive.org/web/20251206192457/https://oakridgetoday.com/tag/atdd/)). This is a single, small team with no named backup: **DIRS-1 supported, emerging** (moderate confidence).

**ASOS.** NWS's Sterling Field Support Center is a "230 acre complex dedicated to the calibration, test, evaluation and support of meteorological systems and sensors" ([NWS](https://www.weather.gov/soic/)). Its Pressure Standards Laboratory calibrates about 500 barometers a year for ASOS and upper air ([NWS PSL](https://www.weather.gov/media/soic/NWS%20Pressure%20Standards%20Laboratory.pdf)). Electronics technicians do quarterly preventive maintenance, and "ASOS sensors require minimal calibration" ([NWSI 30-2111](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf)). NWS is replacing the ASOS temperature/dew-point sensors at all sites with Vaisala HMP155E probes through 2025 ([NWS ASOS Current Events](https://www.weather.gov/asos/CurrentEvents.html)). No SFSC cut was found. The field staff, however, are short:
- In March 2025 NWS grouped offices into "pods" "to mitigate critical staffing shortages" ([NWS ASOS Current Events](https://www.weather.gov/asos/CurrentEvents.html)).
- Former Administrator Spinrad said electronics technicians are "down by at least 16%" ([CBS, 2025](https://www.cbsnews.com/chicago/news/national-weather-service-staffing-shortages-making-forecasts-worse)).

**COOP.** Each office's Observations Program Leader inspects and maintains COOP stations, helped by HMTs, meteorologists or electronics technicians ([NWSI 10-1307, 2025](https://www.weather.gov/media/directives/010_pdfs/pd01013007curr.pdf)). COOP therefore draws on the same thinned staff. **DIRS-2 supported, imminent** for field maintenance capacity, though no lost data was traced to it.

**SNOTEL, NIST, CoCoRaHS.**
- **SNOTEL:** NRCS Nevada still makes over 90 summer SNOTEL visits ([NRCS](https://www.nrcs.usda.gov/state-offices/nevada/news/nevada-snow-survey-whats-new-for-2026)). California's senators warned that staff cuts could end snow surveys in "as many as one third" of the state's watersheds ([Padilla and Schiff, 2025](https://www.padilla.senate.gov/wp-content/uploads/12.22.25-Letter-to-USDA-DOC-on-Diminished-Water_Weather-Forecasting-and-Snowpack-Survey-Capacity.pdf)). Emerging.
- **NIST:** about 150 calibration staff in 2024, down 25–50% over a decade, and calibration income "does not cover maintenance". No 2025–26 cut to services used for weather instruments was found ([NIST, 2025](https://www.nist.gov/document/measurement-services-update)).
- **CoCoRaHS:** no formal gauge standard or certifying body was found. In Colorado tests its gauge caught 101–105% of what the NWS 8-inch gauge caught ([CoCoRaHS](https://media.cocorahs.org/docs/Why%20CoCoRaHS%20requires%20manual%20measurements.pdf)).

**WMO.** A WMO letter of May 26, 2026 proposes replacing the Regional Instrument Centres, citing "only nine" accredited RICs ([WMO](https://extranet.wmo.int/edistrib_exped/grp_prs/_en/6742243-2026-ESDP-MINT_en.pdf)). WMO's own RIC list, updated Oct 29, 2026, marks eight as accredited ([WMO RIC list](https://community.wmo.int/node/36165)); the two counts are unreconciled. WMO's 2026 reorganization abolished 68 posts ([WMO](https://wmo.int/sites/default/files/2026-08/WMO%20Secretariat%20Reorganization%20%282026%29.pdf)). In Oct 2026 the US paid 15.1 million CHF for 2024, with 2025–26 dues still outstanding ([Devdiscourse/Reuters](https://www.devdiscourse.com/article/international/3989889-us-pledges-tens-of-millions-to-un-bodies-in-geneva-sources-say)). This matters for foreign services' instruments, not US ones: emerging.

## Networks abroad and ASOS sites

- **Argentina (SMN):** reported in April 2026 to have a list of 240 workers, "un 20% de la planta", to dismiss, and plans to close interior stations not yet named ([Bichos de Campo](https://bichosdecampo.com/esta-situacion-golpea-de-lleno-a-la-produccion-advierten-los-trabajadores-del-servicio-meteorologico-nacional-ante-una-nueva-oleada-de-despidos-y-la-posibilidad-de-que-cierren-estaciones/)). Another outlet gives "más de 200 despidos" ([El Cronista](https://www.cronista.com/economia-politica/paro-en-el-servicio-meteorologico-por-despidos-y-denuncias-de-vaciamiento)). Emerging; low confidence.
- **Indonesia (BMKG):** BMKG says its 2025 budget rose after "reconstruction" and services continue ([BMKG](https://www.bmkg.go.id/berita/utama/rekonstruksi-anggaran-bmkg-pastikan-layanan-informasi-publik-tetap-optimal)).
- **Russia:** Roshydromet's WIS2 node was declared operational in Jan–Jun 2026 ([WMO](https://wmo.int/media/news/wis2-operational-newsletter-no3)).
- **China:** CMA publishes an open-data catalog ([WMO/CMA](https://wmo.int/media/news-from-members/cma-releases-2025-catalog-of-popular-meteorological-data-open-sharing)). Its 2026 rules bar giving observation sites or data to foreign organizations without approval ([Global Times](https://www.globaltimes.cn/page/202605/1362135.shtml)).
- **Algeria:** nothing found.
- **Route loss, not closures:** Berkeley Earth says such stations "continue to be operated by their local meteorological agencies" but are no longer captured by NOAA's aggregation ([Berkeley Earth](https://berkeleyearth.org/october-2025-temperature-update/)). So the losses read as DIRS-3 (route), not DIRS-2.
- **ASOS → AWOS-C:** the ASOS FAQ's "complete list" link opens the general equipment spreadsheet, which has no AWOS-C or climate-site column ([NWS](https://www.weather.gov/asos/FAQ.html); [spreadsheet](https://www.weather.gov/media/asos/ASOS%20Sites%20by%20Equipment%20As%20Of%203_18_2025.xlsx)). The FAA says only "Replace 206 ASOS with AWOS-C" ([FAA](https://www.faa.gov/air_traffic/weather/aswon)), while the NWS FAQ's text speaks of the "207 transition". The FAQ also gives the reason: FAA funding "is insufficient to recondition all 570 FAA ASOS locations" ([NWS](https://www.weather.gov/asos/FAQ.html)). No list marking climate sites is published.

## Supply chain

**SSODv2 and GHCNh.** v3.33 (Jan 5, 2026) brought in SSODv2 for 2025-onward data only; "Several weeks later, the full period of record for SSODv2 will be integrated" ([NCEI status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)). Neither v3.34 nor v3.35 says it was. Algiers' file still ends in August 2025 on GSOD data ([NCEI](https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/AG000060390.dly)). SSOD is "computed from the hourly and synoptic reports provided in GHCNh" ([NCEI GHCNh](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly)), so GHCNh is now upstream of GHCN-Daily. No funding or staffing for GHCNh is published. **Imminent.**

**Canada.** NCEI gives no cause for the 2024 stop ("unexpectedly discontinued on April 28, 2024"). v3.35 restored the feed from ECCC's web database and moved Canadian IDs to network code N ([NCEI status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)). On Aug 31, 2026 ECCC said the historical data of 180 Government of Alberta stations would be deleted from its open-data platforms by end of September; the data stay on Alberta's ACIS ([ECCC dd_info](https://comm.collab.science.gc.ca/mailman3/hyperkitty/list/dd_info@comm.collab.science.gc.ca/thread/RLV2GKL3NV7GFSIYHOO5W4YL4WIJ6T2R/)). I checked the overlap with GHCN-Daily:
- The attached list has 174 stations ([ECCC](https://comm.collab.science.gc.ca/mailman3/hyperkitty/list/dd_info@comm.collab.science.gc.ca/message/RLV2GKL3NV7GFSIYHOO5W4YL4WIJ6T2R/attachment/6/ABgov_Station-Inventory.xlsx)).
- 120 of them are in [ghcnd-stations.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt).
- The live inventory has data rows for only 38, and their data ends in 2017 (37 stations) or 2024 (1) ([count from ghcnd-inventory.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt)).

So these stations add no current data to GHCN-Daily, and ECCC can no longer supply their history (low confidence; 82 listed stations with no inventory rows are unexplained).

**Regional Climate Centers.** The contracts did not lapse:
- the sources-sought notice SSN-NCEI-RCC-2025 (Sept 10, 2025) ([SAM.gov](https://sam.gov/opp/247583e5d50d4edba32b36f7e860ea8f/view));
- six solicitations on May 27, 2026, under the new name "Regional Weather Records Centers" ([SAM.gov](https://sam.gov/opp/373385828b37436ba1c94f8d0f6dbe11/view));
- six IDIQs signed Sept 11–16, 2026, to Nebraska, the Nevada System of Higher Education, Cornell, UNC Chapel Hill, Purdue and Texas A&M Transportation Institute ([USAspending](https://www.usaspending.gov/keyword_search/Regional%20Weather%20Records%20Center)).

The Southern award runs from Sept 17, 2026 to Sept 16, 2031, with a $5.62M ceiling and nothing obligated yet ([USAspending](https://www.usaspending.gov/award/CONT_IDV_1332KP26D0008_1330)). This matters to GHCN-Daily directly: since v3.32 (Mar 2025) the High Plains RCC has supplied the US airport Daily Summary Messages ([NCEI status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)). **No current threat found.**

## Processing

No page says where GHCN-Daily is processed after the AWS move, or who runs it. NCEI's "Data Access Delays" alert (Nov 16–30, 2026) blames the cloud migration ([NCEI Alerts](https://www.ncei.noaa.gov/alerts)). Updates continue: version 3.35-upd-2026111517 ([NCEI](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt)). No CISESS processing prototype for GHCN-D was found in production. CISESS piloted GHCNm 4.0.1 on a commercial cloud ([CISESS](https://cisess.umd.edu/)) and built NODD's Cloud Ingest Pipeline, which handles distribution, not processing ([Science Advances, 2023](https://repository.library.noaa.gov/view/noaa/59059/noaa_59059_DS1.pdf)). **DIRS-4 supported, emerging.**

## Alternatives

- **HadISD:** stopped with ISD. Its final version covers up to Aug 29, 2025, with "no further monthly releases" ([Met Office](https://www.metoffice.gov.uk/hadobs/hadisd/); [HadISD blog](https://hadisd.blogspot.com/2025/09/hadisd-v342202508p-potentially-final.html)).
- **ECA&D:** current, updated to Oct 31, 2026, with data from 89 participants in 65 countries, mostly for non-commercial use ([ECA&D](https://www.ecad.eu/)).
- **Copernicus C3S** global land in-situ data: 86,499 daily stations from 1718 to present, CC-BY, updated yearly ([C3S](https://cds.climate.copernicus.eu/datasets/insitu-observations-surface-land)).
- **WMO WIS2:** a second real-time route for foreign synoptic data.
  - Its GTS-to-WIS2 gateway has run since March 2025 ([WMO](https://wmo.int/media/news/wis2-operational-newsletter-no2)).
  - It had 116 nodes for 92 Members by June 30, 2026 ([WMO](https://wmo.int/media/news/wis2-operational-newsletter-no3)).
  - Its Global Cache, run by the Met Office and NOAA on AWS, keeps data for only 24 hours ([AWS Registry](https://registry.opendata.aws/wis2-global-cache/)).
- **Berkeley Earth:** CC BY-NC, with no station-level daily product ([Berkeley Earth](https://berkeleyearth.org/data/)). It reports GHCN-D as degraded since late August 2025.

DIRS-5 is partly contradicted: these cover Europe, yearly snapshots or the real-time stream, but none is a global, quality-controlled, daily-updated archive like GHCN-Daily.

## Gaps

- **ARL/ATDD's FY2026 status:** the enacted statement is silent. NOAA's FY2026 spend plan, held by NOAA's budget office, would settle it.
- **SSODv2 full-record integration:** only NCEI can confirm it (ncdc.ghcnd@noaa.gov). Spot-checking more station files for source flag "2" would settle it.
- **AWOS-C list of climate sites:** not published. The FAA AWOS program office holds it.
- **SMN stations to close:** not named. ATE union statements and the Boletín Oficial (DNU 274/2026, a snippet only) are the routes to them.
- **Unread:**
  - the MLex article on CMA's outbound-data rules (paywalled; a Wayback read was denied by the auto-mode classifier);
  - the Copernicus release note;
  - OGIMET, DWD CDC and RIHMI-WDC (not checked).
- **Saved but not reconciled:** some saved lines were not reviewed for the answer: USCRN station counts, CMA's open-data catalog, the ASOS equipment sheet, and NRCS Nevada's sensor replacement.
- **No DuckDuckGo pass ran:** the research stop came while the follow-up queue was being worked.
- `check-by-hand.md` lists the unread pages. `sites-to-trust.md` lists the hosts the sandbox refused.

## Sources

- [NCEI, USCRN product page](https://www.ncei.noaa.gov/access/crn/)
- [NOAA ARL, USCRN at ARL](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/)
- [Goodge, Quality Control of Data from the USCRN](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/research/Goodge.pdf)
- [NOAA, FY2027 budget justification](https://www.noaa.gov/organization/budget-finance-performance/budget-and-reports)
- [E&E News, House panel protects NOAA labs, 2025](https://www.eenews.net/articles/house-panel-protects-noaa-labs-research-from-trump-cuts/)
- [KGOU, federal funding law, 2026](https://www.kgou.org/weather-and-climate/2026-01-27/federal-funding-law-includes-money-for-oklahoma-weather-climate-institutions)
- [Congressional Record, FY2026 Joint Explanatory Statement, H255](https://www.govinfo.gov/content/pkg/CREC-2026-01-08/html/CREC-2026-01-08-pt3-PgH255.htm)
- [Congressional Record, H.R. 6938 text, H151](https://www.govinfo.gov/content/pkg/CREC-2026-01-08/html/CREC-2026-01-08-pt1-PgH151.htm)
- [Oak Ridge Today, ATDD stories, 2017 (Wayback)](https://web.archive.org/web/20251206192457/https://oakridgetoday.com/tag/atdd/)
- [NWS, Sterling Field Support Center](https://www.weather.gov/soic/)
- [NWS, Pressure Standards Laboratory](https://www.weather.gov/media/soic/NWS%20Pressure%20Standards%20Laboratory.pdf)
- [NWS, SFSC Temperature Laboratory](https://www.weather.gov/soic/TemperatureLab)
- [NWS, NWSI 30-2111, 2025](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf)
- [NWS, NWSI 10-1307, 2025](https://www.weather.gov/media/directives/010_pdfs/pd01013007curr.pdf)
- [NWS, ASOS Current Events](https://www.weather.gov/asos/CurrentEvents.html)
- [CBS Chicago, NWS staffing, 2025](https://www.cbsnews.com/chicago/news/national-weather-service-staffing-shortages-making-forecasts-worse)
- [NRCS Nevada, Snow Survey 2026](https://www.nrcs.usda.gov/state-offices/nevada/news/nevada-snow-survey-whats-new-for-2026)
- [Padilla and Schiff, letter to USDA and DOC, 2025](https://www.padilla.senate.gov/wp-content/uploads/12.22.25-Letter-to-USDA-DOC-on-Diminished-Water_Weather-Forecasting-and-Snowpack-Survey-Capacity.pdf)
- [NIST PML, Measurement Services Update, 2025](https://www.nist.gov/document/measurement-services-update)
- [CoCoRaHS, Why CoCoRaHS requires manual measurements](https://media.cocorahs.org/docs/Why%20CoCoRaHS%20requires%20manual%20measurements.pdf)
- [WMO, unified concept for regional instrument centres, 2026](https://extranet.wmo.int/edistrib_exped/grp_prs/_en/6742243-2026-ESDP-MINT_en.pdf)
- [WMO, list of Regional Instrument Centres, 2026](https://community.wmo.int/node/36165)
- [WMO, Secretariat Reorganization (2026)](https://wmo.int/sites/default/files/2026-08/WMO%20Secretariat%20Reorganization%20%282026%29.pdf)
- [Devdiscourse (Reuters), US pledges to UN bodies in Geneva, 2026](https://www.devdiscourse.com/article/international/3989889-us-pledges-tens-of-millions-to-un-bodies-in-geneva-sources-say)
- [Reuters via The Star, WMO funding, 2025](https://www.thestar.com.my/news/world/2025/10/24/un-weather-agency-reviews-priorities-as-funding-falls-short)
- [Bichos de Campo, SMN dismissals, 2026](https://bichosdecampo.com/esta-situacion-golpea-de-lleno-a-la-produccion-advierten-los-trabajadores-del-servicio-meteorologico-nacional-ante-una-nueva-oleada-de-despidos-y-la-posibilidad-de-que-cierren-estaciones/)
- [El Cronista, SMN strike, 2026](https://www.cronista.com/economia-politica/paro-en-el-servicio-meteorologico-por-despidos-y-denuncias-de-vaciamiento)
- [BMKG, budget reconstruction, 2025](https://www.bmkg.go.id/berita/utama/rekonstruksi-anggaran-bmkg-pastikan-layanan-informasi-publik-tetap-optimal)
- [WMO, WIS2 Operational Newsletter No.3, 2026](https://wmo.int/media/news/wis2-operational-newsletter-no3)
- [WMO, WIS2 Operational Newsletter No.2, 2025](https://wmo.int/media/news/wis2-operational-newsletter-no2)
- [WMO, CMA 2025 open data catalog](https://wmo.int/media/news-from-members/cma-releases-2025-catalog-of-popular-meteorological-data-open-sharing)
- [Global Times, foreign-related meteorological data, 2026](https://www.globaltimes.cn/page/202605/1362135.shtml)
- [Berkeley Earth, October 2025 Temperature Update](https://berkeleyearth.org/october-2025-temperature-update/)
- [Berkeley Earth, Data Overview](https://berkeleyearth.org/data/)
- [NWS, ASOS FAQ](https://www.weather.gov/asos/FAQ.html)
- [NWS, ASOS Sites by Equipment, 3/18/2025](https://www.weather.gov/media/asos/ASOS%20Sites%20by%20Equipment%20As%20Of%203_18_2025.xlsx)
- [FAA, ASWON](https://www.faa.gov/air_traffic/weather/aswon)
- [NCEI, GHCN-Daily status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)
- [NCEI, AG000060390.dly (Algiers)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/AG000060390.dly)
- [NCEI, GHCNh product page](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly)
- [ECCC, dd_info notice on Government of Alberta data, 2026](https://comm.collab.science.gc.ca/mailman3/hyperkitty/list/dd_info@comm.collab.science.gc.ca/thread/RLV2GKL3NV7GFSIYHOO5W4YL4WIJ6T2R/)
- [ECCC, ABgov_Station-Inventory.xlsx, 2026](https://comm.collab.science.gc.ca/mailman3/hyperkitty/list/dd_info@comm.collab.science.gc.ca/message/RLV2GKL3NV7GFSIYHOO5W4YL4WIJ6T2R/attachment/6/ABgov_Station-Inventory.xlsx)
- [NCEI, ghcnd-stations.txt (2026-11-23)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt)
- [NCEI, ghcnd-inventory.txt (2026-11-23; count by this run)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt)
- [SAM.gov, SSN-NCEI-RCC-2025, 2025](https://sam.gov/opp/247583e5d50d4edba32b36f7e860ea8f/view)
- [SAM.gov, WRWRC solicitation 1332KP26R0028, 2026](https://sam.gov/opp/373385828b37436ba1c94f8d0f6dbe11/view)
- [USAspending, Regional Weather Records Center awards, 2026](https://www.usaspending.gov/keyword_search/Regional%20Weather%20Records%20Center)
- [USAspending, award 1332KP26D0008, 2026](https://www.usaspending.gov/award/CONT_IDV_1332KP26D0008_1330)
- [NCEI Alerts](https://www.ncei.noaa.gov/alerts)
- [NCEI, ghcnd-version.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt)
- [CISESS, annual report 2020–21](https://cisess.umd.edu/)
- [Willett et al., NODD, Science Advances, 2023](https://repository.library.noaa.gov/view/noaa/59059/noaa_59059_DS1.pdf)
- [Met Office, HadISD](https://www.metoffice.gov.uk/hadobs/hadisd/)
- [HadISD blog, potentially the final release, 2025](https://hadisd.blogspot.com/2025/09/hadisd-v342202508p-potentially-final.html)
- [ECA&D home page](https://www.ecad.eu/)
- [Copernicus C3S, global land in-situ observations](https://cds.climate.copernicus.eu/datasets/insitu-observations-surface-land)
- [Registry of Open Data on AWS, WIS2 Global Cache](https://registry.opendata.aws/wis2-global-cache/)

Saved in [`web_search_results/2026-11-23_ghcn-daily-infrastructure-pt8/`](./): this answer, `method.md`, `research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
