# CoCoRaHS Part 2: QC, calibration, software, documentation and FAIR

CoCoRaHS's daily reports get automated form checks when they are entered. CoCoRaHS headquarters staff and some volunteer coordinators then review them by hand each day, and NCEI runs its automated GHCN-Daily QA once the reports reach it. "Calibration" rests on CoCoRaHS's own approved-gauge list, its training material and one single-site gauge test. No paired comparison with NWS gauges is published. All production software is CoCoRaHS's own, runs on Microsoft Azure plus the vendor Carto's map platform, and none of its code is published. The data are open (CC BY 4.0, CSV/XML/SHEF), but only GHCN-Daily's copy passes the Findable test. On the four risks: P-3 and DIRS-4 are supported, D-4 is contradicted, and DIRS-1 is mostly contradicted. **Overall confidence: moderate to high.**

The April 2019 document is still the current one: the May 2026 QA/QC update says it "describes the automated and manual processes for QA/QC" and that it is in the site's FAQ/Help section ([CoCoRaHS, QA/QC Update 2026](https://media.cocorahs.org/docs/WCC_2026_Day2_Hilberg_QAQC.pdf)). No newer version was found (**moderate**: the media.cocorahs.org docs folder was not listed in the Wayback Machine).

## Quality control

- **Automated checks on entry** (**high**). These are format and consistency rules on the web forms ([CoCoRaHS QA/QC, 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf), pp. 1–2):
  - the date can't be in the future;
  - precipitation must be to the hundredth, T or NA, and "Any value up to and including 30.00 is allowed";
  - snow water equivalent can't be more than 90% of the snow depth;
  - only one daily report per station per date;
  - multi-day reports must be at most 60 days and can't overlap daily reports.

  There are no range checks against neighbours at entry. The 2026 slides add that multi-day/daily conflicts "can no longer be entered".
