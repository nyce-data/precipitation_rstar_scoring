# About PERSIANN-CDR Daily Part 2 R* Query for Claude

About dataset = PERSIANN-CDR Daily Part 2

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset.

## ChatGPT query

Research the quality control (QC) procedures used for the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset. Is quality control performed on the dataset? If so, explain the QC methodology, including how quality control is determined, whether specialized software or algorithms are involved, and whether a different organization or research group performs the QC. What data formats is the PERSIANN-CDR Daily dataset stored in, and are any of these formats considered non-FAIR (Findable, Accessible, Interoperable, and Reusable)? If data processing is performed, identify the software, algorithms, or other methods used. Are the processing software and algorithms publicly available for researchers and the general public to inspect and use?

## Claude web research skill query

/my:broad-web-research

How is PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record) quality-controlled and processed, what formats is it published in, and can the public inspect and use its software? Cover the daily product as published by its producer and by its archive.

- **Quality control:** whether QC is done; the checks it runs, one line each; whether it is automated, manual or both; how suspect values are flagged or handled; and who performs it (the producer, the archive or another group, including any QC on the input datasets before they are used). Include any review the dataset's climate-data-record program requires, such as an algorithm description document or a maturity assessment, where one exists.
- **Processing:** the algorithm and software that produce the daily estimates, named where possible.
- **Public availability:** for each piece of software or algorithm, whether its code is published (where, and under what license) or only described in papers.
- **Formats:** each format and access route the dataset is offered in, judged on four tests: findable (a persistent identifier such as a DOI, and metadata in a searchable catalog); accessible (downloadable over a standard open protocol without a login); interoperable (an open, documented format that common tools read, with standard variable names and units); reusable (a stated license and provenance). Rate each FAIR, partly FAIR (name the tests it fails) or non-FAIR.

Say where something is not published. Use the producer's and archive's documentation, code repositories and the developers' papers ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** how PERSIANN-CDR Daily is checked and by whom, the algorithm and software that make it, whether each piece of code is public, and a FAIR rating for each format and access route, naming the tests it fails. Expect a standard-tier run.

**What I changed from your draft:**
- **FAIR tests defined:** your draft asked whether any format is "non-FAIR" without saying how to judge it. I used the same four tests and three levels as GHCN-D Part 2, so the two datasets are rated the same way. FAIR mostly describes how a dataset is published, so the run rates each format together with the route it is served by.
- **Producer and archive:** the producer's portal and the archive may offer different formats, so the question covers both.
- **QC in a satellite product:** a blended satellite product may have little QC of its own beyond checks on its inputs and the reviews its program requires. The question asks for those, so "no separate QC step" isn't read as "no QC".
- **Code, item by item:** the question asks about each piece of software separately and tells published code apart from methods only described in papers.
- **One processing question:** your draft asked about processing software twice; I merged the two.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run.
- **Rechecked 2026-11-19, after the Part 3 split:** the question didn't need changing; only the note on order below did.

**Order and reuse:** run it in this project, before or after Part 1; if Part 1 ran first, this run reads its record. Parts 3–5 don't depend on it.
