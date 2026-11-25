# GPCP Daily gaps Part 7: People and production R* Query for Claude

About dataset = GPCP Daily Part 7, gaps in People risk (P-1 to P-4), calibration (DIRS-1), outside processing
(DIRS-4), alternatives (DIRS-5) and copies (RRS-1)

Written 2026-11-23 from [gpcp-daily_coverage-gaps.md](../gpcp-daily_coverage-gaps.md), a coverage check of GPCP Daily's
six runs. Rewrite this with `/my:rewrite-research-query` (see
[supplemental-queries-run-sheet.md](../supplemental-queries-run-sheet.md)), then run the rewritten query with
`/my:broad-web-research` in its own session. Repository resilience for NCEI and NASA GES DISC is in the shared A2 runs,
not here.

## Query to refine

Using the earlier runs' records on GPCP Daily (Global Precipitation Climatology Project daily precipitation)
(2026-11-19_gpcp-daily-about-pt1, 2026-11-20_gpcp-daily-qc-formats-pt2, 2026-11-20_gpcp-daily-people-pt3,
2026-11-20_gpcp-daily-funding-news-pt4, 2026-11-20_gpcp-daily-inputs-pt5 and 2026-11-20_gpcp-daily-satellites-pt6), all
in web_search_results/, who are the people critical to producing GPCP Daily now, how close is each to retirement, who
runs each version's production and on what computers, what does its calibration rest on today, and which of its copies
are current? Add to what those runs found rather than repeating it.

- **People (P-1, P-2, P-4):** start from Robert Adler (UMD/ESSIC, PI of both NCEI CDRs), George Huffman (NASA GSFC Code
  612, lead developer), Ali Behrangi (University of Arizona, MEaSUREs PI, V4 lead), David Bolvin and Eric Nelkin (SSAI at
  Code 612), Guojun Gu (UMD), and Jian-Jian Wang and Mathew Sapiano (UMD, status unknown), confirming each by affiliation
  and GPCP co-authorship. For each: current role and whether still active on GPCP; ORCID iD; earliest publication year
  (say from which source); first year on GPCP; estimated age (earliest publication year minus 25–30); and, for federal
  staff, whether likely eligible to retire within 2 years under FERS (56–57 with 30 years' service, 60 with 20, 62 with
  5). Mark estimates as estimates. Also: team size, and any written succession or knowledge-transfer plan, including
  what the NOAA CDR Program's transition from research to operations required.
- **Who runs production (P-3, P-4, DIRS-4):** who computes NCEI's V3.3 CDR copy (UMD or Goddard; two official sources
  disagree); who runs V1.3 and on what machines; where V3.x is computed at NASA (Code 612 workstations or NCCS); which
  contract pays Bolvin and Nelkin after Goddard's atmospheres support moved from SSAI to STC; whether the V3.x code is
  shared on request; when V1.3 will stop and when V3.3 production restarted after its pause.
- **Funding route (D-1):** the number and end date of Behrangi's 2022 MEaSUREs award (NNH22ZDA001N A.27, about $3M),
  and GPCP's share of the CISESS agreement (NA24NESX432C0001), saying so where no share is published.
- **Calibration (DIRS-1):** which SSMIS feed 1DD V1.3 uses since the RSS SSM/I–SSMIS CDR's final record ended in 2023
  and since FNMOC's October 1, 2026 change; who maintains the intercalibration behind it; whether NASA has a calibration
  plan for after GPM (GMI and DPR are V3.3's reference through IMERG).
- **Alternatives (DIRS-5):** what 1DD would do if DMSP F17 or Aqua AIRS stopped (it has relied on F17 alone since 2009
  and on AIRS since 2003); which datasets could replace GPCP Daily as a whole, with coverage and status.
- **Copies (RRS-1):** which version the NODD buckets (`noaa-cdr-precip-gpcp-daily-pds` on AWS, and Google's
  `noaa-cdr-precip-gpcp-daily`) hold, and whether they are current; whether the NSF NCAR GDEX copies (d728007, d728009),
  the Copernicus CDS copy, the GSFC backup FTP, obs4MIPs/ESGF, Earth Engine and gpcp.umd.edu copies exist and are
  current.

For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel
retirement-eligible within 2 years", P-3 "critical knowledge undocumented", P-4 "a single person is a point of
failure", DIRS-1 "depends on an external calibration service that could be disrupted", DIRS-4 "needs outside
processing infrastructure", DIRS-5 "no alternative supplier" or RRS-1 "two or more geographically independent sites
hold verified copies" (RRS-1 is a strength, so "supports" means resilience). Say so where nothing is published. Leave
cuts and news to the earlier runs. Use NOAA's, NASA's and the universities' own pages, papers, and ORCID or OpenAlex
records ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** No cuts or threats are asked for, so the skill shouldn't pick its deep tier. The funding
  and news are already in pt4, and the input threats are in pt5 and pt6.
- **Retirement rules differ by employer.** FERS applies to federal staff (Huffman at NASA). For university and
  contractor staff (UMD, University of Arizona, SSAI), give the estimated age and say no federal rule applies.
- **Where to find ORCID iDs and earliest publication years:** ORCID (orcid.org, pub.orcid.org), OpenAlex
  (api.openalex.org), Google Scholar, Crossref, NASA's NTRS. ORCID records are often incomplete; check one other source.
- **Already found, don't search again (from the coverage check):**
  - about 8 active core people; production was "a consortium of individual scientists" until 2016, then formal under
    the NOAA CDR Program (pt3);
  - Adler spent 35 years at GSFC before 2008; Wang and Sapiano are absent from the 2025–26 author lists (pt3);
  - V1.3 code is public as a 2017 tarball "for reference only", with no licence file; V3.x code is not published (pt2);
  - the calibration chain: V1.3's IR threshold is matched each month to SSM/I–SSMIS GPROF rain frequency and scaled to
    Monthly V2.3 (GPCC gauges); V3.3 is calibrated through IMERG to GMI and the DPR–GMI combined product, with TOVS and
    AIRS histogram-matched to IMERG and each day ratio-scaled to Monthly V3.3 (pt2, pt5, NASA satellite run);
  - the GridSat-B1 recalibration (HIRS ended in 2024, now VIIRS VGAC) paused V3.3 for more than a year (pt5);
  - MEaSUREs V3.2 award 80NSSC19M0006; CISESS agreements NA19NES4320002 and NA24NESX432C0001 (pt4).
- **If the run must be smaller,** drop the copies bullet; the shared A2 runs cover NCEI's and GES DISC's own copies.

### What the answer should give

- A table of people: role, employer, active or not, ORCID iD, earliest publication year and its source, estimated age,
  and a likely-eligible flag where a rule applies.
- Who runs each version's production, on what machines, and who pays them.
- The current calibration feed for 1DD, and any post-GPM calibration plan.
- A 1DD contingency, if any, and substitute datasets.
- A table of copies: version held, last date, and whether current.
- A stance for each finding against the subcategory statements.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
