# About ASOS Part 2: Processing R* Query for Claude

About dataset = ASOS Part 2, processing, quality control, calibration, code and formats

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt2_processing.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_asos-qc-formats-pt2`.

**Subcategories this part answers:** D-4, P-3, DIRS-1, DIRS-4.

**Run order:** after Part 1. It can run before or after Part 3.

## Query to refine

Using Part 1's record (`*_asos-about-pt1`, in web_search_results/), how are ASOS precipitation observations processed
and quality-controlled at each stage: the station's own sensor checks and algorithms, remote monitoring of the network
(such as NWS's ASOS Operations and Monitoring Center), edits by observers and forecast offices, and NCEI's checks on
each archived product (1-minute, 5-minute, hourly in GHCNh, and the daily summaries that enter GHCN-Daily)? Say for
each whether it is automated or manual, how flags work, and who does it. What calibration does it depend on, such as
instrument calibration labs and field technicians (NWS's Sterling Field Support Center and NWS electronics
technicians), traceability to national standards (NIST), WMO Regional Instrument Centres and WMO gauge
intercomparisons, and who runs each? What software, algorithms and computing facilities produce it, from the station
processor to NCEI's product generation, who owns and runs them (NWS, FAA, a vendor or contractor), and does any step
need facilities outside NCEI's and NWS's control? For each piece of code, is it published (where, under what license),
only described in papers or manuals, or unpublished, and is the documentation detailed enough for a newcomer to
reproduce the products? Rate each format and access route FAIR, partly FAIR or non-FAIR, and say whether any needs
proprietary software. Leave cuts and threats to later parts. Tag findings with D-4 "formats obsolete or proprietary",
P-3 "critical knowledge undocumented", DIRS-1 "depends on an external calibration service that could be disrupted" or
DIRS-4 "needs outside processing infrastructure". With a time limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats or news.
- **Calibration examples:** the station-data line from the template, with Sterling named, since ASOS is the
  template's own example.
- **Already known (`2026-11-23_ghcn-daily-infrastructure-pt8`):** Sterling Field Support Center is NWS's 230-acre
  calibration, test and evaluation complex, and its Pressure Standards Laboratory calibrates about 500 barometers a
  year for ASOS and upper air. Electronics technicians do quarterly preventive maintenance, and NWSI 30-2111 says "ASOS
  sensors require minimal calibration". Ask what calibration or field checks the precipitation sensors (HTB, AWPAG)
  get, and who does them; that run didn't find it.
- **Known measurement issues are P-3 and D-4 context.** Tipping-bucket undercatch in snow and wind, AWPAG
  behaviour, and how 1-minute and hourly accumulations differ (IEM's precipitation notes page explains timing) belong
  in the QC answer when documentation describes them.
- **FAIR tests, the same four for every dataset:**
  - findable: a persistent identifier such as a DOI, and metadata in a searchable catalog;
  - accessible: downloadable over a standard open protocol without a login;
  - interoperable: an open, documented format that common tools read, with standard variable names and units;
  - reusable: a stated license and provenance.

  Rate each product with the route it is served by (NCEI directories, GHCNh, AWS buckets, IEM), and name the tests it
  fails. METAR is a coded text format that needs a decoder; say whether open decoders exist.
- **Code, item by item.** Station processor software, NCEI's product code, GHCNh's code, IEM's processing code. Tell
  published code apart from methods only described in manuals.
- **Outside facilities (DIRS-4):** the station processor's vendor, FAA telecommunications, any contractor that runs
  monitoring or processing, and cloud platforms.

### What the answer should give

- The QC steps per stage, one line each, with who does them and how flags work.
- A table of calibration dependencies, with who runs each.
- A table of software, algorithms and facilities: owner, operator, and whether the code is published.
- A FAIR rating for each product and access route.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using Part 1's record (`*_asos-about-pt1`) and 2026-11-23_ghcn-daily-infrastructure-pt8, both in web_search_results/,
how are ASOS precipitation observations processed, quality-controlled and calibrated, what software produces them, and
how open are their formats and access routes?

- **QC by stage:** the station's own sensor checks and algorithms; remote monitoring of the network (such as NWS's ASOS
  Operations and Monitoring Center); edits by observers and forecast offices; and NCEI's checks on each archived product
  (1-minute, 5-minute, hourly in GHCNh, and the daily summaries that enter GHCN-Daily). For each: automated or manual,
  how flags work, and who does it. Include documented measurement issues: tipping-bucket undercatch in snow and wind,
  All Weather Precipitation Accumulation Gauge behaviour, and why 1-minute and hourly accumulations differ.
- **Calibration:** what calibration or field checks the heated tipping bucket and the accumulation gauge get, and who
  does them. pt8 found Sterling Field Support Center calibrates barometers, technicians do quarterly maintenance and
  NWSI 30-2111 says ASOS sensors "require minimal calibration", but nothing on the precipitation sensors. Check these
  without assuming each applies: Sterling, NWS electronics technicians, NIST traceability, WMO Regional Instrument
  Centres and gauge intercomparisons.
- **Software and facilities:** from the station processor to NCEI's product generation, who owns and runs each (NWS,
  FAA, a vendor or contractor), and any step needing facilities outside NCEI's and NWS's control (the processor's
  vendor, FAA telecommunications, contractors, cloud platforms). For each piece of code (station software, NCEI's
  product code, GHCNh's code, IEM's processing): published (where, what licence), only described in manuals or
  papers, or unpublished.
- **Documentation:** whether a newcomer could reproduce the products from it, or whether it only describes them.
- **FAIR:** rate each product with the route that serves it (NCEI directories, GHCNh, AWS buckets, IEM) FAIR, partly
  FAIR or non-FAIR, and name the tests it fails: findable (a persistent identifier such as a DOI, and metadata in a
  searchable catalog); accessible (a standard open protocol, no login); interoperable (an open, documented format common
  tools read, with standard variable names and units); reusable (a stated licence and provenance). Say whether any
  needs proprietary software, and whether open METAR decoders exist.

For each finding, say whether it supports or contradicts D-4 "formats obsolete or proprietary", P-3 "critical
knowledge undocumented", DIRS-1 "depends on an external calibration service that could be disrupted" or DIRS-4 "needs
outside processing infrastructure"; all four are worded as risks, so "supports" means evidence the risk holds. Leave
people, funding and recent developments to later runs. Use NWS directives and manuals, NCEI's documentation and the
network's papers ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** the QC steps per stage, with who does each and how flags work, plus the documented measurement
issues; the calibration dependencies for the precipitation sensors and who runs each; the software, algorithms and
facilities with owner, operator and code status; whether the documentation lets a newcomer reproduce the products; a
FAIR rating per product and route with the failed tests; and each finding tagged D-4, P-3, DIRS-1 or DIRS-4 with a
stance. Expect a standard-tier run.

**What changed and why:**
- **Kept standard tier.** "Cuts and threats" became "recent developments".
- **Named pt8 and its gap.** The Sterling, quarterly-maintenance and "minimal calibration" facts come from
  `2026-11-23_ghcn-daily-infrastructure-pt8`; the question states them in one line and asks only what that run didn't
  find: the precipitation sensors' calibration. The 230-acre and 500-barometer details are in that record.
- **Measurement issues moved into the QC bullet,** as your context note asks, so undercatch and the 1-minute/hourly
  difference are answered where documentation describes them. IEM's precipitation notes page isn't named; the run
  will find it if it is the best source.
- **Code item by item and outside facilities** kept as short candidate lists.
- **FAIR tests written out,** one line each, the same four as in the other R* queries, with each product rated by its
  route, and the METAR decoder question added.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 30 minutes and 240,000 tokens, as in your draft.

**How to reuse:** run after Part 1, in this project; before or after Part 3. Keep the `*_asos-about-pt1` pattern until
Part 1 has run, then put in its folder name.
