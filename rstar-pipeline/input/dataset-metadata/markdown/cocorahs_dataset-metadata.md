# Dataset metadata template

## Ask ChatGPT for the following

Dataset name: CoCoRaHS (Community Collaborative Rain, Hail and Snow Network)

For this dataset, what are the values for the following:

What is the dataset DOI?

What is the data archive(s) it is stored in and served from?

What are the url endpoints to get the dataset (title and link)?

Who is the project leader or curator of the dataset?

precipitation instruments used for measurements

What is the temporal period of the dataset record?

What is the temporal frequency: hourly, daily, monthly, etc.?

What is the spatial coverage?

What is the spatial resolution?

Is it a legacy dataset or ongoing?

## ChatGPT answer

# CoCoRaHS dataset – metadata and data characteristics

The Community Collaborative Rain, Hail and Snow Network (CoCoRaHS) is a volunteer-based, citizen-science precipitation observation network established in Colorado in 1998. It collects localized measurements of rainfall, snowfall, snow depth, hail, and other weather-related conditions.

The network is housed at the Colorado Climate Center at Colorado State University. Its observations are used by NOAA, the National Weather Service, researchers, hydrologists, and other organizations.

National Weather Service



## 1. Dataset metadata

| Requested information | Value |
| --- | --- |
| Dataset name | Community Collaborative Rain, Hail and Snow Network (CoCoRaHS) |
| Dataset DOI | No dedicated DOI for the complete CoCoRaHS observational dataset was identified. The dataset is distributed through the CoCoRaHS website and data export system. |
| Data archive(s) | CoCoRaHS central database and data export system; observations are also incorporated into NOAA/NCEI's Global Historical Climatology Network–Daily (GHCN-Daily). |
| Project leader / curator | CoCoRaHS headquarters at the Colorado Climate Center, Colorado State University. |
| Project originator | Nolan Doesken, former Colorado State Climatologist and founder of CoCoRaHS. |
| Dataset status | Ongoing, with observations collected continuously since 1998. |

NOAA Institutional Repository



## 2. Data access URLs and endpoints

The following are the principal access points. The first-party CoCoRaHS endpoints are the recommended sources for retrieving original observations.

