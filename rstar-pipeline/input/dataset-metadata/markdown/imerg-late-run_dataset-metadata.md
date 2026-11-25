# Dataset metadata template

## Ask ChatGPT for the following

Dataset name: IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM)

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

# IMERG Late Run dataset – Metadata summary

Note =

The Integrated Multi-satellitE Retrievals for GPM (IMERG) Late Run is a NASA Level-3 global precipitation dataset produced under the Global Precipitation Measurement (GPM) mission, a collaboration between NASA and JAXA.

It combines precipitation observations from multiple satellite instruments to produce gridded precipitation estimates. The Late Run is designed for near-real-time applications, with approximately 12–14 hours of processing latency.

The Late Run uses climatological gauge adjustment, whereas the Final Run incorporates monthly gauge analyses.

------

NASA Global Precipitation Measurement Mission

## 1. Dataset metadata

| Requested information | Value |
| --- | --- |
| Dataset name | GPM IMERG Late Run |
| Dataset version | V07 / V07B (current processing generation) |
| Processing level | Level 3 |
| Dataset type | Satellite-derived precipitation estimates |
| Project | Global Precipitation Measurement (GPM) |
| Producing organization | NASA Goddard Space Flight Center |
| Near-real-time latency | Approximately 12–14 hours |

## 2. Dataset DOI

Verified identifierDOI: `10.5067/GPM/IMERG/3B-HH-L/07`

