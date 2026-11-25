# Dataset metadata template

## Ask ChatGPT for the following

Dataset name: GHCN-D (Global Historical Climatology Network Daily)

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

# Global Historical Climatology Network – Daily (GHCN-D)

The Global Historical Climatology Network Daily (GHCN-Daily or GHCNd) is a NOAA-maintained global collection of historical and near-real-time daily weather observations from land-based meteorological stations. It integrates observations from approximately 30 source networks and applies standardized quality-control procedures.

Below are the dataset characteristics, based primarily on NOAA's National Centers for Environmental Information (NCEI) documentation.

## 1. Dataset identification and access

| Requested information | Verified value |
| --- | --- |
| Dataset name | Global Historical Climatology Network – Daily (GHCN-Daily) |
| Abbreviation | GHCN-D or GHCNd |
| Version | Version 3 |
| Dataset DOI | 10.7289/V5D21VHZ |
| DOI link | [https://doi.org/10.7289/V5D21VHZ](<https://doi.org/10.7289/V5D21VHZ>) |
| Data provider | NOAA |
| Data curator / archive manager | NOAA National Centers for Environmental Information (NCEI) |
| Dataset contact | GHCNd Operations Team |
| Contact email | ncdc.ghcnd@noaa.gov |

Official dataset citation:

Menne, M. J., Durre, I., Korzeniewski, B., McNeill, S., Thomas, K., Yin, X., Anthony, S., Ray, R., Vose, R. S., Gleason, B. E., and Houston, T. G. (2012). Global Historical Climatology Network – Daily (GHCN-Daily), Version 3. NOAA National Climatic Data Center. DOI: 10.7289/V5D21VHZ.

Source: NOAA's official dataset metadata.

NCEI



## 2. Data archives and storage locations

The dataset is maintained by NOAA/NCEI and is distributed through multiple access and cloud-storage platforms.

| Archive / repository | Description |
| --- | --- |
| NOAA NCEI | Primary authoritative archive and data curator |
| Amazon Web Services (AWS) | NOAA Open Data Dissemination (NODD) cloud-hosted copy |
| Google Cloud Platform (GCP) | Cloud-hosted access to GHCN-Daily |
| NOAA Climate Data Online (CDO) | Search and retrieval interface for station observations |

The primary authoritative archive is NOAA NCEI. AWS and Google Cloud provide additional distribution mechanisms.

NCEI



## 3. URLs and data access endpoints

These are the principal endpoints for accessing GHCN-Daily data and its documentation.

| Resource title | URL |
| --- | --- |
| NOAA GHCN-Daily official project page | [https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily](<https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily>) |
| NOAA NCEI dataset DOI / landing page | [https://doi.org/10.7289/V5D21VHZ](<https://doi.org/10.7289/V5D21VHZ>) |
| NOAA direct data download directory | [https://www.ncei.noaa.gov/pub/data/ghcn/daily/](<https://www.ncei.noaa.gov/pub/data/ghcn/daily/>) |
| GHCN-Daily README and data-format documentation | [https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt](<https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt>) |
| GHCN-Daily station metadata | [https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt](<https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt>) |
| GHCN-Daily station inventory | [https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt](<https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt>) |
| NOAA Daily Summaries data access | [https://www.ncei.noaa.gov/access/search/data-search/daily-summaries/](<https://www.ncei.noaa.gov/access/search/data-search/daily-summaries/>) |
| AWS Open Data Registry | [https://registry.opendata.aws/noaa-ghcn/](<https://registry.opendata.aws/noaa-ghcn/>) |
| AWS S3 bucket | [https://noaa-ghcn-pds.s3.amazonaws.com/](<https://noaa-ghcn-pds.s3.amazonaws.com/>) |

AWS storage details:

- S3 bucket: `noaa-ghcn-pds`
- AWS region: `us-east-1`
- Update frequency: Daily
- Access: Public; AWS account not required for anonymous access.

The AWS registry documents the bucket and its public access instructions. NOAA also identifies Google Cloud as an additional distribution option.

Registry of Open Data on AWS



## 4. Project leader or dataset curator

There are two relevant roles to distinguish:

- Dataset curator / operational manager: NOAA National Centers for Environmental Information (NCEI), specifically the GHCNd Operations Team.
- Principal scientific developer / lead author: Matthew J. Menne, who is the lead author of the 2012 GHCN-Daily database overview paper.

The official dataset contact is:

- Organization: NOAA/NESDIS/NCEI
- Team: GHCNd Operations Team
- Email: ncdc.ghcnd@noaa.gov

The NOAA metadata does not identify a single current individual as project leader, so the Operations Team is the most appropriate current curator designation.

NCEI



## 5. Precipitation instruments used for measurements

Primary instrument category: Rain gauges (precipitation gauges).

NOAA metadata explicitly identifies rain gauges as an acquisition instrument for the dataset.

However, GHCN-Daily is a compilation of measurements from numerous national and international observing networks. Therefore, it does not use one standardized precipitation instrument across all stations.

Depending on the contributing station network, measurements may originate from:

- Conventional/manual rain gauges.
- Standard meteorological precipitation gauges.
- Automated precipitation-measuring systems.
- Other nationally operated precipitation-observation instruments.

An important consideration is that GHCN-Daily integrates historical measurements from different instruments and observing practices. NOAA notes that the dataset has not been homogenized to correct all biases associated with historical changes in instrumentation and observation practices.

Recommended dataset characterization: Ground-based rain gauges and other station-based precipitation measurement systems.

For instrument-level information, individual station source networks and historical station metadata should be consulted rather than assuming one gauge type applies globally.

NCEI



## 6. Temporal characteristics

| Characteristic | Value |
| --- | --- |
| Temporal start date (official metadata) | January 1, 1880 |
| Earliest observation found in the archive | January 1, 1832 |
| Temporal end date | Present / continuously updated |
| Temporal frequency | Daily |
| Update frequency | Daily, with periodic full-dataset reconstruction |
| Record length | Less than 1 year to more than 175 years, depending on station |

Important distinction: NOAA's official Version 3 metadata specifies a temporal extent beginning January 1, 1880. However, the current NCEI project documentation identifies a precipitation observation from January 1, 1832, at Parramatta, Australia.

For a dataset inventory, I recommend reporting:

1880–Present (official metadata), with historical observations extending back to 1832.

The daily observations are not necessarily measured over identical 24-hour periods at every station. Observation times and reporting conventions can differ between contributing networks.

Daily (GHCN-Daily), Version 3



## 7. Spatial characteristics

| Characteristic | Value |
| --- | --- |
| Spatial coverage | Global land areas |
| Countries and territories | Approximately 180 |
| Number of stations | More than 100,000 |
| Spatial extent – longitude | 180° W to 180° E |
| Spatial extent – latitude | 90° S to 83° N |
| Spatial resolution | Station-based observations; variable and irregular |
| Spatial data format | Geographic coordinates (latitude and longitude) |

Spatial resolution clarification:

GHCN-Daily does not have a fixed spatial resolution such as 1 km, 5 km, 0.25°, or 1°.

Instead, it consists of individual meteorological station observations. Each station has its own geographic coordinates.

Consequently:

- Station density varies geographically.
- North America, Europe, and parts of Australia have relatively dense station coverage.
- Africa, Antarctica, and parts of South America have comparatively sparse coverage.
- Spatial resolution depends on the distribution and density of reporting stations.

For precipitation applications, this distinction is particularly important because the dataset contains point-based precipitation measurements rather than spatially interpolated or gridded precipitation estimates.

Daily (GHCN-Daily), Version 3



## 8. Legacy dataset or ongoing?

Ongoing datasetGHCN-Daily is an ongoing, actively maintained dataset rather than a discontinued legacy dataset.

NOAA/NCEI:

- Receives daily observations from multiple national and international data sources.
- Updates station records as new observations become available.
- Performs quality-control checks.
- Reconstructs the complete dataset periodically, generally each weekend.
- Archives successive daily updates with unique version numbers.

Although it contains historical observations extending back to the nineteenth century, its operational status is ongoing.

NCEI



## 9. Consolidated dataset inventory

For convenient inclusion in a research report, dataset catalog, or comparison spreadsheet, here is the complete summary.

| Parameter | GHCN-Daily value |
| --- | --- |
| Dataset name | Global Historical Climatology Network – Daily |
| Abbreviation | GHCN-D / GHCNd |
| DOI | 10.7289/V5D21VHZ |
| Data archive | NOAA NCEI |
| Additional repositories | AWS S3 and Google Cloud |
| Project curator | NOAA/NCEI GHCNd Operations Team |
| Scientific lead author | Matthew J. Menne |
| Precipitation instruments | Rain gauges and other station-based precipitation measurement systems |
| Temporal start | 1880 (official metadata); earliest observation 1832 |
| Temporal end | Present |
| Temporal frequency | Daily |
| Spatial coverage | Global land areas |
| Geographic extent | 90° S–83° N; 180° W–180° E |
| Station count | More than 100,000 |
| Spatial resolution | Irregular station-based point observations; no fixed grid resolution |
| Dataset status | Ongoing / actively updated |

## 10. Key references

These are the most useful primary references for independently verifying the inventory.

1. NOAA NCEI – Official GHCN-Daily project page

[Global Historical Climatology Network Daily (GHCNd)](<https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily>).

2. NOAA – Official Version 3 metadata and DOI

[GHCN-Daily Version 3 metadata](<https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc%3AC00861/html>).

3. NOAA – Dataset access and search portal

[Daily Summaries data access](<https://www.ncei.noaa.gov/access/search/data-search/daily-summaries/>).

4. AWS – NOAA GHCN-Daily Open Data Registry

[AWS GHCN-Daily repository](<https://registry.opendata.aws/noaa-ghcn/>).

5. Scientific reference paper

Menne et al. (2012), An Overview of the Global Historical Climatology Network-Daily Database, Journal of Atmospheric and Oceanic Technology, 29, 897–910.

DOI: [https://doi.org/10.1175/JTECH-D-11-00103.1](<https://doi.org/10.1175/JTECH-D-11-00103.1>)

Research note: If you are comparing GHCN-Daily with other precipitation datasets, I would classify it as a global, ground-based, daily, station-observation dataset, rather than a gridded precipitation dataset.
