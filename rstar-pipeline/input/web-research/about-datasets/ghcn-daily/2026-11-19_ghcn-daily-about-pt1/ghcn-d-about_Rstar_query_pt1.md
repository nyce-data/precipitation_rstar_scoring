# About GHCN-D Part 1 R* Query for Claude

About dataset = GHCN-D Part 1

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GHCN-D (Global Historical Climatology Network daily) dataset.

## ChatGPT query

Research information about the GHCN-D (Global Historical Climatology Network Daily) dataset. Where is the dataset stored and accessed from (the data repository or laboratory group website)? Is this dataset derived from other data sources, such as multiple satellites or satellite and rain gauge data, or is it an independent dataset with data from a single defined measurement instrument or platform, such as rain gauges or one satellite? If it is a derived dataset, identify which datasets are incorporated and how they are combined to create GHCN-D. How are the data collected and processed, such as through algorithms or direct measurements? Is there a single group responsible for making the measurements or performing the processing? If so, identify the group and determine how many people are involved in measuring and processing the GHCN-D data.

## Claude web research skill query

/my:broad-web-research

What is the GHCN-Daily (Global Historical Climatology Network–Daily) dataset, where is it kept and served, and who makes it? Cover the current version of GHCN-Daily only; mention GHCN-Monthly or the hourly product only to say how they relate. Leave quality control and file formats to a separate question.

- **Where it lives:** the archive or repository that holds it and its main access points (web pages, download servers, cloud copies), with URLs.
- **What kind of dataset it is:** say whether it is compiled from station records of many networks and countries, blended from different kinds of instrument (such as gauges and satellites), or taken from a single network or instrument. Name the source networks and data streams it draws on, with the count or share of stations from each where published, and say how they are merged (matching stations, removing duplicates, choosing among overlapping records).
- **How the data are made:** which values are direct measurements, and by what instruments; which steps are done by algorithm; and how often the dataset is updated.
- **Who is responsible:** the group that compiles and maintains it, and its parent organization. Name the people credited as its developers or maintainers. Give a staff count only where one is published, and say so where none is.

Use the maintainer's own documentation and the peer-reviewed papers by the dataset's developers ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** an overview of GHCN-Daily: where it is kept and served (with links), what kind of dataset it is and which networks feed it, how its values are measured and merged, and who maintains it, with named people, and a staff count only if one is published. Expect a standard-tier run.

**What I changed from your draft:**
- **"Derived" made concrete:** your draft asked whether it is derived from several sources or comes from one instrument. GHCN-Daily fits neither cleanly: it compiles records from many station networks, but they are all ground stations, not a blend of satellites and gauges. The question asks the run to say which of three kinds it is, so the answer doesn't call it "derived" in the satellite-blend sense.
- **Source shares and merging:** for a station compilation, "how they are combined" means which networks supply how many stations and how overlapping records are resolved, so I asked for those.
- **Staff count:** such counts are rarely published. The run names the credited developers and says when no count exists, rather than estimating one.
- **GHCN-Daily only:** I kept GHCN-Monthly and the hourly product out except for how they relate, and left quality control and formats to Part 2, so the two runs don't repeat each other.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run.

**Order and reuse:** run this first, in this project. Part 3 names this run's record to get GHCN-Daily's list of sources; Part 2 can run before or after it. The three parts could be one question, but each would get about a third of the time, so keep them separate. To reuse this for another station dataset, change the name, the related products and the maintainer.
