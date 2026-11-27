"""Build the PERSIANN-CDR Daily R* categorization JSON (first pass, 2026-11-27).

Hand-sorted evidence from every answer file in rstar-pipeline/input/web-research/ that bears on PERSIANN-CDR Daily
(v01r01, the NOAA CDR made by UC Irvine's CHRS and archived at NCEI, DOI 10.7289/V51V5BWQ):
- the six about-datasets/persiann-cdr-daily runs (about-pt1, qc-formats-pt2, about-pt3 on funding, news-pt4,
  inputs-pt5 and satellites-pt6);
- the two archives/noaa-ncei runs (A1 threats; A2 resilience, which covers PERSIANN-CDR by name);
- archives/uci-chrs (A2 resilience run on CHRS's own data site);
- instruments/noaa-satellites (GOES, DMSP, POES; geostationary IR is the direct input, the polar orbiters reach
  it through GPCP's monthly analysis);
- for NODD-wide and NCEI-wide facts only, the GHCN-Daily repository runs pt7 and pt9;
- for one low-confidence inference on substitutes, GPCP Daily's pt7 Run 2 (which lists PERSIANN-CDR among GPCP's
  partial substitutes).
Left out: instruments/nasa-satellites (about GPM and IMERG; PERSIANN-CDR uses no NASA sensor directly, and its one
NASA sensor through GPCP, Aqua AIRS, is covered by inputs-pt5) and instruments/noaa-rain-gauges (gauges reach it only
through GPCC inside GPCP).
Not yet run: the pt7 people-and-production query (datasets-gap-queries/persiann-cdr-daily_gap-queries/), so P-1,
P-2 and P-4, the funding of production, and substitute datasets were never searched; their gaps say so.

Shared people: Braithwaite, Hsu, Nguyen and Sorooshian (CHRS) are also co-authors of IMERG's ATBD (PDIR-Now, an IMERG
input, is CHRS's method).

Filing rules: rstar-pipeline/input/framework/rstar-categorization-decisions.md. Steps:
rstar-pipeline/processing/instructions/categorize-dataset-instructions.md.
Markdown links [label](url) in the text become <a> tags (rstar_common.py does the writing and scoring).

Run:  python3 rstar-pipeline/processing/scripts/categorize/build_persiann-cdr-daily.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rstar_common import H, M, L, write_categories  # noqa: E402

# data-source values: the research run folder names
PT1 = "2026-11-19_persiann-cdr-daily-about-pt1"
PT2 = "2026-11-19_persiann-cdr-daily-qc-formats-pt2"
PT3 = "2026-11-19_persiann-cdr-daily-about-pt3"
PT4 = "2026-11-19_persiann-cdr-daily-news-pt4"
PT5 = "2026-11-19_persiann-cdr-daily-inputs-pt5"
PT6 = "2026-11-19_persiann-cdr-daily-satellites-pt6"
NCEI = "2026-11-17_noaa-ncei-threats"
NCEI_A2 = "2026-11-23_A2_Rstar_query-noaa_ncei"
UCI = "2026-11-27_uci-chrs-resilience"  # archives/uci-chrs A2 run
NOAA_SAT = "2026-11-18_noaa-satellite-precip-threats"
GH_REPO = "2026-11-22_ghcn-daily-repository-pt7"
GH_RRS = "2026-11-23_ghcn-daily-repository-resilience-pt9"
GPCP_PT7B = "2026-11-24_gpcp-daily-calibration-copies-pt7"

# Each evidence item is (confidence, source run, text, stance[, repository for RRS]); stance toward the
# subcategory's statement: F = for, A = against, C = context (not directly tied, or doesn't show it true or false).
# Each gap is (status, text): S = searched and none found, P = not public, U = not searched.

# Repository names (match DATASET below)
NCEI_R = "NOAA NCEI"
CHRS = "UC Irvine CHRS data site"
NODD = "AWS, Google Cloud and Azure (NODD)"

# Frequently cited pages
CATBD = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf"
GUIDE = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UserGuide_01B-16.pdf"
DOCS = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/"
SRC_TAR = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/SourceCode_01B-16.tar.gz"
USE_AGR = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/UseAgreement_01B-16.pdf"
DFD = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/DataFlowDiagram_01B-16.pdf"
DSMR12 = "https://repository.library.noaa.gov/view/noaa/33336"
LANDING = "https://web.archive.org/web/20261031104050/https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00854"
PRODUCT = "https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann"
NCEI_2026 = "https://www.ncei.noaa.gov/data/precipitation-persiann/access/2026/"
ERDDAP = "https://www.ncei.noaa.gov/erddap/info/cdr_persiann_by_time_lon_lat/index.html"
ERDDAP_DAS = "https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.das"
PAUSE = "https://www.ncei.noaa.gov/node/8306"
PAUSE_WB = "https://web.archive.org/web/20250913132027/https://www.ncei.noaa.gov/node/8306"
AGG = "https://www.ncei.noaa.gov/thredds/dodsC/ncFC/cdr/persiann-fc/PERSIANN:_aggregation_best.ncd"
ASHOURI = "https://doi.org/10.1175/BAMS-D-13-00068.1"
NGUYEN19 = "https://pmc.ncbi.nlm.nih.gov/articles/PMC6326112/"
SADEGHI19 = "https://repository.library.noaa.gov/view/noaa/65498"
CHRS_PORTAL = "https://chrsdata.eng.uci.edu/"
CHRS_DAILY = "https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/"
CHRS_YEARLY = "https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/yearly/"
CHRS_ABOUT = "https://chrs.web.uci.edu/about.php"
CHRS_DIR = "https://chrs.web.uci.edu/chrs_directory.php"
UCI_OR = "https://research.uci.edu/center/center-for-hydrometeorology-and-remote-sensing-chrs/"
UCI_CENTERS = "https://research.uci.edu/centers-institutes/"
UCI_MAR26 = "https://research.uci.edu/wp-content/uploads/or-update-march-2026.pdf"
UCI_TOWNHALL = "https://research.uci.edu/wp-content/uploads/250521-Research-Town-Hall_Final.pdf"
UCI_NEWS = "https://news.uci.edu/2026/04/22/water-warming-and-a-world-at-risk/"
OIT = "https://www.oit.uci.edu/services/infrastructure/data-backups/"
OIT_SLA = "https://www.oit.uci.edu/files/2021/07/Data-Backup-and-Recovery-SLA.pdf"
IS12 = "https://security.ucop.edu/files/documents/policies/uc-is-12-archived.pdf"
THAKUR = "https://storage.courtlistener.com/recap/gov.uscourts.cand.450653/gov.uscourts.cand.450653.211.5.pdf"
CPO_AW = "https://api.usaspending.gov/api/v2/awards/ASST_NON_NA23OAR4310443_1330/"
CPO_NEWS = "https://cpo.noaa.gov/noaa-climate-program-offices-climate-observations-and-monitoring-program-awards-1-2-million-for-new-precipitation-data-development-and-analysis/"
CICS_AW = "https://api.usaspending.gov/api/v2/awards/ASST_NON_NA09NES4400006_1330/"
CISESS_AW = "https://api.usaspending.gov/api/v2/awards/ASST_NON_NA24NESX432C0001_1330/"
CISESS_UPD = "https://cisess.umd.edu/updates-to-a-global-precipitation-product/"
AMS19 = "https://ams.confex.com/ams/2019Annual/webprogram/Paper352356.html"
EGU_PUNET = "https://meetingorganizer.copernicus.org/EGU26/EGU26-2633.html"
DRP = "https://portal.datarescueproject.org/datasets/precipitation---persiann-climate-data-record-cdr/"
GEE = "https://developers.google.com/earth-engine/datasets/catalog/NOAA_PERSIANN-CDR"
AWS_REG = "https://registry.opendata.aws/noaa-cdr-atmospheric/"
AZURE = "https://microsoft.github.io/AIforEarthDataSets/data/noaa-cdr.html"
AWS_LIST = "https://noaa-cdr-precip-persiann-pds.s3.amazonaws.com/?list-type=2&max-keys=5"
IRI = "https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.CDR/.PERSIANN-CDR/.v01r01/"
DATACITE = "https://api.datacite.org/dois/10.7289/V51V5BWQ"
DATAGOV = "https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-precipitation-estimation-from-remotely-sensed-information-"
# GridSat-B1, GPCP and the satellites
GRIDSAT_ATBD = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/AlgorithmDescription_01B-02.pdf"
GRIDSAT_2026 = "https://www.ncei.noaa.gov/thredds/catalog/cdr/gridsat/2026/catalog.html"
GRIDSAT_OCT26 = "https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/2026/GRIDSAT-B1.2026.10.01.12.v02r01.nc.das"
ISCCP_B1 = "https://www.ncei.noaa.gov/products/satellite/international-satellite-cloud-climatology-b1"
GPCP_V33_REL = "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf"
GPCP_MON_2026 = "https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-monthly/access/2026/"
GPCP_V33_DG = "https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-the-global-precipitation-climatology-project-gpcp-monthly-"
GPCP_CATBD = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Monthly/AlgorithmDescription_01B-34.pdf"
IPWG26 = "https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf"
DMSP_EARTHDATA = "https://www.earthdata.nasa.gov/data/alerts-outages/status-update-dmsp-data-products"
CLASS = "https://www.aev.class.noaa.gov/"
AFA_DMSP = "https://airandspaceforces.com/space-force-legacy-weather-sats-2028-replacements"
OSPO_SSMIS = "https://www.ospo.noaa.gov/data/messages/2026/09/MSG_20260901_1930.html"
OSPO_WSFM = "https://ospo.noaa.gov/data/messages/2026/07/MSG_20260720_1313.html"
AQUA_END = "https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era/"
AIRS_REPORT = "https://airsnrt.jpl.nasa.gov/report/archive/2026-10-30.txt"
OSPO_HIMA = "https://ospo.noaa.gov/data/messages/2025/11/MSG_20251118_1545.html"
OSPO_MSG = "https://www.ospo.noaa.gov/data/messages/2026/04/MSG_20260428_0930.html"
OSCAR_MET9 = "https://space.oscar.wmo.int/satellites/view/meteosat_9_iodc"
GOES_TRANS = "https://www.nesdis.noaa.gov/our-satellites/currently-flying/goes-east-west/goes-r-series-transition-operations"
GAO_GEO = "https://files.gao.gov/reports/GAO-26-107739/index.html"
POES = "https://www.nesdis.noaa.gov/news/suspension-of-poes-data-users-after-june-16-2025-and-decommissioning"
STAGE4 = "https://api.water.noaa.gov/resources/downloads/precip/stageIV/2026/11/"
GPCC_MON = "https://opendata.dwd.de/climate_environment/GPCC/monitoring_v2022/2026/"
# NCEI-wide and NODD
CJ26 = "https://www.noaa.gov/sites/default/files/2025-06/NOAA%20FY26%20Congressional%20Justification.pdf"
CJ27 = "https://www.noaa.gov/sites/default/files/2026-04/FY2027-NOAA-CJ-Submission.pdf"
HR652 = "https://www.govinfo.gov/content/pkg/CRPT-119hrpt652/html/CRPT-119hrpt652.htm"
SEN27 = "https://www.appropriations.senate.gov/imo/media/doc/cjs_explanatory_stmt.pdf"
JES26 = "https://www.appropriations.senate.gov/imo/media/doc/fy26_cjs_jes.pdf"
SRPT44 = "https://www.govinfo.gov/content/pkg/CRPT-119srpt44/html/CRPT-119srpt44.htm"
S3923 = "https://www.govinfo.gov/content/pkg/BILLS-119s3923es/html/BILLS-119s3923es.htm"
EOS_OAR = "https://eos.org/research-and-developments/proposed-noaa-budget-calls-for-0-for-climate-research"
NESDIS_2025 = "https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes/2025-notice-of-changes"
FEDREG = "https://www.federalregister.gov/api/v1/documents.json?conditions[term]=PERSIANN"
WATCHDOG_AUG = "https://avlwatchdog.org/top-climate-scientists-departure-is-sign-of-brain-drain-at-noaa-hub-in-asheville-and-of-deep-cuts-to-research-across-the-country/"
CTS = "https://dataverse.nl/api/access/datafile/469675"
OIG24 = "https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf"
CLOUD = "https://www.ncei.noaa.gov/news/cloud-migration"
CLOUD_FAQ = "https://www.ncei.noaa.gov/news/cloud-migration-FAQ"
ALERTS = "https://www.ncei.noaa.gov/alerts"
SOS25Q1 = "https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf"
NODD_2019 = "https://www.noaa.gov/media-release/cloud-platforms-unleash-full-potential-of-noaa-s-environmental-data"
AWS_SPONSOR = "https://aws.amazon.com/opendata/open-data-sponsorship-program/"
GOOGLE_PD = "https://docs.cloud.google.com/bigquery/public-data"

# ---------------------------------------------------------------- People risk
P1 = [
    (H, PT1, f"The producing group is small and informal: CHRS calls itself \"an informal interdisciplinary group\" of faculty and researchers at UC Irvine ([CHRS about]({CHRS_ABOUT})). Its directory lists 4 faculty, 4 postdocs, 1 administrator, 11 graduate students and 2 visiting scholars ([CHRS directory]({CHRS_DIR})); no staff count for PERSIANN-CDR is published by CHRS or NCEI.", "C"),
    (H, PT2, f"A full handover package is public at NCEI: the C-ATBD, data flow diagram, 2013 maturity matrix, user guide (2025), use agreement and the complete V1 production code (shell, C/C++ and MATLAB, including the neural-network program and its parameter files) ([NCEI document folder]({DOCS}); [code package]({SRC_TAR})). It dates from 2013–2014, and whether today's runs still match it is not published.", "A"),
    (M, PT3, f"CHRS's leadership has changed: by April 2026 UC Irvine named Amir AghaKouchak director of CHRS ([UCI News, 2026]({UCI_NEWS})), with Soroosh Sorooshian, PERSIANN-CDR's PI, now \"Founding Director\" ([CHRS directory]({CHRS_DIR})). When and how the change was made is not published; an undated UCI listing still names Sorooshian ([UCI Office of Research]({UCI_OR})).", "C"),
    (L, PT1, f"Dan Braithwaite, the C-ATBD co-author named as `creator_name` in NCEI's file metadata ([ERDDAP]({ERDDAP})), is not on the current CHRS directory, and the CHRS run found three other programmer authors of the 2019 portal paper also gone ([CHRS directory]({CHRS_DIR}); subagent's reading). Who took over his work is not published; no search aimed at it was made.", "F"),
]
P1_GAPS = [
    ("U", "A written succession or knowledge-transfer plan for PERSIANN-CDR at CHRS (asked in the pt7 query, not yet run)."),
    ("U", "Who runs the quarterly extension today, and when the directorship changed and why (pt7)."),
]

P2 = [
    (H, PT1, f"The credited people are Soroosh Sorooshian (PI), Kuolin Hsu (C-ATBD lead author), Dan Braithwaite and Hamed Ashouri (now a CHRS alumnus), with Phu Nguyen as CHRS's associate director ([NCEI landing page]({LANDING}); [C-ATBD]({CATBD}); [CHRS directory]({CHRS_DIR})). Braithwaite, Hsu, Nguyen and Sorooshian are also IMERG ATBD co-authors.", "C"),
    (M, PT3, f"Sorooshian holds an endowed Henry Samueli chair (2023) and is now Founding Director, with AghaKouchak director by April 2026 ([UCI News, 2026]({UCI_NEWS})). No source gives a retirement date or plan for any of them.", "C"),
]
P2_GAPS = [
    ("U", "Ages, ORCID iDs, earliest publication years and years on PERSIANN for Sorooshian, Hsu, Nguyen, AghaKouchak, Braithwaite and Sadeghi (the pt7 query asks; not yet run)."),
    ("P", "Real ages and service dates (personnel records). As university staff, federal FERS rules don't apply to CHRS's people."),
]

P3 = [
    (H, PT2, f"The production code is public: a 4.6 MB tarball at NCEI (files dated 2013–2014, posted 2017-03-10) with every step, from splitting GridSat-B1 into subareas (`B1tosubs.c`) and the neural network (`seqSOLO.cc`) to the MATLAB bias adjustment and the netCDF writer, all driven by `Run_PERSIANN.sh` ([code package]({SRC_TAR})). Reuse is limited (\"Proprietary property of The Regents of the University of California\", nonprofit research only), but anyone can read it.", "A"),
    (H, PT2, f"The method is written down: the C-ATBD sets out the network, the 0.1 mm/hr noise threshold and the GPCP ratio (capped at 20) ([C-ATBD]({CATBD})), the data flow diagram lists the steps ([CDRP-DIA-0351]({DFD})), and Ashouri et al. (2015) describe the training ([BAMS]({ASHOURI})).", "A"),
    (H, PT2, f"QC is not documented as a procedure: NCEI's 2020 stewardship assessment scores Quality Control/Monitoring 1.5 of 5, \"Procedure not documented or available\", and notes no data-quality information in the metadata ([NOAA IR 33336]({DSMR12})). The checks that exist are built into the code.", "F"),
    (M, PT5, f"The documents don't match what is run: the User Guide (December 2025) and the code README still say GPCP v2.2, while the 2026 files name `gpcpv23_m2607.bin` ([User Guide]({GUIDE}); [NCEI file attributes]({AGG})). No document states which GPCP version covers which years ([Sadeghi et al. 2019]({SADEGHI19})).", "F"),
    (M, PT2, "The training code (the network's pretraining on NCEP Stage IV) was not found in the package; the method is in papers only. The network is then held fixed, so training is needed only to rebuild it.", "C"),
    (M, PT2, "No CHRS code after 2014 is published, and whether the current operational runs differ from the 2014 package is not known. The bias-adjustment step needs MATLAB, a commercial product.", "C"),
]
P3_GAPS = [
    ("S", "Whether CHRS's current production code differs from the 2014 package (ask CHRS or PERSIANN_contacts@noaa.gov)."),
    ("S", "The training code and the Stage IV period and region used."),
]

P4 = [
    (H, PT1, f"Every production step is algorithmic and runs one month at a time; QC is automated checks built into the code, with no manual review step described ([C-ATBD]({CATBD}); [User Guide]({GUIDE})). Someone still has to run the quarterly extension; who, and how many people can, is not published.", "C"),
    (M, UCI, f"CHRS's data site has one listed \"Program & System Administrator\" ([CHRS directory]({CHRS_DIR})), and the named Programmer Analyst III, Dan Braithwaite, is no longer listed ([CHRS Data Portal, Info tab]({CHRS_PORTAL})). NCEI serves its own copy, so losing CHRS's site alone would not stop distribution.", "C"),
    (H, PT1, "NCEI names no individual steward: its contacts are the Customer Engagement Branch and `cdr-ipt-PERSIANN@noaa.gov`.", "C"),
    (M, PT3, f"Production has slowed with no cause given: NCEI's notice that the CDR \"is experiencing a pause in operations due to processing delays\" was online by 2025-09-13 ([NCEI]({PAUSE}); [Wayback]({PAUSE_WB})), and CHRS posted the 2024 files only in October–December 2025. Whether a staffing gap is behind it is not known.", "C"),
]
P4_GAPS = [
    ("U", "Who runs the quarterly extension and whether it is one person (pt7, not yet run)."),
]

# ---------------------------------------------------------------- Data risk
D1 = [
    (H, PT3, f"NOAA's FY2027 request cuts NCEI, the archive and distributor, to $52.0M (−$17.8M from a $69.8M base); the House committee gives $60.0M and the Senate committee $70.0M; FY2027 runs on a continuing resolution to December 11, 2026 ([NOAA FY2027 CJ]({CJ27}); [H.Rept. 119-652]({HR652}); [Senate statement]({SEN27})). Pending.", "F"),
    (M, PT4, f"About 120 searches (news, trade press, UC Irvine pages, court records, NOAA notices, January 2024 – November 2026) found no cut, termination or proposal aimed at PERSIANN-CDR, CHRS or its precipitation grants; NESDIS's notices and the Federal Register don't name it ([NESDIS 2025 Notice of Changes]({NESDIS_2025}); [Federal Register]({FEDREG})).", "A"),
    (H, PT3, f"NCEI's FY2026 request was also $52.0M; Congress enacted $69.0M ([FY2026 CJ]({CJ26}); [FY2026 JES]({JES26})). Rejected.", "C"),
    (H, PT3, f"No public source says what pays for production today. The record was built in 2009–2014 with CDR Program money through a CICS sub-award ([Ashouri et al. 2015]({ASHOURI}); [USAspending]({CICS_AW})); NCEI staff wrote that \"During the NCEI reorganization in 2015, the CDR Program ended\" ([AMS 2019]({AMS19}), abstract only); no NOAA budget line names Climate Data Records or PERSIANN.", "C"),
    (H, PT3, f"CHRS's main NOAA grant, NA23OAR4310443 ($390,000, 2023-09-01 to 2026-08-31, for the new CCS-CDR v2, PI Phu Nguyen), ran its full term with no successor found; its funding was \"conditional on appropriations\" ([USAspending]({CPO_AW}); [NOAA CPO]({CPO_NEWS})). It is not named as paying for PERSIANN-CDR.", "C"),
    (M, PT4, f"The FY2026 and FY2027 requests ask to end OAR, its cooperative institutes and Climate Competitive Research, which pays CPO grants like CHRS's ([Eos, 2025]({EOS_OAR}); [FY2027 CJ]({CJ27})); Congress kept OAR for FY2026. None names PERSIANN, CHRS or the CDR Program.", "C"),
    (M, PT3, f"The CISESS agreement (NA24NESX432C0001, to 2029-06-30) lists Hsu, Nguyen and Sorooshian as consortium scientists on a JPSS orographic-precipitation project ([USAspending]({CISESS_AW}); [CISESS]({CISESS_UPD})); it does not name PERSIANN-CDR.", "C"),
    (M, PT4, f"UC Irvine had 51 awards terminated and 5 suspended by May 2025, including one unnamed NOAA \"incoming subaward\" ([UCI town hall]({UCI_TOWNHALL})); AghaKouchak's NSF flood grant 2332263 was terminated 4/18/2025 and reinstated 6/30/2025 ([Thakur v. Trump]({THAKUR})). Neither is tied to PERSIANN.", "C"),
    (M, PT4, f"CHRS's EGU 2026 abstract for a new high-resolution CDR (PUnet-CDR) \"has been withdrawn on 19 May 2026\", with no reason given ([EGU26-2633]({EGU_PUNET})).", "C"),
]
D1_GAPS = [
    ("P", "What pays for the quarterly extension since 2014 (held by NCEI's CDR contact or CHRS; asked in pt7)."),
    ("S", "A successor to NA23OAR4310443 (NOAA CPO's FY2026 award list was not found)."),
    ("S", "The FY2027 outcome after the December 11, 2026 continuing resolution."),
]

D2 = [
    (H, NCEI_A2, f"PERSIANN-CDR is archived at NCEI's Asheville site; its maturity report says so and no source names a copy in Boulder ([DSMR-00012]({DSMR12})). Asheville keeps two tape copies, the offsite one \"several kilometers away\" ([CoreTrustSeal application]({CTS})).", "F"),
    (M, NCEI_A2, f"NCEI is moving all its data to AWS through spring 2027 as a \"lift and shift\" ([NCEI]({CLOUD})); OIG found the target platform \"resides in a single region\" ([OIG-24-034-A]({OIG24})), and its recommendation is listed \"Closed\" with no published action. The production regions are not published.", "F"),
    (M, UCI, f"CHRS makes and serves its own copy on its own servers: \"CHRS's servers produce PERSIANN and PERSIANN-CDR by implementing the algorithms locally\" ([Nguyen et al. 2019]({NGUYEN19})). No source says where those servers sit, whether they are backed up, or that a second CHRS site exists.", "F"),
    (H, PT1, f"Several organizations serve PERSIANN-CDR: NCEI (HTTPS, THREDDS, ERDDAP), CHRS (portal, HTTPS and FTP), and NOAA's NODD copies on AWS (`s3://noaa-cdr-precip-persiann-pds/`) and Azure ([NCEI product page]({PRODUCT}); [CHRS portal]({CHRS_PORTAL}); [AWS registry]({AWS_REG}); [Azure]({AZURE})). On 19 Nov 2026 NCEI's and CHRS's daily folders both ended at 31 July 2026.", "A"),
    (H, PT4, f"Volunteers archived NCEI's PERSIANN-CDR folder (16.0 GB, with a torrent) in April 2025 ([Data Rescue Project]({DRP})). A volunteer snapshot is not a repository.", "C"),
]
D2_GAPS = [
    ("P", "NCEI's production AWS regions after the move, and whether the Asheville tapes are kept."),
    ("S", "Where CHRS's servers sit and whether they are backed up (held by CHRS or UCI OIT)."),
]

D3 = [
    (H, NCEI_A2, f"NCEI's severity-high alert (November 16–30, 2026) says \"Many access portals, interactive maps, and data folders are currently unavailable\" and to \"Expect delayed data archival\" ([NCEI Alerts]({ALERTS})); its product page warns of \"slower update cycles\", and the live landing page returned HTTP 503 during the pt1 run.", "F"),
    (H, PT3, f"NCEI has shown a notice since at least 2025-09-13 that \"The Precipitation - PERSIANN CDR is experiencing a pause in operations due to processing delays\", with no cause or end date ([NCEI]({PAUSE}); [Wayback]({PAUSE_WB})). New files still arrived on 2026-07-09 and 2026-10-13 ([NCEI 2026 folder]({NCEI_2026})).", "F"),
    (H, PT4, f"NCEI's FY2027 request is $52.0M, $17.8M below its base, pending under a continuing resolution to December 11, 2026 ([NOAA FY2027 CJ]({CJ27})).", "F"),
    (M, UCI, f"CHRS's data site rests on a very small team: one listed system administrator ([CHRS directory]({CHRS_DIR})), development paid \"mostly from discretionary sources\", and its named programmer analyst gone ([CHRS Data Portal, Info tab]({CHRS_PORTAL})). No money set aside for the site was found.", "F"),
    (M, UCI, f"CHRS's site has had unexplained outages and lags: the portal says \"Download links available again 2024-10-11\" with no cause ([CHRS portal]({CHRS_PORTAL})), and after the last 2023 file (written 2024-04-15) nothing was posted for 18 months, until the 2024 files on 2025-10-21 ([daily index]({CHRS_DAILY}); [yearly index]({CHRS_YEARLY})).", "F"),
    (M, GH_REPO, f"NOAA's NODD cloud copies rest on 2019 \"separate multiyear contracts with AWS, Google Cloud, and Microsoft\" with no published end date ([NOAA, 2019]({NODD_2019})); no enacted budget line for NODD was found.", "F"),
    (M, PT1, f"CHRS's portal info tab still says \"Latest Update: September 2020\" and \"01/01/1983 to 12/31/2015 (delayed present)\" ([CHRS portal]({CHRS_PORTAL})), out of date against its files.", "C"),
    (M, PT2, f"The IRI/LDEO Data Library now \"requires all users to sign in\" and may hold a copy frozen at September 2019 (snippet only) ([IRI]({IRI})); Google Earth Engine's copy ends 2026-07-31 ([Earth Engine]({GEE})). Neither is a repository.", "C"),
]
D3_GAPS = [
    ("S", "The cause of NCEI's pause notice and of CHRS's 2024 outage and posting lag (held by NCEI and CHRS)."),
    ("P", "How CHRS's administrator post is paid for; the NODD contract end dates."),
]

D4 = [
    (H, PT2, f"NCEI's routes (HTTPS, THREDDS/OPeNDAP, ERDDAP) and the AWS copy serve CF-compliant daily netCDF-4 (`precipitation_amount`, mm) with a DOI and no access constraints, rated fully FAIR; generic netCDF tools read them ([NCEI ERDDAP]({ERDDAP_DAS}); [NCEI 2026 folder]({NCEI_2026})).", "A"),
    (M, PT2, f"CHRS's own server serves headerless `.bin.gz` raw binary (its `daily_netcdf/` folder is empty) with no licence stated, rated non-FAIR, and its portal offers ArcGrid, GeoTIFF and NetCDF ([CHRS server]({CHRS_DAILY}); [Nguyen et al. 2019]({NGUYEN19})). Raw binary needs the layout to read but no proprietary software; the CHRS README was not read.", "C"),
    (M, PT2, f"The licence is stated loosely: the files say \"no restrictions are placed upon their use\", DataCite's record has an empty `rightsList` ([DataCite]({DATACITE})), and data.gov names CC0 1.0 on a record that also says \"non-public\" ([data.gov]({DATAGOV})). This is access, not format.", "C"),
    (M, PT2, "The two missing-data markers differ (`missing_value` -9999, `_FillValue` -1), so a user's tool may treat only one as missing.", "C"),
]
D4_GAPS = [
    ("U", "The CHRS binary layout and terms of use (CHRS README not read)."),
]

D5 = [
    (M, PT4, "About 120 searches across news, trade and science press, UC Irvine's pages, court records and NOAA notices (January 2024 – November 2026) found no coverage naming PERSIANN-CDR, CHRS or its researchers in connection with cuts or threats.", "A"),
    (H, PT4, f"The Data Rescue Project archived NCEI's PERSIANN-CDR folder on 2025-04-24 during the rescue of US federal data, stating no reason or threat ([Data Rescue Project]({DRP})).", "C"),
    (H, NCEI, f"The Senate says NOAA \"has decommissioned at least 20 datasets, products and catalogs\" without notice ([S.Rept. 119-44]({SRPT44})); none is named. S. 3923 would keep the archive at \"NCEI, or a successor entity\" ([S. 3923]({S3923})).", "C"),
]
D5_GAPS = []

# ---------------------------------------------------------------- Dependent infrastructure resilience
DIRS1 = [
    (H, PT5, f"GridSat-B1, PERSIANN-CDR's main input, lost its calibration source: HIRS all-sky data production \"ceased in 2024\", and GridSat-B1's C-ATBD Rev 2 (2026-03-02) now intercalibrates against VIIRS VGAC with a constant adjustment for continuity ([GridSat C-ATBD]({GRIDSAT_ATBD})). The same recalibration paused GPCP V3.3 \"while NCEI is developing a new calibration procedure for the GridSat IR input\" ([GPCP V3.3 release notes]({GPCP_V33_REL})).", "F"),
    (M, PT5, f"Each month's estimates are bias-adjusted to GPCP's monthly analysis, a reference product calibrated with GPCC gauges and DMSP microwave data ([C-ATBD]({CATBD}); [GPCP C-ATBD]({GPCP_CATBD})). The v2.3 it uses is marked \"Version Superseded\" by NCEI, with no retirement date ([data.gov]({GPCP_V33_DG})).", "F"),
    (M, PT5, "No source says whether PERSIANN-CDR's months from 2024 on use the VIIRS-recalibrated GridSat-B1, or how the change shifts its values.", "C"),
    (M, PT2, "GridSat-B1's own calibration and QC (scan-line QC, an automated check of each satellite against the others, flagged `intergeo_cal_flag`) are done by NCEI, not CHRS.", "C"),
    (L, PT5, "Inference: as an infrared-derived product, PERSIANN-CDR has no physical calibration lab of its own; its calibration rests on GridSat-B1's intercalibration and on GPCP.", "C"),
]
DIRS1_GAPS = [
    ("S", "Whether PERSIANN-CDR's 2024–2026 months use the recalibrated GridSat-B1 (pt7 asks; not yet run)."),
    ("U", "Who maintains GridSat-B1's calibration at NCEI, and how it is funded."),
]

DIRS2 = [
    (M, PT5, f"Europe, Africa and the Indian Ocean rest on ageing satellites: GridSat-B1 still uses Meteosat-10 (now a backup) and Meteosat-9 over the Indian Ocean (end of life about 2027, set by fuel), and no plan was found to bring MTG (Meteosat-12, prime since June 2025) into ISCCP B1 ([OSPO/EUMETSAT, 2026]({OSPO_MSG}); [WMO OSCAR]({OSCAR_MET9}); [GridSat header, Oct 2026]({GRIDSAT_OCT26})).", "F"),
    (M, PT5, f"DMSP F17 SSMIS, GPCP's only microwave sensor since 2009, is at its end: data have been \"data of opportunity\" on a \"best effort (8x5) basis\" since July 2025, NOAA's CLASS said \"DMSP data flow stopped on 9/30/2026\" before deliveries resumed under new names, and F17's end of life was estimated for September 2026 ([NASA Earthdata]({DMSP_EARTHDATA}); [NOAA CLASS]({CLASS}); [OSPO]({OSPO_SSMIS})). It reaches PERSIANN-CDR only through GPCP's monthly, so it would degrade it rather than stop it.", "F"),
    (M, PT5, f"Aqua AIRS, GPCP's high-latitude sounder since 2003, is nearing its end: NASA projects the end of Aqua's science for September 2027 ([NASA, 2025]({AQUA_END})); AIRS \"remains healthy\" on 30 Oct 2026 ([AIRS report]({AIRS_REPORT})). It acts through GPCP, mostly beyond PERSIANN-CDR's 60°S–60°N.", "F"),
    (H, PT5, f"Geostationary changes so far were absorbed: GOES-19 replaced GOES-16 on 7 Apr 2025 ([NESDIS]({GOES_TRANS})), Himawari-8 covered Himawari-9's imaging anomaly (12 Oct – 26 Nov 2025; [OSPO/JMA]({OSPO_HIMA})), and Meteosat-11 covered Meteosat-10 (24–28 Apr 2026). The October 2026 files list \"GOES-18,GOES-19,Himawari 9,Meteosat-9,Meteosat-10\". Himawari-10 is reported delayed to about fiscal 2030.", "C"),
    (H, NOAA_SAT, f"GOES is working; GAO projects a gap in the geostationary spare from October 2032 (GOES-16's end of life) to early 2033, when GeoXO-1 is operational ([GAO-26-107739]({GAO_GEO})). That is beyond the next few years.", "C"),
    (M, PT5, f"NOAA POES TOVS and AVHRR ended in June 2025 ([NESDIS]({POES})), but GPCP used TOVS only for 1987–2002 and AVHRR for 1981–1988, so the ongoing record is not affected ([GPCP C-ATBD]({GPCP_CATBD})).", "C"),
    (M, PT5, f"NCEP Stage IV, used only to pretrain the network, is still posted daily ([NWS]({STAGE4})); GPCC's gauge monitoring product that GPCP uses is still extended ([DWD]({GPCC_MON})).", "C"),
    (H, PT6, "Over the record GridSat-B1 brings in about 36 geostationary satellites (GOES-1 and -5 to -19, Meteosat-2 to -11, GMS-1 to -5, MTSAT-1R/-2, Himawari-8 and -9, FY-2C/-2E); GPCP adds DMSP F08, F11, F13 (SSM/I) and F17 (SSMIS), TOVS, Aqua AIRS and early AVHRR.", "C"),
]
DIRS2_GAPS = [
    ("S", "When MTG enters ISCCP B1 (EUMETSAT and NCEI hold it; EUMETSAT pages refused the run's tools)."),
    ("S", "Which DMSP satellites still deliver after 30 Sep 2026, and whether GPCP's Sep–Oct 2026 months used SSMIS."),
]

DIRS3 = [
    (H, PT5, f"PERSIANN-CDR is extended \"as new GridSat-B1 IR data and GPCP monthly rainfall data become available\" ([User Guide]({GUIDE})), and its bias adjustment still uses GPCP v2.3 (`gpcpv23_m2607.bin` in the July 2026 file; [NCEI attributes]({AGG})). NCEI issued GPCP V3.3 as the NOAA CDR on 2025-08-05 and marks v2.3 \"Version Superseded\" ([data.gov]({GPCP_V33_DG})); GPCP V4 targets mid 2027 ([Behrangi et al. 2026]({IPWG26})). No date to freeze v2.3 and no plan for PERSIANN-CDR to move was found.", "F"),
    (M, PT5, "Moving to GPCP V3.3 would not be a simple swap: V3.3 itself takes PERSIANN data as an input, so the two would feed each other.", "F"),
    (H, PT5, f"GridSat-B1 is still extended (files to 2026-10-31, posted 2026-11-04, v02r01 unchanged; [NCEI THREDDS]({GRIDSAT_2026})), but its calibration changed in 2024 (see DIRS-1) and NCEI's ISCCP B1 table is out of date ([NCEI]({ISCCP_B1})).", "C"),
    (M, PT5, f"GPCP v2.3 is still produced: final months to August 2026 (created 2026-11-09) and preliminary months for September–October 2026 ([NCEI]({GPCP_MON_2026})).", "C"),
    (M, PT1, "NCEP Stage IV was used only to pretrain the network, then held fixed; it does not feed new months.", "C"),
    (L, PT5, "A search summary (not read) says Google Earth Engine's GridSat-B1 copy has not been updated since 2024; PERSIANN-CDR's files name NCEI's copy, not that one.", "C"),
]
DIRS3_GAPS = [
    ("S", "A retirement date for GPCP v2.3, and any CHRS or NCEI plan for PERSIANN-CDR if it is frozen."),
    ("S", "Which GPCP version covers which years (only 2009–2013 is documented as v2.3)."),
]

DIRS4 = [
    (H, PT1, f"CHRS processes it on its own systems: \"CHRS's servers produce PERSIANN and PERSIANN-CDR by implementing the algorithms locally\" ([Nguyen et al. 2019]({NGUYEN19})), and NCEI lists UC Irvine as the \"Processor\" ([NCEI landing page]({LANDING})).", "A"),
    (M, PT2, f"The code needs gcc, g++, netCDF-4 and MATLAB, a commercial product, for the bias-adjustment step (`dobias_adj_B1.m`) ([code package]({SRC_TAR})). No source says the licence is at risk.", "C"),
    (M, UCI, f"Who maintains CHRS's servers, how its administrator post is paid for, and any role for the engineering school's IT or campus OIT are not published; OIT hosts co-located research systems (snippet only), but no source places CHRS's servers there ([UCI OIT]({OIT})).", "C"),
    (M, PT2, "Its inputs are processed and quality-controlled by their own producers: GridSat-B1 by NCEI, GPCP by UMD and NASA (with GPCC's gauges), Stage IV by the River Forecast Centers. Those are DIRS-3 dependencies, not outside processing of PERSIANN-CDR itself.", "C"),
]
DIRS4_GAPS = [
    ("U", "The machines that run PERSIANN-CDR today and who pays for them (pt7, not yet run)."),
]

DIRS5 = [
    (M, PT5, f"No fallback input is named: no document names a substitute for GPCP v2.3 or for GridSat-B1, and neither CHRS nor NCEI has announced one ([C-ATBD]({CATBD}); [User Guide]({GUIDE})). The run rates losing either as \"would stop extension\".", "F"),
    (H, PT5, f"GridSat-B1's geostationary inputs have backups that have already been used: GOES-19 for GOES-16, Himawari-8 during Himawari-9's anomaly, and Meteosat-11 for Meteosat-10 ([OSPO/JMA]({OSPO_HIMA}); [OSPO/EUMETSAT]({OSPO_MSG})).", "A"),
    (M, PT5, f"Successors exist for GPCP's microwave input: WSF-M01 data have flowed to NOAA since July 2026 ([OSPO]({OSPO_WSFM})), and a GPCP team member named WSF-M as SSMIS's successor in 2023. Neither is in GPCP v2.3 now.", "C"),
    (M, PT1, "CHRS makes related records from the same IR inputs (PERSIANN-CCS-CDR v2.0 from 1983 and \"PERSIANN-CDR V3\" from 1980, both 0.04° and adjusted to GPCP), but no source shows NCEI archives either, and they share PERSIANN-CDR's dependencies.", "C"),
    (L, GPCP_PT7B, "Inference: other satellite precipitation records could stand in for parts of PERSIANN-CDR (GPCP Daily, CMORPH CDR, MSWEP, CHIRPS over land); GPCP's research lists PERSIANN-CDR among GPCP's partial substitutes. None was searched for as a substitute for PERSIANN-CDR, and none matches its 1983 start at 0.25° from IR alone.", "C"),
]
DIRS5_GAPS = [
    ("U", "Substitute datasets for PERSIANN-CDR and how much of it each could replace (pt7, not yet run)."),
]

# ---------------------------------------------------------------- Repository resilience
RRS1 = [
    (M, UCI, f"Independent holders in different places keep current copies: NCEI (Asheville), CHRS's own server at UC Irvine, and NOAA's NODD copies on AWS (us-east-1) and Azure (us-east) ([NCEI 2026 folder]({NCEI_2026}); [CHRS daily]({CHRS_DAILY}); [AWS registry]({AWS_REG}); [Azure]({AZURE})). On 19 Nov 2026 NCEI's and CHRS's daily folders both ended at 31 July 2026. No source says any copy is checked against another.", "F", "NOAA NCEI, UC Irvine CHRS data site, AWS, Google Cloud and Azure (NODD)"),
    (H, NCEI_A2, f"At NCEI, PERSIANN-CDR is archived in Asheville, whose offsite tape copy is \"several kilometers away\"; NCEI documents dispersed copies only for Boulder's own holdings ([CoreTrustSeal application]({CTS}); [DSMR-00012]({DSMR12})). The run finds RRS-1 not shown for PERSIANN-CDR.", "A", NCEI_R),
    (M, NCEI_A2, f"OIG found NCEI's cloud target \"resides in a single region\" ([OIG-24-034-A]({OIG24})); the recommendation is \"Closed\" with no published action, and the AWS regions after the move are not published.", "A", NCEI_R),
    (M, NCEI_A2, f"Nothing published says the NODD copies are checked against NCEI's archive: the `noaa-cdr-precip-persiann-pds` listing shows only S3 ETags ([AWS listing]({AWS_LIST})).", "A", NODD),
    (M, UCI, f"No backup, second site or mirror is published for CHRS's site; the 2019 portal paper mentions none, and a search found only CHRS's own .eng.uci.edu hosts ([Nguyen et al. 2019]({NGUYEN19})). This rests on silence.", "A", CHRS),
    (H, PT4, f"Copies that are not repositories: the Data Rescue Project's 16 GB snapshot (April 2025; [DRP]({DRP})), Google Earth Engine's reformatted collection (to 2026-07-31; [Earth Engine]({GEE})) and the IRI/LDEO Data Library, which now needs a sign-in and may be frozen at September 2019 ([IRI]({IRI})).", "C", "Data Rescue Project, Google Earth Engine, IRI Data Library (not repositories)"),
]
RRS1_GAPS = [
    ("P", "NCEI's production AWS regions and copy count after the move."),
    ("S", "Whether CHRS backs up its server (UCI OIT's service is opt-in) or keeps a second site."),
    ("S", "Whether the AWS, Google and Azure copies are current (the bucket listings were not opened in pt1)."),
]

RRS2 = [
    (H, NCEI_A2, f"PERSIANN-CDR's stewardship maturity report scores \"Data Integrity - 3.5\": checksums are \"generated at ingest\" and \"verified when customer orders data\", with no re-verification schedule; Control/Monitoring scores 1.5 ([DSMR-00012]({DSMR12})).", "A", NCEI_R),
    (H, NCEI_A2, f"NCEI's CoreTrustSeal application (certified to January 29, 2028) says a file's MD5 is checked \"Any time a file is pulled\" and that scripts compare file sizes between copies \"on a routine basis\", with no frequency ([CoreTrustSeal]({CTS})). The procedure (SOP 60-6-015) is not public.", "A", NCEI_R),
    (M, UCI, f"CHRS publishes no checksums: its PERSIANN-CDR daily folder lists 15,900 `.bin.gz` files and no md5, sha or manifest file, and no fixity practice is described anywhere ([daily index]({CHRS_DAILY}); [yearly index]({CHRS_YEARLY})).", "A", CHRS),
    (M, UCI, f"UC Irvine's OIT sells an opt-in, recharge-billed backup service that \"is not an archival storage service\", with encrypted off-site copies ([UCI OIT]({OIT}); [SLA, 2021]({OIT_SLA})). No source shows CHRS subscribes, and encryption is not a fixity check.", "C", CHRS),
    (M, GH_RRS, "AWS says S3 \"regularly\" verifies stored data with checksums, with no frequency; no NOAA or provider document says the NODD copy is verified against NCEI's.", "C", NODD),
]
RRS2_GAPS = [
    ("P", "NCEI's SOP 60-6-015."),
    ("P", "Any fixity practice at CHRS (held by CHRS)."),
]

RRS3 = [
    (M, GH_RRS, f"OIG found that NCEI's cloud target platform, at its moderate impact level, does not offer \"testing contingency plans at alternate processing sites\" ([OIG-24-034-A]({OIG24})).", "A", NCEI_R),
    (M, UCI, f"No CHRS disaster recovery plan or test is published. UC policy says plans \"should be tested on a periodic basis\" ([UC IS-12, 2007]({IS12})), and UC Irvine's backup service is opt-in with no restore testing in its SLA ([OIT SLA]({OIT_SLA})).", "A", CHRS),
    (H, NCEI_A2, f"NCEI has an Information System Contingency Plan with an annual Business Impact Analysis, daily and weekly off-site backups and COOP plans, but it \"cannot be shared outside the US Government\", and no test date or result appears anywhere ([CoreTrustSeal]({CTS})).", "C", NCEI_R),
]
RRS3_GAPS = [
    ("P", "NCEI's contingency-plan test results."),
    ("P", "Any CHRS disaster recovery plan, and whether CHRS uses UCI OIT's backup (held by CHRS and OIT)."),
]

RRS4 = [
    (H, NCEI, f"NCEI's FY2027 request is $52.0M (−$17.8M from a $69.8M base); the House committee gives $60.0M and the Senate committee $70.0M; a continuing resolution runs to December 11, 2026 ([NOAA FY2027 CJ]({CJ27})).", "A", NCEI_R),
    (M, NCEI, f"NCEI's staff fell from 184 FTE (FY2024) to 140 (FY2026 enacted column), with 58 departures by August 2025 ([Asheville Watchdog]({WATCHDOG_AUG})).", "A", NCEI_R),
    (M, NCEI, f"FY2026 was enacted above the request: $69.0M for NCEI ([FY2026 JES]({JES26})), and the FY2027 plan keeps \"the core mission of preserving, hosting, and providing access\" to the archives.", "F", NCEI_R),
    (M, UCI, f"CHRS is a School Center, \"established by Deans for a defined period of time\" ([UCI Centers & Institutes]({UCI_CENTERS})); \"The majority of CHRS research activities are funded by NASA, NOAA, and NSF\" ([UCI Office of Research]({UCI_OR})), and no campus funding, space or staff commitment is published.", "A", CHRS),
    (M, PT3, f"CHRS's main NOAA grant (NA23OAR4310443) ended 2026-08-31 with no successor found ([USAspending]({CPO_AW})), and UC Irvine's federal funding was down about $50M (11.7%) for July 2025 – February 2026 against the year before ([UCI Office of Research, March 2026]({UCI_MAR26})).", "A", CHRS),
    (M, GH_RRS, f"The NODD copies have no guaranteed term: AWS's sponsorship \"covers the cost of storing and sharing\" with no term stated ([AWS]({AWS_SPONSOR})), and Google states no SLA ([Google]({GOOGLE_PD})).", "A", NODD),
]
RRS4_GAPS = [
    ("P", "NCEI's FY2026 spend plan; the FY2027 outcome."),
    ("S", "How CHRS's data site is paid for (no line found)."),
]

RRS5 = [
    (M, NCEI_A2, f"Hurricane Helene (September 2024): Asheville lost power, water and communications; ingest was restored by December 11 and \"92% of the ingest backlog was recovered\", with Boulder's help ([NCEI FY25 Q1]({SOS25Q1})). No loss of archived holdings was reported.", "F", NCEI_R),
    (M, NCEI_A2, "The 2015 NCDC-to-NCEI merger came with \"no products or services ... slated to be cut or reduced\", and no loss or backlog was reported.", "F", NCEI_R),
    (M, NCEI_A2, "The other 8% of Helene's ingest backlog is not accounted for, and no final loss count was published.", "A", NCEI_R),
    (M, NCEI, f"About 27 NCEI products were retired or cut back from April 2025 ([NESDIS 2025 Notice of Changes]({NESDIS_2025})); their existing data were kept. PERSIANN-CDR is not among them.", "A", NCEI_R),
    (M, UCI, f"CHRS's site came back from its 2024 outage (\"Download links available again 2024-10-11\") and its 18-month posting gap with its files present, and no data loss is recorded ([CHRS portal]({CHRS_PORTAL}); [daily index]({CHRS_DAILY})). No cause or after-action note was published, so \"no loss\" rests on silence.", "F", CHRS),
    (M, NCEI_A2, f"NCEI's cloud move is a disruption still under way: its alert (November 16–30, 2026) says to \"Expect delayed data archival\" and states no loss ([NCEI Alerts]({ALERTS})); its FAQ says \"No datasets will be retired as part of the cloud migration\" ([FAQ]({CLOUD_FAQ})).", "C", NCEI_R),
    (M, UCI, f"AghaKouchak's NSF grant 2332263 was terminated 4/18/2025 and reinstated 6/30/2025 ([Thakur v. Trump]({THAKUR})); it doesn't fund the data site.", "C", CHRS),
]
RRS5_GAPS = [
    ("S", "The cause of CHRS's 2024 outage and whether any files were lost (held by CHRS)."),
    ("S", "A final Helene loss count; whether the 2026 migration delays PERSIANN-CDR."),
]

SUBCATEGORIES = {
    "P-1": (P1, P1_GAPS),
    "P-2": (P2, P2_GAPS),
    "P-3": (P3, P3_GAPS),
    "P-4": (P4, P4_GAPS),
    "D-1": (D1, D1_GAPS),
    "D-2": (D2, D2_GAPS),
    "D-3": (D3, D3_GAPS),
    "D-4": (D4, D4_GAPS),
    "D-5": (D5, D5_GAPS),
    "DIRS-1": (DIRS1, DIRS1_GAPS),
    "DIRS-2": (DIRS2, DIRS2_GAPS),
    "DIRS-3": (DIRS3, DIRS3_GAPS),
    "DIRS-4": (DIRS4, DIRS4_GAPS),
    "DIRS-5": (DIRS5, DIRS5_GAPS),
    "RRS-1": (RRS1, RRS1_GAPS),
    "RRS-2": (RRS2, RRS2_GAPS),
    "RRS-3": (RRS3, RRS3_GAPS),
    "RRS-4": (RRS4, RRS4_GAPS),
    "RRS-5": (RRS5, RRS5_GAPS),
}

DATASET = {
    "producer": "Center for Hydrometeorology and Remote Sensing (CHRS), University of California, Irvine, under the NOAA CDR Program",
    # False: NCEI, not CHRS, is the archive of record. CHRS's own copy is listed as a producer site.
    "producer_is_repository": False,
    "repositories": [
        {"name": NCEI_R, "role": "parent"},
        {"name": CHRS, "role": "producer site"},
        {"name": NODD, "role": "child"},
    ],
}

write_categories("persiann-cdr-daily", SUBCATEGORIES, DATASET)
