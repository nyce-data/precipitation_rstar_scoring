# Dataset metadata template

## Ask ChatGPT for the following

Dataset name: USCRN Daily (U.S. Climate Reference Network)

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

# USCRN Daily Dataset – Metadata Summary

The U.S. Climate Reference Network (USCRN) Daily Products dataset is a NOAA climate-observation dataset containing quality-controlled daily measurements from a nationwide network of weather stations. It is maintained as part of NOAA's long-term climate-monitoring program.

The primary data provider is the NOAA National Centers for Environmental Information (NCEI). The USCRN program is managed operationally by NOAA's Atmospheric Turbulence and Diffusion Division (ATDD).

NCEI



## 1. Dataset metadata

| Requested information | Value |
| --- | --- |
| Dataset name | U.S. Climate Reference Network (USCRN) Daily Products |
| Dataset DOI | No separate DOI for the Daily01 product is identified in the NOAA catalog records reviewed. |
| Dataset identifier | `gov.noaa.ncdc:C00466` |
| Data provider | NOAA / National Centers for Environmental Information (NCEI) |
| Project | U.S. Climate Reference Network (USCRN) |
| Data status | Ongoing |
| Update frequency | Daily |

Important DOI distinction: The DOI `10.1175/BAMS-D-12-00170` is associated with a scientific publication describing the USCRN program, not the DOI of the Daily01 dataset itself. It should not be substituted for a dataset DOI.

NCEI



## 2. Data archive(s) and distribution

The primary archive is NOAA NCEI's public data repository.

| Archive / repository | Description |
| --- | --- |
| NOAA NCEI Public FTP/HTTPS | Primary archive for daily USCRN station files |
| NOAA NCEI USCRN Data Portal | Dataset discovery, documentation, observations and visualizations |
| Data.gov | Federal dataset catalog and metadata record; not the primary data archive |

The dataset is distributed as text files, organized by station and year. The archive also provides snapshots and near-real-time updates.

NCEI



## 3. URL endpoints to access the dataset

These are the main access endpoints:

| Title | URL |
| --- | --- |
| USCRN Daily01 Data Archive | [https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/](<https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/>) |
| Daily Products Documentation | [https://www.ncei.noaa.gov/access/crn/products.html](<https://www.ncei.noaa.gov/access/crn/products.html>) |
| USCRN Data Portal | [https://www.ncei.noaa.gov/access/crn/](<https://www.ncei.noaa.gov/access/crn/>) |
| USCRN Measurements and Variables | [https://www.ncei.noaa.gov/access/crn/measurements.html](<https://www.ncei.noaa.gov/access/crn/measurements.html>) |
| USCRN Instruments Documentation | [https://www.ncei.noaa.gov/access/crn/instruments.html](<https://www.ncei.noaa.gov/access/crn/instruments.html>) |
| Data.gov Dataset Catalog | [USCRN Quality Controlled Datasets](<https://catalog.data.gov/dataset/united-states-climate-reference-network-uscrn-quality-controlled-datasets>) |
| Daily Archive FTP Endpoint | ftp://ftp.ncei.noaa.gov/pub/data/uscrn/products/daily01/ |

The Daily01 directory contains year-based subdirectories, including records beginning in 2000, and a snapshots directory for accessing the complete archive.

NCEI



## 4. Project leader or dataset curator

There are two relevant organizational responsibilities:

- Project/program manager: Howard Diamond, PhD, NOAA USCRN Program Manager.
- Station management and operations: Atmospheric Turbulence and Diffusion Division (ATDD), NOAA Air Resources Laboratory.
- Data archive, curation and distribution: NOAA National Centers for Environmental Information (NCEI).

Howard Diamond is the named USCRN Program Manager and the appropriate individual to identify as the project leader/program contact. NCEI is the data curator and archive administrator.

NCEI



## 5. Precipitation instruments used

USCRN uses several precipitation-related instruments.

UCNRS Climate Monitoring Network

1. Geonor T-200B weighing precipitation gauge

Primary instrument- Measures precipitation accumulation.
- Uses three vibrating-wire load-cell sensors.
- Records independent precipitation-depth measurements at 5-minute intervals.
- Includes a wind/snow shield and heater.

Eurelettronica ICAS - Soluzioni per la Meteorologia

2. Vaisala DRD11A Rain Detector

- Detects the presence and intensity of precipitation.
- Provides supporting information for interpreting precipitation gauge measurements.
- Helps distinguish actual precipitation from other gauge-depth changes.

TB3 Syphonic Tipping Bucket Rain Gauge with 0.2 mm Teflon Bucket

3. Hydrological Services TB-3 tipping-bucket rain gauge

- Auxiliary precipitation instrument.
- Installed at most stations for comparison purposes.
- Its measurements are not quality-controlled and are not considered the official USCRN precipitation readings.

Important distinction: The Geonor T-200B is the primary instrument for official precipitation measurements. The rain detector and tipping-bucket gauge provide supporting or comparison measurements.

NCEI



## 6. Temporal period of the dataset record

2000–present- Start date: November 15, 2000 (beginning of the USCRN observational record).
- End date: Ongoing; data are continually updated.
- Daily archive: Annual data directories are available beginning with 2000.
- Temporal coverage varies by station: Individual stations have different installation dates and periods of record.

The daily archive includes records from 2000 onward, although not every station has observations for the entire period.

NCEI



## 7. Temporal frequency

The dataset requested is the Daily01 product, so its primary temporal frequency is daily.

| Frequency | Availability |
| --- | --- |
| 5-minute | Available in separate sub-hourly product |
| Hourly | Available in separate hourly product |
| Daily | This dataset |
| Monthly | Available in separate monthly product |

Daily measurements are calculated from higher-frequency observations. For example, precipitation is measured at 5-minute intervals and processed into daily precipitation values.

The daily dataset includes:

- Daily precipitation.
- Daily maximum, minimum and average air temperature.
- Daily solar radiation.
- Daily relative humidity.
- Daily surface temperature.
- Daily soil moisture and soil temperature.

NCEI



## 8. Spatial coverage

Geographic coverage: United States of America.

The USCRN network covers:

- Contiguous United States (CONUS).
- Alaska.
- Hawaii.

The observations are collected at individual monitoring stations distributed across representative climate regions.

The approximate spatial bounding coordinates reported in the dataset catalog are:

| Coordinate | Value |
| --- | --- |
| Northern latitude | 72° N |
| Southern latitude | 18° N |
| Western longitude | 172° W |
| Eastern longitude | 65° W |

These are broad catalog bounding coordinates, not a claim that every location within the bounding rectangle contains observations.

NCEI



Map

[ncei.noaa.gov](<https://www.ncei.noaa.gov/access/crn/map.html>)

## 9. Spatial resolution

Spatial resolution: Point-based observations (weather station locations).

- Measurements are collected at individual USCRN monitoring stations.
- Each station has its own geographic coordinates (latitude and longitude).
- The dataset is not a regularly spaced raster or gridded dataset.
- There is no single fixed spatial resolution in kilometers or degrees.

Therefore, the appropriate spatial resolution classification is:

Point observations at individual meteorological stations; spatial spacing varies geographically.

For spatial analysis, the station coordinates should be used rather than assigning the dataset a uniform grid resolution.

Climate Data Store



## 10. Legacy dataset or ongoing?

Ongoing datasetUSCRN Daily is an ongoing observational dataset, not a discontinued legacy dataset.

Evidence:

- NOAA continues to operate and maintain the monitoring stations.
- Daily observations are continually collected and processed.
- The NCEI archive continues to receive updates.
- Historical observations are retained and can be accessed alongside newer records.

The USCRN program is specifically designed to provide long-term, consistent climate observations for monitoring climate variability and change.

NCEI



## 11. Consolidated metadata table

For convenience, here is the information in a compact format suitable for transferring into a dataset inventory or research spreadsheet.

| Metadata field | USCRN Daily value |
| --- | --- |
| Dataset name | USCRN Daily Products |
| DOI | No separate Daily01 dataset DOI identified |
| Dataset identifier | gov.noaa.ncdc:C00466 |
| Archive | NOAA NCEI |
| Access format | Text files |
| Primary access URL | [https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/](<https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/>) |
| Project leader | Howard Diamond, PhD |
| Data curator | NOAA NCEI |
| Station operator | NOAA ATDD / Air Resources Laboratory |
| Precipitation instrument | Geonor T-200B |
| Supporting precipitation instruments | Vaisala DRD11A; Hydrological Services TB-3 |
| Temporal start | November 15, 2000 |
| Temporal end | Present |
| Temporal frequency | Daily |
| Other available frequencies | 5-minute, hourly, monthly |
| Spatial coverage | Contiguous USA, Alaska, Hawaii |
| Spatial resolution | Point-based station observations; variable spacing |
| Dataset status | Ongoing |
| Update frequency | Daily |

## 12. Key references

These are the most useful primary references for documenting the dataset in a research project:

1. NOAA NCEI – USCRN Daily Products: [Daily, hourly, monthly and sub-hourly data access](<https://www.ncei.noaa.gov/access/crn/products.html>).

2. NOAA NCEI – USCRN Dataset Metadata: [Quality Controlled Datasets metadata](<https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00546>).

3. NOAA NCEI – USCRN Measurements: [Measurement methods and precipitation instrumentation](<https://www.ncei.noaa.gov/access/crn/measurements.html>).

4. NOAA NCEI – USCRN Instruments: [Official instrument specifications](<https://www.ncei.noaa.gov/access/crn/instruments.html>).

5. Diamond et al. (2013): U.S. Climate Reference Network after one decade of operations: Status and assessment. Bulletin of the American Meteorological Society. DOI: [10.1175/BAMS-D-12-00170](<https://doi.org/10.1175/BAMS-D-12-00170>).

Research note: If you are compiling this information for a formal dataset inventory, retain the distinction between the dataset DOI and the publication DOI. The publication DOI above is a useful scientific reference, but should not be reported as the dataset DOI.
