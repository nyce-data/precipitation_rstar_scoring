# A2 NASA GES DISC and PPS Repository resilience R* Query for Claude

About repository = NASA GES DISC and NASA PPS, repository resilience (shared run for the datasets they serve)

Written 2026-11-23 from `general_archive_queries/A2_Rstar_query_template-repository-resilience.md` and the IMERG Late Run
and GPCP Daily coverage checks (`datasets-gap-queries/` in precipitation_rstar_scoring). Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session in this
project.

**Two repositories in one run.** Both sit at NASA Goddard and serve the same datasets, so one run covers both:
- **GES DISC** (Goddard Earth Sciences Data and Information Services Center) is a shared archive: the archive of
  record for IMERG and the host of GPCP V3.x.
- **PPS** (Precipitation Processing System) is the producer's own data site: it makes IMERG and serves the Late Run in
  near real time.

**Datasets that cite this run:** IMERG Late Run and GPCP Daily (V3.x).

**Subcategories this run answers:** RRS-1, RRS-2, RRS-3 and RRS-5, plus storage for D-2 and access systems for D-3.

**No A1 threats run is planned for now.** NASA's Earth Science Data Systems budget, the proposed DAAC consolidation and
Goddard's staff losses are already in IMERG's funding-pt4 and news-pt5 runs and the NASA satellite run.

## Query to refine

Using the earlier runs' records in web_search_results/ on IMERG Late Run (2026-11-20_imerg-late-run-about-pt1,
2026-11-21_imerg-late-run-formats-people-pt3, 2026-11-21_imerg-late-run-funding-pt4, 2026-11-21_imerg-late-run-news-pt5
and 2026-11-21_imerg-late-run-inputs-pt6), on GPCP Daily (2026-11-19_gpcp-daily-about-pt1 and
2026-11-20_gpcp-daily-funding-news-pt4) and on NASA's satellite precipitation (2026-11-18_nasa-satellite-precip-threats),
how resilient are NASA's GES DISC and the Precipitation Processing System (PPS) as homes for data? Add to what those runs
found rather than repeating it; they cover NASA's budget, the DAAC consolidation plan, Goddard's staff losses and GES
DISC's move to the cloud.

- **Integrity checks (RRS-2, never searched):** the fixity or checksum checks that NASA's ESDIS project, GES DISC and
  PPS run, which algorithm and how often; whether GES DISC is certified by CoreTrustSeal or ISO 16363, or is a World Data
  System member; what NASA's Earth Science data management policy requires; whether Earthdata Cloud verifies stored
  copies.
- **Disaster recovery (RRS-3, never searched):** ESDIS's, GES DISC's and PPS's continuity-of-operations or disaster
  recovery plans, when each was last tested, and with what results; what NASA OIG report IG-26-005 and GAO-26-108556
  found about NASA's data systems; whether PPS's near-real-time system has a backup site.
- **Redundancy (RRS-1):** now that GES DISC's on-premises HTTPS, OPeNDAP and THREDDS services ended in 2026, whether any
  copy besides Earthdata Cloud (AWS us-west-2) exists; whether Earthdata Cloud replicates to a second region or keeps a
  backup; what PPS keeps in its own archive and for how long; whether the GES DISC and PPS copies are checked against
  each other.
- **Storage and access (D-2, D-3):** GES DISC's and PPS's storage design; the contracts and staff that operate them
  (EED-3 80GSFC21CA001, Raytheon, extended to January 31, 2027, and its successor "ESDIS Next"); the dependence on
  Earthdata Login.
- **Track record (RRS-5):** GES DISC's holdings and latency before and after the 43-day 2025 shutdown, the 2026 cloud
  migration and the October 28–30, 2026 ingest pause (ESDIS metrics are a lead); PPS's planned 14-hour near-real-time
  shutdown on January 20, 2026; any earlier disruptions and any data loss.

The statements are worded as strengths, so "supports" means evidence of resilience. For each finding, say which
repository it is about and whether it supports or contradicts RRS-1 "two or more geographically independent sites hold
verified copies", RRS-2 "checksum checks quarterly or more often", RRS-3 "disaster recovery plan tested in the past 2
years with documented results", RRS-5 "has survived a major disruption without data loss", D-2 "storage at end of life
or a single point of failure" or D-3 "access infrastructure fragile or unfunded". Say plainly when nothing is published.
Leave NASA's budget, cuts and news to the earlier runs. Use NASA's, ESDIS's, OIG's, GAO's and CoreTrustSeal's own
documents ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** This run asks about practice and track record, not threats.
- **Already found, don't search again (from the IMERG and GPCP coverage checks):**
  - GES DISC is the archive of record for IMERG, with the DOIs; it serves the half-hourly HDF5 and daily netCDF files,
    OPeNDAP, Harmony and Giovanni, and derives the daily file itself (IMERG pt1, pt3);
  - Earthdata Cloud is NASA's own copy (`gesdisc-cumulus-prod-protected`, AWS us-west-2) (IMERG pt1, pt3);
  - on-premises THREDDS ended July 31, 2026 and HTTPS by September 30, 2026, so the cloud is now GES DISC's only route
    (IMERG pt5);
  - PPS serves the Late Run from `jsimpsonhttps.pps.eosdis.nasa.gov` and GeoTIFFs with their own DOIs, and keeps Late
    files only until the next algorithm version replaces them (IMERG pt1, pt3);
  - GES DISC and PPS kept running through the 2025 shutdown; no outage notice was found (IMERG pt4, pt5);
  - GES DISC hosts GPCP V3.2 and V3.3 (DATA305, DATA307), with Earthdata Login required (GPCP pt1).
