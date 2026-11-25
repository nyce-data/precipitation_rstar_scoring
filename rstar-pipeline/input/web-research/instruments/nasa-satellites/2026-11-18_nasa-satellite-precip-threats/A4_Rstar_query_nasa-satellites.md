# A4 R* Query: NASA Satellites

Instrument = NASA Satellites

## Query to refine

[Dependent infrastructure resilience]

Observation network or sensor platform at risk

Upstream sensors, ground stations, buoys, or satellite instruments that feed this dataset are aging out, losing funding, or operating past design life

## ChatGPT query

Is NASA's precipitation-monitoring satellite observation network facing any risk of interruption, reduction, or termination? Cover January 2025 to the present.

**Primary research question:**

Is NASA's precipitation satellite observation capability at risk of being discontinued, reduced, or rendered operationally unavailable due to funding shortfalls, federal budget cuts, political decisions, administrative actions, satellite end-of-life limitations, or extensions beyond originally planned mission lifespans?

**Investigate the following areas:**

1. **Funding and budget risks**
   - Current and proposed NASA budget reductions affecting precipitation-monitoring missions.
   - Congressional appropriations, proposed budget cuts, funding withdrawals, or program cancellations.
   - Changes in funding for satellite operations, data processing, maintenance, and ground infrastructure.
2. **Political and administrative threats**
   - Executive branch proposals, federal agency directives, congressional actions, or policy changes that could affect operations.
   - NASA administrative decisions to terminate, suspend, reduce, or restructure relevant programs.
   - Any announced or proposed changes that could threaten continuity of precipitation data collection.
3. **Satellite operational lifespan**
   - Current operational status and expected end-of-life dates of relevant satellites.
   - Satellites operating beyond their originally designated mission lifespans.
   - Remaining operational capacity, reliability concerns, and replacement schedules.
   - Risks associated with aging spacecraft, instruments, and supporting infrastructure.
4. **Mission continuity and replacement planning**
   - Whether successor satellites or replacement missions are funded, approved, scheduled, or already operational.
   - Potential gaps between existing satellite retirement and replacement launches.
   - Whether alternative NASA, international, or commercial satellite missions can maintain comparable precipitation observations.
5. **Imminent threats and timelines**
   - Identify any confirmed, proposed, or anticipated actions that could affect operations within the next 6, 12, 24, and 36 months.
   - Identify specific budget deadlines, mission termination dates, administrative decisions, or political developments that could trigger operational disruptions.

## Claude web research skill query

/my:broad-web-research

Is NASA's satellite-based precipitation observing capability at risk of being discontinued, reduced or made unavailable? Cover January 2025 to the present. Count a mission only if its instruments feed NASA's precipitation products (such as IMERG), and say which products. Check these as candidates, without assuming any is affected: the GPM Core Observatory (with JAXA); TROPICS; the older Aqua satellite; the planned INCUS mission and the Atmosphere Observing System (AOS); and the processing and distribution behind the data (the Precipitation Processing System and GES DISC at Goddard). Keep NASA-run missions apart from joint ones and from partner satellites in the GPM constellation (JAXA, NOAA, DoD, EUMETSAT).

For each mission, give its launch date, design life and current status; say whether it is past design life, in an extended mission, or showing failures, and what NASA's Senior Review decided. For each successor, say whether it is funded, on schedule, delayed or cancelled, and whether a gap in coverage is projected. Say whether international or commercial satellites could keep comparable precipitation data going, and what they would lack.

Check for four kinds of threat, without assuming any exists:
- **budgetary:** budget requests, appropriations, continuing resolutions;
- **political and administrative:** executive actions, bills, mission terminations, reorganizations;
- **operational:** staffing cuts, contract cancellations, data processing or distribution reduced;
- **end of life:** retirements, failures, fuel or orbit limits, gaps before replacements.

Rate each kind:
- **imminent:** enacted, ordered, scheduled or already happening;
- **emerging:** proposed or reported but not in effect;
- **no current threat found.**

For each threat, say whether it would take effect within 6, 12, 24 or 36 months, and name the deadline or decision that would trigger it. Give dates and figures; where none is published, say so. Use NASA's, Congress's, GAO's and the Inspector General's own documents ahead of news reports, and use news for events. Thorough mode, with a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** a status line for each mission (launch, design life, health, extension decision, which precipitation products it feeds), the state of each successor and any projected gap, a short judgment on whether international or commercial satellites could fill in, and a rating for each of the four kinds of threat with dated evidence and a 6/12/24/36-month window. Expect a deep-tier run, because the topic involves budgets, scheduled retirements and several missions.

**What I changed from your draft:**
- **What counts as a precipitation satellite:** like the NOAA query, I made the test "its instruments feed NASA's precipitation products", so the run doesn't sweep in every NASA Earth science mission.
- **Candidates:** I named the missions (GPM, TROPICS, Aqua, INCUS, AOS) and the data systems as candidates to check, not as facts. The data systems are there because precipitation data can be lost when processing or distribution stops, even while the satellite still flies. Partner satellites are kept apart, since a JAXA, NOAA or DoD decision can cut the IMERG record without any NASA action.
- **Lifespan and replacements:** your sections 3 and 4 became fields for each mission and successor. I added NASA's Senior Review, which is where extended missions are kept or ended, and fuel and orbit limits under end of life.
- **Threat kinds and ratings:** I merged your sections 1, 2 and 5 into the same four kinds of threat and imminent / emerging scale as the NOAA and NCEI queries, so the answers can be compared.
- **Timelines:** I kept your 6, 12, 24 and 36-month windows as a field for each threat, with the deadline or decision that triggers it.
- **Alternatives:** the rest of your section 4 (can international or commercial missions keep the data going?) stays as one sentence, which also asks what they would lack.

**Reuse:** run it in this project after the NOAA satellites query. The two overlap on partner data (GPM, JPSS, DMSP), and this run will read that one's record first. If it runs before the rain gauge query too, the rain gauge run gets both satellite records for its question about filling a gap. To use it for another kind of NASA data (soil moisture, for example), change the test in the third sentence and the candidate list.
