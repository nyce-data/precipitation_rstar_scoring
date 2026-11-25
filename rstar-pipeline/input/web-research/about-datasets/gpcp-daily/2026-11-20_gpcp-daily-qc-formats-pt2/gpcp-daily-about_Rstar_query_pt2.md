# About GPCP Daily Part 2 R* Query for Claude

About dataset = GPCP Daily Part 2

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GPCP Daily (Global Precipitation Climatology Project) dataset.

## ChatGPT query

Research the data processing and quality control procedures used for the GPCP Daily dataset. Is quality control (QC) performed on the dataset, and if so, what methods are used to determine data quality and identify errors or inconsistencies? Is QC performed automatically using software or algorithms, manually by researchers, or by an independent group? Identify the software, algorithms, and processing methods used to generate and validate the dataset. Are the processing software and algorithms publicly available for researchers and the public to access and use? What data formats are used to store and distribute the GPCP Daily dataset, and do any of these formats present limitations regarding FAIR (Findable, Accessible, Interoperable, and Reusable) data principles?

## Claude web research skill query

/my:broad-web-research

How is GPCP Daily (Global Precipitation Climatology Project daily precipitation) quality-controlled, processed and validated, what formats is it published in, and can the public inspect and use its software? Cover each current version of the daily product (such as the One-Degree Daily record and the Version 3 daily product) as published by its producers and by each archive that serves it.

- **Quality control:** whether QC is done; the checks it runs, one line each; whether it is automated, manual or both; how suspect values are flagged or handled; and who performs it (the producers, the archive or another group, including QC on the input datasets, such as the gauge analyses, before they are used). Include validation against independent data, and any review the dataset's program requires, such as an algorithm description document or a maturity assessment, where one exists.
- **Processing:** the algorithms and software that produce and validate the daily estimates, named where possible.
- **Public availability:** for each piece of software or algorithm, whether its code is published (where, and under what license) or only described in papers.
- **Formats:** each format and access route the dataset is offered in, judged on four tests: findable (a persistent identifier such as a DOI, and metadata in a searchable catalog); accessible (downloadable over a standard open protocol without a login); interoperable (an open, documented format that common tools read, with standard variable names and units); reusable (a stated license and provenance). Rate each FAIR, partly FAIR (name the tests it fails) or non-FAIR.

Say where something is not published. Use the producers' and archives' documentation, code repositories and the developers' papers ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** how GPCP Daily is checked and validated and by whom, the algorithms and software that make it, whether each piece of code is public, and a FAIR rating for each format and access route, naming the tests it fails. Expect a standard-tier run.

**What I changed from your draft:**
- **FAIR tests defined:** your draft asked whether any format limits FAIR use without saying how to judge it. I used the same four tests and three levels as the PERSIANN-CDR and GHCN-D Part 2 queries, so the datasets are rated the same way. FAIR mostly describes how a dataset is published, so the run rates each format together with the route it is served by.
- **Versions and archives:** the daily versions may sit in different archives (a NOAA climate-data-record archive, a NASA data center) in different formats, so the question covers each.
- **QC in a blended product:** a merged satellite-gauge product may have little QC of its own beyond checks on its inputs, validation, and the reviews its program requires. The question asks for those, so "no separate QC step" isn't read as "no QC".
- **Code, item by item:** the question asks about each piece of software separately and tells published code apart from methods only described in papers.
- **Overlap with Part 3:** your Part 3 also asks about software; I kept software here and left Part 3 the people and computing.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run.

**Order and reuse:** run it in this project, before or after Part 1; if Part 1 ran first, this run reads its record and knows the versions. Parts 3–5 don't depend on it.
