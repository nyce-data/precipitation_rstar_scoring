# About PERSIANN-CDR Daily Part 4 R* Query for Claude

About dataset = PERSIANN-CDR Daily Part 4

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset.

## ChatGPT query

Investigate whether the PERSIANN-CDR Daily dataset, its responsible organization, or the researchers, employees, and staff involved in its creation, maintenance, and production have been mentioned in news coverage between 2024 and 2026. Pay particular attention to reporting about political decisions, government policies, changes in federal research priorities, budget cuts, layoffs, funding reductions, organizational restructuring, or threats to the continuation of the research program. Identify relevant news reports and assess their potential implications for the dataset's continued production and availability.

## Claude web research skill query

/my:broad-web-research

Between January 2024 and November 2026, has news coverage mentioned PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record), the group that produces it, or its researchers and staff, in connection with political decisions, policies, shifts in federal research priorities, budget cuts, layoffs, funding reductions, restructuring or threats to the program's continuation? Use the earlier runs' records in web_search_results/ on PERSIANN-CDR Daily (its producer, program and named people) and on its funding, and spend the time on coverage they did not find.

- **What counts:** reporting that names the dataset, its producing group, its parent organization or its named people, or the program that funds it. Count coverage of NOAA, NASA, universities or federal research in general only where it names one of these.
- **For each item:** the outlet, date and headline, what it reports, and whether it names the dataset or group directly or only the program that funds it.
- **Implications:** for each item, what it means for the dataset's continued production and availability, rated imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found.

Say so plainly if no coverage names them. Use news outlets, trade and science press, and the producer's, university's and agency's own announcements; use official documents to check what a report claims. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** a dated list of news items that name PERSIANN-CDR Daily, its producing group, its people or the program that funds it, each with what it reports and a rating of what it means for the dataset (imminent, emerging or no current threat found). If nothing names them, the answer says so. Expect a deep-tier run, because the topic involves cuts and layoffs.

**What I changed from your draft:**
- **What counts as a mention:** a small university group is rarely named in the news, while NOAA and federal research cuts are covered all the time. The question counts general coverage only where it names the dataset, the group, its people or the program that funds it; otherwise the answer would fill up with NOAA-wide stories. This is the same rule as Parts 3 and 5 and the GHCN-D queries.
- **Direct or through the funder:** each item says whether it names the dataset itself or only its funding program, since the second is a weaker signal.
- **Implications rated:** your draft asked to "assess potential implications". I used the same scale as Part 3, so the two answers compare.
- **News first:** unlike the other parts, this one puts news and press releases first, and uses official documents to check them.
- **Your date range kept:** January 2024 to November 2026.
- **Limits:** 40 minutes and 320,000 tokens; the subject is narrow.

**Order and reuse:** run this after Parts 1 and 3, in this project, so the producer's name, its people and its funding programs are in `web_search_results/` to search for. Part 3's run may already have found most of the news on funding; if so, this run may find little new, and a time limit of 30 minutes and a token ceiling of 240,000 would do.
