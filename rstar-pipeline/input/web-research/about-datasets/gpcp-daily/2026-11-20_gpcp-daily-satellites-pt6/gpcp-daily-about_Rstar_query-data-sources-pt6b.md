# About GPCP Daily Data Sources R* Query for Claude

About dataset = GPCP daily data sources

## Query to refine

for GPCP precipitation data, what is the source of the data from rain gauges that goes into the GPCP dataset? How many rain gauge stations are there in the US that contribute to the GPCP dataset?

what are the names of all the satellites used in the GPCP dataset and what is their temporal range?

## ChatGPT query

### About rain gauges used in dataset

1. What is the primary source of rain gauge precipitation data used in the Global Precipitation Climatology Project (GPCP) dataset?
2. Which organizations or meteorological agencies collect and provide the rain gauge observations incorporated into GPCP?
3. How are rain gauge observations collected, quality-controlled, and processed before being integrated into the GPCP dataset?
4. How many rain gauge stations worldwide contribute precipitation observations to the GPCP dataset?
5. Specifically, how many rain gauge stations located in the United States contribute data to GPCP?
6. Where can the station-level information, including station locations, identifiers, and data sources, be accessed or verified?

### About satellite data used in dataset

1. What are the names of all satellites used to generate the Global Precipitation Climatology Project (GPCP) precipitation dataset?
2. Which satellite missions and sensors have contributed precipitation observations to the GPCP dataset since its inception?
3. What is the temporal coverage (start and end dates) of each satellite's contribution to the GPCP dataset?
4. During which years was each satellite operational and providing precipitation measurements?
5. Were multiple satellites used simultaneously, and how did their periods of operation overlap?
6. Can you provide a comprehensive table listing each satellite, its onboard precipitation sensor, its data contribution period, and relevant references or official documentation?

## Claude web research skill query

### Run 1: rain gauges

/my:broad-web-research

Using the earlier runs' records on what GPCP Daily (Global Precipitation Climatology Project daily precipitation) is made from and on its inputs (in web_search_results/), where do the rain-gauge data in GPCP Daily come from, and how many gauge stations contribute, worldwide and in the United States? Also use the earlier records on GHCN-Daily and NOAA's rain-gauge networks.

- **Scope:** both families, 1DD V1.3 and V3.x Daily. Gauges reach them only through the GPCP Monthly they are scaled to, which uses DWD's GPCC analyses. Say which GPCC products and versions feed which GPCP version and years.
- **Providers:** who supplies GPCC's gauges (national weather services, GTS SYNOP/CLIMAT reports, other collections), and which US networks reach it and by what route. Check GHCN-Daily, ASOS/SYNOP and COOP as candidates, without assuming any is used.
- **Counts:** worldwide and US stations, with the product, month or year each figure applies to, and how the count has changed over time. Where no count is published, say so and name the GPCC file or field that would give one; don't download large data files.
- **Processing:** in brief, how GPCC quality-controls and grids the gauges, and how GPCP combines them with the satellite estimates.
- **Station-level information:** where station locations, identifiers and sources can be seen, and whether they are public or restricted.

Use GPCC, DWD and GPCP documents over secondary accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

### Run 2: satellites

/my:broad-web-research

Using the earlier runs' records on GPCP Daily (Global Precipitation Climatology Project daily precipitation) and its inputs, and the record on the satellites behind PERSIANN-CDR Daily (in web_search_results/), which satellites and sensors supply data to GPCP Daily, and over what dates did each contribute?

