# GHCN-D gaps Part 8: Dependent infrastructure resilience R* Query for Claude

About dataset = GHCN-D Part 8, gaps in Dependent infrastructure resilience (DIRS-1 to DIRS-5)

Written 2026-11-22 from [ghcn-daily_categorization-gaps.md](../ghcn-daily_categorization-gaps.md). Rewrite this with
`/my:rewrite-research-query` (see [Rstar Precipitation Queries.md](../Rstar%20Precipitation%20Queries.md)), then run the
rewritten query with `/my:broad-web-research` in its own session.

## Query to refine

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily): about-pt1, about-pt2, about-pt3_combined and sources-pt5, plus the NOAA rain-gauge and NOAA NCEI threats runs (all in web_search_results/), which outside facilities, services and data sources does GHCN-Daily depend on that the earlier runs did not check, and are any at risk from 2025 to now? Add to what those runs found rather than repeating it.

- **Calibration (DIRS-1):** who calibrates and maintains the instruments of the networks GHCN-Daily draws on (ASOS through NWS's Sterling Field Support Center, COOP, USCRN through ARL/ATDD, SNOTEL, CoCoRaHS, and national services abroad); which reference standards or intercomparisons they rely on (NIST traceability, WMO Regional Instrument Centres, WMO precipitation intercomparisons); and whether any of those services faced cuts, closures or staff losses.
- **Networks abroad (DIRS-2):** funding or staff cuts and station closures at the national weather services with the largest GHCN-Daily station losses since August 2025 (Russia, China, Indonesia, Argentina, Algeria), and the NWS list of ASOS sites converting to AWOS-C, marking which are climate sites.
- **Supply chain (DIRS-3):** whether SSODv2's full period of record has been integrated into GHCN-Daily; the cause of Environment Canada's 2024 feed stop; whether the 174 Alberta stations ECCC is removing are in GHCN-Daily; the Regional Climate Center contract after October 16, 2026; and GHCNh's own funding and status.
- **Processing (DIRS-4):** where GHCN-Daily processing runs after NCEI's AWS migration and who operates it; whether the CISESS cloud processing prototype went into production.
- **Alternatives (DIRS-5):** datasets or routes that could replace GHCN-Daily or its lost inputs (national archives, ECA&D, Berkeley Earth, HadISD, Copernicus C3S), with their coverage and status.

For each finding, say whether it supports or contradicts these statements: DIRS-1 "depends on an external calibration service that could be disrupted", DIRS-2 "upstream networks are aging out or losing funding", DIRS-3 "upstream data feeds are vulnerable", DIRS-4 "needs outside processing infrastructure", DIRS-5 "no alternative supplier". Rate each: imminent, emerging, or no current threat found. Use operators' own notices and NCEI's files ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **DIRS-1 (calibration) was never searched. Start there.** Ask who calibrates the instruments that feed GHCN-Daily, and
  whether that service is at risk:
  - **ASOS:** NWS's Sterling Field Support Center (Sterling, VA).
  - **COOP:** field calibration by NWS technicians, and standards for the 8-inch gauge.
  - **USCRN:** Air Resources Laboratory (ATDD, Oak Ridge), which both requests proposed to close.
  - **SNOTEL:** NRCS sensor calibration.
  - **CoCoRaHS:** the gauge standard.
  - **Standards and comparisons:** NIST traceability, the WMO Regional Instrument Centres, and the WMO precipitation
    gauge intercomparisons (for example SPICE).
- **DIRS-2 (networks abroad).** Use the countries with the largest station losses after GSOD ended: Russia (539), China
  (92), Indonesia (85), Argentina (47) and Algeria (45). Also find the NWS AWOS-C conversion list, to see which ASOS
  sites are climate sites.
- **DIRS-3 (supply chain): leads the last runs left open.**
  - Whether SSODv2's full period of record was integrated.
  - Why Canada's feed stopped in 2024.
  - Whether ECCC's removal of 174 Alberta stations reaches GHCN-Daily.
  - The Regional Climate Center contract after October 16, 2026 (SAM.gov SSN-NCEI-RCC-2025).
  - GHCNh's own stability, since SSODv2 is now derived from it.
- **DIRS-4 (processing):**
  - where GHCN-Daily processing runs after the AWS migration;
  - whether the CISESS cloud prototype went into production.
- **DIRS-5 (alternatives):** datasets that could stand in for GHCN-Daily:
  - national archives;
  - ECA&D;
  - Berkeley Earth's daily data;
  - HadISD;
  - Copernicus C3S station data;
  - second routes for foreign stations besides the synoptic stream.

### What the answer should give

- The calibration chain for each network.
- Cuts at the foreign services that matter most.
- Answers to the supply-chain questions left open.
- Where processing will run.
- A list of possible substitute datasets.
- A rating and a stance for each finding.

This is the widest query. If it ends by time with leads left, split off calibration (DIRS-1) as its own run at 30
minutes and 240,000 tokens.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
