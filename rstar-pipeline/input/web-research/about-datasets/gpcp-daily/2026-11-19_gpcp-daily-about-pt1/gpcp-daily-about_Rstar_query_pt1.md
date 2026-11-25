# About GPCP Daily Part 1 R* Query for Claude

About dataset = GPCP Daily Part 1

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GPCP Daily (Global Precipitation Climatology Project) dataset.

## ChatGPT query

Research information about the GPCP Daily (Global Precipitation Climatology Project) dataset. Where is the dataset stored and accessed, including its official data repository or laboratory/group website? Is the dataset derived from multiple data sources, such as multiple satellites or a combination of satellite and rain gauge measurements, or is it an independent dataset based on a single measurement instrument or platform? If it is a derived dataset, identify all the datasets, satellites, instruments, and measurement platforms incorporated into its creation. Explain how these different data sources are combined to produce the GPCP Daily dataset. Describe how the measurements are obtained and processed, including whether processing relies on algorithms, direct measurements, or a combination of both.

## Claude web research skill query

/my:broad-web-research

What is the GPCP Daily (Global Precipitation Climatology Project daily precipitation) dataset, where is it kept and served, and who makes it? Cover the daily product only, and say which versions exist (such as the One-Degree Daily, or 1DD, record and the newer Version 3 daily product), which years each covers and which is current; mention the GPCP monthly and pentad products only to say how they relate. Tell apart the groups that produce it from the archives that only host or redistribute it. Leave quality control, file formats, the people involved, funding and threats to separate questions.

- **Where it lives:** for each version, the archive or repository that holds it and its main access points (archive pages, the producers' sites, download servers), with URLs.
- **What kind of dataset it is:** say whether it is blended from different sources or instruments (such as satellites and gauges) or taken from a single instrument. Name each input dataset, the organization that provides it and the satellites or instruments behind it, with its role (main input, calibration, or scaling to the monthly totals), and say how they are combined. Check these candidates without assuming each is used: geostationary infrared records (such as GridSat-B1 or NOAA CPC's merged infrared), passive microwave (SSM/I, SSMIS), infrared sounders (TOVS, AIRS), GPCC gauge analyses, GPCP monthly and IMERG.
- **How the data are made:** which steps are done by algorithm, what the algorithms are, whether any step uses direct measurements, and how often the record is extended.
- **Who is responsible:** the groups that produce each version, their parent organizations, and the program or project they work under.

Use the producers' and archives' own documentation and the developers' peer-reviewed papers ahead of secondary accounts. The earlier PERSIANN-CDR Daily runs' records (in web_search_results/) cover GPCP monthly as one of that dataset's inputs; use what they hold. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** an overview of GPCP Daily: which daily versions exist and which years each covers, where each is kept and served (with links), which datasets go into it, who provides each and what each one does, how they are merged into daily precipitation, and which groups produce it under which project. Expect a standard-tier run.

**What I changed from your draft:**
- **Versions:** GPCP Daily comes in more than one version (the long-running One-Degree Daily record and a newer Version 3 daily product), and different archives may hold different ones. The question asks which version sits where and for which years, so the later parts know which one they are asking about. The two names are candidates; the run confirms them.
- **Producer versus host:** the dataset may be made by one group and archived by another. The question asks the run to tell them apart, as in the PERSIANN-CDR and GHCN-D queries.
- **Inputs by role:** for a blended product the role matters as much as the name: an input can feed the daily estimate, calibrate it, or scale it to the monthly totals. The question asks for each input's role and its provider (which Part 5 needs), and lists likely inputs as candidates to check, not as facts.
- **People left to Part 3:** your Part 3 asks about the institutions and people in depth, so this run names the producing groups only.
- **Earlier runs:** the PERSIANN-CDR runs already saved material on GPCP (it is one of PERSIANN-CDR's inputs, and they found notes on GPCP v2.3 and V3.3), so the question points to them.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run. If you want more room for two versions' worth of inputs, use 40 minutes and 320,000.

**Order and reuse:** run this first, in this project. Parts 3–5 use its record: Part 3 for the producing groups, Part 4 for the groups and people to look for in funding records and the news, and Part 5 for the list of inputs and their providers. Part 2 can run before or after it. The layout matches PERSIANN-CDR and GHCN-D Part 1, so the answers compare section by section.
