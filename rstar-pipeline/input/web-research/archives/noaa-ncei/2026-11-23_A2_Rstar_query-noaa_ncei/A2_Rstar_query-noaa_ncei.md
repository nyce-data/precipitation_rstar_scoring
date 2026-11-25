# A2 NOAA NCEI Repository resilience R* Query for Claude

About repository = NOAA NCEI, repository resilience (shared run for every dataset NCEI hosts)

Written 2026-11-23 from `general_archive_queries/A2_Rstar_query_template-repository-resilience.md`. It replaces
GHCN-Daily's gap query pt9 (`ghcn-d-gaps_Rstar_query_pt9_repository.md`), which asked the same questions about NCEI
for one dataset only. Rewrite this with `/my:rewrite-research-query`, then run the rewritten query with
`/my:broad-web-research` in its own session in this project.

**Datasets that cite this run:** GHCN-Daily, GPCP Daily and PERSIANN-CDR Daily.

**Subcategories this run answers:** RRS-1, RRS-2, RRS-3 and RRS-5. It adds to D-2 only where the earlier runs left
gaps. RRS-4 and D-1 (NCEI's funding and threats) are in the A1 run.

## Query to refine

Using the earlier runs' records in web_search_results/ on NOAA NCEI (2026-11-17_noaa-ncei-threats), on GHCN-Daily's
storage and serving (2026-11-22_ghcn-daily-repository-pt7) and on its processing after the cloud move
(2026-11-23_ghcn-daily-infrastructure-pt8), and the Part 1 runs that list NCEI's copies of GHCN-Daily, GPCP Daily and
PERSIANN-CDR Daily (2026-11-19_ghcn-daily-about-pt1, 2026-11-19_gpcp-daily-about-pt1 and
2026-11-19_persiann-cdr-daily-about-pt1), how resilient is NOAA's National Centers for Environmental Information (NCEI)
as a home for data? Add to what those runs found rather than repeating it; they cover NCEI's budget, staff losses, its
primary and offsite tape copies, the move to Amazon Web Services and OIG-24-034-A.

- **Integrity checks (RRS-2, never searched):** NCEI's fixity or checksum checks, which algorithm and how often they
  run, on tape and in the cloud; whether NCEI is certified by CoreTrustSeal or ISO 16363, or is a World Data System
  member; what NOAA's archive policy requires (NAO 212-15 and NOAA's procedural directives on archiving); what the
  stewardship maturity reviews of these three datasets say about integrity (GHCN-Daily's is DSMR-00227); whether AWS and
  Google verify the NODD copies (`noaa-ghcn-pds`, `noaa-cdr-precip-gpcp-daily-pds`, `noaa-cdr-precip-persiann-pds`,
  `bigquery-public-data.ghcn_d`).
- **Disaster recovery (RRS-3, never searched):** NCEI's continuity-of-operations or disaster recovery plan, when it
  was last tested or exercised, and with what results; Hurricane Helene (2024) after-action or lessons-learned reports;
  what OIG-16-043-A (NESDIS cyber incident) found about recovery; NCEI's recovery-time and recovery-point targets.
- **Redundancy (RRS-1):** where the offsite "secure copy" is kept; whether Asheville and Boulder each hold a full copy
  now; whether the AWS target keeps two independent copies in separate regions (OIG found the NCCF in one region, and
  NOAA said it would review a multi-region option: was that decided?); what happens to the tape copies when on-premises
  systems are decommissioned; whether the copies are checked against each other.
- **Track record (RRS-5):** NCEI's holdings (petabytes, dataset counts) and ingest backlogs or delays before and after
  each disruption, and any data loss: the 2015 merger of NCDC, NODC and NGDC into NCEI; the 2013 and 2018–19
  shutdowns; Hurricane Helene (2024); the 2025 staff losses; the October–November 2025 shutdown; and the 2026–2027
  cloud migration. NCEI's quarterly "State of the Service" summaries are a lead.

The statements are worded as strengths, so "supports" means evidence of resilience. For each finding, say whether it
supports or contradicts RRS-1 "two or more geographically independent sites hold verified copies", RRS-2 "checksum
checks quarterly or more often", RRS-3 "disaster recovery plan tested in the past 2 years with documented results" or
RRS-5 "has survived a major disruption without data loss", and say plainly when nothing is published. Leave NCEI's
budget, cuts and news from 2025 on to the A1 run. Use NCEI's, NOAA's, OIG's, GAO's, CoreTrustSeal's and the cloud
providers' own documents ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** This run asks about practice and track record, not threats. The A1 run
  (2026-11-17_noaa-ncei-threats) covers NCEI's budget, the 2025 staff losses and the retired products. Keep the
  question's wording off cuts and disputes, so the skill doesn't pick its costly deep tier.
- **What the earlier runs already found (don't search again):**
  - **Two tape copies:** NCEI's archive and backup copy hold more than 60 petabytes. In 2020, one copy was in Asheville
    and a "secure copy" was offsite, at an unnamed site (pt7, citing NCEI's About Us page and its COSMIC-2 news item).
  - **Helene:** the storm hit the Asheville headquarters on September 27, 2024. By December 11, ingest was restored,
    92% of the ingest backlog was recovered, and "data loss was mitigated" with help from Boulder (pt7, citing the
    FY2025 Q1 State of the Service summary). This is a lead for RRS-5: ask what the other quarterly summaries show.
  - **The move to AWS:** all of NCEI's data are moving from Asheville and Boulder to AWS by lift and shift, then into
    the NESDIS Common Cloud Framework (NCCF), through spring 2027, run by contractors (pt7).
  - **OIG-24-034-A (August 2024):** the NCCF is hosted in one region, though its maximum tolerable downtime is a few
    hours; recommendations 3, 9 and 10 were still open in September 2025 (pt7). Ask only whether the multi-region
    review was decided and whether the March 2026 or later OIG reports close them.
  - **Access delays:** NCEI's "Data Access Delays" alert (November 16–30, 2026) blames the migration (pt7, pt8).
  - **Where GHCN-Daily is processed after the move:** not published (pt8). Leave this to the datasets' runs.
- **Never searched by any run:** fixity and checksums, CoreTrustSeal or ISO 16363, NOAA's archive directives, the
  stewardship maturity reviews' integrity scores, the continuity-of-operations plan and its tests, and NCEI's track
  record before 2024.
- **Cloud copies' integrity.** AWS S3 and Google Cloud Storage compute checksums on upload. The question is whether NOAA
  or the providers check the NODD copies against NCEI's archive, and whether that is documented. The four copy names
  come from the Part 1 runs.
- **The 2015 merger counts as a leadership disruption** for RRS-5: NCEI was formed from three data centers (NCDC,
  NODC, NGDC). Ask whether holdings were lost or delayed in the move.
- **Sources likely to help:** CoreTrustSeal's list of certified repositories; NOAA's administrative orders and NESDIS
  procedural directives; NCEI's State of the Service summaries; Commerce OIG and GAO reports; NCEI's Archive Information
  Request System and archive policy pages; the NODD program pages and the 2023 Science Advances paper on NODD (Willett
  et al.).

### What the answer should give

- The fixity or checksum practice and how often it runs, and certification status, or a plain statement that none
  was found.
- Whether a disaster recovery or continuity plan exists, when it was last tested, and what the test found.
- A table of copies: where each is, whether it is a full copy, and whether it is checked against the others, now and
  after the AWS move.
- A dated table of past disruptions: holdings and ingest before and after, and any data loss.
- A stance (supports or contradicts) against RRS-1, RRS-2, RRS-3 or RRS-5 for each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/, above all the GHCN-Daily repository resilience run
(2026-11-23_ghcn-daily-repository-resilience-pt9), how resilient is NOAA NCEI as a home for GPCP Daily, PERSIANN-CDR
Daily and its holdings as a whole, beyond what that run found for GHCN-Daily? It found NCEI CoreTrustSeal-certified to
2028-01-29, a checksum stored per file but no periodic fixity schedule, an offsite tape copy 12.5 miles from Asheville,
NESDIS's annual contingency-test rule with no public results, OIG-24-034-A's recommendations closed, and the Helene and
shutdown record. Build on that rather than repeating it:

- Integrity (RRS-2): what GPCP Daily's and PERSIANN-CDR Daily's stewardship maturity reviews score for integrity;
  whether the NODD copies (`noaa-cdr-precip-gpcp-daily-pds`, `noaa-cdr-precip-persiann-pds`) are checked against
  NCEI's archive; what NCEI's CoreTrustSeal application says about fixity, if it can be read.
- Copies (RRS-1): whether Boulder or any site outside the Asheville area holds a copy; where the copies sit after the
  AWS move and what happens to the tape copies; what action closed OIG's single-region recommendation.
- Track record (RRS-5): holdings, ingest backlogs and any data loss when NCDC, NODC and NGDC became NCEI in 2015, during
  2025 and during the 2026 cloud migration, from NCEI's quarterly State of the Service summaries.

The statements are worded as strengths, so "supports" means evidence of resilience. For each finding, say whether it
supports or contradicts RRS-1 "two or more geographically independent sites hold verified copies", RRS-2 "checksum
checks quarterly or more often", RRS-3 "disaster recovery plan tested in the past 2 years with documented results" or
RRS-5 "has survived a major disruption without data loss", and say plainly when nothing is published. Leave NCEI's
budget and news to the A1 run. Use NCEI's, NOAA's, OIG's, CoreTrustSeal's and the cloud providers' own documents ahead
of news. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** findings tagged RRS-1, RRS-2, RRS-3 or RRS-5 with a stance, on the two CDRs' integrity scores and
cloud copies, any copy outside Asheville, the post-migration copies, and NCEI's track record in 2015, 2025 and 2026,
with "nothing published" where that holds.

**What changed and why:**
- **Built on the GHCN-D resilience run.** `2026-11-23_ghcn-daily-repository-resilience-pt9` ran after this draft was
  written and answered most of it for NCEI as a whole: CoreTrustSeal, DSMR-00227, NAO 212-15, NESDIS NQP-3406,
  OIG-24-034-A, OIG-16-043-A, the offsite site, the GHCN-D cloud copies, Helene and the 2013, 2018–19 and 2025
  shutdowns. The draft lists these as never searched. The rewrite states them as found and asks only what is left.
- **The top note is out of date.** It says this run replaces GHCN-D's pt9 query, but pt9 has run, so this run now adds
  to it. I left the note as it is.
- **Limits lowered** from 40/320k to 30/240k, since about two thirds of the questions are answered.
- **Cut** the context, leads, the already-found list and the answer tables; the run reads the earlier records itself
  and sets its own format. Only pt9 is named, since it matters most; the run searches the whole folder anyway.
- **Tier:** worded to stay standard. The 2015 merger and "during 2025" are track-record questions, but the skill may
  still pick deep; the limits suit either.
- **CoreTrustSeal application** (doi:10.34894/50BIQ1): pt9 couldn't read it because the sandbox refuses dataverse.nl.
  Unless you allow that host, expect it unread again, or open it by hand.

**How to reuse:** run it in its own session in this project; every run it needs exists. If it finds little beyond pt9,
GPCP Daily and PERSIANN-CDR Daily can cite pt9 for NCEI-wide findings, and you may not need to rerun this.
