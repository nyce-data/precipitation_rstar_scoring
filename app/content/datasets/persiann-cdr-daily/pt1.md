PERSIANN-CDR Daily is a satellite precipitation record. It gives daily rainfall estimates from 1 January 1983 to a few months before the present, at 0.25° resolution, between 60°S and 60°N. A neural network turns geostationary infrared imagery (GridSat-B1) into rain rates, and those rates are then bias-adjusted to the GPCP monthly analysis. It is produced by the Center for Hydrometeorology and Remote Sensing (CHRS) at the University of California, Irvine, under NOAA's Climate Data Record (CDR) Program. NOAA NCEI is the archive of record and official distributor; Google Earth Engine, AWS, Azure and others only redistribute NCEI's copy. **Confidence: high**, except for the GPCP version used in each year and the role of Stage IV radar (moderate).

## Producer versus archive

- **Producer: CHRS at UC Irvine.** NCEI's own landing page says "The data were produced by the University of California at Irvine, and are archived at the NOAA National Centers for Environmental Information (NCEI)", and it lists UC Irvine as the "Processor" ([NCEI landing page, Wayback copy of 31 Oct 2026](https://web.archive.org/web/20261031104050/https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00854)). The CHRS developers write that "CHRS's servers produce PERSIANN and PERSIANN-CDR by implementing the algorithms locally" ([Nguyen et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6326112/)). **High.**
- **Archive of record and distributor: NOAA NCEI** (part of NESDIS), within the NOAA CDR Program. NCEI is listed as "Distributor" and the "NOAA Climate Data Record Program Office" as dataset point of contact. NCEI's 2025 user guide calls the dataset "an operational climate data record" available through NCEI ([NCEI User Guide CDRP-GUID-1665, 2025](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf)). The DOI is [10.7289/V51V5BWQ](https://doi.org/10.7289/V51V5BWQ), version v01r01. **High.**
- **Program:** the NOAA Climate Data Record Program at NCEI in Asheville, NC. The CHRS portal says the CDR "was funded in part by" that program ([CHRS Data Portal](https://chrsdata.eng.uci.edu/)). Funding itself is left to Part 3.

## Where it lives: access points

| Host | Role | Access points |
|---|---|---|
| NOAA NCEI | Archive of record, official distributor | [Product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann) (Download, THREDDS, ERDDAP, Google Cloud, Amazon Cloud); [HTTPS archive](https://www.ncei.noaa.gov/data/precipitation-persiann/access/) (year folders 1983–2026); [THREDDS](https://www.ncei.noaa.gov/thredds/catalog/satellite/persiann.html); [ERDDAP](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.html); [landing page / DOI](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00854) |
| CHRS, UC Irvine | Producer; also serves its own copy | [CHRS Data Portal](https://chrsdata.eng.uci.edu/) (daily, monthly and yearly downloads; built in 2016); HTTPS [persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/) (also `mthly/`, `yearly/`); FTP `ftp://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR` |
| Google Earth Engine | Redistributor | [NOAA/PERSIANN-CDR](https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR) (1983-01-01 to 2026-07-31) |
| AWS (NOAA Open Data Dissemination) | Redistributor | [Registry](https://registry.opendata.aws/noaa-cdr-atmospheric/), bucket `s3://noaa-cdr-precip-persiann-pds/` |
| Microsoft Azure | Redistributor | [NOAA CDR listing](https://microsoft.github.io/AIforEarthDataSets/data/noaa-cdr.html), container `precip-persiann` at `noaacdr.blob.core.windows.net` |
| IRI/LDEO Data Library | Redistributor (not verified) | [v01r01 entry](https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.CDR/.PERSIANN-CDR/.v01r01/); now needs a sign-in, and the holdings' end date was not checked |

When checked on 19 Nov 2026, NCEI's 2026 folder and the CHRS daily folder both ended at **31 July 2026**, in files posted on 13 October 2026 ([NCEI 2026 listing](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2026/); [CHRS listing](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/)). The CHRS portal's info tab still says "Latest Update: September 2020" and "01/01/1983 to 12/31/2015 (delayed present)", which is out of date. NCEI's product page warns that its cloud migration means "slower update cycles", and the live landing page returned HTTP 503 during this run.

## What kind of dataset it is

The product is **multi-satellite but infrared-only in its running inputs**, adjusted to a blended satellite-and-gauge monthly product. It uses no radar and no gauges directly. **High.**

| Input | Provider | Satellites or instruments | Role |
|---|---|---|---|
| GridSat-B1 infrared window channel (IRWIN, about 10–12 µm), 3-hourly, 0.07° regridded to 0.25° | NOAA NCEI (a CDR of its own, made from ISCCP B1) | Geostationary imagers on GOES, Meteosat, GMS/MTSAT and FY-2 (NCEI's keywords also list INSAT) | **Main input**: the neural network is run on it |
| GPCP monthly 2.5° analysis (v2.2 in NCEI documents; v2.3 for at least 2009–2013) | GPCP, a WCRP project (NASA GSFC distributes v2.2 per the C-ATBD) | SSM/I microwave and IR satellite estimates, adjusted with GPCC rain-gauge analyses | **Bias adjustment**, month by month |
| NCEP Stage IV hourly precipitation | NOAA NCEP EMC | NEXRAD radar with gauge adjustment, contiguous US | **Initial training** of the neural network, then held fixed (per Ashouri et al. 2015); also used for **evaluation** |

Sources: [User Guide §4](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf); [C-ATBD CDRP-ATBD-0286 Rev. 2](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf); [Ashouri et al. 2015, BAMS](https://doi.org/10.1175/BAMS-D-13-00068.1) (read via a course copy); NCEI landing page.

- **Passive microwave** is not used directly. The user guide says the CDR "does not directly incorporate Passive Microwave (PMW) observations … except indirectly through the GPCP monthly data used for bias correction". Avoiding microwave dependence is what lets the record reach back to 1983.
- **GPCP version (moderate):** the C-ATBD (2014), the data flow diagram and even the 2025 user guide say GPCP v2.2. The developers, however, write that "the updated PERSIANN-CDR V2.3 data has replaced V2.2 data for the 2009–2013 period on CHRS data portal and NOAA National Centers for Environmental Information (NCEI)" ([Sadeghi et al. 2019, Remote Sensing](https://doi.org/10.3390/rs11232755), read via the [NOAA repository copy](https://repository.library.noaa.gov/view/noaa/65498)). A July 2026 file's source attribute also names `gpcpv23_m2607.bin` and GridSat-B1 `v02r01`. No document states which GPCP version covers which years.
- **Stage IV (moderate):** only Ashouri et al. (2015) give it a training role: the model "is pretrained using the … NCEP stage IV hourly precipitation data", and its parameters are then "kept fixed". The C-ATBD and user guide mention Stage IV only for evaluation. GPCP-1DD, CPC Unified gauges and TMPA are likewise used only for evaluation.

## How the data are made

Every production step is algorithmic, and runs one month at a time ([C-ATBD](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf); [Ashouri et al. 2015](https://doi.org/10.1175/BAMS-D-13-00068.1)). **High.**
1. **PERSIANN neural network.** It maps GridSat-B1 brightness temperatures to 3-hourly rain rates at 0.25°, giving "PERSIANN-B1". Its inputs are pixel statistics over 3×3 and 5×5 neighbourhoods. The network was pre-trained and then fixed, with no adaptive updating in the CDR. CHRS describes the general PERSIANN network as one whose input-to-hidden layer "forms a self-organizing feature map (SOFM)" ([CHRS approach page](https://chrs.web.uci.edu/SP_approach.php)), but the CDR documents don't use that term.
2. **Noise threshold.** Rain rates below 0.1 mm/hr are removed. That is the C-ATBD's and the user guide's unit; Sadeghi et al. (2019) write "a threshold of 0.1 mm/day". This answer goes with the C-ATBD.
3. **GPCP bias adjustment.** PERSIANN-B1 is summed to 2.5° monthly totals, and the ratio GPCP/PERSIANN-B1 (capped at 20) is applied to each 3-hourly 0.25° pixel. The C-ATBD says "thd = 0.1 and maximum w = 20 is perhaps the best combination".
4. **Daily totals.** The adjusted 3-hourly values are summed to daily mm/day and written as NetCDF.

**How often it is extended: quarterly**, about 2.5–3 months behind real time. **High.**
- NCEI's landing page gives "Data Update Frequency | Quarterly".
- The user guide says "Quarterly updates to the CDR data sets are produced and delivered to extend the time series".
- The CHRS portal paper's Table 1 gives a 3-month delay ([Nguyen et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6326112/)), and Earth Engine says "produced quarterly, with a typical lag of three months".
- The 2026 files arrived in two batches: January–March 2026 created 9 July, and April–July 2026 created 13 October. The lag figure is worked out from those file dates; NCEI doesn't state one.

**History:**
- The dataset was first submitted to the CDR Program on 29 Aug 2013 and published on 1 June 2014 as v01r01 (NCEI DSI 3611_01).
- v01r00 was withdrawn because of noisy GridSat-B1 input.
- The user guide says work on GridSat-B1 may later add some months of 1980–1982.
- CHRS's server posted the 2024 files in Oct 2025 and the 2025 files from Dec 2025 to Mar 2026. That is slower than a quarterly cycle, and it came after CHRS's download links were down until 11 Oct 2024.

**Start of record (resolved):** NCEI's product page and C-ATBD §3.4 say 1982. The user guide, the landing page, ERDDAP and the files themselves start on 1983-01-01, so 1983 is taken as correct.

## Who is responsible

- **Producing group:** the Center for Hydrometeorology and Remote Sensing (CHRS). CHRS calls itself "an informal interdisciplinary group" of faculty and researchers from Civil and Environmental Engineering and Earth System Science. Its address is Civil and Environmental Engineering, The Henry Samueli School of Engineering, UC Irvine ([CHRS about](https://chrs.web.uci.edu/about.php); [CHRS directory](https://chrs.web.uci.edu/chrs_directory.php)). **Moderate** (the pages are undated, with a © 2017 footer).
- **Parent organization:** the University of California, Irvine. The program is NOAA's CDR Program, run at NCEI (NOAA/NESDIS, US Department of Commerce).
- **Credited people:**
  - The dataset citation reads "Sorooshian, Soroosh; Hsu, Kuolin; Braithwaite, Dan; Ashouri, Hamed; and NOAA CDR Program (2014)".
  - Soroosh Sorooshian is the **Principal Investigator** (NCEI landing and product pages).
  - The C-ATBD's authors are Kuolin Hsu, Hamed Ashouri, Dan Braithwaite and Sorooshian, and the algorithm was "submitted to the National Climatic Data Center (NCDC) by Soroosh Sorooshian".
  - NCEI's ERDDAP file metadata names Dan Braithwaite as `creator_name`.
  - Co-authors from NOAA/NCEI and CICS-NC on Ashouri et al. 2015 include K. R. Knapp (GridSat-B1), B. R. Nelson and O. P. Prat.
  - On the current CHRS directory, Amir AghaKouchak is "Director of CHRS", Sorooshian is "Founding Director", Phu Nguyen is "Associate Director", and Kuo-lin Hsu is a professor. Ashouri is listed as an alumnus, and Braithwaite isn't listed.
  - The directory titles conflict with a search summary of a UC Irvine research page that called Sorooshian director; that page returned HTTP 403 and wasn't read.
- **Staff count: none published.** Neither CHRS nor NCEI gives a number. NCEI names no individual steward: its contacts are the Customer Engagement Branch and `cdr-ipt-PERSIANN@noaa.gov`.

## How the other PERSIANN products relate

All of these are CHRS products. Only PERSIANN-CDR (daily) is the NOAA CDR archived at NCEI; the rest are served from the CHRS portal ([CHRS Data Portal](https://chrsdata.eng.uci.edu/)).
- **PERSIANN-CDR monthly and yearly:** aggregations of the same record, downloadable from CHRS. NCEI's archive holds the daily files.
- **PERSIANN:** the near-real-time parent algorithm, run on CPC infrared imagery from March 2000 with a 2-day delay. It has adaptive training, which the CDR's fixed parameters leave out.
- **PERSIANN-CCS and PDIR-Now:** 0.04° real-time products with latencies of about 1 hour, and 15–60 minutes for PDIR-Now.
- **PERSIANN-CCS-CDR v2.0 and "PERSIANN-CDR V3":** separate 0.04° climate records from 1983 and 1980, also adjusted to GPCP. PERSIANN-CDR V3 uses a deep-learning (U-Net) version of PERSIANN, and CHRS says it was "developed in collaboration with NOAA's Climate Data Record (CDR) Program methodology standards". No source shows that NCEI archives either one.

## Gaps and uncertainties

- **GPCP version by year:** documented only for 2009–2013 (v2.3). NCEI's documents still say v2.2. NCEI's data flow diagram or the CHRS team (via `cdr-ipt-PERSIANN@noaa.gov`) would know.
- **Stage IV training details:** the period and region used are not published in what was read.
- **IRI Data Library copy:** it now needs a sign-in, and a snippet suggested it ends in Sep 2019, so it may be a frozen copy. The AWS S3 and Google Cloud bucket listings were not opened.
- **CHRS headcount:** not published. The CHRS directory lists names (4 faculty, 4 postdocs, 1 administrator, 11 graduate students and 2 visiting scholars), which is not a staff figure.
- **Pages that couldn't be read:** the IRI page (sign-in), the AWS bucket listing, the UCI research page (403) and data.gov (404). NCEI's live landing page and the publisher copies of the papers were read through other copies.

## Sources

- [NCEI, dataset landing page gov.noaa.ncdc:C00854, Wayback capture 2026-10-31](https://web.archive.org/web/20261031104050/https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00854)
- [NCEI, Precipitation – PERSIANN CDR product page](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann)
- [NCEI, PERSIANN CDR User Guide CDRP-GUID-1665 Rev 0, 2025](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf)
- [NOAA CDR Program, C-ATBD CDRP-ATBD-0286 Rev. 2, 2014](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf)
- [NCEI, Data Flow Diagram CDRP-DIA-0351](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/DataFlowDiagram_01B-16.pdf)
- [NCEI, HTTPS archive, 2026 folder listing](https://www.ncei.noaa.gov/data/precipitation-persiann/access/2026/)
- [NCEI, ERDDAP dataset cdr_persiann_by_time_lon_lat](https://www.ncei.noaa.gov/erddap/info/cdr_persiann_by_time_lon_lat/index.html)
- [NCEI, THREDDS catalog](https://www.ncei.noaa.gov/thredds/catalog/satellite/persiann.html)
- [DataCite record, doi:10.7289/V51V5BWQ](https://api.datacite.org/dois/10.7289/V51V5BWQ)
- [CHRS Data Portal, PERSIANN-CDR, V3, CCS-CDR, PDIR-Now and PERSIANN tabs](https://chrsdata.eng.uci.edu/)
- [CHRS HTTPS server, PERSIANN-CDR daily listing](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/)
- [CHRS, About](https://chrs.web.uci.edu/about.php); [CHRS, Directory](https://chrs.web.uci.edu/chrs_directory.php); [CHRS, PERSIANN approach](https://chrs.web.uci.edu/SP_approach.php)
- [Ashouri et al. 2015, BAMS 96:69–83](https://doi.org/10.1175/BAMS-D-13-00068.1), read via the [University at Albany course copy](https://www.atmos.albany.edu/daes/atmclasses/atm305/2015/pdf/Ashouri_et_al_2015_BAMS.pdf)
- [Nguyen et al. 2019, The CHRS Data Portal, Scientific Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC6326112/)
- [Sadeghi et al. 2019, Remote Sensing 11:2755](https://doi.org/10.3390/rs11232755), read via the [NOAA Institutional Repository](https://repository.library.noaa.gov/view/noaa/65498)
- [Sadeghi et al. 2021, PERSIANN-CCS-CDR, Scientific Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC8222311/)
- [Nguyen et al. 2018, HESS, the PERSIANN family](https://hess.copernicus.org/articles/22/5801/2018/)
- [Google Earth Engine, NOAA/PERSIANN-CDR](https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR)
- [AWS Registry of Open Data, NOAA Atmospheric CDRs](https://registry.opendata.aws/noaa-cdr-atmospheric/)
- [Microsoft, AI for Earth NOAA CDR datasets](https://microsoft.github.io/AIforEarthDataSets/data/noaa-cdr.html)
