# A4 R* Query: NOAA Satellites

Instrument = NOAA Satellites

## Query to refine

[Dependent infrastructure resilience]

Observation network or sensor platform at risk

Upstream sensors, ground stations, buoys, or satellite instruments that feed this dataset are aging out, losing funding, or operating past design life

## ChatGPT query

Conduct a comprehensive, evidence-based investigation into whether NOAA's satellite-based precipitation observation network is at risk of interruption, degradation, reduction, or complete discontinuation. Cover January 2025 to the present.

1. **Funding and budgetary risks:** Are proposed federal budget cuts, appropriations reductions, funding expirations, continuing resolutions, or agency funding shortfalls threatening the operation, maintenance, replacement, or development of NOAA's precipitation-monitoring satellites?
2. **Satellite end-of-life risks:** Are any satellites currently providing precipitation-related observations approaching or exceeding their designated operational lifespan? Are there concerns about aging equipment, declining performance, fuel limitations, technical failures, or premature retirement?
3. **Replacement and continuity risks:** Are replacement satellites, successor missions, or planned launches delayed, canceled, unfunded, or otherwise at risk? Could gaps occur between the retirement of existing satellites and the deployment of replacements?
4. **Political and administrative threats:** Are there current or proposed actions by the White House, Congress, NOAA leadership, the Department of Commerce, or other federal agencies that could affect the continuation of these satellite observation programs?
5. **Operational risks:** Are there plans or indications of reduced satellite operations, discontinued data collection, restricted data availability, staffing reductions, contract cancellations, or changes in NOAA's ability to process and distribute precipitation data?
6. **Imminent threats:** Is there evidence of an immediate or near-term threat to the continuity of precipitation observations, including announced termination dates, expiring funding, scheduled satellite retirements, pending budget decisions, or administrative actions?

## Claude web research skill query

/my:broad-web-research

Is NOAA's satellite-based precipitation observing capability at risk of interruption, degradation, reduction or discontinuation? Cover January 2025 to the present. Count a satellite only if its instruments feed NOAA's precipitation estimates or products, and say which products. Check these as candidates, without assuming any is affected: the GOES-R series and its successor GeoXO; the JPSS satellites and Suomi NPP; the legacy POES satellites; NOAA's planned low-orbit missions (QuickSounder, NEON); and partner data NOAA depends on, such as DoD's DMSP microwave data, NASA–JAXA's GPM and EUMETSAT's Metop. Keep NOAA-operated satellites apart from partner ones.

For each satellite, give its launch date, design life and current status, and say whether it is past design life or showing failures. For each successor, say whether it is funded, on schedule, delayed or cancelled, and whether NOAA, GAO or the Inspector General projects a gap in coverage.

Check for four kinds of threat, without assuming any exists:
- **budgetary:** budget requests, appropriations, continuing resolutions;
- **political and administrative:** executive actions, bills, reorganizations;
- **operational:** staffing cuts, contract cancellations, data processing or distribution reduced;
- **end of life:** retirements, failures, gaps before replacements.

Rate each kind:
- **imminent:** enacted, ordered, scheduled or already happening;
- **emerging:** proposed or reported but not in effect;
- **no current threat found.**

Give dates and figures (dollars, dates of retirement or launch); where none is published, say so. Use NOAA's, NESDIS's, Congress's, GAO's and the Inspector General's own documents ahead of news reports, and use news for events. Thorough mode, with a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** a status line for each satellite or series (launch, design life, health, which precipitation products it feeds), the state of each successor mission and any projected coverage gap, and a rating for each of the four kinds of threat with dated evidence. Expect a deep-tier run, because the topic involves budgets and scheduled retirements.

**What I changed from your draft:**
- **What counts as a precipitation satellite:** your draft didn't say, and NOAA has no satellite built only for precipitation. I made the test "its instruments feed NOAA's precipitation estimates or products", so the run doesn't wander into every NOAA satellite.
- **Candidates:** I named the satellite series and the partner data NOAA relies on as candidates to check, not as facts. I kept partner satellites apart, since a DoD or NASA decision can cut NOAA's data without any NOAA action.
- **End of life and replacements:** I turned your sections 2 and 3 into fields for each satellite (design life, status, successor, gap), because those are figures the run can look up.
- **Threat kinds and ratings:** I merged your sections 1, 4, 5 and 6 into four kinds of threat with the same imminent / emerging scale as the NCEI query. "Imminent" here also covers scheduled retirements.

**Reuse:** run it in this project, before or after the rain gauge query. Whichever runs second reads the first one's record. Running this one first gives the rain gauge run better evidence for its question about whether satellites could fill a gap. To use it for another kind of satellite data (sea surface temperature, for example), change the test in the third sentence and the candidate list.

