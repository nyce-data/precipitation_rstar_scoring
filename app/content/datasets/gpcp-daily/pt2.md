**Direct answer.** Both current GPCP daily products get light quality control, done mostly by machine. The 1DD V1.3 record screens its inputs automatically, and its producers review each month's output by hand against climatologies. V3.3 gets the same kind of diagnostic review. Neither product carries a per-pixel QC flag or error field: bad or absent inputs are left out, or the area is set to missing. Independent validation is thin and mostly old. For V3.3 it is still "planned".

All the main routes serve open, CF-labelled netCDF-4 with DOIs. NCEI's HTTPS and S3 copies and NCAR GDEX's copies are the most FAIR. GES DISC needs an Earthdata Login and names no licence.

The only production code published is NCEI's 2017 package for V1.3, offered "for reference only". It has no licence file, and re-use rights are left to the copyright holders named in each file. No V3.2 or V3.3 code is published.

Overall confidence: **moderate**. The documentation is clear, but some licence and login details per route were not confirmed.

## Quality control

**1DD V1.3** (NOAA CDR 01B-35, produced by UMD/ESSIC). Confidence: high.
- **Output review (manual):** "The diagnostic analyses and plots of the output products are performed every month, with comparison to climatologies." In the C-ATBD, Exception Handling and Algorithm Validation both read "Not applicable" ([NOAA NCEI, C-ATBD 01B-35, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)).
- **Input gate (automated):** if inputs are unavailable "or do not pass quality control tests, the calculation and submission are postponed" (same source).
- **Output test (automated):** the code package's README describes input-check modules and a post-run test for anomalous zero values ([NCEI SourceCode_01B-35, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/SourceCode_01B-35.tar.gz)).
- **Pixel screening (automated):** the GPROF SSMIS step rejects brightness temperatures outside 50–325 K, latitudes beyond 70°N/S and invalid surface types (`qualctrl.F`, same package).
- **Outlier audit:** the original method deleted TMPI outliers with a subjectively chosen cutoff and smooth-filled the gaps. In the paper's example month, the cutoff excluded the highest 10% of boxes and deleted the outlier 1% of values ([Huffman et al. 2001](https://ntrs.nasa.gov/api/citations/20000068519/downloads/20000068519.pdf)). Whether V1.3 still does this is not stated.

**V3.2/V3.3 Daily** (NASA MEaSUREs; GSFC, UMD, U. Arizona). Confidence: high.
- **Review (manual):** diagnostic plots for selected months, compared with climatologies and V3.2. Input or processing errors are "corrected or documented" ([GES DISC, V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)).
- **Missing high-latitude input:** when TOVS or AIRS data are missing, the areas outside 55°N–S are "set to missing", for example 1–18 Nov 2003 ([GES DISC, V3.3 Daily README](https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.3/doc/README.GPCPV3.3_Daily.pdf)).
- **Range caps (automated):** IMERG values are thresholded at 0.24 mm/d, and daily-to-monthly scaling ratios are capped at 0.2–4.0 (same README).
- **No flags:** files hold only `precip` and `probability_liquid_phase`, with no error or QC field.

