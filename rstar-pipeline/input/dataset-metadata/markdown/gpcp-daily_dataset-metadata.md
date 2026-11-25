# Dataset metadata template

## Ask ChatGPT for the following

Dataset name: GPCP Daily (Global Precipitation Climatology Project)

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

# GPCP Daily – Global Precipitation Climatology Project

The GPCP Daily dataset is a globally gridded precipitation product combining satellite observations and surface precipitation measurements.

Important version distinction: GPCP Daily has multiple versions. The original One-Degree Daily product (V1.3) has a 1° × 1° resolution and begins in October 1996. The newer NOAA GPCP Daily V3.3 product has a 0.5° × 0.5° resolution and begins in 1998. The information below prioritizes the latest documented version, V3.3, while identifying the older version where relevant.

NCEI



## 1. Dataset DOI

Current version: V3.3- DOI: [10.25921/9b5m-ka77](<https://doi.org/10.25921/9b5m-ka77>)
- Dataset title: NOAA Climate Data Record (CDR) of the Global Precipitation Climatology Project (GPCP) Daily Version 3.3.
- Publisher: NOAA National Centers for Environmental Information (NCEI).
- Publication date: August 5, 2025.
  NCEI
  +1

For the older V1.3 dataset:

- DOI: [10.7289/V5RX998Z](<https://doi.org/10.7289/V5RX998Z>).

NCEI

## 2. Data archives and repositories

The dataset is archived and distributed through the following sources:

| Archive / repository | Description |
| --- | --- |
| NOAA National Centers for Environmental Information (NCEI) | Primary official archive and distribution center for the NOAA CDR |
| Amazon Web Services (AWS) | Cloud-based access to the GPCP Daily V3.3 files |
| Google Cloud | Cloud-based data access |
| NASA / Goddard Space Flight Center (GSFC) | GPCP project and scientific data distribution |
| World Data Center for Meteorology | Secondary distribution conduit for GPCP data |

NOAA identifies NCEI as the principal archive, with AWS and Google Cloud listed as access options.

NCEI



## 3. Dataset access URLs and endpoints

The following are the principal access points.

| Title | Link | Purpose |
| --- | --- | --- |
| NOAA GPCP Daily CDR landing page | [NCEI – GPCP Daily](<https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily>) | Official dataset information and access |
| NOAA direct data download | [NCEI GPCP Daily archive](<https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/>) | Browse and download archived files |
| Amazon Web Services | [NOAA GPCP Daily AWS bucket](<https://noaa-cdr-precip-gpcp-daily-pds.s3.amazonaws.com/index.html>) | Cloud data access |
| Google Cloud | [Google Cloud GPCP bucket](<https://console.cloud.google.com/storage/browser/noaa-cdr-precip-gpcp-daily>) | Cloud data access |
| NOAA metadata record | [GPCP Daily V3.3 metadata](<https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01726>) | Detailed metadata, coverage and lineage |
| Dataset DOI | [10.25921/9b5m-ka77](<https://doi.org/10.25921/9b5m-ka77>) | Permanent dataset identifier |

Note: The NOAA landing page currently warns of cloud migration-related delays affecting some data access services. The AWS endpoint is an alternative download route.

ncei.noaa.gov



## 4. Project leader or dataset curator

- Principal Investigator (PI): Robert F. Adler.
- Institution: University of Maryland, College Park.
- Data production institution: University of Maryland.
- Project collaborators and scientific contributors: George J. Huffman, Jian-Jian Wang, Mathew Sapiano, Guojun Gu, Ali Behrangi, David Bolvin and Eric Nelkin.
- Data archive and stewardship: NOAA National Centers for Environmental Information (NCEI).

The GPCP Daily V3.3 analysis is computed at the University of Maryland and submitted to NOAA NCEI for archival and distribution.

For dataset contact and inquiries: gpcp\_contacts@noaa.gov.

NCEI



## 5. Precipitation instruments used for measurements

GPCP is a merged satellite-and-gauge precipitation product. It does not rely on a single precipitation instrument.

For the current V3.3 product, the main observational inputs include:

| Instrument / measurement source | Measurement type | Contribution |
| --- | --- | --- |
| Passive Microwave (PMW) satellite sensors | Microwave radiances | Estimates precipitation from microwave observations |
| SSM/I – Special Sensor Microwave/Imager | Passive microwave | Microwave precipitation observations |
| SSMIS – Special Sensor Microwave Imager/Sounder | Passive microwave | Successor to SSM/I observations |
| GPM constellation sensors | Passive microwave and radar-derived precipitation | Satellite precipitation estimates incorporated through IMERG |
| Geostationary infrared (IR) imagers | Infrared brightness temperatures | Identifies cloud characteristics and estimates precipitation |
| GridSat IR | Infrared satellite observations | Extends daily coverage back to January 1998 |
| Rain gauges (GPCC) | In-situ surface precipitation measurements | Provides ground-based precipitation observations for calibration and merging |

Important distinction: Some of these are instrument families or data products rather than individual instruments.

The V3.3 daily product incorporates Integrated Multi-satellitE Retrievals for GPM (IMERG) Version 07B Final Run, infrared GridSat observations, and the GPCP monthly precipitation analysis. Its gauge component uses the Global Precipitation Climatology Centre (GPCC) data.

The earlier V1.3 product specifically used:

- SSM/I and SSMIS microwave radiometers.
- Geostationary and low-Earth-orbit infrared imagers.
- TOVS (TIROS Operational Vertical Sounder).
- AIRS (Atmospheric Infrared Sounder).
- Surface rain-gauge analyses.

NCEI



## 6. Temporal period of the dataset record

For the current V3.3 daily product:

- Start date: January 1998.
- End date: Present (delayed/near-real-time updates).
- Temporal coverage: January 1998–present.

For the older V1.3 daily product:

- Start date: October 1996.
- End date: The historical record extends through the later archived years; V1.3 is superseded.

The newer V3.3 product begins in January 1998, incorporating GridSat infrared observations to extend the daily record earlier than the June 2000 starting point of its predecessor V3.2.

AMS Journals



## 7. Temporal frequency

Daily- Data temporal resolution: Daily precipitation estimates.
- Data update frequency: Monthly.
- Data format: Daily NetCDF4 files.
- Update latency: Delayed processing; data are not necessarily available immediately after observations.

It is important to distinguish the temporal resolution from the archive update frequency: the dataset provides daily precipitation values but is updated approximately monthly.

NCEI



## 8. Spatial coverage

- Coverage: Global.
- Latitude: 90° South to 90° North.
- Longitude: 180° West to 180° East.
- Geographic coverage: Both land and ocean surfaces.

The dataset provides globally complete gridded precipitation estimates.

NCEI



## 9. Spatial resolution

| Dataset version | Spatial resolution |
| --- | --- |
| V3.3 (current) | 0.5° × 0.5° |
| V3.2 | 0.5° × 0.5° |
| V1.3 (legacy) | 1° × 1° |

For V3.3:

- Grid dimensions: 720 × 360.
- Grid spacing: 0.5 degrees latitude and longitude.
- Grid type: Cylindrical Equal Distance.
- Data format: NetCDF4.

Recommended value to report: 0.5° × 0.5°, if you are documenting the latest V3.3 dataset.

NCEI



## 10. Legacy dataset or ongoing?

Ongoing datasetThe GPCP Daily project is ongoing.

- NOAA continues to maintain and distribute the daily precipitation Climate Data Record.
- V3.3 is the latest documented version.
- Data are updated monthly.
- The record extends from January 1998 to the delayed present.
- Earlier V1.3 data are considered superseded by newer versions.

The original V1.3 product is a legacy version, but the overall GPCP Daily dataset is an actively maintained data record.

NCEI



## Consolidated dataset information

The following table provides a concise summary suitable for a dataset inventory, research report, or data catalog.

| Requested information | GPCP Daily V3.3 |
| --- | --- |
| Dataset name | Global Precipitation Climatology Project (GPCP) Daily |
| DOI | 10.25921/9b5m-ka77 |
| Data archive | NOAA NCEI |
| Additional archives | AWS, Google Cloud, NASA/GSFC distribution resources |
| Project leader / PI | Robert F. Adler |
| Institution | University of Maryland |
| Instruments | Passive microwave radiometers, infrared imagers, GPM satellite sensors, radar-derived precipitation inputs, and rain gauges |
| Temporal start | January 1998 |
| Temporal end | Present (delayed) |
| Temporal resolution | Daily |
| Archive update frequency | Monthly |
| Spatial coverage | Global, 90°S–90°N, 180°W–180°E |
| Spatial resolution | 0.5° × 0.5° |
| Grid dimensions | 720 × 360 |
| File format | NetCDF4 |
| Dataset status | Ongoing |
| Current version | V3.3 |

## Primary references

These are the most useful sources to retain as references for your dataset documentation:

1. NOAA NCEI – GPCP Daily CDR: [Official dataset landing page](<https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily>).

2. NOAA – GPCP Daily V3.3 metadata: [Dataset metadata and source information](<https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01726>).

3. NOAA – GPCP Daily V3.3 technical information: [Dataset lineage and source datasets](<https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc%3AC01726/html>).

4. GPCP V3.3 scientific publication: [GPCP Version 3.3: A Refined Global View of Precipitation from Satellite and Gauge Observations](<https://journals.ametsoc.org/view/journals/hydr/aop/JHM-D-26-0048.1/JHM-D-26-0048.1.xml>).

5. NASA – GPCP V1.3 Technical Note: [One-Degree Daily Precipitation Technical Documentation](<https://esgf.nccs.nasa.gov/esgdoc/GPCP_precip_1DD-V1.3_TechNote_180510.pdf>).

