# About GHCN-D Part 2 R* Query for Claude

About dataset = GHCN-D Part 2

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GHCN-D (Global Historical Climatology Network daily) dataset.

## ChatGPT query

Research the quality control (QC) procedures used for the GHCN-D (Global Historical Climatology Network Daily) dataset. Is quality control performed on the dataset? If so, explain the QC methodology, including how quality control is determined, whether specialized software or algorithms are involved, and whether a different organization or research group performs the QC. What data formats is the GHCN-D dataset stored in, and are any of these formats considered non-FAIR (Findable, Accessible, Interoperable, and Reusable)? If data processing is performed, identify the software, algorithms, or other methods used. Are the processing software and algorithms publicly available for researchers and the general public to inspect and use?

## Claude web research skill query

/my:broad-web-research

How is GHCN-Daily (Global Historical Climatology Network–Daily) quality-controlled and processed, what formats is it published in, and can the public inspect and use its software? Cover the current version of GHCN-Daily, maintained by NOAA's National Centers for Environmental Information (NCEI).

- **Quality control:** whether QC is done; the checks it runs, one line each; whether it is automated, manual or both; how failed values are flagged and whether they are removed; and who performs it (NCEI or another group, including any QC a source network does before its data reach NCEI).
- **Other processing:** the software or algorithms used beyond QC, such as merging sources or producing the published files, named where possible.
- **Public availability:** for each piece of software or algorithm, whether its code is published (where, and under what license) or only described in papers.
- **Formats:** each format and access route GHCN-Daily is offered in, judged on four tests: findable (a persistent identifier such as a DOI, and metadata in a searchable catalog); accessible (downloadable over a standard open protocol without a login); interoperable (an open, documented format that common tools read, with standard variable names and units); reusable (a stated license and provenance). Rate each FAIR, partly FAIR (name the tests it fails) or non-FAIR.

Say where something is not published. Use NCEI's documentation, code repositories and the developers' papers ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** the QC checks GHCN-Daily runs, who runs them and how flags work; the other processing software; whether each piece of code is public; and a FAIR rating for each format and access route, naming the tests it fails. Expect a standard-tier run.

**What I changed from your draft:**
- **FAIR tests defined:** your draft asked whether any format is "non-FAIR" without saying how to judge it. I gave one test per principle and three levels, so every format is rated the same way. FAIR mostly describes how a dataset is published rather than the file format itself, so the run rates each format together with the route it is served by.
- **Who does QC:** I added QC done by the source networks before the data reach NCEI, because a network may check its own data first, and that check belongs in the answer too.
- **Code, item by item:** your draft asked once whether the software is public. The question asks for each piece separately and tells published code apart from methods only described in papers, since a paper is not code you can inspect or run.
- **One processing question:** your draft asked about processing software twice; I merged the two.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run.

**Order and reuse:** run it in this project, before or after Part 1; if Part 1 ran first, this run reads its record. For another dataset's Part 2 (for example PERSIANN-CDR Daily), change the name and the maintainer; the FAIR tests carry over unchanged.
