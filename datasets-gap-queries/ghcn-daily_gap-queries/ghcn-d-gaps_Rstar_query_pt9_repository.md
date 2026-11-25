# GHCN-D gaps Part 9: Repository resilience R* Query for Claude

About dataset = GHCN-D Part 9, gaps in Repository resilience (RRS-1 to RRS-5)

Written 2026-11-22 from [ghcn-daily_categorization-gaps.md](../ghcn-daily_categorization-gaps.md). Rewrite this with
`/my:rewrite-research-query` (see [Rstar Precipitation Queries.md](../Rstar%20Precipitation%20Queries.md)), then run the
rewritten query with `/my:broad-web-research` in its own session.

## Query to refine

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily): about-pt1, about-pt2, about-pt3_combined, funding-pt3 and threats-news-pt4, plus the NOAA NCEI threats run (all in web_search_results/), how resilient are the repositories that hold GHCN-Daily — NOAA NCEI, the AWS Open Data copy (noaa-ghcn-pds) and Google BigQuery (ghcn_d) — in redundancy, integrity checks, disaster recovery, funding and track record? Add to what those runs found rather than repeating it.

- **Integrity checks (RRS-2):** NCEI's fixity or checksum checks and how often they run; current CoreTrustSeal or ISO 16363 certification; NOAA archive policy (NAO 212-15 and related directives); what the 2021 stewardship maturity review DSMR-00227 says about GHCN-Daily; whether AWS and Google verify their copies.
- **Disaster recovery (RRS-3):** NCEI's continuity-of-operations or disaster recovery plan and when it was last tested, with results; after-action reports on Hurricane Helene (2024); what OIG-24-034-A and OIG-16-043-A found.
- **Redundancy (RRS-1):** whether GHCN-Daily is held at both NCEI sites (Asheville, Boulder); which AWS regions NCEI uses after its 2026–2027 migration; whether the copies are checked against each other; any other independent copies.
- **Funding (RRS-4):** the terms and funding of NOAA's Open Data Dissemination agreements with AWS and Google; whether NCEI received its FY2026 $69.0M (spend plan); threats from 2025 to now not already covered.
- **Track record (RRS-5):** NCEI's holdings and ingest before and after disruptions: Helene, the 2025 staff losses, the 2025 shutdown, and the 2013 and 2018–19 shutdowns. Note any data loss or ingest delays.

For each finding, say whether it supports or contradicts these statements: RRS-1 "two or more geographically independent sites hold verified copies", RRS-2 "checksum checks quarterly or more often", RRS-3 "disaster recovery plan tested in the past 2 years with documented results", RRS-4 "no imminent threat to operations funding", RRS-5 "has survived a major disruption without data loss". Say plainly when nothing is found. Use NCEI's, NOAA's, OIG's, GAO's, CoreTrustSeal's and the cloud providers' own documents ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Repositories:** NCEI (the producer and main archive), the AWS copy (`noaa-ghcn-pds`, us-east-1) and Google
  BigQuery (`bigquery-public-data.ghcn_d`).
- **RRS-2 and RRS-3 were never searched.**
  - **RRS-2, checksums.** Search for:
    - "NCEI CoreTrustSeal" and "NCEI ISO 16363" (trustworthy-repository certification);
    - NCEI's fixity and checksum practice and how often it runs;
    - NOAA's archive policy (NAO 212-15 and NOAA's procedural directives on archiving);
    - the 2021 stewardship maturity review DSMR-00227 for GHCN-Daily;
    - whether AWS and Google verify their copies (NODD documentation).
  - **RRS-3, disaster recovery.** Search for:
    - NCEI's continuity-of-operations (COOP) or disaster recovery plan and its last test;
    - lessons-learned or after-action reports from Hurricane Helene (2024);
    - Commerce OIG reports OIG-24-034-A (NESDIS cloud) and OIG-16-043-A (NESDIS cyber incident), which were found but
      not opened.
- **RRS-1 (geography):**
  - whether NCEI holds GHCN-Daily at both Asheville and Boulder;
  - which AWS regions it will use after the migration;
  - whether the copies are checked against each other.
- **RRS-4 (funding):** the NODD agreements with AWS and Google (length, cost, whether no-cost hosting can end), and
  whether NCEI actually received its FY2026 $69.0M.
- **RRS-5 (track record):** NCEI's holdings and ingest before and after disruptions:
  - dataset counts, petabytes, and ingest backlogs or delays after Helene;
  - the 2025 staff losses;
  - the October–November 2025 shutdown;
  - earlier shutdowns (2013, 2018–19).

### What the answer should give

- Certification and checksum status.
- Whether a disaster recovery plan exists and was tested.
- Where the copies are.
- How the cloud copies are funded.
- Holdings and delays around past disruptions.
- A stance for each finding against the RRS statements.

The RRS statements are worded as good things, so here "supports" means evidence of resilience.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
