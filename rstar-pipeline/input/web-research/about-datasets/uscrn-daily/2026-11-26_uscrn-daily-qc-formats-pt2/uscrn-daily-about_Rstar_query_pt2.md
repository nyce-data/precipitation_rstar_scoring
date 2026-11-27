# About USCRN Daily Part 2: Processing R* Query for Claude

About dataset = USCRN Daily Part 2, processing, quality control, calibration, code and formats

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt2_processing.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_uscrn-daily-qc-formats-pt2`.

**Subcategories this part answers:** D-4, P-3, DIRS-1, DIRS-4.

**Run order:** after Part 1. It can run before or after Part 3.

## Query to refine

Using Part 1's record (`*_uscrn-daily-about-pt1`, in web_search_results/), how is USCRN Daily processed and
quality-controlled: how the three Geonor sensor readings and the wetness sensor are combined into 5-minute and then
daily precipitation, the automated checks, any manual review, how flags work, and who does each step at NCEI and ATDD?
What calibration does it depend on, such as instrument calibration labs and field technicians of the network (ATDD's
annual maintenance visits), traceability to national standards (NIST), WMO Regional Instrument Centres and WMO gauge
intercomparisons (such as WMO-SPICE), and who runs each? What software, algorithms and computing facilities produce
it, who owns and runs them, and does any step need facilities outside NCEI's and ATDD's control? For each piece of
code, is it published (where, under what license), only described in papers, or unpublished, and is the documentation
detailed enough for a newcomer to reproduce the dataset? Rate each format and access route FAIR, partly FAIR or
non-FAIR, and say whether any needs proprietary software. Leave cuts and threats to later parts. Tag findings with D-4
"formats obsolete or proprietary", P-3 "critical knowledge undocumented", DIRS-1 "depends on an external calibration
service that could be disrupted" or DIRS-4 "needs outside processing infrastructure". With a time limit of 30 minutes
and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats or news.
- **Calibration examples:** the station-data line from the template, with ATDD's visits in place of Sterling.
- **Already known (`2026-11-23_ghcn-daily-infrastructure-pt8`):** "ATDD has a small team of eight technicians and
  engineers responsible for annual maintenance visits to each station"; on each visit they swap one of the three
  platinum resistance thermometers and calibrate the rain gauges; the thermometers are traceable to NIST (Goodge,
  NCDC). That run found nothing on the Geonor gauge's traceability. Ask for it: how the gauge is calibrated, against
  what reference, and by whom.
- **Precipitation algorithm.** Ask for the published method (papers and NCEI documentation) for turning the three
  vibrating-wire depths into precipitation, and how the wetness sensor is used; say whether the code is published.
- **FAIR tests, the same four for every dataset:**
  - findable: a persistent identifier such as a DOI, and metadata in a searchable catalog;
  - accessible: downloadable over a standard open protocol without a login;
  - interoperable: an open, documented format that common tools read, with standard variable names and units;
  - reusable: a stated license and provenance.

  The metadata file says daily01 has no DOI but an NCEI catalog identifier; rate each route (NCEI directory, portal,
  any cloud or Climate Data Store copy) separately, and name the tests it fails.
- **Documentation for a newcomer (P-3):** the daily01 README, station siting and functional-requirements documents,
  maintenance manuals, and processing descriptions; say whether they cover running the processing or only describe it.
- **Outside facilities (DIRS-4):** NESDIS's satellite data collection system if the stations transmit that way,
  NCEI's computing, and any contractor.

### What the answer should give

- The QC and processing steps, one line each, with who does them and how flags work.
- A table of calibration dependencies, with who runs each.
- A table of software, algorithms and facilities: owner, operator, and whether the code is published.
- A FAIR rating for each format and access route.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using Part 1's record (`*_uscrn-daily-about-pt1`) and 2026-11-23_ghcn-daily-infrastructure-pt8, both in
web_search_results/, how is USCRN Daily (the U.S. Climate Reference Network's daily01 product) processed,
quality-controlled and calibrated, what software produces it, and how open are its formats and access routes?

- **Processing and QC:** the published method (papers and NCEI documentation) for combining the weighing gauge's three
  vibrating-wire depths and the wetness sensor into 5-minute and then daily precipitation; the automated checks, any
  manual review, how flags work, and who does each step at NCEI and ATDD.
- **Calibration:** how the weighing gauge is calibrated, against what reference and by whom. pt8 found that ATDD's
  eight-person team calibrates the gauges on annual visits and that the thermometers are NIST-traceable, but nothing
  on the gauge's traceability. Check these without assuming each applies: NIST, WMO Regional Instrument Centres,
  WMO-SPICE and other gauge intercomparisons, and the gauge maker.
- **Software and facilities:** the software, algorithms and computing that produce it, who owns and runs each, and any
  step needing facilities outside NCEI's and ATDD's control (such as NESDIS's satellite data collection system or a
  contractor). For each piece of code: published (where, under what licence), only described in papers, or
  unpublished.
- **Documentation:** whether the daily01 README, siting and functional-requirements documents, maintenance manuals and
  processing descriptions would let a newcomer run the processing, or only describe it.
- **FAIR:** rate each format and access route separately (NCEI directory, portal, any cloud or Climate Data Store copy)
  FAIR, partly FAIR or non-FAIR, and name the tests it fails: findable (a persistent identifier such as a DOI, and
  metadata in a searchable catalog); accessible (a standard open protocol, no login); interoperable (an open,
  documented format common tools read, with standard variable names and units); reusable (a stated licence and
  provenance). Say whether any needs proprietary software.

For each finding, say whether it supports or contradicts D-4 "formats obsolete or proprietary", P-3 "critical
knowledge undocumented", DIRS-1 "depends on an external calibration service that could be disrupted" or DIRS-4 "needs
outside processing infrastructure"; all four are worded as risks, so "supports" means evidence the risk holds. Leave
people, funding and recent developments to later runs. Use NCEI's and ATDD's documents and the network's papers ahead
of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** the processing and QC steps with who does each and how flags work; the calibration dependencies
and who runs each, including whatever is published on the gauge's traceability; the software, algorithms and
facilities with owner, operator and code status; whether the documentation covers running the processing; a FAIR
rating per format and access route with the failed tests; and each finding tagged D-4, P-3, DIRS-1 or DIRS-4 with a
stance. Expect a standard-tier run.

**What changed and why:**
- **Kept standard tier.** "Cuts and threats" became "recent developments".
- **Named pt8.** The draft's "already known" calibration facts come from
  `2026-11-23_ghcn-daily-infrastructure-pt8`; the question names that run and says what it left open (the gauge's
  traceability), so the run starts there.
- **Calibration bodies as candidates.** NIST, WMO RICs, WMO-SPICE and the maker are listed "without assuming each
  applies".
- **FAIR tests written out**, one line each, the same four as in the other R* queries, with each route rated
  separately.
- **Outside facilities.** NESDIS's data collection system and contractors are given as examples for DIRS-4, so the run
  checks how the stations transmit rather than assuming it; Part 1's record should already say.
- **Cut** the answer tables and the note that daily01 has no DOI (Part 1 checks that; the findable test covers it).
- **Limits:** 30 minutes and 240,000 tokens, as in your draft.

**How to reuse:** run after Part 1, in this project; before or after Part 3. Keep the `*_uscrn-daily-about-pt1`
pattern until Part 1 has run, then put in its folder name.