- **Scope:** both families, 1DD V1.3 and V3.x Daily. Count a satellite whether it enters directly or through an input: the GPCP Monthly the daily is scaled to, IMERG, CPC's merged infrared or GridSat-B1. Say which route each takes.
- **Candidates:** check these without assuming any is used: SSM/I and SSMIS on DMSP F08–F19; TOVS, AVHRR, AMSU and MHS on NOAA polar orbiters and MetOp; AIRS and AMSR-E on Aqua; TRMM; GPM Core; GCOM-W1; ATMS on Suomi NPP and NOAA-20/-21; geostationary GOES, Meteosat, GMS/MTSAT/Himawari and FY-2.
- **For each satellite:** its precipitation-relevant sensor, the route, and the first and last dates it contributed to GPCP Daily, or "to present". Give its operational life only where it differs from those dates. Say where a document lists satellites without dates.
- **Overlaps:** which satellites were used at the same time, and where only one satellite of a kind was used for a period.
- Explain conflicting dates between documents.

Use the algorithm documents, file metadata and mission documents over secondary accounts. With a time limit of 50 minutes and a token ceiling of 400,000.

## Claude comments about the rewritten query

**What you'll get:**
- **Run 1 (gauges):** the gauge chain into GPCP Daily: which GPCC products feed which GPCP version, who supplies GPCC, which US networks reach it, station counts worldwide and in the US with their dates (or a plain "not published" and where a count could come from), a short account of the QC and the merge, and where station lists can be seen. Expect a standard-tier run.
- **Run 2 (satellites):** a list of every satellite and sensor behind GPCP Daily, each with its route in, its first and last dates in the record, and the overlaps. Expect a deep-tier run, because it covers well over 15 satellites with dates for each.

**What I changed from your draft:**
- **Split into two runs:** gauges and satellites live in different documents (GPCC and DWD versus algorithm documents, file metadata and mission pages), and the satellite list alone is long enough to need a full deep budget. Neither run needs the other, so they can go in either order.
- **"Gauges enter only through the monthly" stated up front:** Part 1 and Part 5 found that GPCP Daily uses no gauges directly; they reach it through the GPCP Monthly and GPCC. So the gauge run asks about GPCC's gauges, and which GPCC version feeds which GPCP version.
- **US count made answerable:** GPCC may publish no US figure. The run says so and names the file or field that would give one, instead of downloading large GPCC files. If you want the count computed, that's a separate step.
- **Satellites by route:** "all satellites used" depends on how far up the chain you count. The question counts satellites inside the inputs (GPCP Monthly, IMERG, CPC infrared, GridSat-B1) and asks for the route of each, so you can filter later. IMERG alone brings in the GPM constellation from 2000 on (V3.x only).
- **Dates of contribution, not mission life:** your draft asked for both. The run gives the dates in GPCP Daily and adds mission life only where it differs, which keeps the list readable.
- **Your table request:** dropped as a layout (the skill uses its own answer format), but the per-satellite items it asked for are kept.
- **Candidates, not facts:** the candidate lists say "without assuming any is used".
- **Built on earlier runs:** GPCP Parts 1 and 5 list the inputs and their satellites; the PERSIANN-CDR satellites run read GridSat-B1 file headers for about 36 geostationary satellites, and its GPCP satellites (DMSP F08/F11/F13/F17, TOVS, AIRS, AVHRR); the GHCN-D and rain-gauge runs cover US networks. The questions name those records so the runs spend their time on what's missing.

**Limits:** Run 1 has 30 minutes and 240,000 tokens. Run 2 has 50 minutes and 400,000, because the PERSIANN-CDR satellites run used 33 minutes and 350,000 tokens on a shorter list. To save weekly usage, Run 2 could use 40 minutes and 320,000, leaning on that run's record; the IMERG constellation is the part most likely to be thin.

**One-run version:** join both questions, keeping the gauge and satellite bullets, with a time limit of 50 minutes and a token ceiling of 400,000. It gives up depth on the gauges: the satellite list would take most of the budget, and the US count and station-list access would get the least.

**Reuse:** run both in this project so they can read the earlier records in `web_search_results/`. Don't add "Don't use earlier runs."; both depend on them. The two questions are in one file; you can split it into pt6a and pt6b if you want one query per file.
