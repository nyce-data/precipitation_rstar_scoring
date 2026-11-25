# GHCN-D gaps Part 7: Data risk R* Query for Claude

About dataset = GHCN-D Part 7, gaps in Data risk (D-1 to D-5)

Written 2026-11-22 from [ghcn-daily_categorization-gaps.md](../ghcn-daily_categorization-gaps.md). Rewrite this with
`/my:rewrite-research-query` (see [Rstar Precipitation Queries.md](../Rstar%20Precipitation%20Queries.md)), then run the
rewritten query with `/my:broad-web-research` in its own session.

## Query to refine

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily): about-pt1, about-pt2, about-pt3_combined, funding-pt3 and threats-news-pt4, plus the NOAA NCEI threats run (all in web_search_results/), how is GHCN-Daily stored, backed up and served, and how secure are the systems and programs that serve it from 2025 to now? Add to what those runs found rather than repeating it; the NCEI budget, file formats and political news are already covered.

- **Storage (D-2):** NCEI's archive storage and backup design; whether GHCN-Daily is held at more than one NCEI site (Asheville, Boulder); what the 2026–2027 move to Amazon Web Services changes, including whether GHCN-Daily processing moves too and who will run it; OIG-24-034-A (NESDIS cloud) and any other audit of NCEI's systems.
- **Access (D-3):** funding, staffing and status of Climate Data Online, the NCEI Access Data Service, and NOAA's Open Data Dissemination (NODD) program and its agreements with AWS and Google (terms, length, whether hosting can end); whether the NCEI fee schedule effective May 14, 2026 applies to GHCN-Daily; any outage of these routes since January 2025.
- **Formats (D-4):** the AWS Parquet schema and units, the BigQuery table schema, and whether the Access Data Service returns NetCDF with CF standard names.
- **Smaller funding routes (D-1):** whether NOAA's Climate Program Office still supports GHCN-Daily through Climate Observations and Monitoring (COM) and NCEI's Applied Research Center after 2021, with amounts if published.
- **Decommissioning (D-5):** whether NOAA has named the "at least 20 datasets, products and catalogs" it decommissioned, and whether any are GHCN-Daily routes or tools.

For each finding, say whether it supports or contradicts these statements: D-2 "storage at end of life or a single point of failure", D-3 "access infrastructure fragile or unfunded", D-4 "formats obsolete or proprietary", D-5 "subject to political suppression or alteration". Rate each threat: imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect), or no current threat found. Use NOAA's, OIG's, GAO's and the cloud providers' own documents ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Already well covered:** D-1 (the NCEI budget), D-4 (formats) and D-5 (politics). Don't repeat them.
- **The open pieces:**
  - D-2, storage and failover:
    - how NCEI stores and backs up its archive;
    - whether GHCN-Daily is held at both Asheville and Boulder;
    - where processing runs after the AWS migration (Spring 2027). OIG-24-034-A (NESDIS cloud) is a lead.
  - D-3, access: the funding and staff behind:
    - Climate Data Online and the Access Data Service;
    - NOAA's Open Data Dissemination (NODD) program, which places the AWS and Google copies;
    - whether the 2026 NCEI fee schedule touches GHCN-Daily.
  - D-1, smaller funding routes: NODD's own funding, which pays for the AWS and Google copies, and whether NOAA's
    Climate Program Office still funds GHCN-Daily through Climate Observations and Monitoring (last seen in 2021).
  - D-4, schemas: the AWS Parquet schema and units, the BigQuery table schema, and NetCDF output from the Access Data
    Service.
  - D-5: which "at least 20" datasets NOAA decommissioned (the update owed to the Senate under S. Rept. 119-44).
- **Time window:** 2025 to the present for threats; earlier only as background.

### What the answer should give

- How the archive is stored and backed up, and what changes with AWS.
- Funding and status for each access route, including NODD.
- The missing schemas.
- A rating and a stance for each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
