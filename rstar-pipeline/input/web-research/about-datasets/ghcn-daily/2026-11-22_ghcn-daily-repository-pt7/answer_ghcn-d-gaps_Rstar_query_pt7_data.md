# GHCN-Daily: storage, backup, serving and the security of the systems behind it (Jan 2025 – Nov 2026)

GHCN-Daily sits inside NCEI's general archive. That archive keeps a primary and a backup copy, and since May 2026 it has been moving, by lift and shift, from NCEI's Asheville and Boulder servers to Amazon Web Services, finishing by spring 2027. Contractors are doing the move. The cloud platform it is moving onto failed key security and resilience tests in a 2024 inspector-general audit, and some of that audit's recommendations were still open in September 2025. Access is free and still works, but it is degraded by the migration now (an alert running Nov 16–30, 2026), and the cloud copies rest on 2019 contracts of about ten years that can lapse. Nothing published retires a GHCN-Daily route, puts a fee on it or changes its formats. No NOAA document says where GHCN-Daily's own copies are held or who will run its processing on AWS. **Overall confidence: moderate.**

## Findings, threats and the D-ratings

Threat: **imminent** = enacted, ordered or happening; **emerging** = proposed or reported, not in effect; **none found**. Each entry says which D-statement the finding supports or contradicts: D-2 storage at end of life or a single point of failure; D-3 access fragile or unfunded; D-4 formats obsolete or proprietary; D-5 political suppression or alteration.

| # | Finding | Bears on | Threat |
|---|---|---|---|
| 1 | Archive keeps a primary and a "secure" copy; GHCN-Daily's own sites not stated | contradicts D-2 in part (a second copy exists); D-2 unknown for GHCN-Daily | none found |
| 2 | Whole archive moving to AWS by spring 2027; on-premises IT to be decommissioned | supports D-2 (old hardware wears out) during the move; D-3 during cutover | imminent (under way) |
| 3 | OIG-24-034-A: the NCCF (the target platform) is in one region and on a moderate-impact platform; testers got full admin control | supports D-2 (single region), and a security weakness | imminent (findings stand; 3 of 11 recommendations open Sept 2025) |
| 4 | Migration run by contractors (AWS, Alpha Omega, GAMA-1) | supports D-3 (depends on contracts) | emerging |
| 5 | High-severity "Data Access Delays" alert, Nov 16–30, 2026 | supports D-3 | imminent |
| 6 | Oct 2025 shutdown: "site will not be updated"; pages still served | supports D-3 mildly | past (alert from Oct 1, 2025) |
| 7 | Fee schedule of May 14, 2026 covers only special-access items | contradicts D-3 for online GHCN-Daily | none found |
| 8 | NODD cloud copies on 2019 contracts of about ten years, with options; no end date published | supports D-3 (contract dependence) | emerging |
| 9 | NODD funding: FY2022 request +$3.3M; no enacted amount found | supports D-3 (unfunded line) | emerging |
| 10 | No CPO COM support for GHCN-Daily production found after 2021 | supports D-3 weakly | none found |
| 11 | Parquet and BigQuery copies are open formats but have no published schema or units | contradicts D-4 (open formats); a documentation gap | none found |
| 12 | Access Data Service NetCDF: offered, but returned an empty file; CF names untested | D-4 unknown | none found |
| 13 | None of the decommissioned products is a GHCN-Daily route or tool | contradicts D-5 for GHCN-Daily | none found for GHCN-Daily |

## Storage and backup (D-2)

