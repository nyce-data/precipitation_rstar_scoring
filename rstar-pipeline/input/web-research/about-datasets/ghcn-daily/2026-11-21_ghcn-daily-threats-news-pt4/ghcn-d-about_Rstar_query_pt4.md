# About GHCN-D Part 4 R* Query for Claude

About dataset = GHCN-D Part 4

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GHCN-D (Global Historical Climatology Network daily) dataset.

## ChatGPT query

Determine whether funding for the GHCN-D program or its responsible organization has remained stable or experienced funding cuts, threats of funding reductions, or potential program elimination between January 1, 2025, and November 2026. Investigate whether the GHCN-D dataset, its responsible organization, or the people and staff involved in its production have been mentioned in news coverage between 2024 and 2026, particularly regarding political decisions, government policies, layoffs, staffing changes, or funding reductions. Identify relevant developments and their potential consequences.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily), its funding and its combined funding-and-threats run, and on NOAA NCEI (in web_search_results/), has the funding for GHCN-Daily and for NCEI's work on it been stable, cut or threatened between January 1, 2025 and November 2026, and what news from 2024 to 2026 names the dataset, its team or its people in connection with political decisions, policies, layoffs, staffing changes or funding cuts? Add to what those runs found rather than repeating it.

- **Funding:** enacted or proposed cuts, proposed termination or retirement of GHCN-Daily or its products, and budget uncertainty (continuing resolutions, shutdowns, spend plans) for NCEI and the partners that pay for the work (such as CISESS), with dates and figures. Include FY2027's outcome after the continuing resolution ending December 11, 2026, if decided.
- **Workforce:** layoffs, reductions in force, buyouts, hiring freezes, reorganizations, contract changes or the NCEI cloud migration affecting the people who produce it, with numbers where published.
- **News:** for each item, outlet, date, headline, what it reports, and whether it names GHCN-Daily, its team or a person directly, or only NCEI or NOAA. Say plainly if none names them.
- **Consequences:** what each development could mean for its updates, completeness or availability.

Count actions aimed at NOAA or NCEI as a whole only where a source ties them to GHCN-Daily or its team. Rate each development and the funding overall: imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Use NOAA's, Congress's, GAO's and court documents to check what news claims, and news for events. Threats to its source networks are a separate question. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** dated funding developments for GHCN-Daily and NCEI from January 2025 to November 2026 (requests, enacted amounts, the FY2027 outcome if decided), staffing changes at NCEI that touch the GHCN-Daily work, a list of news items from 2024 on saying whether each names the dataset or only NCEI, what each could mean for the dataset, and a rating (imminent, emerging or no current threat found) for each development and for the funding overall. Expect a deep-tier run, because the topic involves cuts and layoffs.

**What I changed from your draft:**
- **Built on earlier runs:** the combined run already has the FY2026 and FY2027 NCEI figures, the 2025 NCEI staff losses, and three news items naming GHCN. The NCEI archive run covers NCEI's budget and reorganization. Part 3 will add the funding route. The question names those records and asks the run to add to them, so its time goes to what is new: the FY2027 outcome, CISESS's status, the cloud migration, and news the combined run had no budget left to find (it ran out of tokens, not leads).
- **Your two date ranges kept:** funding from January 1, 2025, news from 2024.
- **"Potential consequences"** became a line per development on updates, completeness or availability, so the answer says what each means for the dataset, not only for NCEI.
- **Same rating scale and NOAA-wide rule** as the combined run and the GPCP, PERSIANN-CDR and IMERG funding queries, so the answers compare.
- **Source networks left to Part 5,** which your Part 5 draft asks about.
- **Limits:** 40 minutes and 320,000 tokens, as the IMERG and PERSIANN-CDR funding runs used. GPCP's funding-and-news run needed the full 50 minutes and 400,000; use those if you want more room for news.

**Order and reuse:** run this after Part 3, in this project, so the funding route is in `web_search_results/`. It can also run without Part 3, since the combined run names the route. For another dataset, change the name, the host organization and the earlier runs it names.
