"""Build the GHCN-Daily R* categorization JSON (fourth pass, 2026-11-23).

Hand-sorted evidence from every answer file in rstar-pipeline/input/web-research/ that bears on
GHCN-Daily: the ten about-datasets/ghcn-daily runs (six first runs, four gap runs pt6-pt9),
the two archives/noaa-ncei runs (threats, A2 resilience) and instruments/noaa-rain-gauges.
The third pass added the gap runs and the NCEI A2 run. The fourth pass applied the rules in
rstar-pipeline/input/framework/rstar-categorization-decisions.md: "neutral" became "context", items one step
removed became context, gaps got a status, RRS items got a repository, and each subcategory a score.
Markdown links [label](url) in the text become <a> tags (rstar_common.py does the writing and scoring).

Run:  python3 rstar-pipeline/processing/scripts/categorize/build_ghcn-daily.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rstar_common import H, M, L, write_categories  # noqa: E402

# data-source values: the research run folder names
PT1 = "2026-11-19_ghcn-daily-about-pt1"
PT2 = "2026-11-19_ghcn-daily-about-pt2"
PT3C = "2026-11-19_ghcn-daily-about-pt3_combined"
FUND = "2026-11-21_ghcn-daily-funding-pt3"
PT4 = "2026-11-21_ghcn-daily-threats-news-pt4"
PT5 = "2026-11-21_ghcn-daily-sources-pt5"
NCEI = "2026-11-17_noaa-ncei-threats"
GAUGE = "2026-11-18_noaa-rain-gauge-threats"
# Third pass (2026-11-23): the four gap runs and the NCEI A2 run
PPL = "2026-11-23_ghcn-daily-people-pt6"
REPO = "2026-11-22_ghcn-daily-repository-pt7"
INFRA = "2026-11-23_ghcn-daily-infrastructure-pt8"
RRS = "2026-11-23_ghcn-daily-repository-resilience-pt9"
NCEI_A2 = "2026-11-23_A2_Rstar_query-noaa_ncei"

# Each evidence item is (confidence, source run, text, stance[, repository for RRS]); stance toward the
# subcategory's statement: F = for, A = against, C = context (not directly tied, or doesn't show it true or false).
# Each gap is (status, text): S = searched and none found, P = not public, U = not searched.
# Filing rules: rstar-pipeline/input/framework/rstar-categorization-decisions.md (fourth pass, 2026-11-23).

# Frequently cited pages
ISO = "https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html"
README = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt"
STATUS = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt"
PRODUCT = "https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily"
MENNE12 = "https://www.ncei.noaa.gov/pub/data/ushcn/papers/menne-etal2012.pdf"
DURRE10 = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf"
ORG23 = "https://www.nesdis.noaa.gov/s3dl?path=/s3/2023-02/NCEI_Org_Chart_Feb_2023.pdf"
CJ26 = "https://www.noaa.gov/sites/default/files/2025-06/NOAA%20FY26%20Congressional%20Justification.pdf"
CJ27 = "https://www.noaa.gov/sites/default/files/2026-04/FY2027-NOAA-CJ-Submission.pdf"
JES26 = "https://www.appropriations.senate.gov/imo/media/doc/fy26_cjs_jes.pdf"
HR652 = "https://www.govinfo.gov/content/pkg/CRPT-119hrpt652/html/CRPT-119hrpt652.htm"
SEN27 = "https://www.appropriations.senate.gov/imo/media/doc/cjs_explanatory_stmt.pdf"
WATCHDOG_AUG = "https://avlwatchdog.org/top-climate-scientists-departure-is-sign-of-brain-drain-at-noaa-hub-in-asheville-and-of-deep-cuts-to-research-across-the-country/"
CT_YAHOO = "https://www.yahoo.com/news/articles/asheville-federal-workers-bare-minimum-090818131.html"
OSUPG = "https://www.ncei.noaa.gov/operating-system-upgrade-outage"
GSTATUS = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-status.txt"
SUPER_WB = "https://web.archive.org/web/20251111202310id_/https://www.ncei.noaa.gov/pub/data/ghcn/daily/superghcnd/"
CLOUD = "https://www.ncei.noaa.gov/news/cloud-migration"
CLOUD_FAQ = "https://www.ncei.noaa.gov/news/cloud-migration-FAQ"
ALERTS = "https://www.ncei.noaa.gov/alerts"
AWS = "https://registry.opendata.aws/noaa-ghcn/"
BQ = "https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d"
ASOS_FAQ = "https://www.weather.gov/asos/faq.html"
FR_COOP = "https://public-inspection.federalregister.gov/2026-09099.pdf"
CISESS_AW = "https://api.usaspending.gov/api/v2/awards/ASST_NON_NA24NESX432C0001_1330/"
S3923 = "https://www.govinfo.gov/content/pkg/BILLS-119s3923es/html/BILLS-119s3923es.htm"
SRPT44 = "https://www.govinfo.gov/content/pkg/CRPT-119srpt44/html/CRPT-119srpt44.htm"
BE_SEP25 = "https://berkeleyearth.org/september-2025-temperature-update/"
BE_MAR26 = "https://berkeleyearth.org/march-2026-temperature-update/"
UCS = "https://blog.ucs.org/carlos-martinez/the-trump-administration-threatens-noaa-again-as-extreme-weather-looms/"
SSOD = "https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly/synoptic-summary-of-the-day"
INVENTORY = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt"
ECCC = "https://climate.weather.gc.ca/archived_messages_e.html"
FRANKFORT = "https://www.weather.gov/lmk/FrankfortASOSRetiringasOfficialNWSClimateSite"
HELENE = "https://fedscoop.com/ncei-working-to-recoup-data-after-helene-outage/"
DSMR = "https://repository.library.noaa.gov/view/noaa/34330/noaa_34330_DS1.pdf"
DRP = "https://portal.datarescueproject.org/datasets/global-historical-climatology-network-daily-ghcnd/"
PR292 = "https://github.com/rhiza-research/weather-skills/pull/292"
WMO_WIS2 = "https://community.wmo.int/site/knowledge-hub/programmes-and-initiatives/wmo-information-system-wis/guidance-transition-from-gtswis1-wis2"

# ---------------------------------------------------------------- People risk
P1 = [
    (H, PT1, f"The point of contact is a team, the \"GHCNd Operations Team\" (ncdc.ghcnd@noaa.gov), with Matthew Menne and Imke Durre as principal investigators ([NCEI ISO record C00861]({ISO})). The dataset citation credits 11 people for Version 3 (2012): Menne, Durre, Korzeniewski, McNeill, Thomas, Yin, Anthony, Ray, Vose, Gleason and Houston ([readme]({README})).", "A"),
    (M, FUND, f"Where the team sits is inferred, not stated: NCEI's February 2023 org chart has a Dataset Section and a Products Section under the Climatic Science & Development Branch (Climatic Science & Services Division). Durre heads the Products Section; a 2023 NWS seminar bio places Menne, GHCN's \"technical and scientific lead\", in the Dataset Section ([NCEI org chart, 2023]({ORG23})). No chart newer than 2023 was found.", "C"),
    (H, PT1, "The GHCN-Daily team's size is not published anywhere the research looked. NCEI-wide figures conflict: 175 NOAA staff in Asheville, most at NCEI (BPR, Feb 2025); 177 NCEI staff before the March 2025 departures (Asheville Watchdog); a union local's \"30-person staff\" (Citizen Times, Oct 2025).", "C"),
    (H, PT1, f"The dataset has run a long time with versioned releases: Version 3.00 was released September 24, 2012, and releases have continued to v3.35 (October 1, 2026) ([status.txt]({STATUS})). Its international part descends from the earlier Global Daily Climatology Network.", "C"),
    (H, PT2, f"Written documentation that would support a handover exists: peer-reviewed descriptions of integration ([Menne et al. 2012]({MENNE12})) and of the QC system ([Durre et al. 2010]({DURRE10})); a readme with every flag and the source priority order; a version file; a change log ([status.txt]({STATUS})); `mingle-list.txt`, which ranks each station's sources; and superghcnd diff files that list value-level changes between versions.", "A"),
    (M, PT2, f"Menne et al. (2012) say each version is archived \"along with the latest processing source code\", so the code is kept internally, though it is not published ([Menne et al. 2012]({MENNE12})).", "A"),
    (M, FUND, "People outside the core team also know parts of the system: CISESS staff (NC State's NCICS in Asheville) built a cloud processing prototype for GHCN-D (2019–20) and a GHCN-D graph database (2021–23). The CISESS agreement runs to June 30, 2029.", "A"),
    (M, NCEI, f"The pool of possible successors at NCEI shrank in 2025: NCEI FTE fell from 184 (FY2024) to 140 (FY2026 enacted column), and a former NCEI science chief put 2025 departures at 58, \"about one third of the workforce\" ([Asheville Watchdog, Aug 2025]({WATCHDOG_AUG})). No source ties these departures to the GHCN-Daily team.", "C"),
    (M, PPL, 'A search aimed at one found no succession, workforce or knowledge-transfer plan for GHCN-Daily, NCEI or NESDIS. NOAA\'s workforce-planning order (NAO 202-1103, 2007, review "In Process") lists succession planning only among "possible strategies" ([NAO 202-1103](https://www.noaa.gov/organization/administration/nao-202-1103-noaa-workforce-planning-policy)).', "F"),
    (H, PPL, 'One of the two principal investigators has gone with no published successor: Imke Durre\'s ORCID ends her NCEI role ("Supervisory Physical Scientist / Products Section Chief") on April 30, 2025 ([ORCID](https://pub.orcid.org/v3.0/0000-0001-5689-3846/activities)). Nothing published says why she left or who replaced her.', "F"),
    (M, PPL, 'The only published team statement (NCEI references page, archived 2021) says "The GHCN-Daily team includes Matt Menne, and Bryant Korzeniewski"; current pages give only a group mailbox ([NCEI references page, Wayback 2021](https://www.ncdc.noaa.gov/ghcn-daily-references)). Team size is still not published.', "C"),
    (L, PPL, 'Generic guidance exists but was not read: a NOAA "Workforce Succession Planning Toolkit" (2012) and a Commerce "OHCS Succession Planning Guide" (2022), both seen only in search results. Neither is a plan for GHCN-Daily.', "C"),
    (M, PPL, 'Oversight bodies don\'t cover NCEI\'s workforce: Commerce OIG\'s FY2026 challenges report covers NWS ("approximately 13 percent of its 4,369 employees" left January–April 2025), ships and aircraft ([OIG-26-003](https://www.oig.doc.gov/wp-content/OIGPublications/OIG-26-003_TMC_FY_2026_SECURED-1.pdf)); GAO\'s NOAA workforce reports cover other offices.', "C"),
]
P1_GAPS = [
    ("P", 'Who replaced Durre as Products Section chief (not published; NCEI holds it).'),
    ("U", 'The NOAA and Commerce succession guides, seen only in search results.'),
    ("S", 'An NCEI org chart newer than February 2023.'),
]

P2 = [
    (H, PT1, f"The people named as critical are Matthew Menne and Imke Durre (principal investigators, [ISO record]({ISO})). The 2012 overview paper's authors were Menne, Durre, Vose, Gleason and Houston, then at NCDC in Asheville ([Menne et al. 2012]({MENNE12})).", "C"),
    (M, PT4, "Russ Vose was still quoted as \"NOAA climate monitoring chief\" in January 2026 (AP), and a NOAA media advisory listed him in October 2026 (search result only). No 2025–2026 news names Menne, Durre, Vose, Rennie, Korzeniewski, Yin or Stevens in connection with retirements, departures or cuts.", "C"),
    (M, PT3C, f"Retirement is already thinning NCEI's senior staff: NCEI said in March 2025 that \"the loss of a significant number of staff resulting from the recent release of probationary employees, the Deferred Resignation Program and employees retiring\" ended its monthly climate calls. David Easterling, NCEI's chief of scientific services, left in April 2025, \"one of 58 employees who have retired or resigned\"; the same article quotes a former NCEI science chief who retired early partly because he was on a list of staff \"eligible for reclassification as political employees\" ([Asheville Watchdog, Aug 2025]({WATCHDOG_AUG})).", "C"),
    (M, PT4, f"Nearly 60 NCEI Asheville staff took the deferred-resignation offer by October 2025 ([Citizen Times via Yahoo]({CT_YAHOO})). Whether any were GHCN-Daily staff is not reported.", "C"),
    (L, PPL, 'Estimate, not a personnel record (earliest publication year minus 25–30, FERS rules): Russell Vose, the branch chief above the team (earliest publication 1990, NCEI since 2000, about 61–66), is likely already eligible to retire ([ORCID](https://pub.orcid.org/v3.0/0000-0002-6669-3319/activities)).', "F"),
    (L, PPL, "Estimate: Matthew Menne may become eligible by November 2028. If a 1991 publication is his he is about 60–65 with 20+ years' service; if his first is the 2000 NCDC paper he is about 51–56 and not eligible until about 2030 ([ORCID](https://pub.orcid.org/v3.0/0000-0001-9725-248X/activities)).", "C"),
    (L, PPL, 'Estimate: the others named are mostly not close. Tamara Houston (45–50), Xungang Yin (53–58), Scott Applequist (54–59) and Jared Rennie (40–45) are unlikely to be eligible by November 2028; Byron Gleason (54–59) possibly, but his status after 2019 is unknown; the contractors (Korzeniewski, McNeill, Casey) are not under FERS.', "A"),
    (H, PPL, 'Durre left NCEI on April 30, 2025 after about 24 years ([ORCID](https://pub.orcid.org/v3.0/0000-0001-5689-3846/activities)), so one of the two people most tied to the daily processing is already gone; whether she retired is not published.', "C"),
    (M, PPL, 'On February 28, 2025, 20 NCEI employees left, "about 10 percent of the Center\'s authorized staff", including two "retirement eligible" senior scientists; none is named as GHCN-Daily staff ([Asheville Watchdog, 2025](https://avlwatchdog.org/it-is-a-dark-time-trump-cuts-deeply-into-staff-of-asheville-scientists-who-maintain-worlds-largest-archive-of-environmental-records/)).', "C"),
]
P2_GAPS = [
    ("P", 'Real service dates and ages (OPM and NCEI personnel records); the estimates are proxies.'),
    ("S", 'Current status of Gleason, Houston, Kantor, Thomas, Anthony and Ray.'),
]

P3 = [
    (H, PT2, f"The QC system is documented in detail: about 20 fully automated tests (19 in 2010), each with its thresholds, are described in [Durre et al. 2010]({DURRE10}) and listed on the [NCEI product page]({PRODUCT}); the [readme]({README}) defines each quality flag. Integration (screening, matching, mingling by a fixed source priority) is described in [Menne et al. 2012]({MENNE12}).", "A"),
    (M, PT2, "The processing and QC code is not published. The QC programs are \"written in FORTRAN 95 on a Linux platform\" and users are pointed to a contact. No public code was found for integration, mingling, format checking or file production, in NCEI's GHCN-Daily folders or its GitHub organizations (NCEI-NOAAGov, 11 repositories, none on GHCN; `ncei`, none public). code.noaa.gov could not be checked.", "F"),
    (H, PT2, "NCEI does publish code for related products: GHCN-Monthly v4 source, \"provided for inspection, but without any support\" from NCEI's \"internal Git\", and the PHA homogenization code. So the GHCN-Daily code likely sits in the same internal Git, but that is not confirmed.", "A"),
    (M, PT2, "QC runs \"unsupervised\": manual checking is called \"impractical\", and the tests were \"manually validated\" only to set thresholds. Most QC knowledge is therefore in code and papers, not in daily human judgement.", "A"),
    (M, PT2, "The one human QC channel is undocumented: the \"Datzilla Gatekeeper\" investigates values raised by tickets and sets flag Z, but how Datzilla works (who decides, whether values are corrected) is not public. An NWS directive that mentions it returned HTTP 403.", "F"),
    (H, PT2, "Documentation has small holes: the product page doesn't map each check to its flag letter (several checks' flags are \"not stated\"); `GHCND_sample.csv` returns 404; `superghcnd/readme.txt` is missing; the readme still names the retired ftp.ncdc.noaa.gov.", "F"),
    (H, PT2, "Third-party readers exist (for example rOpenSci rnoaa, MIT, being archived; a Zenodo converter, CC BY 4.0; many GitHub readers). They help users read the files but not reproduce the dataset.", "C"),
    (M, PT5, f"The rules for integrating each new source are not all documented: v3.33 (January 2026) added SSODv2 \"initially … only to provide updates to stations from 2025 onwards\" and promised the full period of record \"several weeks later\"; no later log entry says this was done ([ghcnd-status.txt]({GSTATUS})).", "F"),
    (M, PPL, f'NOAA\'s 2021 stewardship review of GHCN-Daily says "GHCN-D is not currently under Configuration Management" and rates Transparency/Traceability 2.75 ([DSMR-00227]({DSMR})).', "F"),
    (M, PPL, 'A search aimed at it found no processing or QC code on code.noaa.gov or GitHub, and nothing saying NCEI shares it on request.', "F"),
    (L, PPL, 'Unverified lead (search summaries only): 2022 NCEI slides for the WERA1012 meeting list Bryant Korzeniewski, a contractor, as "Datzilla Gatekeeper". Current NCEI metadata reportedly names Menne as principal investigator and the "GHCNd Operations Team" as contact.', "C"),
]
P3_GAPS = [
    ("S", 'Whether NCEI shares the code on request (ask ncdc.ghcnd@noaa.gov).'),
    ("U", 'The 2022 WERA1012 slides naming the Datzilla Gatekeeper (unread).'),
]

P4 = [
    (H, PT1, f"The listed point of contact is a team (\"GHCNd Operations Team\") with two principal investigators, not one person ([ISO record]({ISO})). One of the two, Durre, left NCEI in April 2025 (see the people-pt6 item).", "A"),
    (M, PT2, "QC and the regular build are fully automated, which lowers the chance that one absent person stops production. The one human step, Datzilla ticket review, has a single role title (\"Datzilla Gatekeeper\"); how many people fill it is not known.", "A"),
    (M, PT3C, f"Production kept going without most staff: daily update files were posted every day through the October–November 2025 shutdown ([superghcnd listing, Wayback]({SUPER_WB})), when about 95% of NCEI's Asheville staff were furloughed ([Citizen Times via Yahoo]({CT_YAHOO})).", "A"),
    (M, PT2, "Some QC happens before data reach NCEI, at the source networks: CoCoRaHS headquarters staff and volunteer coordinators review reports daily; COOP summaries (DSI-3210) are quality controlled by NCEI personnel. Production work is therefore spread over several groups.", "A"),
    (M, FUND, "Extra hands sit outside the federal team: CISESS development staff, and NCEI support contracts (science support 1332KP24F0017 and data stewardship 1332KP24F0001, both to February 2028). The contracts don't name GHCN, so their role is unknown.", "A"),
    (L, PT5, "Inference: restoring lost source feeds is slow (Canada's feed took 2.5 years, April 2024 to October 2026; SSODv2's full period of record is still not confirmed), which may point to few people able to integrate new sources. No source says why.", "F"),
    (M, PT4, "No source ties any 2025–2026 layoff, firing, buyout, furlough or reorganization to a GHCN-Daily team member.", "C"),
    (M, PPL, "Matthew Menne is now the one named federal scientist on GHCN-Daily: he was the only technical contact on the 2021 team page, and his 2025–2026 work (SSOD Version 2, ERSSTv6) carries an NCEI affiliation ([OpenAlex](https://api.openalex.org/works?filter=author.id:A5025236587|A5062803068|A5067810956|A5111947040|A5009917272|A5001807221,publication_year:2024-2026&sort=publication_year:desc&per_page=25)). Durre's departure (April 2025) halved the two-PI structure.", "F"),
    (M, PPL, 'The other named hands-on staff are mostly Riverside Technology contractors: Korzeniewski ("Riverside Technology Inc. at NOAA/NCEI"), Nancy Casey (scientific programmer since 2019) and probably Shelley McNeill ([Menne, CPASW 2023](https://www.weather.gov/media/climateservices/CPASW/2023/Tuesday/Menne-GHCNdaily-CPASW2023.pdf); [Casey, ORCID](https://pub.orcid.org/v3.0/0009-0001-7709-889X/employments)). Their continuity depends on the contract.', "F"),
    (M, PPL, f'Routine updates need no person: status.txt says that in a funding lapse "GHCN-Daily will continue to update automatically" ([status.txt]({STATUS})). Integrating new sources, Datzilla tickets and QC changes still rest on Menne and the contractors.', "A"),
    (M, PPL, 'Since 2023 no OpenAlex work names new GHCN-Daily staff. Scott Applequist (NCEI since 2009, lead of the 2024 GHCN-Monthly precipitation v4 paper) is the nearest federal colleague in the same work ([ORCID](https://pub.orcid.org/v3.0/0009-0006-2721-0800/employments)).', "C"),
]
P4_GAPS = [
    ("S", "Whether anyone at NCEI could take over Menne's role; the current status of Korzeniewski and Kantor."),
]

# ---------------------------------------------------------------- Data risk
D1 = [
    (H, PT3C, f"GHCN-Daily has no budget line of its own. It is paid for inside the NESDIS Operations, Research and Facilities subactivity \"National Centers for Environmental Information\"; no budget justification, House or Senate report or CRS report names GHCN ([NOAA FY2027 CJ]({CJ27})).", "C"),
    (H, NCEI, f"FY2026: the President asked for $52.0M for NCEI, $18.0M and 16 positions below FY2024, to \"reduce engagement services, tailored products, and eliminate the Regional Climate Services program\" ([FY2026 CJ]({CJ26})). Congress enacted $69.0M (P.L. 119-74, January 2026; [joint explanatory statement]({JES26})).", "C"),
    (H, PT4, f"FY2027: NOAA again asks for $52.0M, a cut of $17.8M (about 25%) from a $69.8M base, again eliminating Regional Climate Services while it \"will continue the core mission of preserving, hosting, and providing access to its extensive environmental data archives\" ([FY2027 CJ]({CJ27})). The House recommends $60.0M ([H. Rept. 119-652]({HR652})) and the Senate committee $70.0M ([Senate statement]({SEN27})). Nothing is enacted; a continuing resolution runs to December 11, 2026.", "F"),
    (M, PT4, f"No source proposes to end or retire GHCN-Daily. It is not on NESDIS's 2025 Notice of Changes or the Bulletin of the Atomic Scientists' list of retired products. The Senate says NOAA \"decommissioned at least 20 datasets, products and catalogs\" without notice but names none ([Senate statement]({SEN27})).", "A"),
    (H, PT4, f"NCEI's cloud-migration FAQ says \"No datasets will be retired as part of the cloud migration\", while noting that \"several NCEI datasets were retired over the last 18 months\" ([NCEI FAQ]({CLOUD_FAQ})).", "A"),
    (H, PT3C, f"The product is active: v3.32 (March 2025), v3.33 and v3.34 (January 2026) and v3.35 (October 1, 2026) added or restored sources ([status.txt]({STATUS})).", "A"),
    (H, FUND, "Positions on the NCEI line are falling even where dollars hold: enacted positions went from 225 (FY2020) to 185 (FY2026) and FTE from 222 to 140; FY2025 actual was 126 positions.", "F"),
    (M, PT4, f"The CISESS cooperative agreement (some GHCN-Daily development work) runs July 2024 – June 2029, $77.5M obligated, last modified September 30, 2026, with no termination ([USAspending]({CISESS_AW})). The April 2025 budget plan proposed \"terminating funding for NOAA's cooperative institutes\", but the FY2027 cooperative-institute cuts are OAR lines, not NESDIS.", "A"),
    (M, FUND, "A second, smaller route: NOAA's Climate Program Office (Climate Observations and Monitoring, in OAR) called GHCN-D \"The COM funded\" dataset (2019) and \"supported by COM and NCEI\" (2021). No amount or post-2021 evidence was found, so whether it continues is unknown.", "C"),
    (L, PT4, "A FY2025 NOAA spend plan was reported as \"$239 million less overall than the current enacted budget for NOAA's six line offices\" (Bloomberg Law, snippet only; NESDIS's share not seen).", "F"),
    (M, FUND, "Context before 2025: the NCEI line rose from $61.6M (FY2020) to $71.4M (FY2023), then held at $69–70M; the run rated the structure \"narrow but steady\".", "C"),
    (L, REPO, 'No Climate Program Office COM support for GHCN-Daily production was found after 2021: the last statement calling GHCN-D "COM funded" is from 2019 ([CPO, 2019](https://cpo.noaa.gov/National-Centers-for-Environmental-Information-and-CPO-lay-groundwork-for-new-extreme-heat-product/)), and COM\'s FY23 precipitation awards fund a study that uses GHCNd, not its production. This rests on an absence.', "C"),
    (M, RRS, 'FY2026 full-year appropriations (P.L. 119-74, January 2026) funded NOAA above the request, and the September 2026 pocket rescission ($809.5M across 11 accounts) names no NOAA account ([CRS IF13024](https://www.everycrsreport.com/files/2026-03-12_IF13024_eb7ce330a93e719e4ae88b7880d3a76d47b0721b.html); [GAO B-338788](https://www.gao.gov/assets/900/890546.pdf)). No FY2026 spend plan was found.', "A"),
]
D1_GAPS = [
    ("P", "GHCN-Daily's own share of the NCEI line (unpublished)."),
    ("P", "NCEI's FY2026 spend plan."),
    ("S", 'The FY2027 outcome after the December 11, 2026 continuing resolution (not decided yet).'),
]

D2 = [
    (H, PT1, f"NCEI is the holding archive; each daily update gets a version number and is archived at NCEI, and every version is kept \"in perpetuity\" ([Menne et al. 2012]({MENNE12})).", "A"),
    (H, NCEI, f"NCEI is moving all its data from servers in Asheville and Boulder to Amazon Web Services through Spring 2027 ([NCEI cloud migration]({CLOUD})). An NCEI alert for November 16–30, 2026 warns of \"delayed data archival and slower update cycles\" ([NCEI Alerts]({ALERTS})).", "F"),
    (H, PT4, f"During the migration, a user reported that \"Every path under … /pub/data/ghcn/ returns 404\" (November 18, 2026; [GitHub PR]({PR292})); the folder loaded again on November 21, but the version file showed an update about six days old for a daily product.", "F"),
    (H, PT1, f"Copies are served outside NCEI: AWS S3 bucket `noaa-ghcn-pds` (us-east-1, updated daily, [AWS registry]({AWS})) and Google BigQuery `bigquery-public-data.ghcn_d` (daily, [Google Cloud]({BQ})). No Microsoft Planetary Computer copy was found (low confidence: two searches).", "A"),
    (M, PT4, f"The Data Rescue Project archived a copy on March 23, 2025 (141.0 GB) ([Data Rescue Project]({DRP})). It is a static snapshot.", "C"),
    (M, PT1, "Inference: the dataset is produced only at NCEI. The AWS and Google copies are fed from NCEI's daily output, so if NCEI's processing stops, every copy stops updating, though existing data stay readable.", "F"),
    (H, PT3C, f"Hurricane Helene (September 2024) disrupted all of NCEI's ingest streams ([FedScoop, 2024]({HELENE})); GHCN-Daily's update files show a 19-day gap, September 27 – October 16, 2024. Two shorter gaps followed in early 2025 (January 14–18, February 3–9), with no cause given.", "F"),
    (H, NCEI, f"NCEI's August 2025 operating-system upgrade ended ISD, LCDv1 and GSOD and decommissioned the Image and Publications System on August 29, 2025 ([NCEI]({OSUPG})).", "F"),
    (M, NCEI, "GSA listed NCEI's Asheville headquarters building for disposal in March 2025 and then pulled the list; its current status was not found.", "C"),
    (M, REPO, 'NCEI keeps two copies: "The NCEI archive and backup copy contains more than 60 petabytes" ([NCEI About Us](https://www.ncei.noaa.gov/about-us)); in 2020 one copy was on tape in Asheville and a "secure copy" offsite ([NCEI, 2020](https://www.ncei.noaa.gov/news/ncei-archives-cosmic-2-data)). Whether GHCN-Daily itself is held at both Asheville and Boulder is not published.', "A"),
    (M, RRS, "The offsite copy is close by: NCEI's 2016 off-site backup SOP puts the backup library 12.5 miles from the Asheville office ([NCEI SOP 200-01-018](https://web.archive.org/web/20201028083622/https://www1.ncdc.noaa.gov/pub/data/paleo/data_management/20160928-MSC_SOP_AppendixM-NCDC200-01-018_IT_Off-site_Backup_Procedures.pdf)), so one regional disaster such as Helene could reach both.", "F"),
    (H, REPO, 'The target cloud platform has known weaknesses: OIG-24-034-A (August 2024) found the NESDIS Common Cloud Framework "hosted in one region of the country" though its maximum tolerable downtime is "only a few hours", and testers could "gain full administrative control of the system using only basic cyberattacks" ([OIG-24-034-A](https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf)). Oversight.gov now lists the recommendations, including the single-region one, as "Closed", with no date or action stated ([Oversight.gov](https://www.oversight.gov/reports/audit/lack-program-management-controls-and-attention-it-security-threatens-success-noaas-10)).', "F"),
    (M, REPO, 'Contractors run the move: AWS holds delivery order 1305M426F0030, "IT Modernization Support for NESDIS and NOAA NCEI" (April 2026 – February 2027, ceiling $7.3M), and Alpha Omega Integration a sole-source bridge to run and migrate the NCEI Archive LAN ([HigherGov](https://www.highergov.com/contract/47QTCA19D000C-1305M426F0030/)).', "F"),
    (M, NCEI_A2, 'No source gives the AWS regions, storage class or number of copies after the move, or says whether the tapes are kept. A 2022 Science Advisory Board working group asked whether NOAA would keep "an on-premises disaster recovery copy of data just in case"; NOAA\'s 2024 response doesn\'t answer ([SAB DAARWG report](https://repository.library.noaa.gov/view/noaa/61393/noaa_61393_DS1.pdf)).', "C"),
]
D2_GAPS = [
    ("S", "Where GHCN-Daily's copies sit after the AWS move, in which regions, and whether the tapes are kept (NCCF design documents)."),
    ("S", "How OIG's single-region recommendation was closed."),
]

D3 = [
    (H, PT2, "Users reach the data through six routes: NCEI HTTPS folders (/pub/data/ghcn/daily/ and /data/…-daily/), the NCEI Access Data Service, CDO web services v2 (token required; 5 requests a second, 10,000 a day), CDO search and order (delivered by email), AWS S3, and Google BigQuery (Google Cloud account; free up to 1 TB a month).", "A"),
    (M, PT3C, "Inference: NCEI's access services are paid from the same NCEI line as production, so the FY2026 and FY2027 proposed cuts apply to them too. The FY2027 request's cut falls mostly on contracted services (advisory services −$11.04M, non-federal services −$6.77M).", "F"),
    (H, PT4, f"Access is interrupted now: NCEI's cloud move (November 16–30, 2026) brought 404s across /pub/data/ghcn/ on November 18 ([GitHub PR]({PR292})), and one user tool switched to the AWS S3 copy as a fallback.", "F"),
    (H, PT3C, f"Past interruptions: a 19-day update gap after Hurricane Helene (2024; [FedScoop]({HELENE})); short gaps in January and February 2025; the August 2025 operating-system upgrade outage ([NCEI]({OSUPG})).", "F"),
    (M, PT4, "During the October–November 2025 shutdown, about 95% of NCEI's Asheville staff were furloughed, and state climatologists lost \"quality-controlled climatological observations from the National Centers for Environmental Information\" (Farms.com). GHCN-Daily's own daily files kept being posted.", "C"),
    (M, PT4, "NCEI's support contracts (data stewardship 1332KP24F0001 and science support 1332KP24F0017) run to February 3, 2028; their potential values were cut slightly by undated changes. They don't name GHCN.", "A"),
    (M, NCEI, "Staff shortages have already taken other NCEI services offline: Sen. Cantwell's office says shortages took data sources offline, including the billion-dollar disaster report, and NCEI ended its monthly climate briefings after February 2025.", "F"),
    (M, REPO, 'The cloud copies rest on contracts with no published end: the NODD agreements became "separate multiyear contracts" in 2019 ([NOAA, 2019](https://www.noaa.gov/media-release/cloud-platforms-unleash-full-potential-of-noaa-s-environmental-data)), called "signed ten year contracts" ([NODD FAQ](https://www.noaa.gov/big-data-project-frequently-asked-questions)). NOAA\'s FY2022 request warned that without NODD funding the providers "are less likely to renew the contracts" ([FY22 CJ](https://www.noaa.gov/sites/default/files/2021-06/NOAA%20FY22%20CJ.pdf)); no enacted NODD amount was found.', "F"),
    (L, RRS, 'Inference from 2023 NODD slides ("Two year base contract with four options of two years each", "Oct 1, 2022 start of year four of ten"): the last option year would end about September 30, 2029 ([NOAA NODD, CPASW 2023](https://www.weather.gov/media/climateservices/CPASW/2023/Thursday/Keown-NODD-CPASW.pdf)). Two 2019 Big Data Project IDIQs on USAspending ended 2025-09-19; they may be different instruments.', "C"),
    (H, REPO, 'The NOAA fee rule effective May 14, 2026 covers only special access (certifications, paper, offline copies, order handling); online GHCN-Daily stays free ([91 FR 19078](https://www.govinfo.gov/content/pkg/FR-2026-04-14/pdf/2026-07250.pdf)).', "A"),
    (H, REPO, 'The routes are still served: on November 22, 2026 the GHCNd product page listed HTTPS and CDO, the CDO home was up, and the CDO v2 API documentation had no retirement notice ([CDO v2](https://www.ncei.noaa.gov/cdo-web/webservices/v2)).', "A"),
    (M, REPO, f'During the October 2025 shutdown NCEI\'s alert said "This site will not be updated"; Wayback copies show the NCEI and CDO home pages still served ([NCEI Alerts]({ALERTS})).', "C"),
]
D3_GAPS = [
    ("S", 'NODD contract records for AWS and Google (FPDS or USAspending, or nodd@noaa.gov).'),
    ("P", 'Staff and funding of CDO and the Access Data Service.'),
]

D4 = [
    (H, PT2, "Formats: fixed-width ASCII `.dly` per-station files, CSV (by_year, by_station), superghcnd full and diff CSV, tar.gz bundles; the Access Data Service offers CSV, SSV, JSON, PDF and NetCDF; AWS offers CSV, CSV.gz and Parquet; Google offers BigQuery tables.", "C"),
    (H, PT2, "All formats are open and documented in NCEI readmes. No proprietary software is needed except on the BigQuery route (a Google Cloud account and SQL).", "A"),
    (H, PT2, f"No route passes all four FAIR tests. Variables use NCEI element codes in scaled units (\"PRCP = Precipitation (tenths of mm)\") rather than CF standard names ([readme]({README})); NCEI's routes state no licence; CDO needs a token or delivers by email.", "F"),
    (M, PT2, f"Licence conflict: AWS and data.gov say CC0-1.0, but NCEI's own ISO record, the DataCite record and the readme state no licence ([AWS registry]({AWS})).", "C"),
    (H, PT2, "Metadata faults: the DataCite record's formats, subjects and rights fields are empty; data.gov shows accessLevel \"non-public\" and a 2012 modified date.", "C"),
    (M, PT2, "The AWS Parquet schema and units are not documented in the bucket or NODD readmes, and a NetCDF request to the Access Data Service came back empty in one test.", "F"),
    (H, PT2, "Many third-party readers exist (rnoaa, MIT, being archived; a Zenodo converter, CC BY 4.0; many GitHub readers), so users don't depend on one tool.", "A"),
    (M, REPO, "All routes use open formats. NOAA's NODD readme says the Parquet files are Hive-partitioned snappy Parquet ([NODD readme](https://github.com/NOAA-Big-Data-Program/nodd-data-docs/blob/main/GHCN-D/Readme.md)) but publishes no column types or units; that the Parquet keeps the raw units (tenths of mm) is likely but not stated.", "A"),
    (M, REPO, 'An Access Data Service JSON test gave values as strings with no units or attributes, and the NetCDF request returned an empty file, so whether it uses CF standard names is untested ([ADS docs](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation)).', "C"),
]
D4_GAPS = [
    ("S", 'Official Parquet and BigQuery column schemas, and the ADS NetCDF attributes (read by hand).'),
]

D5 = [
    (M, PT4, "No source shows GHCN-Daily records being removed, altered or restricted for political reasons, and no news names its team in connection with politics.", "A"),
    (M, PT4, f"A Union of Concerned Scientists blog (May 21, 2026) ties GHCN's \"severe disruptions\" to the administration's actions against NOAA ([UCS]({UCS})). Berkeley Earth reports GHCN-Daily \"broken or in a degraded state\" since late August 2025 ([Berkeley Earth, Mar 2026]({BE_MAR26})). NOAA has given no cause.", "F"),
    (L, PT4, "Interpretation by the research run: the degradation began the day ISD and GSOD reached end of life (August 29, 2025), which points to a product transition rather than political interference. No source says so.", "A"),
    (H, NCEI, f"Congress objected to unannounced removals: the Senate says NOAA \"has decommissioned at least 20 datasets, products and catalogs\" without notice and directs NOAA to restart them ([S. Rept. 119-44]({SRPT44})); in November 2026 it still \"awaits the update\".", "C"),
    (M, NCEI, "NOAA's notice retiring the billion-dollar disaster product cited \"evolving priorities, statutory mandates, and staffing changes\" (E&E News). E&E News's \"Here's where the Trump team is scrubbing climate data\" (August 2025) names NCEI but not GHCN.", "C"),
    (M, NCEI, f"S. 3923 passed the Senate November 10, 2026 and would require NOAA to \"maintain the National Centers for Environmental Information, or a successor entity\" as the long-term archive ([S. 3923]({S3923})). It protects the archive role in law but allows it to move.", "C"),
    (M, NCEI, f"Some NCEI staff were reportedly on a list \"eligible for reclassification as political employees\", who could then be fired without cause ([Asheville Watchdog, Aug 2025]({WATCHDOG_AUG})).", "C"),
    (L, NCEI, "Context: Project 2025 said NOAA \"should be broken up and downsized\" and that its information services \"could be provided commercially\", without naming NCEI. No executive order or Commerce directive aimed at NCEI was found.", "C"),
    (M, NCEI, "Counterevidence: Commerce's Gold Standard Science plan (August 2025) says NOAA \"will leverage\" NCEI for public access.", "C"),
    (M, PT3C, "International politics: the US withdrawal memo of January 7, 2026 lists the IPCC and UNFCCC but not WMO, through which much of GHCN-Daily's foreign data are exchanged.", "A"),
    (M, PT4, f"The Data Rescue Project archived a copy in March 2025 ([Data Rescue Project]({DRP})), a sign that outside groups saw a risk of loss.", "F"),
    (M, REPO, "None of NCEI's 2025–2026 retirements in NESDIS's Notices of Changes is a GHCN-Daily route or tool; they include ISD's FTP/HTTPS service, nClimGrid-Daily's FTP point and Billion Dollar Disasters ([NESDIS Notice of Changes](https://www.nesdis.noaa.gov/about/documents-reports/notice-of-changes)).", "A"),
]
D5_GAPS = [
    ('P', 'The Senate\'s list of "at least 20" decommissioned datasets (NOAA\'s report under S. Rept. 119-44).'),
]

# ---------------------------------------------------------------- Dependent infrastructure resilience
DIRS1 = [
    (H, PT1, f"NCEI does not own or calibrate any instruments; they belong to the contributing networks (COOP, ASOS, SNOTEL, CoCoRaHS and national services), and no NCEI document maps instruments to GHCN-Daily elements ([Menne et al. 2012]({MENNE12})).", "F"),
    (H, PT2, f"NCEI does all GHCN-Daily QC itself, with its own automated tests ([Durre et al. 2010]({DURRE10})). The tests check values against world records, the station's own climatology and neighbouring stations, so they rely on internal comparison rather than an external calibration service.", "C"),
    (L, PT2, f"GHCN-Daily is not homogenized: no adjustments are made for changes in instruments or observing practice ([product page]({PRODUCT})). Inference: any calibration drift or instrument change in a source network passes straight into the dataset.", "F"),
    (M, PT2, "Some source networks QC their own data first: CoCoRaHS uses automated and manual checks; COOP summaries are checked by NCEI personnel. What QC foreign national services do was not found.", "C"),
    (M, GAUGE, "ASOS sensor maintenance is under strain: a March 2025 memo reorganized maintenance into \"pods\" \"to mitigate critical staffing shortages\"; a NOAA staffer told CNN of \"more than 90 vacancies\" among technicians who repair radars and automated surface stations (May 2025). The Commerce OIG counted 564 NWS departures (about 13%) from January to April 2025.", "F"),
    (H, GAUGE, "COOP \"relies on equipment that is no longer supported by manufacturers\", and the budget plans only to \"initiate refresh\" (FY2026 and FY2027 CJs).", "F"),
    (M, GAUGE, "USCRN, a reference-quality network (GHCN-Daily source R, near the top of the source priority), is maintained by NOAA's Air Resources Laboratory (ATDD, Oak Ridge). Both the FY2026 and FY2027 requests would close ARL; Congress rejected this for FY2026.", "F"),
    (M, PT5, "Australia's audit office found the Bureau of Meteorology only \"partly effective in managing assets in its observing network\", with 52–79% of target preventative maintenance done in 2023–24.", "F"),
    (M, INFRA, 'USCRN\'s calibration rests on one small team: "ATDD has a small team of eight technicians and engineers responsible for annual maintenance visits to each station" ([NOAA ARL](https://www.arl.noaa.gov/news-pubs/arl-news-stories/uscrn-at-arl/)); each visit swaps a NIST-traceable thermometer and calibrates the rain gauges. Its parent lab, ARL, is proposed for closure in the FY2026 and FY2027 requests, and the enacted FY2026 statement funds OAR without naming ARL, ATDD or USCRN ([Congressional Record, H255](https://www.govinfo.gov/content/pkg/CREC-2026-01-08/html/CREC-2026-01-08-pt3-PgH255.htm)).', "F"),
    (M, INFRA, '"ASOS sensors require minimal calibration"; electronics technicians do quarterly preventive maintenance ([NWSI 30-2111](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf)), and former Administrator Spinrad said those technicians are "down by at least 16%" ([CBS, 2025](https://www.cbsnews.com/chicago/news/national-weather-service-staffing-shortages-making-forecasts-worse)).', "F"),
    (M, INFRA, 'Abroad, calibration support is thinning: a WMO letter of May 26, 2026 proposes replacing the Regional Instrument Centres, citing "only nine" accredited ([WMO](https://extranet.wmo.int/edistrib_exped/grp_prs/_en/6742243-2026-ESDP-MINT_en.pdf)); WMO\'s October 2026 list marks eight, and WMO abolished 68 posts in 2026.', "C"),
    (H, INFRA, 'ASOS calibration itself is running: NWS\'s Sterling Field Support Center, a "230 acre complex dedicated to the calibration, test, evaluation and support of meteorological systems and sensors", shows no cuts ([NWS](https://www.weather.gov/soic/)); its Pressure Standards Laboratory calibrates about 500 barometers a year.', "A"),
    (M, INFRA, 'NIST had about 150 calibration staff in 2024, down 25–50% over a decade, and calibration income "does not cover maintenance"; no 2025–26 cut to services used for weather instruments was found ([NIST, 2025](https://www.nist.gov/document/measurement-services-update)).', "C"),
    (M, INFRA, 'CoCoRaHS has no formal gauge standard or certifying body; in Colorado tests its gauge caught 101–105% of what the NWS 8-inch gauge caught ([CoCoRaHS](https://media.cocorahs.org/docs/Why%20CoCoRaHS%20requires%20manual%20measurements.pdf)).', "C"),
]
DIRS1_GAPS = [
    ("P", "ARL/ATDD's FY2026 status (NOAA's spend plan)."),
    ("U", 'Calibration practice of foreign national services beyond the WMO RIC picture.'),
]

DIRS2 = [
    (H, PT1, f"GHCN-Daily depends on many station networks. By station entries: CoCoRaHS 40.0%, national met/hydro service numbers 23.1%, COOP 17.4%, unspecified 9.9%, ECA&D 3.8%, WMO 2.3%, WBAN 1.7%, RAWS 1.1%, SNOTEL 0.6% (the run's own count of [ghcnd-stations.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt), closed stations included; ID codes, not value sources).", "C"),
    (H, PT1, "Instruments: COOP uses liquid-in-glass thermometers, MMTS, standard 8-inch, plastic 4-inch and Fisher-Porter gauges; ASOS uses heated tipping-bucket or all-weather accumulation gauges with manual snow; SNOTEL uses snow pillows and storage gauges; CoCoRaHS uses a manual 4-inch gauge. Most US values are read once a day by volunteers.", "C"),
    (H, GAUGE, "NOAA's FY2027 request says \"Over half of NWS major observing systems and capabilities are beyond or reaching end-of-life\". NWS's procurement line for equipment refresh fell from $36.2M (FY2025 actual) to $16.2M (FY2026 enacted), while the Observations operations line stayed about flat ($266.8M, $262.5M, $262.5M requested).", "F"),
    (H, GAUGE, f"COOP (emerging): NWS's May 7, 2026 Federal Register notice proposes \"Right-sizing and optimizing the scope and coverage of the existing ~6,700-site COOP network\" and asks whether mesonet data could replace COOP stations ([Federal Register 2026-09099]({FR_COOP})). A sources-sought notice prices \"up to 3,000\" sites. No decision has been published.", "F"),
    (H, GAUGE, f"ASOS (imminent): FAA funding is \"insufficient to recondition all 570 FAA ASOS locations\", so 206–207 sites move to AWOS-C from 2025 to 2029 ([NWS ASOS FAQ]({ASOS_FAQ})). Frankfort, KY was retired as an official climate site after being offline since June 2025 ([NWS Louisville]({FRANKFORT})). Which of the converted sites are climate sites is not published.", "F"),
    (M, GAUGE, "USCRN (emerging, rejected so far): the FY2026 and FY2027 requests would close the Air Resources Laboratory that maintains it; Congress funded Climate Labs at $104.1M for FY2026. ARL finished a 139-tower transmitter upgrade on April 25, 2026. A 2025 NOAA report assessed downsizing only its soil-moisture sensors, which aren't GHCN-Daily elements.", "F"),
    (M, PT3C, "CoCoRaHS (40% of station entries): no threat found; its current NOAA funding route is not public.", "A"),
    (M, PT3C, "SNOTEL/SCAN (emerging): the NRCS Portland snow office shrank from 12 to 5 staff, \"The NRCS Snow Program is only about 50 people\", and senators reported staff cuts threatening manual snow surveys (December 2025). Active SNOTEL stations rose from 909 to 919.", "C"),
    (M, PT3C, "RAWS: no threat found (\"nearly 2,200\" stations; the latest notice is a 2024 sensor end-of-life).", "A"),
    (M, PT5, "National weather services abroad (emerging): WMO says records \"rest on short-term grants\" and the basic network is \"less than 40 per cent in place\" (2026); WMO cut staff funding and abolished 68 posts; USAID, a funder of African station projects, was dissolved in July 2025. Argentina's SMN dismissed 140 staff on April 15, 2026, with reduced night observations reported.", "F"),
    (M, PT5, "Australia's Bureau of Meteorology: staff steady (1,711 to 1,722), and 3,457 Australian stations have 2026 data; no network cut found. Other services (Met Office, INMET) had no cuts found in a thin search.", "A"),
    (M, INFRA, "COOP stations are inspected and maintained by each office's Observations Program Leader with HMTs, meteorologists or electronics technicians ([NWSI 10-1307](https://www.weather.gov/media/directives/010_pdfs/pd01013007curr.pdf)), the same thinned field staff as ASOS; no lost data was traced to it.", "F"),
    (L, INFRA, 'Argentina\'s SMN was reported in April 2026 to have a list of 240 workers ("un 20% de la planta") to dismiss and plans to close interior stations not yet named ([Bichos de Campo](https://bichosdecampo.com/esta-situacion-golpea-de-lleno-a-la-produccion-advierten-los-trabajadores-del-servicio-meteorologico-nacional-ante-una-nueva-oleada-de-despidos-y-la-posibilidad-de-que-cierren-estaciones/)).', "F"),
    (M, INFRA, 'No national station closures were found for Russia, China, Indonesia or Algeria: BMKG says its 2025 budget rose, and Roshydromet\'s WIS2 node became operational in 2026. Berkeley Earth says such stations "continue to be operated by their local meteorological agencies" ([Berkeley Earth](https://berkeleyearth.org/october-2025-temperature-update/)), so the losses are of the route (DIRS-3), not the networks.', "A"),
    (M, INFRA, 'NRCS Nevada still makes over 90 summer SNOTEL visits ([NRCS](https://www.nrcs.usda.gov/state-offices/nevada/news/nevada-snow-survey-whats-new-for-2026)).', "A"),
    (H, INFRA, f'No published list marks which of the 206–207 ASOS sites moving to AWOS-C are climate sites; the ASOS equipment spreadsheet has no such column ([NWS ASOS FAQ]({ASOS_FAQ})).', "C"),
]
DIRS2_GAPS = [
    ("P", 'Which ASOS sites moving to AWOS-C are climate sites (held by the FAA AWOS program office).'),
    ("S", 'The outcome of the COOP right-sizing (no decision published).'),
    ("S", 'Which SMN Argentina stations close.'),
]

DIRS3 = [
    (H, PT1, f"GHCN-Daily is a compilation: NCEI merges \"more than 25\" (product page) or \"approximately 30\" (ISO record) source datasets from US networks, national weather services, bilateral exchanges and the Global Summary of the Day, combined day by day under a fixed source priority ([readme]({README})).", "C"),
    (H, PT5, f"The synoptic stream was lost: NCEI's ISD and GSOD (GHCN-Daily sources S and W) reached end of life on August 29, 2025 ([NCEI]({OSUPG})). By the run's count from NCEI's inventory, 1,371 of the 1,907 WMO-ID stations reporting in mid-2025 have no 2026 data, mostly in Russia (539), China (92), Indonesia (85), Argentina (47) and Algeria (45) ([inventory]({INVENTORY})).", "F"),
    (M, PT5, f"The replacement is partial: SSODv2, derived from GHCNh, was added in v3.33 (January 5, 2026) for 2025 onward; the full period of record was promised \"several weeks later\" but no entry confirms it ([ghcnd-status.txt]({GSTATUS})). Only 590 WMO-ID stations report in 2026. NCEI warns that SSOD precipitation \"may be underreported\" ([SSOD page]({SSOD})).", "F"),
    (M, PT4, f"Users saw the loss: Berkeley Earth reported GHCN-Daily \"broken or incomplete\" from late August 2025 ([Berkeley Earth, Sept 2025]({BE_SEP25})) and still degraded in April 2026.", "F"),
    (H, PT5, f"Environment Canada's daily feed was \"unexpectedly discontinued on April 28, 2024\" and restored on October 1, 2026 by re-integrating weekly from ECCC's web database; no cause was found. The run also reports earlier Canadian feed failures in 2016 and 2018 ([ghcnd-status.txt]({GSTATUS})).", "F"),
    (H, PT5, f"The Canadian source is itself changing: in March 2026 ECCC moved its URLs to Climate Identifiers, and in August 2026 said the historical data of 174 Government of Alberta climate stations \"will be permanently removed\" ([ECCC]({ECCC})).", "F"),
    (H, PT5, "ECA&D (Europe) was static from September 20, 2024 to January 20, 2025, then resumed monthly updates.", "F"),
    (M, PT5, "Regional Climate Centers (the High Plains RCC supplies airport Daily Summary Messages, v3.32): four of six RCCs went dark April 17, 2025 when funding lapsed, and were restored within days. All six contracts end October 16, 2026; the Southeast RCC announced a $5M five-year NOAA grant (September 2026). The FY2026 and FY2027 requests would eliminate Regional Climate Services; the House FY2027 report gives the RCCs $6.1M.", "F"),
    (M, PT3C, f"WMO exchange (emerging): the GTS \"is planned to be decommissioned by 2033\" as WIS2 takes over ([WMO]({WMO_WIS2})); 59% of WMO's 2026 assessment was unpaid on April 30, 2026; the GCOS secretariat \"will cease to operate after 2027\" without new funding. No source ties these to lost station data yet.", "F"),
    (M, FUND, "Foreign station data come in kind \"through official bi-lateral agreements\" with national services; US inputs are paid for by their own programs (COOP by NWS, CoCoRaHS and SNOTEL by their funders). GHCN-Daily controls none of these budgets.", "F"),
    (H, PT2, "Real-time US streams are replaced by archive-quality sources (such as COOP summaries) 45 to 60 days after month end, so the final record depends on those archive streams continuing.", "C"),
    (M, GAUGE, "The COOP right-sizing plan leans on state and private mesonets, whose NOAA purchase line (National Mesonet Program) faced a proposed cut of about 1,200 platforms in FY2026 that Congress rejected ($30.0M enacted; House FY2027 $40.0M).", "C"),
    (M, INFRA, 'SSODv2\'s full record is still unconfirmed: neither v3.34 nor v3.35 says it was integrated, and Algiers\' file still ends in August 2025 on GSOD data ([AG000060390.dly](https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/AG000060390.dly)). SSOD is "computed from the hourly and synoptic reports provided in GHCNh", so GHCNh is now upstream of GHCN-Daily; no GHCNh funding or staffing is published ([NCEI GHCNh](https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly)).', "F"),
    (M, INFRA, "China's 2026 rules bar giving observation sites or data to foreign organizations without approval ([Global Times](https://www.globaltimes.cn/page/202605/1362135.shtml)).", "F"),
    (H, INFRA, 'The Regional Climate Centers did not lapse: six IDIQs, under the new name "Regional Weather Records Centers", were signed September 11–16, 2026 and run to 2031 ([USAspending](https://www.usaspending.gov/keyword_search/Regional%20Weather%20Records%20Center)). The High Plains RCC supplies GHCN-Daily\'s US airport Daily Summary Messages.', "A"),
    (L, INFRA, f"Alberta: of the 174 Government of Alberta stations ECCC removed from its open data, 120 are in GHCN-Daily's station list but only 38 have data rows, ending in 2017 or 2024, so the removal costs no current data (the run's own count of [ghcnd-inventory.txt]({INVENTORY}); 82 listed stations with no rows are unexplained).", "A"),
]
DIRS3_GAPS = [
    ('S', 'SSODv2 full-record integration (spot-check station files for source flag "2", or ask NCEI).'),
    ("S", "GHCNh's funding and staffing; why Canada's feed stopped in 2024."),
]

DIRS4 = [
    (H, PT1, "GHCN-Daily uses no satellite data and no reanalysis: it is station observations only, so it needs no external satellite or model processing.", "A"),
    (M, PT2, "Production runs at NCEI on NCEI's own software (Fortran 95 QC on Linux, plus unnamed integration and file-writing programs). No outside processing facility is named.", "A"),
    (M, FUND, "CISESS (NC State's NCICS) built a cloud processing prototype for GHCN-D in 2019–20 under task NC-SON-02-NCICS-BB, so a cloud processing path has been developed by a partner, not by NCEI alone.", "F"),
    (M, PT2, "Upstream processing is done outside NCEI by the source networks: CoCoRaHS QC at Colorado State University, High Plains RCC processing of airport summaries, NWS WxCoder3 for COOP reports, KNMI for ECA&D, and WMO's GTS for synoptic reports.", "F"),
    (M, INFRA, "No page says where GHCN-Daily is processed after the AWS move or who runs it; updates continue (version 3.35-upd-2026111517, [ghcnd-version.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt)). No CISESS GHCN-D processing prototype was found in production; CISESS's NODD Cloud Ingest Pipeline handles distribution, not processing.", "F"),
]
DIRS4_GAPS = [
    ("P", 'Where GHCN-Daily processing runs after the AWS move, and who operates it (NCEI holds it).'),
]

DIRS5 = [
    (H, PT1, f"The source priority gives some built-in fallback: values are mingled from several sources per station, and GSOD (now SSODv2) is used only when nothing else exists ([readme]({README})). For many foreign WMO stations, though, the synoptic stream was the only source.", "C"),
    (M, PT5, f"When GSOD ended there was no full substitute: SSODv2 restores only part of the stations, its precipitation \"may be underreported\", and NCEI points users to national met service summaries instead ([SSOD page]({SSOD})).", "F"),
    (H, PT5, "Canada's stations had no replacement feed for 2.5 years (April 2024 – October 2026); the fix was a new route from ECCC's web database, not an alternative supplier.", "F"),
    (H, PT5, f"Airport sites gained a second route: NWS CF6 summaries were added in v3.34 (January 2026). But NWS says an AWOS \"cannot serve as a direct replacement for official NWS climate archiving\" ([NWS Louisville]({FRANKFORT})).", "C"),
    (M, GAUGE, "For COOP, NWS itself names mesonets as possible \"suitable alternatives to federally managed COOP stations\"; no decision has been made.", "A"),
    (L, GAUGE, "Interpretation by the research run: radar and satellite can fill spatial gaps for real-time warnings but cannot replace gauges for snow, terrain or the long, uniform records that climate normals need.", "F"),
    (M, PT1, "No other organization produces GHCN-Daily. The AWS and Google copies are mirrors of NCEI's output, not independent producers.", "F"),
    (M, PT5, "Foreign stations depend on their national services, through WMO exchange, as sole suppliers; WMO says the basic network is \"less than 40 per cent in place\".", "F"),
    (H, INFRA, 'HadISD, another station compilation, stopped with ISD: its final version covers to August 29, 2025, with "no further monthly releases" ([Met Office](https://www.metoffice.gov.uk/hadobs/hadisd/)).', "F"),
    (M, INFRA, 'Berkeley Earth has no station-level daily product (CC BY-NC) ([Berkeley Earth](https://berkeleyearth.org/data/)). None of the alternatives found is a global, quality-controlled, daily-updated archive like GHCN-Daily.', "F"),
    (H, INFRA, 'Partial alternatives are current: ECA&D (Europe, updated to October 31, 2026, mostly non-commercial; [ECA&D](https://www.ecad.eu/)); Copernicus C3S global land in-situ data (86,499 daily stations, CC-BY, updated yearly; [C3S](https://cds.climate.copernicus.eu/datasets/insitu-observations-surface-land)); and WMO WIS2, a second real-time route for synoptic data (116 nodes for 92 Members by June 2026), whose Global Cache keeps data only 24 hours.', "A"),
]
DIRS5_GAPS = [
]

# ---------------------------------------------------------------- Repository resilience
RRS1 = [
    (H, PT1, f"At least three organizations serve the data: NCEI (HTTPS folders, Access Data Service, CDO), AWS S3 `noaa-ghcn-pds` in us-east-1 ([AWS registry]({AWS})), and Google BigQuery `ghcn_d` ([Google Cloud]({BQ})). NCEI's ISO record links both cloud copies; both update daily.", "F", "NCEI, AWS, Google BigQuery"),
    (M, NCEI, f"NCEI has held data on servers in two places, Asheville and Boulder ([NCEI cloud migration]({CLOUD})). Whether GHCN-Daily is copied at both was not found.", "C", "NCEI"),
    (M, PT4, f"A static copy (March 23, 2025, 141.0 GB) is held by the Data Rescue Project ([Data Rescue Project]({DRP})).", "C", "Data Rescue Project (not a repository)"),
    (L, NCEI, "Inference: once NCEI's own data move to AWS (by Spring 2027), NCEI's copy and the AWS Open Data copy will both be on AWS, so the number of independent vendors may shrink. The AWS region of NCEI's new storage is not stated.", "A", "NCEI, AWS"),
    (M, PT4, f"The mirrors work as failover in practice: during NCEI's November 2026 404s, a user tool switched to the AWS S3 copy ([GitHub PR]({PR292})).", "F", "AWS"),
    (L, PT1, "No Microsoft Planetary Computer copy was found (two searches).", "C", "Microsoft Planetary Computer (none found)"),
    (H, RRS, 'The cloud copies are each in one region: S3 stores across at least three Availability Zones in one Region ([AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)); BigQuery uses two zones in one region with "no cross-region replication" ([Google](https://docs.cloud.google.com/bigquery/docs/availability)). Nothing says either is reconciled with NCEI\'s copy.', "A", "AWS, Google BigQuery"),
    (M, RRS, 'NCEI\'s two Asheville copies are not geographically independent: the 2016 off-site backup SOP puts the backup library 12.5 miles from the office, reached by van each business day ([NCEI SOP 200-01-018](https://web.archive.org/web/20201028083622/https://www1.ncdc.noaa.gov/pub/data/paleo/data_management/20160928-MSC_SOP_AppendixM-NCDC200-01-018_IT_Off-site_Backup_Procedures.pdf)); NCEI\'s CoreTrustSeal application says "several kilometers away".', "A", "NCEI"),
    (M, NCEI_A2, 'Boulder\'s own holdings have dispersed copies: "A copy of NCEI-CO archive is stored in two separate and geographically dispersed locations" (NCEI CoreTrustSeal application, R15, [DataverseNL](https://dataverse.nl/api/access/datafile/469675)). No source places a GHCN-Daily copy in Boulder; during Helene NCEI used "facilities and staff in Colorado, Mississippi and Maryland" to restore ingest ([NCEI, 2024](https://www.ncei.noaa.gov/node/6756)).', "C", "NCEI"),
    (M, NCEI_A2, 'Conflict: a 2021 NOAA briefing on the cloud-archive prototype described "cross-region replication" ([NOAA, 2021](https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-51/3.Thursday/2021.04.22_NOAA_Data_Preservation-Stewardship.pdf)), but OIG found the production platform in a single region in 2024. Which describes production now is not published.', "C", "NCEI"),
    (L, RRS, "Unverified lead from the run's checker: GitHub threads say the AWS per-station files have not been written since 2025-02-09, which may reflect a NODD prefix change.", "C", "AWS"),
]
RRS1_GAPS = [
    ("S", 'AWS regions and number of copies after the migration; whether the copies are reconciled.'),
    ("U", 'Object dates in `noaa-ghcn-pds` (per-station files).'),
]

RRS2 = [
    (L, PT2, "The superghcnd diff files list value-level updates, inserts and deletes between versions. They track data changes, not storage integrity.", "C", "NCEI"),
    (M, RRS, f'GHCN-Daily\'s maturity review scores Data Integrity at Level 2 of 5: "a checksum is stored in the archive catalog for each data file", provided on request, and "No known audits performed on the archive at this time" ([DSMR-00227, Table 3]({DSMR})).', "A", "NCEI"),
    (H, NCEI_A2, 'NCEI\'s CoreTrustSeal application (R9): an MD5 checksum is held in the catalog, and "Any time a file is pulled either from primary or offsite, the file\'s checksum is checked"; scripts "on a routine basis" compare file sizes, not checksums, between copies; tapes are refreshed "every few years" ([DataverseNL](https://dataverse.nl/api/access/datafile/469675)). Checksums are checked on use, not on a quarterly schedule.', "A", "NCEI"),
    (H, RRS, 'NCEI holds a current CoreTrustSeal certificate, valid until 2028-01-29 ([CoreTrustSeal certificates](https://amt.coretrustseal.org/certificates/)). No ISO 16363 certification was found.', "C", "NCEI"),
    (M, RRS, 'AWS says S3 "regularly" verifies checksums, frequency not stated ([AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)); Google states no checksum practice for BigQuery and says "There is no service-level agreement (SLA) for the Public Dataset Program" ([Google](https://docs.cloud.google.com/bigquery/public-data)). No document says either copy is verified against NCEI\'s.', "C", "AWS, Google BigQuery"),
    (M, RRS, "NOAA's archive order NAO 212-15 requires secure storage but sets no checksum rule or frequency ([NAO 212-15](https://www.nesdis.noaa.gov/s3/2025-07/NAO-212-15.pdf)).", "C", "NCEI"),
]
RRS2_GAPS = [
    ("P", "NCEI's fixity procedure SOP 60-6-015."),
]

RRS3 = [
    (H, PT3C, f"A real disaster tested NCEI: Hurricane Helene (September 2024) disrupted all its ingest streams at the Asheville headquarters ([FedScoop]({HELENE})). GHCN-Daily updates stopped for 19 days (September 27 – October 16, 2024) and then resumed. This is a record of recovery, not a documented plan.", "C", "NCEI"),
    (M, PT3C, f"During the October–November 2025 shutdown, daily GHCN-Daily files were still posted with about 95% of Asheville staff furloughed ([superghcnd listing, Wayback]({SUPER_WB})).", "C", "NCEI"),
    (H, PT4, f"The November 2026 cloud migration is causing outages and delays now ([NCEI Alerts]({ALERTS})).", "C", "NCEI"),
    (H, RRS, 'OIG-24-034-A found the cloud platform\'s moderate-impact tier doesn\'t offer "testing contingency plans at alternate processing sites" ([OIG-24-034-A](https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf)).', "A", "NCEI"),
    (M, RRS, 'Searches aimed at them found no NCEI disaster-recovery test date or result and no Hurricane Helene after-action report.', "A", "NCEI"),
    (M, RRS, 'Policy requires tests: NESDIS\'s contingency policy says "Testing/exercising must be conducted annually or more frequently", with results recorded on a template, and a tabletop alone isn\'t enough for moderate- or high-impact systems ([NQP-3406](https://www.nesdis.noaa.gov/s3/2021-08/NQP_Series_3406_NESDIS%20Contingency%20Planning%20Policy%20and%20Procedures_March_2015.pdf)). This is a requirement, not evidence a test took place.', "C", "NCEI"),
    (H, NCEI_A2, 'NCEI\'s CoreTrustSeal application (R16) describes an Information System Contingency Plan with an annual Business Impact Analysis and COOP plans; the plan "cannot be shared outside the US Government", and no test date or result is published ([DataverseNL](https://dataverse.nl/api/access/datafile/469675)).', "C", "NCEI"),
    (H, RRS, 'A NESDIS precedent outside the archive: after the October 2014 attack on its satellite product system, NESDIS "was unable to recover the satellite data gathered from October 20–22" ([OIG-16-043-A](https://www.oig.doc.gov/OIGPublications/OIG-16-043-A.pdf)).', "C", "NESDIS (not a GHCN-Daily repository)"),
]
RRS3_GAPS = [
    ("P", 'Contingency plan test results for the NCEI system (FOIA, or ask ncei.info@noaa.gov).'),
]

RRS4 = [
    (H, NCEI, f"NCEI funding: FY2026 request $52.0M, enacted $69.0M ([joint explanatory statement]({JES26})); FY2027 request $52.0M (about −25%), House $60.0M, Senate committee $70.0M, not enacted; a continuing resolution runs to December 11, 2026 ([FY2027 CJ]({CJ27})).", "A", "NCEI"),
    (M, NCEI, "NCEI staffing (in effect): FTE fell from 184 (FY2024) to 140 (FY2026 enacted column); press counts give 20 departures by February 28, 2025 and 58 by August 2025.", "A", "NCEI"),
    (H, NCEI, "NCEI retired or cut back about 27 products from April 2025 (NESDIS 2025 Notice of Changes); the Senate says at least 20 were decommissioned without notice. GHCN-Daily is not among those named.", "A", "NCEI"),
    (M, NCEI, f"S. 3923 (passed the Senate November 10, 2026) would write the archive role into law for \"the National Centers for Environmental Information, or a successor entity\" ([S. 3923]({S3923})).", "C", "NCEI"),
    (L, NCEI, "The FY2027 request cuts NESDIS by 5.4% ($162M), including a shift of satellite operations to contractors; NCEI is not named. A 2026 NOAA reorganization is mentioned but its content was not found. NCEI's director, Deke Arndt, is still listed.", "A", "NCEI"),
    (M, PT4, "NCEI's support contracts run to February 3, 2028; the CISESS agreement runs to June 30, 2029 with no termination.", "F", "NCEI"),
    (M, RRS, "FY2026 is enacted (P.L. 119-74) above the request, and the September 2026 pocket rescission names no NOAA account ([CRS IF13024](https://www.everycrsreport.com/files/2026-03-12_IF13024_eb7ce330a93e719e4ae88b7880d3a76d47b0721b.html)). With FY2027 under a continuing resolution to December 11, 2026, the run rates the threat to NCEI's funding emerging, not imminent.", "F", "NCEI"),
    (M, RRS, 'The cloud copies have no guaranteed term: AWS\'s Open Data Sponsorship "covers the cost of storing and sharing" but states no term or termination ([AWS](https://aws.amazon.com/opendata/open-data-sponsorship-program/)); Google pays for storage with no SLA. NOAA calls NODD "no net cost to the taxpayer" ([NOAA OCIO](https://www.noaa.gov/information-technology/open-data-dissemination)).', "A", "AWS, Google BigQuery"),
]
RRS4_GAPS = [
    ("P", "NCEI's FY2026 spend plan."),
    ("S", 'The FY2027 outcome after the December 11, 2026 continuing resolution.'),
    ("S", 'NODD contract end dates for AWS and Google.'),
]

RRS5 = [
    (H, PT3C, f"NCEI recovered from Hurricane Helene (2024): ingest was disrupted, GHCN-Daily updates stopped for 19 days, and the archive resumed ([FedScoop]({HELENE})). No loss of archived data was reported.", "F", "NCEI"),
    (M, PT3C, "NCEI lost about a third of its workforce in 2025 (58 departures) and went through the October–November 2025 shutdown; GHCN-Daily kept daily updates and added sources (v3.33, v3.34, v3.35).", "F", "NCEI"),
    (H, FUND, "Every fiscal year from FY2020 to FY2024 began on continuing resolutions of 81 to 166 days, and FY2025 ran on a full-year CR, while enacted NCEI dollars stayed at $61.6M–$71.4M.", "F", "NCEI"),
    (H, PT1, "GHCN-Daily has had continuous versioned releases since Version 3.00 (2012), and every version is kept \"in perpetuity\".", "F", "NCEI"),
    (M, PT5, "Lost source feeds have been restored more than once (Canada in 2016, 2018 and 2024–2026; ECA&D in 2025), though restoration took months to 2.5 years.", "C", "NCEI"),
    (M, PT3C, "The 2025 losses were of incoming data (the GSOD stream), not of archived records; NOAA has published no figure for the station loss.", "F", "NCEI"),
    (H, NCEI, "Other NCEI products did not survive the 2025 disruptions intact: about 27 were retired or cut back, and the billion-dollar disaster database stopped updating after 2024 (its 1980–2024 archive is kept).", "A", "NCEI"),
    (M, RRS, 'Hurricane Helene: on October 4, 2024 "All archived data at NCEI is currently inaccessible"; by October 29 all ingest streams ran and NOAA expected "minimal data loss" ([NOAA, 2024](https://www.noaa.gov/news/some-noaa-ncei-websites-systems-down-due-to-helene-devastation-in-asheville-nc)); by December 11 ingest was "fully restored" and "92% of the ingest backlog was recovered", with help from Boulder ([NCEI FY25 Q1](https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf)).', "F", "NCEI"),
    (M, RRS, 'Shutdowns: in October 2013 and December 2018 – January 2019 ncdc.noaa.gov redirected to a lapse notice, and in October 2025 `ghcnd_all.tar.gz` was rebuilt mid-shutdown ([Wayback](https://web.archive.org/web/20251018190509/https://www.ncei.noaa.gov/pub/data/ghcn/daily/)). No data loss from any shutdown was found.', "F", "NCEI"),
    (M, NCEI_A2, 'The other 8% of Helene\'s ingest backlog is not accounted for; NCEI had warned that "some observations might eventually be unrecoverable", and no final loss count was published. Nothing names GHCN-Daily.', "A", "NCEI"),
    (M, NCEI_A2, f'The cloud move is a disruption still under way: NCEI\'s alert (November 16–30, 2026) says to "Expect delayed data archival" and states no loss ([NCEI Alerts]({ALERTS})).', "C", "NCEI"),
]
RRS5_GAPS = [
    ("S", 'A final Helene loss count; whether the 2026 migration loses or delays any GHCN-Daily data.'),
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
    "producer": "NOAA NCEI",
    "producer_is_repository": True,
    "repositories": [
        {"name": "NOAA NCEI archive", "role": "parent"},
        {"name": "AWS noaa-ghcn-pds", "role": "child"},
        {"name": "Google BigQuery ghcn_d", "role": "child"},
    ],
}

write_categories("ghcn-daily", SUBCATEGORIES, DATASET)