- **Two copies.** NCEI says "The NCEI archive and backup copy contains more than 60 petabytes of data" ([NCEI About Us](https://www.ncei.noaa.gov/about-us)). In 2020 it said records were kept on tape in two copies, "one is stored onsite at NCEI in Asheville, North Carolina, while another—known as the secure copy—is stored offsite" ([NCEI, COSMIC-2 news](https://www.ncei.noaa.gov/news/ncei-archives-cosmic-2-data)). The offsite site is not named. Hurricane Helene hit the Asheville headquarters on September 27, 2024. By December 11, archival ingest was fully restored and "92% of the ingest backlog was recovered", and "Data loss was mitigated with support from NCEI's Boulder, CO location" ([NCEI FY2025 Q1 State of the Service](https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf)). **Whether GHCN-Daily itself is held at both Asheville and Boulder is not published.** Moderate.
- **The move to AWS.** NESDIS is "migrating all of its data, products, and services to the cloud through Spring 2027". Servers "in Asheville, North Carolina and Boulder, Colorado" are moving "in waves" to AWS by "lift and shift", then into the NESDIS Common Cloud Framework (NCCF) ([NCEI, Cloud Migration, May 12, 2026, updated Sep 3, 2026](https://www.ncei.noaa.gov/news/cloud-migration)). NOAA's FY2026 justification plans to "Decommission on premises information technology infrastructure" as capabilities move ([NOAA FY26 CJ](https://www.noaa.gov/sites/default/files/2025-06/NOAA%20FY26%20Congressional%20Justification.pdf)). Bulk folders move from web folders to Amazon S3; formats "will not change", with Zarr, Parquet and GeoJSON added ([NCEI Cloud Migration FAQ](https://www.ncei.noaa.gov/news/cloud-migration-FAQ)). No source says whether a tape or on-premises copy is kept after the move, which regions are used, or whether GHCN-Daily's processing moves. High on the plan; the GHCN-Daily specifics are not found.
- **Who runs it.** AWS holds delivery order 1305M426F0030, "IT Modernization Support for NESDIS and NOAA NCEI", up to $7,332,139 (ceiling), Apr 2026 – Feb 2027 ([HigherGov copy](https://www.highergov.com/contract/47QTCA19D000C-1305M426F0030/)). Alpha Omega Integration holds a sole-source bridge to run and migrate NOAA5009, "the NCEI Archive" LAN; its earlier contract was $19,720,355 for 07/13/20–05/31/26 ([HigherGov](https://www.highergov.com/contract-opportunity/information-technology-support-services-itss-bri-1332kp26f0037-u-93d9b/); [Govly](https://app.govly.com/public/opportunities/16585624)). The two aggregators disagree on the bridge's start date (Dec 1, 2025 or Jun 1, 2026). A search snippet gives the bridge award as May 2026, "worth up to $3,962,751", with 1 bidder; the page was not read. The NCCF's acting program manager leads "a large, multi contractor team", with AWS Professional Services and GAMA-1 ([AWS Public Sector Blog, Jun 2, 2025](https://aws.amazon.com/blogs/publicsector/aws-professional-services-collaborates-with-noaa-and-gama-1-technologies-to-expand-nesdis-common-cloud-framework-capabilities/)). Moderate: the contract figures come from aggregator copies read through WebFetch.
- **Audits.** [OIG-24-034-A](https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf) (Aug 27, 2024) found:
  - the NCCF "lacks fundamental project management";
  - testers could "gain full administrative control of the system using only basic cyberattacks", finding 11 "critical" and 2 "high" issues;
  - the platform lacked over 100 high-baseline controls;
  - the NCCF is "hosted in one region of the country", although its maximum tolerable downtime is "only a few hours" and the cloud provider itself recommends a multi-region design for such systems.

  NOAA answered that the NCCF "provides equivalent protection" to the NIST high baseline, and said it would review a multi-region option. OIG's [September 2025 semiannual report](https://www.oig.doc.gov/wp-content/OIGPublications/SAR-2025-09.pdf) still lists recommendations 3, 9 and 10 as open. The [March 2026 report](https://www.oig.doc.gov/wp-content/OIGPublications/SAR-2026-03.pdf) no longer lists the audit and gives no reason. The FY2025 FISMA audit (OIG-25-028-A) is "Not Public". No 2025–2026 GAO report on NOAA's cloud systems was found ([GAO-26-108443](https://files.gao.gov/reports/GAO-26-108443/index.html) covers other agencies). High on the findings; whether they have been closed is unknown.

## Access (D-3)

- **Status now.** NCEI's alert "Data Access Delays" (Nov 16–30, 2026, severity-high) says "Many access portals, interactive maps, and data folders are currently unavailable due to the migration" ([NCEI Alerts](https://www.ncei.noaa.gov/alerts)). No alert names GHCN-Daily, Climate Data Online (CDO) or the Access Data Service. On Nov 22, 2026 the [GHCNd product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) listed HTTPS and CDO, and the [CDO home](https://www.ncei.noaa.gov/cdo-web/) was served. The [CDO v2 API documentation](https://www.ncei.noaa.gov/cdo-web/webservices/v2) is live with no retirement notice. High.
- **Outages since Jan 2025.** During the shutdown that began Oct 1, 2025, NCEI's alert said "This site will not be updated". The alert ran from 10/01/2025 to 02/01/2026; that end date is probably when the alert stopped showing, not when the shutdown ended, which the saved files don't give. An undated NCEI page (probably 2025) says an OS upgrade "beginning August 22" cut access to many datasets for weeks and that ISD, LCDv1 and GSOD reached end of life on August 29; GHCN-Daily is not on its affected list. Wayback copies show the NCEI and CDO home pages still served on Oct 14–20 ([Alerts, Oct 14, 2025 copy](https://www.ncei.noaa.gov/alerts); [NCEI home, Oct 20, 2025 copy](https://www.ncei.noaa.gov/)). News reports of a redirect to governmentshutdown.noaa.gov could not be read. Search summaries suggest they describe the 2018–19 shutdown, not 2025 (snippet only). An undated NCEI notice reports "network issues affecting access to some access systems" ([NCEI node 1930](https://www.ncei.noaa.gov/node/1930)). No dated outage notice names CDO, the Access Data Service or GHCN-Daily. Moderate.
- **Fees.** The rule effective May 14, 2026 sets fees "for special access to NOAA data": certifications ($170 Department of Commerce, $148 general), paper, offline copies and order handling. NOAA otherwise provides data "without any fee in most instances", including through NODD ([91 FR 19078](https://www.govinfo.gov/content/pkg/FR-2026-04-14/pdf/2026-07250.pdf)). The rule does not name GHCN-Daily. It touches GHCN-Daily only through CDO's paid certified copies ("requires payment"). High.
- **NODD agreements.** They began as CRADAs in 2015 ([NOAA, Evolution of NODD](https://www.noaa.gov/nodd/about)). In 2019 they became "separate multiyear contracts with AWS, Google Cloud, and Microsoft"; providers may charge for compute but must give free access to the data ([NOAA, Dec 19, 2019](https://www.noaa.gov/media-release/cloud-platforms-unleash-full-potential-of-noaa-s-environmental-data)). NOAA's FAQ calls them "signed ten year contracts" ([NODD FAQ](https://www.noaa.gov/big-data-project-frequently-asked-questions)). Google's has "the potential to span 10 years" ([NOAA/Google, 2021](https://www.noaa.gov/information-technology/stories/noaa-and-google-cloud-data-match-made-in-cloud)). The FY2022 justification describes option periods and dates the signing differently: "NOAA signed contracts with three Cloud Service Providers in late FY20", moving off the CRADAs "in Jan of 2020" ([NOAA FY22 CJ](https://www.noaa.gov/sites/default/files/2021-06/NOAA%20FY22%20CJ.pdf)). The 2019 release and the FY22 justification thus put the start in late 2019 and in FY2020; this answer takes late 2019 to early 2020 as the start. No end date or termination clause is published. Hosting can lapse if NOAA stops exercising options, which would be around 2029 at the latest under a ten-year term (an inference). Moderate.
- **Staff and funding of CDO and the Access Data Service:** not published.

## Schemas (D-4)

- **AWS Parquet.** NOAA's readme says the files are "partitioned using Hive patterning either by station or by year and by GHCNd Element", as snappy Parquet ([NODD GHCN-D readme](https://github.com/NOAA-Big-Data-Program/nodd-data-docs/blob/main/GHCN-D/Readme.md)). The 2025 partitions were rewritten on 2026-11-18 ([S3 listing](https://noaa-ghcn-pds.s3.amazonaws.com/?list-type=2&prefix=parquet/by_year/YEAR=2025/&max-keys=30)). NOAA publishes no column types or units for the Parquet files. A third-party footer read gives "ID BYTE_ARRAY, DATE BYTE_ARRAY, DATA_VALUE INT64, M_FLAG, Q_FLAG, S_FLAG, OBS_TIME" ([Scigantic card](https://github.com/Scigantic/scigantic-cards)). The CSV documentation gives the raw units: PRCP in tenths of mm, TMAX/TMIN in tenths of °C ([AWS open-data-docs](https://github.com/awslabs/open-data-docs/tree/main/docs/noaa/noaa-ghcn)). That the Parquet keeps these raw units is likely but not stated. Moderate.
- **BigQuery.** `bigquery-public-data.ghcn_d` holds `ghcnd_stations` and one table per year, `ghcnd_YYYY` ([Google Cloud blog](https://cloud.google.com/blog/products/gcp/global-historical-daily-weather-data-now-available-in-bigquery)). Example queries use id, date, element, value and qflag, and divide value by 10 for mm ([tutorial](https://github.com/acadali/Using-BigQuery-to-do-Analysis)). Google's column types were not read. Moderate.
- **Access Data Service.** It can return NetCDF "Depending on the dataset" ([NCEI ADS docs](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation)). A daily-summaries JSON test gave values as strings with no units or attributes ([test request](https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00013874&startDate=2025-01-01&endDate=2025-01-03&format=json&units=metric)). The NetCDF request returned an empty file, so **whether it uses CF standard names is untested.**

All routes use open formats (text, CSV, Parquet, NetCDF), so D-4 is not supported. The gap is missing schema documentation, not obsolete formats.

## Smaller funding routes (D-3)

- **CPO Climate Observations and Monitoring (COM).** The last statement found calling GHCN-D "COM funded" is from 2019 ([CPO, Nov 9, 2019](https://cpo.noaa.gov/National-Centers-for-Environmental-Information-and-CPO-lay-groundwork-for-new-extreme-heat-product/)). COM's funded-projects list, sorted newest first, starts at 2021 ([CPO COM projects](https://cpo.noaa.gov/divisions-programs/earth-system-science-and-modeling-division/climate-observations-and-monitoring/funded-projects/?_funded_projects_sort=year_funded)). COM's FY23 precipitation awards ($1.2M for seven projects) include a Cornell study that *uses* GHCNd, not one that produces it ([CPO FY23 awards](https://cpo.noaa.gov/noaa-climate-program-offices-climate-observations-and-monitoring-program-awards-1-2-million-for-new-precipitation-data-development-and-analysis/)). No COM support for GHCN-Daily production was found after 2021. Low: this rests on the absence of evidence, and the 2024 COM brochure could not be read.
- **NODD's own funding.** The FY2022 request asked for "+$3,300, 3 FTE/4 Positions" (thousands of dollars) to make NODD an enterprise service, and warned that without the funding, cloud providers ("CSPs") "are less likely to renew the contracts" ([NOAA FY22 CJ](https://www.noaa.gov/sites/default/files/2021-06/NOAA%20FY22%20CJ.pdf)). No enacted amount was found, and the FY2026 and FY2027 justifications don't mention NODD. NOAA describes the partnerships as "no net cost to the taxpayer" ([NOAA OCIO, NODD](https://www.noaa.gov/information-technology/open-data-dissemination)). Moderate.

## Decommissioning (D-5)

- The Senate report says NOAA "decommissioned at least 20 datasets, products and catalogs", directs NOAA to restart them and to report "not later than 90 days after enactment", but names none ([S. Rept. 119-44](https://www.congress.gov/committee-report/119th-congress/senate-report/44/1)). No NOAA report back was found.
- NESDIS's 2025–2026 notices list the NCEI retirements ([Notice of Changes](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes); [2025 list](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes/2025-notice-of-changes)):
  - coastal, marine and geophysical tools, among them the Coastline Extractor viewer, the Marine Buoy Database and IMLGS;
  - Billion Dollar Disasters and ISCCP H (May 8, 2025);
  - CoRTAD, AVHRR Pathfinder and WOCE;
  - the nClimGrid-Daily FTP point (notice Apr 28, 2025, retired June 30, 2025; its HTTPS and NODD copies kept) ([notice](https://www.nesdis.noaa.gov/news/nclimgrid-daily));
  - ISD's FTP/HTTPS service (notice Jun 23, 2026; NODD only, with ISD superseded since 08/24/2025).

  **None is a GHCN-Daily route or tool.** Eos counted 14 slated in April plus 6 slated and 3 retired in May 2025 ([Eos](https://eos.org/research-and-developments/noaa-datasets-will-soon-disappear)). That makes 23, a sum Eos does not state, against the Senate's "at least 20". Whether these are the same list is unresolved.
- NCEI says "No datasets will be retired as part of the cloud migration" ([FAQ](https://www.ncei.noaa.gov/news/cloud-migration-FAQ)). Moderate: the Senate's list itself is not published.

## Gaps and next steps

- **Where GHCN-Daily's copies are held, whether its processing moves to AWS, and who runs it:** NCEI holds this. Ask ncdc.ghcnd@noaa.gov, or file a FOIA request for the migration wave plan.
- **NODD contract terms and end dates:** NOAA's acquisition office holds them. USAspending or FPDS should show the late-FY2020 awards to Amazon, Google and Microsoft. Federal News Network's 2024 interview (two-year base plus four two-year options) could not be read.
- **Whether OIG-24-034-A's recommendations are closed:** OIG holds this; watch OIG's next semiannual report or ask OIG.
- **The Senate's list of 20:** NOAA's report owed under S. Rept. 119-44 is not published.
- **Official Parquet and BigQuery column schemas, and ADS NetCDF attributes:** the S3 host is refused by this sandbox; read a Parquet footer, the BigQuery schema tab, or retry the NetCDF request.
- **CDO and ADS staff and funding:** not published.
- `check-by-hand.md` lists the pages that couldn't be read; `sites-to-trust.md` lists the hosts the sandbox refused, for you to decide whether to allow.

## Sources

- [NCEI, About Us](https://www.ncei.noaa.gov/about-us)
- [NCEI, NCEI archives COSMIC-2 data, 2020](https://www.ncei.noaa.gov/news/ncei-archives-cosmic-2-data)
- [NCEI, FY2025 Q1 State of the Service, 2025](https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf)
- [NCEI, Cloud Migration Offers Bright Future for NOAA's Data, 2026](https://www.ncei.noaa.gov/news/cloud-migration)
- [NCEI, Cloud Migration FAQ, 2026](https://www.ncei.noaa.gov/news/cloud-migration-FAQ)
- [NCEI, Alerts (live and Wayback copies), 2025–2026](https://www.ncei.noaa.gov/alerts)
- [NCEI, home page (Wayback copy, Oct 20, 2025)](https://www.ncei.noaa.gov/)
- [NCEI, alert node 1930 (undated)](https://www.ncei.noaa.gov/node/1930)
- [NCEI, GHCNd product page, read 2026](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)
- [NCEI, Climate Data Online home, read 2026](https://www.ncei.noaa.gov/cdo-web/)
- [NCEI, CDO Web Services v2 documentation, 2026](https://www.ncei.noaa.gov/cdo-web/webservices/v2)
- [NCEI, Access Data Service documentation](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation)
- [NCEI, Access Data Service test request, 2026](https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00013874&startDate=2025-01-01&endDate=2025-01-03&format=json&units=metric)
- [NOAA, FY2026 Congressional Justification, 2025](https://www.noaa.gov/sites/default/files/2025-06/NOAA%20FY26%20Congressional%20Justification.pdf)
- [NOAA, FY2022 Congressional Justification, 2021](https://www.noaa.gov/sites/default/files/2021-06/NOAA%20FY22%20CJ.pdf)
- [NOAA, Evolution of the NODD Program](https://www.noaa.gov/nodd/about)
- [NOAA, NODD Frequently Asked Questions](https://www.noaa.gov/big-data-project-frequently-asked-questions)
- [NOAA OCIO, Open Data Dissemination, 2025](https://www.noaa.gov/information-technology/open-data-dissemination) (read via WebFetch extract)
- [NOAA, Cloud platforms unleash full potential of NOAA's environmental data, 2019](https://www.noaa.gov/media-release/cloud-platforms-unleash-full-potential-of-noaa-s-environmental-data)
- [NOAA, NOAA and Google Cloud: a data match made in the cloud, 2021](https://www.noaa.gov/information-technology/stories/noaa-and-google-cloud-data-match-made-in-cloud)
- [NOAA NODD, GHCN-D readme](https://github.com/NOAA-Big-Data-Program/nodd-data-docs/blob/main/GHCN-D/Readme.md)
- [NESDIS, Notice of Changes, 2025–2026](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes)
- [NESDIS, 2025 Notice of Changes](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes/2025-notice-of-changes)
- [NESDIS, nClimGrid-Daily notice, 2025](https://www.nesdis.noaa.gov/news/nclimgrid-daily)
- [NOAA NESDIS, Schedule of Fees final rule, 91 FR 19078, 2026](https://www.govinfo.gov/content/pkg/FR-2026-04-14/pdf/2026-07250.pdf)
- [CPO, NCEI and CPO lay groundwork for new extreme heat product, 2019](https://cpo.noaa.gov/National-Centers-for-Environmental-Information-and-CPO-lay-groundwork-for-new-extreme-heat-product/)
- [CPO, COM Funded Projects](https://cpo.noaa.gov/divisions-programs/earth-system-science-and-modeling-division/climate-observations-and-monitoring/funded-projects/?_funded_projects_sort=year_funded)
- [CPO, COM awards $1.2 million for precipitation data, 2023](https://cpo.noaa.gov/noaa-climate-program-offices-climate-observations-and-monitoring-program-awards-1-2-million-for-new-precipitation-data-development-and-analysis/)
- [Commerce OIG, OIG-24-034-A, Audit of NESDIS' Transition of Ground System Capabilities to its Common Cloud Framework, 2024](https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf)
- [Commerce OIG, Semiannual Report, Sept 2025](https://www.oig.doc.gov/wp-content/OIGPublications/SAR-2025-09.pdf)
- [Commerce OIG, Semiannual Report, Mar 2026](https://www.oig.doc.gov/wp-content/OIGPublications/SAR-2026-03.pdf)
- [GAO, GAO-26-108443, 2026](https://files.gao.gov/reports/GAO-26-108443/index.html)
- [Senate Appropriations, S. Rept. 119-44, 2025](https://www.congress.gov/committee-report/119th-congress/senate-report/44/1)
- [AWS Public Sector Blog, NCCF with GAMA-1, 2025](https://aws.amazon.com/blogs/publicsector/aws-professional-services-collaborates-with-noaa-and-gama-1-technologies-to-expand-nesdis-common-cloud-framework-capabilities/)
- [AWS, noaa-ghcn-pds S3 listing, 2026](https://noaa-ghcn-pds.s3.amazonaws.com/?list-type=2&prefix=parquet/by_year/YEAR=2025/&max-keys=30) (read via WebFetch)
- [AWS open-data-docs, noaa-ghcn](https://github.com/awslabs/open-data-docs/tree/main/docs/noaa/noaa-ghcn)
- [Google Cloud blog, GHCN daily in BigQuery, 2016](https://cloud.google.com/blog/products/gcp/global-historical-daily-weather-data-now-available-in-bigquery)
- [HigherGov, 1305M426F0030, 2026](https://www.highergov.com/contract/47QTCA19D000C-1305M426F0030/) (read via WebFetch extract)
- [HigherGov, ITSS bridge 1332KP26F0037, 2026](https://www.highergov.com/contract-opportunity/information-technology-support-services-itss-bri-1332kp26f0037-u-93d9b/) (read via WebFetch extract)
- [Govly, NCEI bridge contract, 2026](https://app.govly.com/public/opportunities/16585624) (read via WebFetch extract)
- [Scigantic dataset cards](https://github.com/Scigantic/scigantic-cards)
- [Using BigQuery to do Analysis (tutorial)](https://github.com/acadali/Using-BigQuery-to-do-Analysis)
- [Eos, NOAA datasets will soon disappear, 2025](https://eos.org/research-and-developments/noaa-datasets-will-soon-disappear)

Saved in [`web_search_results/2026-11-22_ghcn-daily-repository-pt7/`](./): this answer, `method.md`, `research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