- **Manual review** (**high**). "CoCoRaHS headquarters staff and a number of our volunteer coordinators review the data each day." They use the national maps, a web tool that compares each report with its neighbours, and the NWS's MPE and radar maps. A questionable report "may be changed to 'NA'", a comment is added, and a QC ticket goes "to the regional coordinator and state coordinator", who follow up with the observer ([QA/QC 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf), p. 3).
  - Overflow reports of 11 or 12 inches with no comment are set to NA until the observer is reached.
  - The NWS is not named as a reviewer, and neither are Colorado Climate Center staff by that name (HQ is in Fort Collins).
  - One staff member does most of the QC. There were 4,541 QC tickets from May 16, 2019 to May 15, 2020, against 5,900 in 2017–2018 ([Hilberg, WERA 2020](https://media.cocorahs.org/docs/HilbergWERA20.pdf)). The 2026 slides list "Enlisting coordinators to consistently help with QC" as a challenge.
  - In 5/2025–4/2026, false zeros were 43.0% of tickets and date errors 18.5% ([QA/QC 2026](https://media.cocorahs.org/docs/WCC_2026_Day2_Hilberg_QAQC.pdf)).
- **Corrections** are made through a monthly "frequent offender" report and a Data Correction Form in the Data Explorer ([QA/QC 2024](https://media.cocorahs.org/docs/WERA_2024_11_QAQC_update_Hilberg.pdf)). A daily NA report is deleted only on request to HQ ([Data-entry FAQ](https://www.cocorahs.org/Content.aspx?page=faqdataentry)).
- **NCEI** (**high**). Data "are continually streamed", and stations with at least 100 values for an element enter GHCN-Daily. There the values go through "fully automated" QA: the document lists 24 checks (trace-flag, duplicate, bounds, streak, frequent-value, gap, snow ratio, spatial and climatological-outlier). A failing value "is assigned an associated data quality flag"; it is not deleted ([QA/QC 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf), pp. 4–5). NCEI's own 2022 slides describe flag files sent to NWS offices for review. They also describe a check for CoCoRaHS data that duplicate NWS/COOP submissions, which affected 215 GHCN-Daily stations in 2014 and 345 in 2022 ([NCEI and CoCoRaHS Data, 2022](https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf)).
- **Conflict, resolved:** whether the QC ticket system (QCTS) is part of the main database.
  - The 2021 minutes say ticketing was "integrated" after the move to Azure ([WERA1012 minutes 2020–22](https://nimss.org/storage/3841/WERA1012_Summary_of_Meeting_Minutes_2020-2022.pdf)).
  - The June 2024 IT slides call QCTS "completely isolated", on its own MySQL/JSP stack ([Turner, IT Update 2024](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf)).
  - The 2026 slides say "QCTS moved to CoCoRaHS web site as of 10/1/2024".
  - My reading: it was on CoCoRaHS's own servers by 2021 and part of the web site from October 2024.
- **Against the risks:** QC that depends on NWS MPE and radar maps is a minor outside input to QC (weak support for DIRS-1). The undocumented review criteria support P-3.

## Calibration

- **Gauge standard** (**high**). CoCoRaHS headquarters sets it. The [Approved Rain Gauges page](https://www.cocorahs.org/Content.aspx?page=approved_rain_gauges) lists three gauges:
  - the Stratus 4-inch by Productive Alternatives, which "meets the minimum requirements set by the National Weather Service to be within +/- 4% of the Standard Rain Gauge";
  - the TROPO 4-inch by Climalytic, which "CoCoRaHS Headquarters is pleased to designate";
  - the NWS 8-inch gauge.

  "Digital/electronic rain gauges are not approved." WeatherYourWay.com is "the official CoCoRaHS gauge supplier" ([Rain Gauge Suppliers](https://www.cocorahs.org/Content.aspx?page=Store)). No written NWS specification for the ±4% figure was found.
- **Comparisons** (**moderate**). The only published test with figures is CoCoRaHS's own ten-year side-by-side test at CSU's Fort Collins campus station (1995–2004). The 4-inch gauge averaged 16.42 in a year against 15.95 in for the 8-inch SRG: "0.47" per year is 3%". By year, the 4-inch gauge read between 0.8% and 5.8% higher ([Doesken, AMS](https://ams.confex.com/ams/pdfpapers/91615.pdf)). CoCoRaHS also states 101–105% catch efficiency from three decades of Colorado tests ([Why manual gauges](https://media.cocorahs.org/docs/WhyManualGauge.pdf)).
  - **No peer-reviewed paired comparison of CoCoRaHS reports with NWS COOP, ASOS or USCRN gauges was found.** Two AMS abstracts by CoCoRaHS staff compare frequency distributions with COOP stations, with no figures published ([AMS 2011 abstract](https://ams.confex.com/ams/19Applied/webprogram/Paper190535.html), [AMS 2010 abstract](https://ams.confex.com/ams/90annual/webprogram/Paper162256.html); abstracts only).
  - A [USGS report (OFR 2018-1061)](https://pubs.usgs.gov/of/2018/1061/ofr20181061.pdf) goes the other way: it uses 51 CoCoRaHS gauges as the reference for USGS gauges. In freezing weather, heated USGS gauges caught 61% less than the CoCoRaHS gauges.
- **Training** rests on CoCoRaHS's own slide show (V10.1), its snow and siting pages and webinars ([Training Slide Shows](https://www.cocorahs.org/Content.aspx?page=training_slideshows), [Snow](https://www.cocorahs.org/Content.aspx?page=Snow)). No source says training is required.
- **Against the risks:** DIRS-1 is mostly contradicted. There is no external calibration service; the standard is CoCoRaHS's own. The supply side leans on one maker of the most common gauge, but a second approved maker exists.

## Software and facilities

All of this comes from the CoCoRaHS IT lead's 2024 slides ([Turner, 2024](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf)) (**high**). Code status for each part is at the end of this section.

- **Hosting:** all public applications sit behind "an Azure Front Door service with Web Application Firewall". The primary database is SQL Server, with a PostgreSQL copy kept in sync for maps. A Databricks lakehouse is planned.
- **Maps:** maps.cocorahs.org is an Angular app on "the Carto raster mapping platform" with "a shared Carto database". The plan is to move it to a CoCoRaHS-managed PostgreSQL in Azure.
- **Apps:** the original mobile apps "were created by an observer years ago", and "He no longer wants to maintain them". The new app is a React Native shell around mobile.cocorahs.org, which talks to api2.cocorahs.org. The App Store names an individual, Julian Turner, as seller and developer (snippet only).
- **Data export and the Data Explorer:** data.cocorahs.org (Export Manager) and dex.cocorahs.org are CoCoRaHS's own web applications. The QCTS "was inherited years ago" and moved off a Midwest Regional Climate Center server around 2020 ([minutes](https://nimss.org/storage/3841/WERA1012_Summary_of_Meeting_Minutes_2020-2022.pdf)).
- **Code:** none of the production code is published (**moderate**).
  - A GitHub search found no CoCoRaHS or Colorado Climate Center organization; the slides list "Migrate all DevOps to GitHub" as a future project.
  - The only public CoCoRaHS code is the retired volunteer Android app, [sjwoodr/CoCoRaHS](https://github.com/sjwoodr/CoCoRaHS) (licence file not read).
  - Every other component is only described on the site.
- **Against the risks:** DIRS-4 is supported. Producing and serving the data needs Microsoft Azure and Carto, which are vendor facilities. Who holds the Azure subscription (CSU or CoCoRaHS) was not found.

## Documentation

The documentation supports P-3 (**moderate**). It is written for observers:
- a 73-page training slide show ([v9.2B](https://media.cocorahs.org/docs/CoCoTrainingSlideshow_v9.2B.pdf));
- the data-entry FAQ;
- the five-page QA/QC document, which gives manual review one paragraph and no criteria.

The coordinator's duties are a one-page 2006 list, where "Check data routinely" is an optional task for the "really, really willing" ([Local Coordinator description](https://media.cocorahs.org/docs/CoCoRaHs_LocalCoordinatorDescription2006.pdf)). The IT slides list system-admin, database and cyberinfrastructure documentation as future projects. The 2026 slides want coordinator webinars on "how we determine if an observation is an error – the process". A newcomer could keep observers reporting, but could not rebuild the review process or the systems from what is written.

## FAIR, by route

| Route | Rating | Tests failed | Notes |
|---|---|---|---|
| ViewData report pages | partly FAIR | F (no DOI; NOAA catalog record gives DOI "N/A"), I (HTML tables) | HTTPS, no login (Part 1); CC BY 4.0 |
| Export Manager (CSV, XML, SHEF) | partly FAIR | F; I partly (no column or flag documentation found) | open formats; ASP.NET form, not a documented URL scheme; CC BY 4.0 |
| CoCoRaHS API (api2) | non-FAIR as a public route | F, A (not documented or publicized), I | a keyed public Web API is planned; CUAHSI separately serves a WaterOneFlow SOAP copy |
| GHCN-Daily copy at NCEI | FAIR (R partly) | R partly: the record lines read give a citation and a disclaimer, not a named licence | DOI 10.7289/V5D21VHZ; NCEI catalog; HTTPS, AWS and Google Cloud with no login; documented format with flags |

*Sources by row:* [Data Usage Policy](https://www.cocorahs.org/Content.aspx?page=datausagepolicy) (CC BY 4.0); [NOAA DIF record](https://paleo.ltrr.arizona.edu/dc/noaa-other-1002736.xml) (DOI N/A); [DataCite search](https://api.datacite.org/dois?query=CoCoRaHS) (33 records, none a CoCoRaHS dataset); [Export Manager](https://data.cocorahs.org/cocorahs/export/exportmanager.aspx); [Turner 2024](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf) (API); [CUAHSI WaterOneFlow](https://hydroportal.cuahsi.org/CocoRaHs/cuahsi_1_1.asmx); [NCEI C00861](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html).

No route needs proprietary software to read the data. D-4 is contradicted: CSV, XML and SHEF are open, and GHCN-Daily's formats are documented. What is proprietary is the server stack (SQL Server, Azure, Carto), which is a DIRS-4 matter, not D-4.

## Gaps

- Not found:
  - a newer QA/QC document;
  - written criteria for manual QC;
  - a written NWS gauge specification;
  - who holds the Azure subscription (ask info@cocorahs.org);
  - the Export Manager's column documentation;
  - re3data registration (lookup refused by the sandbox).
- Saved but not reconciled: the 2015–2026 ticket-total chart (its labels couldn't be matched to years) and four sources with no saved file (two AMS abstracts, the GitHub results, the CUAHSI service page).
- [check-by-hand.md](check-by-hand.md) lists 3 pages: the 2014 NSF PI slides on the Web API, re3data, and the Google Play listing.
- [sites-to-trust.md](sites-to-trust.md) lists 5 refused hosts; you can decide whether to add any to the sandbox's allowed domains.

## Sources

- CoCoRaHS: [QA/QC document, Apr 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf); [QA/QC Update 2026](https://media.cocorahs.org/docs/WCC_2026_Day2_Hilberg_QAQC.pdf); [QA/QC Update 2024](https://media.cocorahs.org/docs/WERA_2024_11_QAQC_update_Hilberg.pdf); [QC Team, 2020](https://media.cocorahs.org/docs/HilbergWERA20.pdf); [IT Update 2024](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf); [Approved Rain Gauges](https://www.cocorahs.org/Content.aspx?page=approved_rain_gauges); [Rain Gauge Suppliers](https://www.cocorahs.org/Content.aspx?page=Store); [Why manual gauges](https://media.cocorahs.org/docs/WhyManualGauge.pdf); [Training Slide Shows](https://www.cocorahs.org/Content.aspx?page=training_slideshows); [Training slide show v9.2B](https://media.cocorahs.org/docs/CoCoTrainingSlideshow_v9.2B.pdf); [Snow](https://www.cocorahs.org/Content.aspx?page=Snow); [Data-entry FAQ](https://www.cocorahs.org/Content.aspx?page=faqdataentry); [Local Coordinator description, 2006](https://media.cocorahs.org/docs/CoCoRaHs_LocalCoordinatorDescription2006.pdf); [Data Usage Policy](https://www.cocorahs.org/Content.aspx?page=datausagepolicy); [Export Manager](https://data.cocorahs.org/cocorahs/export/exportmanager.aspx).
- NCEI/NOAA: [GHCN-Daily record C00861](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html); [NCEI and CoCoRaHS Data, 2022](https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf); [NOAA DIF record](https://paleo.ltrr.arizona.edu/dc/noaa-other-1002736.xml).
- Other: [WERA1012 minutes 2020–2022](https://nimss.org/storage/3841/WERA1012_Summary_of_Meeting_Minutes_2020-2022.pdf); [Doesken, AMS paper](https://ams.confex.com/ams/pdfpapers/91615.pdf); [AMS 2011 abstract](https://ams.confex.com/ams/19Applied/webprogram/Paper190535.html) (abstract only); [AMS 2010 abstract](https://ams.confex.com/ams/90annual/webprogram/Paper162256.html) (abstract only); [USGS OFR 2018-1061](https://pubs.usgs.gov/of/2018/1061/ofr20181061.pdf); [DataCite search](https://api.datacite.org/dois?query=CoCoRaHS); [GitHub sjwoodr/CoCoRaHS](https://github.com/sjwoodr/CoCoRaHS); [CUAHSI WaterOneFlow](https://hydroportal.cuahsi.org/CocoRaHs/cuahsi_1_1.asmx); [App Store listing](https://apps.apple.com/us/app/cocorahs/id6475901195) (snippet only).

Saved in [web_search_results/2026-11-25_cocorahs-qc-formats-pt2/](./): this answer, the research record, `method.md`, `check-by-hand.md` and `sites-to-trust.md`.
