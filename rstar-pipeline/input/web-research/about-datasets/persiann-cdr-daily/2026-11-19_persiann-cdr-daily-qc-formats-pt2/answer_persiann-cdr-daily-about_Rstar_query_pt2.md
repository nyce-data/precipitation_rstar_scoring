# PERSIANN-CDR Daily: quality control, processing, software and formats (Part 2)

PERSIANN-CDR Daily is quality-controlled only by automated checks built into its producer's code (CHRS, UC Irvine). Those checks catch missing or corrupt input files and noisy infrared pixels. The dataset has no per-pixel quality flag and no documented QC procedure: NCEI's own stewardship assessment scores its QC monitoring 1.5 of 5, "Procedure not documented or available". The full production code (shell, C/C++ and MATLAB, including the neural-network program) is public as a tarball on NCEI's server. It is not open source, though: the UC Regents' copyright allows use only by nonprofit research institutions for research. The data are offered mainly as CF-compliant daily netCDF-4 files with a DOI, open over HTTPS, THREDDS/OPeNDAP, ERDDAP and AWS, and those routes are FAIR. CHRS's own routes (raw binaries, and a portal with GeoTIFF, ArcGrid and NetCDF) are only partly FAIR. **Confidence: high** for QC, processing and the code license; **moderate** for the CHRS routes and the Earth Engine ratings.

## Quality control

