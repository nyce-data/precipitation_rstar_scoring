# About IMERG Late Run Part 3 R* Query for Claude

About dataset = IMERG Late Run

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM) dataset.

## ChatGPT query

Research the data formats in which the IMERG Late Run dataset is distributed and stored, including whether any formats or associated metadata create barriers to FAIR data principles (Findable, Accessible, Interoperable, and Reusable). Identify whether one research group or multiple organizations are responsible for collecting the measurements, processing the data, and maintaining the final dataset. How many researchers, scientists, technicians, or other personnel are involved in the groups responsible for measurement collection and data processing? Identify the processing software and algorithms used to create IMERG Late Run and determine whether their source code, documentation, and technical specifications are publicly available. Include links to the relevant software repositories, documentation, and organizational websites where possible.

## Claude web research skill query

/my:broad-web-research

How is the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM, Late Run) dataset published, who does the work, and is its software public? Using the earlier runs' records on IMERG Late Run's sources, hosts and processing (in web_search_results/), cover the current version and each archive or route that serves it.

- **Formats:** each file format and access route (check HDF5, netCDF-4, GeoTIFF, text, OPeNDAP and cloud copies, without assuming any is offered), judged on four tests: findable (a persistent identifier such as a DOI, and metadata in a searchable catalog); accessible (downloadable over a standard open protocol without a login); interoperable (an open, documented format that common tools read, with standard variable names and units); reusable (a stated license and provenance). Rate each FAIR, partly FAIR (name the tests it fails) or non-FAIR.
- **Institutions:** whether one group or several organizations collect the measurements, process the data and maintain the dataset, and what each is responsible for. Check these candidates without assuming each takes part: the IMERG team and the Precipitation Processing System at NASA Goddard, NASA's GES DISC, JAXA, NOAA's Climate Prediction Center, UC Irvine's CHRS, and GPCC at Germany's weather service.
- **People:** principal investigators, team leads and key staff, with institution and role; a headcount only where one is published (say so where none is, and give documented team or author lists as the nearest evidence).
- **Software:** for each processing program and algorithm, whether its source code, documentation and specifications are public, where (with links), and under what license.

Use the producers' and archives' own pages, code repositories and the developers' papers ahead of secondary accounts. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** a FAIR rating for each format and access route, naming the tests it fails; the institutions behind IMERG Late Run and what each does; the named leads and key staff, with a headcount only if one is published; and for each piece of software, whether its code is public, where and under what license. Expect a standard-tier run.

**What I changed from your draft:**
- **FAIR tests defined:** your draft asked whether formats or metadata create FAIR barriers without saying how to judge them. I used the same four tests and three levels as the GPCP, PERSIANN-CDR and GHCN-D Part 2 queries, so the datasets are rated the same way. FAIR mostly describes how a dataset is published, so the run rates each format together with the route that serves it.
- **Built on Parts 1 and 2:** Part 1 names the producers and hosts, and Part 2 names the software; this run starts from their records.
- **Collect, process, maintain:** your draft asked who does each. For IMERG the measurements come from many satellite operators, so the question asks for each organization's responsibility, and lists likely participants as candidates, not facts. Part 4 needs this to decide whose funding counts.
- **Staff count:** such counts are rarely published. The run says so and gives team or author lists instead of guessing. (The NASA satellites run found no published staffing for the Precipitation Processing System or GES DISC.)
- **Code, item by item:** the question asks about each program separately and tells published code apart from methods only described in papers.
- **Limits:** 40 minutes and 320,000 tokens, because this covers three things (formats, people, code) that GPCP split across two runs of about 170,000 tokens each. If time is short, 30 minutes and 240,000 will do, with thinner coverage of the people.

**Order and reuse:** run this after Parts 1 and 2, in this project. Part 4 uses its record for the institutions and people to look for in funding records, and Part 5's news run for the names to search for.
