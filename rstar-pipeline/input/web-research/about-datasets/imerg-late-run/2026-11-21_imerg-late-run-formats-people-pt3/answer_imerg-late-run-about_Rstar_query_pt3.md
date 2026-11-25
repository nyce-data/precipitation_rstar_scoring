# IMERG Late Run: publication, formats (FAIR), institutions, people and software (Part 3)

**Direct answer.** The IMERG Late Run (V07B) is published by NASA in two places. GES DISC is the catalogued archive: half-hourly HDF5 and daily netCDF, each with a DOI, plus OPeNDAP and subsetting services and a cloud copy on AWS. PPS serves near-real-time HDF5 and GeoTIFF ("IMERG GIS") files, with its own DOIs. Every NASA route needs a free sign-up (Earthdata Login or PPS e-mail registration), and no licence is attached to the dataset itself, so each NASA route is only **partly FAIR**. The open third-party Zarr copy by dynamical.org lacks a persistent identifier. The work is split among several organizations: the GSFC IMERG team (lead George Huffman) writes one integrated code, PPS runs it, GES DISC archives, and NOAA CPC, UC Irvine CHRS, GPCC/DWD, JAXA and other sensor agencies supply inputs. The documentation and file specifications are public, but the IMERG production code is not. **Confidence: moderate-high** (high for routes and roles; moderate for the licence, which sources state differently, and for the code findings, which rest on absences).

## Formats and access routes, rated FAIR

| Route (Late Run V07) | Format | Findable | Accessible | Interoperable | Reusable | Rating |
|---|---|---|---|---|---|---|
| GES DISC HTTPS archive, GPM_3IMERGHHL | HDF5 (native, ~2.8 MB/file) | DOI 10.5067/GPM/IMERG/3B-HH-L/07; CMR record | Earthdata Login required | open, documented format; units mm/hr, degrees_east; CF standard names not confirmed | no licence in record; provenance in ATBD | partly FAIR (fails A; R weak) |
| GES DISC daily, GPM_3IMERGDL | netCDF (native) | DOI 10.5067/GPM/IMERGDL/DAY/07; CMR | Earthdata Login | yes | no licence in record | partly FAIR (fails A; R weak) |
| GES DISC OPeNDAP, Harmony subsetters, Giovanni | OPeNDAP; netCDF-4 or GeoTIFF on request; Giovanni CSV/GeoTIFF/ASCII text | through the parent DOI | Earthdata Login (Giovanni: "for full functionality") | yes | no licence | partly FAIR (fails A; R weak) |
| Earthdata Cloud S3 (`gesdisc-cumulus-prod-protected`, us-west-2) | HDF5/netCDF | via CMR/DOI | temporary credentials from Earthdata Login; "Controlled Access" | yes | AWS Registry says CC BY 4.0; NASA policy says CC0 (conflict) | partly FAIR (fails A) |
| PPS near-real-time server (jsimpson, FTPS/HTTPS) | HDF5 | Master List of PPS products; GES DISC DOI not PPS's own (not confirmed) | e-mail registration | yes | no licence | partly FAIR (fails A; F unconfirmed; R weak) |
| PPS IMERG GIS (Late: 30-min, 3-h, 1-day, 3-day, 7-day, monthly) | zipped 2-byte GeoTIFF + ESRI WorldFile | PPS DOIs, e.g. 10.25966/zp54-tb85 (daily) | e-mail registration | documented scaled integers | no licence | partly FAIR (fails A; R weak) |
| Google Earth Engine `NASA/GPM_L3/IMERG_V07` | EE image collection (Late "provisional" mixed with Final) | catalog entry cites the Late DOI | Earth Engine registration; proprietary API | EE only, unless exported | "freely available"; no licence named | partly FAIR (fails A, I, R; findable only) |
| dynamical.org on AWS (`s3://dynamical-nasa-imerg`) | Icechunk Zarr | AWS Registry entry; no DOI shown | open, `--no-sign-request` | open cloud format | CC BY 4.0; NASA source named | partly FAIR (fails F) |

