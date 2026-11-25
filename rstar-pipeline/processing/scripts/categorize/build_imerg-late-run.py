"""Build the IMERG Late Run R* categorization JSON (second pass, 2026-11-24).

Hand-sorted evidence from every answer file in rstar-pipeline/input/web-research/ that bears on the IMERG Late Run
(V07, V07B processing, in "hybrid" mode with GPROF V08 inputs since March 2026; half-hourly GPM_3IMERGHHL and
daily GPM_3IMERGDL), made by NASA's Precipitation Processing System (PPS) with the GSFC IMERG team's code and
archived at NASA GES DISC:
- the eight about-datasets/imerg-late-run runs (about-pt1, processing-qc-pt2, formats-people-pt3, funding-pt4,
  news-pt5, inputs-pt6, and both halves of the pt7 gap query: Run 2 calibration-copies-pt7 and, added in the
  second pass, Run 1 people-production-pt7);
- instruments/nasa-satellites (GPM, the calibrator) and instruments/noaa-satellites (S-NPP, NOAA-20/21, POES,
  DMSP, Metop, AMSR2, GOES);
- for the AWS S3 integrity statement only, the GHCN-Daily repository-resilience run pt9.
Left out: instruments/noaa-rain-gauges (the Late Run sees no gauges, only a climatology of the Final Run's GPCC
adjustment) and both archives/noaa-ncei runs (no source puts an IMERG copy at NCEI).
Not available: the NASA GES DISC + PPS A2 repository run (RRS-2 and RRS-3 are unsearched). Its gaps say so.

Second pass (2026-11-24): added pt7 Run 1 (people, ages, contracts, PPS processing) to P-1 to P-4, D-1, DIRS-4 and
DIRS-5; corrected Kidd's departure (2020-2023, not 2023-2026) and PDIR-Now's location (computed at PPS). The first
pass's three items from GPCP Daily's people-production-pt7 (Huffman, Bolvin, Nelkin) were replaced by this run's
items, which re-checked the same people, so that run is no longer a source.

Filing rules: rstar-pipeline/input/framework/rstar-categorization-decisions.md. Steps: rstar-pipeline/processing/instructions/categorize-dataset-instructions.md.
Markdown links [label](url) in the text become <a> tags (rstar_common.py does the writing and scoring).

Run:  python3 rstar-pipeline/processing/scripts/categorize/build_imerg-late-run.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rstar_common import H, M, L, write_categories  # noqa: E402

# data-source values: the research run folder names
PT1 = "2026-11-20_imerg-late-run-about-pt1"
PT2 = "2026-11-21_imerg-late-run-processing-qc-pt2"
PT3 = "2026-11-21_imerg-late-run-formats-people-pt3"
PT4 = "2026-11-21_imerg-late-run-funding-pt4"
PT5 = "2026-11-21_imerg-late-run-news-pt5"
PT6 = "2026-11-21_imerg-late-run-inputs-pt6"
PT7 = "2026-11-24_imerg-late-run-calibration-copies-pt7"
PT7P = "2026-11-24_imerg-late-run-people-production-pt7"
NASA_SAT = "2026-11-18_nasa-satellite-precip-threats"
NOAA_SAT = "2026-11-18_noaa-satellite-precip-threats"
GH_RRS = "2026-11-23_ghcn-daily-repository-resilience-pt9"

# Each evidence item is (confidence, source run, text, stance[, repository for RRS]); stance toward the
# subcategory's statement: F = for, A = against, C = context (not directly tied, or doesn't show it true or false).
# Each gap is (status, text): S = searched and none found, P = not public, U = not searched.

# Repository names (match DATASET below)
GESDISC = "NASA GES DISC"
PPS = "NASA PPS"
BOTH = "NASA GES DISC, NASA PPS"
NOT_REPO = "None (third-party copies, not repositories)"

# Frequently cited pages
ATBD = "https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf"
TECHDOC = "https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf"
RELNOTES = "https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf"
FAQ = "https://gpm.nasa.gov/sites/default/files/2025-02/FAQ%20for%20IMERG%20V07%20Applications%20Users_202502.pdf"
FILESPEC = "https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/new/filespec.GPM.V7.pdf"
L1C_111 = "https://arthurhou.pps.eosdis.nasa.gov/Documents/L1C_ATBD_GPM_V08.pdf"
V08_APR = "https://gpm.nasa.gov/data/news/imerg-v08-transition-schedule"
V08_AUG = "https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026"
GESDISC_HHL = "https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHHL_07/summary"
AWS_REG = "https://registry.opendata.aws/nasa-gpm3imerghhl/"
CMR_HHL = "https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_3IMERGHHL&version=07"
CMR_LATE = "https://cmr.earthdata.nasa.gov/search/collections.json?keyword=IMERG%20Late&page_size=50"
README_GIS = "https://arthurhou.pps.eosdis.nasa.gov/Documents/README.GIS.pdf"
PPS_CONTACTS = "https://storm.pps.eosdis.nasa.gov/storm/PPSContacts.jsp"
PPS_HOME = "https://pps.gsfc.nasa.gov/"
PPS_GMI_ANOM = "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/gpm_anomalous.html"
PPS_METOPC = "https://pps.gsfc.nasa.gov/Documents/PPS_Will_Reprocess_All_METOPC_GPROF_Data.txt"
PPS_AUTOSNOW = "https://pps.gsfc.nasa.gov/Documents/PPS_Temporarily_Halting_GPM_V08_STD_L2_L3_GPROF.txt"
PPS_AMSR3 = "https://pps.gsfc.nasa.gov/Documents/L2_GPROF_V08B_Data_Release_New_WSFM1_MWI_L1_L2_and_GOSAT_GW_AMSR3_L2_L3%20Products.txt"
GPROF_RECALL = "https://www.earthdata.nasa.gov/data/alerts-outages/all-l3-gprof-data-gpm-v08-being-recalled"
KROODSMA = "https://science.gsfc.nasa.gov/sci/bio/rachael.a.kroodsma"
GSICS = "https://web.archive.org/web/20250523022002/https://gsics.atmos.umd.edu/bin/view/Development/Microwave-Deliverable"
ESD_MAR26 = "https://www.nationalacademies.org/cdn/materials/a175298a-2c27-49b1-991f-41000e915647"
GMAO_STATUS = "https://gmao.gsfc.nasa.gov/operations/status.php"
CMR_MERGIR = "https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPM_MERGIR"
SSMIS_MWI = "https://gpm.nasa.gov/sites/default/files/2025-08/SSMIS-MWI_transition.pdf"
SSMIS_END = "https://gpm.nasa.gov/data/news/end-ssmis-data-coming-gpm-near-real-time-products"
WSFM_NRT = "https://gpm.nasa.gov/data/news/new-wsf-m1-mwi-nrt-files-available"
SNPP4 = "https://www.nesdis.noaa.gov/news/update-4-cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-november-02-2026-1540-utc-and-decommissioning-issued-november-2-2026-1800-utc"
AMSR2_NOAA = "https://www.nesdis.noaa.gov/news/decommissioning-of-advanced-microwave-scanning-radiometer-amsr2-products-and-transition-amsr3-products"
N19 = "https://ospo.noaa.gov/data/messages/2025/08/MSG_20250813_1715.html"
POES = "https://www.nesdis.noaa.gov/news/suspension-of-poes-data-users-after-june-16-2025-and-decommissioning"
DMSP_LETTER = "https://www.hickenlooper.senate.gov/wp-content/uploads/2026/10/2026-DMSP-Continuity-Letter-Hickenlooper-Murkowski-King.pdf"
METOPB = "https://database.eohandbook.com/database/missionsummary.aspx?missionID=230"
MET9 = "https://space.oscar.wmo.int/satellites/view/meteosat_9_iodc"
GAO_GEO = "https://files.gao.gov/reports/GAO-26-107739/index.html"
SR2023 = "https://science.nasa.gov/wp-content/uploads/2024/02/response-to-2023-earth-science-senior-review-and-2022-2023-out-of-cycle-senior-reviews-final.pdf"
NASA26 = "https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf"
NASA27 = "https://www.nasa.gov/wp-content/uploads/2026/04/fiscal-year-2027-full-budget-request.pdf"
JES26 = "https://www.appropriations.senate.gov/imo/media/doc/fy26_cjs_jes.pdf"
SEN27 = "https://www.appropriations.senate.gov/imo/media/doc/cjs_explanatory_stmt.pdf"
SR2026 = "https://science.nasa.gov/earth-science/senior-review-2026/"
CR27 = "https://spacepolicyonline.com/news/house-clears-fy2027-cr-now-to-the-president/"
TOWNHALL = "https://assets.science.nasa.gov/content/dam/science/esd/earth-science-division/resources/ESD%20Town%20Hall%2012162025.pdf"
ESDS26 = "https://espo.nasa.gov/sites/default/files/documents/2026-05/D2_0915_Scott_ESDS-Updates.pdf"
CONSIDINE = "https://ceres.larc.nasa.gov/documents/STM/2026-05/01_ceres-st-May2026-considine2.pdf"
IA_MIGRATION = "https://www.earthdata.nasa.gov/data/alerts-outages/ingest-archive-migration-interrupt-data-ingestion-oct.-28-30"
GESDISC_MOVE = "https://github.com/nasa/gesdisc-tutorials/blob/main/user-guidance/GES_DISC_Migration_to_Earthdata_Website_and_Earthdata_Cloud.md"
OIG_GSFC = "https://oig.nasa.gov/wp-content/uploads/2026/06/final-memorandum-ig-26-005-review-of-goddard-space-flight-centers-transformation-efforts.pdf"
WARN = "https://labor.maryland.gov/Employment/pdf/warn-log-2025.pdf"
EED3 = "https://api.usaspending.gov/api/v2/awards/CONT_AWD_80GSFC21CA001_8000_-NONE-_-NONE-/"
MEXT_PMM = "https://www8.cao.go.jp/space/comittee/27-kagaku/kagaku-dai70/siryou1.pdf"
PRECIP_WP = "https://ntrs.nasa.gov/api/citations/20260008217/downloads/PrecipWhitePaper_V4.pdf"
GPM_DATA_NEWS = "https://gpm.nasa.gov/category/blog-type/data-news"
ESDIS_METRICS = "https://www.earthdata.nasa.gov/about/data-metrics/esdis-metrics/weekly-metrics/10-20-2025"
OSS_POLICY = "https://www.earthdata.nasa.gov/engage/open-data-services-software-policies/open-source-software-policy"
SPD41A = "https://science.nasa.gov/wp-content/uploads/2023/08/smd-information-policy-spd-41a.pdf"
GPROF_NN = "https://github.com/simonpf/gprof_nn"
GMU_CEOSR = "https://ceosr.science.gmu.edu/microwave-remote-sensing-group/"
PDIR = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8216223/"
GDEX_FINAL = "https://gdex.ucar.edu/datasets/d731000/"
IRI_SUNSET = "https://iri.columbia.edu/resources/data-library/sunset/"
DYNAMICAL = "https://registry.opendata.aws/dynamical-nasa-imerg/"
EARTH_ENGINE = "https://developers.google.com/earth-engine/datasets/catalog/NASA_GPM_L3_IMERG_V07"
CMORPH2 = "https://ftp.cpc.ncep.noaa.gov/precip/CMORPH2/CMORPH2NRT/readme_CMORPH2x_NRT.txt"
BOLVIN = "https://science.gsfc.nasa.gov/earth/bio/david.t.bolvin"
NELKIN = "https://science.gsfc.nasa.gov/earth/bio/eric.j.nelkin"
HUFFMAN_SLIDES = "https://ntrs.nasa.gov/api/citations/20240011596/downloads/20240011596%20Huffman%20G%20slides.pdf"
AWS_S3 = "https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html"
# pt7 Run 1 (people and production)
ATBD_PAGE = "https://gpm.nasa.gov/resources/documents/algorithm-information/IMERG-V07-ATBD"
ATBD_V063 = "https://gpm.nasa.gov/sites/default/files/2020-05/IMERG_ATBD_V06.3.pdf"
ATBD_V07_2023 = "https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_V07_ATBD_final_230712.pdf"
HUFFMAN_EARTH = "https://science.gsfc.nasa.gov/earth/bio/george.j.huffman"
STOCKER = "https://science.gsfc.nasa.gov/earth/bio/erich.f.stocker"
STOCKER_ORCID = "https://pub.orcid.org/v3.0/0000-0003-0657-0066/employments"
TRMM_SR2011 = "https://gpm.nasa.gov/sites/default/files/document_files/TRMMSenRevProp_v1.2.pdf"
JOYCE = "https://science.gsfc.nasa.gov/earth/bio/robert.joyce"
TAN = "https://science.gsfc.nasa.gov/sci/bio/jackson.tan"
KELLEY = "https://science.gsfc.nasa.gov/sci/bio/owen.a.kelley"
KELLEY_ORCID = "https://pub.orcid.org/v3.0/0000-0002-4481-9005/employments"
PMM_TEAM_2024 = "https://web.archive.org/web/20240501224602/https://gpm.nasa.gov/science/pmm-science-team"
PMM_TEAM_2026 = "https://web.archive.org/web/20261028182629/https://gpm.nasa.gov/science/pmm-science-team"
PPS_CONTACTS_2024 = "https://web.archive.org/web/20240521055833/https://storm.pps.eosdis.nasa.gov/storm/PPSContacts.jsp"
PPS_CONTACTS_2026 = "https://web.archive.org/web/20260411213639/https://storm.pps.eosdis.nasa.gov/storm/PPSContacts.jsp"
PPS_PROJECT = "https://science.gsfc.nasa.gov/earth/projects/212/"
CODE612_ORG = "https://science.gsfc.nasa.gov/earth/mesoscale/orgchart/"
CODE612_STAFF_2025 = "https://web.archive.org/web/20250208101416/https://science.gsfc.nasa.gov/earth/mesoscale/staff"
CODE619_STAFF = "https://science.gsfc.nasa.gov/earth/terrestrialinfo/staff/"
APPEL = "https://www.nasa.gov/wp-content/uploads/2025/10/sustaining-knowledge-through-transitions.pdf"
OIG_TMPC = "https://oig.nasa.gov/wp-content/uploads/2026/01/2025-report-on-nasas-top-management-and-performance-challenges.pdf"
OPENALEX_KIDD = "https://api.openalex.org/works?filter=author.id:A5084463178,from_publication_date:2024-01-01&sort=publication_date:desc"
ATMOS = "https://api.usaspending.gov/api/v2/awards/CONT_IDV_80GSFC26D0002_8000/"
ATMOS_NEWS = "https://www.nasa.gov/news-release/nasa-awards-atmosphere-research-support-contract/"
ATMOS_RFP = "https://www.highergov.com/contract-opportunity/atmosphere-support-atmos-request-for-proposal-r-80gsfc24r0037-o-b8c8b/"
GMU_COOP = "https://api.usaspending.gov/api/v2/awards/ASST_NON_80NSSC22M0109_8000/"
CEOSR_MELISSA = "https://ceosr.science.gmu.edu/large-rainfall-accumulation-from-hurricane-melissa-2025-as-it-passes-over-jamaica/"
GPROF_IR = "https://arxiv.org/abs/2605.07167"
GPM_FAQ = "https://gpm.nasa.gov/data/faq"
SCIAM_54 ="https://www.scientificamerican.com/article/white-house-budget-puts-54-nasa-science-missions-on-the-chopping-block/"
PLANETARY27 = "https://www.planetary.org/articles/analyzing-the-fy-2027-nasa-budget-request"

# ---------------------------------------------------------------- People risk
P1 = [
    (H, PT2, f"The Late Run's processing is written down in detail and kept current: the V07 ATBD (13 Aug 2026) with a step-by-step chain and a table of how the Late Run differs from Early and Final ([ATBD]({ATBD})), the Technical Documentation (2023; [Tech Doc]({TECHDOC})), the V07 release notes (2024; [Release Notes]({RELNOTES})), an applications FAQ (2025), the PPS file specification ([File Spec V7.18]({FILESPEC})) and the L1C ATBD v1.11 for calibration (Aug 2026; [L1C ATBD]({L1C_111})).", "A"),
    (H, PT3, f"Handover between the algorithm team and the operators is a documented step: \"the entire package is assembled and transferred to PPS for integration and testing\" ([ATBD]({ATBD})).", "A"),
    (M, PT7P, "A search aimed at one found no written succession or knowledge-transfer plan for IMERG, PPS, GSFC Codes 612, 613 or 619, or NASA's Earth Science Division, and no page read names a successor or deputy for anyone on the team.", "F"),
    (M, PT3, "No headcount is published for the IMERG team, PPS or GES DISC. The nearest evidence is the 13-person ATBD author list (Aug 2026) and the five \"data set creators\" named in the Technical Documentation.", "C"),
    (M, PT7P, f"Team size is still unpublished: the [PPS project page]({PPS_PROJECT}) lists no people; Code 619, which holds PPS, lists 192 staff records for the whole lab ([Code 619 staff]({CODE619_STAFF})); Code 612 grew from 82 records (Feb 2025) to 103 (Nov 2026) as ocean and land staff were added, with only Grecu, Huffman and Meneghini listing precipitation ([Code 612 staff, 2025]({CODE612_STAFF_2025})). The 13-author ATBD list is the same in July 2023 and August 2026. These are page entries, not official counts.", "C"),
    (H, PT3, f"Production is spread across groups: the IMERG team at GSFC Code 612 (lead George Huffman), PPS at Code 619 (Project Manager Erich Stocker), GES DISC, and input suppliers. ATBD co-authors: Bolvin, Joyce and Nelkin (SSAI), Tan (UMBC), Braithwaite, Hsu, Nguyen and Sorooshian (UC Irvine), Kelley, Watters, West and Xie (NOAA CPC) ([ATBD]({ATBD}); [Huffman slides, 2024]({HUFFMAN_SLIDES})).", "C"),
    (M, PT7P, f"No departures since 2024 among the IMERG or PPS people: the PPS contacts page has the same entries in May 2024 and April 2026 ([2024]({PPS_CONTACTS_2024}); [2026]({PPS_CONTACTS_2026})), Huffman's and Stocker's rows in the PMM Science Team table are unchanged, and Bolvin, Joyce and Nelkin published in 2026. Walter Petersen (Ground Validation, MSFC, not on the IMERG team) left the PMM table between May 2024 and October 2026 ([PMM team, 2024]({PMM_TEAM_2024}); [2026]({PMM_TEAM_2026})).", "C"),
    (H, PT7P, f"Christopher Kidd left the IMERG author list between 2020 and 2023, not after 2023: he is on the V06.3 ATBD (January 2020) and absent from V07 (July 2023) and the August 2026 version ([ATBD V06.3]({ATBD_V063}); [ATBD V07, 2023]({ATBD_V07_2023})). No reason is published; he still publishes IMERG work (GSFC/ESSIC in 2025; a University of Birmingham affiliation in August 2026 is not linked to his ORCID) ([OpenAlex]({OPENALEX_KIDD})).", "C"),
    (M, PT7P, f"Owen Kelley (George Mason University, on site at PPS since 1997) runs algorithm checks before and after production runs and mentors newer PPS staff ([GSFC staff page]({KELLEY})). That is informal knowledge transfer, not a written plan.", "C"),
    (M, PT7P, f"NASA has an agency-wide \"Sustaining Knowledge Through Transitions\" guide (October 2025) that tells leaders to hold \"legacy\" discussions with departing staff ([NASA APPEL]({APPEL})); nothing shows it was applied to IMERG or PPS. NASA's OIG cites \"the Agency's lack of a workforce planning process\" ([NASA OIG, 2025]({OIG_TMPC})).", "C"),
    (M, PT4, f"Goddard lost \"approximately a third of its civilian workforce\" in 2025 ([NASA OIG IG-26-005]({OIG_GSFC})), and SSAI, IMERG's contractor, filed Maryland WARN layoffs of 148 (Apr 2025) and 79 (Aug 2025) ([WARN log]({WARN})). No source names an IMERG, PPS or GES DISC staff member.", "C"),
]
P1_GAPS = [
    ("P", "PPS's and the IMERG group's real headcount (GSFC holds it; staff pages are not counts)."),
    ("P", "Why Kidd left the IMERG author list between 2020 and 2023 (unpublished; the IMERG team would know)."),
]

P2 = [
    (H, PT3, f"The people most tied to production: George Huffman (IMERG lead and ATBD preparer, GPM Project Scientist since 2022, Lab Chief), David Bolvin, Robert Joyce and Eric Nelkin (contractors at GSFC), Jackson Tan (UMBC/GSFC), Owen Kelley, and Erich Stocker (PPS Project Manager and PPS's \"NASA Official\"; [PPS contacts, 2024]({PPS_CONTACTS})).", "C"),
    (L, PT7P, f"Estimate, not a personnel record (earliest publication year minus 25–30; FERS rules): Huffman (ORCID 0000-0003-3858-8308; earliest publication 1980) is about 71–76, a NASA civil servant since 2012 and GSFC-based since 1988, so likely eligible to retire now under FERS (62 with 5 years). The GPCP Daily people run gives the same estimate ([GSFC staff page]({HUFFMAN_EARTH})).", "F"),
    (L, PT7P, f"Estimate: Erich Stocker, PPS Project Manager and a NASA civil servant (ORCID 0000-0003-0657-0066; earliest publication 1999), is 52–57 by the formula but likely older: he has been at GSFC since 1991 and managed TSDIS/PPS since at least 2011. With about 35 years at GSFC, he is likely eligible now or within 2 years if that service is federal (the run's inference) ([GSFC staff page]({STOCKER}); [ORCID]({STOCKER_ORCID}); [TRMM Senior Review, 2011]({TRMM_SR2011})).", "F"),
    (L, PT7P, f"Estimate: the three algorithm contractors are now Science and Technology Corp staff (SSAI in 2023): Bolvin (about 60–65), Joyce (about 61–66, the originator of CMORPH) and Nelkin (about 59–64). FERS does not apply to contractors ([Bolvin]({BOLVIN}); [Joyce]({JOYCE}); [Nelkin]({NELKIN})).", "C"),
    (L, PT7P, f"Estimate: two of the people closest to production are younger and not federal: Jackson Tan (UMBC, about 38–43; [GSFC staff page]({TAN})) and Owen Kelley (George Mason University, on site at PPS, about 54–59; [GSFC staff page]({KELLEY}); [ORCID]({KELLEY_ORCID})). The run reads them as contradicting P-2.", "A"),
    (L, PT7P, f"Estimate: the GMU CEOSR staff who write PPS's job-control software and appear in a 2004 NASA–GMU report are about 63–65 by degree year; they are university staff, so no federal rule applies.", "C"),
    (M, PT7P, f"Goddard's workforce fell \"over 40 percent\" from March 2020 to January 2026, and a letter in the OIG's review describes \"a senior workforce increasingly eligible for retirement\" ([NASA OIG IG-26-005]({OIG_GSFC})). No IMERG or PPS person is named.", "C"),
]
P2_GAPS = [
    ("P", "Real birth years and federal service dates for Huffman and Stocker (NASA HR records); the ages are estimates."),
    ("S", "The PPS staff who run the Late Run day to day: not named on any NASA page, so no age."),
    ("U", "Ages for ATBD co-authors Daniel Watters and B. Jason West."),
]

P3 = [
    (M, PT3, "The IMERG production code is not public: the ATBD gives no release location and NASA's GitHub organization has no IMERG repository (only the nasa organization was searched; the GitHub API was refused). The run rates this moderate because it rests on absence.", "F"),
    (M, PT2, "Some operating details are not written down anywhere read: which GPROF `qualityFlag` values IMERG rejects, whether SPEEDe runs before each Late Run, and what the October 2026 GPROF V08 recall did to the Late Run. The run says the IMERG team at GSFC holds them. Bad real-time data are stopped by hand, case by case.", "F"),
    (H, PT2, f"The processing chain is documented step by step: Level 1C intercalibration, GPROF, quantile matching to CORRA, PDIR-Now IR, morphing along GEOS FP motion vectors with a Kalman filter, and the climatological gauge step, with the Late Run's settings in ATBD Table 3 ([ATBD]({ATBD}); [Tech Doc]({TECHDOC})).", "A"),
    (H, PT7, f"The calibration tables are published: the L1C ATBD v1.11 (Aug 2026) gives each sensor's offset table and its vintage (XCAL2016 to XCAL2026) ([L1C ATBD v1.11]({L1C_111})).", "A"),
    (M, PT3, f"NASA policy pulls both ways: ESDS requires government-funded software to be released as open source ([Earthdata]({OSS_POLICY})), while SPD-41a says mission software \"is often restricted software and shall not be shared openly unless approved for release\" ([SPD-41a]({SPD41A})). No release decision or exemption for IMERG was found.", "C"),
    (M, PT3, f"Pieces are public elsewhere: GPROF-NN on GitHub (MIT; not stated to be PPS's operational build; [gprof_nn]({GPROF_NN})), the GEOS model, PPS's TKIO toolkit, and the PDIR-Now method paper ([Nguyen et al. 2020]({PDIR})). Third-party readers such as GPM-API help users read files, not rebuild the dataset.", "C"),
    (M, PT7P, f"No statement in the ATBD, the Technical Documentation, the [GPM Data FAQ]({GPM_FAQ}) or the 2025 V08 slides says the production code is shared on request ([ATBD]({ATBD_PAGE}); [Tech Doc]({TECHDOC})).", "F"),
    (M, PT2, "The 2026 \"hybrid\" Late Run (V07 algorithm ingesting GPROF V08, climatological CORRA from 1 March 2026) is described only in news items, not in the ATBD, Technical Documentation or release notes.", "C"),
    (M, PT7P, f"For V08, the IR step will be CSU's open GPROF-IR, \"designed to provide precipitation estimates ... for the upcoming IMERG V08\" ([Pfreundschuh et al., 2026, preprint]({GPROF_IR})). That is open code for a future version, not the V07 Late Run now running.", "C"),
]
P3_GAPS = [
    ("S", "Whether the IMERG production code is shared on request (no statement found; the PPS help desk was not asked)."),
    ("U", "PPS's operating runbooks (not covered by the people run)."),
    ("S", "The SPEEDe code statement (behind a bot check)."),
]

P4 = [
    (M, PT2, f"The Late Run runs in a system, not by hand: \"The Early and Late Runs are executed in the PPS Real Time (RT) processing system\", and the Late Run has no routine manual inspection ([ATBD]({ATBD})). QC is almost entirely automated.", "A"),
    (M, PT3, "The work is split among several organizations, each with its own part: the IMERG team writes one integrated code, PPS runs it, GES DISC archives, and CPC, UC Irvine CHRS, GPCC and the sensor agencies supply inputs.", "A"),
    (M, PT7P, f"Huffman holds four roles at once: IMERG algorithm lead, GPM Project Scientist, PMM Science Team Lead and Chief of the Code 612 lab; the [Code 612 org chart]({CODE612_ORG}) names no deputy ([GSFC staff page]({HUFFMAN_EARTH}); [PMM team, 2026]({PMM_TEAM_2026})). No source says the Late Run would stop without him.", "F"),
    (M, PT7P, f"Erich Stocker has been the only named PPS manager since the TSDIS era (\"Manager, PPS/TSDIS\" in 2015; PPS Project Manager now), and no PPS deputy or operations lead is named anywhere ([GSFC staff page]({STOCKER}); [TRMM Senior Review, 2011]({TRMM_SR2011})).", "F"),
    (M, PT7P, f"No day-to-day Late Run operator is named on any NASA page: PPS's contacts list only Charles Cosner (NASA/GSFC, Code 619, no role given), an \"operators\" mailbox and Stocker; B. Jason West (KBR) curates PPS's web pages ([PPS contacts, 2026]({PPS_CONTACTS_2026})).", "C"),
    (M, PT7P, f"Owen Kelley (GMU, on site at PPS since 1997) runs algorithm checks before and after production runs ([GSFC staff page]({KELLEY})); no source says whether anyone else does.", "C"),
    (M, PT7P, f"Bolvin, Joyce and Nelkin all list Science and Technology Corp (STC) as employer (SSAI in 2023; Joyce's August 2026 paper metadata still gives SSAI). STC's GSFC contract is ATMOS (80GSFC26D0002), a cost-plus IDIQ with a $163.1M ceiling, $19.7M obligated by 2026-11-17, running to 2030-12-01, scoped to Earth Science Division atmospheres research ([USAspending]({ATMOS}); [NASA, 2025]({ATMOS_NEWS})). No record names IMERG, precipitation or a task order, so \"ATMOS pays them\" is the run's inference.", "C"),
    (M, PT4, "SAMDA (SSAI, NNG17HP01C), which paid Goddard atmospheric contractors, ended 2025-05-31; its successor ATMOS went to STC from November 2025. No source names the contract that pays the IMERG staff (Bolvin, Joyce, Nelkin).", "C"),
    (H, PT2, "Bad real-time data are stopped by hand: NOAA-19 MHS artifacts went into Early and Late for almost 24 hours in October 2017, and those hours were not reprocessed. Who does this is not named.", "C"),
]
P4_GAPS = [
    ("S", "Who runs the Late Run day to day at PPS, and who backs them up: not named on any NASA page."),
    ("P", "ATMOS task orders and staffing (STC and GSFC hold them), and PPS's operations contract (GSFC procurement)."),
]

# ---------------------------------------------------------------- Data risk
D1 = [
    (H, PT4, f"GPM's own budget line, which pays for the mission and, per NASA's 2023 Senior Review, \"the near real-time processing system\" ([NASA, 2024]({SR2023})), is $19.7M in the FY2026 request and $0.0 for FY2027 onward in both the FY2026 and FY2027 requests. NASA \"will allocate GPM funding beyond FY 2026 based on the 2026 Senior Review recommendations\" from a pooled $68.8M line ([NASA FY2027 request]({NASA27})); no result was published by November 21, 2026 ([Senior Review]({SR2026})). Pending.", "F"),
    (H, PT4, f"NASA's FY2027 request cuts Earth Science to $1,021.2M against $2,153M enacted for FY2026, and Earth Science Data Systems (which funds GES DISC) to $124.8M (FY2024 op plan $311.5M) ([NASA FY2027 request]({NASA27})). Pending: the House committee gives $1,325M, the Senate committee $2,187.9M, and a continuing resolution runs to December 11, 2026 ([Senate statement]({SEN27}); [SpacePolicyOnline]({CR27})).", "F"),
    (M, PT4, f"NASA plans to \"replace the existing Distributed Active Archive Centers (DAACs) with a small number of thematic science-enabling teams\" ([NASA FY2026 Technical Supplement]({NASA26})); the 2026 ESDS slides list GES DISC among the 11 DAACs to move, with a study under way ([NASA ESDS, May 2026]({ESDS26})).", "F"),
    (L, PT5, f"A May 2026 NASA HQ slide says \"Flight mission science teams eliminated (e.g., CALIPSO/CloudSat, PMM, etc.)\" ([Considine, 2026]({CONSIDINE})). If PMM means the Precipitation Measurement Missions science team, IMERG's algorithm work package loses its usual funding route; \"PMM\" may instead mean the planned Precipitation Measuring Mission. Ambiguous.", "F"),
    (H, PT4, f"The FY2026 request also folded the Precipitation Science project into ESM Research ($39.0M to $10.6M) and roughly halved Earth Science; Congress enacted $2,153M for Earth Science with no GPM or ESDS line ([FY2026 JES]({JES26})). Rejected.", "C"),
    (M, PT4, "No public budget line, grant or contract names IMERG, the Late Run or PPS. No source names PPS in any cut or consolidation.", "C"),
    (M, PT7P, "Three targeted searches found no PPS contract, contractor or funding line (GPM project, ESDIS or SMD). PPS is led by a civil servant; its known non-federal staff are George Mason University's (on site) and KBR's (B. Jason West), and KBR's vehicle is not documented.", "C"),
    (L, PT7P, f"Inference (the run's, which it rates moderate): if ATMOS (80GSFC26D0002, to 2030-12-01) pays the three algorithm contractors, their part has a contract vehicle to 2030, which the run reads as contradicting D-1 for that piece. No record names IMERG or a task order, and the RFP's scope is \"clouds, aerosols, and precipitation\" ([USAspending]({ATMOS}); [HigherGov, RFP]({ATMOS_RFP})).", "A"),
    (M, PT7P, f"The likely vehicle for George Mason University's PPS software work, NASA–GMU cooperative agreement 80NSSC22M0109, runs 2022-05-01 to 2027-08-31 ($7.68M obligated); its record describes \"a long standing cost effective partnership\" on \"science data system capabilities\" but doesn't name PPS ([USAspending]({GMU_COOP})). It ends in nine months; no renewal news was searched.", "C"),
    (M, PT7, f"NASA's March 2026 slides cut mission science teams from \"18 Mission Teams to 10 DART Teams\" without naming PMM or X-CAL ([NASA ESD, 2026]({ESD_MAR26})).", "C"),
    (M, PT4, f"JAXA's PMM radar satellite, GPM's planned successor, got ¥200M enacted for FY2026 against ¥1,900M requested ([Cabinet Office, 2026]({MEXT_PMM})). This bears on a future input, not the Late Run's own program.", "C"),
]
D1_GAPS = [
    ("P", "The 2026 Senior Review result for GPM and NASA's FY2026 operating plan (GPM, ESDS, PMM lines)."),
    ("P", "PPS's contract and funding line (GSFC procurement holds them; a records request would settle it), and ATMOS's task orders."),
    ("U", "Renewal of GMU's cooperative agreement 80NSSC22M0109 (ends 2027-08-31) and whether it covers PPS."),
    ("S", "The FY2027 outcome after the December 11, 2026 continuing resolution."),
]

D2 = [
    (M, PT5, f"GES DISC is now cloud-only: its on-premises HTTPS ended by September 30, 2026 and THREDDS on July 31, 2026 ([GES DISC migration notice]({GESDISC_MOVE})), and the Late Run is served from one Earthdata Cloud bucket, `gesdisc-cumulus-prod-protected` in AWS us-west-2 ([AWS Registry]({AWS_REG})). No source describes a second region or a backup.", "F"),
    (M, PT7, f"Only PPS and GES DISC, both NASA Goddard, hold current copies. NASA's catalog lists only GES DISC ([CMR]({CMR_LATE})); NCAR GDEX holds the Final Run only ([GDEX d731000]({GDEX_FINAL})); the IRI Data Library's V06 Late copy was to shut by the end of October 2026 ([IRI]({IRI_SUNSET})).", "F"),
    (H, PT1, f"The files \"are hosted on both PPS and GES DISC\" ([Tech Doc]({TECHDOC})), and PPS keeps Early and Late files \"until a new version of the Early and Late IMERG algorithm replaces them\" ([README.GIS]({README_GIS})). So two NASA organizations hold the V07 Late record.", "A"),
    (M, PT5, f"New GES DISC ingest paused October 28–30, 2026 for the \"Consolidated Ingest and Archive (I&A) system migration\"; downloads stayed up ([Earthdata]({IA_MIGRATION})).", "C"),
    (L, PT4, f"PPS's one near-real-time outage found (January 20, 2026, about 14 hours) was a planned storage move ([GPM Data News]({GPM_DATA_NEWS})).", "C"),
]
D2_GAPS = [
    ("U", "GES DISC's and ESDIS's storage, backup and failover design (the NASA GES DISC + PPS A2 run is not back)."),
    ("U", "Where PPS stores its copy and whether it has a second site."),
]

D3 = [
    (H, PT5, f"GES DISC's cloud move already changed access: on-premises HTTPS, OPeNDAP and THREDDS are gone, the L3/4 regridder-subsetter ended by September 15, 2026, and scripts built on them stop working; data stay \"available for HTTPS download free of charge from the Earthdata Cloud\" ([GES DISC migration notice]({GESDISC_MOVE})).", "F"),
    (M, PT4, f"GES DISC is to be consolidated with the other DAACs into thematic teams; NASA lists \"Risks associated with data system consolidation\" as a known issue ([ESD town hall, Dec 2025]({TOWNHALL}); [NASA ESDS, May 2026]({ESDS26})).", "F"),
    (H, PT4, f"Earth Science Data Systems, which funds GES DISC, falls from $311.5M (FY2024 op plan) to $124.8M in the FY2027 request, pending under a continuing resolution to December 11, 2026 ([NASA FY2027 request]({NASA27})).", "F"),
    (H, PT3, "Every NASA route needs a free sign-up (Earthdata Login for GES DISC and its cloud copy; e-mail registration for PPS), so each is only partly FAIR on access. The protocols are standard (HTTPS, FTPS, OPeNDAP, S3).", "C"),
    (M, PT4, "No budget line, contract or staff figure was found for PPS's distribution servers; no source names PPS in any cut.", "C"),
    (M, PT5, f"During the 43-day shutdown (Oct 1 – Nov 12, 2025) the GPM website stopped updating, and ESDIS blamed only an OMI-Aura delay on it ([ESDIS metrics]({ESDIS_METRICS})). No PPS or GES DISC outage was found.", "C"),
    (M, PT5, f"New GES DISC ingest paused October 28–30, 2026 for the consolidated ingest migration; downloads stayed up ([Earthdata]({IA_MIGRATION})).", "C"),
]
D3_GAPS = [
    ("U", "GES DISC's and PPS's staffing and funding for distribution (the NASA A2 run is not back)."),
    ("S", "The DAAC consolidation schedule and what it does to IMERG distribution (not published)."),
]

D4 = [
    (H, PT3, f"The Late Run comes in open, documented formats with standard readers: half-hourly HDF5 and daily netCDF at GES DISC, OPeNDAP and netCDF-4 or GeoTIFF on request, GeoTIFF at PPS, and a public file specification ([CMR]({CMR_HHL}); [README.GIS]({README_GIS}); [File Spec]({FILESPEC})).", "A"),
    (M, PT3, "Every NASA route is only partly FAIR because of the login and the missing licence (CMR names none; NASA policy says CC0; the AWS Registry says CC BY 4.0). That is access and licence, not format.", "C"),
    (M, PT3, "CF standard names inside the files were not confirmed.", "C"),
    (M, PT3, f"Third-party copies use other formats: Google Earth Engine's proprietary API, mixing Late with Final ([Earth Engine]({EARTH_ENGINE})), and dynamical.org's Icechunk Zarr with no DOI ([AWS Registry]({DYNAMICAL})). Neither is the dataset's own format.", "C"),
]
D4_GAPS = [
    ("U", "CF `standard_name` attributes in the HDF5 and netCDF files."),
]

D5 = [
    (M, PT5, "No news item from January 2024 to November 2026 names IMERG, the Late Run, PPS, GES DISC, the IMERG team or its people (Huffman, Bolvin, Nelkin, Tan, Stocker) in connection with cuts, layoffs or cancellations; GPM is absent from every termination list the run read.", "A"),
    (M, PT5, f"The FY2027 request would cancel 54 NASA science missions, 17 of them in Earth science; the lists name CYGNSS, TROPICS, OCO-2/3 and Aura, not GPM ([Scientific American]({SCIAM_54}); [Planetary Society]({PLANETARY27})).", "C"),
    (M, PT5, "Coverage of Goddard's staff losses, building closures and the Earth Science budget fights names only the center and programs around IMERG.", "C"),
]
D5_GAPS = [
    ("S", "Mission-list articles that could not be read (Science, CNN, SpaceNews) could name GPM."),
    ("U", "Executive orders affecting NASA science."),
]

# ---------------------------------------------------------------- Dependent infrastructure resilience
DIRS1 = [
    (H, PT7, f"Every microwave sensor in IMERG is put on one reference, GPM's GMI, calibrated to the DPR–GMI combined product; no backup reference is named. A drifting GMI \"cannot be accommodated\", and changing that \"would require a major development effort\" ([ATBD]({ATBD})).", "F"),
    (H, NASA_SAT, f"GPM, the calibrator, has no funding of its own after FY2026 in the FY2026 and FY2027 requests, pending the unpublished 2026 Senior Review ([NASA FY2027 request]({NASA27})). A NASA white paper says its successor PMM \"may be insufficient to serve as the next reference\" ([NASA GSFC, 2026]({PRECIP_WP})); no NASA statement says how IMERG would be calibrated after GPM.", "F"),
    (M, PT7, f"PPS's anomaly table logs GMI electronics side switches on March 25 and June 24, 2026, and a reaction-wheel anomaly on September 8, 2026 ([PPS anomaly table]({PPS_GMI_ANOM})).", "F"),
    (M, PT7, f"On November 20, 2026 PPS found \"METOPC has incorrectly used METOPB calibration files\" in V08A and V08B; it stopped production processing, but \"NRT continues its processing METOPC GPROF data\" ([PPS]({PPS_METOPC})). Whether the near-real-time MetOp-C feeding the Late Run has the same error is not stated.", "F"),
    (M, PT1, f"Since March 1, 2026 the Late Run's CORRA calibration has been \"set to climatological values\" while V08 is pending ([GPM, Apr 2026]({V08_APR})), because the V07 Final record ended on September 30, 2025 and V08 Final had not shipped by November 2026 ([GPM, Aug 2026]({V08_AUG})).", "F"),
    (H, PT7, f"The intercalibration itself is done in-house at NASA and is current: Rachael Kroodsma (GSFC Code 615) \"leads the ... inter-calibration working group (XCAL)\" that delivers the tables ([NASA GSFC]({KROODSMA})), and the L1C ATBD v1.11 (Aug 2026) adds tables for WSF-M1 MWI and AMSR3 ([L1C ATBD v1.11]({L1C_111})).", "A"),
    (M, PT7, f"CPC's merged geostationary IR is \"dynamically calibrated to GOES East, using a 35 day trailing inter-calibration\" ([CMR GPM_MERGIR]({CMR_MERGIR})), a further dependency on NOAA's GOES-East, which is working (GOES-19 since April 2025).", "C"),
    (H, PT7, f"The Late Run's gauge calibration is a fixed climatology: coefficients by month and location computed once after the V07B Final Run and in use from June 1, 2024; the ATBD still names GPCC V2022 ([ATBD]({ATBD}); [Release Notes]({RELNOTES})). Inference (the run's): GPCC's V2025 change can reach the Late Run only through a V08 Final Run.", "C"),
    (M, PT7, f"X-CAL's funding was not found. GSICS holds only an old copy of the tables (V05, 2018) and does not maintain them ([GSICS wiki, Wayback]({GSICS})).", "C"),
]
DIRS1_GAPS = [
    ("S", "X-CAL's funding, and a backup calibration reference if GMI or DPR stopped."),
    ("S", "Whether the near-real-time MetOp-C GPROF has the calibration-file error (PPS holds it)."),
]

DIRS2 = [
    (H, PT6, f"DMSP SSMIS (F16, F17, F18), about 25% of IMERG's microwave data and 3 of its 11 radiometers ([GPM, 2025]({SSMIS_MWI})), is more than a decade past expected end of life. The program reached its planned end in September 2026; CLASS reports \"DMSP data flow stopped on 9/30/2026\", with backlog since resumed; there was an outage from June 11, 2026 ([GPM]({SSMIS_END}); [Senators' letter, Oct 2026]({DMSP_LETTER})). GPM's analysis: losing SSMIS raises the Late Run's IR share from 9.9% to 22.9%.", "F"),
    (H, PT6, f"All Suomi NPP data, including ATMS, one of three ATMS in the Late Run, ended permanently at 15:40 UTC on November 2, 2026 ([NESDIS Update #4]({SNPP4})).", "F"),
    (M, PT6, f"AMSR2 on GCOM-W1 is past its 5-year design life. NOAA ended near-real-time AMSR2 on September 2, 2026, citing \"the limited timeframe before AMSR2 data is discontinued by JAXA\" ([NESDIS]({AMSR2_NOAA})). IMERG gets AMSR2 \"through NASA\" per the Technical Documentation, so whether the Late Run lost it is not stated.", "F"),
    (M, PT6, f"MHS on NOAA-18 and NOAA-19 ended in 2025 (NOAA-18 decommissioned June 6; POES delivery ended June 16; NOAA-19 battery failure August 9, passivated August 13) ([NESDIS]({POES}); [OSPO]({N19})). Conflict: pt1's 2023 sensor table says NOAA-19 MHS ended as an IMERG input in September 2020.", "F"),
    (H, NASA_SAT, f"The GPM Core Observatory (GMI and DPR), IMERG's anchor, is past its 3-year prime mission; NASA's 2023 review extended it \"through FY 2026\" ([NASA]({SR2023})), its own budget line is $0.0 after FY2026 in both requests, and the 2026 Senior Review result is not published. IMERG documents estimate its data to December 2029; JAXA says \"early 2030s\".", "F"),
    (M, PT6, f"MetOp-B (MHS) has an end of life of November 2027 in CEOS's listing ([CEOS]({METOPB})).", "F"),
    (M, PT6, f"Meteosat-9, the Indian Ocean geostationary IR in CPC's merged IR, has an end of life of \"≥2027\" and had short outages in 2025–26 ([WMO OSCAR]({MET9})).", "F"),
    (H, PT6, "NOAA-20 ATMS was non-nominal on July 10, 2026 (some data unrecoverable) and back on July 14; NOAA-21 is primary, and JPSS-3 and -4 follow.", "C"),
    (H, NOAA_SAT, f"The other geostationary IR is working: GOES-19 replaced GOES-16 in April 2025, Himawari-8 stood in for Himawari-9 in late 2025, and Meteosat-12 has been prime since June 2025. GAO projects a gap in the GOES spare from October 2032 ([GAO-26-107739]({GAO_GEO})).", "C"),
    (H, NASA_SAT, "TROPICS ended on November 12, 2025 and Aqua is being closed out, but neither feeds the Late Run (AMSR-E on Aqua has been off since 2011).", "C"),
]
DIRS2_GAPS = [
    ("S", "What PPS's near-real-time stream ingests after the SSMIS, AMSR2 and S-NPP losses (in Late Run file headers, behind a PPS sign-up)."),
    ("U", "JAXA's AMSR2 end and EUMETSAT's Metop-B and Meteosat-9 end dates (hosts refused; check by hand)."),
]

DIRS3 = [
    (H, PT6, "The near-real-time microwave feeds the Late Run is built from broke one after another in 2026: SSMIS (data flow stopped September 30), NOAA's AMSR2 feed (September 2) and S-NPP ATMS (November 2). PPS has published no notice on what its near-real-time stream receives now.", "F"),
    (M, PT1, f"The research CORRA feed the Late Run calibrates to stopped updating: with the V07 Final record ended (September 30, 2025) and V08 Final late, CORRA was \"set to climatological values\" from March 1, 2026, and the Late Run's own V08 switch is \"no sooner than winter of 2026\" ([GPM, Apr 2026]({V08_APR}); [GPM, Aug 2026]({V08_AUG})).", "F"),
    (M, PT7, f"NOAA upgraded Autosnow, which sets the quality index over frozen surfaces, on August 19, 2026; PPS then found its standard GPROF V08 \"neglecting to use any new v1r1 AUTOSNOW data that includes AMSR3\" and halted it ([PPS, Sep 2026]({PPS_AUTOSNOW})). Which Autosnow the V07 Late Run reads is not stated.", "F"),
    (L, PT6, f"The Late Run ingests GPROF V08 (hybrid mode), and PPS's V08 GPROF had setbacks: data from August 18–19 retracted, and all L3 GPROF V08 recalled on October 1, 2026 for a flag bug ([Earthdata]({GPROF_RECALL})). These were standard products; no source says the near-real-time GPROF was affected.", "F"),
    (M, PT6, "A corrupted CPC IR file kept IR out of the Late Run from 16:00 UTC October 18 to 20:00 UTC October 19, 2024; PPS reran the products.", "F"),
    (L, PT4, "NOAA CPC, which makes the merged IR, is to be folded into other NWS units, with \"No layoffs or staff relocations ... expected\" (Bloomberg via Spokesman-Review, 2026). No source ties this to the IR product.", "F"),
    (H, PT7, f"GEOS FP, the Late Run's motion vectors, did not end: GMAO's status page shows \"GEOS-FP 5.44 | Nominal\" on November 24, 2026 ([GMAO]({GMAO_STATUS})); the May 31, 2026 end in an Earthdata Forum post concerned FP-IT.", "C"),
    (H, PT7, "The JMA forecast, which PPS gets from JAXA, sets the precipitation phase for the Late Run and is ancillary data for its GPROF; no 2026 notice on this feed was found.", "C"),
    (M, PT6, f"PDIR-Now (UC Irvine CHRS), which turns IR into rain rates, shows no funding or end statement and its portal is online. PDIR-Now is computed at PPS from CPC's IR (pt7 Run 1), and V08 replaces it with CSU's GPROF-IR.", "C"),
    (L, PT7, f"Whether CPC's merged IR switched to Meteosat-12 is unresolved: CMR lists \"METEOSAT-5/7/8/9/10/11\" ([CMR GPM_MERGIR]({CMR_MERGIR})).", "C"),
]
DIRS3_GAPS = [
    ("S", "Whether the Late Run uses AMSR3 and which Autosnow version it reads (PPS holds both)."),
    ("S", "Meteosat-12 in CPC's merged IR (GPM_MERGIR file metadata)."),
]

DIRS4 = [
    (M, PT2, f"The microwave retrievals are another group's software: GPROF uses the GPROF team's (CSU) code, run at PPS ([ATBD]({ATBD})).", "F"),
    (M, PT3, f"George Mason University's CEOSR group \"develops job-control, archiving, and distribution software\" for PPS ([GMU CEOSR]({GMU_CEOSR}), read through a subagent).", "F"),
    (M, PT7P, f"That GMU software work tests new IMERG versions and is \"funded by NASA's Goddard Space Flight Center\" ([GMU CEOSR]({GMU_CEOSR}); [CEOSR, 2025]({CEOSR_MELISSA})); its likely vehicle, cooperative agreement 80NSSC22M0109, ends 2027-08-31 ([USAspending]({GMU_COOP})).", "F"),
    (M, PT2, "NOAA CPC assembles, zenith-corrects and filters the merged 4-km geostationary IR before forwarding it to PPS.", "F"),
    (H, PT2, f"The Late Run itself is computed on NASA's own systems: \"all of the Runs share a common code\", and PPS installs a copy in its Real Time system for Early and Late (retrospective Late data are computed in its Production system) ([ATBD]({ATBD})).", "A"),
    (H, PT7P, f"PDIR-Now, UC Irvine CHRS's IR rain-rate method, is computed at PPS: CPC forwards the merged geo-IR \"to PPS for use in the PDIR computation routines\" ([ATBD, Aug 2026]({ATBD_PAGE}); [Nguyen et al. 2020]({PDIR})). The IR imagery itself still comes from NOAA CPC.", "A"),
    (M, PT7P, f"PPS runs its own production system: in March 2024 it restarted radar production \"after PPS's production system conversion to RHEL 8\" ([PPS contacts, 2024]({PPS_CONTACTS_2024})).", "A"),
    (M, PT4, f"ESDIS's support contract EED-3 (Raytheon, 80GSFC21CA001) is extended to January 31, 2027 and its successor, ESDIS Next, was not found awarded ([USAspending]({EED3})). That is archive support, not Late Run processing.", "C"),
    (M, PT7P, f"V08 replaces PDIR-Now with CSU's open GPROF-IR ([Pfreundschuh et al., 2026, preprint]({GPROF_IR})); where it will run is not stated. The Late Run stays in V07 \"hybrid\" mode until \"no sooner than winter of 2026\" ([GPM, Aug 2026]({V08_AUG})).", "C"),
]
DIRS4_GAPS = [
    ("P", "Whether GMU's agreement 80NSSC22M0109 covers PPS, and its renewal (GMU's or NASA's grant office)."),
    ("S", "Where V08's GPROF-IR will run (not stated)."),
]

DIRS5 = [
    (H, PT7, f"No backup calibration reference is named if GMI or DPR stopped ([ATBD]({ATBD})), and JAXA's PMM, the only planned GPM-class radar, \"may be insufficient to serve as the next reference\" ([NASA GSFC, 2026]({PRECIP_WP})).", "F"),
    (M, PT4, f"GPM's successor is losing money: JAXA's PMM got ¥200M enacted for FY2026 against ¥1,900M requested ([Cabinet Office, 2026]({MEXT_PMM})), and NASA's role is now \"science expertise and launch\" (GAO). WMO OSCAR estimates launch about March 2030, after GPM's estimated end (December 2029).", "F"),
    (M, PT7, "IMERG's documents name no real-time substitute for CPC's merged IR; GridSat is mentioned only for the period before 2000, and using it \"would require study\".", "F"),
    (H, PT1, f"WSF-M1 MWI, in nearly F17's orbit, has been in the Early and Late Runs since August 17, 2026 ([GPM]({WSFM_NRT})); with it, the Late Run's IR share after SSMIS is about 15.1% rather than 22.9% ([GPM, 2025]({SSMIS_MWI})).", "A"),
    (M, PT7, f"For GEOS FP there is a workaround: PPS \"just uses the most recent forecast sequence\", and forecasts a few days old still work ([Tech Doc]({TECHDOC})).", "A"),
    (M, PT6, "The microwave constellation overlaps: GMI, AMSR2, three SSMIS, MWI, ATMS on three satellites and MHS on two, with imagers preferred over sounders in each grid box. Losing one sensor degrades the Late Run rather than stopping it.", "A"),
    (M, PT7, f"Other near-real-time datasets could stand in for the Late Run, all running in November 2026: CPC's CMORPH2 NRT (0.05°, 30 min, global; [CPC]({CMORPH2})), PDIR-Now and PERSIANN-CCS (CHRS, 60°N–60°S), EUMETSAT H SAF H60B (SEVIRI disk), NOAA's experimental Enterprise Rain Rate, and probably JAXA's GSMaP_NRT. None is a copy, and several use the same CPC IR and microwave satellites.", "A"),
    (M, PT7P, f"PDIR-Now, the Late Run's IR rain-rate step, has a named successor: CSU's GPROF-IR, \"designed to provide precipitation estimates ... for the upcoming IMERG V08\" ([Pfreundschuh et al., 2026, preprint]({GPROF_IR})).", "A"),
    (M, PT6, f"AMSR3 (GOSAT-GW, launched June 2025), AMSR2's successor, is in PPS production (L1C from August 25, 2026; GPROF V08B from November 4, 2026; [PPS]({PPS_AMSR3})), but no source says the Late Run uses it.", "C"),
]
DIRS5_GAPS = [
    ("U", "Model substitutes for GEOS FP (JMA GSM, GFS, ECMWF): not documented by NASA, not searched."),
    ("S", "GSMaP_NRT's current status (JAXA pages refused or 404)."),
]

# ---------------------------------------------------------------- Repository resilience
RRS1 = [
    (M, PT7, f"Only PPS and GES DISC, both NASA Goddard, hold current copies of the Late Run, and neither publishes fixity or a check of one copy against the other. NASA's catalog lists only GES DISC ([CMR]({CMR_LATE})); no outside current copy was found (NCAR GDEX holds the Final Run only, [GDEX]({GDEX_FINAL}); IRI's V06 Late copy was to shut by end of October 2026, [IRI]({IRI_SUNSET})). The run rates RRS-1 not supported.", "A", BOTH),
    (M, PT5, f"GES DISC's on-premises services ended in 2026, so its copy is served from one Earthdata Cloud bucket in AWS us-west-2 ([GES DISC migration notice]({GESDISC_MOVE}); [AWS Registry]({AWS_REG})); no source describes a second region.", "A", GESDISC),
    (L, PT3, "Inference: PPS's copy (location not published; PPS is part of GSFC in Maryland) and GES DISC's cloud copy (AWS us-west-2) may be at separate sites, but no source gives PPS's storage location or says either copy is verified.", "F", BOTH),
    (M, PT7, f"PPS keeps Late files only \"until a new version of the Early and Late IMERG algorithm replaces them\" ([README.GIS]({README_GIS})); the Late Run's V08 switch is due no sooner than winter 2026, after which PPS may no longer hold V07.", "C", PPS),
    (M, PT3, f"Third-party copies are not repositories: dynamical.org's Zarr on AWS (no DOI; [AWS Registry]({DYNAMICAL})) and Google Earth Engine, which mixes Late with Final ([Earth Engine]({EARTH_ENGINE})).", "C", NOT_REPO),
]
RRS1_GAPS = [
    ("U", "How many copies GES DISC keeps and in which regions; where PPS stores its copy (the NASA GES DISC + PPS A2 run is not back)."),
]

RRS2 = [
    (M, GH_RRS, f"GES DISC's copy sits in AWS S3, which AWS says \"regularly\" verifies stored data with checksums, with no frequency ([AWS]({AWS_S3})). No NASA source says GES DISC or PPS runs its own fixity checks.", "C", GESDISC),
]
RRS2_GAPS = [
    ("U", "Checksum or fixity practice at GES DISC, Earthdata Cloud and PPS (the NASA A2 run is not back)."),
]

RRS3 = []
RRS3_GAPS = [
    ("U", "Disaster recovery plans and tests at ESDIS, GES DISC and PPS (the NASA A2 run is not back)."),
]

RRS4 = [
    (H, PT4, f"GES DISC is funded inside Earth Science Data Systems, whose FY2027 request is $124.8M (FY2024 op plan $311.5M), pending; NASA plans to replace the DAACs with \"a small number of thematic science-enabling teams\" ([NASA FY2026 Technical Supplement]({NASA26}); [NASA FY2027 request]({NASA27})).", "A", GESDISC),
    (M, PT4, f"The DAAC consolidation is under way: GES DISC is among the 11 DAACs to move to thematic teams, with a study under way ([NASA ESDS, May 2026]({ESDS26})), and its ingest moved to a consolidated system on October 28–30, 2026 ([Earthdata]({IA_MIGRATION})).", "A", GESDISC),
    (M, PT4, f"The near-real-time processing system was funded through GPM's mission line (\"additional funding ... to support the near real-time processing system\", 2023 Senior Review; [NASA]({SR2023})), which is $0.0 after FY2026 in both requests, pending the unpublished 2026 Senior Review ([NASA FY2027 request]({NASA27})).", "A", PPS),
    (M, PT4, f"Congress has held NASA's funding so far: Earth Science $2,153M enacted for FY2026 against a $1,035.9M request ([FY2026 JES]({JES26})), a continuing resolution at FY2026 levels to December 11, 2026, and the Senate committee's $2,187.9M for FY2027, which \"awaits the results of the 2026 Senior Review\" ([Senate statement]({SEN27})).", "F", BOTH),
    (M, PT4, "PPS has no published budget line, contract or award, and no source names it in any cut.", "C", PPS),
    (M, PT7P, "Three targeted searches in the people run also found no PPS contract, contractor or funding line (GPM project, ESDIS or SMD).", "C", PPS),
    (M, PT4, f"ESDIS's support contract EED-3 (Raytheon) is extended to January 31, 2027; its successor, ESDIS Next ($250M–$500M), was not found awarded ([USAspending]({EED3})).", "C", GESDISC),
]
RRS4_GAPS = [
    ("P", "PPS's funding route, NASA's FY2026 operating plan, and the 2026 Senior Review result for GPM."),
    ("S", "The FY2027 outcome after the December 11, 2026 continuing resolution."),
]

RRS5 = [
    (M, NASA_SAT, "PPS and GES DISC kept producing and distributing data through Goddard's 2025 workforce losses and the 43-day shutdown (October 1 – November 12, 2025), and released GPM V08 in spring 2026. No data loss was reported.", "F", BOTH),
    (M, PT5, f"GES DISC came through its 2026 move to Earthdata Cloud (on-premises services ended by September 30) and the ingest migration of October 28–30 with downloads up and no loss reported ([GES DISC migration notice]({GESDISC_MOVE}); [Earthdata]({IA_MIGRATION})); scripts built on the old services stopped working.", "F", GESDISC),
    (L, PT4, f"PPS's planned near-real-time shutdown of about 14 hours on January 20, 2026 (a storage move) is the only PPS outage found; no loss was reported ([GPM Data News]({GPM_DATA_NEWS})).", "F", PPS),
    (M, PT6, "The Late Run's production record through input losses (the October 2024 IR outage, which PPS reran; the 2025–26 sensor losses) is a production track record, not the repository's.", "C", PPS),
]
RRS5_GAPS = [
    ("U", "GES DISC's and PPS's holdings before and after a disruption, checked against an inventory (the NASA A2 run is not back)."),
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
    "producer": "NASA Goddard Space Flight Center (the IMERG team in Code 612 writes the algorithm; the Precipitation "
                "Processing System, PPS, runs it and serves the files; GES DISC archives them)",
    "producer_is_repository": True,
    "repositories": [
        {"name": GESDISC, "role": "parent"},
        {"name": PPS, "role": "producer site"},
    ],
}

write_categories("imerg-late-run", SUBCATEGORIES, DATASET)
