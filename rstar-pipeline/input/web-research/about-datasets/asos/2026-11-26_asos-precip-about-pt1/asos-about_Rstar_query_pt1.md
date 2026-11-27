# About ASOS Part 1: Overview R* Query for Claude

About dataset = ASOS Part 1, overview: products, hosts, sensors and the organizations behind them

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt1_overview.md` and the metadata file
`rstar-pipeline/input/dataset-metadata/markdown/asos_dataset-metadata.md` in precipitation_rstar_scoring. Rewrite this
with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session.
Suggested run folder: `<date>_asos-about-pt1`.

**Scope (user's choice, 2026-11-25):** the ASOS network's precipitation observations, scored as one dataset. Its
products (1-minute, 5-minute, hourly, daily and monthly summaries) are listed here with their status; none is scored
on its own.

**Subcategories this part feeds:** RRS-1 (copies and mirrors), D-2 (who serves it), DIRS-3 (inputs and data flow),
DIRS-4 (outside groups), P-4 (which groups do the work).

**Run order:** first of ASOS's five runs. Parts 2, 3, 4 and 5 all use this run's record.

## Query to refine

Research the ASOS (Automated Surface Observing System) network's precipitation observations as one dataset, taking
each of its products in turn: the 1-minute data (NCEI DSI 3285, pages 1 and 2), the 5-minute data (DSI 6401), the
hourly and special METAR/SPECI observations as archived at NOAA NCEI (formerly the Integrated Surface Database and
Global Hourly, now GHCNh), and the daily and monthly climate summaries (CF6/F-6 and DSM). Mention AWOS only to say how
it differs. For each product, give its period of record, how often it is updated, whether it is current or has been
replaced (and by what, when), and where it is stored and served: NCEI's pages and bulk directories, the NOAA Open Data
Dissemination copies on AWS, the Iowa Environmental Mesonet, NWS and FAA real-time feeds, and any other place that
holds a copy, with URLs, which one is the archive of record, whether each copy is current, and whether each is a
shared archive, the operators' own data site, or a copy. What kind of dataset is it (one network of automated stations
with a standard sensor suite, operated by three agencies)? What are its inputs: how many stations there are by
operating agency, which precipitation sensors each uses (heated tipping bucket, All Weather Precipitation Accumulation
Gauge, freezing-rain and present-weather sensors) and how many stations have each, the station processor, how
observations travel from the site to NCEI, and where human observers augment or back up the automated reports? Which
values are measured directly and which are derived (such as precipitation type, hourly and daily totals)? Which
organizations operate, maintain, process, host and pay for it, and what does each do, including NWS, FAA, DoD, NCEI,
contractors and outside groups? Leave quality control, people, funding amounts, and any cuts or threats to later parts.
Tag findings with RRS-1 "two or more geographically independent copies", D-2 "storage is a single point of failure",
DIRS-3 "depends on external data feeds" or DIRS-4 "needs outside processing infrastructure". With a time limit of 30
minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats, layoffs or news; Part 4 covers them. "Replaced" and
  "current" are product facts, not threats.
- **What kind of dataset it is:** a single operational network with one standard sensor suite at about 900–950 sites,
  not a compilation of networks or a satellite blend. The inputs are the sensors, the station processor, the
  communications path and any human augmentation.
- **Already known (metadata file, a ChatGPT answer, not yet checked):**
  - NCEI is the archive; there is no DOI for the whole network, only NCEI dataset identifiers (DSI 6401 for 5-minute,
    DSI 3285 for 1-minute). The 5-minute metadata gives July 1, 1996 to present; the 1-minute pages, June 1, 1998 to
    present;
  - access points it lists: NCEI's ASOS/AWOS product page, Global Hourly search, the `noaa-global-hourly-pds` and
    `noaa-isd-pds` buckets on AWS, NCEI's 1-minute and 5-minute directories, and IEM's ASOS and 1-minute download pages;
  - precipitation sensors: heated tipping bucket (HTB), All Weather Precipitation Accumulation Gauge (AWPAG, a heated
    weighing gauge), freezing-rain sensor; equipment differs by station.
- **Already known (earlier runs in web_search_results/):**
  - NCEI says ISD "reached end of life on August 29" 2025, replaced by GHCNh, with SSOD replacing GSOD
    (`2026-11-21_ghcn-daily-sources-pt5`). So the metadata's ISD and Global Hourly links may now be frozen copies: ask
    which hosts are still updated;
  - NWS maintains all units under a tri-agency agreement: 308 NWS, 570 FAA and 78 DoD units, about 950 sites
    (`2026-11-18_noaa-rain-gauge-threats`);
  - ASOS daily data enter GHCN-Daily (source flag W, and CF6 since v3.34), about 1.7% of GHCN-Daily's entries
    (`2026-11-21_ghcn-daily-sources-pt5`).

  Ask the run to build on these, not repeat them.
- **Hosts list.** NCEI already has its A1 (`2026-11-17_noaa-ncei-threats`) and A2 (`2026-11-23_A2_Rstar_query-noaa_ncei`)
  runs. AWS buckets and IEM are copies under `rstar-pipeline/processing/research-queries/archive-query-plan.md`, so
  they get no repository run; this run checks whether each is current and who runs it (RRS-1). If the run finds that
  NWS, FAA or IEM keeps a full archive of its own, say so: that would change the repository runs needed.
- **Organizations, not people.** Named people, staff counts and ages are Part 3's job.

### What the answer should give

- A table of products: period of record, update frequency, status (current or replaced, and by what).
- A table of hosts and access points per product, with URLs, which is the archive of record, the kind of each, and
  whether each is current.
- Station counts by agency, and the precipitation sensors with how many stations have each.
- The data path from the station to NCEI, and where human observers augment it.
- A table of organizations and their roles.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

What are the ASOS (Automated Surface Observing System) network's precipitation observations, taken as one dataset:
which products carry them, where is each stored and served, what goes into them, and which organizations make them?
Mention AWOS only to say how it differs. Build on the earlier runs' records in web_search_results/: ISD was replaced
by GHCNh on August 29, 2025 (2026-11-21_ghcn-daily-sources-pt5), and NWS maintains about 950 units under a tri-agency
agreement (2026-11-18_noaa-rain-gauge-threats).

- **Products:** the 1-minute data (NCEI DSI 3285, pages 1 and 2), the 5-minute data (DSI 6401), the hourly and special
  METAR/SPECI observations as NCEI archives them (formerly ISD and Global Hourly, now GHCNh), and the daily and monthly
  summaries (CF6/F-6 and DSM). For each: period of record, update frequency, and whether it is current or was replaced
  (by what, when).
- **Hosts:** for each product, every place that holds or serves a copy, with URLs. Check these without assuming each is
  current: NCEI's pages and bulk directories, the NOAA Open Data Dissemination buckets on AWS (`noaa-global-hourly-pds`,
  `noaa-isd-pds`), the Iowa Environmental Mesonet, and NWS and FAA real-time feeds. For each: a shared archive, the
  operators' own data site or a copy; whether it is still updated; and which is the archive of record. Say whether NWS,
  FAA or IEM keeps a full archive of its own.
- **Inputs:** station counts by operating agency; the precipitation sensors (heated tipping bucket, All Weather
  Precipitation Accumulation Gauge, freezing-rain and present-weather sensors) and how many stations have each; the
  station processor; how observations travel from the site to NCEI; where human observers augment or back up the
  reports; which values are measured and which derived (such as precipitation type and hourly and daily totals).
- **Organizations:** what NWS, FAA, DoD, NCEI, contractors and outside groups each do: operate, maintain, process, host
  or pay for it.

For each finding, say whether it supports or contradicts RRS-1 "two or more geographically independent copies", D-2
"storage is a single point of failure", DIRS-3 "depends on external data feeds" or DIRS-4 "needs outside processing
infrastructure". RRS-1 is worded as a strength and the others as risks, so "supports" means evidence for the statement
as worded. Leave quality control, people, funding amounts and recent developments to later runs. Use NCEI's, NWS's and
FAA's own documents ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** each ASOS product with its period of record, update frequency and status; every host and access
point per product with URLs, kind, whether it is still updated and the archive of record; station counts by agency and
the precipitation sensors with how many stations have each; the data path from site to NCEI and where observers step
in; the organizations and their roles; and each finding tagged RRS-1, D-2, DIRS-3 or DIRS-4 with a supports or
contradicts stance. Expect a standard-tier run.

**What changed and why:**
- **Kept standard tier.** "Cuts or threats" became "recent developments". ISD's end is stated as a product fact
  ("replaced by GHCNh"), not as a threat.
- **Built on earlier runs.** ISD's replacement and the tri-agency agreement are named with their runs, so this run asks
  which hosts are still updated rather than finding those facts again. The 308/570/78 unit split and the 1.7%
  GHCN-Daily share are in those records; I didn't restate them.
- **Hosts as candidates.** The metadata file's access points (a ChatGPT answer, written before ISD ended) are listed
  "without assuming each is current", since the ISD and Global Hourly links may now be frozen copies.
- **Full archives asked for.** If NWS, FAA or IEM keeps a full archive of its own, the repository runs needed would
  change; the question asks.
- **Stance on each finding.** RRS-1 is a strength and the other three are risks, so the question says what "supports"
  means.
- **P-4** is listed as fed by this part but has no tag in your draft; Part 3 tags it, so I left it out here.
- **Cut** the answer tables and the "what kind of dataset" prompt (the inputs bullet shows it is one network with one
  sensor suite).
- **Limits:** 30 minutes and 240,000 tokens, as in your draft. Five products with several hosts each is a lot for one
  standard run; if it ends with hosts unchecked, a 20-minute follow-up on hosts alone would close them.

**How to reuse:** run first, in its own session in this project. Parts 2, 3, 4 and 5 read its record. After it runs,
fix the metadata file's ISD and Global Hourly entries (see the run sheet).
