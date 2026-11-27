# USCRN Daily (daily01): threats to its inputs, Jan 2024 – Nov 2026, and what could replace them

**Direct answer.** Overall the threat to USCRN Daily's inputs is **emerging**. No input was cut or closed outright. Three things are close to imminent, though:
- **Operations at the stations are degrading now.** Days with missing precipitation in daily01 rose from 1,893 (2024) to 2,810 (2025) to 4,481 (2026, to Nov 15). Eight Alaska stations went silent for 4–8 months in 2025–26, and three CONUS stations stopped reporting in 2026.
- **The datalogger is retired.** Campbell retired the CR3000 in 2022, and its free support ends 2027-12-31.
- **Maintenance has slipped, and the field team's parent lab is in question.** NOAA's budget requests proposed closing ARL. Of 26 stations checked in NCEI's station-history log, 21 had an annual visit in 2024 but only 10 in 2025–26.

The gauge, the wetness sensor and the tipping bucket face no current threat. The GOES link met its May 2026 deadline. No substitute network matches USCRN's reference quality. Confidence: moderate. The file evidence is strong, but almost no source explains the outages.

## Ratings by input

| Input | What happened (2024–2026) | Status | Rating |
|---|---|---|---|
| **Stations and site agreements** | Ivotuk AK's record ends 2023-04-07, and Blue Hill MA was added 2024-09-17. A Kingston RI station is "scheduled to be decommissioned the summer of 2026" but still reported to 2026-11-14. Alaska build-out: the plan was the final 6–7 stations by Sept 2026, "funding dependent"; none were added in 2024–26. Outages: 8 AK stations were out for months, and Joplin MO, St. Mary MT and Edinburg TX went silent in 2026 | outages happening; closure planned; build-out stalled | **imminent** (operational disruption) |
| **Geonor T-200B and its maker** | On sale from Geonor Inc. (NJ) and Geonor AS (Norway), with no discontinuation notice. Geonor AS is in the Norwegian register | none | no current threat found |
| **Vaisala DRD11A** | Product page live, no end-of-life wording | none | no current threat found |
| **TB-3 tipping bucket** | Sold as KISTERS TB3 (HSA acquired 2020), no successor notice | none | no current threat found |
| **Dataloggers (Campbell CR3000)** | Retired 2022-01-06. Free support ends 2027-12-31, repair and calibration 2032-12-31. Its named replacement, the CR1000X, was itself retired 2024-12-31 (now CR1000Xe). No NOAA migration plan found | vendor end of support enacted, takes effect 2027 | **emerging** |
| **GOES DCS link** | CS2 certification was required by May 31, 2026, "No waivers"; the old TX320 transmitter reached end of life 2025-03-31. The swap finished 2026-04-25. Short DCS outages: 2025-02-12 (1 h 16 min) and the GOES-19 safehold 2026-07-15/16. DADDS replacement planned for end of 2026 | deadline met; outages resolved | emerging (minor) |
| **ATDD field and calibration team** | Eight technicians and engineers make annual visits and calibrate sensors in-house. ISIS (26 stations checked): annual visits fell from 21 logged in 2024 to 10 in 2025–26; 10 stations have nothing logged after 2024 (Hilo since 2022). FY2026/27 requests proposed closing ARL; Congress has not enacted it (Part 4) | proposed | **emerging** |