- Dataset short name: `GPM_3IMERGHHL`
- Product: GPM IMERG Late Precipitation L3 Half Hourly
- Version: V07
- DOI link: [https://doi.org/10.5067/GPM/IMERG/3B-HH-L/07](<https://doi.org/10.5067/GPM/IMERG/3B-HH-L/07>)

This is the DOI for the half-hourly Late Run product, rather than the Early or Final Run.

NASA Open Data Portal

## 3. Data archives and repositories

The dataset is stored and distributed through the following NASA data archives:

| Archive | Description |
| --- | --- |
| NASA GES DISC | Goddard Earth Sciences Data and Information Services Center; primary public archive and distribution service |
| NASA PPS | Precipitation Processing System; operational processing and distribution archive for GPM products |
| NASA Earthdata | Discovery and access infrastructure for NASA Earth science datasets |
| AWS Open Data Registry | Cloud-hosted access to the GES DISC IMERG dataset |

The two principal distribution systems are GES DISC and PPS.

NASA Global Precipitation Measurement Mission


## 4. Dataset access URLs and endpoints

These are the relevant access points for the Late Run dataset.

| Endpoint title | URL |
| --- | --- |
| IMERG Late Run – 30-minute data (GES DISC) | [GPM\_3IMERGHHL V07](<https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary>) |
| IMERG Late Run – Daily data (GES DISC) | [GPM\_3IMERGDL V07](<https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_07/summary>) |
| IMERG data directory (NASA GPM) | [NASA GPM Data Directory](<https://gpm.nasa.gov/data/directory>) |
| IMERG Late Run – PPS archive | [NASA PPS IMERG directory](<https://jsimpsonhttps.pps.eosdis.nasa.gov/imerg/>) |
| IMERG Late Run – AWS Registry | [AWS Open Data Registry](<https://registry.opendata.aws/nasa-gpm3imerghhl/>) |
| IMERG products in NASA Giovanni | [NASA Giovanni](<https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=IMERG>) |

Recommended access: Use GES DISC for downloading the half-hourly or daily dataset, subsetting geographical areas, and accessing metadata. PPS is particularly useful for accessing operational products.

Note that PPS access may require registration.

NASA Global Precipitation Measurement Mission


## 5. Project leader or dataset curator

Scientific and algorithm leadership:

- Dr. George J. Huffman
- Organization: NASA Goddard Space Flight Center (GSFC).
- Role: GPM Project Scientist and lead of the GPM Multi-satellite Algorithm Team.
- Research responsibility: Development and scientific leadership of the IMERG algorithm.

Dataset archive and curation:

- NASA Goddard Earth Sciences Data and Information Services Center (GES DISC).
- Publisher: NASA/GSFC/SED/ESD/TISL/GESDISC.
- Dataset support: NASA Earthdata Support.

It is useful to distinguish the scientific algorithm lead from the data archive curator: George Huffman is the scientific lead, while GES DISC manages the archived dataset and its distribution.

NASA Sciences and Exploration Directorate

## 6. Precipitation instruments used for measurements

IMERG uses observations from multiple satellites in the GPM international constellation.

The main measurement technologies are:

1. Passive Microwave (PMW) radiometers – provide satellite observations of precipitation-related microwave emissions.
2. Infrared (IR) sensors – provide cloud-top temperature and cloud information used to estimate precipitation between microwave satellite observations.

Examples of contributing satellite instruments include:

| Satellite instrument | Instrument type |
| --- | --- |
| GMI – GPM Microwave Imager | Passive microwave radiometer |
| TMI – TRMM Microwave Imager | Passive microwave radiometer |
| SSMIS – Special Sensor Microwave Imager/Sounder | Passive microwave radiometer/sounder |
| AMSR2 – Advanced Microwave Scanning Radiometer 2 | Passive microwave radiometer |
| AMSU-B – Advanced Microwave Sounding Unit-B | Microwave sounder |
| MHS – Microwave Humidity Sounder | Microwave sounder |
| ATMS – Advanced Technology Microwave Sounder | Microwave sounder |
| SAPHIR – Sounder for Atmospheric Profiling of Humidity in the Intertropics by Radiometry | Microwave sounder |

Additional observations from international geostationary infrared satellite systems contribute to the precipitation estimates.

Important distinction: IMERG is not a direct measurement from one precipitation instrument. It is a merged satellite-derived precipitation product. Microwave observations provide the principal precipitation estimates, while infrared observations help fill temporal gaps through the interpolation process.

NASA Global Precipitation Measurement Mission

## 7. Temporal period of the dataset record

- Start date: January 1998.
- End date: Present (continuously updated).
- Historical coverage: Includes the TRMM era (1998–2015) and the GPM era (2014–present).
- Processing latency: Approximately 12–14 hours after observation time.

The Late Run has been retrospectively processed to extend the historical record, in addition to providing near-real-time observations.

The NASA GPM Data Directory identifies January 1998 to present as the current record period.

NASA Global Precipitation Measurement Mission


## 8. Temporal frequency

Primary frequency: 30 minutesThe dataset provides:

| Temporal frequency | Availability |
| --- | --- |
| Half-hourly (30 minutes) | Yes – primary product |
| Daily (1 day) | Yes – derived product |
| Hourly | Can be calculated by aggregating two half-hourly observations |
| Monthly | Available through aggregation, but not the standard Late Run product |

Each half-hourly observation represents a precipitation estimate over a 30-minute period.

The standard Late Run products available through GES DISC include:

- Half-hourly: `GPM_3IMERGHHL`
- Daily: `GPM_3IMERGDL`

Source: NASA GPM Data Directory and GES DISC.

NASA Global Precipitation Measurement Mission


## 9. Spatial coverage

Global coverage

- Longitude: −180° to +180°
- Latitude: −90° to +90°
- Geographic extent: Global, including land and ocean surfaces.

The product provides near-global coverage, with some limitations in a small number of grid boxes very close to the poles.

It is particularly useful for precipitation monitoring over oceans and remote regions where ground-based rain gauges are unavailable.

NASA Open Data Portal

## 10. Spatial resolution

0.1° × 0.1°- Angular resolution: 0.1° latitude × 0.1° longitude.
- Approximate ground resolution: 10 km × 10 km.
- Grid type: Regular latitude–longitude grid.

The actual ground dimensions vary with latitude because longitude spacing decreases toward the poles.

Source: NASA GPM Data Directory and GES DISC dataset metadata.

NASA Global Precipitation Measurement Mission

## 11. Legacy dataset or ongoing?

Ongoing datasetIMERG Late Run is an ongoing, actively maintained dataset, not a discontinued legacy dataset.

Reasons:

- NASA continues to generate near-real-time precipitation estimates.
- New observations are incorporated approximately every 30 minutes.
- The dataset has undergone algorithm and version updates.
- Version 07B is identified in NASA's current documentation as the latest processing generation.
- Historical data have been reprocessed to extend the record back to January 1998.

The dataset is therefore both an ongoing operational product and a historical climate and precipitation data resource.

NASA Global Precipitation Measurement Mission


## 12. Consolidated metadata table

This table provides a concise version suitable for a research report, dataset inventory, or metadata spreadsheet.

| Metadata field | IMERG Late Run |
| --- | --- |
| Dataset name | Integrated Multi-satellitE Retrievals for GPM (IMERG) Late Run |
| DOI | 10.5067/GPM/IMERG/3B-HH-L/07 |
| Data archive | NASA GES DISC; NASA PPS |
| Additional access | NASA Earthdata; AWS Open Data Registry |
| Download endpoint | [https://disc.gsfc.nasa.gov/datasets/GPM\_3IMERGHHL\_07/summary](<https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary>) |
| Daily endpoint | [https://disc.gsfc.nasa.gov/datasets/GPM\_3IMERGDL\_07/summary](<https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_07/summary>) |
| Project leader | Dr. George J. Huffman |
| Dataset curator / distributor | NASA GES DISC |
| Measurement instruments | Passive microwave radiometers, microwave sounders, and infrared satellite sensors |
| Temporal start | January 1998 |
| Temporal end | Present |
| Temporal frequency | 30 minutes (primary); daily derived product |
| Spatial coverage | Global |
| Latitude coverage | −90° to +90° (with limited polar gaps) |
| Longitude coverage | −180° to +180° |
| Spatial resolution | 0.1° × 0.1° (approximately 10 km) |
| Dataset status | Ongoing |
| Current processing generation | V07B |

## 13. Key references and documentation

These are the most useful authoritative sources for verifying and citing the metadata.

1. NASA GPM – IMERG Technical Documentation: [IMERG V07 Technical Documentation](<https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation>).

2. NASA GPM – Precipitation Data Directory: [GPM Precipitation Data Directory](<https://gpm.nasa.gov/data/directory>).

3. NASA GES DISC – IMERG Late Run: [IMERG Late Run dataset information](<https://gpm.nasa.gov/node/3322>).

4. NASA Earthdata – Dataset DOI and metadata: [GPM IMERG Late Run V07](<https://doi.org/10.5067/GPM/IMERG/3B-HH-L/06>).

5. NASA GSFC – George J. Huffman biography and project responsibilities: [Dr. George J. Huffman – NASA](<https://science.gsfc.nasa.gov/earth/bio/george.huffman>).

6. NASA GPM – IMERG overview: [IMERG: Integrated Multi-satellitE Retrievals for GPM](<https://gpm.nasa.gov/data/imerg>).

Metadata note: For a formal dataset inventory, I recommend recording the half-hourly product (`GPM_3IMERGHHL`) as the primary dataset. Daily data are a separate derived product with their own dataset identifier. Also, the Late Run uses climatological gauge adjustment, whereas the Final Run incorporates monthly gauge analyses; these should not be treated as identical products.

NASA Global Precipitation Measurement Mission


