# Dataset metadata template

## Ask ChatGPT for the following

Dataset name: PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks)

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

# PERSIANN-CDR Daily Dataset: Metadata and Data Access

The PERSIANN-CDR (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record) is a NOAA climate data record developed using satellite infrared observations and an artificial neural network to estimate daily precipitation.

The primary authoritative data provider is NOAA's National Centers for Environmental Information (NCEI), with scientific development associated with the Center for Hydrometeorology and Remote Sensing (CHRS) at the University of California, Irvine.

## 1. Dataset metadata

| Metadata field | Value |
| --- | --- |
| Dataset name | PERSIANN-CDR Daily |
| Dataset DOI | [10.7289/V51V5BWQ](<https://doi.org/10.7289/V51V5BWQ>) |
| Dataset version | Version 1, Revision 1 (v01r01) |
| Project leader / Principal Investigator | Soroosh Sorooshian, University of California, Irvine |
| Other principal contributors | Kuolin Hsu, Dan Braithwaite, Hamed Ashouri, and NOAA CDR Program |
| Data provider / steward | NOAA National Centers for Environmental Information (NCEI) |
| Scientific development organization | Center for Hydrometeorology and Remote Sensing (CHRS), University of California, Irvine |
| Data format | NetCDF (.nc) |
| Precipitation measurement units | mm/day |

Source: NOAA NCEI dataset documentation and metadata.

NCEI



## 2. Data archive(s) and repositories

The dataset is distributed through several archives and access platforms.

| Archive / repository | Description |
| --- | --- |
| NOAA NCEI Climate Data Record Archive | Primary authoritative archive and long-term data steward. |
| University of California, Irvine – CHRS | Scientific development and data distribution through the CHRS Data Portal. |
| NOAA THREDDS / ERDDAP | Provides online data access, subsetting, and gridded-data services. |
| Amazon Web Services (AWS) | Cloud-hosted access through the Registry of Open Data. |
| Microsoft Azure | Cloud-hosted data access. |
| Google Earth Engine | Cloud-based access for analysis and processing. |

Sources: NOAA NCEI and its metadata catalog, Google Earth Engine, and UCAR Climate Data Guide.

NCEI



## 3. Dataset URL endpoints (title and link)

These are the principal access points for obtaining or working with the dataset.

| Title | URL |
| --- | --- |
| NOAA NCEI – PERSIANN-CDR Dataset Landing Page | [NOAA Dataset Landing Page](<https://doi.org/10.7289/V51V5BWQ>) |
| NOAA NCEI – PERSIANN-CDR Product Page | [PERSIANN-CDR Product](<https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann>) |
| NOAA NCEI – Direct FTP Download | [PERSIANN-CDR NetCDF Files](<https://data.ncei.noaa.gov/cdr/persiann/files/>) |
| NOAA NCEI – ERDDAP Data Access | [ERDDAP Data Access](<https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.html>) |
| NOAA NCEI – THREDDS Data Service | [NOAA THREDDS Server](<https://www.ncei.noaa.gov/thredds/>) |
| UC Irvine – CHRS Data Portal | [CHRS Data Portal](<https://chrsdata.eng.uci.edu/>) |
| Google Earth Engine – PERSIANN-CDR | [Earth Engine Dataset Catalog](<https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR>) |
| NOAA – PERSIANN-CDR User Guide | [Download User Guide (PDF)](<https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf>) |
| NOAA – Algorithm Description | [Algorithm Description (PDF)](<https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf>) |

Recommended access methods:

- For downloading original daily NetCDF files: NOAA FTP/download archive.
- For selecting particular dates and geographic areas: NOAA ERDDAP.
- For visualization and spatial analysis: CHRS Data Portal.
- For cloud-based processing: Google Earth Engine.

Sources:

NCEI



## 4. Project leader or curator

- Principal Investigator / Project Leader: Professor Soroosh Sorooshian.
- Institution: University of California, Irvine.
- Research and development group: Center for Hydrometeorology and Remote Sensing (CHRS).
- Other major contributors: Kuolin Hsu, Dan Braithwaite, and Hamed Ashouri.
- Data curator and archive steward: NOAA National Centers for Environmental Information (NCEI).

An important distinction: UC Irvine/CHRS developed the scientific product, while NOAA NCEI provides the official climate data record archive and stewardship.

NCEI



## 5. Precipitation instruments used for measurements

PERSIANN-CDR is a satellite-derived precipitation estimation product. It does not directly measure rainfall using a single precipitation gauge or onboard satellite rain sensor.

Its primary input is infrared (IR) satellite imagery.

Primary satellite observing system:

- GridSat-B1 (Gridded Satellite Data from ISCCP B1): The principal satellite input dataset.
- Infrared Window (IRWIN) channel: Approximately 10–12 µm wavelength, particularly the 11 µm brightness-temperature channel.
- Satellite instruments: Infrared imagers aboard geostationary meteorological satellites.

Examples of contributing satellite platforms and instruments include:

| Satellite platform | Instrument |
| --- | --- |
| Meteosat | MVIRI / SEVIRI |
| GOES | GOES Imager |
| Himawari | AHI |
| GMS / MTSAT | VISSR / JAMI |
| Fengyun (FY) | VISSR / related IR imagers |

Additional precipitation datasets used in the algorithm:

1. NCEP Stage IV precipitation estimates: Hourly precipitation data used to train the artificial neural network.
2. GPCP Version 2.2: Monthly precipitation analysis used for bias adjustment and calibration. This incorporates satellite and ground-based precipitation observations, including rain gauges.

The processing chain is:

Geostationary satellite IR observations
GridSat-B1, approximately 3-hourly observations

PERSIANN Artificial Neural Network
Trained using NCEP Stage IV hourly precipitation estimates

GPCP v2.2 bias adjustment
Monthly precipitation calibration at 2.5° resolution

PERSIANN-CDR daily precipitation
0.25° gridded precipitation estimates in mm/day

Important: The primary satellite measurement is infrared brightness temperature, not direct rainfall. Precipitation is estimated through the neural-network algorithm.

ncei.noaa.gov



## 6. Temporal period of the dataset record

- Start date: January 1, 1983.
- End date: Present, subject to processing and availability of upstream satellite inputs.
- Latest indexed data endpoint: July 31, 2026.
- Historical record length: More than 43 years as of November 2026, although the latest months may not yet be processed.

The dataset is updated with a delay, rather than providing real-time precipitation observations.

Data Access Form



## 7. Temporal frequency

Daily- Output temporal resolution: Daily.
- Measurement period represented: Accumulated precipitation over a 24-hour period (00:00–23:59 UTC).
- Original satellite input frequency: Approximately every 3 hours.
- Update frequency: Quarterly, typically with an approximately three-month delay.

The original satellite observations are more frequent, but the distributed PERSIANN-CDR product is daily.

PERSIANN CDR (01B-16) User Guide



## 8. Spatial coverage

Quasi-global coverageThe dataset covers the following geographic area:

| Parameter | Coverage |
| --- | --- |
| Northern latitude | 60° N |
| Southern latitude | 60° S |
| Western longitude | 0° |
| Eastern longitude | 360° |
| Geographic extent | Most of the globe, excluding polar regions |

The dataset does not cover the polar regions beyond 60° N and 60° S.

It includes land and ocean areas within its geographic coverage.

NCEI



## 9. Spatial resolution

- Grid resolution: 0.25° × 0.25°.
- Grid dimensions: 1,440 columns × 480 rows.
- Approximate ground resolution: 27.8 km at the equator.
- Data format: NetCDF.
- Variable: Daily precipitation.
- Units: mm/day.

The actual ground distance represented by a grid cell varies with latitude because longitude spacing decreases toward the poles.

PERSIANN CDR (01B-16) User Guide



## 10. Legacy dataset or ongoing?

Ongoing / Operational Climate Data RecordPERSIANN-CDR is an ongoing climate data record, not simply a discontinued legacy dataset.

Evidence:

- The historical record begins in 1983.
- NOAA continues to maintain the dataset through its Climate Data Record Program.
- New data are processed and released quarterly.
- The record is extended toward the present as upstream satellite observations become available.
- The current product version is v01r01.

Important distinction: Although the dataset is ongoing, it is not real-time. New observations are incorporated with a processing delay, typically around three months.

NCEI



## 11. Consolidated metadata summary

This table can be used directly in a dataset inventory, research proposal, or scientific data catalog.

| Requested information | PERSIANN-CDR value |
| --- | --- |
| Dataset name | PERSIANN-CDR Daily |
| DOI | 10.7289/V51V5BWQ |
| Main archive | NOAA NCEI |
| Additional archives / platforms | UC Irvine CHRS, NOAA THREDDS, ERDDAP, AWS, Azure, Google Earth Engine |
| Project leader | Soroosh Sorooshian |
| Curating organization | NOAA NCEI |
| Satellite instruments | Geostationary satellite infrared imagers (GridSat-B1) |
| Supporting precipitation data | NCEP Stage IV and GPCP v2.2 |
| Temporal start | 1983-01-01 |
| Temporal end | Present (latest indexed endpoint: 2026-07-31) |
| Temporal frequency | Daily |
| Archive update frequency | Quarterly |
| Spatial coverage | 60°S–60°N, 0°–360° longitude |
| Spatial resolution | 0.25° × 0.25° |
| Approximate spatial cell size | 27.8 km at equator |
| Data format | NetCDF |
| Measurement units | mm/day |
| Dataset status | Ongoing / operational CDR |

## 12\. Key references and documentation

For scientific documentation and independent verification, I recommend these five references:

1\. NOAA NCEI – Official dataset landing page: [PERSIANN-CDR DOI](<https://doi.org/10.7289/V51V5BWQ>).

2\. Ashouri et al. (2015) – Original scientific publication: PERSIANN-CDR: Daily Precipitation Climate Data Record from Multi-Satellite Observations for Hydrological and Climate Studies. DOI: [10.1175/BAMS-D-13-00068.1](<https://doi.org/10.1175/BAMS-D-13-00068.1>).

3\. NOAA PERSIANN-CDR User Guide: [Technical User Guide](<https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf>).

4\. UCAR Climate Data Guide: [PERSIANN-CDR Dataset Assessment](<https://climatedataguide.ucar.edu/climate-data/persiann-cdr-precipitation-estimation-remotely-sensed-information-using-artificial>).

5\. NOAA Algorithm Theoretical Basis Document: [Algorithm and Instrument Documentation](<https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf>).

