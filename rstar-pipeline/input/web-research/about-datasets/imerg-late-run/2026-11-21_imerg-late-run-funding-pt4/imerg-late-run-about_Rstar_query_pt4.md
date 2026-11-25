# About IMERG Late Run Part 4 R* Query for Claude

About dataset = IMERG Late Run

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM) dataset.

## ChatGPT query

Research how the organizations, laboratories, research groups, and projects responsible for creating, processing, and maintaining the IMERG Late Run dataset are funded. Identify their primary funding agencies, government programs, grants, and other financial support mechanisms. Investigate whether their funding has remained stable or whether funding reductions, budget cuts, program cancellations, or potential termination have occurred or are anticipated between January 1, 2025, and November 2026. Identify any reported layoffs, hiring freezes, staffing reductions, reorganizations, or other workforce changes affecting the researchers and personnel responsible for the dataset. Provide relevant news reports, official announcements, government budget documents, and other reliable sources.

## Claude web research skill query

/my:broad-web-research

How are the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM, Late Run) dataset and the groups that produce, process and maintain it funded, and has that funding been stable, cut or threatened between January 1, 2025 and November 2026? Use the earlier runs' records in web_search_results/ on IMERG Late Run (its producers, institutions and people), NASA's satellite precipitation capability, and GPCP Daily's people and funding (its Version 3 is built by the same Goddard group), and spend the time on what they did not cover.

- **Funding sources:** each route that pays for producing, processing and serving it: NASA programs (such as the Precipitation Measurement Missions science team, GPM mission operations, and the data-system funding for the Precipitation Processing System and GES DISC), JAXA's share of GPM, and grants, contracts or cooperative agreements to the producing groups and their contractors. Give amounts, award or contract numbers and fiscal years where published, and say so where none is.
- **Stability and threats:** for each source, enacted or proposed cuts, cancellations or proposed terminations, mission reviews (such as NASA's 2026 Senior Review of GPM), and budget uncertainty (continuing resolutions, shutdowns).
- **Workforce:** layoffs, reductions in force, hiring freezes, contract changes, reorganizations or data-center consolidation affecting the people who produce, process or archive it.

Count actions aimed at NASA or federal research as a whole only where a source ties them to one of these funding sources or groups. Rate each funding source, each workforce change and the funding overall: imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Use agency budget documents, award and contract databases, and Congress's and GAO's documents ahead of news, and use news for events. News coverage and threats to the input satellites are separate questions. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** each source of money behind IMERG Late Run, with amounts, award or contract numbers and years where published; any cuts, proposed terminations, reviews or budget uncertainty touching them; staffing changes at the groups that make it; and a rating (imminent, emerging or no current threat found) for each funding source, each workforce change and the funding overall. Expect a deep-tier run, because the topic involves cuts and layoffs.

**What I changed from your draft:**
- **Built on earlier runs:** Parts 1 and 3 name the producers, institutions and people. The NASA satellites run covers GPM's mission budget, the 2026 Senior Review (results not yet published when it ran) and the NASA data-center changes. GPCP's Parts 3 and 4 cover Huffman's Goddard group and its contractors (they found Goddard and SSAI staff losses, and an open question about which contract pays two of its programmers). The question names those records so this run spends its time on IMERG's own money.
- **What counts:** a cut to a program that funds a producing group counts; a cut aimed at NASA or federal research in general counts only where a source ties it to IMERG's funding or groups. That is the same rule and the same rating scale as the GPCP, PERSIANN-CDR and GHCN-D funding queries, so the answers compare.
- **Your workforce questions kept** (layoffs, hiring freezes, staffing reductions, reorganizations), with contract changes and data-center consolidation added, since contractors and the NASA archive do much of the work.
- **JAXA:** GPM is a joint NASA–JAXA mission, so Japan's funding is a candidate too.
- **News and input threats left to Part 5,** which your Part 5 draft asks about; this run uses official records and uses news only for events.
- **Your date range kept:** January 1, 2025 to November 2026.
- **Limits:** 40 minutes and 320,000 tokens, as PERSIANN-CDR's funding-only run used (it ended at 28 minutes). GPCP's funding-and-news run needed the full 50 minutes and 400,000; this one leaves the news to Part 5.

**Order and reuse:** run this after Parts 1 and 3, in this project, so the producers and people are in `web_search_results/` to look for. Part 5's news run uses its record so it doesn't repeat the funding search.
