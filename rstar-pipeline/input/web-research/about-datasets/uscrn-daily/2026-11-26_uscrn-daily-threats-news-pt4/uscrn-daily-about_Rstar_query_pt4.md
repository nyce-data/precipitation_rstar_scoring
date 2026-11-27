# About USCRN Daily Part 4: Threats R* Query for Claude

About dataset = USCRN Daily Part 4, threats to the dataset, its producers and its archive

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt4_threats.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_uscrn-daily-threats-news-pt4`.

**Subcategories this part answers:** D-1, D-3, D-5 and RRS-4, plus staff losses for P-2 and P-4.

**Run order:** last of USCRN Daily's five runs, after Part 3 (and Part 5, so it can cite it).

## Query to refine

Using the earlier runs' records (`*_uscrn-daily-about-pt1`, `*_uscrn-daily-qc-formats-pt2`,
`*_uscrn-daily-people-funding-pt3`, `*_uscrn-daily-inputs-pt5`, `2026-11-18_noaa-rain-gauge-threats`,
`2026-11-23_ghcn-daily-infrastructure-pt8`) and the shared NCEI runs (`2026-11-17_noaa-ncei-threats` and
`2026-11-23_A2_Rstar_query-noaa_ncei`), all in web_search_results/, has funding for USCRN, the Air Resources
Laboratory and its Atmospheric Turbulence and Diffusion Division, and the NCEI systems that process and serve the data
been stable, cut or threatened between January 1, 2025 and November 2026, including proposed closure of the
laboratory, proposed downsizing of the network or its sensors, and budget uncertainty? What layoffs, buyouts, hiring
freezes, reorganizations or contract changes have affected the people who maintain the stations and produce the data?
Has the dataset or its access systems faced outages, access limits, removal, alteration or political pressure? What
news from 2024 to November 2026 names USCRN, ATDD, ARL or its people, and does each item name them directly or only
NOAA or OAR? Rate each development imminent (enacted, ordered or already happening), emerging (proposed or reported but
not in effect) or no current threat found; count agency-wide actions only where a source ties them to USCRN; and say
what each could mean for its updates and availability. Tag findings with D-1 "program defunded or under threat", D-3
"access infrastructure fragile or unfunded", D-5 "subject to political suppression or alteration", RRS-4 "no imminent
threat to the host's funding", P-2 "key personnel retirement-eligible" or P-4 "a single person is a point of
failure". With a time limit of 50 minutes and a token ceiling of 400,000.

### Context for the rewrite

- **This is USCRN Daily's one controversy run,** so it will be deep tier.
- **Build on what is known; don't find it again** (`2026-11-18_noaa-rain-gauge-threats`,
  `2026-11-23_ghcn-daily-infrastructure-pt8`):
  - both the FY2026 and FY2027 requests would close ARL (College Park, Idaho Falls and Oak Ridge) "as well as a
    nation-wide network of soil moisture sensors", as part of ending OAR's Climate Labs (−$102,292K and −$104,964K);
  - Congress funded Climate Labs at $104.1M for FY2026; the joint explanatory statement never names ARL, ATDD or
    USCRN; a House panel told NOAA to "avoid closures, consolidations or eliminations"; Congress rejected the same
    closure for FY2018;
  - NOAA is on a continuing resolution to December 11, 2026; a 2025 NOAA report assessed downsizing the soil-moisture
    sensors (not the gauges).

  Ask for what's new or unresolved: the FY2027 outcome after the CR, NOAA's FY2026 spend plan for ARL, any ATDD staff
  losses, and any station closures.
- **The archive's side (D-3, RRS-4):** NCEI's agency-wide budget and staff are in the A1 run. Ask only for what ties to
  USCRN: whether its directories and portal stayed current through NCEI's 2025 system changes, and any outage.
- **Rating scale, the same in every R* query:** imminent, emerging, or no current threat found.
- **Check news against documents.** Use NOAA's, Congress's and GAO's documents to check what news claims.

### What the answer should give

- A dated table of funding developments, with figures and a rating each.
- Staff changes that touch USCRN, with numbers where published.
- A list of news items: outlet, date, headline, and whether each names USCRN or only the agency.
- What each development could mean for the dataset, and an overall rating.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ (`*_uscrn-daily-about-pt1`, `*_uscrn-daily-qc-formats-pt2`,
`*_uscrn-daily-people-funding-pt3`, `*_uscrn-daily-inputs-pt5`, 2026-11-18_noaa-rain-gauge-threats,
2026-11-23_ghcn-daily-infrastructure-pt8, 2026-11-17_noaa-ncei-threats and 2026-11-23_A2_Rstar_query-noaa_ncei), what
has happened between January 1, 2025 and November 2026 to the funding, staff and access of USCRN Daily (the U.S.
Climate Reference Network's daily01 product), the Air Resources Laboratory (ARL) and its Atmospheric Turbulence and
Diffusion Division (ATDD), and the NCEI systems that process and serve it?

Already known; build on it rather than finding it again: the FY2026 and FY2027 requests would close ARL (College
Park, Idaho Falls and Oak Ridge) and "a nation-wide network of soil moisture sensors" as part of ending OAR's Climate
Labs; Congress funded Climate Labs at $104.1M for FY2026 without naming ARL, ATDD or USCRN, and a House panel told
NOAA to avoid closures; NOAA is on a continuing resolution to December 11, 2026; a 2025 NOAA report assessed
downsizing the soil-moisture sensors, not the gauges.

- **Funding:** the FY2027 outcome after the continuing resolution, NOAA's FY2026 spend plan for ARL, and any proposal
  to downsize the network or its sensors.
- **Staff:** layoffs, buyouts, hiring freezes, reorganizations or contract changes affecting ATDD's field team and the
  people who produce the data, with numbers where published.
- **Access:** whether the daily01 directories and portal stayed current through NCEI's 2025–2026 system changes; any
  outage, access limit, removal, alteration, station closure or political pressure.
- **News, 2024 to November 2026:** items naming USCRN, ATDD, ARL or its people, with outlet, date and headline, and
  whether each names them directly or only NOAA or OAR.

Rate each development imminent (enacted, ordered or already happening), emerging (proposed or reported, not in
effect) or no current threat found, and give an overall rating. Count agency-wide actions only where a source ties
them to USCRN, and say what each could mean for its updates and availability. For each finding, say whether it
supports or contradicts D-1 "program defunded or under threat", D-3 "access infrastructure fragile or unfunded", D-5
"subject to political suppression or alteration", RRS-4 "no imminent threat to the host's funding", P-2 "key personnel
retirement-eligible" or P-4 "a single person is a point of failure". RRS-4 is worded as a strength and the others as
risks, so "supports" means evidence for the statement as worded. Check news claims against NOAA's, Congress's and
GAO's documents. With a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** a dated list of funding developments for USCRN, ARL/ATDD and the NCEI systems that serve it,
with figures and a rating each; staff changes that touch USCRN, with numbers where published; whether the daily01
directories and portal stayed current, and any outage or station closure; news items with outlet, date, headline and
whether each names USCRN or only the agency; what each could mean for the dataset; an overall rating; and each finding
tagged D-1, D-3, D-5, RRS-4, P-2 or P-4 with a stance. Expect a deep-tier run.

**What changed and why:**
- **Known facts stated once, as a starting point.** The ARL closure proposals, the FY2026 Climate Labs figure, the
  House language, the CR date and the soil-moisture report come from `2026-11-18_noaa-rain-gauge-threats` and
  `2026-11-23_ghcn-daily-infrastructure-pt8`; the question states them and asks only for what's new or unresolved.
  I left out the dollar figures for the requested cuts (−$102,292K and −$104,964K) and the FY2018 precedent; they are
  in those records.
- **Archive side narrowed.** NCEI's agency-wide budget and staff are in the A1 run; the access bullet asks only what
  ties to USCRN.
- **Rating scale and stance spelled out.** RRS-4 is the one statement worded as a strength, so the question says what
  "supports" means.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 50 minutes and 400,000 tokens, as in your draft; this is USCRN's one controversy run and will be deep.

**Order and reuse:** run last, after Parts 1, 2, 3 and 5, in this project. The four `*_uscrn-daily-…` patterns stay
until those runs exist; fill in the real folder names then (the run sheet suggests rewriting Parts 4 and 5 again at
that point). If Parts 1–3 and 5 together already cover most of this, 40 minutes and 320,000 tokens may be enough.
