# About GHCN-D Part 3 R* Query for Claude

About dataset = GHCN-D Part 3

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GHCN-D (Global Historical Climatology Network daily) dataset.

## ChatGPT query

Research how the group or organization responsible for creating, maintaining, and processing the GHCN-D (Global Historical Climatology Network Daily) dataset is funded. Identify its funding sources and determine whether its funding is stable or whether there have been funding cuts, threats of funding reductions, or potential elimination of the program between January 1, 2025, and November 2026. Has the GHCN-D dataset, its responsible organization, or the people/staff involved in its production been mentioned in news coverage between 2024 and 2026, particularly regarding political decisions, government policies, layoffs, or funding changes? If GHCN-D is a derived dataset, also investigate whether any of its underlying data sources, measurement platforms, instruments, or contributing organizations have been in the news or experienced funding cuts, termination, or end-of-life announcements during this period.

## Claude web research skill query

/my:broad-web-research

How is the production of GHCN-Daily (Global Historical Climatology Network–Daily) funded, and are that funding, its team or the data sources it depends on at risk? Use the earlier runs' records in web_search_results/ on GHCN-Daily's sources, on NOAA NCEI and on NOAA's rain-gauge networks, and spend the time on what they did not cover.

- **Funding:** the route that pays for GHCN-Daily (appropriation line, program, grants or partner money), with amounts and fiscal years where published. Say so where it has no budget line of its own.
- **Threats, January 1, 2025 to November 2026:** cuts, proposed cuts, staff losses, or plans to end or retire GHCN-Daily or its products. Count actions aimed at NOAA or NCEI as a whole only where a source ties them to GHCN-Daily.
- **Sources:** for each main network or data stream it draws on, including non-US ones, whether it faced cuts, termination or end-of-life announcements in that period. Check COOP, ASOS, CoCoRaHS, USCRN, WMO exchange feeds and national weather services' station data, without assuming any is affected.
- **News, 2024 to 2026:** coverage naming GHCN-Daily, its maintainers or its staff in connection with political decisions, policies, layoffs or funding changes, with dates.

Rate GHCN-Daily and each source: imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Give dates and figures. Use NOAA's, Congress's and GAO's own documents ahead of news reports, and use news for events. With a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** how GHCN-Daily is paid for, with amounts where published; a rating (imminent, emerging or no current threat found) for GHCN-Daily and for each of its main sources; and dated news items that name the dataset or its staff. Expect a deep-tier run, because the topic involves funding cuts.

**What I changed from your draft:**
- **Built on earlier runs:** the NCEI run already covers NCEI's budget, staff losses and product retirements, and the rain-gauge run covers COOP, ASOS, USCRN and CoCoRaHS. The question names those records, and Part 1's, so this run spends its time on what is specific to GHCN-Daily and on the non-US sources.
- **No budget line of its own:** GHCN-Daily is likely funded inside NCEI's budget rather than as its own line. The run says so instead of offering NCEI's total as GHCN-Daily's figure.
- **Ratings:** I used the same scale and the same rule on NOAA-wide actions as the NCEI and rain-gauge queries, so the three answers can be compared.
- **Sources as candidates:** the networks are listed "without assuming any is affected", so the run checks them rather than looking for a threat to each.
- **Your two date ranges kept:** threats from January 1, 2025, and news from 2024.

**Order and reuse:** run this after Part 1, in this project, so its list of sources is in `web_search_results/`. If the earlier records already answer most of it, a time limit of 30 minutes and a token ceiling of 240,000 may be enough. The candidate list lets the run start even if Part 1 hasn't been run. For another dataset, change the name, the sources and the earlier runs it names.
