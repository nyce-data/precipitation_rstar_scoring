# About CoCoRaHS Part 4: Threats R* Query for Claude

About dataset = CoCoRaHS Part 4, threats to the network, its producers and its data site

Written 2026-11-23 from `templates/template-dataset-about_Rstar_query_pt4_threats.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_cocorahs-threats-news-pt4`.

**Subcategories this part answers:** D-1, D-3, D-5 and RRS-4, plus staff losses for P-2 and P-4.

**Run order:** last of CoCoRaHS's six runs, after Part 3 and the A2 data-site run.

## Query to refine

Using the earlier runs' records (`*_cocorahs-about-pt1`, `*_cocorahs-qc-formats-pt2`, `*_cocorahs-people-funding-pt3`,
the CoCoRaHS data-site A2 run, and `2026-11-18_noaa-rain-gauge-threats`), all in web_search_results/, has funding for
CoCoRaHS, the Colorado Climate Center and the systems that serve its data been stable, cut or threatened between
January 1, 2025 and November 2026, including NOAA, NWS and NSF awards, Colorado State University support, and any
federal grant terminations? What layoffs, hiring freezes, reorganizations or contract changes have affected its paid
staff, and has the NWS partnership or the NWS staff who use and promote it changed? Has the data site faced outages,
access limits, removal of data or political pressure? What news from 2024 to November 2026 names CoCoRaHS, the Colorado
Climate Center or its people, and does each item name them directly or only NOAA or NSF? Rate each development imminent
(enacted, ordered or already happening), emerging (proposed or reported but not in effect) or no current threat found;
count NOAA-wide or NSF-wide actions only where a source ties them to CoCoRaHS; and say what each could mean for its
reports and availability. Tag findings with D-1 "program defunded or under threat", D-3 "access infrastructure
fragile or unfunded", D-5 "subject to political suppression or alteration", RRS-4 "no imminent threat to the data
site's funding", P-2 "key personnel retirement-eligible" or P-4 "a single person is a point of failure". With a time
limit of 50 minutes and a token ceiling of 400,000.

### Context for the rewrite

- **This is CoCoRaHS's one controversy run,** so it will be deep tier.
- **The data site has no A1 threats run.** CoCoRaHS serves its own data, so its funding is the producer's funding,
  covered here. The A2 run covers the site's copies, backups and track record.
- **Build on the rain-gauge run.** It found no threat to CoCoRaHS (moderate confidence, from absence of evidence) and
  no current NOAA funding route. Ask this run to look for what that run couldn't: the current awards, CSU's position,
  and NSF grant terminations in 2025.
- **NWS staffing matters here.** NWS offices recruit observers and use the reports; the 2025 NWS staff losses are in
  the rain-gauge run. Ask only for what ties them to CoCoRaHS.
- **Check news against documents.** Use NOAA's, NSF's, Congress's and CSU's own documents to check what news claims.

### What the answer should give

- A dated table of funding developments, with figures and a rating each.
- Staff changes that touch CoCoRaHS, with numbers where published.
- A list of news items: outlet, date, headline, and whether each names CoCoRaHS or only the agency.
- What each development could mean for the network, and an overall rating.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ (`*_cocorahs-about-pt1`, `*_cocorahs-qc-formats-pt2`,
`*_cocorahs-people-funding-pt3`, the CoCoRaHS data-site A2 run, and 2026-11-18_noaa-rain-gauge-threats), what has
happened between January 1, 2025 and November 2026 to the funding, staff and data access of CoCoRaHS (Community
Collaborative Rain, Hail and Snow Network), the Colorado Climate Center and the systems that serve its data?
CoCoRaHS serves its own data, so the data site's funding is the producer's funding; the A2 run covers the site's
copies, backups and track record.

The rain-gauge run found no threat to CoCoRaHS (from absence of evidence) and no current NOAA funding route; look for
what it couldn't find:

- **Funding:** current NOAA, NWS and NSF awards, Colorado State University's support, and any federal grant
  termination or reinstatement in 2025–2026 that touches CoCoRaHS or the Colorado Climate Center.
- **Staff:** layoffs, hiring freezes, reorganizations or contract changes affecting its paid staff; whether the NWS
  partnership changed, and how 2025 NWS staff losses touch the offices that recruit observers and use the reports,
  only where a source ties them to CoCoRaHS.
- **Access:** outages, access limits, removal of data or political pressure on the data site.
- **News, 2024 to November 2026:** items naming CoCoRaHS, the Colorado Climate Center or its people, with outlet, date
  and headline, and whether each names them directly or only NOAA or NSF.

Rate each development imminent (enacted, ordered or already happening), emerging (proposed or reported, not in
effect) or no current threat found, and give an overall rating. Count NOAA-wide or NSF-wide actions only where a
source ties them to CoCoRaHS, and say what each could mean for its reports and availability. For each finding, say
whether it supports or contradicts D-1 "program defunded or under threat", D-3 "access infrastructure fragile or
unfunded", D-5 "subject to political suppression or alteration", RRS-4 "no imminent threat to the data site's
funding", P-2 "key personnel retirement-eligible" or P-4 "a single person is a point of failure". RRS-4 is worded as a
strength and the others as risks, so "supports" means evidence for the statement as worded. Check news claims against
NOAA's, NSF's, Congress's and CSU's own documents. With a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** a dated list of funding developments for CoCoRaHS and the Colorado Climate Center, with figures
and a rating each; staff changes and NWS partnership changes that touch CoCoRaHS, with numbers where published; any
outage or access limit on the data site; news items with outlet, date, headline and whether each names CoCoRaHS or only
the agency; what each could mean for the network; an overall rating; and each finding tagged D-1, D-3, D-5, RRS-4, P-2
or P-4 with a stance. Expect a deep-tier run.

**What changed and why:**
- **Producer and data site are one.** The question says so, and that the A2 run covers copies and backups, so this run
  doesn't repeat them.
- **Built on the rain-gauge run.** Its "no threat found" and "no current NOAA route" are stated once, and the bullets
  ask for what it couldn't find: current awards, CSU's position and 2025 grant terminations.
- **NWS staffing tied to CoCoRaHS only;** the agency-wide losses are in the rain-gauge record.
- **Rating scale and stance spelled out.** RRS-4 is the one statement worded as a strength, so the question says what
  "supports" means.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 50 minutes and 400,000 tokens, as in your draft; this is CoCoRaHS's one controversy run and will be
  deep. If Part 3 and the A2 run already find stable current funding and nothing in the news, 40 minutes and 320,000
  tokens may be enough.

**Order and reuse:** run last of CoCoRaHS's six runs, after Part 3 and the A2 data-site run, in this project (it
doesn't name Part 5; it will find its record if Part 5 has run). The three `*_cocorahs-…` patterns stay until those
runs exist. Your draft names the A2 run by description, not by a pattern; I kept that, so put in its folder name
once it has run.
