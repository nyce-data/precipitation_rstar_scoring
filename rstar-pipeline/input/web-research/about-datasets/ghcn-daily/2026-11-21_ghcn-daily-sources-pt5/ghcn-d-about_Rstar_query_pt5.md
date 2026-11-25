# About GHCN-D Part 5 R* Query for Claude

About dataset = GHCN-D Part 5

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GHCN-D (Global Historical Climatology Network daily) dataset.

## ChatGPT query

If GHCN-D is a derived dataset, investigate its underlying data sources, measurement platforms, instruments, and contributing organizations. Determine whether any of these sources, platforms, instruments, or organizations have appeared in news coverage between 2024 and 2026 or experienced funding cuts, termination, program elimination, operational disruptions, or end-of-life announcements during this period. Identify the affected entities, explain the nature and timing of the developments, and assess their potential implications for the continued collection, availability, processing, and long-term reliability of the GHCN-D dataset.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily), its sources and its combined funding-and-threats run, on NOAA NCEI and on NOAA's rain-gauge networks (in web_search_results/), which of the networks, data streams, instruments and organizations that GHCN-Daily compiles its station records from faced funding cuts, termination, program elimination, operational disruptions or end-of-life announcements, or appeared in news about them, between January 2024 and November 2026, and what does each mean for GHCN-Daily's continued collection, availability, processing and long-term reliability?

- **Sources:** start from Part 1's list of source networks, and include the routes in, such as NCEI's synoptic streams (GSOD, ISD and their successors) and WMO exchange (GTS/WIS2). Check these as candidates, without assuming any is affected: COOP, ASOS, USCRN, CoCoRaHS, SNOTEL/SCAN, RAWS, the Regional Climate Centers, Environment Canada, ECA&D, Australia's Bureau of Meteorology, and national weather services in Latin America, Africa and Asia.
- **For each affected source:** what happened and when, whether it is enacted, proposed or reversed, and its share of GHCN-Daily's stations where published or countable from NCEI's inventory (say which).
- **Effects:** where GHCN-Daily's own files show the change (station counts, status notes, gaps), and whether NCEI has replaced the stream.

Rate each source and the inputs overall: imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Spend most of the time on non-US sources and on what the earlier runs left open: how many stations were lost after GSOD ended, whether the Regional Climate Center contracts were restored, which ASOS sites moving to AWOS-C are climate sites, and why Canada's feed stopped in 2024. Use operators' own notices and NCEI's files ahead of news, and news for events. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** each source network or data stream behind GHCN-Daily that was cut, ended, disrupted or in the news from 2024 to November 2026, with dates, its share of GHCN-Daily's stations, whether GHCN-Daily's own files show the effect and whether NCEI replaced it, and a rating (imminent, emerging or no current threat found) for each source and for the inputs overall. Expect a deep-tier run, because it covers many sources and their cuts.

**What I changed from your draft:**
- **"If GHCN-D is a derived dataset":** Part 1 found that it is a compilation of 25–30+ networks and national services, so the question states that and starts from Part 1's list instead of asking the run to find out.
- **Built on earlier runs:** the combined run rated 12 sources and streams (GSOD/ISD ended Aug 29, 2025; Argentina's SMN layoffs; COOP, ASOS, USCRN, SNOTEL and WMO emerging), and the rain-gauge run covers COOP, ASOS, USCRN and CoCoRaHS. The combined run calls its search of other national services thin, and its research ended at the token budget. So the question points this run at non-US sources and the four questions the combined run left open.
- **Candidates, not facts:** the networks are listed "without assuming any is affected", so the run checks them rather than hunting for a threat to each. Latin America, Africa and Asia are named as regions so the run looks beyond Canada, Europe and Australia without a long list of countries.
- **"Instruments" kept** in the question (sensor end-of-life notices count, as the combined run found for RAWS), and **"platforms"** folded into networks and streams.
- **"Implications"** made concrete: whether GHCN-Daily's own files show the change and whether NCEI replaced the stream, which is the evidence for continued collection and reliability.
- **Your date range kept:** January 2024 to November 2026.

**Order and reuse:** run this after Part 1 (it has run), in this project; it doesn't depend on Parts 3 or 4, so it can run before, after or between them. The IMERG and GPCP input runs at 40 minutes and 320,000 tokens ended by time with leads left; if you want more room for the non-US sources, use 50 minutes and 400,000. Another option is to split it into two runs, US sources and non-US sources, each at 30 minutes and 240,000; the combined run's notes suggested that split. For another dataset, change the name, the candidate sources and the earlier runs it names.
