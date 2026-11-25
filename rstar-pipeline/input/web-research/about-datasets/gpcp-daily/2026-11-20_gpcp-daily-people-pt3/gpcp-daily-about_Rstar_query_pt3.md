# About GPCP Daily Part 3 R* Query for Claude

About dataset = GPCP Daily Part 3

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GPCP Daily (Global Precipitation Climatology Project) dataset.

## ChatGPT query

Investigate the research group, laboratory, or organization responsible for creating, measuring, processing, and maintaining the GPCP Daily dataset. Is there one primary group responsible for the measurements and processing, or are multiple institutions and research groups involved? Identify the institutions and groups participating in the dataset's production and describe their respective responsibilities. How many researchers, scientists, technicians, or other personnel are involved in measuring, processing, and maintaining the GPCP Daily dataset? Identify the principal investigators, project leaders, or other key personnel when this information is publicly available. Determine what software, algorithms, and computational resources the responsible group uses to process and maintain the dataset, and whether these tools are publicly accessible.

## Claude web research skill query

/my:broad-web-research

Who produces and maintains GPCP Daily (Global Precipitation Climatology Project daily precipitation), and how is the work divided among institutions and people? Using the earlier run's record on what GPCP Daily is and who makes it (in web_search_results/), cover each current version of the daily product, and tell apart the groups that produce it or supply its inputs from the archives that only host it.

- **Institutions:** whether one group leads or several share the work; each institution and group taking part, and what it is responsible for (supplying inputs, merging, processing, archiving, oversight). Check these candidates without assuming each still takes part: NASA Goddard Space Flight Center, the University of Maryland's Earth System Science Interdisciplinary Center, the Global Precipitation Climatology Centre (GPCC) at Germany's weather service (DWD), NOAA's Climate Prediction Center and NCEI, and the GEWEX project of the World Climate Research Programme.
- **People:** the principal investigators, project leads and other key personnel named in the dataset's documentation, papers or project pages, with their institution and role, and whether they are still active on it.
- **Staffing:** how many scientists, programmers and technicians work on it, only where a figure is published; say so where none is, and give the documented team or author lists as the nearest evidence.
- **Computing:** whose computing systems process and serve it, where that is published.

Use the producers' documentation, project and staff pages and recent papers ahead of secondary accounts. Software and code availability are a separate question. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** the institutions behind GPCP Daily and what each does, the named principal investigators and key staff with their roles, a staff count only if one is published (otherwise the team lists), and where the processing runs. Expect a standard-tier run.

**What I changed from your draft:**
- **Built on Part 1:** Part 1 names the producing groups; this run starts from its record and spends its time on who does what and the people.
- **Candidate institutions:** GPCP is an international project, so the work is likely shared. The question lists likely participants as candidates, not facts, and asks whether each still takes part.
- **Producers, input suppliers and hosts:** a group that supplies an input (for example a gauge analysis) or only hosts the files has a different role from the one that merges the data. The question asks for each one's responsibility, which Part 4 needs to decide whose funding counts.
- **Staff count:** such counts are rarely published. The run says so and gives the documented team or author lists instead of guessing.
- **Software moved to Part 2:** your draft asked about software and its availability here too; Part 2 already covers that, so this run keeps only the computing resources.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run.

**Order and reuse:** run this after Part 1, in this project. Part 4 uses its record for the institutions and people to look for in funding records and the news. If Part 1's record already names the institutions and people in full, this run may add little; a time limit of 20 minutes and a token ceiling of 160,000 would do.
