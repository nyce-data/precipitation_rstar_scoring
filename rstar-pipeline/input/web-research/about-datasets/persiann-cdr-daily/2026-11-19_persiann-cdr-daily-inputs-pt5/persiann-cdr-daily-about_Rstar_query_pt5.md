# About PERSIANN-CDR Daily Part 5 R* Query for Claude

About dataset = PERSIANN-CDR Daily Part 5

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset.

## ChatGPT query

Determine whether PERSIANN-CDR Daily is a derived dataset and identify its underlying data sources, satellite observations, measurement platforms, instruments, algorithms, and contributing organizations. Investigate whether any of these underlying data providers, measurement systems, satellite missions, instruments, or contributing organizations have been mentioned in news coverage or experienced funding cuts, budget reductions, termination announcements, mission cancellations, operational disruptions, or end-of-life decisions between 2024 and November 2026. Assess whether these developments could affect the availability, continuity, quality, or long-term production of PERSIANN-CDR Daily.

## Claude web research skill query

/my:broad-web-research

Using the earlier run's record on what PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record) is made from (in web_search_results/), have any of its input datasets, the satellites, instruments and networks behind them, or the organizations that provide them faced cuts, terminations, mission cancellations, operational disruptions or end-of-life decisions between January 2024 and November 2026, and how could that affect the dataset? Also use the earlier records on NOAA NCEI, NOAA's and NASA's satellite precipitation capability and NOAA's rain-gauge networks, and spend the time on what they did not cover.

- **Inputs:** confirm from Part 1's record that the dataset is derived, and use its list of inputs and providers. Check these candidates without assuming any is used or affected: GridSat-B1 and the geostationary satellites behind it (GOES, Meteosat, Himawari); GPCP monthly and its own inputs, such as GPCC gauges and DMSP SSMIS microwave data; NCEP Stage IV radar.
- **For each:** what happened, with dates, and how far it is along, rated imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found.
- **Effect on PERSIANN-CDR Daily:** stops extension (no replacement for an input the ongoing record needs), degrades (quality or coverage falls, or a substitute is needed), or little effect (used only for the historical period, used only to train the model, or replaceable). Say whether the producer or archive has announced a substitute.

Use agency, mission and archive documents ahead of news reports, and use news for events. With a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** for each input of PERSIANN-CDR Daily, and the satellites, instruments and organizations behind it, what happened to it between 2024 and November 2026, rated imminent, emerging or no current threat found; and what that does to the dataset: stops its extension, degrades it, or has little effect. Expect a deep-tier run, because it covers terminations across several members.

**What I changed from your draft:**
- **"Is it derived?" handed to Part 1:** Part 1 already answers that and lists the inputs; this run confirms it from Part 1's record and spends its time on what happened to them.
- **Built on earlier runs:** the NOAA and NASA satellite runs, the rain-gauge run and the NCEI run already cover much of what sits behind the inputs (geostationary satellites, DMSP, GPM, gauges, NCEI's CDR products). The question names those records.
- **Effect defined:** your draft asked whether developments "could affect" the dataset. An input matters differently depending on its role: losing one the ongoing record needs stops it, while losing one used only to train the model or for past years may change nothing. The three effect levels make the run say which.
- **Inputs of inputs:** GPCP is itself blended, so its own inputs (gauges, microwave satellites) are candidates too. DMSP SSMIS is on the list because the NOAA satellites run found its data feed in question after September 30, 2026.
- **Candidates, not facts:** the list says "without assuming any is used or affected". If Part 1 finds different inputs, the run uses its list.
- **Your date range kept:** January 2024 to November 2026.
- **Limits:** 50 minutes and 400,000 tokens, the deep tier's full budget, because the chain of inputs is long.

**Order and reuse:** run this after Part 1, in this project, so its list of inputs and providers is in `web_search_results/`. It doesn't need Parts 2–4. If the earlier satellite and gauge records already answer most of it, a time limit of 40 minutes and a token ceiling of 320,000 may be enough.