**Inputs** (QC done by their own producers). Confidence: moderate.
- **Gauges:** GPCC (DWD) runs "automatic and intensive manual quality-control" and keeps quality flags internally ([DWD GPCC, 2011](https://opendata.dwd.de/climate_environment/GPCC/PDF/GPCC_intro_products_v2011.pdf)). Gauges reach both daily products only through the monthly scaling.
- **SSM/I:** RSS quality-controls and intercalibrates the SSM/I data used by V1.3 (C-ATBD).
- **Not researched:** QC of IMERG (which has its own quality index), CPC merged IR and TOVS/AIRS.

## Validation and program reviews

Confidence: moderate.
- **1DD V1.3:**
  - Checked against Oklahoma Mesonet gauges, January 1997 to December 1998, with a correlation of 0.73 ([Huffman et al. 2001](https://ntrs.nasa.gov/api/citations/20000068519/downloads/20000068519.pdf)).
  - Later checked against high-latitude gauges (Bolvin et al. 2009, cited by the [Climate Data Guide](https://climatedataguide.ucar.edu/climate-data/gpcp-daily-global-precipitation-climatology-project); not read).
  - No uncertainty estimate is provided.
- **Ocean study, V1.3 against V3.2:** an independent comparison with 58 Passive Aquatic Listeners found V3.2 better than V1.3 for daily rain occurrence and intensity ([Li et al. 2023](https://experts.arizona.edu/en/publications/performance-of-gpcp-daily-products-over-oceans-evaluation-using-p/); abstract only).
- **V3.3:** the ATBD lists validation against MRMS and Pacific atoll gauges as future work. The release notes compare it only with V3.2 and IMERG V07B ([GES DISC, V3.3 Release Notes](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)). A developer poster lists daily gauge-network validation as future work too ([Nelkin et al., AGU 2021](https://ntrs.nasa.gov/api/citations/20220000683/downloads/Nelkin_AGU21.pdf)).
- **NOAA CDR program reviews:** V1.3 has a C-ATBD (CDRP-ATBD-0913, Rev. 0) and a maturity matrix dated 2017-08-14 ([NCEI Maturity Matrix 01B-35](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/MaturityMatrix_01B-35.pdf)).
  - **Scores (low confidence):** they are shown only by cell colour. My reading of the shading is Software Readiness 5, Metadata 5, Documentation 4, Product Validation 3, Public Access 6, Utility 6.
  - **V3.3:** no maturity matrix or operational readiness review was found, even though NCEI publishes it as a CDR.

## Processing

Confidence: high.
- **V1.3:**
  - Between 40°N and 40°S it uses TMPI: a geo-IR threshold matched to SSM/I-SSMIS GPROF rain frequency, with one rain rate per grid box so that each month sums to GPCP Monthly V2.3.
  - Gaps are filled with leo-IR. TOVS/AIRS is rescaled to the monthly at high latitudes.
  - Code: shell, Fortran, C and MATLAB on RHEL 6.7 (C-ATBD).
- **V3.3:**
  - IMERG V07 Final, averaged to 0.5° daily, between 55°N and 55°S.
  - TOVS/AIRS histogram-matched to IMERG and bias-adjusted to the monthly at higher latitudes, with "feathering" at 55°.
  - Every day ratio-scaled to sum to the V3.3 Monthly.
  - The flowchart's step names are COMPHIST, AIRS2IMERG, CORR_T, FUSE, SCALEME, BLD_NETCDF and others (ATBD; [README](https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.3/doc/README.GPCPV3.3_Daily.pdf)).
  - The V3.3 Daily ATBD was last revised 2026-06-12, and the README 2025-05-28.
  - V3.2 code ran in C shell, Fortran and Python on CentOS 7 ([V3.2 ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf)).

## Can the public inspect and use the software?

Confidence: moderate.
- **V1.3 code is public:** `SourceCode_01B-35.tar.gz`, 15,408,824 bytes, dated 2017-09-18, is in NCEI's [CDR folder](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/). It holds about 150 files, and NCEI calls it "for reference only" and "not intended to be portable".
- **Licence:**
  - NCEI's use agreement makes the data open but puts the software outside that policy: permission "should be sought from the software's copyright owner identified within its source code" ([NCEI Use Agreement 01B-35](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/UseAgreement_01B-35.pdf)).
  - The archive has no licence file. One C file is declared public domain; the QC Fortran file carries no notice. Most files' headers were not read.
- **V3.2/V3.3 code is not published.** None was found at NCEI, at GES DISC or on GitHub. The README offers only generic netCDF tools and Giovanni.
- **Conflict (unresolved):** NCEI's V3.3 metadata record links the same 2017 V1.3 tarball and labels it "CDR Source Code (GPCP Daily v3.3)" ([NCEI ISO C01726](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01726)). The tarball's README and modules (GPROF V2004, IR threshold) are V1.3's, so the label looks like a metadata carry-over.
- **Inputs:** IMERG's and GPCC's production code was not checked.

## Formats and access routes (FAIR)

| Route | Version | Format, conventions | Identifier and catalog | Protocol, login | Licence | Rating |
|---|---|---|---|---|---|---|
| NCEI HTTPS directory | 1DD V1.3 | netCDF-4, CF and ACDD (version not stated) | DOI 10.7289/V5RX998Z; NCEI catalog | HTTPS, no login | NCEI use agreement: data open, no restrictions | **FAIR** |
| NCEI S3 archive (archive.data.noaa.gov) | V3.3 CDR | netCDF-4, CF and ACDD | DOI 10.25921/9b5m-ka77; NCEI and data.gov | S3/HTTPS, no login | CC0 1.0 (data.gov) | **FAIR** (landing page unreadable) |
| AWS NODD bucket noaa-cdr-precip-gpcp-daily-pds | NCEI copies | presumably as NCEI; not listed | AWS registry; no own DOI | anonymous S3 | NOAA open-data terms | **probably FAIR** (contents not checked) |
| NASA GES DISC (HTTPS, OPeNDAP, S3) | V3.2, V3.3 | netCDF-4, CF-1.5, `precip` in mm/day | DOI 10.5067/MEASURES/GPCP/DATA305 and DATA307; CMR | Earthdata Login required | no licence named in CMR or README | **partly FAIR**: fails A (login); R weak (no named licence) |
| NCAR GDEX d728007, d728009 | V1.3, V3.2 | netCDF4 | DOI 10.5065/ZGJD-9B02, 10.5065/X4KB-XJ98 | HTTPS, Globus, THREDDS; the access page names no login (not tested) | CC BY 4.0 | **FAIR** if downloads are open (likely; not tested) |
| Copernicus CDS | V1.3, V3.2, V3.3 | netCDF-4, CF-1.6 + ACDD-1.3 (V1.3), CF-1.5 (V3) | CDS catalog | login and acceptance of both licences required ("Login/register to accept licences") | GPCP product licence; NASA GES DISC data licence (not Creative Commons) | **partly FAIR**: fails A (login) |
| obs4MIPs/ESGF, Google Earth Engine | n/a | not confirmed | not confirmed | not confirmed | not confirmed | not rated |

Sources by row:
- **NCEI HTTPS:** [NCEI ISO C00999](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00999) and the [HTTPS directory](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/).
- **NCEI S3:** [NCEI ISO C01726](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01726) and [data.gov](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-the-global-precipitation-climatology-project-gpcp-daily-version-3-3).
- **AWS:** the [AWS registry](https://registry.opendata.aws/noaa-cdr-atmospheric/).
- **GES DISC:** the [dataset page](https://disc.gsfc.nasa.gov/datasets/GPCPDAY_3.3/summary), the [Data Access how-to](https://disc.gsfc.nasa.gov/data-access), [CMR](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPCPDAY) and the README.
- **GDEX:** [d728007](https://gdex.ucar.edu/datasets/d728007/) and [d728009](https://gdex.ucar.edu/datasets/d728009/).
- **CDS:** the [dataset page](https://cds.climate.copernicus.eu/datasets/satellite-precipitation?tab=overview) and the [GPCP licence](https://ewds.climate.copernicus.eu/licences/global-precipitation-climatology-project).

**Licences differ by route (unresolved, a difference in scope):** CC0 (data.gov), CC BY 4.0 (GDEX), GPCP's own licence (CDS), NCEI's "no restrictions" wording, and none named at GES DISC.

**V1.3 status (from Part 1):** data.gov labels V1.3 superseded, yet NCEI still adds V1.3 files for 2026.

## Gaps

- **Maturity scores:** read from colour only.
- **Login and catalog rules not confirmed:**
  - whether GDEX downloads need a login (the access page names none);
  - NCEI's THREDDS/OPeNDAP path;
  - obs4MIPs/ESGF and Earth Engine copies.
- **DOIs:** the DataCite lookups failed, so the DOIs come from the archives' own pages.
- **Not researched:**
  - QC of IMERG, CPC merged IR and TOVS/AIRS;
  - Bolvin et al. 2009 and the full text of Li et al. 2023.
- **Software licence:** only one or two of the ~150 files' copyright notices were read. The holders, UMD and NASA GSFC (for GPROF), would have to say what re-use is allowed.
- **Time budget:** research stopped at the 30-minute budget, and the DuckDuckGo pass did not run.

## Sources

Producer documents:
- [NOAA NCEI / UMD ESSIC, GPCP Daily C-ATBD 01B-35, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)
- [NOAA NCEI, GPCP Daily Maturity Matrix 01B-35, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/MaturityMatrix_01B-35.pdf)
- [NOAA NCEI, Fair Use of NOAA's CDR Data Sets, Algorithms and Documentation, 01B-35](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/UseAgreement_01B-35.pdf)
- [NASA GES DISC, GPCP V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)
- [NASA GES DISC, GPCP V3.2 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf)
- [NASA GES DISC, GPCP V3.3 Release Notes](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)
- [NASA GES DISC, README for GPCP V3.3 Daily, 2025](https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.3/doc/README.GPCPV3.3_Daily.pdf)

Code:
- [NOAA NCEI, SourceCode_01B-35.tar.gz, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/SourceCode_01B-35.tar.gz)
- [NOAA NCEI, CDR document folder for GPCP Daily](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/)

Archive and catalog records:
- [NOAA NCEI, ISO metadata C01726 (V3.3)](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01726)
- [NOAA NCEI, landing page C00999 (V1.3), Wayback copy](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00999)
- [NOAA NCEI, GPCP daily HTTPS directory](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/)
- [data.gov, NOAA CDR of GPCP Daily Version 3.3](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-the-global-precipitation-climatology-project-gpcp-daily-version-3-3)
- [AWS Registry of Open Data, NOAA CDR atmospheric](https://registry.opendata.aws/noaa-cdr-atmospheric/)
- [NASA GES DISC, GPCPDAY 3.3 dataset page](https://disc.gsfc.nasa.gov/datasets/GPCPDAY_3.3/summary)
- [NASA GES DISC, Data Access how-to](https://disc.gsfc.nasa.gov/data-access)
- [NASA CMR, GPCPDAY collections](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPCPDAY)
- [NCAR GDEX, d728007](https://gdex.ucar.edu/datasets/d728007/)
- [NCAR GDEX, d728009](https://gdex.ucar.edu/datasets/d728009/)
- [Copernicus CDS, satellite-precipitation](https://cds.climate.copernicus.eu/datasets/satellite-precipitation?tab=overview)
- [Copernicus CDS, satellite-precipitation download tab](https://cds.climate.copernicus.eu/datasets/satellite-precipitation?tab=download)
- [NCAR GDEX, d728007 Data Access](https://gdex.ucar.edu/datasets/d728007/dataaccess/)
- [Copernicus, GPCP product licence](https://ewds.climate.copernicus.eu/licences/global-precipitation-climatology-project)

Studies and inputs:
- [Huffman et al., One-Degree Daily, J. Hydrometeor. 2001 (NTRS manuscript)](https://ntrs.nasa.gov/api/citations/20000068519/downloads/20000068519.pdf)
- [Li et al., GRL 2023, Passive Aquatic Listeners](https://experts.arizona.edu/en/publications/performance-of-gpcp-daily-products-over-oceans-evaluation-using-p/) (abstract only)
- [Nelkin et al., AGU 2021 poster](https://ntrs.nasa.gov/api/citations/20220000683/downloads/Nelkin_AGU21.pdf)
- [UCAR Climate Data Guide, GPCP Daily](https://climatedataguide.ucar.edu/climate-data/gpcp-daily-global-precipitation-climatology-project)
- [DWD GPCC, Introduction to products, 2011](https://opendata.dwd.de/climate_environment/GPCC/PDF/GPCC_intro_products_v2011.pdf)
