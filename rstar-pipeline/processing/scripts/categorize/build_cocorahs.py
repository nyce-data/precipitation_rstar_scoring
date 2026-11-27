"""Build the CoCoRaHS R* categorization JSON (first pass, 2026-11-27).

Hand-sorted evidence from every answer file in rstar-pipeline/input/web-research/ that bears on CoCoRaHS (the
Community Collaborative Rain, Hail and Snow Network's daily precipitation reports; no DOI or version), run by CoCoRaHS
headquarters at the Colorado Climate Center, Colorado State University:
- the five about-datasets/cocorahs runs (about-pt1, qc-formats-pt2, people-funding-pt3, threats-news-pt4, inputs-pt5);
- archives/cocorahs (the A2 resilience run on CoCoRaHS's own data site, pt6);
- the two archives/noaa-ncei runs (A1 threats; A2 resilience), for NCEI's copy of the reports inside GHCN-Daily;
- instruments/noaa-rain-gauges (COOP, ASOS, USCRN and CoCoRaHS; used for CoCoRaHS's own row and for COOP as a
  substitute).
Left out: both satellite runs (CoCoRaHS uses no satellite data). GHCN-Daily's own runs name CoCoRaHS only as a GHCN-Daily
source (40% of its entries, normal station turnover); CoCoRaHS's own runs cover the same ground, so nothing is borrowed.

Filing rules: rstar-pipeline/input/framework/rstar-categorization-decisions.md. Steps:
rstar-pipeline/processing/instructions/categorize-dataset-instructions.md.
Markdown links [label](url) in the text become <a> tags (rstar_common.py does the writing and scoring).

Run:  python3 rstar-pipeline/processing/scripts/categorize/build_cocorahs.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rstar_common import H, M, L, write_categories  # noqa: E402

# data-source values: the research run folder names
PT1 = "2026-11-25_cocorahs-about-pt1"
PT2 = "2026-11-25_cocorahs-qc-formats-pt2"
PT3 = "2026-11-25_cocorahs-people-funding-pt3"
PT4 = "2026-11-25_cocorahs-threats-news-pt4"
PT5 = "2026-11-26_cocorahs-inputs-pt5"
SITE = "2026-11-26_cocorahs-site-resilience-pt6"  # archives/cocorahs A2 run
NCEI = "2026-11-17_noaa-ncei-threats"
NCEI_A2 = "2026-11-23_A2_Rstar_query-noaa_ncei"
GAUGES = "2026-11-18_noaa-rain-gauge-threats"

# Each evidence item is (confidence, source run, text, stance[, repository for RRS]); stance toward the
# subcategory's statement: F = for, A = against, C = context (not directly tied, or doesn't show it true or false).
# Each gap is (status, text): S = searched and none found, P = not public, U = not searched.

# Repository names (match DATASET below)
COCO = "CoCoRaHS database and data site"
NCEI_R = "NOAA NCEI (GHCN-Daily)"

# Frequently cited pages: CoCoRaHS
QAQC19 = "https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf"
QAQC26 = "https://media.cocorahs.org/docs/WCC_2026_Day2_Hilberg_QAQC.pdf"
QCTEAM20 = "https://media.cocorahs.org/docs/HilbergWERA20.pdf"
IT20 = "https://media.cocorahs.org/docs/JulianWERA20.pdf"
IT21 = "https://media.cocorahs.org/docs/Turner-WERA21.pdf"
IT24 = "https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf"
ORG24 = "https://media.cocorahs.org/docs/Coordinator_Training_April_2024.pdf"
CONTACT = "https://www.cocorahs.org/Content.aspx?page=contactus"
CCC_STAFF = "https://climate.colostate.edu/ccc_info.html"
ATS_STAFF = "https://www.atmos.colostate.edu/people/research/"
MIN2022 = "https://nimss.org/storage/3841/WERA1012_Summary_of_Meeting_Minutes_2020-2022.pdf"
BUDGET22 = "https://media.cocorahs.org/docs/WERA1012_2022_Budget.pdf"
OUTLINE = "https://nimss.org/projects/view/mrp/outline/18627"
PODCAST = "https://www.buzzsprout.com/1136681/8628856-cocorahs-citizen-science-in-weather-reporting"
NIMSS25 = "https://nimss.org/seas/52786"
CATCH_OCT25 = "https://mailchi.mp/cocorahs/newsletter_the-catch_oct-2025-new-water-year"
CATCH_DEC25 = "https://mailchi.mp/cocorahs/newsletter_the-catch_dec-2025-happy-holidays"
CATCH_MAR25 = "https://mailchi.mp/cocorahs/newsletter_the-catch_march_2025"
CATCH_JUL20 = "https://mailchi.mp/cocorahs/newsletter_the-catch_july_2020"
CATCH_APR11 = "https://media.cocorahs.org/docs/TheCatch_2010-04-22.pdf"
CATCH_APR13 = "https://media.cocorahs.org/docs/TheCatch_2013-04-09.pdf"
CATCH_DEC13 = "https://media.cocorahs.org/docs/TheCatch_2013-12-22.pdf"
LETTER15 = "https://www.cocorahs.org/Content.aspx?page=CoCoRaHSLetter15"
LETTER16 = "https://www.cocorahs.org/Content.aspx?page=cocoletter16"
SPONSORS = "https://www.cocorahs.org/Content.aspx?page=sponsors"
GIVE = "https://give.colostate.edu/"
GIVE24 = "https://give.colostate.edu/cocorahs-2024"
MEMORIAL = "https://www.cocorahs.org/Content.aspx?page=nolanmemorial"
CSU_SOURCE26 = "https://source.colostate.edu/csu-atmospheric-community-remembers-nolan-doesken/"
GOBLE17 = "https://mountainscholar.org/bitstreams/577906e2-f9d0-4e09-bc23-94055d6d0a67/download"
NEW_SC17 = "https://source.colostate.edu/new-state-climatologist-challenge-colorados-fascinating-diverse-climate/"
GAUGES_PAGE = "https://www.cocorahs.org/Content.aspx?page=approved_rain_gauges"
WHY_MANUAL = "https://media.cocorahs.org/docs/WhyManualGauge.pdf"
DOESKEN_TEST = "https://ams.confex.com/ams/pdfpapers/91615.pdf"
COORD06 = "https://media.cocorahs.org/docs/CoCoRaHs_LocalCoordinatorDescription2006.pdf"
TRAINING = "https://media.cocorahs.org/docs/CoCoTrainingSlideshow_v9.2B.pdf"
USAGE = "https://www.cocorahs.org/content.aspx?page=datausagepolicy"
EXPORT = "https://data.cocorahs.org/cocorahs/export/exportmanager.aspx"
DEX_ROADMAP = "https://dex.cocorahs.org/roadmap"
VIEWING = "https://www.cocorahs.org/Content.aspx?page=Resources_viewingdata"
SPIES26 = "https://media.cocorahs.org/docs/WCC_2026_Day2_Spies_Recruiting_Retention.pdf"
SPIES24 = "https://media.cocorahs.org/docs/WERA_2024_15_RecruitingRetention_Spies.pdf"
RALLY26 = "https://www.cocorahs.org/marchmadness.aspx"
MAPHUB = "https://cocorahs.blogspot.com/2026/11/the-latest-cocorahs-innovation-maphub.html"
APP_GUIDE = "https://media.cocorahs.org/docs/CoCoRaHS_MobileApp_User_Guide.pdf"
BLOG24 = "https://cocorahs.blogspot.com/2024"
NY_NEWS = "https://media.cocorahs.org/docs/NY_CoCo_Newsletter_Jan2025.pdf"
TX_COORD = "https://www.cocorahs.org/Content.aspx?page=coord_tx"
MN_COORD = "https://www.cocorahs.org/Content.aspx?page=coord_MN"
GITHUB_APP = "https://github.com/sjwoodr/CoCoRaHS"
# Others
PROD_ALT = "https://productivemn.org/"
DARTER = "https://darterproducts.com/products/rain-gauge"
FLI = "https://www.fliproducts.com/blogs/america250-made-in-usa/america250-stratus-rain-gauge-made-in-usa-darter-plastics"
NSF_API = "https://api.nsf.gov/services/v1/awards.json?keyword=CoCoRaHS"
NSF_TERM = "https://nsf-gov-resources.nsf.gov/files/NSF-Terminated-Awards.csv"
NMP_PARTNER = "https://nationalmesonet.us/cocorahs/"
NOAA_NMP26 = "https://www.noaa.gov/news-release/noaa-boosts-weather-data-collection-capabilities-with-new-mesonet-contract"
JES26_NMP = "https://appropriations.house.gov/sites/evo-subsites/republicans-appropriations.house.gov/files/evo-media-document/FY26-CJS-JES.pdf"
CSU_BUDGET26 = "https://president.colostate.edu/speeches-and-writing/budget-update-and-next-steps/"
ATS_NEWS25 = "https://www.atmos.colostate.edu/wp-content/uploads/2025/12/2025-CSU-Atmospheric-Science-Newsletter.pdf"
AUDIT23 = "https://content.leg.colorado.gov/sites/default/files/documents/audits/2316f-a_colorado_state_university_system_fy23.pdf"
AUDIT25 = "https://content.leg.colorado.gov/sites/default/files/documents/audits/2516f-a-colorado-state-university-system-fy25-accessible.pdf"
WAYBACK_CDX = "https://web.archive.org/cdx/search/cdx?url=www.cocorahs.org/&from=2025&to=2026&collapse=timestamp:8&fl=original,timestamp,statuscode&output=json"
FLOWINGDATA = "https://flowingdata.com/2025/04/22/list-of-noaa-datasets-to-be-discontinued/"
CCC_NEWS = "https://climate.colostate.edu/ccc_news.html"
NWS_STAFF = "https://www.eenews.net/articles/national-weather-service-in-transition-as-hurricane-season-begins/"
PBS_NWS = "https://www.pbs.org/newshour/politics/nearly-half-of-national-weather-service-offices-are-critically-understaffed-experts-warn"
NWS_MOB = "https://www.weather.gov/mob/CoCoRaHSRecruitingBlitz2026"
COOP_FR = "https://public-inspection.federalregister.gov/2026-09099.pdf"
DURRE24 = "https://media.cocorahs.org/docs/WERA_2024_7_NOAA_NCEI_Durre.pdf"
PRISM = "https://prism.oregonstate.edu/participate"
MRMS = "https://vlab.noaa.gov/web/wdtd/-/multi-sensor-qpe"
MADIS = "https://madis.ncep.noaa.gov/madis_hydro.shtml"
IEM = "https://mesonet.agron.iastate.edu/cocorahs/"
# NCEI
GHCND_README = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt"
GHCND_STATUS = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt"
GHCND_VERSION = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt"
NCEI22 = "https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf"
CTS = "https://dataverse.nl/api/access/datafile/469675"
CJ27 = "https://www.noaa.gov/sites/default/files/2026-04/FY2027-NOAA-CJ-Submission.pdf"
JES26 = "https://www.appropriations.senate.gov/imo/media/doc/fy26_cjs_jes.pdf"
WATCHDOG_AUG = "https://avlwatchdog.org/top-climate-scientists-departure-is-sign-of-brain-drain-at-noaa-hub-in-asheville-and-of-deep-cuts-to-research-across-the-country/"
BERKELEY = "https://berkeleyearth.org/october-2025-temperature-update/"
ALERTS = "https://www.ncei.noaa.gov/alerts"
CLOUD = "https://www.ncei.noaa.gov/news/cloud-migration"
SOS25Q1 = "https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf"
OIG24 = "https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf"

# ---------------------------------------------------------------- People risk (P)

P1 = [
    (M, PT3, f"No written succession, workforce or knowledge-transfer plan was found in the WERA1012 agendas (2012–2024), notes, minutes or the 2019–2024 project outline ([NIMSS outline]({OUTLINE})); the 2015 Sustainability Committee was \"Funding mostly\". The only knowledge-transfer trace is that the web developer \"keeps detailed notes\" on priorities.", "F"),
    (M, PT2, f"What is written down is for observers: a training slide show, a data-entry FAQ and a five-page QA/QC document that gives manual review one paragraph and no criteria ([QA/QC 2019]({QAQC19})). The coordinator's duties are a one-page 2006 list ([Local Coordinator description]({COORD06})). A newcomer could keep observers reporting but could not rebuild the review process or the systems from it.", "F"),
    (H, PT2, f"System-admin, database and cyberinfrastructure documentation are listed only as future projects in the 2024 IT update ([Turner, 2024]({IT24})).", "F"),
    (M, PT4, f"Founder Nolan Doesken, emeritus since 2017 but back \"primarily to work on CoCoRaHS\", died on 15 November 2026 ([CoCoRaHS memorial]({MEMORIAL})). CSU names Russ Schumacher and Henry Reges as the current leaders, and no page names a successor to his role ([CSU Source, 2026]({CSU_SOURCE26})).", "F"),
    (H, PT3, f"The paid core is small and long-serving: about five to seven staff at the Colorado Climate Center (the April 2024 org chart lists Hilberg, Turner, Reges, Newman, Talmadge, Stolz and Erikson; [CoCoRaHS, 2024]({ORG24})), and in 2021 Reges spoke of \"a core staff now of about five of us that have been with the program over 10 years\" ([podcast, 2021]({PODCAST})).", "C"),
    (H, PT3, f"Doesken's 2017 retirement was a phased handover, not a written plan: he returned in October 2017 \"primarily to work on CoCoRaHS\" ([Goble, 2017]({GOBLE17})), and CSU appointed Schumacher State Climatologist on 6 October 2017 after a search ([CSU Source, 2017]({NEW_SC17})).", "C"),
    (M, PT3, "The 250+ state, regional and county coordinators are volunteers or other agencies' staff (state climate offices and NWS in Minnesota and Wisconsin), not CoCoRaHS staff, so they are a pool of trained people but not successors for the paid posts.", "C"),
]
P1_GAPS = [
    ("S", "A written succession or knowledge-transfer plan for the paid staff (searched; none published)."),
    ("U", "Who, if anyone, takes on Doesken's emeritus work after his death (too recent for the research)."),
]

P2 = [
    (L, PT3, f"Estimate: Steve Hilberg, project manager and lead on day-to-day QC, has a B.S. from 1974 and earliest publication in 1982, and retired once already as Midwestern Regional Climate Center director ([CSU research staff]({ATS_STAFF})). Estimated age about 69–74, past every CSU retirement threshold (\"Age 60 or greater with at least 5 years\" of service).", "F"),
    (L, PT3, "Estimate: Henry Reges (earliest publication 2005; joined 2004), Russ Schumacher (CSU graduate student from 2001), Julian Turner (CSU start 2003) and Noah Newman (joined about 2004) are about 44–53, so retirement within two years is unlikely; Turner only at the top of his range.", "A"),
    (M, PT3, f"CSU staff must join its Defined Contribution Plan (or PERA in limited cases), so FERS rules don't apply; which plan each person is in is not published ([CSU HR](https://hr.colostate.edu/preparing-for-retirement/)).", "C"),
    (H, PT4, "Doesken had retired from paid roles in 2017 and died on 15 November 2026; he was not a retirement-eligible staff member (he counts in P-1 and P-4).", "C"),
    (H, PT3, f"Becky Bolinger, Assistant State Climatologist, left the Colorado Climate Center by January 2025 with no reason given ([CCC staff page]({CCC_STAFF})); she is not named as CoCoRaHS staff.", "C"),
]
P2_GAPS = [
    ("P", "Real ages, service dates and retirement plans (CSU personnel records)."),
    ("S", "Ages or service dates for Dani Talmadge (QC) and Carol Stolz (help desk): no publications or dates found."),
]

P3 = [
    (M, PT2, f"None of the production code is published: no CoCoRaHS or Colorado Climate Center GitHub organization was found, \"Migrate all DevOps to GitHub\" is a future project ([Turner, 2024]({IT24})), and the only public CoCoRaHS code is the retired volunteer Android app ([sjwoodr/CoCoRaHS]({GITHUB_APP})).", "F"),
    (M, PT2, f"Manual QC has no written criteria: the QA/QC document gives the daily review one paragraph ([QA/QC 2019]({QAQC19})), and the 2026 update wants coordinator webinars on \"how we determine if an observation is an error – the process\" ([QA/QC 2026]({QAQC26})).", "F"),
    (H, PT2, f"System-admin, database and cyberinfrastructure documentation are future projects ([Turner, 2024]({IT24})); the QC ticket system \"was inherited years ago\" ([WERA1012 minutes]({MIN2022})).", "F"),
    (H, PT2, f"The entry checks are written down (no future dates, values to the hundredth up to 30.00, snow water equivalent at most 90% of depth, one report per station per day, multi-day reports up to 60 days; [QA/QC 2019]({QAQC19}), pp. 1–2), as are the observer procedures ([training slide show]({TRAINING})). They document how to report, not how to run QC or the systems.", "C"),
    (H, PT2, "NCEI's own QA of the GHCN-Daily copy (24 automated checks) is published in papers, but it is NCEI's processing of its copy, not CoCoRaHS's production.", "C"),
]
P3_GAPS = [
    ("S", "Written manual-QC criteria; a newer QA/QC document (searched; none found)."),
    ("P", "Internal runbooks or code repositories (CoCoRaHS holds them; ask info@cocorahs.org)."),
]

P4 = [
    (H, SITE, f"One developer runs the systems: CSU lists Julian Turner as \"Web developer and database administrator for the CoCoRaHS ... Network\" ([CSU ATS staff]({ATS_STAFF})), and his 2021 update put capacity at \"One developer => 50 Work weeks a year\" ([Turner, 2021]({IT21})). No source names a second developer.", "F"),
    (H, PT2, f"One staff member does most of the QC (4,541 QC tickets from May 2019 to May 2020; [Hilberg, 2020]({QCTEAM20})), and \"Enlisting coordinators to consistently help with QC\" is still a challenge in 2026 ([QA/QC 2026]({QAQC26})).", "F"),
    (M, PT3, "Henry Reges is the national coordinator, the fundraising contact and the person behind the NIDIS support; no deputy or backup is named for him or anyone else (no named backup is not proof there is none).", "F"),
    (L, PT4, f"The October 2025 newsletter still speaks of \"our web developer\", singular, and no second developer or job posting was found ([The Catch, Oct 2025]({CATCH_OCT25})).", "F"),
    (H, PT3, "The network kept running through the founder's 2017 retirement (a phased handover), so losing that one person did not halt it. This doesn't show the developer or QC posts have backups.", "C"),
    (M, PT2, f"\"CoCoRaHS headquarters staff and a number of our volunteer coordinators review the data each day\" ([QA/QC 2019]({QAQC19}), p. 3), so QC is shared in part; most of it still rests on one person (above).", "C"),
    (M, PT3, f"An outside vendor (Solliance, $150 an hour) helps with operations, but CSU caps a vendor at $150K, \"not that we have the budget for it\" ([Turner, 2021]({IT21})).", "C"),
]
P4_GAPS = [
    ("P", "Staff FTEs, cover arrangements and who can administer the Azure systems besides the developer (not published)."),
]

# ---------------------------------------------------------------- Data risk (D)

D1 = [
    (M, NCEI, f"NCEI, which hosts the GHCN-Daily copy of the reports, faces a pending FY2027 request of $52.0M against a $69.8M base; the House committee gives $60.0M and the Senate committee $70.0M ([NOAA FY2027 CJ]({CJ27})).", "F"),
    (L, PT4, f"The National Mesonet Program, CoCoRaHS's last known federal payment route, was recompeted in 2026 (KBR prime, Synoptic lead subcontractor, from 1 September 2026; [NOAA, 2026]({NOAA_NMP26})); no source says whether CoCoRaHS is still paid under it.", "F"),
    (M, PT4, f"Donations, the documented mainstay, reached records: the 2024 drive raised $279,040 ([CSU GiveCampus]({GIVE24})) and the 2025 drive $351,517 from 3,081 donors ([CSU GiveCampus]({GIVE})), \"to help sustain the network in 2026\".", "A"),
    (M, GAUGES, "A NOAA-wide review of gauge networks (January 2025 – November 2026) found no cut to CoCoRaHS (an absence of evidence; its current NOAA funding is not public).", "A"),
    (L, PT4, f"The National Mesonet Program itself was funded at $30.0M in FY2026 ([FY2026 JES]({JES26_NMP})), and the FY2027 committee levels are $35–40M; NMP's undated partner list still names CoCoRaHS ([NMP]({NMP_PARTNER})).", "A"),
    (H, PT4, f"NSF award 2313996 (NC State–led IDEAL, with CoCoRaHS as one of two partner projects) was \"Administratively Terminated\" with an end date of 18 April 2025 ([NSF API]({NSF_API}); [NSF terminated awards]({NSF_TERM})). It paid for education research, not for running the network.", "C"),
    (M, PT4, f"CSU's FY2027 plan cuts $35.8M and some positions ([CSU, 2026]({CSU_BUDGET26})), but no source ties any cut to Atmospheric Science, the Colorado Climate Center or CoCoRaHS.", "C"),
    (M, PT3, f"Before 2025: NOAA's grants ended in September 2015 ([2015 letter]({LETTER15})) and NSF's in 2017; in 2016 \"The future of CoCoRaHS was very much in doubt\" ([2016 letter]({LETTER16})). Since then about $0.4–0.6M a year comes from data users, donations and the National Mesonet Program ([FY22 budget slides]({BUDGET22})).", "C"),
    (M, PT4, f"The December 2025 department newsletter mentions \"federal funding headwinds\" but says CoCoRaHS \"continues to thrive\" and reports no cuts ([CSU Atmospheric Science, 2025]({ATS_NEWS25})).", "C"),
]
D1_GAPS = [
    ("P", "Whether CoCoRaHS is paid under the 2026–2031 NMP contract, and how much (KBR's subcontract lists)."),
    ("P", "CSU's unit-level FY2027 cuts and any CSU or Agricultural Experiment Station amount for CoCoRaHS."),
    ("S", "The final FY2027 NCEI and NMP appropriations (not enacted as of November 2026)."),
]

D2 = [
    (H, SITE, f"Since a move scheduled for 7 August 2020, all of CoCoRaHS runs in one commercial cloud, Microsoft Azure ([The Catch, Jul 2020]({CATCH_JUL20})), with one \"Azure SQL Database\" as the \"Primary CoCoRaHS DB\" ([Turner, 2021]({IT21})); on 26 November 2026 its www, data, dex, wys and media hosts all answered through Azure Front Door.", "F"),
    (H, PT1, "The full record (every report type, every station, the latest days) exists only in CoCoRaHS's own database: GHCN-Daily takes only stations with at least 100 values, adds new stations once a month, and holds only precipitation and snow elements.", "F"),
    (M, SITE, f"Nothing published describes CoCoRaHS's backups: the 2021 architecture slide lists no backup component, and the Azure region, geo-redundancy, retention and restore testing are not published ([Turner, 2021]({IT21})).", "F"),
    (M, NCEI_A2, f"NCEI's Asheville archive, where the GHCN-Daily copy sits, has its offsite tape copy only \"several kilometers away\" ([CoreTrustSeal]({CTS})).", "F"),
    (H, SITE, f"NCEI's GHCN-Daily has held the core daily precipitation and snow reports since 12 July 2010 (source flag N), with multi-day totals from version 3.27 in 2019 ([GHCN-Daily status]({GHCND_STATUS})). For those series a CoCoRaHS outage would not take the data offline.", "A"),
    (M, SITE, f"Downstream copies (MADIS for nine states, the Iowa Environmental Mesonet, ACIS via GHCN-Daily; [MADIS]({MADIS}); [IEM]({IEM})) are reformatted, so they are not repositories.", "C"),
    (H, NCEI, f"NCEI is moving all its data to Amazon Web Services through spring 2027 ([NCEI]({CLOUD})); no source says where the GHCN-Daily copy will sit.", "C"),
]
D2_GAPS = [
    ("P", "The Azure region and backup settings, and who holds the subscription (CoCoRaHS holds them)."),
    ("S", "Whether NCEI or anyone else holds the hail, condition-monitoring and ET reports (not stated)."),
]

D3 = [
    (H, SITE, f"One CSU developer builds and runs every CoCoRaHS site (www, data export, Data Explorer, maps, app; [CSU ATS staff]({ATS_STAFF}); [Turner, 2021]({IT21})).", "F"),
    (H, SITE, f"Parts of the access system are fragile or cut for money: the volunteer-built apps were abandoned by their maker, the QC ticket system is \"fragile\", the data export \"is having a harder time keeping up\", and the watershed maps were turned off \"for budget reasons\" ([Turner, 2024]({IT24})).", "F"),
    (M, SITE, f"The sites have always run on short-term money: a 2003 NSF grant hired the first developer, NSF and NOAA support for \"staff, coordination and web development costs\" was ending in December 2013 ([The Catch, Dec 2013]({CATCH_DEC13})), and Microsoft's AI for Earth grant covered hosting in 2020 ([Turner, 2020]({IT20})). Who pays for hosting now is not published; HQ says gifts support \"data management, web development work\" ([The Catch, Dec 2025]({CATCH_DEC25})).", "F"),
    (M, PT5, f"In November 2026 CoCoRaHS began moving its maps to MapHub, partly from \"a need to reduce our costs\" ([CoCoRaHS blog]({MAPHUB})).", "F"),
    (M, NCEI, f"NCEI's GHCN-Daily copy was \"broken or incomplete\" from late August 2025 ([Berkeley Earth]({BERKELEY})); it was reprocessed on 6 November 2026 ([GHCN-Daily version]({GHCND_VERSION})), and NCEI's alert for 16–30 November 2026 says \"Many access portals, interactive maps, and data folders are currently unavailable\" ([NCEI Alerts]({ALERTS})).", "F"),
    (M, PT4, f"No outage, login, rate limit or data removal was found for 2025–2026: Wayback captures show no error codes ([Wayback CDX]({WAYBACK_CDX})), and CoCoRaHS reported \"99+ percent uptime\" in July 2025 ([NIMSS 2025]({NIMSS25})). A clean record doesn't remove the single-developer and soft-money risks above.", "C"),
    (M, PT1, f"The bulk export has no API documentation or stability statement, and the Export Manager's state list has no Canada or Bahamas option ([Export Manager]({EXPORT})); \"Data export capabilities\" are still on the Data Explorer's roadmap ([DEx roadmap]({DEX_ROADMAP})).", "C"),
    (H, PT1, f"New stations reach GHCN-Daily and ACIS only once a month, \"so depending on timing it could be four months\" ([CoCoRaHS]({VIEWING})).", "C"),
]
D3_GAPS = [
    ("P", "Who pays for hosting now, and what the Azure bill is (not published)."),
    ("S", "Short outages after 2020 (no public status log; Wayback can't see outages under a day)."),
]

D4 = [
    (H, PT2, f"The Export Manager serves CSV, XML and SHEF, all open formats needing no proprietary software, under CC BY 4.0 ([Export Manager]({EXPORT}); [Data Usage Policy]({USAGE})).", "A"),
    (H, PT2, f"NCEI's GHCN-Daily copy is in a documented fixed-width format with flags, with a DOI and catalog record ([GHCN-Daily readme]({GHCND_README})).", "A"),
    (M, PT2, "The routes are only partly FAIR: the CoCoRaHS data have no DOI or version (NOAA's catalog gives \"Dataset_DOI N/A\"), no column or flag documentation was found for the exports, and the API is not public. That is findability and documentation, not format obsolescence.", "C"),
    (H, PT2, "What is proprietary is the server stack (SQL Server, Azure, Carto), which is a DIRS-4 matter.", "C"),
]
D4_GAPS = [
    ("S", "Column and flag documentation for the Export Manager files (not found)."),
]

D5 = [
    (M, PT4, "No political pressure on CoCoRaHS was found for 2025–2026 (searched in CoCoRaHS's, CSU's and NOAA's records and with two search engines).", "A"),
    (M, PT4, f"NOAA's 2025 product retirements did not include CoCoRaHS ([FlowingData list]({FLOWINGDATA})), and the Colorado Climate Center kept publishing climate-change material through 2026 ([CCC news]({CCC_NEWS})).", "A"),
    (M, PT4, f"In March 2025, after volunteers wrote in about federal changes, CoCoRaHS said it \"is not part of NOAA, rather, we are extremely close partners\" ([The Catch, Mar 2025]({CATCH_MAR25})).", "C"),
    (M, PT4, "News in 2025–2026 presents CoCoRaHS as help during NWS cuts (Detroit Free Press, March 2025), not as a target; federal budget threats in the news name NOAA, NSF and NCAR, not CoCoRaHS.", "C"),
]
D5_GAPS = []

# ---------------------------------------------------------------- Dependent infrastructure resilience (DIRS)

DIRS1 = [
    (H, PT2, f"CoCoRaHS sets its own gauge standard: its Approved Rain Gauges page lists the Stratus 4-inch, the TROPO 4-inch and the NWS 8-inch gauge, and \"Digital/electronic rain gauges are not approved\" ([approved gauges]({GAUGES_PAGE})). No outside calibration service enters the chain.", "A"),
    (H, PT5, "The 2025–2026 change of Stratus maker involved no calibration service; gauges are built to the NWS standard (no external calibration found).", "A"),
    (M, PT2, f"The only published gauge test is CoCoRaHS's own ten-year side-by-side test at CSU's Fort Collins station (1995–2004): the 4-inch gauge read 3% above the 8-inch standard ([Doesken, AMS]({DOESKEN_TEST}); [Why manual gauges]({WHY_MANUAL})). No paired comparison with NWS COOP, ASOS or USCRN gauges was found.", "C"),
    (M, PT2, "The Stratus page says it \"meets the minimum requirements set by the National Weather Service to be within +/- 4% of the Standard Rain Gauge\", but no written NWS specification was found.", "C"),
    (L, PT2, f"Manual QC compares reports with NWS MPE and radar maps ([QA/QC 2019]({QAQC19}), p. 3), a minor outside reference for QC rather than a calibration service.", "F"),
]
DIRS1_GAPS = [
    ("S", "A written NWS gauge specification; a peer-reviewed comparison of CoCoRaHS with NWS gauges."),
]

DIRS2 = [
    (H, PT5, f"The observer network held steady: stations reporting in the prior 12 months were 27,118 on 1 May 2024, 27,676 in 2025 and 27,623 in 2026 ([Spies, 2024]({SPIES24}); [Spies, 2026]({SPIES26})).", "A"),
    (M, PT5, f"NWS, whose offices recruit CoCoRaHS observers and whose staff serve as state coordinators in some states ([MN coordinators]({MN_COORD})), lost more than 600 staff in 2025 and had rehired about 274 by June 2026 ([E&E News, 2026]({NWS_STAFF}); [AP via PBS]({PBS_NWS})). No source shows an effect on CoCoRaHS; offices kept running drives ([NWS Mobile, 2026]({NWS_MOB})).", "F"),
    (M, PT5, f"Volunteer coordinator posts are thin: New York had county coordinators in 26 of its 62 counties ([NY newsletter, Jan 2025]({NY_NEWS})), and Texas lists vacant county posts ([Texas coordinators]({TX_COORD})).", "F"),
    (H, PT5, f"Recruiting softened: new observers in the spring contest fell from 1,884 (2024) to 1,196 (2025) and 1,544 (2026) ([Rally 2026]({RALLY26})), and the share of new stations sending a first report fell from 60% to 54%. The total stayed flat.", "C"),
    (M, PT5, f"Turnover is high but steady: about 3,000 observers stop each year ([WERA minutes]({MIN2022})); 3,170 stations last reported in 2022 and 3,245 in 2024.", "C"),
    (M, PT5, f"The 2025 committee meeting was replaced by an internal one because many participants could not attend \"due to constraints and uncertainty\" ([NIMSS 2025]({NIMSS25})).", "C"),
    (M, PT5, f"The maker of the Stratus gauge, the network's most common, \"has officially closed its production area\" ([Productive Alternatives]({PROD_ALT})); the gauges are still sold through Darter Plastics (see DIRS-5).", "C"),
]
DIRS2_GAPS = [
    ("S", "The 2025 count of stations whose last report was in 2025 (not published until a 2027 deck)."),
    ("U", "Observer counts by state over time, and where coordinator gaps line up with observer losses."),
]

DIRS3 = [
    (H, PT1, "CoCoRaHS is built from its own volunteers' manual reports, entered through its own app or web form; it takes in no outside data feed.", "A"),
    (H, PT5, f"The volunteer-built apps were retired and replaced in-house in November 2024 ([CoCoRaHS blog, 2024]({BLOG24})), with the website as a full backup route; no outage was found.", "A"),
    (L, PT2, "Manual QC uses NWS MPE and radar maps as references; no disruption to them was found.", "C"),
]
DIRS3_GAPS = []

DIRS4 = [
    (H, PT2, f"Producing and serving the data needs vendor platforms: everything sits behind \"an Azure Front Door service with Web Application Firewall\", the primary database is SQL Server in Azure, and the maps ran on \"the Carto raster mapping platform\" with \"a shared Carto database\" ([Turner, 2024]({IT24})).", "F"),
    (M, SITE, f"An outside vendor, Solliance, did the Azure migration and then helped with monitoring at $150 an hour ([Turner, 2021]({IT21})).", "F"),
    (M, PT2, "The QC ticket system moved off a Midwestern Regional Climate Center server around 2020 and onto CoCoRaHS's own web site from 1 October 2024, so QC no longer depends on another centre's computer.", "C"),
    (M, PT5, "The maps are moving from Carto to CoCoRaHS's own MapHub (November 2026), partly to cut costs.", "C"),
    (H, NCEI, "NCEI runs its own automated QA on the GHCN-Daily copy; that is NCEI's processing of its copy, not a step CoCoRaHS needs to produce its reports.", "C"),
]
DIRS4_GAPS = [
    ("S", "Who holds the Azure subscription, CSU or CoCoRaHS (not found)."),
]

DIRS5 = [
    (M, SITE, "No fallback host or second cloud is published for the Azure systems that produce and serve the data; the 2021 architecture shows one primary database and no backup component.", "F"),
    (M, PT5, f"No substitute matches CoCoRaHS's density of manual daily gauge reports: COOP has about 6,700 sites and is itself under a proposed \"right-sizing\" ([Federal Register 2026-09099]({COOP_FR})); PRISM ingests CoCoRaHS ([PRISM]({PRISM})); nClimGrid-Daily uses no CoCoRaHS and is sparser (adding CoCoRaHS \"triples\" the inputs; [Durre, 2024]({DURRE24})).", "F"),
    (M, PT5, f"The gauge has alternative suppliers: Stratus gauges are still sold, and reportedly made in Minnesota, by Darter Plastics ([Darter]({DARTER}); [FLI Products, 2026]({FLI})), and the TROPO (Climalytic) and the NWS 8-inch gauge are also approved.", "A"),
    (H, PT5, f"Data entry has a backup: the app and the website give \"the same user experience\" ([user guide]({APP_GUIDE})).", "A"),
    (M, PT5, "The cheap, most common gauge still has one maker, and CoCoRaHS's own gauge page still names the closed maker; the alternatives cost more ($89.99 for the TROPO).", "C"),
    (H, PT5, f"MRMS gives full CONUS coverage from radar plus automated gauges, so it can stand in for some uses but not for manual daily gauge totals ([MRMS]({MRMS})).", "C"),
    (M, GAUGES, "COOP, the main other manual network, faces a proposed restructuring that may lean on mesonet or contractor data (May 2026 notice; no decision).", "C"),
]
DIRS5_GAPS = [
    ("U", "Stage IV as a substitute (its gauge inputs were not read)."),
    ("S", "Whether Darter took over the Stratus molds (not published)."),
]

# ---------------------------------------------------------------- Repository resilience (RRS)

RRS1 = [
    (M, SITE, f"Two organizations in separate places hold the core reports: CoCoRaHS's database (in Azure, run from Fort Collins) and NCEI's GHCN-Daily (Asheville, moving to AWS), which has taken CoCoRaHS daily precipitation and snow since 12 July 2010 ([GHCN-Daily status]({GHCND_STATUS})).", "F", "CoCoRaHS database and data site; NOAA NCEI (GHCN-Daily)"),
    (H, SITE, "NCEI's copy is partial: it holds only precipitation and snow elements, only stations with at least 100 values, and new stations once a month. No copy of the hail, condition-monitoring or ET reports, or of the observer and station records, was found outside CoCoRaHS.", "A", NCEI_R),
    (M, SITE, f"No source describes a check of NCEI's copy against the CoCoRaHS database; NCEI checks only for CoCoRaHS reports that duplicate NWS COOP submissions (345 GHCN-Daily stations in 2022; [NCEI, 2022]({NCEI22})).", "A", NCEI_R),
    (M, SITE, "CoCoRaHS's own copy sits in one Azure database; its region and any geo-redundant backup are not published.", "C", COCO),
    (M, NCEI_A2, f"NCEI's Asheville copies (where GHCN-Daily is archived) are two tapes, the offsite one \"several kilometers away\" ([CoreTrustSeal]({CTS})); OIG found NOAA's cloud platform \"resides in a single region\" ([OIG-24-034-A]({OIG24})).", "C", NCEI_R),
    (M, PT1, "MADIS (nine states), the Iowa Environmental Mesonet and ACIS hold reformatted or partial copies; they are not repositories.", "C", "CoCoRaHS database and data site; NOAA NCEI (GHCN-Daily)"),
]
RRS1_GAPS = [
    ("P", "CoCoRaHS's Azure region and backup copies (CoCoRaHS holds them)."),
    ("P", "NCEI's AWS regions and copy count after the move (NCCF design documents)."),
]

RRS2 = [
    (M, SITE, "Targeted searches of CoCoRaHS, CSU, NCEI and Wayback pages found no checksum, fixity or database-integrity checks published for CoCoRaHS; \"Review Database Data Versioning\" is only a possible future project.", "A", COCO),
    (H, NCEI_A2, f"NCEI checks checksums at ingest and \"Any time a file is pulled\", and compares file sizes between copies \"on a routine basis\", with no checksum schedule ([CoreTrustSeal]({CTS})).", "A", NCEI_R),
    (L, SITE, "Azure SQL keeps automatic backups by default, but that is the vendor's default, not evidence of CoCoRaHS's settings (the vendor page was not read).", "C", COCO),
]
RRS2_GAPS = [
    ("P", "Any integrity check on the CoCoRaHS database (CoCoRaHS holds it); NCEI's SOP 60-6-015 (not public)."),
]

RRS3 = [
    (M, SITE, "Targeted searches found no published CoCoRaHS disaster recovery or continuity plan, or a test of one.", "A", COCO),
    (M, SITE, f"CSU had no formal IT disaster-planning policy in FY2023 ([State Auditor FY2023]({AUDIT23})); it was implemented by FY2025 ([FY2025]({AUDIT25})). The audits covered CSU's business systems, not the Climate Center's Azure systems.", "C", COCO),
    (H, NCEI_A2, f"NCEI has an Information System Contingency Plan with an annual Business Impact Analysis, but it \"cannot be shared outside the US Government\" and no test date or result is published ([CoreTrustSeal]({CTS})).", "C", NCEI_R),
]
RRS3_GAPS = [
    ("P", "Any CoCoRaHS DR plan and test (ask the developer or info@cocorahs.org)."),
    ("P", "NCEI's contingency-plan test results."),
]

RRS4 = [
    (H, PT4, f"Donations rose to records: $279,040 for the 2024 drive and $351,517 for the 2025 drive ([CSU GiveCampus]({GIVE})), and HQ says gifts support \"data management, web development work\" ([The Catch, Dec 2025]({CATCH_DEC25})).", "F", COCO),
    (L, PT4, f"The National Mesonet Program, which paid 12–15% of CoCoRaHS's revenue in FY2020–22, was funded at $30.0M in FY2026 ([FY2026 JES]({JES26_NMP})); whether CoCoRaHS is still paid under it is not known.", "F", COCO),
    (M, PT3, f"CoCoRaHS has had no direct federal grant since 2017 and runs year to year on data-user payments, an annual donation drive and NMP money ([FY22 budget slides]({BUDGET22})); the 2025 drive was \"to help sustain the network in 2026\".", "A", COCO),
    (M, PT5, f"Cost pressure continues: the maps are moving to MapHub partly from \"a need to reduce our costs\" (November 2026; [CoCoRaHS blog]({MAPHUB})).", "A", COCO),
    (L, PT4, "The 2026 NMP recompete (KBR prime from 1 September 2026) does not name CoCoRaHS, and NSF award 2313996, with CoCoRaHS as a partner project, was terminated in April 2025 (education research, not site money).", "A", COCO),
    (H, NCEI, f"NCEI's FY2027 request is $52.0M against a $69.8M base; the House committee gives $60.0M and the Senate committee $70.0M ([NOAA FY2027 CJ]({CJ27})).", "A", NCEI_R),
    (M, NCEI, f"NCEI's staff fell from 184 FTE (FY2024) to 140 (FY2026 enacted column), with 58 departures by August 2025 ([Asheville Watchdog]({WATCHDOG_AUG})).", "A", NCEI_R),
    (M, NCEI, f"FY2026 was enacted above the request: $69.0M for NCEI ([FY2026 JES]({JES26})).", "F", NCEI_R),
    (M, PT4, "CSU's FY2027 cuts are not tied to the Colorado Climate Center or CoCoRaHS.", "C", COCO),
]
RRS4_GAPS = [
    ("P", "Who pays for CoCoRaHS's hosting and its NMP amount; NCEI's FY2026 spend plan."),
]

RRS5 = [
    (M, SITE, f"CoCoRaHS came through the end of its NOAA (2015) and NSF (2017) grants, when \"The future of CoCoRaHS was very much in doubt\" ([2016 letter]({LETTER16})), and through the founder's 2017 retirement, with no data loss reported.", "F", COCO),
    (M, SITE, f"The planned move to Azure on 7 August 2020 took \"a few hours of downtime\" and no loss was found ([The Catch, Jul 2020]({CATCH_JUL20})).", "F", COCO),
    (M, SITE, f"NCEI's GHCN-Daily copy kept updating automatically through the October 2013 and January 2018 shutdowns ([GHCN-Daily status]({GHCND_STATUS})).", "F", NCEI_R),
    (M, NCEI_A2, f"After Hurricane Helene (September 2024) NCEI restored ingest by 11 December and \"92% of the ingest backlog was recovered\" ([NCEI FY25 Q1]({SOS25Q1})).", "F", NCEI_R),
    (M, NCEI_A2, "The other 8% of Helene's ingest backlog is not accounted for, and no final loss count was published.", "A", NCEI_R),
    (M, SITE, f"Outages that weren't funding or leadership disruptions: on 7 April 2011 a host firewall took the site down and about 500 daily reports were never entered after back-filling ([The Catch, Apr 2011]({CATCH_APR11})); on 9 April 2013 a data-centre power problem took it down for at least three hours ([The Catch, Apr 2013]({CATCH_APR13})).", "C", COCO),
    (M, SITE, f"NCEI's daily CoCoRaHS updates were interrupted before 1 December 2020 by \"an issue with the provider\" ([GHCN-Daily status]({GHCND_STATUS})); no loss is stated.", "C", NCEI_R),
    (M, NCEI, f"NCEI's cloud move is still under way, with \"delayed data archival\" in November 2026 and no statement on loss ([NCEI Alerts]({ALERTS})).", "C", NCEI_R),
]
RRS5_GAPS = [
    ("S", "How the sites fared through the 2014–15 award endings (no source describes it); outages after 2020 (no public log)."),
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
    "producer": "CoCoRaHS headquarters, Colorado Climate Center, Colorado State University",
    # True: CoCoRaHS headquarters both makes the reports and holds the archive of record (its own database).
    "producer_is_repository": True,
    "repositories": [
        {"name": COCO, "role": "parent"},
        {"name": NCEI_R, "role": "child"},
    ],
}

write_categories("cocorahs", SUBCATEGORIES, DATASET)
