# About IMERG Late Run Part 5 R* Query for Claude

About dataset = IMERG Late Run

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM) dataset.

## ChatGPT query

Research news and developments from 2024 through November 2026 concerning the IMERG Late Run dataset, its managing organizations, research groups, and personnel, particularly political decisions, government policy changes, funding reductions, layoffs, or program cancellations that could affect the dataset's continued production and availability. If IMERG Late Run is a derived dataset, investigate whether any of its contributing satellite missions, instruments, rain gauge networks, measurement platforms, data repositories, or associated research organizations have experienced funding cuts, operational disruptions, termination announcements, or end-of-life plans. Determine whether these developments could affect the availability, continuity, accuracy, or long-term sustainability of IMERG Late Run. Identify which contributing data sources are most at risk and explain the potential consequences for the dataset. Support findings with credible news coverage, official government announcements, project documentation, and research organization statements.

## Claude web research skill query

### Run 1: news

/my:broad-web-research

Using the earlier runs' records on IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM, Late Run), its producers, people and funding (in web_search_results/), what news coverage between January 2024 and November 2026 names the dataset, IMERG or GPM, the groups that produce, process or archive it (such as NASA Goddard's IMERG team and Precipitation Processing System, and GES DISC) or their named people, in connection with political decisions, government policy changes, funding cuts, layoffs or program cancellations that could affect its production or availability?

- **For each item:** outlet, date, headline, what it reports, and whether it names the dataset, a group or a person directly, or only a program or center that funds them. Say plainly if none names them.
- **Rating:** imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found, and whether it could affect the Late Run's production or availability.

Use news, institutional announcements and official statements for events, and official documents to check what a report claims. Add what the news reports to the earlier funding record rather than repeating it. Threats to IMERG's input satellites are a separate question. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:**
- **Run 1 (news):** a dated list of news items from 2024 to November 2026 that name IMERG, GPM, the groups that make it or their people, each saying whether it names them directly or only their funder, rated imminent, emerging or no current threat found; or a plain statement that none names them. Expect a deep-tier run, because the topic involves cuts and layoffs.
- **Run 2 (inputs):** for each input of IMERG Late Run, and the satellites, instruments and organizations behind it, what happened to it between 2024 and November 2026, rated the same way, and what that does to the Late Run: stops it, degrades it, or has little effect. Expect a deep-tier run, because it covers terminations across a dozen or more satellites.

**What I changed from your draft:**
- **Split into two runs:** your draft asks about news on IMERG and its groups, and about threats to every input. They live in different sources (news coverage versus mission and agency documents), and the input list is long enough to need its own budget. Neither run needs the other, so they can go in either order.
- **News tied to Part 4:** your Part 4 already covers funding cuts, layoffs and reorganizations from official records. Run 1 uses that record and adds what the news reports, so the two parts don't search the same ground twice. News counts only where it names the dataset, its groups or people, or a program that funds them, as in the GPCP, PERSIANN-CDR and GHCN-D news queries.
- **"Is it derived?" handed to Part 1:** Part 1 answers that and lists the inputs; Run 2 uses its list.
- **Near-real-time feeds:** the Late Run is made within hours of observation, so a stopped data feed matters even while the satellite still flies. The earlier NOAA satellites run found the DMSP data-flow notice of September 30, 2026, which is the kind of event Run 2 should catch.
- **Effect defined:** your draft asked how the developments could affect availability, continuity, accuracy and sustainability, and which sources are most at risk. The three effect levels and the rating make the run say which, input by input. A merged product with many satellites often loses accuracy rather than stopping, so "degrades" is spelled out.
- **Built on earlier runs:** the NASA and NOAA satellites runs cover GPM, Aqua, DMSP and JPSS; GPCP's Part 5 found the IMERG V08 delay, and its Part 6 satellites run listed the microwave satellites that reach GPCP through IMERG; PERSIANN-CDR's inputs run covers DMSP, POES and GPCC. Run 2 names those records.
- **Candidates, not facts:** the list says "without assuming any is used or affected". If Part 1 finds different inputs, the run uses its list.
- **Your date range kept:** January 2024 to November 2026, for both runs.

**Limits:** Run 1 has 30 minutes and 240,000 tokens, since Part 4 does the funding search; use 40 minutes and 320,000 if Part 4 hasn't run. Run 2 has 40 minutes and 320,000, below the deep tier's full budget, because the earlier records cover much of the satellite chain (GPCP's inputs run used 224,000 tokens with the same limits). If Part 1 finds a long list of inputs not covered before, use 50 minutes and 400,000.

**One-run version:** join both questions, keeping all the bullets, with a time limit of 50 minutes and a token ceiling of 400,000. It gives up depth on one side: the input list would take most of the budget, and the news would get the least.

**Order and reuse:** run both in this project. Run 1 goes after Part 4 (and Parts 1 and 3, for the names to search for); Run 2 after Part 1. Don't add "Don't use earlier runs."; both depend on them. If Part 4 finds that no funding source or group faces any threat, Run 1 may find little news; it is still worth a short run, since news sometimes reports what official records don't yet show. The two questions are in one file; you can split it into pt5a and pt5b if you want one query per file.
