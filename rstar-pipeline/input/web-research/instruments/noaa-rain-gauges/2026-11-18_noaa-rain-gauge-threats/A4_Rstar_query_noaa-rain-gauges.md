# A4 R* Query: NOAA Rain Gauges

Instrument = NOAA Rain Gauges

## Query to refine

[Dependent infrastructure resilience]

Observation network or sensor platform at risk

Upstream sensors, ground stations, buoys, or satellite instruments that feed this dataset are aging out, losing funding, or operating past design life

## ChatGPT query

Determine whether NOAA's network of ground-based precipitation monitoring stations, including rain gauges and associated observational infrastructure, faces a credible risk of reduction, disruption, defunding, or termination. Cover January 2025 to the present.

1. **Funding and Budgetary Risks**
   - Are there proposed or enacted federal budget cuts, funding reductions, appropriations changes, or grant cancellations that could affect NOAA's precipitation monitoring network?
   - Are any specific programs, operational budgets, or funding streams supporting rain gauges and precipitation observation stations at risk?
2. **Political and Administrative Threats**
   - Are there current or proposed political, legislative, executive, or administrative actions that could threaten the network's continued operation?
   - Have NOAA, the Department of Commerce, the federal administration, or Congress proposed reorganizations, staffing reductions, program consolidations, or policy changes that could affect these monitoring systems?
3. **Infrastructure and Operational Vulnerabilities**
   - Are precipitation monitoring stations experiencing equipment failures, deferred maintenance, aging infrastructure, staffing shortages, or insufficient resources?
   - Are there documented plans or indications of station closures, decommissioning, reduced maintenance, or diminished data collection?
4. **Program-Specific Exposure**
   - Identify the NOAA programs and partnerships responsible for ground-based precipitation observations, including:
     - Cooperative Observer Program (COOP).
     - NOAA/National Weather Service precipitation monitoring stations.
     - Community Collaborative Rain, Hail and Snow Network (CoCoRaHS), where relevant.
     - Other federally supported precipitation observation networks and associated data infrastructure.
   - Distinguish NOAA-operated stations from volunteer-operated, state-supported, university-supported, and other partner-operated networks.
5. **Evidence of Imminent or Long-Term Threats**
   - Is there documented evidence of impending station closures, network reductions, funding interruptions, or operational discontinuation?
   - Are threats immediate (within the next 12 months), medium-term (1–3 years), or longer-term?
   - Distinguish confirmed actions from proposed measures, political statements, budget requests, and speculation.
6. **Consequences of Potential Network Disruption**
   - What would be the implications for rainfall measurement, flood forecasting, drought monitoring, water resource management, climate records, agricultural planning, and weather model validation?
   - Are alternative observation systems capable of replacing the data provided by ground-based rain gauges? What limitations would exist?

## Claude web research skill query

/my:broad-web-research

Is NOAA's ground-based precipitation observing network at risk of reduction, disruption, defunding or termination? Cover January 2025 to the present. Check these networks as candidates, and add any other federally supported precipitation network you find: the Cooperative Observer Program (COOP), precipitation gauges at NWS-run stations such as ASOS, the U.S. Climate Reference Network, and CoCoRaHS. For each, say who operates it (NOAA, volunteers, states, universities or other partners) and who funds it. Count actions aimed at NOAA or the NWS as a whole only where a source ties them to precipitation observations.

Check for three kinds of threat, without assuming any exists:
- **budgetary:** budget requests, enacted appropriations, continuing resolutions, grant or contract cancellations;
- **political and administrative:** executive actions, bills, reorganizations, staffing cuts;
- **operational:** equipment failures, deferred maintenance, staff shortages, reduced data collection, stations closed or planned for closure.

Rate each network:
- **imminent:** enacted, ordered or already happening;
- **emerging:** proposed or reported but not in effect;
- **no current threat found.**

Say which kinds of threat drive the rating, and when each would take effect (within 12 months, in 1–3 years, or later). Give dates and figures (dollars, station counts, staff); where none is published, say so. Then say briefly what losing these gauges would mean for flood forecasting, drought monitoring and climate records, and how far radar and satellite estimates could fill the gap. Use NOAA's, Commerce's, Congress's and GAO's own documents ahead of news reports, and use news for events. Thorough mode, with a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** a rating for each precipitation network (imminent, emerging or no current threat found), with the kinds of threat behind it, dated evidence, its status and when it would take effect. Each network also gets a line on who runs and funds it. A short section covers what a loss would mean and how far radar and satellites could make up for it. Expect a deep-tier run, because the topic involves proposed cuts.

**What I changed from your draft:**
- **Rating per network:** your draft asked the same questions about the whole network. I made the answer rate each network on its own, because COOP, CoCoRaHS and the Climate Reference Network are run and funded differently, and a cut to one may not touch the others.
- **Networks as candidates:** I named the four networks as candidates, so the run checks each one without assuming it is threatened, and let it add others it finds.
- **NOAA-wide actions:** I added the rule about actions aimed at NOAA or the NWS as a whole, as in the NCEI query. Without it, every NWS staffing cut could count as a threat to the gauges.
- **Fewer threat kinds:** I merged your sections 2–3 and 5 into three kinds of threat, and turned your 12-month / 1–3 year split into a "when it takes effect" field on each rating.
- **Consequences:** I kept your section 6 but shortened it to one sentence, so it doesn't take time from the main question. If that part comes back thin, run it as a second question that names this run's record.

**Reuse:** the NCEI run already looked at GHCN station counts, which include COOP stations. This run reads that record first, so run it in this project. To use the question for another ground network, change the network names, the operators and the agencies in the first paragraph.