**Is QC done, and by whom?** Yes. The producer (CHRS) builds automated checks into the production code. No manual review step is described ([C-ATBD, CDRP-ATBD-0286, 2014](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf); [User Guide CDRP-GUID-1665, 2025](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf)). The checks, one line each:
- **Missing input file:** replaced with a NODATA file, or the time step is flagged for possible reprocessing (C-ATBD §5.3). In practice, time steps made from problem files are removed, not reprocessed, before bias correction, "due to the length of time required to run the PERSIANN model" (C-ATBD §5.4).
- **Corrupt GridSat-B1 files:** identified and set aside for reprocessing (C-ATBD; User Guide).
- **Abnormal IR pixels:** pixels outside the expected normal range, or very different from their neighbours, are removed (User Guide §5.4).
- **IR range filter and noise threshold:** IR is filtered for out-of-range values when upscaled to 0.25°, and a threshold (thd) on the 3-hourly rain rates removes noisy pixels ([Ashouri et al. 2015](https://doi.org/10.1175/BAMS-D-13-00068.1)).
- **Proposed only:** the C-ATBD says code "could be included" to quantify the GPCP bias adjustment and flag out-of-range data, and that new files "can be compared" with other sources. It doesn't say either was done. Validation against CPC Unified gauges and Stage IV over CONUS was described as "under evaluation" in 2014 (C-ATBD §5.5).

**How suspect values are handled:** by leaving values out, not by flagging them.
- The files have one variable, `precipitation`, with `missing_value` -9999 and `_FillValue` -1. These two missing-data markers differ, so a user's tool may treat only one of them as missing. No quality-flag variable appears in NCEI's ERDDAP description ([NCEI ERDDAP .das](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.das)), and the production code writes only the -9999 missing value.
- Bad months are dropped whole. All of February 1992 is unusable because the IR input couldn't be cleaned and the bias adjustment is monthly ([Use Agreement, Known Issues](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UseAgreement_01B-16.pdf)).
- The first release (v01r00) took in bad GridSat data. It was withdrawn and reprocessed as v01r01 on GridSat v2 ([NCEI metadata, C00854](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00854/html)).

**What the archive and program review (NCEI, NOAA CDR Program):** NCEI runs no QC of its own on the values. The CDR Program required, and NCEI publishes, a C-ATBD, a maturity matrix, a data flow diagram, a user guide and a use agreement ([NCEI document folder](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/)).
- **2013 maturity matrix** ([CDRP-MM-0352](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/MaturityMatrix_01B-16.pdf)): its scores are drawn as coloured cells, which the text can't show. A subagent's reading of them (software 3, metadata 5, documentation 4, validation 3, access 4, utility 4) wasn't checked.
- **NCEI's 2020 stewardship assessment** ([NOAA IR 33336](https://repository.library.noaa.gov/view/noaa/33336)): Data Quality Assurance 4, Quality Control/Monitoring 1.5 ("Procedure not documented or available"), Quality Assessment 3. It notes there is no data-quality information in the metadata record.
- **Not published:** no QA-procedures document and no operational-readiness or transition review is in NCEI's folder.

**QC on the inputs** is done by each input's own producer, not by CHRS:
- **GridSat-B1 (NCEI):** a Fortran scan-line QC, an automated check of each satellite against the others (outliers corrected; flagged `intergeo_cal_flag`), and visual checks of PNG images ([GridSat C-ATBD, 2026](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/AlgorithmDescription_01B-02.pdf); [NCEI GridSat page](https://www.ncei.noaa.gov/products/gridded-geostationary-brightness-temperature)).
- **GPCP monthly:** artifacts are edited out before merging. Its GPCC gauges get "an automated screening and then a manual step" ([GPCP C-ATBD](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-monthly)).
- **NCEP Stage IV**, used to train the network: the River Forecast Centers do manual QC, but hourly estimates at some centres "suffer from lack of manual quality control" ([Nelson et al. 2016](https://repository.library.noaa.gov/view/noaa/15745/noaa_15745_DS1.pdf)).

QC is therefore **automated at the producer, and both automated and manual upstream** (GPCC gauges, Stage IV).

## Processing

The chain, per the data flow diagram ([CDRP-DIA-0351](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/DataFlowDiagram_01B-16.pdf)) and the code package:
1. Read GridSat-B1 IR and split it into subareas (`B1tosubs.c`).
2. Run the PERSIANN neural network (`model/seqSOLO/seqSOLO.cc`, C++, with parameter files for each region and subarea). It was pretrained on NCEP Stage IV hourly data and then kept fixed (Ashouri 2015).
3. Merge to global 3-hourly 0.25° fields (`merg_PERSIANN.c`).
4. Bias-adjust to GPCP monthly in MATLAB (`dobias_adj_B1.m`).
5. Write daily netCDF-4 with CDR metadata (`persiann-cdr_daily.c`), all driven by `Run_PERSIANN.sh`.

The model runs on 4 major subareas split into 24 subareas (C-ATBD §5.1). Production is quarterly, with about a three-month lag (Earth Engine catalog). The package README needs gcc, g++, netCDF-4 and MATLAB ([SourceCode_01B-16.tar.gz](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/SourceCode_01B-16.tar.gz)). The README still names GPCP v2.2.

## Can the public inspect and use the software?

| Software or algorithm | Code published? | Where | License |
|---|---|---|---|
| PERSIANN-CDR package V1: network, preprocessing, merging, bias adjustment, netCDF writer | Yes, as a 4,604,083-byte tarball (files dated 2013–2014, posted 2017-03-10) | [NCEI](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/SourceCode_01B-16.tar.gz) | Not open source. "Proprietary property of The Regents of the University of California". Redistribution and use "permitted by nonprofit, research institutions for research use only" |
| Same code, under the CDR Program's policy | n/a | [Use Agreement](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UseAgreement_01B-16.pdf) | Production software "is outside of the scope of the Open Data policies"; ask the copyright owner named in the code |
| Bias-adjustment step | In the package (`.m` files) | NCEI tarball | As above; also needs MATLAB, a commercial product |
| Network training on Stage IV | Training code not identified in the package; method in papers only | [Ashouri 2015](https://doi.org/10.1175/BAMS-D-13-00068.1) | not found |
| Any CHRS code after 2014 (current operational runs) | Not published | — | — |
| Related PERSIANN-CCS-CDR (a different product) | Yes | [GitHub](https://github.com/mojtabasadeghi77/PERSIANN-CCS-CDR) (no license); [V02](https://github.com/bolbolim/PERSIANN-CCS-CDR-V02) (Apache-2.0) | as listed |
| Input QC code (GridSat Fortran QC, `gridsat_2_image.pro`) | Not checked | — | — |

So the public can **inspect** the PERSIANN-CDR algorithm's code, but **reuse is limited** to nonprofit research. NCEI's metadata also says the package is "for reference only" and not intended to be portable. No repository of the PERSIANN-CDR code was found on GitHub, and no CHRS page offers it. (The GitHub API was refused by the sandbox, so the GitHub search was only partial.)

## Formats and FAIR ratings

Rule used: FAIR passes all four tests; partly FAIR fails one or two (named); non-FAIR passes at most one.

| Route | Format | F: DOI and catalog | A: open protocol, no login | I: open format, CF names and units | R: license and provenance | Rating |
|---|---|---|---|---|---|---|
| [NCEI HTTPS](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2026/) | netCDF-4, one file per day (~1.3 MB) | DOI 10.7289/V51V5BWQ; NCEI ISO, NASA CMR, data.gov | yes | yes: CF, `precipitation_amount`, mm | "No constraints on data access or use"; lineage stated | **FAIR** |
| NCEI THREDDS/OPeNDAP | same files | as above | yes (seen only through ERDDAP's source address; catalog not read) | yes | as above | **FAIR** (moderate) |
| [NCEI ERDDAP](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.das) | gridded subsets | as above | yes | yes (`Conventions` CF-1.4; `Metadata_Conventions` says CF-1.6) | license attribute as above | **FAIR** |
| [AWS S3, NODD](https://registry.opendata.aws/noaa-cdr-atmospheric/) | same netCDF | AWS registry, plus NCEI's DOI | yes (`--no-sign-request`) | yes | NODD: "open to the public and can be used as desired"; attribution requested | **FAIR** |
| [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR) | EE image collection | catalog entry | sign-in not stated in what was read (Earth Engine normally needs an account) | only through EE's API; units mm | "no restrictions are placed upon their use" | **partly FAIR** (likely fails A and I; low confidence) |
| [CHRS HTTPS/FTP server](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/) | daily `.bin.gz` raw binary (`daily_netcdf/` is empty) | no DOI or catalog record on the pages read | yes | no: headerless binary | no license stated | **non-FAIR** |
| [CHRS Data Portal](https://chrsdata.eng.uci.edu/) | ArcGrid, GeoTIFF, NetCDF on request; shapefiles for subsets ([Nguyen 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326112/)) | no DOI on the portal page | web tool; login not stated | open formats; CF names not checked | no license stated | **partly FAIR** (fails F and R) |
| [IRI Data Library](https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.CDR/.PERSIANN-CDR/.v01r01/) | IRI's own data services | listed in IRI's catalog | no: "now requires all users to sign in" | not checked | not checked | **partly FAIR at best** (fails A) |

**The license is stated loosely.** The files, ERDDAP and the CDR Program say use is unrestricted ("non-proprietary, publicly available, and no restrictions are placed upon their use"). But DataCite's DOI record has an empty `rightsList` ([DataCite](https://api.datacite.org/dois/10.7289/V51V5BWQ)). Only [data.gov](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-precipitation-estimation-from-remotely-sensed-information-) names a license, CC0 1.0, on the same harvested record that says Access Level "non-public" and Rights "otherRestrictions". This conflict is unresolved. Each NCEI-route row passes R on the no-constraints statement, not on a named license.

## Gaps

- **Native file attributes not opened:** the variable list comes from ERDDAP and the netCDF writer code, not from a downloaded daily file.
- **2013 maturity matrix scores** are graphical and weren't checked by eye.
- **No missing-data threshold is published.** A user study counts 419 missing days over 32 years, 95% of them in 1983–1999 ([Pietroiusti et al. 2024](https://esd.copernicus.org/articles/15/225/2024/)).
- **Not read:** the CHRS README and the portal's terms of use (format layout, any license); the NCEI THREDDS catalog (timed out).
- **Not covered:** whether CHRS's current production code differs from the 2014 package is unpublished; ask CHRS or PERSIANN_contacts@noaa.gov. The GitHub API was refused.
- `check-by-hand.md` lists 2 pages. `sites-to-trust.md` lists 1 refused host, api.github.com; you can check whether to add it to your sandbox's allowed domains.

## Sources

**NCEI / NOAA CDR Program**
- [CHRS / NOAA CDR Program, C-ATBD CDRP-ATBD-0286, 2014](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf)
- [NOAA CDR Program, User Guide CDRP-GUID-1665, 2025](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf)
- [NOAA CDR Program, Use Agreement, UseAgreement_01B-16](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UseAgreement_01B-16.pdf)
- [NOAA CDR Program, Maturity Matrix CDRP-MM-0352, 2013](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/MaturityMatrix_01B-16.pdf)
- [NOAA CDR Program, Data Flow Diagram CDRP-DIA-0351, 2013](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/DataFlowDiagram_01B-16.pdf)
- [CHRS, PERSIANN-CDR package V1 source code, 2014](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/SourceCode_01B-16.tar.gz)
- [NCEI, PERSIANN document folder listing](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/)
- [NCEI, data stewardship maturity report, 2020](https://repository.library.noaa.gov/view/noaa/33336)
- [NCEI, ISO metadata C00854 (Wayback copy, 2026-10-31)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00854/html)
- [NCEI, ERDDAP .das](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.das)
- [NCEI, 2026 file listing](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2026/)
- [NCEI, GridSat-B1 C-ATBD, 2026](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/AlgorithmDescription_01B-02.pdf)
- [NCEI, GridSat-B1 product page](https://www.ncei.noaa.gov/products/gridded-geostationary-brightness-temperature)
- [NOAA CDR Program, GPCP Monthly C-ATBD](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-monthly)

**CHRS**
- [CHRS, PERSIANN-CDR server listing](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/)
- [CHRS, daily folder listing](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/)
- [CHRS, Data Portal](https://chrsdata.eng.uci.edu/)

**Papers**
- [Ashouri et al., BAMS, 2015](https://doi.org/10.1175/BAMS-D-13-00068.1)
- [Nguyen et al., Scientific Data, 2019 (CHRS Data Portal)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6326112/)
- [Nelson et al., Weather and Forecasting, 2016](https://repository.library.noaa.gov/view/noaa/15745/noaa_15745_DS1.pdf)
- [Pietroiusti et al., ESD, 2024 (read as an extract)](https://esd.copernicus.org/articles/15/225/2024/)

**Registries and other routes**
- [DataCite, DOI 10.7289/V51V5BWQ](https://api.datacite.org/dois/10.7289/V51V5BWQ)
- [data.gov catalog record (read as an extract)](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-precipitation-estimation-from-remotely-sensed-information-)
- [AWS Registry of Open Data, NOAA CDRs](https://registry.opendata.aws/noaa-cdr-atmospheric/)
- [Google Earth Engine catalog (read as an extract)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR)
- [IRI Data Library (sign-in page only)](https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.CDR/.PERSIANN-CDR/.v01r01/)

**GitHub**
- [GitHub, PERSIANN-CCS-CDR](https://github.com/mojtabasadeghi77/PERSIANN-CCS-CDR)
- [GitHub, PERSIANN-CCS-CDR-V02](https://github.com/bolbolim/PERSIANN-CCS-CDR-V02)

Saved in [`web_search_results/2026-11-19_persiann-cdr-daily-qc-formats-pt2/`](./): this answer, the research record, `method.md`, `check-by-hand.md` and `sites-to-trust.md`.
