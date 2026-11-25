# About PERSIANN-CDR Daily Part 3 R* Query for Claude

About dataset = PERSIANN-CDR Daily Part 3

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset.

## ChatGPT query

Research how the group or organization responsible for creating, maintaining, and processing the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset is funded. Identify its primary funding sources, including government agencies, research grants, institutional support, and other funding arrangements. Determine whether its funding is stable or whether there have been funding cuts, threats of funding reductions, budget uncertainties, or potential elimination of relevant programs between January 1, 2025, and November 2026.

## Claude web research skill query

/my:broad-web-research

How is the production of PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record) funded, and has that funding been stable, or cut or threatened, between January 1, 2025 and November 2026? Use the earlier runs' records in web_search_results/ on PERSIANN-CDR Daily (who produces it, under which program) and on NOAA NCEI (its budget), and spend the time on what they did not cover. Cover the group that produces and extends the record; count the archive's budget only for its hosting role.

- **Funding sources:** each route that pays for producing and maintaining it: agency programs (such as NOAA's Climate Data Record program), grants or contracts to the producing group, university or institutional support, and any other arrangement. Give amounts, award numbers and fiscal years where published, and say so where none is.
- **Stability and threats:** for each source, cuts, proposed cuts, grant or contract terminations or non-renewals, staff losses, budget uncertainty (such as continuing resolutions or shutdowns), or proposals to end the program. Count actions aimed at NOAA, NASA or federal research grants as a whole only where a source ties them to that funding source or to the producing group.

Rate each funding source, and the dataset's funding overall: imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Use agency, university and award-database records and Congress's and GAO's documents ahead of news reports, and use news only for events; news coverage and the input datasets are separate questions. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** each source of money behind PERSIANN-CDR Daily (programs, grants, contracts, university support), with amounts, award numbers and years where published; and a rating (imminent, emerging or no current threat found) for each source and for the dataset's funding overall, with dates. Expect a deep-tier run, because the topic involves funding cuts.

**What I changed from your draft:**
- **Funding only:** the old Part 3 also covered news and the input datasets; those are now Parts 4 and 5. The question says so, so this run doesn't spend its time on them, though it still uses news to date events.
- **Built on earlier runs:** Part 1's record names the producing group and its program, and the NCEI run covers NCEI's budget. The question names both, so this run spends its time on the producing group's own money.
- **Producer versus archive:** if a university group makes the dataset and NOAA archives it, NCEI's budget pays for hosting, not production. The run counts it only for that role.
- **Grants, contracts and institutional support:** your draft listed these; for a university group they are often where the money comes from. Award amounts and numbers are asked for because award databases publish them even when agencies don't.
- **"Relevant programs":** a cut to a program that funds the producer counts. A cut aimed at NOAA, NASA or federal grants in general counts only where a source ties it to this dataset's funding. That is the same rule as the NCEI and GHCN-D queries, and so is the rating scale, so the answers compare.
- **Budget uncertainty** (your draft's term) is spelled out as continuing resolutions and shutdowns. FY2027 runs on a continuing resolution to December 11, 2026.
- **Limits:** 40 minutes and 320,000 tokens. The question is narrower than GHCN-D Part 3, which ran out of tokens covering four topics; this one covers one. Use 50 minutes and 400,000 if you want the deep tier's full budget.

**Order and reuse:** run this after Part 1, in this project, so the producing group and its program are in `web_search_results/`. Without Part 1 the run finds the producer itself, with less time for the funding. Part 2 doesn't matter to it. Part 4 (news) and Part 5 (inputs) can run after it and reuse its record.
