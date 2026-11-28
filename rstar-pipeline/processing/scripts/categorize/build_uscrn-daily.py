"""Build the USCRN Daily R* categorization JSON (first pass, 2026-11-27).

Hand-sorted evidence from every answer file in rstar-pipeline/input/web-research/ that bears on USCRN Daily (daily01:
NCEI's daily files for the U.S. Climate Reference Network, 2000 to present; DOI 10.7289/V5H13007 covers all USCRN
products). NCEI ingests, quality-controls, produces, archives and serves daily01; NOAA ARL's Atmospheric Turbulence and
Diffusion Division (ATDD) in Oak Ridge built and maintains the 141 stations, with a non-federal field team (ORAU, then
CISESS). Runs used:
- the five about-datasets/uscrn-daily runs (about-pt1, qc-formats-pt2, people-funding-pt3, threats-news-pt4,
  inputs-pt5);
- the two archives/noaa-ncei runs (A1 threats; A2 resilience): NCEI is the producer and the only repository;
- instruments/noaa-rain-gauges (its USCRN row);
- GHCN-Daily's repository-resilience run (pt9), for one NCEI-wide fact (OIG on contingency-plan testing), as GPCP and
  PERSIANN-CDR did.
Left out: both satellite runs (USCRN uses no satellite data; the GOES satellite is only its data relay, covered by its
own pt1, pt2 and pt5). GHCN-Daily's pt8 covers ATDD's calibration team as a GHCN-Daily source; USCRN's own pt2 and pt5
cover the same ground, so nothing else is borrowed.

Filing rules: rstar-pipeline/input/framework/rstar-categorization-decisions.md. Steps:
rstar-pipeline/processing/instructions/categorize-dataset-instructions.md.
Markdown links [label](url) in the text become <a> tags (rstar_common.py does the writing and scoring).

Run:  python3 rstar-pipeline/processing/scripts/categorize/build_uscrn-daily.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rstar_common import H, M, L, write_categories  # noqa: E402

# data-source values: the research run folder names
PT1 = "2026-11-26_uscrn-daily-about-pt1"
PT2 = "2026-11-26_uscrn-daily-qc-formats-pt2"
PT3 = "2026-11-26_uscrn-daily-people-funding-pt3"
PT4 = "2026-11-26_uscrn-daily-threats-news-pt4"
PT5 = "2026-11-27_uscrn-daily-inputs-pt5"
NCEI = "2026-11-17_noaa-ncei-threats"
NCEI_A2 = "2026-11-23_A2_Rstar_query-noaa_ncei"
GAUGES = "2026-11-18_noaa-rain-gauge-threats"
GH_RRS = "2026-11-23_ghcn-daily-repository-resilience-pt9"

# Each evidence item is (confidence, source run, text, stance[, repository for RRS]); stance toward the
# subcategory's statement: F = for, A = against, C = context (not directly tied, or doesn't show it true or false).
# Each gap is (status, text): S = searched and none found, P = not public, U = not searched.

# Repository names (match DATASET below)
NCEI_R = "NOAA NCEI (daily01 archive)"
CDS_X = "Copernicus CDS (not a repository)"
DRP_X = "Data Rescue Project (not a repository)"

# Frequently cited pages: NCEI's USCRN files and documents
CRN_DOCS = "https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program"
DAILY01 = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/"
SNAPSHOTS = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/snapshots/"
SNAP_2611 = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/snapshots/CRND0103-202611160850.zip"
UPDATES25 = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/updates/2025/"
D01_2026 = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/2026/"
README = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt"
STATUS = "https://www.ncei.noaa.gov/pub/data/uscrn/products/DATASET-STATUS.txt"
STATIONS = "https://www.ncei.noaa.gov/pub/data/uscrn/products/stations.tsv"
C00546 = "https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00546"
DATACITE = "https://api.datacite.org/dois/10.7289/V5H13007"
DMP17 = f"{CRN_DOCS}/USCRN_Data_Management_Plan-August_2017.pdf"
INGEST = f"{CRN_DOCS}/CRN_Ingest_Functional_Spec.pdf"
X040 = f"{CRN_DOCS}/X040_d0.pdf"
X041 = f"{CRN_DOCS}/X041_d0.pdf"
INSTALL = f"{CRN_DOCS}/USCRN%20Installation%20Guide.pdf"
CCRS = f"{CRN_DOCS}/CCRs/"
TN05002 = f"{CRN_DOCS}/technotes/TN05002PrecipTesting.pdf"
OAP20 = ("https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2015-09/"
         "USCRN_OAP2.0.Description_PrecipChanges.pdf")
OAP21 = ("https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2017-06/"
         "USCRN_OAP2.1.Description_PrecipChanges.pdf")
DOC_PAGE = "https://www.ncei.noaa.gov/access/crn/documentation.html"
CONTACTS = "https://www.ncei.noaa.gov/access/crn/contacts.html"
FY06 = "https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY06_USCRN_Annual_Report.pdf"
FY19 = "https://www.ncei.noaa.gov/pub/data/uscrn/publications/annual_reports/FY19_USCRN_Annual_Report.pdf"
ISIS = "https://www.ncei.noaa.gov/access/isis/station.htm?stationid=1019"
# ARL, ATDD and partners
ARL_STORY = "https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/"
ARL_UPGRADE = "https://www.arl.noaa.gov/news-pubs/arl-news-stories/upgrading-arls-largest-meteorological-network/"
ARL_BLUEHILL = "https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-blue-hill-observatory/"
ARL_DIR = "https://www.arl.noaa.gov/about/staff-directory-2/"
ARL_DIR_2024 = "https://web.archive.org/web/20241213113100/https://www.arl.noaa.gov/about/staff-directory-2/"
DIAMOND_BIO = "https://www.arl.noaa.gov/about/staff-directory-2/howard-diamond/"
ARL_REVIEW23 = "https://www.arl.noaa.gov/wp_arl/wp-content/uploads/2025/02/ARL-Review-Response-Sept-30-2023-edited.pdf"
ORAU25 = "https://orau.org/news/resources/2025-orau-story.pdf"
DIAMOND13 = "https://mural.maynoothuniversity.ie/6481/1/PT_US%20climate.pdf"
OPM_FERS = "https://www.opm.gov/retirement-center/fers-information/eligibility/"
# Budgets and news
CJ21 = "https://www.noaa.gov/sites/default/files/legacy/document/2020/Mar/508%20Compliant_FY21%20NOAA%20CJ.pdf"
CJ27 = "https://www.noaa.gov/sites/default/files/2026-04/FY2027-NOAA-CJ-Submission.pdf"
CRS_CR = ("https://www.everycrsreport.com/files/2026-09-17_R49353_98ddd8e7b1852b47b24e394ed7ddf6d6d53b4632"
          ".html")
HRPT652 = "https://www.govinfo.gov/content/pkg/CRPT-119hrpt652/html/CRPT-119hrpt652.htm"
SEN27 = "https://www.appropriations.senate.gov/imo/media/doc/cjs_explanatory_stmt.pdf"
CREC26 = "https://www.govinfo.gov/content/pkg/CREC-2026-01-08/html/CREC-2026-01-08-pt1-PgH255.htm"
AIP25 = "https://www.aip.org/fyi/democrats-accuse-administration-of-cutting-spending-at-nasa-and-noaa"
BRL26 = ("https://boulderreportinglab.org/2026/04/02/half-of-staff-at-boulders-noaa-global-monitoring-lab-face-"
         "furloughs-as-funding-freeze-drags-on/")
NPR25 = "https://www.npr.org/2025/04/09/nx-s1-5356166/noaa-contracts-reviewed-one-by-one"
TN_LOOKOUT = "https://tennesseelookout.com/2025/09/30/map-shows-how-trumps-proposed-noaa-budget-cuts-could-affect-tennessee/"
EOS26 = "https://eos.org/features/the-looming-data-loss-that-threatens-public-safety-and-prosperity"
AMS25 = "https://www.eurekalert.org/news-releases/1080955"
DRP = "https://portal.datarescueproject.org/datasets/us-climate-reference-network-uscrn/"
# Inputs, makers and substitutes
CAMPBELL = "https://s.campbellsci.com/documents/us/miscellaneous/cr3000-discontinuation-notice.pdf"
CR1000X = "https://www.campbellsci.com/products/cr1000x"
ESPC25 = "https://ospo.noaa.gov/data/messages/2025/02/MSG_20250212_1541.html"
ESPC26 = "https://ospo.noaa.gov/data/messages/2026/07/MSG_20260716_1637.html"
DADDS = ("https://www.noaasis.noaa.gov/pdf/docs/TWG2025/1400%20Replacement%20DADDS%20Demo%20&%20User%20Input"
         "%20Detwiler.pdf")
WALLOPS25 = ("https://noaasis.noaa.gov/pdf/docs/TWG2025/1105%20Wallops%20Command%20and%20Data%20Acquisition"
             "%20Update%20Sullivan.pdf")
GEONOR = "https://geonor.com/t-200b-all-weather-precipitation---rain-gauge"
VAISALA = "https://www.vaisala.com/en/products/weather-environmental-sensors/rain-detector-drd11a"
KISTERS_TB3 = "https://hydromet-products.kisters-group.com/products/instruments/meteorology/tb3/"
SPICE = ("https://old.wmo.int/extranet/pages/prog/www/IMOP/intercomparisons/SPICE/Docs/SPICE%20GEONOR%20Calibration"
         "%20and%20Configuration%20Recommendations%20Dec%205,%202012.pdf.pdf")
IMO24 = "https://arc.lib.montana.edu/snow-science/objects/ISSW2024_P8.30.pdf"
BUBAN20 = "https://repository.library.noaa.gov/view/noaa/29193/noaa_29193_DS1.pdf"
COOP_FR = "https://public-inspection.federalregister.gov/2026-09099.pdf"
FRANKFORT = "https://www.weather.gov/lmk/FrankfortASOSRetiringasOfficialNWSClimateSite"
AASC = ("https://stateclimate.org/docs/AASC%20Recommendations%20and%20Best%20Practices%20for%20Mesonets%20-%20Final,"
        "%20Ver%201;%20approved%2026%20Jun%2019.pdf")
SCN14 = "https://www.weather.gov/media/notification/pdfs/scn14-25usrcrn_decom.pdf"
CDS = ("https://cds.climate.copernicus.eu/datasets/insitu-observations-near-surface-temperature-us-climate-reference-"
       "network?tab=overview")
NODD = "https://www.noaa.gov/nodd/datasets"
# NCEI-wide
JES26 = "https://www.appropriations.senate.gov/imo/media/doc/fy26_cjs_jes.pdf"
WATCHDOG_AUG = ("https://avlwatchdog.org/top-climate-scientists-departure-is-sign-of-brain-drain-at-noaa-hub-in-"
                "asheville-and-of-deep-cuts-to-research-across-the-country/")
CTS = "https://dataverse.nl/api/access/datafile/469675"
OIG24 = "https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf"
SOS25Q1 = "https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf"
ALERTS = "https://www.ncei.noaa.gov/alerts"
CLOUD = "https://www.ncei.noaa.gov/news/cloud-migration"
CLOUD_FAQ = "https://www.ncei.noaa.gov/news/cloud-migration-FAQ"
S3923 = "https://www.govinfo.gov/content/pkg/BILLS-119s3923es/html/BILLS-119s3923es.htm"

# ---------------------------------------------------------------- People risk (P)

P1 = [
    (M, PT3, "Targeted searches found no USCRN succession, workforce or knowledge-transfer plan at USCRN, ARL or NCEI, and no OIG or GAO audit of USCRN.", "F"),
    (L, PT3, f"According to a search summary only (the PDF returned HTTP 403), ARL's lab-review response says civil-service rules bar naming successors in advance ([ARL review response, 2023]({ARL_REVIEW23})).", "F"),
    (M, PT2, f"The handover documents are incomplete and old: the code, the QC parameter files, the ISIS station-metadata system, the change requests after CCR 36 of 2008 ([CCRs folder]({CCRS})), the rule that sums the hourly totals into the daily value and any current ATDD maintenance manual are not public, and most of the library dates from 2002–2007.", "F"),
    (L, PT3, f"Mark Hall, Ed Dumas and Michael Buban, on the FY10 and FY19 USCRN team lists, are not in ARL's directory in December 2024 or now ([ARL directory, Dec 2024]({ARL_DIR_2024})); no source says who took over their work.", "F"),
    (H, PT2, f"What is written down: NCEI's public library holds the requirements, the maintenance, commissioning and data-management plans, the installation guide, the ingest specification, the precipitation algorithm descriptions with their constants, and the product READMEs ([documentation page]({DOC_PAGE})). The run judged it \"enough to re-implement the precipitation algorithm and to read the files, but not to run the processing\".", "C"),
    (H, PT3, f"The team has depth in places: ATDD's field team is \"a small team of eight technicians and engineers\", \"the majority\" with ARL \"15 years or more\" ([ARL]({ARL_STORY})), and the FY19 Climate Science Team (Palecki, Leeper, Rennie) gives Palecki two possible backups ([FY19 report]({FY19})). No deputy is named for the Program Manager or the field lead.", "C"),
    (M, PT4, f"ATDD is no longer a division: by November 2026 ARL lists a \"SORD-ATD\" office inside its Special Research and Operations Division, with ATDD's former director John Kochendorfer as Division Deputy; no announcement or date was found ([ARL directory]({ARL_DIR})).", "C"),
]
P1_GAPS = [
    ("S", "A written succession or knowledge-transfer plan for USCRN (searched at USCRN, ARL and NCEI; none found)."),
    ("U", "ARL's 2016 and 2022 lab-review responses (PDFs refused with HTTP 403), which may say how ARL handles succession."),
    ("U", "Whether the SORD reorganization changed who holds USCRN's roles."),
]

P2 = [
    (L, PT3, f"Estimate: Howard Diamond, USCRN Program Manager, began federal service in 1981 ([ARL bio]({DIAMOND_BIO})), about 45 years, so he is likely already eligible under FERS (minimum retirement age 56–57 with 30 years; [OPM]({OPM_FERS})). Estimated age about 66–70.", "F"),
    (L, PT3, "Estimate: Michael Palecki, NCEI's science lead for processing and QC (USCRN since 2008), has his earliest publication in 1986 (OpenAlex and Crossref agree): estimated age 65–70, likely already eligible (62 with 5 years).", "F"),
    (L, PT3, "Estimate: Tilden Meyers, ATDD scientist on the FY10 and FY19 USCRN teams and still publishing on USCRN, has his earliest publication in 1985–86 and an ARL affiliation from 1986: estimated age 66–71, likely already eligible.", "F"),
    (L, PT3, "Estimate: Ronald Leeper (CISESS, earliest publication 2006; under NC State's TSERS rules, 16 years' service), John Kochendorfer (2003–05), Temple Lee (2006) and Jared Rennie (2011) are about 40–53, so retirement within two years is unlikely.", "A"),
    (M, PT3, "The field team (Brent French, Tim Wilson and the technicians) are not federal staff (ORAU, then a cooperative institute), so FERS doesn't apply; their employers' rules and their ages were not found.", "C"),
    (H, PT3, "C. Bruce Baker, ATDD Director in FY19, is not in ARL's directory by December 2024; he has already left, so he counts in P-1, not here.", "C"),
    (M, PT4, f"NCEI lost 58 employees, about a third, by spring 2025, according to a retiring NCEI official ([Asheville Watchdog]({WATCHDOG_AUG})); no source names a USCRN team member among them.", "C"),
]
P2_GAPS = [
    ("P", "Real ages, service dates and retirement plans (personnel records)."),
    ("S", "Publication years or ORCIDs for French, Hall and Baker; the field team's employer retirement rules."),
]

P3 = [
    (M, PT2, f"The production code is not published: the ingest decoder, the QC flagging, the precipitation calculation, the USCRN database and product generation are NCEI's, and no NOAA repository holds them, although the 2007 requirements say \"the detailed quality control software code shall be made available to users\" ([Functional Requirements, 2007]({X040})). The only GitHub hits were third-party readers.", "F"),
    (M, PT2, f"The QC limits sit in internal CSV parameter files and in NCEI's ISIS system, neither published ([ingest specification]({INGEST})); no public document gives the rule that turns hourly totals into the daily value (for example how many missing hours make a day missing); and who runs the manual \"exception procedure\" today isn't stated.", "F"),
    (M, PT2, f"Every calibration procedure found dates from 2002–2003 ([X041 maintenance plan]({X041})); no current ATDD procedure was found, and the change requests after 2008, including CCR 46 that approved the current algorithm, are not in the public folder ([CCRs folder]({CCRS})).", "F"),
    (H, PT2, f"The precipitation algorithm is documented well enough to re-implement: the OAP 2.0 and 2.1 descriptions give its steps and constants (MIN_PRECIP 0.2 mm, DELTA_THRESHOLD 0.5 mm, GIANTSTEP 25 mm) ([OAP 2.0]({OAP20}); [OAP 2.1]({OAP21})), the method is peer-reviewed (Leeper, Palecki and Davis 2015, JTECH), and the ingest specification lists the automatic RANGE, DELTA, DOOR, FROZEN and SENSOR checks ([ingest specification]({INGEST})).", "A"),
    (H, PT2, f"The file formats are documented in each product's README ([daily01 README]({README})), which helps users read the data rather than rebuild it.", "C"),
]
P3_GAPS = [
    ("P", "The production code, the QC parameter files and ISIS (NCEI internal)."),
    ("S", "The daily summation and completeness rule (not published; NCEI's USCRN team holds it)."),
    ("U", "Whether the datalogger program is published; the X030–X039 plans and the Site Information Handbook (not read)."),
]

P4 = [
    (M, PT3, f"Howard Diamond is the only named Program Manager: NCEI's contacts page names him alone and no deputy is named ([NCEI contacts]({CONTACTS})); he also directs ARL's ASMD division ([ARL bio]({DIAMOND_BIO})).", "F"),
    (M, PT3, f"Field maintenance is shared: \"a small team of eight technicians and engineers\" makes every station's annual visit, most with 15 or more years at ARL ([ARL]({ARL_STORY})).", "A"),
    (M, PT3, f"Science and QC are shared: the FY19 Climate Science Team is Palecki (NCEI) with Leeper and Rennie, non-federal affiliates who could back him up ([FY19 report]({FY19})).", "A"),
    (H, PT4, f"The field team still works, but in smaller crews: \"a crew of five technicians and engineers\" replaced the transmitters at 139 towers, the last on 25 April 2026 ([ARL, 2026]({ARL_UPGRADE})).", "C"),
    (M, PT4, "ATDD lost its own director post when it was folded into ARL's SORD division (Kochendorfer is now Division Deputy).", "C"),
    (M, PT2, f"Ingest, QC flagging and the products run automatically in NCEI's ingest system and USCRN database ([Data Management Plan, 2017]({DMP17})); a manual exception procedure exists, but who does it now isn't stated.", "C"),
]
P4_GAPS = [
    ("P", "Cover arrangements for the Program Manager and the field lead; the federal and non-federal split of the field team."),
]

# ---------------------------------------------------------------- Data risk (D)

D1 = [
    (H, PT4, f"The FY2027 request terminates Climate Laboratories and Cooperative Institutes (−$104,964K, −180 FTE) and says NOAA will close ARL in College Park, Idaho Falls and Oak Ridge \"as well as a nation-wide network of soil moisture sensors\" ([NOAA FY2027 CJ]({CJ27})). ATDD in Oak Ridge runs USCRN; the request doesn't name USCRN. It is pending: NOAA runs on a continuing resolution to 11 December 2026 ([CRS R49353]({CRS_CR})).", "F"),
    (M, PT4, f"The House FY2027 committee report gives Climate Laboratories and Cooperative Institutes $92,500K against $103,877K for FY2026, an 11% cut by the minority's count, while directing NOAA \"to avoid closures, consolidations, or eliminations\" ([H.Rept. 119-652]({HRPT652})). Not law.", "F"),
    (H, NCEI, f"NCEI, which produces and hosts daily01, faces a pending FY2027 request of $52.0M against a $69.8M base; the House committee gives $60.0M and the Senate committee $70.0M ([NOAA FY2027 CJ]({CJ27})).", "F"),
    (H, PT4, f"Congress rejected the FY2026 closure: the FY2026 law gives Climate Laboratories and Cooperative Institutes $104,102K ([Congressional Record H255]({CREC26})), and the Senate's FY2027 draft gives $104,602K and \"rejects the proposed terminations\" ([Senate explanatory statement]({SEN27})).", "C"),
    (M, PT4, f"No FY2026 spend plan is public and no report says it cuts ARL; for FY2025, senators said NOAA's plan was $246M below what Congress directed, with labs and cooperative institutes affected ([AIP, 2025]({AIP25})).", "C"),
    (M, PT4, f"OMB paused NOAA grants, cooperative-institute grants included, from 27 February to April 2026 ([Boulder Reporting Lab]({BRL26})); the USCRN field team now sits under a cooperative institute, but no source ties the pause to USCRN.", "C"),
    (H, PT3, f"Before 2025: the FY2019, FY2020 and FY2021 requests each proposed closing ARL, with USCRN \"consolidated into other NOAA laboratories\" ([FY2021 CJ]({CJ21})); none took effect.", "C"),
    (M, PT3, "USCRN has no budget line of its own: it is paid from OAR's climate line through ARL, from NCEI's line and from cooperative agreements, and no USCRN amount was found for any year.", "C"),
]
D1_GAPS = [
    ("P", "NOAA's FY2026 spend plan for ARL (held by the Appropriations Committees)."),
    ("S", "The FY2027 outcome after the continuing resolution ends on 11 December 2026."),
    ("P", "USCRN's own budget (NOAA's budget office or ARL's spend plan; a FOIA request)."),
]

D2 = [
    (M, PT1, f"daily01's home and archive of record is a single NCEI server: the FTP and web copies are the same files, and the weekly snapshots sit beside them on it ([daily01]({DAILY01}); [snapshots]({SNAPSHOTS})). NCEI's plan names no second site and describes backups only as \"the latest and best practices\" ([Data Management Plan, 2017]({DMP17})).", "F"),
    (M, PT1, f"Only one organization serves the original files: NOAA's open-data cloud list has no USCRN entry ([NODD list]({NODD})), and no ARL copy was found.", "F"),
    (H, PT1, f"Behind the files, NCEI's holdings are \"archived on a Hierarchical Data Storage System\" with tape robotics ([Data Management Plan, 2017]({DMP17}), §8.4).", "C"),
    (M, NCEI_A2, f"NCEI's Asheville archive keeps its offsite tape copy only \"several kilometers away\" ([CoreTrustSeal]({CTS})); no source says which NCEI site holds USCRN's tapes.", "C"),
    (M, PT1, f"Copernicus's Climate Data Store holds a reprocessed copy (values from 2006, NetCDF and CSV with uncertainties added, updated yearly; its download form was \"temporarily closed\" on 26 November 2026; [CDS]({CDS})). It is not the original format, so it is not a repository.", "C"),
    (H, PT4, f"NCEI is moving bulk data folders \"from web accessible folders (WAFs) to Amazon Simple Storage Service (S3)\" through spring 2027 ([NCEI FAQ]({CLOUD_FAQ})); USCRN is not named.", "C"),
    (M, PT4, f"The Data Rescue Project archived 52.0 GB of USCRN on 24 March 2025 ([DRP]({DRP})), a volunteer snapshot, not a repository.", "C"),
]
D2_GAPS = [
    ("P", "Which NCEI site holds USCRN's tapes, and its AWS regions after the move (NCEI holds them)."),
    ("U", "NCAR EOL dataset 100.023, \"NOAA Climate Reference Network (CRN) Data\", a possible copy (its page could not be read)."),
]

D3 = [
    (H, NCEI, f"NCEI, which runs the USCRN portal and the daily01 files, faces a pending FY2027 request of $52.0M against a $69.8M base, most of it from contracted services (advisory services −$11.04M, non-federal services −$6.77M; [NOAA FY2027 CJ]({CJ27})).", "F"),
    (M, NCEI, f"NCEI's staff fell from 184 FTE (FY2024) to 140 (FY2026 enacted column), with 58 departures by August 2025 ([Asheville Watchdog]({WATCHDOG_AUG})); no source names USCRN staff among them.", "F"),
    (H, PT4, f"daily01 stayed current through the disruptions: update files were written every day of the 1 October – 12 November 2025 shutdown, about two days after each data day ([updates/2025]({UPDATES25})); weekly snapshots ran every Monday from 6 January 2025 to 16 November 2026 with no week missing ([snapshots]({SNAPSHOTS})); and on 26 November 2026, 157 of 159 station files for 2026 had been updated the day before ([daily01/2026]({D01_2026})).", "A"),
    (M, PT4, f"NCEI's high-severity alert for 16 November – 31 December 2026 says \"many access portals ... and data folders are currently unavailable\" ([NCEI alerts]({ALERTS})); USCRN is not named, and daily01 was updating during it.", "C"),
    (M, PT4, "During the 2025 shutdown NCEI's home page said \"This site will not be updated\", while the USCRN portal kept serving its normal page.", "C"),
    (L, PT2, f"NCEI's catalog landing page for the USCRN record returned HTTP 503 during the 26 November run ([C00546 record]({C00546})); the data files were not affected.", "C"),
    (M, PT4, f"OAR staff were told in April 2025 that web-hosting contracts were likely to be cancelled ([NPR, 2025]({NPR25})); daily01 is served by NCEI, not OAR.", "C"),
]
D3_GAPS = [
    ("S", "Who staffs the USCRN portal and file service at NCEI, and whether the November 2026 alert reached the USCRN folders."),
]

D4 = [
    (H, PT2, f"The daily files are open fixed-width ASCII text with a column README, served over open HTTPS and FTP with no login; no route needs proprietary software ([daily01 README]({README})).", "A"),
    (M, PT2, f"The NCEI route is only partly FAIR: it has DOI 10.7289/V5H13007 and a catalog record ([DataCite]({DATACITE})), but no stated licence (DataCite's rightsList is empty) and its own variable names (P_DAILY_CALC), not CF names. That is findability and reuse, not format obsolescence.", "C"),
    (M, PT2, "Some program documents are old .doc and .xls files (2002–2007).", "C"),
    (H, PT2, f"Copernicus's copy is NetCDF4 or CSV under CC-BY, but it needs a login and licence acceptance ([CDS]({CDS})); it is a third-party reformatted copy.", "C"),
]
D4_GAPS = []

D5 = [
    (M, PT4, f"USCRN is named in news about the proposed cuts: Tennessee Lookout (30 September 2025) on the Crossville station and the OAR labs in Oak Ridge ([Tennessee Lookout]({TN_LOOKOUT})), the AMS and NWA appeal \"Stand up for NOAA research\" (17 April 2025; [EurekAlert]({AMS25})), and an Eos feature by Karl et al., \"The Looming Data Loss That Threatens Public Safety and Prosperity\" (9 January 2026; [Eos]({EOS26})).", "F"),
    (M, PT4, f"No removal, alteration, access restriction or political pressure on USCRN's records was found for 2025–2026, and stations.tsv lists no USCRN closing after 2016 ([stations.tsv]({STATIONS})).", "A"),
    (M, PT4, f"146 of the 159 data-year-2023 files were rewritten on 14 May 2026 with no entry in the change log, whose newest entry is from 2017 ([DATASET-STATUS.txt]({STATUS})): undocumented reprocessing, not evidence of suppression.", "C"),
    (M, PT4, f"The Data Rescue Project archived USCRN in March 2025 ([DRP]({DRP})), a sign of concern, not of pressure on the records.", "C"),
]
D5_GAPS = [
    ("U", "Two Science articles (bot check) and local Oak Ridge and Knoxville papers (not reachable)."),
]

# ---------------------------------------------------------------- Dependent infrastructure resilience (DIRS)

DIRS1 = [
    (M, PT2, f"ATDD, which takes the measurements, calibrates the Geonor gauges itself at the annual visits, with its own brass weights \"compared to a NIST traceable standard weight\" ([X041 maintenance plan]({X041}); [Installation Guide]({INSTALL})); ARL still describes calibrating at every visit ([ARL]({ARL_STORY})). No outside calibration service, WMO centre or NIST service is tied to USCRN.", "A"),
    (L, PT5, f"Campbell's repair and calibration service for the CR3000 datalogger ends 31 December 2032 ([Campbell notice]({CAMPBELL})); no source says USCRN uses it.", "F"),
    (L, PT5, "ATDD's standards are \"re-certified annually\" (2003 plan), but who re-certifies them is not stated, so the one outside step is unknown.", "C"),
    (L, PT2, f"WMO-SPICE's 2012 recommendations (not about USCRN) relay Geonor's view that its factory calibration does not drift and say faulty wires go back to Geonor ([WMO SPICE]({SPICE})).", "C"),
    (M, PT2, "Every calibration procedure found dates from 2002–2003, and no wetness-sensor calibration was found.", "C"),
    (H, PT4, "ARL, whose ATDD does the calibration, is proposed for closure in the FY2027 request. That is the measuring team itself, not an outside service, so it is filed in DIRS-2 and D-1.", "C"),
]
DIRS1_GAPS = [
    ("S", "The current calibration procedure, the weight certification body and interval, and any wetness-sensor calibration (ATDD holds them)."),
]

DIRS2 = [
    (H, PT5, f"Station outages are rising: days with missing precipitation went from 1,893 (2024) to 2,810 (2025) to 4,481 (2026, to 15 November), counted from NCEI's 16 November 2026 snapshot ([snapshot]({SNAP_2611})). Eight Alaska stations were silent for 4–8 months in 2025–26, Joplin MO, St. Mary MT and Edinburg TX stopped in 2026, and precipitation is missing all of 2026 at Gadsden AL, Bedford IN and Denio NV. No source gives the causes.", "F"),
    (H, PT5, f"The datalogger is retired: Campbell retired the CR3000 on 6 January 2022, its free support ends 31 December 2027, and its named replacement, the CR1000X, was itself retired on 31 December 2024 ([Campbell notice]({CAMPBELL}); [CR1000X]({CR1000X})). No NOAA migration plan was found.", "F"),
    (M, PT5, f"Annual visits slipped: of 26 stations checked in NCEI's station-history log, 21 had a visit logged in 2024 but only 10 in 2025–26, and 10 have nothing logged after 2024 ([ISIS]({ISIS})). The log lags, so 2026 is under-recorded.", "F"),
    (H, PT4, f"The FY2027 request would close ARL, including the Oak Ridge site where ATDD maintains the stations; it is pending ([NOAA FY2027 CJ]({CJ27})).", "F"),
    (M, PT5, f"The Alaska build-out to 29 stations is \"funding dependent\" and none were added in 2024–26 ([ARL review response, 2023]({ARL_REVIEW23})). It limits growth rather than thinning the current network.", "C"),
    (H, PT5, f"The TX320 transmitter reached end of life on 31 March 2025, and the swap at 139 towers finished on 25 April 2026, before the May 2026 deadline ([ARL, 2026]({ARL_UPGRADE})).", "C"),
    (M, PT5, f"The Geonor T-200B, the Vaisala DRD11A and the TB-3 tipping bucket are on sale with no end-of-life notice ([Geonor]({GEONOR}); [Vaisala]({VAISALA}); [KISTERS]({KISTERS_TB3})).", "C"),
    (H, PT5, f"Kingston RI is being retired for siting (a parking lot \"just over 300 feet away\"), with Blue Hill MA added so \"USCRN will maintain the number of stations\" ([ARL, 2024]({ARL_BLUEHILL})); Ivotuk AK's record ends 7 April 2023.", "C"),
    (M, PT4, f"The field team moved from ORAU to cooperative-institute (CISESS) staffing in 2025, with ORAU still involved \"through a contract extension\" ([ORAU Story 2025]({ORAU25})).", "C"),
    (M, GAUGES, "A 2025 NOAA report assessed downsizing USCRN's soil-moisture sensors, not its gauges.", "C"),
]
DIRS2_GAPS = [
    ("P", "Why the Alaska stations, Joplin, St. Mary and Edinburg went silent (ARL/ATDD event notes and quarterly reports)."),
    ("U", "Maintenance visits at the other 113 stations (ISIS pages not checked); NOAA's datalogger replacement plan."),
]

DIRS3 = [
    (H, PT1, f"All routine data arrive through one feed: every hour the stations transmit through NESDIS's GOES Data Collection System to Wallops, and the FY06 report called the network \"100% dependent upon the GOES DCS systems for data delivery\" ([FY06 report]({FY06})). No Iridium or cellular backup was found.", "F"),
    (M, PT5, f"The GOES DCS has had outages and is changing: a 1 h 16 min outage on 12 February 2025 ([ESPC]({ESPC25})), the GOES-19 safehold on 15–16 July 2026 ([ESPC]({ESPC26})), and a replacement of its DADDS system planned for the end of 2026 ([TWG 2025]({DADDS})).", "F"),
    (H, PT5, "The new CS2 certification, required by 31 May 2026 with \"No waivers\", was met when the last transmitter was swapped on 25 April 2026.", "C"),
    (H, PT1, "USCRN uses no model, reanalysis or reference data: its values come from its own sensors, so the relay is its only outside feed.", "C"),
]
DIRS3_GAPS = [
    ("U", "The 2026 GOES DCS overview and the DADDS cutover date (the deck could not be read)."),
]

DIRS4 = [
    (H, PT1, f"Processing is NCEI's own: ingest, QC and the products run at NCEI on \"LRGS, Oracle database on Linux box\" ([C00546 record]({C00546})), under NCEI configuration management ([Data Management Plan, 2017]({DMP17})).", "A"),
    (M, PT2, f"Routine updates need outside facilities: data reach NCEI only through NESDIS's GOES DCS and Wallops receive station, outside both NCEI and ATDD; downloading the loggers on site is the slow fallback ([ingest specification]({INGEST})).", "F"),
    (L, PT1, "The USCRN database runs on Oracle, commercial software, but on NCEI's own computers.", "C"),
    (M, PT3, "CISESS (NC State) staff lead USCRN's QA and soil-moisture tasks (Leeper); they work with NCEI as its cooperative institute, not on outside systems.", "C"),
    (H, PT4, f"NCEI's cloud move ([NCEI]({CLOUD})) is repository IT; no source says USCRN's processing moves with it.", "C"),
]
DIRS4_GAPS = [
    ("S", "Where NCEI now runs the processing, on its own computers or in the cloud (not checked)."),
]

DIRS5 = [
    (M, PT5, f"The gauge has other suppliers: Geonor has US and Norwegian companies, NOAA tested an OTT Pluvio for USCRN in 2003–05 ([TN05002]({TN05002})), and USCRN's stated policy is to run alternative models side by side \"in case that model is discontinued\" ([Diamond et al., 2013]({DIAMOND13})).", "A"),
    (M, PT1, f"The data path has fallbacks: a second route through the USGS EDDN, NCEI's own HRIT receiver as backup since 2019 ([FY19 report]({FY19})), and the datalogger files collected at the yearly visits, which are the definitive record and fill gaps.", "A"),
    (M, PT5, f"No other relay exists: GOES DCS is the only transmission path found, and the Fairmont WV backup site has no DCS receive system ([Wallops TWG 2025]({WALLOPS25})).", "F"),
    (M, PT5, "The datalogger replacement path runs through Campbell alone (now the CR1000Xe); no NOAA plan or spares figure was found.", "F"),
    (M, PT5, f"No backup maintenance provider exists: site hosts do only \"small resets and replacements\" ([ARL]({ARL_STORY})).", "F"),
    (M, PT5, f"No substitute matches USCRN's reference quality, and it is treated as \"ground truth\" ([Buban et al., 2020]({BUBAN20})). COOP is manual or unshielded and faces a proposed \"right-sizing\" ([Federal Register 2026-09099]({COOP_FR})); ASOS is sited for aviation and its replacement AWOS \"typically do[es] not meet\" climate-record criteria ([NWS Louisville]({FRANKFORT})); state mesonets mostly use unheated tipping buckets ([AASC, 2019]({AASC})); SNOTEL is mountain and snow focused.", "F"),
    (M, PT5, f"The Pluvio is weaker in snow: Iceland's Met Office found the Pluvio2 L caught about 50% less than the Geonor at a snowy site ([IMO, 2024]({IMO24})).", "C"),
    (H, PT5, f"The one network built to USCRN's standard, the 72-station Southwest regional network, ended in 2014 after its funding was cut ([NWS SCN 14-25]({SCN14})).", "C"),
]
DIRS5_GAPS = [
    ("U", "Canada's Reference Climate Stations as a substitute (count and status not found)."),
]

# ---------------------------------------------------------------- Repository resilience (RRS)

RRS1 = [
    (M, PT1, f"One NCEI server holds the live daily01 files and their weekly snapshots ([snapshots]({SNAPSHOTS})); NCEI's plan names no second site ([Data Management Plan, 2017]({DMP17})), and no cloud copy exists ([NODD list]({NODD})).", "A", NCEI_R),
    (M, NCEI_A2, f"NCEI's Asheville archive keeps two tape copies, the offsite one \"several kilometers away\" ([CoreTrustSeal]({CTS})); no source says which NCEI site holds USCRN's tapes.", "C", NCEI_R),
    (M, NCEI_A2, "Only Boulder's own archive is documented in \"two separate and geographically dispersed locations\"; after Hurricane Helene, Boulder helped limit data loss. No source says Boulder holds USCRN.", "C", NCEI_R),
    (H, NCEI, f"All NCEI data are moving to Amazon Web Services through spring 2027 ([NCEI]({CLOUD})); no source gives the regions or the number of copies, and OIG found NOAA's cloud platform \"resides in a single region\" ([OIG-24-034-A]({OIG24})).", "C", NCEI_R),
    (M, PT1, f"Copernicus's reprocessed copy sits in Europe, but it starts in 2006, is updated yearly and is not the original format ([CDS]({CDS})).", "C", CDS_X),
    (M, PT4, f"The Data Rescue Project's 52.0 GB snapshot of 24 March 2025 ([DRP]({DRP})) is a volunteer copy.", "C", DRP_X),
]
RRS1_GAPS = [
    ("P", "Where USCRN's tape copies sit, and NCEI's AWS regions and copy count after the move (NCCF design documents)."),
]

RRS2 = [
    (H, NCEI_A2, f"NCEI checks checksums at ingest and \"Any time a file is pulled\", compares only file sizes between its copies \"on a routine basis\" and refreshes tapes \"every few years\", with no checksum schedule ([CoreTrustSeal]({CTS})).", "A", NCEI_R),
]
RRS2_GAPS = [
    ("P", "NCEI's SOP 60-6-015 (not public)."),
    ("U", "A stewardship maturity report for USCRN (only GPCP's and PERSIANN-CDR's were looked for)."),
]

RRS3 = [
    (M, GH_RRS, f"OIG found that NCEI's cloud target platform, at its moderate impact level, does not offer \"testing contingency plans at alternate processing sites\" ([OIG-24-034-A]({OIG24})).", "A", NCEI_R),
    (H, NCEI_A2, f"NCEI has an Information System Contingency Plan with an annual Business Impact Analysis and off-site backups, but it \"cannot be shared outside the US Government\", and no test date or result appears anywhere ([CoreTrustSeal]({CTS})).", "C", NCEI_R),
]
RRS3_GAPS = [
    ("P", "NCEI's contingency-plan test results."),
]

RRS4 = [
    (H, NCEI, f"NCEI's FY2027 request is $52.0M (−$17.8M from a $69.8M base); the House committee gives $60.0M and the Senate committee $70.0M; a continuing resolution runs to 11 December 2026 ([NOAA FY2027 CJ]({CJ27})).", "A", NCEI_R),
    (M, NCEI, f"NCEI's staff fell from 184 FTE (FY2024) to 140 (FY2026 enacted column), with 58 departures by August 2025 ([Asheville Watchdog]({WATCHDOG_AUG})).", "A", NCEI_R),
    (M, NCEI, f"FY2026 was enacted above the request: $69.0M for NCEI ([FY2026 JES]({JES26})).", "F", NCEI_R),
    (M, NCEI, f"S. 3923 passed the Senate on 10 November 2026 and would require NOAA to \"maintain the National Centers for Environmental Information, or a successor entity\" as the long-term archive ([S. 3923]({S3923})).", "C", NCEI_R),
]
RRS4_GAPS = [
    ("P", "NCEI's FY2026 spend plan."),
]

RRS5 = [
    (H, PT4, f"daily01 came through the 1 October – 12 November 2025 shutdown without a gap: update files for every data day and a snapshot every week ([updates/2025]({UPDATES25}); [snapshots]({SNAPSHOTS})).", "F", NCEI_R),
    (M, NCEI_A2, f"After Hurricane Helene (September 2024) NCEI restored ingest by 11 December and \"92% of the ingest backlog was recovered\" ([NCEI FY25 Q1]({SOS25Q1})).", "F", NCEI_R),
    (M, NCEI_A2, "The other 8% of Helene's ingest backlog is not accounted for, and no final loss count was published.", "A", NCEI_R),
    (M, PT4, f"146 of the 159 data-year-2023 files were rewritten on 14 May 2026 with no change-log entry ([DATASET-STATUS.txt]({STATUS})); no loss is shown.", "C", NCEI_R),
    (M, NCEI, f"NCEI's cloud move is still under way, with \"delayed data archival\" in November 2026 and no statement on loss ([NCEI alerts]({ALERTS})).", "C", NCEI_R),
]
RRS5_GAPS = [
    ("S", "Whether USCRN's files were affected by Helene (not checked) and a final Helene loss count."),
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
    # NOAA ARL's ATDD runs the stations (see the docstring); NCEI makes daily01 from their data.
    "producer": "NOAA NCEI",
    # True: NCEI both produces daily01 and is its archive of record (as for GHCN-Daily).
    "producer_is_repository": True,
    "repositories": [
        {"name": NCEI_R, "role": "parent"},
    ],
}

write_categories("uscrn-daily", SUBCATEGORIES, DATASET)
