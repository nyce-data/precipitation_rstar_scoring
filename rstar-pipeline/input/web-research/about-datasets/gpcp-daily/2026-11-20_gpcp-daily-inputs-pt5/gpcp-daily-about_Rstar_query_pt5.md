# About GPCP Daily Part 5 R* Query for Claude

About dataset = GPCP Daily Part 5

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GPCP Daily (Global Precipitation Climatology Project) dataset.

## ChatGPT query

If the GPCP Daily dataset is a derived product, investigate whether any of its contributing datasets, satellites, measurement instruments, platforms, research groups, or supporting institutions have experienced funding cuts, program cancellations, operational disruptions, or termination announcements between 2024 and November 2026. Identify any contributing satellites or instruments that are approaching the end of their operational lifetimes, have already been decommissioned, or are scheduled for replacement or termination. Determine whether the organizations responsible for these contributing data sources are experiencing budget reductions, layoffs, political interference, or other threats to their continued operations. Explain how the loss or disruption of any contributing data source could affect the availability, quality, accuracy, or long-term continuity of the GPCP Daily dataset. Provide supporting evidence from news reports, official agency announcements, research publications, and institutional websites.

## Claude web research skill query

/my:broad-web-research

Using the earlier run's record on what GPCP Daily (Global Precipitation Climatology Project daily precipitation) is made from (in web_search_results/), have any of its input datasets, the satellites, instruments and gauge networks behind them, or the organizations that provide them faced funding cuts, program cancellations, operational disruptions, end-of-life decisions or termination announcements between January 2024 and November 2026, and how could that affect GPCP Daily? Also use the earlier records on PERSIANN-CDR Daily's inputs (which include GPCP), NOAA's and NASA's satellite precipitation capability, NOAA's rain-gauge networks and NOAA NCEI, and spend the time on what they did not cover.

- **Inputs:** confirm from Part 1's record that the dataset is derived, and use its list of inputs and providers. Check these candidates without assuming any is used or affected: SSM/I and SSMIS on DMSP satellites; geostationary infrared records (GridSat-B1, NOAA CPC's merged infrared) and the satellites behind them (GOES, Meteosat, Himawari); TOVS sounders on NOAA polar orbiters and AIRS on Aqua; GPCC gauge analyses; GPCP monthly; IMERG and GPM.
- **For each:** what happened, with dates, including satellites past or near the end of their lives, decommissioned or due for replacement, and whether a successor exists; and how far it is along, rated imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Count budget cuts, layoffs or political interference at a provider only where a source ties them to that input.
- **Effect on GPCP Daily:** stops extension (no replacement for an input the ongoing record needs), degrades (quality, accuracy or coverage falls, or a substitute is needed), or little effect (used only for the historical period, or replaceable). Say whether the producers or archives have announced a substitute or a pause in production.

Use agency, mission and archive documents ahead of news reports, and use news for events. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** for each input of GPCP Daily, and the satellites, instruments, gauge networks and organizations behind it, what happened to it between 2024 and November 2026, rated imminent, emerging or no current threat found; and what that does to the dataset: stops its extension, degrades it, or has little effect. Expect a deep-tier run, because it covers terminations across several members.

**What I changed from your draft:**
- **"Is it derived?" handed to Part 1:** Part 1 already answers that and lists the inputs; this run confirms it from Part 1's record and spends its time on what happened to them.
- **Built on earlier runs:** much of this was covered for PERSIANN-CDR Daily, which uses GPCP as an input: its Part 5 run found the GridSat-B1 calibration change that paused GPCP V3.3, the DMSP data-flow notice of September 30, 2026, and the end of POES. The NOAA and NASA satellite runs and the rain-gauge run cover the satellites and gauges behind the inputs. The question names those records.
- **Effect defined:** your draft asked how losing an input could affect the dataset. An input matters differently depending on its role: losing one the ongoing record needs stops it, while losing one used only for past years may change nothing. The three effect levels make the run say which, and cover your draft's "availability, quality, accuracy or long-term continuity".
- **Organizations' troubles tied to inputs:** your draft asked about budget cuts, layoffs and political interference at the providers. They count where a source ties them to an input, so the answer doesn't fill up with agency-wide stories (Part 4 covers GPCP's own funders).
- **Candidates, not facts:** the list says "without assuming any is used or affected". If Part 1 finds different inputs, the run uses its list.
- **Your date range kept:** January 2024 to November 2026.
- **Limits:** 40 minutes and 320,000 tokens, below the deep tier's full budget, because the earlier records already cover much of the chain. If Part 1 finds a long list of inputs, use 50 minutes and 400,000.

**Order and reuse:** run this after Part 1, in this project, so its list of inputs and providers is in `web_search_results/`. It doesn't need Parts 2–4.
