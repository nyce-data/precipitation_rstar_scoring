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
relate. Where is it stored and served: the CoCoRaHS data site (cocorahs.org ViewData, the Station Data Explorer at
dex.cocorahs.org, the Water Year Summaries at wys.cocorahs.org and the maps), any bulk download, API or web service, and
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

(not written yet)

## Claude comments about the rewritten query

(not written yet)
