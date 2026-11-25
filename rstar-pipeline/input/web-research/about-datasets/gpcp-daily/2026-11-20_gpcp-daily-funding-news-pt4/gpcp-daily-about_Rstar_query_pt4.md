# About GPCP Daily Part 4 R* Query for Claude

About dataset = GPCP Daily Part 4

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GPCP Daily (Global Precipitation Climatology Project) dataset.

## ChatGPT query

Investigate how the GPCP Daily dataset and the research groups responsible for producing and maintaining it are funded. Identify the primary funding agencies, government programs, research institutions, grants, and other financial sources supporting the dataset's measurements, processing, and continued availability. Determine whether this funding is stable or whether there have been funding reductions, budget cuts, grant cancellations, or threats of program elimination between January 1, 2025, and November 2026. Research whether the GPCP project, its associated research groups, institutions, or personnel have appeared in news reports between 2024 and 2026 concerning political decisions, changes in government research priorities, funding uncertainty, layoffs, staffing reductions, or institutional restructuring. Include relevant news articles, official announcements, government documents, and institutional statements to support the findings.

## Claude web research skill query

/my:broad-web-research

How are GPCP Daily (Global Precipitation Climatology Project daily precipitation) and the groups that produce it funded, has that funding been stable, or cut or threatened, between January 1, 2025 and November 2026, and have the project, its groups or their people appeared in news coverage between January 2024 and November 2026 about political decisions, shifts in research priorities, funding uncertainty, layoffs or restructuring? Use the earlier runs' records in web_search_results/ on GPCP Daily (its producers, institutions and named people), NOAA NCEI, NASA's satellite precipitation capability and PERSIANN-CDR Daily's inputs (which include GPCP), and spend the time on what they did not cover.

- **Funding sources:** each route that pays for producing, maintaining and serving it: agency programs (such as NASA Earth science or precipitation science funding and NOAA's Climate Data Record program), grants, contracts or cooperative agreements to the producing groups, Germany's funding of GPCC, and institutional support. Give amounts, award numbers and fiscal years where published, and say so where none is.
- **Stability and threats:** for each source, cuts, proposed cuts, grant or contract terminations or non-renewals, staff losses, budget uncertainty (such as continuing resolutions or shutdowns), or proposals to end the program. Count actions aimed at NASA, NOAA or federal research as a whole only where a source ties them to that funding source or to a producing group.
- **News:** each item that names the dataset, the project, a producing group or its named people, or a program that funds them: outlet, date, headline, what it reports, and whether it names them directly or only the funding program. Say plainly if none names them.

Rate each funding source, each news item and the dataset's funding overall: imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Use agency, university and award-database records and Congress's and GAO's documents for funding, news and institutional announcements for events, and official documents to check what a report claims. Threats to the input satellites and datasets are a separate question. With a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:** each source of money behind GPCP Daily, with amounts, award numbers and years where published; a dated list of news items that name the dataset, its groups or people, or their funders; and a rating (imminent, emerging or no current threat found) for each funding source, each news item and the funding overall. Expect a deep-tier run, because the topic involves cuts and layoffs.

**What I changed from your draft:**
- **Built on earlier runs:** Parts 1 and 3 name the producers, institutions and people; the NCEI and NASA satellite runs cover those agencies' budgets and the NASA data-center changes; the PERSIANN-CDR runs found notes on GPCP's own versions. The question names those records, so this run spends its time on GPCP's own money and coverage.
- **What counts:** a cut to a program that funds a producing group counts. A cut aimed at NASA, NOAA or federal research in general counts only where a source ties it to GPCP's funding or groups, and news counts only where it names one of them. That is the same rule as the PERSIANN-CDR and GHCN-D queries, and so is the rating scale, so the answers compare.
- **Direct or through the funder:** each news item says whether it names GPCP itself or only its funding program, since the second is a weaker signal.
- **Non-US funding:** GPCC's gauge analysis is run by Germany's weather service, so its funding is a candidate too.
- **Budget uncertainty** (your draft's term) is spelled out as continuing resolutions and shutdowns. FY2027 runs on a continuing resolution to December 11, 2026.
- **Input threats left to Part 5,** so this run doesn't spend its time on satellites.
- **Your date ranges kept:** funding from January 1, 2025, news from 2024, both to November 2026.
- **Limits:** 50 minutes and 400,000 tokens, the deep tier's full budget, because the question covers both funding and news.

**Splitting it (optional):** funding and news live in different sources, and PERSIANN-CDR's version split them into two runs (its Parts 3 and 4). If this run ends at its token ceiling with leads left, run the news part again on its own, using this run's record, with a time limit of 30 minutes and a token ceiling of 240,000.

**Order and reuse:** run this after Parts 1 and 3, in this project, so the producers, institutions and people are in `web_search_results/` to search for. Part 2 doesn't matter to it; Part 5 can run before or after it.
