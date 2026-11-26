# Dataset metadata template

## Ask ChatGPT for the following

Dataset name: ASOS (Automated Surface Observing System)

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

# ASOS (Automated Surface Observing System) – Dataset information

The Automated Surface Observing System (ASOS) is a U.S. operational meteorological observation network jointly operated by the National Weather Service (NWS), Federal Aviation Administration (FAA), and Department of Defense (DoD). It provides continuous surface weather observations, including precipitation, temperature, wind, atmospheric pressure, visibility, and cloud conditions.

The principal archive and data distributor is NOAA's National Centers for Environmental Information (NCEI). ASOS is a network rather than one single, fixed-format dataset: its one-minute, five-minute, hourly, and climatological products have different identifiers and periods of record.

NCEI



## 1. Dataset identification and archive

| Requested information | Finding |
| --- | --- |
| Dataset name | Automated Surface Observing System (ASOS) |
| Project operators | NOAA/NWS, FAA, and DoD |
| Primary archive | NOAA National Centers for Environmental Information (NCEI) |
| Main archive database | Global Surface Hourly (GSH) / Integrated Surface Database (ISD) |
| Data status | Ongoing operational dataset |
| Geographic focus | United States and associated territories, with some products incorporating international stations |

NCEI



## 2. DOI

An important distinction: I could not establish a single DOI assigned to the entire operational ASOS network. NOAA distributes ASOS observations through several separately catalogued data products, which have their own dataset identifiers.

For example:

- Five-minute ASOS observations: NCEI DSI 6401\_02.
- One-minute ASOS observations: NCEI DSI 3285.

These identifiers should not be mistaken for DOIs.

NCEI



## 3. Data access URLs and endpoints

The following are the principal official access points. They provide different temporal resolutions and data products.