Sources by row: [CMR HHL](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGHHL&version=07), [GES DISC page](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary), [CMR DL](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGDL&version=07), [CMR services](https://cmr.earthdata.nasa.gov/search/services.umm_json), [IMERG Tech Doc 2023, pp. 15–16, 21](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation), [AWS Registry](https://registry.opendata.aws/nasa-gpm3imerghhl/), [PPS README.GIS](https://pps.gsfc.nasa.gov/Documents/README.GIS.pdf), [PPS GIS DOI page](https://doi.org/10.25966/564j-4331), [Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NASA_GPM_L3_IMERG_V07), [dynamical.org](https://registry.opendata.aws/dynamical-nasa-imerg/).

Notes:
- **Login is the common failure.** The IMERG documentation says users must complete "a simple, free, and automatic on-line registration for both PPS and GES DISC" ([Tech Doc, 2023](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation)). PPS asks users to "register an email address" ([PPS README.GIS](https://pps.gsfc.nasa.gov/Documents/README.GIS.pdf)). The protocols themselves are standard: HTTPS, FTPS, OPeNDAP, S3. (High)
- **Licence conflict (unresolved).** Neither CMR's UseConstraints nor the GES DISC landing page names a licence; both point only to EOSDIS data-use guidance ([CMR](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGHHL&version=07)). That guidance says unmarked NASA-mission data "are licensed as Creative Commons Zero (CC0)" ([Earthdata](https://www.earthdata.nasa.gov/engage/open-data-services-software-policies/data-use-guidance)). The AWS Registry entry for the same bucket says "Creative Commons BY 4.0" ([AWS Registry](https://registry.opendata.aws/nasa-gpm3imerghhl/)). NASA's policy is the better authority, but the dataset's own record doesn't apply it, so R is rated weak. (Moderate)
- **What NASA asks instead of a licence.** CMR's quality summary calls the data access policy "freely available" with three caveats: acknowledge the source in a set form naming the GSFC Mesoscale Atmospheric Processes Laboratory and PPS; get a clean copy from an official archive, not a third party; and report errors to the creators ([CMR](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGHHL&version=07)). This gives provenance, but it isn't a named licence.
- **Two figures differ between sources (unresolved):**
  - **Late Run latency.** The ATBD's Table 3 gives "Late (12 hours)", while the ATBD's text and the 2023 Tech Doc say ~14 hours after observation ([ATBD](https://gpm.nasa.gov/resources/documents/imerg-v07-atbd); [Tech Doc](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation)). No source explains the difference.
  - **File size.** GES DISC gives 2.8 MB per half-hourly file ([GES DISC](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary)), while the Tech Doc gives about 10 MB with internal compression for 3IMERGHH. The table uses GES DISC's current figure.
- **Coverage:** the GES DISC Late archive runs from 1998-01-01 to 2026-11-20 (as read on 2026-11-21).
- **Text and GeoTIFF:** no stored text product for the Late Run was found. Text (ASCII/CSV) comes only from Giovanni. GeoTIFF comes from PPS GIS files or on-request conversion. PPS keeps Early and Late files "until a new version of the Early and Late IMERG algorithm replaces them" ([README.GIS](https://pps.gsfc.nasa.gov/Documents/README.GIS.pdf)).

## Institutions: several organizations, each with its own part

- **IMERG team, NASA GSFC (Code 612, Mesoscale Atmospheric Processes Lab):** designs and maintains the algorithm. "All of the Runs share a common code"; "the entire package is assembled and transferred to PPS for integration and testing" ([ATBD, Aug 2026](https://gpm.nasa.gov/resources/documents/imerg-v07-atbd)). (High)
- **PPS, NASA GSFC (Code 619):** "The Early and Late Runs are executed in the PPS Real Time (RT) processing system". PPS makes the Level 1C and GPROF inputs, distributes NRT files and GIS files, and gets JMA forecasts from JAXA and GEOS FP fields ([ATBD](https://gpm.nasa.gov/resources/documents/imerg-v07-atbd); [Tech Doc](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation)). George Mason University's CEOSR group "develops job-control, archiving, and distribution software" for PPS ([GMU CEOSR](https://ceosr.science.gmu.edu/microwave-remote-sensing-group/), read through a subagent). (High)
- **GES DISC, NASA GSFC:** archive of record, DOIs, OPeNDAP, Giovanni and the cloud copy ([CMR](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGHHL&version=07)). It does not process IMERG.
- **Measurement collectors:** the sensor agencies compute Level 1B: "NOAA and EUMETSAT data are accessed through NOAA, DMSP from NRL Monterey, and the Japanese AMSR2 through NASA, and GPM DPR and GMI within GPM" ([Tech Doc](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation)). **JAXA** built the DPR (with NICT) and launched GPM ([JAXA](https://global.jaxa.jp/projects/sat/gpm/), read through a subagent).
- **NOAA CPC:** produces the merged 4-km geo-IR "under the direction of P. Xie" and forwards it to PPS. (High)
- **UC Irvine CHRS** (Braithwaite, Hsu, Nguyen): supplies the PDIR method, and distributes PDIR-Now itself through its CHRS Data Portal ([Nguyen et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8216223/)). For IMERG, the ATBD's wording (CPC forwards IR to PPS for "PDIR computation routines") implies that PPS computes the IR estimates, but no source states it. (Moderate)
- **JAXA** also works with PPS on operations: "PPS and JAXA MOS have changed the primary source of the GPM core satellite ephemeris data" from the 1 March 2025 data date ([PPS contacts](https://storm.pps.eosdis.nasa.gov/storm/PPSContacts.jsp)).
- **GPCC at DWD** (Becker, Schneider): the gauge analysis enters the Final Run. The Late Run gets only "a monthly climatological concluding calibration" derived from the Final ([GES DISC/AWS description](https://registry.opendata.aws/nasa-gpm3imerghhl/); [FAQ 2025](https://gpm.nasa.gov/sites/default/files/2025-02/FAQ%20for%20IMERG%20V07%20Applications%20Users_202502.pdf)). The 2023 Tech Doc's line that the Final's monthly calibration is "not applied" to Early and Late refers to the direct monthly adjustment, so the two don't conflict.

## People

- **George J. Huffman** (NASA GSFC Code 612): IMERG lead and prepares the ATBD; GPM Project Scientist since 2022; Lab Chief ([ATBD](https://gpm.nasa.gov/resources/documents/imerg-v07-atbd); [GSFC bio](https://science.gsfc.nasa.gov/sci/bio/george.huffman), via a subagent).
- **ATBD co-authors (13 Aug 2026):** David T. Bolvin, Robert Joyce and Eric J. Nelkin (SSAI, at GSFC); Jackson Tan (UMBC, GSFC 613); Dan Braithwaite, Kuolin Hsu, Phu Nguyen and Soroosh Sorooshian (UC Irvine); Owen A. Kelley; Daniel C. Watters; B. Jason West; Pingping Xie (NOAA CPC). Employers are from Huffman's 2024 slides and the Tech Doc ([slides](https://ntrs.nasa.gov/api/citations/20240011596/downloads/20240011596%20Huffman%20G%20slides.pdf)). Christopher Kidd (UMD), listed in 2023, is not on the 2026 list.
- **Erich F. Stocker** (GSFC Code 619): GPM Deputy Project Scientist for Data and PPS Project Manager, and PPS's "NASA Official" ([PMM team page](https://gpm.nasa.gov/science/pmm-science-team), dated 2019; [PPS contacts](https://storm.pps.eosdis.nasa.gov/storm/PPSContacts.jsp), updated 02/21/2024).
- **NASA HQ:** Will McCarty, GPM Program Scientist; Craig Ferguson, deputy program scientist for GPM ([McCarty](https://science.nasa.gov/people/will-mccarty/), [Ferguson](https://science.nasa.gov/people/craig-ferguson/), via a subagent).
- **GES DISC:** Mahabal Hegde (DAAC Manager), Gary Alcott (Operations Lead), Jennifer Wei (DAAC Scientist); Zhong Liu (GMU) supports GPM data ([GES DISC people](https://www.earthdata.nasa.gov/centers/gesdisc-daac/people)).
- **Headcount:** none is published for the IMERG team, PPS or GES DISC. The nearest evidence is the 13-person ATBD author list and the five "data set creators" named in the Tech Doc. (Moderate: an absence, across the pages read.)

## Software: is it public?

| Program | Source code | Documentation / spec | Licence |
|---|---|---|---|
| IMERG (merging, KF morphing, SHARPEN, calibrations) | **not public**: no release location in the ATBD; 0 IMERG repos in NASA's GitHub org | ATBD (2026), Tech Doc (2023), FAQ, release notes, GPM file spec: public | none |
| GPROF (CSU) | GPROF-NN on [GitHub](https://github.com/simonpf/gprof_nn), MIT; the GPROF V08 preprint cites its `gprof_v8` branch; not stated to be PPS's operational build | GPROF ATBD; V08 preprints | MIT (repo) |
| Level 1C / XCAL | not found; GSICS calibration tables page unreachable | [L1C ATBD v1.9](https://arthurhou.pps.eosdis.nasa.gov/Documents/L1C_ATBD_v1.9_GPMV07.pdf) public | none found |
| PDIR-Now (CHRS) | not found | [Nguyen et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8216223/) | none found |
| CPC merged 4-km IR | not found | GES DISC README (GPM_MERGIR) | none found |
| SPEEDe (PPS bad-orbit detection) | not checked: paper's code statement behind a bot check | Tan et al. 2024, GRL | unknown |
| GEOS FP (motion vectors) | GEOS model on [GitHub](https://github.com/GEOS-ESM/GEOSgcm); FP configuration not confirmed | GMAO pages | Apache-2.0 (repo) vs "NOSA 1.1 or later" ([GMAO](https://gmao.gsfc.nasa.gov/geos-systems/accessing-geos-software/)) |
| PPS user toolkit TKIO (C/Fortran) | downloadable from PPS | Toolkit User's Guide, file specs ([PPS docs](https://arthurhou.pps.eosdis.nasa.gov/ppsdocuments.html)) | not stated |
| Third-party readers | [GPM-API](https://github.com/ghiggi/gpm_api) (MIT); GES DISC tutorials | | MIT / not stated |

This sits awkwardly with NASA policy. ESDS requires software from government-funded development "to be made available to the public as Open-Source Software" ([Earthdata OSS policy](https://www.earthdata.nasa.gov/engage/open-data-services-software-policies/open-source-software-policy)). SPD-41a says mission software "shall be developed openly in a publicly accessible, version-controlled platform", but it also says mission software "is often restricted software and shall not be shared openly unless approved for release" ([SPD-41a](https://science.nasa.gov/wp-content/uploads/2023/08/smd-information-policy-spd-41a.pdf)). No release decision, exemption or plan for IMERG was found. (Moderate: absence of evidence; the GitHub API was refused, and only the nasa organization was searched.)

## Gaps and uncertainties

- **The budget limited this run, and two subagents stalled.** The formats and software subagents waited on permission prompts from about 05:00 and 05:06 and were stopped at the research stop. The formats findings come from their saved files plus my own browser reads.
- **Not checked:**
  - CF `standard_name` attributes inside the files;
  - whether PPS's NRT HDF5 has its own DOI;
  - Worldview/GIBS imagery;
  - the SPEEDe code statement (AGU bot check);
  - the licence of the `gprof_v8` branch;
  - the JAXA GPM handbook (PDF; sandbox-refused host).
- **Who holds the missing facts:**
  - code release: the PPS helpdesk (helpdesk@pps-mail.nascom.nasa.gov) or the IMERG team, on request;
  - the licence statement: GES DISC (gsfc-help-disc@lists.nasa.gov);
  - headcounts: not published; GSFC Code 619 and 612 management.
- `check-by-hand.md` lists 7 pages; `sites-to-trust.md` lists 5 hosts the sandbox refused (api.github.com, arxiv.org, developers.google.com, raw.githubusercontent.com, www.eorc.jaxa.jp), which you can check against your sandbox's allowed domains.

## Sources

- [NASA GPM, IMERG V07 ATBD, 13 Aug 2026](https://gpm.nasa.gov/resources/documents/imerg-v07-atbd)
- [NASA GPM, IMERG V07 Technical Documentation, 2023](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation)
- [NASA GPM, FAQ for IMERG V07 Applications Users, 2025](https://gpm.nasa.gov/sites/default/files/2025-02/FAQ%20for%20IMERG%20V07%20Applications%20Users_202502.pdf)
- [NASA CMR, GPM_3IMERGHHL V07 record](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGHHL&version=07)
- [NASA CMR, GPM_3IMERGDL V07 record](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGDL&version=07)
- [NASA CMR, services for GPM_3IMERGHHL](https://cmr.earthdata.nasa.gov/search/services.umm_json)
- [GES DISC, GPM_3IMERGHHL 07 landing page](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary)
- [PPS, README.GIS (Kelley, 2023)](https://pps.gsfc.nasa.gov/Documents/README.GIS.pdf)
- [PPS, IMERG GIS DOI landing page](https://doi.org/10.25966/564j-4331)
- [PPS, Contacts](https://storm.pps.eosdis.nasa.gov/storm/PPSContacts.jsp)
- [PPS, STORM Tools](https://storm.pps.eosdis.nasa.gov/storm/Tools.jsp)
- [PPS, documentation page](https://arthurhou.pps.eosdis.nasa.gov/ppsdocuments.html)
- [NASA GPM, TKIO 3.9 announcement](https://gpm.nasa.gov/data/news/tkio-annoucement-pps-announcing-new-tkio-39-release)
- [PPS, L1C ATBD v1.9](https://arthurhou.pps.eosdis.nasa.gov/Documents/L1C_ATBD_v1.9_GPMV07.pdf)
- [NASA GPM, PMM Science Team](https://gpm.nasa.gov/science/pmm-science-team)
- [NASA Earthdata, People of GES DISC](https://www.earthdata.nasa.gov/centers/gesdisc-daac/people)
- [NASA Earthdata, GES DISC fact sheet 2022](https://www.earthdata.nasa.gov/sites/default/files/2022-01/GESDISC22719_FactSheet.pdf)
- [Huffman, IMERG V07 slides, 2024 (NTRS)](https://ntrs.nasa.gov/api/citations/20240011596/downloads/20240011596%20Huffman%20G%20slides.pdf)
- [NASA GSFC, George Huffman bio](https://science.gsfc.nasa.gov/sci/bio/george.huffman) (read through a subagent)
- [NASA, Will McCarty](https://science.nasa.gov/people/will-mccarty/) and [Craig Ferguson](https://science.nasa.gov/people/craig-ferguson/) (read through a subagent)
- [JAXA, About GPM/DPR](https://global.jaxa.jp/projects/sat/gpm/) (read through a subagent)
- [GMU CEOSR, Microwave Remote Sensing Group](https://ceosr.science.gmu.edu/microwave-remote-sensing-group/) (read through a subagent)
- [NASA Earthdata, Data Use Guidance](https://www.earthdata.nasa.gov/engage/open-data-services-software-policies/data-use-guidance)
- [NASA Earthdata, Open-Source Software Policy](https://www.earthdata.nasa.gov/engage/open-data-services-software-policies/open-source-software-policy)
- [NASA SMD, SPD-41a, 2023](https://science.nasa.gov/wp-content/uploads/2023/08/smd-information-policy-spd-41a.pdf)
- [AWS Registry, GPM_3IMERGHHL at GES DISC](https://registry.opendata.aws/nasa-gpm3imerghhl/)
- [AWS Registry, dynamical.org NASA IMERG Zarr](https://registry.opendata.aws/dynamical-nasa-imerg/)
- [Google Earth Engine, NASA/GPM_L3/IMERG_V07](https://developers.google.com/earth-engine/datasets/catalog/NASA_GPM_L3_IMERG_V07)
- [GitHub search, org:nasa IMERG](https://github.com/search?q=org%3Anasa+IMERG&type=repositories)
- [GitHub search, IMERG](https://github.com/search?q=IMERG&type=repositories&s=stars&o=desc)
- [simonpf/gprof_nn](https://github.com/simonpf/gprof_nn) (read through a subagent)
- [GEOS-ESM/GEOSgcm](https://github.com/GEOS-ESM/GEOSgcm) (read through a subagent)
- [GMAO, Accessing GEOS Software](https://gmao.gsfc.nasa.gov/geos-systems/accessing-geos-software/)
- [ghiggi/gpm_api](https://github.com/ghiggi/gpm_api) (read through a subagent)
- [Nguyen et al. 2020, PDIR-Now (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8216223/)

Saved in [`web_search_results/2026-11-21_imerg-late-run-formats-people-pt3/`](./): this answer, `research-record.json`, `method.md`, `check-by-hand.md` and `sites-to-trust.md`.
