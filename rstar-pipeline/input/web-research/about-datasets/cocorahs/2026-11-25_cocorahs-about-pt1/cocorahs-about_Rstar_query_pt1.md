# About CoCoRaHS Part 1: Overview R* Query for Claude

About dataset = CoCoRaHS Part 1, overview: hosts, inputs and producers

Written 2026-11-23 from `templates/template-dataset-about_Rstar_query_pt1_overview.md` and
`rstar-pipeline/processing/research-queries/archive-query-plan.md` in precipitation_rstar_scoring. Rewrite this with `/my:rewrite-research-query`,
then run the rewritten query with `/my:broad-web-research` in its own session. Suggested run folder:
`<date>_cocorahs-about-pt1`.

**Subcategories this part feeds:** RRS-1 (copies), D-2 (who serves it), DIRS-3 (inputs), DIRS-4 (outside groups),
P-4 (which groups do the work).

**Run order:** first of CoCoRaHS's six runs (Parts 1–5 and the A2 data-site run).

## Query to refine

Research the CoCoRaHS (Community Collaborative Rain, Hail and Snow Network) daily precipitation observations as a
dataset; mention its hail, snow, condition-monitoring, soil-moisture and evapotranspiration reports only to say how they
relate. Where is it stored and served: the CoCoRaHS data site (cocorahs.org ViewData, the Data Export Portal and
Export Manager at data.cocorahs.org, the Station Data Explorer at dex.cocorahs.org, the Water Year Summaries at
wys.cocorahs.org and the maps), any other bulk download, API or web service, and
every other place that holds a copy, such as NOAA NCEI's GHCN-Daily, the National Weather Service and state
climatologists, with URLs, which one is the archive of record, and whether each is a shared archive, CoCoRaHS's own
data site, or a copy? What are its inputs: how many volunteer observers and stations it has in each country and how
that has changed, what gauge they use, how reports are entered, and how often the data are updated? Which values are
direct measurements and which are derived (such as multi-day accumulations and summaries)? Which organizations
produce, host, use and pay for it, and what does each do, including the Colorado Climate Center at Colorado State
University, the sponsors, and state and regional coordinators? Leave quality control, people, funding amounts, and any
cuts or threats to later parts. Tag findings with RRS-1 "two or more geographically independent copies", D-2 "storage
is a single point of failure", DIRS-3 "depends on external data feeds" or DIRS-4 "needs outside processing
infrastructure". With a time limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats, layoffs or news; Part 4 covers them.
- **What kind of dataset it is:** a single network of volunteer observers with manual gauges, not a compilation or a
  satellite blend. The inputs are the volunteers, their gauges and the report-entry system.
- **Already known (CoCoRaHS site, read 2026-11-23):**
  - the network began at the Colorado Climate Center at Colorado State University in 1998, and the site carries the
    Colorado Climate Center's copyright; NOAA and NSF are named as major sponsors, with a longer sponsor list;
  - the ViewData page lists report pages and summaries, but says nothing about download formats, an API, a DOI or a
    data version;
  - the data use policy makes the data free under CC BY 4.0, provided "as is".
- **Already known (metadata file `rstar-pipeline/input/dataset-metadata/markdown/cocorahs_dataset-metadata.md`, a ChatGPT answer, added 2026-11-25, not yet checked):**
  - a Data Export Portal (data.cocorahs.org) with an Export Manager and a daily CSV export endpoint that takes start
    and end dates, state, station and units as parameters, so a bulk route does exist; no DOI for the dataset;
  - coverage: the United States, Canada, Puerto Rico, the U.S. Virgin Islands and the Bahamas;
  - users documented beyond NCEI: NWS river forecasting (NOAA report noaa/62044) and the METplus verification
    software, whose CoCoRaHS page describes the data and how to retrieve them.
  Ask the run to confirm these and say whether the export route is documented as public and stable.
- **Already known (earlier runs in web_search_results/):** CoCoRaHS stations are about 40% of GHCN-Daily's entries, and
  about 2,139 CoCoRaHS station IDs had 2025 data but none in 2026, against normal turnover of 1,785–2,078 a year
  (`2026-11-21_ghcn-daily-sources-pt5`). The rain-gauge run reports more than 28,000 volunteers
  (`2026-11-18_noaa-rain-gauge-threats`). Ask the run to build on these.
