"""Build the GPCP Daily R* categorization JSON (second pass, 2026-11-27; first pass and pt7 Run 2 2026-11-24).

Hand-sorted evidence from every answer file in rstar-pipeline/input/web-research/ that bears on GPCP Daily
(1DD V1.3, the NOAA CDR at NCEI, and V3.x Daily, from NASA MEaSUREs at GES DISC with a V3.3 CDR copy at NCEI):
- the eight about-datasets/gpcp-daily runs (about-pt1, qc-formats-pt2, people-pt3, funding-news-pt4,
  inputs-pt5, satellites-pt6 and the two gap runs of the pt7 query: people-production-pt7 and
  calibration-copies-pt7, its Run 2 on calibration, alternatives and copies);
- the two archives/noaa-ncei runs (A1 threats, A2 resilience; the A2 run covers GPCP Daily by name);
- instruments/nasa-satellites and instruments/noaa-satellites (GPM, Aqua, DMSP, POES, S-NPP, GOES);
- archives/nasa-gesdisc-pps (A2 resilience run; its GES DISC findings, added in the second pass);
- for NCEI-wide and NODD facts only, the GHCN-Daily repository runs pt7 and pt9.
Left out: instruments/noaa-rain-gauges (GPCP's gauges come only through DWD's GPCC analysis; no run ties US
gauge networks to it) and the other GHCN-Daily runs.
Not available: no repository run for NCAR GDEX or Copernicus CDS (their RRS gaps say so).

Second pass (2026-11-27): added the NASA GES DISC + PPS A2 run to D-2, D-3 and RRS-1 to RRS-5 for GES DISC, which
holds V3.x (the run found no PPS copy of GPCP).

Filing rules: rstar-pipeline/input/framework/rstar-categorization-decisions.md. Steps: rstar-pipeline/processing/instructions/categorize-dataset-instructions.md.
Markdown links [label](url) in the text become <a> tags (rstar_common.py does the writing and scoring).

Run:  python3 rstar-pipeline/processing/scripts/categorize/build_gpcp-daily.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rstar_common import H, M, L, write_categories  # noqa: E402

# data-source values: the research run folder names
PT1 = "2026-11-19_gpcp-daily-about-pt1"
PT2 = "2026-11-20_gpcp-daily-qc-formats-pt2"
PT3 = "2026-11-20_gpcp-daily-people-pt3"
PT4 = "2026-11-20_gpcp-daily-funding-news-pt4"
PT5 = "2026-11-20_gpcp-daily-inputs-pt5"
PT6 = "2026-11-20_gpcp-daily-satellites-pt6"
PT7 = "2026-11-24_gpcp-daily-people-production-pt7"
PT7B = "2026-11-24_gpcp-daily-calibration-copies-pt7"  # Run 2 of the pt7 query: calibration, alternatives, copies
NCEI ="2026-11-17_noaa-ncei-threats"
NCEI_A2 = "2026-11-23_A2_Rstar_query-noaa_ncei"
NASA_SAT = "2026-11-18_nasa-satellite-precip-threats"
NOAA_SAT = "2026-11-18_noaa-satellite-precip-threats"
GH_REPO = "2026-11-22_ghcn-daily-repository-pt7"
GH_RRS = "2026-11-23_ghcn-daily-repository-resilience-pt9"
GDP = "2026-11-27_gesdisc-pps-resilience"  # archives/nasa-gesdisc-pps A2 run

# Each evidence item is (confidence, source run, text, stance[, repository for RRS]); stance toward the
# subcategory's statement: F = for, A = against, C = context (not directly tied, or doesn't show it true or false).
# Each gap is (status, text): S = searched and none found, P = not public, U = not searched.

# Repository names (match DATASET below)
NCEI_R = "NOAA NCEI"
GESDISC = "NASA GES DISC"
NODD = "AWS and Google Cloud (NODD)"
GDEX = "NSF NCAR GDEX"
CDS = "Copernicus CDS"

# Frequently cited pages
CATBD = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf"
CDR_DIR = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/"
SRC_TAR = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/SourceCode_01B-35.tar.gz"
MATRIX = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/MaturityMatrix_01B-35.pdf"
ATBD33 = "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf"
README33 = "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.3/doc/README.GPCPV3.3_Daily.pdf"
# NASA GES DISC + PPS A2 resilience run (2026-11-27)
GD_FORUM = "https://forum.earthdata.nasa.gov/viewtopic.php?t=8190"
WGISS61 = "https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-61/8.7%20WGISS-61%20NASA_s%20evolving%20Archive%20Guidelines%20for%20the%20cloud.pdf"
OIG_DAAC = "https://oig.nasa.gov/docs/IG-20-011.pdf"
OIG_OPEN26 = "https://oig.nasa.gov/wp-content/uploads/2026/10/or-10-26.pdf"
ADURD = "https://www.earthdata.nasa.gov/s3fs-public/imported/423-10-69_ADURD_RevB.pdf"
CMR_GRANULE = "https://cmr.earthdata.nasa.gov/search/granules.umm_json?short_name=GPM_3IMERGHHL&version=07&page_size=1"
ORCA_BUCKET = "https://nasa.github.io/cumulus-orca/docs/developer/deployment-guide/deployment-s3-bucket"
ORCA_RECON = "https://nasa.github.io/cumulus-orca/docs/developer/research/research-reconciliation"
LZARDS = "https://nasa.github.io/cumulus/docs/workflow_tasks/lzards_backup/"
CTS_LIST = "https://amt.coretrustseal.org/certificates/"
WDS_GESDISC = "https://worlddatasystem.org/member-highlight-goddard-earth-sciences-data-and-information-services-center/"
EDL_STATUS = "https://status.earthdata.nasa.gov/client_applications/21/history"
EDL_STATUS2 = "https://status.earthdata.nasa.gov/client_applications/21/history?page=2"
ENX = "https://sam.gov/workspace/contract/opp/155dc55f43934efe8e91537863f990b7/view"
ENX_FORECAST = "https://www.highergov.com/contract-forecast/earth-science-data-and-information-system-esdis-1121962"
IA_HISTORY = "https://www.earthdata.nasa.gov/data/alerts-outages/content/data-alert-history/17367"
GESDISC_ALERTS = "https://disc.gsfc.nasa.gov/information/alerts"
RELNOTES = "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf"
C01726 = "https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C01726.xml"
C00999 = "https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C00999.xml"
NCEI_2026 = "https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2026/"
CMR_LATEST = "https://cmr.earthdata.nasa.gov/search/granules.json?short_name=GPCPDAY&version=3.3&sort_key=-start_date&page_size=2"
HUFFMAN = "https://science.gsfc.nasa.gov/sci/bio/george.j.huffman"
BOLVIN = "https://science.gsfc.nasa.gov/earth/bio/david.t.bolvin"
NELKIN = "https://science.gsfc.nasa.gov/earth/bio/eric.j.nelkin"
EGU26 = "https://meetingorganizer.copernicus.org/EGU26/EGU26-5885.html"
UA23 = "https://has.arizona.edu/news/ali-behrangi-named-principal-investigator-new-3-million-nasa-grant-advance-global"
UA_HB = "https://has.arizona.edu/sites/default/files/2026-08/ATMO-PhD-Handbook-draft-FINAL_Fall_2026.pdf"
R2O = "https://www.ncei.noaa.gov/pub/data/sds/cdr/Guidelines/Transitioning_CDRs_from_R2O.pdf"
CISESS_AW = "https://api.usaspending.gov/api/v2/awards/ASST_NON_NA24NESX432C0001_1330/"
NASA26 = "https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf"
NASA27 = "https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf"
ESDS26 = "https://espo.nasa.gov/sites/default/files/documents/2026-05/D2_0915_Scott_ESDS-Updates.pdf"
TOWNHALL = "https://assets.science.nasa.gov/content/dam/science/esd/earth-science-division/resources/ESD%20Town%20Hall%2012162025.pdf"
JES26 = "https://www.appropriations.senate.gov/imo/media/doc/fy26_cjs_jes.pdf"
CJ26 = "https://www.noaa.gov/sites/default/files/2025-06/NOAA%20FY26%20Congressional%20Justification.pdf"
CJ27 = "https://www.noaa.gov/sites/default/files/2026-04/FY2027-NOAA-CJ-Submission.pdf"
HR652 = "https://www.govinfo.gov/content/pkg/CRPT-119hrpt652/html/CRPT-119hrpt652.htm"
SEN27 = "https://www.appropriations.senate.gov/imo/media/doc/cjs_explanatory_stmt.pdf"
SRPT44 = "https://www.govinfo.gov/content/pkg/CRPT-119srpt44/html/CRPT-119srpt44.htm"
S3923 = "https://www.govinfo.gov/content/pkg/BILLS-119s3923es/html/BILLS-119s3923es.htm"
OIG_GSFC = "https://oig.nasa.gov/wp-content/uploads/2026/06/final-memorandum-ig-26-005-review-of-goddard-space-flight-centers-transformation-efforts.pdf"
WARN = "https://labor.maryland.gov/Employment/pdf/warn-log-2025.pdf"
DBK = "https://dbknews.com/2025/09/23/umd-earth-science-researcher-funding-cuts"
EENEWS_CI = "https://www.eenews.net/articles/trump-cuts-would-cripple-noaas-wide-ranging-science-partnerships/"
GDEX_WD = "https://gdex.ucar.edu/resources/docs/gdex-strategy-to-wind-down-services-due-to-a-change-in-nsf-or-ncars-strategic-direction/"
EOS_NCAR = "https://eos.org/research-and-developments/judge-blocks-nsf-from-dismantling-ncar"
GDEX7 = "https://gdex.ucar.edu/datasets/d728007/"
GDEX9 = "https://gdex.ucar.edu/datasets/d728009/"
CDS_PAGE = "https://cds.climate.copernicus.eu/datasets/satellite-precipitation?tab=overview"
AWS_REG = "https://registry.opendata.aws/noaa-cdr-atmospheric/"
AWS_LIST = "https://noaa-cdr-precip-gpcp-daily-pds.s3.amazonaws.com/?list-type=2&max-keys=5"
CDR_BUCKET = "https://archive.data.noaa.gov/climatedatarecords#UMD_ESSIC/GPCP/Daily/GPCP-D-CDR_01B-35/"
DSMR163 = "https://repository.library.noaa.gov/view/noaa/34101/noaa_34101_DS1.pdf"
CTS = "https://dataverse.nl/api/access/datafile/469675"
OIG24 = "https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf"
CLOUD = "https://www.ncei.noaa.gov/news/cloud-migration"
CLOUD_FAQ = "https://www.ncei.noaa.gov/news/cloud-migration-FAQ"
ALERTS = "https://www.ncei.noaa.gov/alerts"
SOS25Q1 = "https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf"
WATCHDOG_AUG = "https://avlwatchdog.org/top-climate-scientists-departure-is-sign-of-brain-drain-at-noaa-hub-in-asheville-and-of-deep-cuts-to-research-across-the-country/"
NESDIS_2025 = "https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes/2025-notice-of-changes"
DMSP_EARTHDATA = "https://www.earthdata.nasa.gov/data/alerts-outages/status-update-dmsp-data-products"
OSPO_SSMIS = "https://www.ospo.noaa.gov/data/messages/2026/09/MSG_20260901_1930.html"
OSPO_WSFM = "https://ospo.noaa.gov/data/messages/2026/07/MSG_20260720_1313.html"
DMSP_LETTER = "https://www.hickenlooper.senate.gov/wp-content/uploads/2026/10/2026-DMSP-Continuity-Letter-Hickenlooper-Murkowski-King.pdf"
RSS_CDR = "https://www.ncei.noaa.gov/products/climate-data-records/ssmis-brightness-temperature-rss"
AQUA = "https://aqua.nasa.gov/sites/default/files/AquaStatus_May2025.pdf"
AIRS_WEEKLY = "https://airsnrt.jpl.nasa.gov/report/latest"
GRIDSAT = "https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Geostationary_IR_Channel_Brightness_Temperature/AlgorithmDescription_01B-02.pdf"
IMERG_V08 = "https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026"
GPROF_RECALL = "https://www.earthdata.nasa.gov/data/alerts-outages/all-l3-gprof-data-gpm-v08-being-recalled"
IMERG_ATBD = "https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf"
PRECIP_WP = "https://ntrs.nasa.gov/api/citations/20260008217/downloads/PrecipWhitePaper_V4.pdf"
SR2023 = "https://science.nasa.gov/wp-content/uploads/2024/02/response-to-2023-earth-science-senior-review-and-2022-2023-out-of-cycle-senior-reviews-final.pdf"
GAO_NASA = "https://files.gao.gov/reports/GAO-26-108556/index.html"
GAO_GEO = "https://files.gao.gov/reports/GAO-26-107739/index.html"
POES = "https://www.nesdis.noaa.gov/news/suspension-of-poes-data-users-after-june-16-2025-and-decommissioning"
SNPP = "https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026"
AMSR2 = "https://www.ospo.noaa.gov/data/messages/2026/07/MSG_20260728_1045.html"
AXIOS_CPC = "https://www.axios.com/2025/03/27/noaa-merges-climate-prediction-center"
MERGIR = "https://disc2.gesdisc.eosdis.nasa.gov/data/MERGED_IR/GPM_MERGIR.1/2026/"
EGU_GPCC = "https://meetingorganizer.copernicus.org/EGU26/EGU26-12777.html"
CPC_GSPDC = "https://www.cpc.ncep.noaa.gov/products/global_precip/html/wpage.gspdc.shtml"
AWS_SPONSOR = "https://aws.amazon.com/opendata/open-data-sponsorship-program/"
GOOGLE_PD = "https://docs.cloud.google.com/bigquery/public-data"
AWS_S3 = "https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html"
NODD_2019 = "https://www.noaa.gov/media-release/cloud-platforms-unleash-full-potential-of-noaa-s-environmental-data"
# Added from calibration-copies-pt7 (Run 2)
C01567 = "https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01567/html"
OSPO_F17 = "https://ospo.noaa.gov/data/messages/2026/03/MSG_20260326_1733.html"
NSIDC_SSMIS = "https://nsidc.org/data/user-resources/data-announcements/user-notice-ssmis-processing-will-now-continue-through-september-2026"
AFA_DMSP = "https://airandspaceforces.com/space-force-legacy-weather-sats-2028-replacements"
GPM_WSFM = "https://gpm.nasa.gov/data/news/new-wsf-m1-mwi-nrt-files-available"
CSU_FCDR = "https://rain.atmos.colostate.edu/FCDR/"
SR26_CALL = "https://assets.science.nasa.gov/content/dam/science/esd/earth-science-division/senior-reviews/2026/2026%20ESD%20Senior%20Review%20Call%20for%20Proposals_DRAFT20251219.pdf"
SR26 = "https://science.nasa.gov/earth-science/senior-review-2026/"
PMM23 = "https://science.nasa.gov/science-research/earth-science/summary-of-the-2023-precipitation-measurement-mission-science-team-meeting/"
NTRS_GPM = "https://ntrs.nasa.gov/citations/20240004796"
NTRS_AOS = "https://ntrs.nasa.gov/citations/20230007913"
IPWG26 = "https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf"
AQUA23 = "https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf"
AQUA_PAGE = "https://science.nasa.gov/mission/aqua/"
CMORPH = "https://www.ncei.noaa.gov/products/climate-data-records/precipitation-cmorph"
PERSIANN = "https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann"
MSWEP = "https://www.gloh2o.org/mswep/"
CHIRPS = "https://www.chc.ucsb.edu/data/chirps"
GPCC_DWD = "https://www.dwd.de/EN/ourservices/gpcc/gpcc.html"
V08_REPRO = "https://www.earthdata.nasa.gov/data/alerts-outages/gpm-version-08-reprocessing"
HESS26 = "https://hess.copernicus.org/articles/30/3399/2026/"
CDS_API = "https://cds.climate.copernicus.eu/api/catalogue/v1/collections/satellite-precipitation"
ESGF = "https://esgf-node.ornl.gov/proxy/search?project=obs4MIPs&query=GPCP&type=Dataset&format=application%2Fsolr%2Bjson&limit=30"
UMD_GP = "https://essic.umd.edu/globalprecipitation/"
GSFC_BACKUP = "https://meso.gsfc.nasa.gov/pub/gpcp-v3/"

# ---------------------------------------------------------------- People risk
P1 = [
    (M, PT7, f"A search aimed at one found no GPCP team size and no succession or knowledge-transfer plan, and no page read names a successor for anyone. The only knowledge-transfer rule found is the NOAA CDR Program's research-to-operations process ([CDRP-PLAN-0017, 2014]({R2O})), which is generic.", "F"),
    (H, PT7, f"For 1DD V1.3, the CDR Program's handover package exists at NCEI: the C-ATBD, a data-flow diagram, a maturity matrix (2017-08-14) and the source code `SourceCode_01B-35.tar.gz` (2017-09-18), delivered to reach Initial Operational Capability ([NCEI CDR folder]({CDR_DIR})). NCEI holds nothing of the kind for V3.x, and no Operational Algorithm Description for either.", "A"),
    (H, PT2, f"The V3.x method is written down in detail: the V3.3 Daily ATBD (last revised 2026-06-12) with a step-by-step flowchart ([ATBD]({ATBD33})), the README (2025-05-28; [README]({README33})) and the release notes ([V3.3 Release Notes]({RELNOTES})). V1.3 has its C-ATBD ([C-ATBD]({CATBD})).", "A"),
    (H, PT3, "The team is small and long-standing: an active core of about 8 named people (Adler and Gu at UMD/ESSIC; Huffman, Bolvin and Nelkin at NASA Goddard; Behrangi, Song and Kumah at the University of Arizona), several of whom have worked on GPCP since the 1990s. No published head count exists; author lists give 6 to 8.", "C"),
    (M, PT7, f"The bench has shrunk: Jian-Jian Wang and Mathew Sapiano (UMD, 1DD V1.3 collaborators in 2017) are no longer on GPCP (Sapiano at CDC since 2015), so the core fell from about 8 to about 6 ([EGU26-5885]({EGU26})).", "C"),
    (H, PT3, f"Until 2016 GPCP was \"produced by a consortium of individual scientists\"; moving it into the CDR Program was meant to \"formalize its production under NOAA's commitment\" ([C-ATBD]({CATBD})).", "C"),
    (M, PT4, f"Both producing institutions lost staff in 2025: about 25 ESSIC scientists were told their funding would end ([The Diamondback, 2025]({DBK})) and Goddard lost about a third of its civil servants ([NASA OIG IG-26-005]({OIG_GSFC})). No source names any GPCP team member.", "C"),
]
P1_GAPS = [
    ("S", "A written succession or knowledge-transfer plan for GPCP at NASA Goddard, UMD/ESSIC or the University of Arizona."),
    ("S", "The GPCP team's size; only author lists are published."),
]

P2 = [
    (H, PT3, "The people most tied to production are George Huffman (NASA GSFC, lead developer of 1DD and V3), Robert Adler (UMD/ESSIC, PI of both NCEI CDRs) and Ali Behrangi (University of Arizona, MEaSUREs PI), with David Bolvin and Eric Nelkin (Goddard contractors) and Guojun Gu (UMD).", "C"),
    (L, PT7, f"Estimate, not a personnel record (earliest publication year minus 25–30; FERS rules): George Huffman (BS 1976, PhD 1982, earliest publication 1980) is about 71–76, a federal employee since September 2012 (one source, his [NASA bio]({HUFFMAN})), so very likely eligible to retire now under FERS (age 62 with 5 years).", "F"),
    (L, PT7, "Estimate: Robert Adler (earliest publication 1973–1981) is about 78–83 and still active (ESSIC summaries to November 2026). As university staff no federal rule applies, but he is past any usual retirement age.", "F"),
    (L, PT7, f"Estimate: David Bolvin (about 60–65) and Eric Nelkin (about 59–64) are contractors with Science and Technology Corp, so FERS does not apply ([Bolvin]({BOLVIN}); [Nelkin]({NELKIN})).", "C"),
    (L, PT7, "Estimate: Ali Behrangi (about 44–49) and Guojun Gu (about 50–62) are university staff and not near retirement.", "A"),
    (M, PT7, "Departures so far are not retirements: Wang and Sapiano left GPCP work (last GPCP papers 2021).", "C"),
]
P2_GAPS = [
    ("P", "Real ages and service dates (personnel records); the estimates are proxies."),
    ("S", "Huffman's federal start date from a second source; Gu's earliest publication; Wang's current employer."),
]

P3 = [
    (H, PT2, f"1DD V1.3's production code is public: `SourceCode_01B-35.tar.gz` (about 150 files in 6 modules plus 4 utilities, one shell-script driver; shell, Fortran, C and MATLAB), offered \"for reference only\" and \"not intended to be portable\" ([NCEI]({SRC_TAR})). It passed the CDR Program's code delivery ([NCEI C00999]({C00999})).", "A"),
    (M, PT2, f"No V3.2 or V3.3 code is published: none was found at NCEI, GES DISC or on GitHub, and no statement on sharing it on request was found (pt7). NCEI's V3.3 record links the 2017 V1.3 tarball as \"CDR Source Code (GPCP Daily v3.3)\", which looks like a metadata carry-over ([NCEI C01726]({C01726})).", "F"),
    (H, PT2, f"The V3.3 processing is documented step by step: IMERG averaged to 0.5° daily, TOVS/AIRS histogram-matched to IMERG, \"feathered\" at 55°, and each day ratio-scaled to the monthly, with named steps (COMPHIST, AIRS2IMERG, CORR_T, FUSE, SCALEME, BLD_NETCDF) ([V3.3 Daily ATBD]({ATBD33}); [README]({README33})).", "A"),
    (L, PT2, f"The 2017 maturity matrix for V1.3 rates Software Readiness about 5 and Documentation about 4, read from cell shading only ([Maturity Matrix 01B-35]({MATRIX})).", "A"),
    (H, PT2, "Output QC includes a monthly manual review: \"diagnostic analyses and plots of the output products are performed every month, with comparison to climatologies\" (V1.3), and diagnostic plots compared with climatologies and V3.2 (V3.3). Who does it and how is not written beyond that.", "C"),
]
P3_GAPS = [
    ("S", "Whether the V3.x code is shared on request, and where it is kept (Goddard Code 612 systems)."),
    ("U", "The contents and licences of the 2017 code package (not downloaded; only one or two file headers read)."),
]

P4 = [
    (M, PT7, f"Huffman is the one federal employee and the sole reviser of the V3.3 ATBD (June 2026); his job line reads \"Produce, revise, analyze GPCP Satellite-Gauge and One-Degree Daily data sets\", and his bio says V3 is \"computed at Goddard\" ([NASA GSFC]({HUFFMAN})). The run reads this as supporting P-4 for V3.x.", "F"),
    (M, PT7, "Production is shared, not held by one person: the Goddard production side is three people (Huffman, Bolvin, Nelkin), UMD/ESSIC (Adler, Gu) is NCEI's producer of record, and the University of Arizona group (Behrangi, Song, Kumah) leads V4.", "A"),
    (M, PT7, f"The two Goddard contractors moved from SSAI to Science and Technology Corp, now under the ATMOS contract (80GSFC26D0002, from 11/30/25, ordering to 12/1/30), with no change of people ([Bolvin]({BOLVIN}); [Nelkin]({NELKIN})). That they are paid under it is the run's inference.", "C"),
    (M, PT4, f"SSAI filed Maryland WARN layoffs of 148 (April 2025) and 79 (August 2025), and Goddard's atmospheres support moved to STC ([Maryland WARN log 2025]({WARN})). None names Code 612 or GPCP staff.", "C"),
    (L, PT7, "Who runs 1DD V1.3 is in conflict: NCEI says UMD computes it, while Huffman's job line says he produces the One-Degree Daily. Who computes NCEI's V3.3 copy is also unresolved (UMD per NCEI, Goddard per NASA); the run's likeliest reading is that Goddard runs the code and UMD is NCEI's producer of record (low).", "C"),
]
P4_GAPS = [
    ("S", "Who computes each version each month, and who is the backup if Huffman leaves."),
    ("P", "Which contract and task now pays Bolvin and Nelkin (not named in any document)."),
]

# ---------------------------------------------------------------- Data risk
D1 = [
    (H, PT4, f"NOAA's FY2027 request cuts NCEI, which archives and serves both CDRs, to $52.0M (−$17.8M); the House committee gives $60.0M and the Senate committee $70.0M; FY2027 runs on a continuing resolution to December 11, 2026 ([NOAA FY2027 CJ]({CJ27}); [H.Rept. 119-652]({HR652}); [Senate statement]({SEN27})). Pending.", "F"),
    (M, PT4, f"NASA's FY2027 request puts Earth Science Data Systems (which funds MEaSUREs and GES DISC) at $124.8M, does not name MEaSUREs and adds a new Foundational Data Products project; Earth Science as a whole falls to $1,021.2M against $2.153B enacted for FY2026 ([NASA FY2027 request]({NASA27})). Pending: the House gives $1.325B, the Senate committee $2.1879B.", "F"),
    (M, PT4, f"GDEX, which redistributes V1.3 and V3.2, sits at NCAR, whose break-up by NSF was announced in December 2025; a June 2026 injunction blocked one part ([Eos, 2026]({EOS_NCAR})), and GDEX has a wind-down plan ([GDEX]({GDEX_WD})). This hits a copy, not the archives of record.", "F"),
    (M, PT7, f"Behrangi's MEaSUREs award was announced in 2023 as \"$3 million ... for 5 more years\" ([U. Arizona, 2023]({UA23})); a Fall 2026 handbook dates the NASA support \"(2017-2028)\" ([UA handbook]({UA_HB}), low, not an award record). No source says the award was shortened. The award number was not found.", "A"),
    (M, PT4, f"The CISESS cooperative agreement with UMD/ESSIC, which supports routine CDR production, runs 2024-07-01 to 2029-06-30 with $77,486,317 obligated and was last modified 2026-09-30 ([USAspending]({CISESS_AW})). GPCP's share is not published.", "A"),
    (H, PT4, f"NASA's FY2026 request said MEaSUREs \"will complete current projects by the end of CY 2026 and cancel future selections\" and cut ESDS from 311.5 to 114.6 $M ([NASA FY2026 Technical Supplement]({NASA26})). Congress rejected the Earth Science cut ($2.153B enacted; [FY2026 JES]({JES26})).", "C"),
    (H, NCEI, f"NCEI's FY2026 request was also $52.0M; Congress enacted $69.0M ([FY2026 JES]({JES26})). Rejected.", "C"),
    (M, PT4, f"Cooperative institutes in general were threatened: an OMB proposal to terminate their funding (April 2025), payment delays and a February 2026 grant pause ([E&E News, 2025]({EENEWS_CI})); the FY2027 request ends OAR's institutes. None of these names CISESS, which NESDIS funds.", "C"),
    (M, PT4, "GEWEX's project office (oversight of GPCP, not production) had uncertain 2025 funding until NASA's Year 1 support arrived; WCRP called losing NSF funding \"highly likely\".", "C"),
    (M, NCEI, f"NCEI's cloud-migration FAQ says \"No datasets will be retired as part of the cloud migration\" ([NCEI FAQ]({CLOUD_FAQ})); no NESDIS notice names GPCP.", "C"),
]
D1_GAPS = [
    ("P", "Behrangi's MEaSUREs award number and end date (NASA award records)."),
    ("P", "GPCP's share of the CISESS agreement; NCEI's and NASA's FY2026 operating plans."),
    ("S", "The FY2027 outcome after the December 11, 2026 continuing resolution."),
]

D2 = [
    (H, NCEI_A2, f"Both GPCP Daily CDRs are \"Archived at NOAA NCEI-NC\" (Asheville) ([DSMR-00163]({DSMR163})). Asheville's two tape copies sit close together, the offsite one \"several kilometers away\" ([CoreTrustSeal application]({CTS})), and no source names a copy in Boulder.", "F"),
    (M, NCEI_A2, f"NCEI is moving all its data to AWS through spring 2027 as a \"lift and shift\" ([NCEI]({CLOUD})); OIG found the target platform \"resides in a single region\" ([OIG-24-034-A]({OIG24})). Its single-region recommendation is listed \"Closed\" with no published action, and the production regions are not published.", "F"),
    (H, PT1, f"GPCP Daily is served by several organizations: NCEI (HTTPS, and V3.3 from its open-data bucket), NOAA's NODD copies on AWS and Google, NASA GES DISC (V3.2 and V3.3, Earthdata Cloud), NCAR GDEX ([d728007]({GDEX7}), [d728009]({GDEX9})) and Copernicus CDS ([CDS]({CDS_PAGE})). Each version has at least two.", "A"),
    (L, NCEI_A2, f"GPCP Daily also has a copy in NCEI's own `climatedatarecords` cloud bucket, with year folders 1998–2025 ([NCEI archive S3]({CDR_BUCKET})); its region and number of copies were not seen.", "A"),
    (M, GDP, f"GES DISC, the archive of record for V3.x, stores its data in \"the AWS region US West (Oregon), or us-west-2\" ([GES DISC, Earthdata Forum, 2026]({GD_FORUM})). ESDIS counts Availability Zones \"up to 60 miles\" apart within one Region as its off-site copy ([ESDIS, WGISS-61, 2026]({WGISS61})), and NASA's inspector general recorded ESDIS calling one-vendor storage \"a single point of failure\" ([IG-20-011, 2020]({OIG_DAAC})); no later document says a backup outside that vendor was built. The run found no PPS copy of GPCP.", "F"),
    (M, PT7B, f"Outside NOAA, 1DD V1.3's copies are stale: NCAR GDEX holds it to 2024-11-01 ([GDEX d728007]({GDEX7})) and Copernicus CDS to March 2024 ([CDS]({CDS_PAGE})); the GSFC backup folder was unreachable ([GSFC]({GSFC_BACKUP})). V1.3's current data are held only by NCEI and its NODD copies.", "F"),
    (M, PT7B, f"V3.3 Daily is current off NASA's systems: Copernicus CDS (Europe) holds it through 2025-12-31, the same end as GES DISC's record, updated twice a year (catalogue updated 2026-10-06; [CDS catalogue]({CDS_API})), and ESGF obs4MIPs holds a reformatted copy (v20260220) at two US DOE sites, ORNL and NERSC ([ESGF]({ESGF})).", "A"),
]
D2_GAPS = [
    ("P", "Whether GES DISC holds any copy of V3.x outside us-west-2, or runs Cumulus's ORCA backup (ESDIS holds this; not public)."),
    ("P", "NCEI's production AWS regions, and whether the Asheville tapes are kept after the move."),
]

D3 = [
    (H, NCEI_A2, f"NCEI's severity-high alert (November 16–30, 2026) says \"Many access portals, interactive maps, and data folders are currently unavailable\" and to \"Expect delayed data archival\" ([NCEI Alerts]({ALERTS})).", "F"),
    (H, PT4, f"NCEI's FY2027 request is $52.0M, $17.8M below its base, pending under a continuing resolution to December 11, 2026 ([NOAA FY2027 CJ]({CJ27})).", "F"),
    (M, GH_REPO, f"The NODD cloud copies rest on 2019 multiyear contracts with AWS and Google with no published end date ([NOAA, 2019]({NODD_2019})); NODD has no enacted budget line found, and NOAA calls it \"no net cost to the taxpayer\".", "F"),
    (M, PT4, f"NASA plans to consolidate its 11 data centers, GES DISC among them, \"to thematic science enabling teams\" ([NASA ESDS, May 2026]({ESDS26})) and lists \"Risks associated with data system consolidation\" as a known issue ([ESD town hall, Dec 2025]({TOWNHALL})). ESDS's FY2027 request is $124.8M, pending.", "F"),
    (M, PT4, f"GDEX's copies are at risk from NSF's planned NCAR break-up; its wind-down plan points users of copied datasets to NCEI ([GDEX]({GDEX_WD})).", "F"),
    (L, PT1, "NCEI's V3.3 landing page returned HTTP 503 during the run and has no Wayback copy; its ISO XML was read instead.", "F"),
    (H, PT2, "GES DISC needs an Earthdata Login and Copernicus CDS a login and licence acceptance; NCEI's HTTPS and S3 routes and GDEX need none.", "C"),
    (M, GDP, f"ESDIS's support contract EED-3 ends January 31, 2027, and its successor, ESDIS Next (ENX), is still only a sources-sought notice: SAM.gov marks it \"Inactive\" and says \"No solicitation exists\" (last updated 2026-10-23; [SAM.gov]({ENX})), against a forecast award in the third quarter of FY2026 ([HigherGov]({ENX_FORECAST})).", "F"),
    (M, GDP, f"Earthdata Login, which every GES DISC download goes through, had token generation degraded from December 16 to 21, 2025, and shorter degraded spells on seven days between December 2025 and November 19, 2026 ([Earthdata Status]({EDL_STATUS}); [page 2]({EDL_STATUS2})).", "F"),
]
D3_GAPS = [
    ("U", "Funding and staffing of Copernicus CDS (no repository run)."),
    ("S", "The ENX award for ESDIS, which supports GES DISC (none by November 2026; SAM.gov notice RFI-NASA-GSFC-ENX)."),
    ("P", "NODD contract end dates for AWS and Google."),
]

D4 = [
    (H, PT2, "Every main route serves open, CF-labelled netCDF-4 (NCEI HTTPS and S3, NODD, GES DISC with CF-1.5, GDEX, CDS with CF-1.6 and ACDD-1.3), readable with generic netCDF tools; no proprietary software is needed. NCEI's HTTPS and S3 copies and GDEX's are rated fully FAIR.", "A"),
    (M, PT2, "Licences differ by route (CC0 at data.gov, CC BY 4.0 at GDEX, GPCP's own licence at CDS, none named at GES DISC), and GES DISC and CDS need a login, so those two routes are only partly FAIR. This is access, not format.", "C"),
    (M, PT2, "The NODD bucket's contents, obs4MIPs/ESGF and Google Earth Engine copies were not checked; Earth Engine would be a third-party format.", "C"),
]
D4_GAPS = [
    ("U", "Which version and format the NODD AWS and Google buckets hold."),
]

D5 = [
    (M, PT4, "About 40 news searches (January 2024 – November 2026) found no item naming GPCP, GPCP Daily or its named people in coverage of cuts; no NESDIS notice of changes names GPCP.", "A"),
    (H, NCEI, f"The Senate says NOAA \"has decommissioned at least 20 datasets, products and catalogs\" without notice ([S.Rept. 119-44]({SRPT44})); none is named. S. 3923 would keep the archive at \"NCEI, or a successor entity\" ([S. 3923]({S3923})).", "C"),
    (M, PT4, "Goddard staff said they were \"constantly being attacked\" (NPR, November 2025) as buildings closed; the FY2027 NASA request plans to end 53 science missions. None names GPCP.", "C"),
]
D5_GAPS = [
    ("S", "Any data rescue snapshot or news naming GPCP Daily."),
]

# ---------------------------------------------------------------- Dependent infrastructure resilience
DIRS1 = [
    (H, PT1, f"1DD V1.3 is calibrated by microwave: each month its IR threshold is set so IR \"cold\" coverage matches SSM/I–SSMIS rain frequency, from DMSP F17 SSMIS alone since 2009 ([C-ATBD]({CATBD})). DoD's DMSP delivery to NOAA changed on October 1, 2026 ([OSPO]({OSPO_SSMIS})).", "F"),
    (M, PT7B, f"Which SSMIS feed calibrates 1DD now is not published. The 2017 code README names only \"RSS SSMIS files\" ([NCEI code package]({SRC_TAR})); NCEI's record for the RSS V8 SSMIS CDR has data \"through July 31, 2025\" and status \"Complete\" ([NCEI C01567]({C01567})). No GPCP, NCEI or GES DISC page says what replaced it. (NCEI's product page still says the CDR \"extends from 1987–2023\" ([NCEI]({RSS_CDR})); the metadata record is newer.)", "F"),
    (H, PT7B, f"The F17 feed itself is disrupted: FNMOC's PolarProd ended and from October 1, 2026 DMSP files go \"directly to NCCF\" under new names, with the F-17 and F-18 scan products in BUFR and HDF to \"be discontinued\" ([NOAA OSPO]({OSPO_SSMIS})). F-17 was out for 4 days (21–25 March 2026), traced to FNMOC, and F-16 and F-18 also had outages ([NOAA OSPO, Mar 2026]({OSPO_F17})).", "F"),
    (M, PT7B, f"No funded reference is named for after GPM. GPM is in the 2026 Senior Review (FY2027–29), but no GPM outcome was found ([NASA Senior Review]({SR26}); [call]({SR26_CALL})); its fuel lasts to December 2027 counting fuel alone, with the end forecast for \"the late 2020's\" ([NASA PMM, 2024]({PMM23}); [NTRS]({NTRS_GPM})). NASA wants GPM to overlap with AOS for cross-calibration ([NTRS, 2023]({NTRS_AOS})), and a GSFC white paper says JAXA's PMM, which lacks 19–37 GHz radiometer channels, \"may be insufficient\" as the next reference ([NASA GSFC, 2026]({PRECIP_WP})).", "F"),
    (M, PT7B, f"Who keeps the SSMIS intercalibration behind 1DD is not published. NASA PPS (X-CAL) has intercalibrated the new WSF-M1 MWI into GPM's near-real-time files since 12 Aug 2026 ([GPM]({GPM_WSFM})), and CSU says its SSM/I–SSMIS FCDR continues but names no version, funding or reference sensor ([CSU]({CSU_FCDR})). Neither is on 1DD's documented input list.", "C"),
    (H, PT5, f"GridSat-B1's calibration source, HIRS all-sky data, \"ceased in 2024\"; V3.3 was \"paused at March 2024 while NCEI is developing a new calibration procedure for the GridSat IR input\" ([V3.3 Release Notes]({RELNOTES})) for more than a year, until GridSat was recalibrated with VIIRS VGAC ([GridSat C-ATBD Rev 2]({GRIDSAT})).", "F"),
    (M, NASA_SAT, f"V3.x rests on IMERG, which uses GPM's GMI, calibrated to the DPR-GMI combined product, as the calibrator \"for all the other satellite precipitation estimates\" ([IMERG ATBD]({IMERG_ATBD})). GPM has no funding of its own after FY2026 in the FY2026 and FY2027 requests, and a NASA white paper says its successor PMM \"may be insufficient to serve as the next reference\" ([NASA GSFC, 2026]({PRECIP_WP})).", "F"),
    (M, PT2, "Some calibration is done by the input producers: RSS quality-controls and intercalibrates the SSM/I data V1.3 uses, and GPCC quality-controls the gauges. V3.x's own step (histogram-matching TOVS/AIRS to IMERG) is done in-house.", "C"),
]
DIRS1_GAPS = [
    ("S", "Which SSMIS feed calibrates 1DD since the RSS V8 CDR ended (2025-07-31), and whether it survives FNMOC's October 2026 change. The GPCP team at Goddard (Code 612) and NCEI's CDR program hold it; ask the GES DISC or NCEI help desk."),
    ("S", "How IMERG, and so V3.x, would be calibrated after GPM, and GPM's 2026 Senior Review outcome (not yet posted)."),
    ("S", "Who maintains the SSMIS intercalibration 1DD relies on."),
]

DIRS2 = [
    (H, PT5, f"DMSP SSMIS, 1DD V1.3's only microwave input since 2009 (F17), is more than a decade past expected end of life. DoD set data cutoffs for June 30 and then July 31, 2025, extended sharing to September 2026, and now plans to run DMSP to \"no earlier than 2028\" ([Senators' letter, Oct 2026]({DMSP_LETTER})); delivery changed on October 1, 2026, with outages in June 2026 ([NASA Earthdata]({DMSP_EARTHDATA})).", "F"),
    (H, PT5, f"Aqua AIRS, the only sounder in both families' high latitudes since 2002–2003, is on a drifting satellite: a May 2025 plan ended its science on August 26, 2026, with passivation November 4, 2026 ([Aqua status]({AQUA})); AIRS was still operating on October 30, 2026 ([AIRS weekly report]({AIRS_WEEKLY})).", "F"),
    (H, PT7B, f"AIRS is past its planned end and degrading: a 2023 plan set instrument shutdown for 26 Aug 2026 and passivation for 4 Nov 2026 ([NASA Aqua, 2023]({AQUA23})). AIRS was \"healthy\" on 30 Oct 2026, but since 4 Oct 2026 its L1B files carry an advisory about telemetry out-of-limit flags caused by Aqua's orbital drift ([JPL AIRS report]({AIRS_WEEKLY})).", "F"),
    (M, PT7B, f"The 2026 Senior Review recommended that Aqua continue into FY2027 ([NASA Aqua]({AQUA_PAGE})). That extends AIRS by about a year on a drifting satellite; it does not remove the risk.", "C"),
    (M, PT7B, f"DMSP's end date is in conflict: DoD, via NSIDC, said SSMIS processing continues \"through the retirement of the DMSP mission, which is expected in September 2026\", with gaps since spring 2025 ([NSIDC, 2025]({NSIDC_SSMIS})); a press report says the FY2026 NDAA keeps DMSP running \"no earlier than 2028\" ([Air & Space Forces, Aug 2026]({AFA_DMSP})). Either way F17, 1DD's only microwave sensor, is at the end of its life.", "F"),
    (M, PT7B, f"GPM Core's end is near: its fuel lasts to December 2027 counting fuel alone, with the end forecast for \"the late 2020's\" ([NASA PMM, 2024]({PMM23}); [NTRS]({NTRS_GPM})), and no 2026 Senior Review outcome for GPM was found ([NASA Senior Review]({SR26})).", "F"),
    (M, NOAA_SAT, f"Microwave satellites inside IMERG, which feeds V3.x, have been lost: NOAA-15, -18 and -19 (data ended June 16, 2025; [NESDIS]({POES})), Suomi NPP ATMS (November 2, 2026; [NESDIS]({SNPP})) and AMSR2's near-real-time feed (September 2026; [OSPO]({AMSR2})).", "F"),
    (H, NASA_SAT, f"GPM Core, IMERG's anchor, is past its 3-year prime mission; NASA's 2023 review extended it \"through FY 2026\" ([NASA]({SR2023})), the FY2026 and FY2027 requests give it $0 on its own line after FY2026, and the 2026 Senior Review result is not published. IMERG documents estimate its data to December 2029, and PMM's launch is about March 2030.", "F"),
    (H, NOAA_SAT, f"Geostationary IR (GOES, Meteosat, Himawari) is working; GAO projects a gap in the spare from October 2032 to early 2033 ([GAO-26-107739]({GAO_GEO})). No current threat to GPCP's IR.", "C"),
    (M, PT5, "TOVS/HIRS on NOAA POES was decommissioned in 2025, but GPCP uses TOVS only for 1996–2002, so the ongoing record is not affected.", "C"),
    (M, PT5, f"GPCC's gauge analysis (via the monthly) shows no funding cut or station loss; it merged its products into Monthly V2025 ([EGU26-12777]({EGU_GPCC})).", "C"),
]
DIRS2_GAPS = [
    ("S", "DMSP's actual end date (September 2026 or \"no earlier than 2028\"); no DoD page settles it. FNMOC's notice shows deliveries going on past September 2026."),
    ("S", "Aqua's actual end-of-science date (continued into FY2027 by the 2026 Senior Review)."),
]

DIRS3 = [
    (H, PT5, f"IMERG V07 Final, V3.3's main input in 55°N–S, ended at September 2025; V3.3 used IMERG Late for October–December 2025 ([V3.3 Daily ATBD]({ATBD33})). V08 Final slipped to \"fall 2026\" and was not out by November 20, 2026 ([NASA GPM]({IMERG_V08})), and all L3 GPROF V08 data were recalled on October 1, 2026 ([NASA Earthdata]({GPROF_RECALL})). V3.3 cannot be extended until V08 Final ships.", "F"),
    (H, PT5, f"The GridSat-B1 IR record paused V3.3 for more than a year (from March or September 2024) until NCEI recalibrated it; V3.3 resumed with no notice, its files extended through 2025 between February and May 2026 ([NASA CMR]({CMR_LATEST})).", "F"),
    (M, PT7B, f"1DD V1.3's SSMIS feed is undocumented since the RSS V8 SSMIS CDR it names ended at July 31, 2025 ([NCEI C01567]({C01567})). FNMOC's October 1, 2026 change sends DMSP files directly to NCCF under new names and drops the F-17 and F-18 BUFR and HDF scan products ([NOAA OSPO]({OSPO_SSMIS})).", "F"),
    (H, PT7B, f"The SSMIS supply has already broken: F-17 data were out for 4 days (21–25 March 2026) because of FNMOC, and F-16 and F-18 also had outages ([NOAA OSPO, Mar 2026]({OSPO_F17})).", "F"),
    (M, PT7B, f"UMD makes the GPCP Monthly Interim CDR, \"sponsored by NOAA NCEI\", with summaries to October 2026 ([UMD ESSIC]({UMD_GP})); the daily is scaled to the monthly.", "C"),
    (H, PT5, "Aqua AIRS estimates, the high-latitude input for both families, end with Aqua (science end planned August 2026; still operating October 30, 2026).", "F"),
    (L, PT4, "A search summary says NCEI's preliminary GPCP Monthly catalog for 2025 ends at February 2025; the run could not verify it.", "F"),
    (M, PT5, f"CPC's merged IR, 1DD's IR source and IMERG's since 2000, has daily files to November 20, 2026 ([GES DISC]({MERGIR})). CPC moved under the Weather Prediction Center in March 2025 ([Axios]({AXIOS_CPC})), with no tie to the IR product.", "C"),
    (M, PT5, "The GPCP Monthly the daily is scaled to is current (V2.3 final to August 2026; V3.3 to December 2025), and GPCC's gauge analysis shows no current threat.", "C"),
]
DIRS3_GAPS = [
    ("S", "How V3.3 will be extended past December 2025 (the V08 transition)."),
    ("S", "Whether NCEI's preliminary monthly feed is still updated."),
]

DIRS4 = [
    (M, PT3, f"1DD V1.3 relies on outside processing for its IR: CPC's GPCP Geostationary Satellite Precipitation Data Centre makes the 3-hourly IR histograms, \"processed and provided by Pingping Xie\" ([C-ATBD]({CATBD}); [CPC]({CPC_GSPDC})); TOVS data were \"obtained directly from Joel Susskind\" (GSFC).", "F"),
    (H, PT7B, f"V3.x's high-latitude AIRS/TOVS precipitation estimates are made outside the GPCP team: the NASA/GSFC Sounder Research Team supplies them ([V3.3 Daily ATBD, rev. 12 Jun 2026]({ATBD33})).", "F"),
    (M, PT3, f"The producers compute it on their own systems: NCEI's records say the analysis runs on \"moderate-sized workstations at the University of Maryland\" ([NCEI C01726]({C01726})), and Huffman's bio says V3 is \"computed at Goddard\".", "A"),
    (L, PT7, "Inference: NCEI holds no Operational Algorithm Description, which suggests GPCP Daily never reached Full Operational Capability, so NCEI does not run it and depends on UMD and Goddard to produce it.", "F"),
    (M, PT7, "No source names the computers either version runs on (Code 612 workstations or NASA's NCCS).", "C"),
    (M, PT4, "Goddard planned to empty 13 buildings and about 100 labs by March 2026; no source ties this to Code 612 or GPCP computing.", "C"),
]
DIRS4_GAPS = [
    ("S", "The machines that run V1.3 and V3.x, and whether CPC still makes 1DD's IR histograms."),
]

DIRS5 = [
    (H, PT6, "1DD V1.3 has one satellite of each kind: F17 SSMIS alone since January 2009 and Aqua AIRS alone since 2003, with no other microwave sensor in the algorithm and no successor named for V1.3. The run rates losing F17 as \"stops extension\".", "F"),
    (M, NASA_SAT, "No NASA statement was found on how IMERG would be calibrated after GPM; JAXA's PMM is the only planned GPM-class radar, and it may not serve as the reference alone.", "F"),
    (M, PT6, "V3.x gets about 30 microwave satellites through IMERG, many overlapping (for 2023–2025: GPM, F16–F18, AMSR2, MetOp-B/C and ATMS on three satellites), so losing one degrades it rather than stopping it.", "A"),
    (M, PT5, f"Successors exist or are planned: WSF-M1's data are operational to NOAA from July 2026 ([OSPO]({OSPO_WSFM})), and GPCP V4 (mid 2027 target) plans WSF-M MWI in place of SSMIS and AVHRR in place of TOVS/AIRS ([V3.3 Daily ATBD]({ATBD33})). Neither is in V1.3 or V3.3 now.", "C"),
    (M, PT7B, f"No written contingency exists for losing F17 or AIRS. 1DD V1.3 has no such document, and the V3.3 Daily ATBD says days without TOVS or AIRS data are \"set to missing\" outside 55°N–S ([V3.3 Daily ATBD]({ATBD33})).", "F"),
    (M, PT7B, f"When an input stopped, V3.3 used a stand-in: IMERG Late for October–December 2025 and GPROF V07 for December 2025, after IMERG V07 Final ended ([V3.3 Daily ATBD]({ATBD33})).", "A"),
    (M, PT7B, f"Other datasets could replace GPCP Daily in part: CMORPH CDR (global, 8 km, 1998–present; [NCEI]({CMORPH})), PERSIANN-CDR (60°S–60°N, 0.25°, 1982–present; [NCEI]({PERSIANN})), MSWEP (global, 0.1°, 1979–present, commercial terms; [GloH2O]({MSWEP})), CHIRPS (land only, 50°S–50°N; [UCSB]({CHIRPS})), GPCC Full Data Daily (land only, 1982–2019; [DWD]({GPCC_DWD})) and IMERG Final (V08 reprocessing began 9 March 2026; [Earthdata]({V08_REPRO})). None is an independent, global, gauge-calibrated daily record on GPCP's terms, and IMERG shares GPCP's GMI calibration.", "A"),
    (M, PT7B, f"In a 2026 test of 24 daily datasets, MSWEP V2.8 scored best and IMERG Final V7 did not beat GPCP V3.2 ([HESS, 2026]({HESS26})).", "C"),
    (M, PT7B, f"Behrangi's 2026 slides say the team is switching from TOVS/AIRS to AVHRR, with V4 targeted for mid-2027 ([Behrangi, IPWG 2026]({IPWG26})).", "C"),
]
DIRS5_GAPS = [
    ("S", "How much of GPCP Daily each substitute could replace; the IMERG, GSMaP and ERA5 producer pages were not read."),
    ("S", "A 1DD contingency plan if F17 or AIRS stops (none found)."),
]

# ---------------------------------------------------------------- Repository resilience
RRS1 = [
    (M, PT1, f"Copies are held by independent organizations in different places: NCEI (Asheville), GES DISC (AWS us-west-2), NODD on AWS (us-east-1) and Google, NCAR GDEX (Colorado) and Copernicus CDS (Europe) ([AWS registry]({AWS_REG}); [GDEX]({GDEX7}); [CDS]({CDS_PAGE})). No source says any copy is verified against another.", "F", "NOAA NCEI, NASA GES DISC, AWS and Google Cloud (NODD), NSF NCAR GDEX, Copernicus CDS"),
    (H, NCEI_A2, f"At NCEI both CDRs are archived in Asheville, whose offsite tape copy is \"several kilometers away\"; NCEI documents dispersed copies only for Boulder's own holdings ([CoreTrustSeal application]({CTS})). The run finds RRS-1 not shown for GPCP Daily.", "A", NCEI_R),
    (M, NCEI_A2, f"OIG found NCEI's cloud target \"resides in a single region\" ([OIG-24-034-A]({OIG24})); the recommendation is \"Closed\" with no published action, and the AWS regions after the move are not published.", "A", NCEI_R),
    (M, NCEI_A2, f"Nothing published says the NODD copies are checked against NCEI's archive; the bucket listing shows only S3 ETags ([AWS listing]({AWS_LIST})).", "A", NODD),
    (M, GDP, f"GES DISC keeps V3.x in one AWS Region (us-west-2) by design: ESDIS meets its \"1 copy located off-site\" rule with Availability Zones \"up to 60 miles\" apart, uses S3 versioning and object lock instead of extra copies ([ESDIS, WGISS-61, 2026]({WGISS61}); [GES DISC, Earthdata Forum]({GD_FORUM})), and was recorded calling one-vendor storage \"a single point of failure\" ([IG-20-011, 2020]({OIG_DAAC})). The run found no PPS copy of GPCP.", "A", GESDISC),
    (M, GDP, f"ESDIS's DAAC requirements ask for an off-site backup of products only as \"selected data products, depending on need\" ([ADURD Rev B, 2017]({ADURD})); whether GES DISC runs Cumulus's backup tools (ORCA, LZARDS), and in which Region, is not published ([ORCA]({ORCA_BUCKET}); [LZARDS]({LZARDS})).", "C", GESDISC),
    (M, PT1, "The copies are not all current: GDEX holds V1.3 to 2024-11-01 and V3.2; CDS holds v1.3 only to March 2024; which version the NODD buckets hold is not confirmed.", "A", "NSF NCAR GDEX, Copernicus CDS, AWS and Google Cloud (NODD)"),
    (L, NCEI_A2, f"NCEI's own `climatedatarecords` bucket holds a GPCP Daily copy (1998–2025) separate from NODD ([NCEI archive S3]({CDR_BUCKET})); its region and copies are unknown.", "C", NCEI_R),
    (M, PT7B, f"Copernicus CDS (ECMWF, Europe) holds V3.3 Daily through 2025-12-31, the same end as NASA's own record, updated twice a year (catalogue updated 2026-10-06; [CDS catalogue]({CDS_API})). With GES DISC that gives V3.3 two current copies on two continents.", "F", CDS),
    (M, PT7B, f"The other outside copies are behind: GDEX holds 1DD V1.3 only to 2024-11-01, about two years behind ([GDEX d728007]({GDEX7})), and V3.2 Daily to 2021-10-01, superseded by V3.3 ([GDEX d728009]({GDEX9})); CDS holds V1.3 only to March 2024.", "A", "NSF NCAR GDEX, Copernicus CDS"),
    (M, PT7B, f"ESGF obs4MIPs holds V3.3 Daily (version v20260220) at two US DOE sites, ORNL and NERSC, and V1.3 (v20180519, to 2016-12-31) at NASA NCCS only ([ESGF]({ESGF})). obs4MIPs files are rewritten to CMIP conventions, so it is filed here as a reformatted copy, not a repository (a categorizing call).", "C", "ESGF obs4MIPs (not a repository)"),
    (M, PT7B, f"The GSFC backup folder ([meso.gsfc.nasa.gov]({GSFC_BACKUP})) was unreachable and has no Wayback captures, and gpcp.umd.edu now points to a UMD page with monthly summaries only ([UMD ESSIC]({UMD_GP})); neither shows a Daily copy.", "C", "NASA GSFC, UMD ESSIC (not repositories)"),
]
RRS1_GAPS = [
    ("P", "Whether GES DISC holds any copy of V3.x outside us-west-2, or runs ORCA (ESDIS holds this)."),
    ("P", "NCEI's production AWS regions and copy count after the move."),
    ("S", "Which version the NODD buckets hold and whether it is current (asked in pt7 Run 2, not answered)."),
    ("S", "The GSFC backup folder's contents (unreachable); ESGF V3.3's last file date (its file search failed)."),
]

RRS2 = [
    (H, NCEI_A2, f"GPCP Daily v1.3's stewardship maturity report scores \"Data Integrity - 3.5\": checksums are \"generated at ingest\" and \"verified when customer orders data\", with no re-verification schedule, and \"No known external audits of the archive performed at this time\" ([DSMR-00163]({DSMR163})).", "A", NCEI_R),
    (H, NCEI_A2, f"NCEI's CoreTrustSeal application (certified to January 29, 2028) says a file's MD5 is checked \"Any time a file is pulled\" and that scripts compare file sizes between copies \"on a routine basis\", with no frequency ([CoreTrustSeal]({CTS})). The procedure (SOP 60-6-015) is not public.", "A", NCEI_R),
    (M, GH_RRS, f"AWS says S3 \"regularly\" verifies stored data with checksums, with no frequency ([AWS]({AWS_S3})); no NOAA or provider document says the NODD copy is verified against NCEI's.", "C", NODD),
    (M, GDP, f"ESDIS requires checksums at GES DISC only for transfers: each DAAC system \"shall ensure data integrity through the use of checksums\" at ingest, archive and distribution, with no re-check interval ([ADURD Rev B]({ADURD})). No checksum algorithm or check frequency is published for GES DISC or Earthdata Cloud, and the one NASA granule record checked (IMERG) carries no checksum.", "A", GESDISC),
    (H, GDP, f"GES DISC is not CoreTrustSeal-certified, though five other NASA data centers are ([CoreTrustSeal]({CTS_LIST})); it has been a World Data System Regular Member since September 2014 ([WDS]({WDS_GESDISC})).", "C", GESDISC),
]
RRS2_GAPS = [
    ("P", "Any fixity schedule at GES DISC or Earthdata Cloud (in ESDIS operations documents; GES DISC user services or a FOIA request)."),
    ("S", "Checksum practice at GDEX and CDS: neither copy's page shows checksums (pt7 Run 2)."),
    ("P", "NCEI's SOP 60-6-015."),
]

RRS3 = [
    (M, GH_RRS, f"OIG found that NCEI's cloud target platform, at its moderate impact level, does not offer \"testing contingency plans at alternate processing sites\" ([OIG-24-034-A]({OIG24})).", "A", NCEI_R),
    (H, NCEI_A2, f"NCEI has an Information System Contingency Plan with an annual Business Impact Analysis, daily and weekly off-site backups and COOP plans, but it \"cannot be shared outside the US Government\", and no test date or result appears anywhere ([CoreTrustSeal]({CTS})).", "C", NCEI_R),
    (M, GDP, f"Targeted searches found no published disaster recovery or continuity plan, and no record of a recovery test, for ESDIS or GES DISC. ESDIS requires each DAAC system to have \"the capability to restore its archive to avoid permanent loss of archived data\" ([ADURD Rev B]({ADURD})), but no test of it is published; the only documented exercise is Earthdata Login's failover test on February 12, 2026, which covers logins, not data ([Earthdata Status]({EDL_STATUS})).", "A", GESDISC),
]
RRS3_GAPS = [
    ("P", "NCEI's contingency-plan test results."),
    ("P", "GES DISC's and ESDIS's disaster recovery plans and test results (held at NASA Goddard; GES DISC user services or a FOIA request)."),
    ("U", "Disaster recovery plans at GDEX and CDS."),
]

RRS4 = [
    (H, NCEI, f"NCEI's FY2027 request is $52.0M (−$17.8M from a $69.8M base); the House committee gives $60.0M and the Senate committee $70.0M; a continuing resolution runs to December 11, 2026 ([NOAA FY2027 CJ]({CJ27})).", "A", NCEI_R),
    (M, NCEI, f"NCEI's staff fell from 184 FTE (FY2024) to 140 (FY2026 enacted column), with 58 departures by August 2025 ([Asheville Watchdog]({WATCHDOG_AUG})).", "A", NCEI_R),
    (M, NCEI, f"FY2026 was enacted above the request: $69.0M for NCEI ([FY2026 JES]({JES26})), and the FY2027 plan keeps \"the core mission of preserving, hosting, and providing access\" to the archives.", "F", NCEI_R),
    (M, PT4, f"GES DISC is funded inside NASA's Earth Science Data Systems, whose FY2027 request is $124.8M (FY2024 op plan 311.5 $M), with the data centers to be consolidated ([NASA FY2027 request]({NASA27}); [NASA ESDS]({ESDS26})). Pending.", "A", GESDISC),
    (M, GH_RRS, f"The NODD copies have no guaranteed term: AWS's sponsorship \"covers the cost of storing and sharing\" with no term stated ([AWS]({AWS_SPONSOR})), and Google states no SLA ([Google]({GOOGLE_PD})).", "A", NODD),
    (M, PT4, f"GDEX faces NSF's planned NCAR break-up (announced December 2025, partly blocked June 2026) and has a wind-down plan ([GDEX]({GDEX_WD})).", "A", GDEX),
    (M, GDP, f"NASA OIG's 2020 recommendation for an independent analysis of the cloud's long-term financial sustainability was still open on October 15, 2026 ([NASA OIG]({OIG_OPEN26})), and ESDIS says \"Our budgets are not in lock-step with our data growth\" ([ESDIS, WGISS-61]({WGISS61})).", "A", GESDISC),
    (M, GDP, f"ESDIS's support contract EED-3 ends January 31, 2027, and its successor, ENX, is still a sources-sought notice marked \"Inactive\" with \"No solicitation exists\" (last updated 2026-10-23; [SAM.gov]({ENX})).", "C", GESDISC),
]
RRS4_GAPS = [
    ("U", "Funding of Copernicus CDS."),
    ("P", "NCEI's and NASA's FY2026 spend plans; the FY2027 outcome."),
]

RRS5 = [
    (M, NCEI_A2, f"Hurricane Helene (September 2024): Asheville lost power, water and communications; ingest was restored by December 11 and \"92% of the ingest backlog was recovered\", with Boulder's help ([NCEI FY25 Q1]({SOS25Q1})). No loss of archived holdings was reported.", "F", NCEI_R),
    (M, NCEI_A2, "The 2015 NCDC-to-NCEI merger came with \"no products or services ... slated to be cut or reduced\", and no loss or backlog was reported.", "F", NCEI_R),
    (M, NCEI_A2, "The other 8% of Helene's ingest backlog is not accounted for, and no final loss count was published.", "A", NCEI_R),
    (M, NCEI, f"About 27 NCEI products were retired or cut back from April 2025 ([NESDIS 2025 Notice of Changes]({NESDIS_2025})); their existing data were kept. GPCP is not among them.", "A", NCEI_R),
    (M, NASA_SAT, "GES DISC kept distributing data through Goddard's 2025 workforce losses and the 43-day shutdown (October 1 – November 12, 2025), and released GPM V08 in spring 2026. No data loss was reported.", "F", GESDISC),
    (M, GDP, f"GES DISC's October 28–30, 2026 ingest pause for the consolidated ingest migration ended (resolved November 2) with search and download up and no loss reported ([Earthdata]({IA_HISTORY})); its alerts from August to November 2026 list service retirements and GPM V08 recalls but no lost granules ([GES DISC alerts]({GESDISC_ALERTS})). No after-action report was published, so \"no loss\" rests on silence.", "F", GESDISC),
    (M, NCEI_A2, f"NCEI's cloud move is a disruption still under way: its alert (November 16–30, 2026) says to \"Expect delayed data archival\" and states no loss ([NCEI Alerts]({ALERTS})).", "C", NCEI_R),
    (M, PT5, "GPCP Daily's own record came through the 2024–2026 input losses (the V3.3 pause and restart; V1.3 kept extended). That is a production track record, not the repository's.", "C", "NOAA NCEI, NASA GES DISC"),
]
RRS5_GAPS = [
    ("P", "After-action reports for GES DISC's 2025–2026 disruptions (none published)."),
    ("U", "GDEX's and CDS's holdings before and after a disruption."),
    ("S", "A final Helene loss count; whether the 2026 migration delays GPCP Daily."),
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
    "producer": "University of Maryland ESSIC (1DD V1.3 and NCEI's V3.3 CDR) and NASA Goddard, under NASA MEaSUREs (V3.x)",
    "producer_is_repository": False,
    "repositories": [
        {"name": NCEI_R, "role": "parent"},
        {"name": GESDISC, "role": "parent"},
        {"name": NODD, "role": "child"},
        {"name": GDEX, "role": "child"},
        {"name": CDS, "role": "child"},
    ],
}

write_categories("gpcp-daily", SUBCATEGORIES, DATASET)
