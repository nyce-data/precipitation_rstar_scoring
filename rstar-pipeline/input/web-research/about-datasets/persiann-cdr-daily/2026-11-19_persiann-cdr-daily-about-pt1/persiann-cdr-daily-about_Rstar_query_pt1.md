# About PERSIANN-CDR Daily Part 1 R* Query for Claude

About dataset = PERSIANN-CDR Daily Part 1

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset.

## ChatGPT query

Research information about the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks) dataset. Where is the dataset stored and accessed from (the data repository or laboratory group website)? Is this dataset derived from other data sources, such as multiple satellites or satellite and rain gauge data, or is it an independent dataset with data from a single defined measurement instrument or platform, such as rain gauges or one satellite? If it is a derived dataset, identify which datasets are incorporated and how they are combined to create PERSIANN-CDR Daily. How are the data collected and processed, such as through algorithms or direct measurements? Is there a single group responsible for making the measurements or performing the processing? If so, identify the group and determine how many people are involved in measuring and processing the PERSIANN-CDR Daily data.

## Claude web research skill query

/my:broad-web-research

What is the PERSIANN-CDR Daily (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks – Climate Data Record) dataset, where is it kept and served, and who makes it? Cover the daily product only; mention the monthly and yearly versions and other PERSIANN products (such as PERSIANN, PERSIANN-CCS and PDIR-Now) only to say how they relate. Tell apart the group that produces it from the archives that only host or redistribute it. Leave quality control, file formats, funding and threats to separate questions.

- **Where it lives:** the archive or repository that holds it and its main access points (archive pages, the producer's data portal, download servers), with URLs.
- **What kind of dataset it is:** say whether it is blended from different sources or instruments (such as satellites, radar and gauges) or taken from a single instrument. Name each input dataset, the organization that provides it and the satellites or instruments behind it, with its role (main input, training data, bias adjustment), and say how they are combined. Check these candidates without assuming each is used: geostationary infrared records such as GridSat-B1, GPCP monthly precipitation, and NCEP Stage IV radar.
- **How the data are made:** which steps are done by algorithm, what the algorithm is, and how often the record is extended.
- **Who is responsible:** the group that produces it, its parent organization, and the program it is produced under. Name the people credited as its developers or maintainers. Give a staff count only where one is published, and say so where none is.

Use the producer's and the archive's own documentation and the developers' peer-reviewed papers ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** an overview of PERSIANN-CDR Daily: where it is kept and served (with links), which datasets go into it, who provides each and what each one does, how the algorithm turns them into daily precipitation, who produces it and under which program, with named people, and a staff count only if one is published. Expect a standard-tier run.

**What I changed from your draft:**
- **Producer versus host:** the dataset may be made by one group and archived by another (for example a university group producing it under a NOAA program, with NOAA holding the archive copy). The question asks the run to tell the two apart, because Part 3's funding question depends on who actually does the work.
- **Inputs by role:** your draft asked which datasets are incorporated. For a blended product the role matters as much as the name: an input can feed the estimate, train the model or adjust its totals. The question asks for each input's role, and lists three likely inputs as candidates to check, not as facts.
- **Input providers (added 2026-11-19, after the Part 3 split):** Part 5 asks about threats to the inputs' providers, satellites and instruments, so this run now names them for each input. That gives Part 5 a list to check instead of making it rebuild one.
- **Related products kept out:** PERSIANN has several versions, and the daily CDR is easy to mix up with them. They come in only to say how they relate.
- **Staff count:** such counts are rarely published. The run names the credited developers and says when no count exists.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run.

**Order and reuse:** run this first, in this project. Parts 3–5 use this run's record: Part 3 for the producing group and its program, Part 4 for the names of the group and its staff to look for in the news, and Part 5 for the list of inputs and their providers. Part 2 can run before or after it. The layout matches GHCN-D Part 1, so the two answers compare section by section.