- **Hosts list.** The A2 data-site run and Part 4 start from this list. NCEI's copy inside GHCN-Daily is RRS-1 evidence.
- **Organizations, not people.** Named people and staff counts are Part 3's job.

### What the answer should give

- A table of hosts and access points, with URLs, which is the archive of record, and the kind of each.
- The observer and station counts over time, by country where published.
- The gauge, the report-entry system and the update schedule.
- A table of organizations and their roles.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

What are CoCoRaHS's (Community Collaborative Rain, Hail and Snow Network's) daily precipitation observations as a
dataset: where are they stored and served, what goes into them, and which organizations make them? Mention its hail,
snow, condition-monitoring, soil-moisture and evapotranspiration reports only to say how they relate. Build on the
earlier runs' records in web_search_results/: CoCoRaHS stations are about 40% of GHCN-Daily's entries
(2026-11-21_ghcn-daily-sources-pt5), and the network reports more than 28,000 volunteers
(2026-11-18_noaa-rain-gauge-threats).

- **Hosts:** every place that holds or serves a copy, with URLs. Check these without assuming each works as described:
  cocorahs.org ViewData and maps; the Data Export Portal and Export Manager at data.cocorahs.org (reported to have a
  daily CSV export by date range, state, station and units); the Station Data Explorer (dex.cocorahs.org); the Water
  Year Summaries (wys.cocorahs.org); any other bulk download, API or web service; and copies at NOAA NCEI's
  GHCN-Daily, the National Weather Service and state climatologists. For each: a shared archive, CoCoRaHS's own data
  site or a copy, and which is the archive of record. Say whether the export route is documented as public and
  stable, and whether the dataset has a DOI or a data version.
- **Inputs:** volunteer observer and station counts in each country covered (reported as the United States, Canada,
  Puerto Rico, the U.S. Virgin Islands and the Bahamas) and how they have changed; the gauge observers use; how reports
  are entered; how often the data are updated; which values are direct measurements and which derived (such as
  multi-day accumulations and summaries).
- **Organizations:** what the Colorado Climate Center at Colorado State University, the sponsors (NOAA and NSF are
  named), state and regional coordinators, and documented users such as NWS river forecasting and the METplus
  verification software each do: produce, host, use or pay for it.

For each finding, say whether it supports or contradicts RRS-1 "two or more geographically independent copies", D-2
"storage is a single point of failure", DIRS-3 "depends on external data feeds" or DIRS-4 "needs outside processing
infrastructure". RRS-1 is worded as a strength and the others as risks, so "supports" means evidence for the statement
as worded. Leave quality control, people, funding amounts and recent developments to later runs. Use CoCoRaHS's own
pages ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** CoCoRaHS's hosts and access points with URLs, kind and the archive of record, and whether the
export route is public and stable; observer and station counts over time by country where published; the gauge, the
report-entry system and the update schedule; the organizations and their roles, including documented users; and each
finding tagged RRS-1, D-2, DIRS-3 or DIRS-4 with a supports or contradicts stance. Expect a standard-tier run.

**What changed and why:**
- **Kept standard tier.** "Cuts or threats" became "recent developments".
- **Candidates, not facts.** The data.cocorahs.org export details, the countries covered and the users (NWS river
  forecasting, METplus) come from the metadata file, a ChatGPT answer, so they are listed to check. The ViewData
  finding (no formats, API, DOI or version stated) is folded into the DOI and version question.
- **Built on earlier runs.** The 40% GHCN-Daily share and the 28,000 volunteers are named with their runs. The 2,139
  station IDs with 2025 data but none in 2026 are left to Part 5, which owns station counts as an input.
- **Stance on each finding.** RRS-1 is a strength and the other three are risks, so the question says what "supports"
  means.
- **P-4** is listed as fed by this part but has no tag in your draft; Part 3 tags it, so I left it out here.
- **Cut** the answer tables, the CC BY 4.0 licence note (Part 2's FAIR rating covers it) and the "what kind of
  dataset" prompt; the skill sets its own format.
- **Limits:** 30 minutes and 240,000 tokens, as in your draft.

**How to reuse:** run first of CoCoRaHS's six runs, in its own session in this project. Parts 2–5 and the A2 data-site
run read its record; the A2 run and Part 4 start from its host list.
