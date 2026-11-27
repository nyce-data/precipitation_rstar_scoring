# About USCRN Daily Part 1: Overview R* Query for Claude

About dataset = USCRN Daily Part 1, overview: hosts, stations, instruments and producers

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt1_overview.md` and the metadata file
`rstar-pipeline/input/dataset-metadata/markdown/uscrn-daily_dataset-metadata.md` in precipitation_rstar_scoring.
Rewrite this with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own
session. Suggested run folder: `<date>_uscrn-daily-about-pt1`.

**Subcategories this part feeds:** RRS-1 (copies and mirrors), D-2 (who serves it), DIRS-3 (inputs and data flow),
DIRS-4 (outside groups), P-4 (which groups do the work).

**Run order:** first of USCRN Daily's five runs. Parts 2, 3, 4 and 5 all use this run's record.

## Query to refine

Research the USCRN Daily (U.S. Climate Reference Network daily01 product) dataset, current version only; mention the
sub-hourly, hourly and monthly USCRN products, the U.S. Regional Climate Reference Network and the soil-moisture
measurements only to say how they differ. Where is it stored and served: NCEI's `pub/data/uscrn/products/daily01/`
directory and its snapshots, the USCRN data portal, any NOAA Open Data Dissemination cloud copy, the Copernicus Climate
Data Store, GHCN-Daily and GHCNh where they carry USCRN stations, the Air Resources Laboratory's own pages, and every
other place that holds a copy, with URLs, which one is the archive of record, whether each copy is current, and
whether each is a shared archive, the producer's own data site, or a copy? What kind of dataset is it (one reference
network of identical stations with redundant sensors)? What are its inputs: how many stations there are in the
contiguous US, Alaska and Hawaii and how that has changed, the precipitation instruments at each (the weighing gauge
and its shield, the wetness sensor, the auxiliary tipping bucket), the datalogger, how observations travel from the
station to NCEI, and how the daily values are computed from 5-minute data? Which values are measured directly and
which are derived? Which organizations produce, maintain, process, host and pay for it, and what does each do,
including NCEI, the Air Resources Laboratory's Atmospheric Turbulence and Diffusion Division, cooperative institutes,
the site hosts and any contractors? Leave quality control, people, funding amounts, and any cuts or threats to later
parts. Tag findings with RRS-1 "two or more geographically independent copies", D-2 "storage is a single point of
failure", DIRS-3 "depends on external data feeds" or DIRS-4 "needs outside processing infrastructure". With a time
limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats, layoffs or news; Part 4 covers them.
- **What kind of dataset it is:** a single network of identical reference stations, not a compilation or a satellite
  blend. The inputs are the instruments, the datalogger, the transmission path and the station sites.
- **Already known (metadata file, a ChatGPT answer, not yet checked):**
  - no DOI for daily01; NCEI identifier `gov.noaa.ncdc:C00466` (its reference list also points at `C00546`; ask which
    is current). The DOI 10.1175/BAMS-D-12-00170 is a paper (Diamond et al. 2013), not the dataset;
  - record from November 15, 2000, updated daily; text files by station and year;
  - instruments: Geonor T-200B weighing gauge with three vibrating-wire sensors (primary), Vaisala DRD11A rain
    detector, Hydrological Services TB-3 tipping bucket (auxiliary, not quality-controlled);
  - NCEI curates and serves the data; ATDD operates the stations; Howard Diamond is named as program manager.
- **Already known (earlier runs in web_search_results/):** ATDD in Oak Ridge designed and built the stations and
  maintains them; 114 CONUS, 2 Hawaii and 25 Alaska stations, with NCEI saying 29 are being deployed in Alaska
  (`2026-11-18_noaa-rain-gauge-threats`); ARL finished a transmitter upgrade on 139 towers in 45 states on April 25,
  2026 (same run). Ask the run to build on these, and to say how the transmitter sends data (for example GOES DCS).
- **Hosts list.** NCEI already has its A1 (`2026-11-17_noaa-ncei-threats`) and A2 (`2026-11-23_A2_Rstar_query-noaa_ncei`)
  runs. Cloud copies and the Climate Data Store are copies under
  `rstar-pipeline/processing/research-queries/archive-query-plan.md`, so this run checks whether each is current and
  who runs it (RRS-1). If ATDD or ARL serves a full copy of its own, say so: that would need a repository run.
- **Organizations, not people.** Named people, staff counts and ages are Part 3's job.

### What the answer should give

- A table of hosts and access points, with URLs, which is the archive of record, the kind of each, and whether each is
  current.
- Station counts by region over time, and the instruments at each station.
- The data path from station to NCEI, how daily values are made, and the update schedule.
- A table of organizations and their roles.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

What is USCRN Daily (the U.S. Climate Reference Network's daily01 product), where is it stored and served, what goes
into it, and which organizations make it? Cover the current version only; mention the sub-hourly, hourly and monthly
USCRN products, the U.S. Regional Climate Reference Network and the soil-moisture measurements only to say how they
differ. Build on the earlier runs' records in web_search_results/, which already give ATDD's role, station counts and
the April 2026 transmitter upgrade (2026-11-18_noaa-rain-gauge-threats).

- **Hosts:** every place that holds or serves a copy, with URLs. Check these without assuming each holds one: NCEI's
  `pub/data/uscrn/products/daily01/` directory and its snapshots, the USCRN data portal, any NOAA Open Data
  Dissemination cloud copy, the Copernicus Climate Data Store, GHCN-Daily and GHCNh where they carry USCRN stations,
  and the Air Resources Laboratory's (ARL's) own pages. For each: a shared archive, the producer's own data site or a
  copy; whether it is current; and which is the archive of record. Say which NCEI identifier is current
  (`gov.noaa.ncdc:C00466` or `C00546`), whether daily01 has a DOI, and whether ARL or ATDD serves a full copy.
- **Inputs:** station counts in the contiguous US, Alaska and Hawaii and how they changed; the precipitation
  instruments at each (reported as a Geonor T-200B weighing gauge and its shield, a Vaisala DRD11A wetness sensor and
  an auxiliary TB-3 tipping bucket; confirm) and the datalogger; how observations travel from station to NCEI (for
  example GOES DCS); how daily values are computed from 5-minute data; which values are measured and which derived;
  the record's start and update schedule.
- **Organizations:** what NCEI, ARL's Atmospheric Turbulence and Diffusion Division (ATDD), cooperative institutes,
  site hosts and any contractors each do: produce, operate, process, host or pay for it.

For each finding, say whether it supports or contradicts RRS-1 "two or more geographically independent copies", D-2
"storage is a single point of failure", DIRS-3 "depends on external data feeds" or DIRS-4 "needs outside processing
infrastructure". RRS-1 is worded as a strength and the others as risks, so "supports" means evidence for the statement
as worded. Leave quality control, people, funding amounts and recent developments to later runs. Use NCEI's and ARL's
own documents ahead of secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** a list of USCRN Daily's hosts and access points with URLs, kind, currency and the archive of
record; station counts by region over time; the instruments, datalogger and data path to NCEI; how daily values are
made; the organizations and their roles; and each finding tagged RRS-1, D-2, DIRS-3 or DIRS-4 with a supports or
contradicts stance. Expect a standard-tier run.

**What changed and why:**
- **Kept standard tier.** "Cuts or threats" became "recent developments", so the wording doesn't push the run to
  deep; Part 4 covers them.
- **Candidates, not facts.** The hosts and the three precipitation instruments (from the metadata file, a ChatGPT
  answer) are listed to check, not assumed. The C00466/C00546 question and the "no DOI" claim are asked, not stated.
- **Built on earlier runs.** The rain-gauge run's ATDD role, 114 + 2 + 25 station counts and 139-tower upgrade are
  named by run, not restated in full; the run reads that record first. GOES DCS is given as the example data path.
- **Stance on each finding.** RRS-1 is a strength and the other three are risks, so the question says what
  "supports" means.
- **P-4** is listed as fed by this part but has no tag in your draft; the organizations' roles feed it, and Part 3
  tags it. I left it out of the tags.
- **Cut** the answer tables and the "what kind of dataset" prompt (the inputs bullet makes it plain it is one network
  of stations); the skill sets its own format.
- **Limits:** 30 minutes and 240,000 tokens, as in your draft.

**How to reuse:** run first, in its own session in this project. Parts 2, 3, 4 and 5 read its record. If it finds
that ARL or ATDD serves a full copy of its own, add an A2 run for that site before Part 4 (see the run sheet).
