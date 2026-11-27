# About ASOS Part 4: Threats R* Query for Claude

About dataset = ASOS Part 4, threats to the network, its operators and its archive

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt4_threats.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_asos-threats-news-pt4`.

**Subcategories this part answers:** D-1, D-3, D-5 and RRS-4, plus staff losses for P-2 and P-4.

**Run order:** last of ASOS's five runs, after Part 3 (and Part 5, so it can cite it).

## Query to refine

Using the earlier runs' records (`*_asos-about-pt1`, `*_asos-qc-formats-pt2`, `*_asos-people-funding-pt3`,
`*_asos-inputs-pt5`, `2026-11-18_noaa-rain-gauge-threats`, `2026-11-23_ghcn-daily-infrastructure-pt8`) and the shared
NCEI runs (`2026-11-17_noaa-ncei-threats` and `2026-11-23_A2_Rstar_query-noaa_ncei`), all in web_search_results/, has
funding for ASOS, the NWS, FAA and DoD programs that run it, and the NCEI systems that archive and serve it been stable,
cut or threatened between January 1, 2025 and November 2026, including proposed retirement or replacement of ASOS
sites or products, the FAA's funding for its sites, and budget uncertainty? What layoffs, buyouts, hiring freezes,
reorganizations or contract changes have affected the people who maintain, monitor and archive it? Have ASOS data or
their access systems faced outages, access limits, removal, alteration or political pressure, including product
retirements at NCEI and long station outages? What news from 2024 to November 2026 names ASOS, its program offices or
its people, and does each item name them directly or only NOAA, NWS or FAA? Rate each development imminent (enacted,
ordered or already happening), emerging (proposed or reported but not in effect) or no current threat found; count
agency-wide actions only where a source ties them to ASOS; and say what each could mean for its observations and their
availability. Tag findings with D-1 "program defunded or under threat", D-3 "access infrastructure fragile or
unfunded", D-5 "subject to political suppression or alteration", RRS-4 "no imminent threat to the host's funding", P-2
"key personnel retirement-eligible" or P-4 "a single person is a point of failure". With a time limit of 50 minutes and
a token ceiling of 400,000.

### Context for the rewrite

- **This is ASOS's one controversy run,** so it will be deep tier.
- **Build on what is known; don't find it again.** From `2026-11-18_noaa-rain-gauge-threats` and
  `2026-11-23_ghcn-daily-infrastructure-pt8`:
  - the NWS FAQ says FAA funding is "insufficient to recondition all 570 FAA ASOS locations", so 206–207 FAA sites
    move to AWOS-C from 2025 to 2029; NWS says AWOS "cannot serve as a direct replacement for official NWS climate
    archiving" (Frankfort, KY, offline since June 2025, retired as a climate site);
  - a March 20, 2025 ASOS memo grouped maintenance into "pods" "to mitigate critical staffing shortages"; electronics
    technicians are "down by at least 16%"; the Commerce OIG counted 564 NWS departures, January–April 2025;
  - Observations procurement fell from $36.2M (FY2025) to $16.2M (FY2026 enacted); NOAA is on a continuing
    resolution to December 11, 2026;
  - S. 3923 (Senate-passed November 10, 2026) would require an ASOS assessment and a GAO report.

  Ask for what's new or unresolved: the outcome after the CR, S. 3923 in the House, the AWOS-C site list and which
  are climate stations, the Commerce OIG staffing audit 2025-523 if published, and NWS's rehiring.
- **Part 5 owns the station losses as inputs.** Here, ask about the AWOS-C conversion as a funding and program
  decision (D-1); Part 5 asks how many stations, sensors and records it removes (DIRS-2).
- **The archive's side (D-3, D-5, RRS-4):** NCEI's agency-wide budget and staff are in the A1 run. Ask only for what
  ties to ASOS products: ISD's end of life on August 29, 2025, whether GHCNh, the 1-minute and 5-minute directories
  and the AWS copies are kept current, and any outage that stopped ASOS data flowing to NCEI.
- **Check news against documents.** Use NOAA's, FAA's, Congress's, GAO's and the OIG's documents to check what news
  claims.

### What the answer should give

- A dated table of funding and program developments, with figures and a rating each.
- Staff changes that touch ASOS's maintenance, monitoring and archive, with numbers where published.
- A list of news items: outlet, date, headline, and whether each names ASOS or only the agency.
- What each development could mean for ASOS data, and an overall rating.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ (`*_asos-about-pt1`, `*_asos-qc-formats-pt2`,
`*_asos-people-funding-pt3`, `*_asos-inputs-pt5`, 2026-11-18_noaa-rain-gauge-threats,
2026-11-23_ghcn-daily-infrastructure-pt8, 2026-11-17_noaa-ncei-threats and 2026-11-23_A2_Rstar_query-noaa_ncei), what
has happened between January 1, 2025 and November 2026 to the funding, staff and data access of ASOS (Automated
Surface Observing System), the NWS, FAA and DoD programs that run it, and the NCEI systems that archive and serve it?

Already known; build on it rather than finding it again: FAA funding is "insufficient to recondition all 570 FAA ASOS
locations", so 206–207 FAA sites move to AWOS-C in 2025–2029, and NWS says AWOS can't replace ASOS for official climate
archiving; a March 2025 memo grouped maintenance into "pods" for "critical staffing shortages", electronics technicians
are down at least 16%, and the Commerce OIG counted 564 NWS departures in January–April 2025; Observations procurement
fell from $36.2M (FY2025) to $16.2M (FY2026 enacted); NOAA is on a continuing resolution to December 11, 2026; S. 3923
(Senate-passed November 10, 2026) would require an ASOS assessment and a GAO report.

- **Funding and program:** the outcome after the continuing resolution; S. 3923 in the House; the AWOS-C conversion as
  a funding and program decision, the site list and which are climate stations; any other proposal to retire or
  replace ASOS sites or products.
- **Staff:** layoffs, buyouts, hiring freezes, reorganizations or contract changes affecting the people who maintain,
  monitor and archive it, with numbers where published; NWS's rehiring; Commerce OIG audit 2025-523 if published.
- **Archive and access:** what ties to ASOS products only: whether GHCNh, the 1-minute and 5-minute directories and the
  AWS copies are kept current after ISD's end on August 29, 2025; any outage that stopped ASOS data reaching NCEI; any
  access limit, removal, alteration or political pressure; long station outages.
- **News, 2024 to November 2026:** items naming ASOS, its program offices or its people, with outlet, date and
  headline, and whether each names them directly or only NOAA, NWS or FAA.

Rate each development imminent (enacted, ordered or already happening), emerging (proposed or reported, not in
effect) or no current threat found, and give an overall rating. Count agency-wide actions only where a source ties
them to ASOS, and say what each could mean for its observations and their availability. For each finding, say whether
it supports or contradicts D-1 "program defunded or under threat", D-3 "access infrastructure fragile or unfunded", D-5
"subject to political suppression or alteration", RRS-4 "no imminent threat to the host's funding", P-2 "key personnel
retirement-eligible" or P-4 "a single person is a point of failure". RRS-4 is worded as a strength and the others as
risks, so "supports" means evidence for the statement as worded. Check news claims against NOAA's, FAA's, Congress's,
GAO's and the OIG's documents. With a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** a dated list of funding and program developments for ASOS, its three operating programs and the
NCEI systems that serve it, with figures and a rating each; staff changes touching its maintenance, monitoring and
archive, with numbers where published; whether the archived products and AWS copies stayed current, and any outage;
news items with outlet, date, headline and whether each names ASOS or only the agency; what each could mean for ASOS
data; an overall rating; and each finding tagged D-1, D-3, D-5, RRS-4, P-2 or P-4 with a stance. Expect a deep-tier
run.

**What changed and why:**
- **Known facts stated once, as a starting point.** The AWOS-C conversion, the maintenance pods and technician losses,
  the OIG departures, the procurement drop, the CR date and S. 3923 come from `2026-11-18_noaa-rain-gauge-threats` and
  `2026-11-23_ghcn-daily-infrastructure-pt8`; the question states them and asks only for what's new or unresolved
  (your list of five). The Frankfort example is in those records; I left it out.
- **AWOS-C split with Part 5.** Here it is a funding and program decision (D-1); Part 5 counts the stations and records
  it removes (DIRS-2).
- **Archive side narrowed.** NCEI's agency-wide budget and staff are in the A1 run; the access bullet asks only what
  ties to ASOS products.
- **Rating scale and stance spelled out.** RRS-4 is the one statement worded as a strength, so the question says what
  "supports" means.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 50 minutes and 400,000 tokens, as in your draft; this is ASOS's one controversy run and will be deep.

**Order and reuse:** run last, after Parts 1, 2, 3 and 5, in this project. The four `*_asos-…` patterns stay until
those runs exist; fill in the real folder names then (the run sheet suggests rewriting Parts 4 and 5 again at that
point).