| Resource / endpoint title | URL |
| --- | --- |
| CoCoRaHS official website | [https://www.cocorahs.org/](<https://www.cocorahs.org/>) |
| CoCoRaHS Data Reports | [https://www.cocorahs.org/ViewData/](<https://www.cocorahs.org/ViewData/>) |
| CoCoRaHS Data Export Portal | [https://data.cocorahs.org/](<https://data.cocorahs.org/>) |
| CoCoRaHS Export Manager | [https://data.cocorahs.org/cocorahs/Export/ExportManager.aspx](<https://data.cocorahs.org/cocorahs/Export/ExportManager.aspx>) |
| CoCoRaHS Data Explorer (station histories) | [https://dex.cocorahs.org/](<https://dex.cocorahs.org/>) |
| Daily Precipitation CSV Export | [CSV export endpoint](<https://data.cocorahs.org/cocorahs/export/exportreports.aspx?ReportType=Daily&Format=CSV&StartDate=2022-09-14&EndDate=2022-09-14>) |
| NOAA/NCEI Global Historical Climatology Network – Daily | [GHCN-Daily](<https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily>) |
| CoCoRaHS Data Usage Policy | [Data Usage Policy](<https://www.cocorahs.org/content.aspx?page=datausagepolicy>) |

Important CSV export information: The CSV endpoint supports date-range filtering, station filtering, and metric or imperial units. For example, changing `StartDate` and `EndDate` retrieves a different observation period. The `State` and `Station` parameters can also be added to narrow the results.

METplus 13.1.0-beta1-dev documentation



## 3. Precipitation instruments used

CoCoRaHS primarily uses manual precipitation measurement instruments.

Join volunteers working together to measure precipitation - Florida Climate Institute

Standard 4-inch diameter rain gauge

- Clear plastic manual rain gauge.
- Measures liquid precipitation.
- Read manually by volunteers, generally once each morning.
- Rainfall is recorded in inches, commonly to hundredths of an inch.

Winter storm watch issued for northern California - Action News Jax

Snow measurement equipment

- Snowboard or designated snow measurement surface.
- Snow ruler or measuring stick.
- Used to measure new snowfall and total snow depth.
- Snow-water equivalent may also be measured or reported.

Weather Words: Hailpad | Weather Underground

Hail measurement equipment

- Hail pad or hail collection surface may be used.
- Used to document hailstone size, quantity, and characteristics.
- Hail observations are also submitted through the reporting system.

The standard CoCoRaHS precipitation observation is based on a manually read 4-inch rain gauge. It is not an automated weather-station network.

weather.gov



## 4. Temporal characteristics

| Parameter | Value |
| --- | --- |
| Start of record | 1998 |
| End of record | Present (ongoing) |
| Temporal period | 1998–2026 and continuing |
| Primary temporal frequency | Daily |
| Observation interval | Approximately 24 hours |
| Typical observation time | Around 7:00 AM local time |
| Data reporting frequency | Daily, with reports submitted throughout the day |
| Other temporal products | Multiple-day accumulation, intense rainfall, hail, significant weather, and other event-based reports |

The primary dataset consists of daily precipitation observations representing the preceding 24-hour period. Observers generally take measurements around 7:00 AM local time.

Some supplementary observations, such as hail and intense rainfall, are submitted when events occur. These are not necessarily daily measurements.

cocorahs.org



## 5. Spatial characteristics

| Parameter | Value |
| --- | --- |
| Spatial coverage | United States, Canada, Puerto Rico, U.S. Virgin Islands, and other participating locations, including the Bahamas |
| Spatial data type | Point-based ground observations |
| Spatial reference | Individual monitoring station latitude and longitude |
| Spatial resolution | Variable and station-dependent; no fixed grid-cell resolution |
| Station distribution | Irregular, depending on volunteer participation and population density |

Spatial resolution clarification:

CoCoRaHS is a point-observation dataset rather than a gridded precipitation product.

Each observation is associated with a specific volunteer monitoring station, with geographic coordinates. Therefore:

- There is no standard spatial resolution such as 1 km, 4 km, or 0.25 degrees.
- Station spacing varies considerably between rural and urban areas.
- Some locations have multiple stations within a relatively small geographic area.
- The network provides localized precipitation information that can capture differences missed by conventional weather-station networks.

The METplus dataset documentation specifically describes CoCoRaHS as point observations with variable station density.

METplus 13.1.0-beta1-dev documentation



## 6. Legacy or ongoing dataset?

Ongoing datasetCoCoRaHS is an ongoing observational dataset.

- Established: 1998, in Colorado.
- Historical record: 1998–present.
- Current data collection: Continues through volunteer observers.
- Data updates: Daily observations are continually submitted to the central database.
- Historical preservation: Observations are retained and can be accessed through the CoCoRaHS data reporting and export systems.

The observations have also been incorporated into NOAA's GHCN-Daily archive. CoCoRaHS observations have been streamed to NOAA since 1998, subject to station inclusion and quality-control requirements.

media.cocorahs.org



## 7. Consolidated dataset metadata sheet

Here is a summary suitable for transferring into a dataset inventory, research spreadsheet, or data catalog.

| Metadata field | CoCoRaHS value |
| --- | --- |
| Dataset | Community Collaborative Rain, Hail and Snow Network |
| Acronym | CoCoRaHS |
| DOI | No dedicated DOI identified |
| Primary archive | CoCoRaHS central database |
| Secondary archive | NOAA/NCEI GHCN-Daily |
| Project institution | Colorado State University |
| Project center | Colorado Climate Center |
| Founder | Nolan Doesken |
| National coordinator | Henry Reges (listed in CoCoRaHS organizational information) |
| Instruments | Manual 4-inch rain gauge; snow ruler and snowboard; hail observation equipment |
| Start year | 1998 |
| End year | Present |
| Temporal frequency | Daily (primary); event-based supplementary reports |
| Observation interval | Approximately 24 hours |
| Spatial coverage | United States, Canada, Puerto Rico, U.S. Virgin Islands, Bahamas, and other participating locations |
| Spatial resolution | Irregular point-based station observations; no fixed grid resolution |
| Data format | CSV, downloadable reports, and web-based data products |
| Data status | Ongoing |
| Access restrictions | Publicly accessible |
| Data license | Creative Commons Attribution 4.0, unless otherwise noted |

## 8. Key references and documentation

These are particularly useful for validating the metadata and citing the dataset in research.

1. Official CoCoRaHS website: [CoCoRaHS Network](<https://www.cocorahs.org/>).
2. CoCoRaHS data access and reports: [Data Reports](<https://www.cocorahs.org/ViewData/>).
3. CoCoRaHS data usage policy: [Data Usage Policy](<https://www.cocorahs.org/content.aspx?page=datausagepolicy>).
4. METplus dataset documentation: [CoCoRaHS Precipitation Reports](<https://metplus.readthedocs.io/en/develop/Verification_Datasets/datasets/cocorahs.html>). Particularly useful for temporal frequency, spatial coverage, instruments, and data format.
5. NOAA/NCEI quality assurance documentation: [CoCoRaHS Data Quality Assurance and Quality Control](<https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf>).
6. NOAA documentation: [Integration of CoCoRaHS Observations into River Forecasting Operations](<https://repository.library.noaa.gov/view/noaa/62044/noaa_62044_DS1.pdf>).

Two important qualifications for your dataset inventory:

- DOI: Do not assign the GHCN-Daily DOI or another NOAA archive identifier as the DOI of the original CoCoRaHS dataset. These are distinct data products.
- Spatial resolution: Record this as irregular point-based observations (station-level) rather than assigning an artificial kilometer-scale resolution.

The most useful source for a research-grade description is the METplus documentation because it explicitly describes the measurement method, temporal resolution, spatial characteristics, and data retrieval procedure.