Sources by row:
- **Stations:** [NCEI daily01 snapshot, 2026](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/snapshots/CRND0103-202611160850.zip) (counted by this run); [NCEI element listing](https://www.ncei.noaa.gov/access/crn/element-listing); [ARL, Blue Hill, 2024](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-blue-hill-observatory/); [ARL review response, 2023](https://www.arl.noaa.gov/wp_arl/wp-content/uploads/2025/02/ARL-Review-Response-Sept-30-2023-edited.pdf).
- **Instruments:** [Geonor Inc.](https://geonor.com/t-200b-all-weather-precipitation---rain-gauge); [Brønnøysund register](https://virksomhet.brreg.no/en/oppslag/enheter/911954567); [Vaisala](https://www.vaisala.com/en/products/weather-environmental-sensors/rain-detector-drd11a); [KISTERS TB3](https://hydromet-products.kisters-group.com/products/instruments/meteorology/tb3/); [KISTERS, 2020](https://www.kisters.net/hydrological-services-america-hsa-joins-the-kisters-group/).
- **Dataloggers:** [Campbell CR3000 notice, 2021](https://s.campbellsci.com/documents/us/miscellaneous/cr3000-discontinuation-notice.pdf); [CR3000 page](https://www.campbellsci.com/products/cr3000); [CR1000X page](https://www.campbellsci.com/products/cr1000x).
- **GOES DCS:** [GOES DCS TWG minutes, 2024](https://www.noaasis.noaa.gov/pdf/docs/TWG2024/Spring2024TWGMinutes.pdf); [Campbell TX320](https://www.campbellsci.com/products/tx320); [ESPC 2025-02-12](https://ospo.noaa.gov/data/messages/2025/02/MSG_20250212_1541.html); [ESPC 2026-07-16](https://ospo.noaa.gov/data/messages/2026/07/MSG_20260716_1637.html); [TWG 2025 DADDS deck](https://www.noaasis.noaa.gov/pdf/docs/TWG2025/1400%20Replacement%20DADDS%20Demo%20&%20User%20Input%20Detwiler.pdf).
- **Field team:** [ARL, USCRN at ARL](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/); NCEI ISIS station histories ([Kingston 1 W](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1043), [Deadhorse 3 S](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1793), [Asheville 8 SSW](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1026), [Bethel 87 WNW](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1800)).

## What the daily01 files show

| Year | Station files | CONUS | AK | HI | Days with precipitation missing (−9999) | Stations added / dropped |
|---|---|---|---|---|---|---|
| 2023 | 159 | 132 | 25 | 2 | not counted | +Galena, +Huslia (AK) |
| 2024 | 159 | 133 | 24 | 2 | 1,893 | +Blue Hill MA / −Ivotuk AK |
| 2025 | 159 | 133 | 24 | 2 | 2,810 | none |
| 2026 (to Nov 15) | 159 | 133 | 24 | 2 | 4,481 | none |

Sources: counted by this run's script from [NCEI's 2026-11-16 daily01 snapshot](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/snapshots/CRND0103-202611160850.zip). The file counts include the Alabama regional-network sites and the Egbert, Ontario test site, so they are not the commissioned-station count; ARL gives 141 stations (2024). Each figure's source, file and passage are in `results.csv`. (**High** confidence.)

- **Alaska outages.** Eight Alaska stations had neither precipitation nor temperature for months:
  - Deadhorse: 2025-03-30 to 2026-08-10.
  - Bethel: 2025-11-19 to 2026-08-26.
  - Ruby: to 2026-08-21.
  - Galena: 2026-01-28 to 2026-08-17.
  - Cordova, Denali, Glennallen and Tok: to mid-May 2026.

  These are whole-station losses rather than gauge faults, and they ended around the summer 2026 field season. No source gives the cause.
- **Whole-year precipitation gaps.** Precipitation is missing all of 2026 at Gadsden AL (also 2024–25), Bedford IN (also 2025) and Denio NV. This looks like gauge failures that went unrepaired.
- **Stations that stopped in 2026:**
  - Joplin MO: last data 2026-09-24.
  - St. Mary MT: last data 2026-10-11.
  - Edinburg TX: all values missing after 2026-07-21.

  stations.tsv gives no USCRN closing date in 2024–2026, and still lists Ivotuk as operational. (**High** for the counts; causes unknown.)
- **Kingston RI.** The Kingston RI station is being retired because a paved parking lot was built "just over 300 feet away". Blue Hill was added so that "USCRN will maintain the number of stations" ([ARL, 2024](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-blue-hill-observatory/)).
- **Alaska counts disagree** (not resolved):
  - ARL wrote in 2023 that "In FY23, ARL installed two new stations in Alaska for a total of 29" ([ARL, 2023](https://www.arl.noaa.gov/wp_arl/wp-content/uploads/2025/02/ARL-Review-Response-Sept-30-2023-edited.pdf)).
  - NCEI says 25 Alaska stations, "with a plan to eventually have a total of 29" ([NCEI overview](https://www.ncei.noaa.gov/access/crn/overview.html)).
  - daily01 has files for 25 Alaska stations in 2023 and 24 in 2024–26.

  ARL's 29 is probably the planned total, not stations installed. I rely on the files.
- **Maintenance log.** I checked NCEI's public station-history log (ISIS) for 26 of about 139 stations across all regions, including those with outages ([tally](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1019)):
  - 21 had an annual visit logged in 2024.
  - **10** had one logged in 2025–26: Monahans, Socorro, Arco, Sioux Falls, Goodridge, Joplin, Edinburg, Champaign, Tucson and Galena. Most of these 2025 visits also swapped the transmitter.
  - **5** had only a 2025 transmitter swap ("GOES ID Change"): Montrose, Redding, Utqiaġvik, Sitka and Stillwater.
  - **1** had only a rain-gauge service: Denio NV, in 2025. Its last annual visit was 2022, and its precipitation has been missing since July 2025.
  - **10** have nothing logged after 2024: Kingston RI, Deadhorse, Bethel, Fairbanks, Asheville, Elkins, St. Mary, Durham NH, Moose and Hilo HI (nothing since 2022).

  The log lags: only one 2026 visit is logged (Tucson), although the transmitter swap finished in April 2026 and the Alaska stations came back in summer 2026. So 2026 is under-recorded. Even so, 2025 shows the yearly visits slipping. (**Moderate**: NCEI's own log, but 26 stations, not chosen at random.)

## Suppliers and backups

- **Gauge.** More than one maker could supply a weighing gauge.
  - Geonor has US and Norwegian companies.
  - NOAA tested an Ott Pluvio for USCRN in 2003–05; it over-caught by up to 3% against the Geonor ([NCEI TN05002](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/technotes/TN05002PrecipTesting.pdf)).
  - USCRN's stated policy (2013) is to run alternative models side by side "in case that model is discontinued" ([Diamond et al., 2013](https://mural.maynoothuniversity.ie/6481/1/PT_US%20climate.pdf)).
  - No NOAA gauge test since 2024 was found. Iceland's Met Office found in 2023/24 that the Pluvio2 L caught about 50% less than the Geonor at one snowy site, and it is going back to Geonor ([IMO, ISSW 2024](https://arc.lib.montana.edu/snow-science/objects/ISSW2024_P8.30.pdf)). So the Pluvio is a weaker substitute in snow. (Moderate.)
- **Datalogger.** The replacement path runs through Campbell alone: the CR1000Xe, after the CR1000X was itself retired. No NOAA plan or spares figure was found.
- **Transmission.** GOES DCS is the only path found. Its own backup receive system is at NSOF Suitland. The Fairmont WV backup site has no DCS receive system; a move there was "tentative" for 2024, and whether it happened was not found ([Wallops TWG 2025 deck](https://noaasis.noaa.gov/pdf/docs/TWG2025/1105%20Wallops%20Command%20and%20Data%20Acquisition%20Update%20Sullivan.pdf)). No USCRN Iridium, cellular or other backup was found. Part 1 found only an ATDD FTP gap-fill path.
- **Field team.** No backup maintenance provider was found. The crew's size differs by source and scope: ARL's undated page says "eight technicians and engineers"; four technicians installed Blue Hill in 2024; Part 4 reported a crew of five for the 2026 transmitter swap. Site hosts do only "small resets and replacements" ([ARL](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/)). Calibration is done in-house against NIST-traceable standards "re-certified annually" ([NOAA X041 plan, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X041_d0.pdf)); who re-certifies them was not found.

## Substitutes for USCRN Daily

None matches USCRN's reference quality: triple-wire weighing gauges in a double-fence shield, pristine siting, and annual calibration. USCRN is treated as "ground truth" in comparisons ([Buban et al., 2020](https://repository.library.noaa.gov/view/noaa/29193/noaa_29193_DS1.pdf)).

| Network | Coverage | Siting and quality versus USCRN | Status 2024–2026 |
|---|---|---|---|
| COOP (NWS) | about 6,700 sites | Manual or unshielded gauges. Known inconsistencies include "inadequate maintenance" ([Demaria et al., 2019](https://repository.library.noaa.gov/view/noaa/69347/noaa_69347_DS1.pdf)) | "Right-sizing" proposed in May 2026 ([Federal Register 2026-09099](https://public-inspection.federalregister.gov/2026-09099.pdf)) |
| ASOS (NWS/FAA) | airports | Aviation siting. At Frankfort KY the replacement AWOS "typically do[es] not meet" climate-record criteria | Frankfort KY retired as a climate site in 2025 ([NWS Louisville](https://www.weather.gov/lmk/FrankfortASOSRetiringasOfficialNWSClimateSite)); national status not found |
| State mesonets | e.g. Oklahoma 120, NY 127 stations | Mostly unheated tipping buckets. Weighing gauges are used "in high-quality networks (e.g., U.S. Climate Reference Network)" ([AASC, 2019](https://stateclimate.org/docs/AASC%20Recommendations%20and%20Best%20Practices%20for%20Mesonets%20-%20Final,%20Ver%201;%20approved%2026%20Jun%2019.pdf)) | NY Mesonet $3M DHS grant cut in 2025 ([Schumer, 2025](https://www.schumer.senate.gov/newsroom/press-releases/schumer-demands-trump-admin-immediately-reverse-ripping-away-funding-for-ualbanys-mesonet-new-yorks-state-of-the-art-weather-tracking-system-that-helps-keep-upstate-ny-communities-prepared-and-safe-during-storms)); Oklahoma state-funded, no cut found ([OU, 2025](https://www.ou.edu/news/articles/2025/august/oklahoma-mesonet-honored-for-30-years-of-service)) |
| SNOTEL (NRCS) | about 900 mountain sites | Snow-focused, mountain siting | Staff losses in 2025: Portland office down from 12 to 5 ([OPB, 2025](https://www.opb.org/article/2025/03/11/snow-or-no-northwests-water-outlook-gets-murky-with-federal-cuts/)). Sites were "offline for unusually long periods" ([50-group letter, 2025](https://www.mountaineers.org/conservation/advocacy/comment-letters/2025-comment-letters/04-17-25-outdoor-recreation-snotel-support-letter-to-usda-nrcs.pdf)). Counterpoint: Nevada kept up maintenance ([NRCS Nevada, 2025](https://www.nrcs.usda.gov/state-offices/nevada/news/nevada-snow-survey-whats-new-for-2026)) |
| Canada RCS (ECCC) | not found | Used for ECCC's adjusted (homogenized) climate data ([ECCC](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-adjusted-climate-data.html)) | not found |
| USRCRN (context) | 72 Southwest sites | Built to USCRN standards | Funding was cut in the FY14 omnibus and the data ended in 2014 ([NWS SCN 14-25](https://www.weather.gov/media/notification/pdfs/scn14-25usrcrn_decom.pdf)) |

## DIRS criteria

- **DIRS-1** (depends on an external calibration service): **mostly contradicted.** Calibration is in-house at ATDD. There is partial support: Campbell's repair and calibration of the CR3000 ends in 2032, and who re-certifies ATDD's standards is unknown.
- **DIRS-2** (upstream networks or platforms aging out or losing funding): **supported.**
  - The CR3000 is retired, and its named successor was also retired in 2024.
  - The TX320 transmitter reached end of life in 2025; the risk was handled by the April 2026 swap.
  - The Alaska build-out is "funding dependent" and stalled.
  - ARL closure was proposed.
  - Outages are rising.
- **DIRS-3** (upstream data feeds vulnerable): **supported.** GOES DCS is the only feed found. Whole-station outages lasting months in Alaska and 4,481 missing precipitation days in 2026 show data loss that was not back-filled.
- **DIRS-5** (no alternative supplier): **contradicted for the gauge** (two Geonor firms, OTT tested). **Supported for the field team** (no backup provider) **and for the dataset** (no reference-quality substitute). Partly supported for the datalogger (one vendor's line).

## Gaps

- **Outage causes.** Why the Alaska stations, Joplin, St. Mary and Edinburg went silent, why Ivotuk ended and why Alaska installs paused: ARL/ATDD holds this (ISIS event notes, ARL quarterly reports).
- **2025 maintenance visits.** 26 of about 139 stations were checked in ISIS. The other 113 station pages (ids in stations.tsv) would complete the count; ARL/ATDD's own trip records would show what ISIS misses.
- **Datalogger plan.** NOAA's plan for replacing the CR3000: ATDD.
- **DADDS cutover.** The 2026 GOES DCS overview deck could not be read (NESDIS).
- **Canada RCS.** Count and status were not found.
- **Earlier findings.** The ARL budget status and the CISESS/ORAU field-crew arrangement come from Part 4 and were not re-checked here.
- **Unread pages.** `check-by-hand.md` lists them; `sites-to-trust.md` lists the hosts the sandbox refused, which you may want to allow.

## Sources

Full details (titles, dates, saved files, passages) are in `research-record.json`.

**NOAA data and station records**
- [NCEI, daily01 weekly snapshot CRND0103-202611160850.zip, 2026](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/snapshots/CRND0103-202611160850.zip) (counted by this run)
- [NCEI, USCRN stations.tsv, 2026](https://www.ncei.noaa.gov/pub/data/uscrn/products/stations.tsv)
- [NCEI, USCRN element listing](https://www.ncei.noaa.gov/access/crn/element-listing) (read via extract)
- [NCEI, USCRN program overview](https://www.ncei.noaa.gov/access/crn/overview.html)
- [NCEI ISIS station histories for 22 stations (ids 1019–1802), tallied by this run, 2026](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1019)
- NCEI ISIS station histories: [Kingston 1 W](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1043), [Deadhorse 3 S](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1793), [Asheville 8 SSW](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1026), [Bethel 87 WNW](https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1800)

**NOAA ARL and ATDD**
- [ARL, Blue Hill added to USCRN, 2024](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-blue-hill-observatory/)
- [ARL, USCRN at ARL (undated)](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/)
- [ARL, Science Review response, 2023](https://www.arl.noaa.gov/wp_arl/wp-content/uploads/2025/02/ARL-Review-Response-Sept-30-2023-edited.pdf) (read via Wayback)
- [NOAA, USCRN Field Site Maintenance Plan X041, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X041_d0.pdf)
- [NCEI, TN05002 precipitation gauge testing, 2005](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/technotes/TN05002PrecipTesting.pdf)
- [Diamond et al., USCRN after one decade, 2013](https://mural.maynoothuniversity.ie/6481/1/PT_US%20climate.pdf)

**GOES DCS (NESDIS)**
- [GOES DCS TWG Spring 2024 minutes](https://www.noaasis.noaa.gov/pdf/docs/TWG2024/Spring2024TWGMinutes.pdf) (read via Wayback)
- [TWG 2025, Wallops update](https://noaasis.noaa.gov/pdf/docs/TWG2025/1105%20Wallops%20Command%20and%20Data%20Acquisition%20Update%20Sullivan.pdf) (read via Wayback)
- [TWG 2025, Replacement DADDS](https://www.noaasis.noaa.gov/pdf/docs/TWG2025/1400%20Replacement%20DADDS%20Demo%20&%20User%20Input%20Detwiler.pdf) (read via Wayback)
- [ESPC, DCS data outage, 2025-02-12](https://ospo.noaa.gov/data/messages/2025/02/MSG_20250212_1541.html)
- [ESPC, GOES-19 safehold, 2026-07-16](https://ospo.noaa.gov/data/messages/2026/07/MSG_20260716_1637.html)

**Makers**
- [Campbell Scientific, CR3000 discontinuation notice, 2021](https://s.campbellsci.com/documents/us/miscellaneous/cr3000-discontinuation-notice.pdf)
- [Campbell, CR3000 page](https://www.campbellsci.com/products/cr3000), [CR1000X page](https://www.campbellsci.com/products/cr1000x), [TX320 page](https://www.campbellsci.com/products/tx320) (read via extract)
- [Geonor Inc., T-200B series](https://geonor.com/t-200b-all-weather-precipitation---rain-gauge) (read via extract)
- [Brønnøysund Register, Geonor AS](https://virksomhet.brreg.no/en/oppslag/enheter/911954567) (read via extract)
- [Vaisala, DRD11A](https://www.vaisala.com/en/products/weather-environmental-sensors/rain-detector-drd11a) (read via extract)
- [KISTERS, TB3](https://hydromet-products.kisters-group.com/products/instruments/meteorology/tb3/) (read via extract)
- [KISTERS, HSA joins KISTERS, 2020](https://www.kisters.net/hydrological-services-america-hsa-joins-the-kisters-group/)
- [Icelandic Met Office, ISSW 2024 gauge comparison](https://arc.lib.montana.edu/snow-science/objects/ISSW2024_P8.30.pdf)

**Substitute networks**
- [Federal Register 2026-09099, COOP request for comments, 2026](https://public-inspection.federalregister.gov/2026-09099.pdf)
- [Demaria et al., COOP reliability, 2019](https://repository.library.noaa.gov/view/noaa/69347/noaa_69347_DS1.pdf)
- [Buban et al., USCRN comparison, 2020](https://repository.library.noaa.gov/view/noaa/29193/noaa_29193_DS1.pdf)
- [NWS Louisville, Frankfort ASOS retiring, 2025](https://www.weather.gov/lmk/FrankfortASOSRetiringasOfficialNWSClimateSite)
- [AASC, Mesonet best practices, 2019](https://stateclimate.org/docs/AASC%20Recommendations%20and%20Best%20Practices%20for%20Mesonets%20-%20Final,%20Ver%201;%20approved%2026%20Jun%2019.pdf) (read via extract)
- [Sen. Schumer, NY Mesonet funding, 2025](https://www.schumer.senate.gov/newsroom/press-releases/schumer-demands-trump-admin-immediately-reverse-ripping-away-funding-for-ualbanys-mesonet-new-yorks-state-of-the-art-weather-tracking-system-that-helps-keep-upstate-ny-communities-prepared-and-safe-during-storms)
- [University of Oklahoma, Mesonet at 30, 2025](https://www.ou.edu/news/articles/2025/august/oklahoma-mesonet-honored-for-30-years-of-service)
- [OPB, SNOTEL and federal cuts, 2025](https://www.opb.org/article/2025/03/11/snow-or-no-northwests-water-outlook-gets-murky-with-federal-cuts/) (read via extract)
- [50-group SNOTEL letter to NRCS, 2025](https://www.mountaineers.org/conservation/advocacy/comment-letters/2025-comment-letters/04-17-25-outdoor-recreation-snotel-support-letter-to-usda-nrcs.pdf) (read via extract)
- [NRCS Nevada, Snow Survey 2026](https://www.nrcs.usda.gov/state-offices/nevada/news/nevada-snow-survey-whats-new-for-2026) (read via extract)
- [ECCC, Adjusted climate data technical documentation](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services/display-download/technical-documentation-adjusted-climate-data.html)
- [NWS, SCN 14-25 USRCRN termination, 2014](https://www.weather.gov/media/notification/pdfs/scn14-25usrcrn_decom.pdf)

Saved in [web_search_results/2026-11-27_uscrn-daily-inputs-pt5/](web_search_results/2026-11-27_uscrn-daily-inputs-pt5/): this answer, the research record, `results.csv`, `check-by-hand.md`, `sites-to-trust.md` and the counting scripts in `work/`.