- **Leads:** the ESDIS weekly and annual metrics; the ESDIS Project pages and its data management plans; the ESD town
  hall of December 2025 ("Risks associated with data system consolidation"); the GES DISC and PPS help desks.
- **If the run must be smaller,** split it in two: GES DISC and PPS, each at 30 minutes and 240,000 tokens.

### What the answer should give

- For each repository: the fixity or checksum practice, certification, and whether a disaster recovery plan exists
  and was tested, or a plain statement that none was found.
- A table of copies: where each is, how long it is kept, and whether it is checked against the others.
- The storage design and the contracts and staff that run each repository.
- A dated table of past disruptions: holdings and latency before and after, and any data loss.
- A repository name, subcategory tag and stance on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ on IMERG Late Run (the 2026-11-20 and 2026-11-21
`imerg-late-run-*` folders), on GPCP Daily (2026-11-19_gpcp-daily-about-pt1 and 2026-11-20_gpcp-daily-funding-news-pt4)
and on NASA's satellite precipitation (2026-11-18_nasa-satellite-precip-threats), how resilient are NASA's GES DISC (the
archive of record for IMERG and host of GPCP V3.x) and the Precipitation Processing System (PPS, which makes IMERG and
serves the Late Run) as homes for data? Build on those runs, which cover NASA's budget, staffing and GES DISC's move to
Earthdata Cloud, rather than repeating them. For each repository:

- Integrity (RRS-2): fixity or checksum checks by ESDIS, GES DISC and PPS, the algorithm and how often; CoreTrustSeal,
  ISO 16363 or World Data System status; what NASA's Earth science data policy requires; whether Earthdata Cloud
  verifies stored copies.
- Recovery (RRS-3): continuity or disaster recovery plans, when last tested and with what results; what NASA OIG's
  IG-26-005 and GAO-26-108556 found on data systems; whether PPS's near-real-time system has a backup site.
- Copies (RRS-1): with GES DISC's on-premises services ended in 2026, whether any copy exists besides Earthdata Cloud
  (AWS us-west-2) or in a second region; what PPS keeps and for how long; whether the two are checked against each other.
- Storage and access (D-2, D-3): the storage design, the contracts and staff that run them (EED-3 to January 31, 2027,
  and ESDIS Next), and the dependence on Earthdata Login.
- Track record (RRS-5): holdings and latency around the 2025 shutdown, the 2026 cloud migration, the October 28–30, 2026
  ingest pause and PPS's January 20, 2026 outage, and any data loss.

The RRS statements are worded as strengths and the D statements as risks, so "supports" means evidence for the
statement as worded. Tag each finding with its repository and say whether it supports or contradicts RRS-1 "two or more
geographically independent sites hold verified copies", RRS-2 "checksum checks quarterly or more often", RRS-3 "disaster
recovery plan tested in the past 2 years with documented results", RRS-5 "has survived a major disruption without data
loss", D-2 "storage at end of life or a single point of failure" or D-3 "access infrastructure fragile or unfunded". Say
plainly when nothing is published. Use NASA's, ESDIS's, OIG's, GAO's and CoreTrustSeal's own documents ahead of news.
With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** for GES DISC and PPS separately, findings tagged with a subcategory and stance: integrity checks
and certification, recovery plans and tests, where the copies are and how long PPS keeps them, the storage design and
contracts, and a dated record of disruptions, with "nothing published" where that holds.

**What changed and why:**
- **"Supports" for D-2 and D-3 is now defined.** The draft said all the statements are worded as strengths, but D-2
  and D-3 are worded as risks, so "supports D-2" would have been ambiguous.
- **Wording kept off cuts.** I dropped "DAAC consolidation" and "staff losses" from the question so the skill keeps
  the standard tier; the earlier runs already hold them.
- **IMERG runs named by pattern** instead of five folder names; the run reads the whole folder anyway.
- **Cut** the already-found list, the leads and the answer tables. The facts the question relies on (us-west-2, the
  2026 shutdown of on-premises services, EED-3's end date) are kept in a few words.
- **Limits kept** at 40/320k: two repositories, six subcategories.

**How to reuse:** run it in its own session in this project; every run it needs exists. If you need smaller runs, split
it into two: copy the question once for GES DISC and once for PPS, drop the other repository's items, and set 30 minutes
and 240,000 tokens for each.