| Dataset / endpoint title | Link |
| --- | --- |
| NOAA NCEI – ASOS/AWOS overview and access | [NCEI ASOS/AWOS](<https://www.ncei.noaa.gov/products/land-based-station/automated-surface-weather-observing-systems>) |
| Global Hourly – searchable observations | [Global Hourly Data Access](<https://www.ncei.noaa.gov/access/search/data-search/global-hourly/>) |
| Global Hourly – bulk archive | [NOAA Global Hourly S3 Archive](<https://noaa-global-hourly-pds.s3.amazonaws.com/index.html>) |
| Integrated Surface Dataset – bulk archive | [NOAA ISD Archive](<https://noaa-isd-pds.s3.amazonaws.com/index.html>) |
| ASOS One-Minute Page 1 | [One-Minute Page 1 Data](<https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg1/>) |
| ASOS One-Minute Page 2 | [One-Minute Page 2 Data](<https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg2/>) |
| ASOS Five-Minute Data | [Five-Minute Data Archive](<https://www.ncei.noaa.gov/data/automated-surface-observing-system-five-minute/>) |
| Iowa Environmental Mesonet – ASOS data download | [IEM ASOS Data Download](<https://mesonet.agron.iastate.edu/request/download.phtml>) |
| Iowa Environmental Mesonet – One-Minute Data | [IEM One-Minute Archive](<https://mesonet.agron.iastate.edu/request/asos/1min.phtml>) |

The NOAA NCEI archive is the primary authoritative source. Iowa Environmental Mesonet (IEM) is a useful secondary access service that processes and redistributes ASOS observations.

ncei.noaa.gov



## 4. Project leader or dataset curator

There are three organizations responsible for the ASOS program:

- National Weather Service (NWS), NOAA: operational weather observation program.
- Federal Aviation Administration (FAA): aviation weather observation requirements and infrastructure.
- Department of Defense (DoD): participating military installations and observation requirements.

Dataset archive curator and processor: NOAA National Centers for Environmental Information (NCEI).

NCEI acquires and processes the station observations, performs basic quality assurance, organizes monthly station files, and maintains the archive.

The metadata identifies the NCEI Customer Engagement Branch as the dataset point of contact. It does not identify one individual as the overall ASOS project leader or curator.

NCEI



Official equipment documentation: [NWS ASOS Equipment](<https://www.weather.gov/asos/asosequip.html>).

## 5. Precipitation instruments used

ASOS uses several precipitation-related instruments. The main accumulation gauges are:

File:2015-04-18 12 15 13 Closeup of the heated tipping bucket rain gauge at the Lovelock Airport-Derby Field ASOS in Pershing County, Nevada.jpg - Wikimedia Commons

1. Heated Tipping Bucket (HTB)

- Measures liquid precipitation accumulation.
- Uses a heated funnel and tipping bucket.
- Typically records 0.01 inch per bucket tip.
- Heating melts frozen precipitation for liquid-equivalent measurement.
- Original standard ASOS precipitation gauge.

Precipitation Accumulation.html

2. All Weather Precipitation Accumulation Gauge (AWPAG)

- Heated weighing-type precipitation gauge.
- Measures liquid and frozen precipitation.
- Designed to improve measurements of snow and freezing precipitation.
- Replaces the older heated tipping bucket at equipped stations.

3. Freezing Rain Sensor (FRS)

- Detects freezing rain and icing conditions.
- Uses a magnetostrictive oscillator principle.
- Provides precipitation/icing identification rather than serving as the main accumulation gauge.

Other relevant instrumentation includes the present-weather sensor, which helps identify precipitation type and intensity.

Important: Not every ASOS station has identical equipment. Some stations have HTB gauges, while others have upgraded AWPAG equipment. The installed equipment varies by station.

National Weather Service



## 6. Temporal coverage / period of record

The period of record depends on the particular ASOS data product.

| Data product | Period of record |
| --- | --- |
| Five-minute ASOS observations | July 1, 1996 – Present |
| One-minute ASOS Page 1 | June 1, 1998 – Present (catalogued record) |
| One-minute ASOS Page 2 | June 1, 1998 – Present (catalogued record) |
| Global Hourly / ISD | Longer historical record; varies by station |

For the five-minute dataset, NOAA's official metadata explicitly gives July 1, 1996, to present.

NCEI



## 7. Temporal frequency

ASOS supports multiple observation frequencies:

| Frequency | Description |
| --- | --- |
| 1-minute | High-resolution observations, including precipitation |
| 5-minute | Five-minute surface weather observations |
| Hourly | Routine METAR weather observations |
| Special observations | Generated when significant weather conditions change |
| Daily | Daily precipitation and climatological summaries |
| Monthly | Monthly climatological summaries |

For precipitation research, the one-minute and five-minute datasets are particularly useful.

Note that hourly precipitation accumulation and one-minute precipitation measurements can represent different accumulation periods and should not be treated as interchangeable.

NCEI



## 8. Spatial coverage

- Approximately 900 ASOS stations.
- United States (50 states).
- Puerto Rico.
- U.S. Virgin Islands.
- Some Pacific island territories.
- Some international locations in certain data products.

The official five-minute dataset metadata specifies the following approximate bounding coordinates:

| Coordinate | Value |
| --- | --- |
| Northern latitude | 72° N |
| Southern latitude | 15° N |
| Eastern longitude | 60° W |
| Western longitude | 170° W |

These coordinates represent the metadata bounding box, not a continuous geographical observation grid.

NCEI



## 9. Spatial resolution

Spatial resolution: Point-based, irregular station distribution.

ASOS is a network of individual weather stations, generally located at airports.

- Each station represents observations at its own geographic coordinates.
- Stations are not arranged on a uniform grid.
- Distance between stations varies geographically.
- There is no single standardized spatial resolution in kilometers or degrees.

For spatial analysis, the station latitude and longitude should be used. Interpolation or gridding must be performed separately if a regular spatial resolution is required.

## 10. Legacy or ongoing dataset?

Ongoing operational datasetASOS is an ongoing dataset rather than a discontinued legacy dataset.

- Stations continuously collect observations, 24 hours a day.
- NOAA continues to archive and distribute observations.
- Equipment upgrades and replacements occur over time.
- Historical observations remain available for climate and meteorological research.

NCEI



## 11. Consolidated dataset summary

This table is suitable for transferring into a dataset inventory or literature review.

| Parameter | ASOS dataset information |
| --- | --- |
| Dataset name | Automated Surface Observing System (ASOS) |
| DOI | No single DOI identified for the overall ASOS network |
| Dataset identifier | NCEI DSI 6401\_02 (five-minute product); NCEI DSI 3285 (one-minute product) |
| Primary archive | NOAA National Centers for Environmental Information (NCEI) |
| Secondary archive/access | Iowa Environmental Mesonet (IEM); AWS-hosted NOAA bulk archives |
| Project operators | NOAA/NWS, FAA, and DoD |
| Dataset curator | NOAA NCEI |
| Precipitation instruments | Heated Tipping Bucket (HTB), All Weather Precipitation Accumulation Gauge (AWPAG), Freezing Rain Sensor |
| Temporal coverage | Five-minute: July 1996–present; one-minute: June 1998–present in the NCEI catalogue |
| Temporal frequency | 1-minute, 5-minute, hourly, daily, and monthly products |
| Spatial coverage | United States, Puerto Rico, U.S. Virgin Islands, and Pacific island territories |
| Spatial resolution | Irregular point-based station network; no fixed grid resolution |
| Dataset status | Ongoing |

## 12. Important references

These are the most useful primary sources for documenting your dataset.

1. NOAA NCEI – Automated Surface/Weather Observing Systems (ASOS/AWOS) [Official dataset description and access methods](<https://www.ncei.noaa.gov/products/land-based-station/automated-surface-weather-observing-systems>).

2\. NOAA NCEI – Five-Minute ASOS Dataset Metadata [Official metadata, period of record, spatial extent, and dataset citation](<https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00418/html>).

3\. NWS – ASOS Sensor Suite Design [Official instrumentation documentation](<https://www.weather.gov/asos/TechnicalOverview.html>).

4\. NWS – Heated Tipping Bucket [Precipitation gauge specifications and operation](<https://www.weather.gov/asos/TippingBucket.html>).

5\. NWS – ASOS Equipment FAQ [Equipment types installed at individual stations](<https://www.weather.gov/asos/asosequip.html>).

6\. Iowa Environmental Mesonet – ASOS Precipitation Data Notes [Precipitation measurement and accumulation timing](<https://mesonet.agron.iastate.edu/ASOS/precipnote.phtml>).

DOI clarification: If you need a citable DOI rather than a NOAA dataset identifier, there are separately archived ASOS subsets with DOIs. For example, the NCAR/EOL ASOS five-minute dataset for December 2013–January 2014 has DOI [10.26023/RTF3-A0N3-E20P](<https://doi.org/10.26023/RTF3-A0N3-E20P>). This DOI applies only to that specific subset, not the complete operational ASOS archive.

