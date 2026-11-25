# About IMERG Late Run Part 1 R* Query for Claude

About dataset = IMERG Late Run

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM) dataset.

## ChatGPT query

Research the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM) dataset. Where is the dataset stored and accessed, including the official data repository, laboratory, or project group website? Is IMERG Late Run an independently measured dataset from a single instrument, satellite, or platform, or is it a derived dataset incorporating multiple data sources? If it is a derived dataset, identify all the datasets, satellite instruments, rain gauges, and other measurement sources incorporated into it. For each incorporated source, identify its associated project, research group, and organization responsible for collecting or providing the data.

## Claude web research skill query

/my:broad-web-research

What is the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM, Late Run) precipitation dataset, where is it kept and served, and what is it made from? Cover the Late Run only, including its half-hourly and daily products, and say which version is current; mention the Early and Final Runs only to say how they differ from it (how soon after observation each is made, and how gauge data enter each). Tell apart the groups that produce it from the archives that only host or redistribute it. Leave processing details, quality control, formats, people, funding and threats to separate questions.

- **Where it lives:** the official archive or repository and the main access points (archive pages, the producers' servers, visualization tools and cloud copies), with URLs.
- **What kind of dataset it is:** whether it comes from a single instrument, satellite or platform, or is derived from several sources, and in outline how they are combined.
- **Inputs:** each input dataset, satellite sensor, gauge analysis or model field; its role (precipitation estimate, calibration reference, motion vectors for filling gaps, gauge adjustment); and the project, group and organization that collects or provides it. Check these candidates without assuming each is used: passive microwave sensors (GMI, AMSR2, SSMIS, MHS, ATMS) and the satellites that carry them; the GPM Core Observatory's radar; geostationary infrared (NOAA CPC's merged infrared) and PERSIANN-CCS; GPCC gauge analyses; MERRA-2 or GEOS model fields. Name satellites by family where the full list is long.

Use NASA's and the IMERG team's own documentation (algorithm description document, technical documentation, release notes) and the developers' papers ahead of secondary accounts. The earlier GPCP Daily runs' records (in web_search_results/) cover IMERG as an input to GPCP, including the microwave satellites behind it; use what they hold. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** an overview of IMERG Late Run: which version is current, how it differs from the Early and Final Runs, where it is kept and served (with links), whether it is derived (it almost certainly is), and each input with its role and the organization that provides it. Expect a standard-tier run.

**What I changed from your draft:**
- **Late Run only:** IMERG comes in three runs made at different times after observation, and they differ mainly in which inputs are available and how gauges are used (the Final Run uses monthly gauge analyses; the Early and Late Runs can't wait for them). The question keeps the run on the Late Run and asks for the differences only as context, so the later parts know what they are asking about.
- **Producer versus host:** the dataset may be made by one NASA group and served by another (and copied to cloud and visualization services). The question asks the run to tell them apart, as in the GPCP, PERSIANN-CDR and GHCN-D Part 1 queries.
- **Inputs by role:** for a merged product the role matters as much as the name: an input can give the precipitation estimate, calibrate the others, supply motion vectors, or adjust to gauges. The question asks for each input's role and provider (which Part 5 needs), and lists likely inputs as candidates to check, not as facts.
- **Satellites by family:** your draft asked for every instrument. IMERG draws on a constellation of a dozen or more satellites, so a full satellite-by-satellite list with dates would take a run of its own (as GPCP's Part 6 did). Here the run names them by family; the GPCP Part 6 satellites run already listed about 30 microwave satellites that reach GPCP through IMERG, and the question points to it.
- **Processing, QC and the rest left to Parts 2–5,** so this run stays an overview.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run. If you want more room for the input list, use 40 minutes and 320,000.

**Order and reuse:** run this first, in this project. Parts 2–5 use its record: Part 2 for the inputs and how they are combined, Part 3 for the producing groups and hosts, Part 4 for the groups to look for in funding records, and Part 5 for the list of inputs and providers. The layout matches the GPCP, PERSIANN-CDR and GHCN-D Part 1 queries, so the answers compare section by section.
