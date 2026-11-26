# A2 CoCoRaHS data site Repository resilience R* Query for Claude

About repository = CoCoRaHS data site (cocorahs.org), repository resilience (producer's own data site)

Written 2026-11-23 from `general_archive_queries/A2_Rstar_query_template-repository-resilience.md` and
`rstar-pipeline/processing/research-queries/archive-query-plan.md` in precipitation_rstar_scoring. Rewrite this with `/my:rewrite-research-query`, then
run the rewritten query with `/my:broad-web-research` in its own session. Suggested run folder:
`<date>_cocorahs-data-site-a2`.

**A producer's own data site.** The Colorado Climate Center at Colorado State University runs CoCoRaHS and serves its
data from cocorahs.org. The site's funding is the producer's funding, which CoCoRaHS's Part 3 (funding route) and
Part 4 (threats) cover, so there is no A1 threats run.

**Datasets that cite this run:** CoCoRaHS. GHCN-Daily holds a copy of CoCoRaHS reports, so this run's findings on how
reports reach NCEI also bear on GHCN-Daily's inputs (DIRS-3).

**Subcategories this run answers:** RRS-1, RRS-2, RRS-3 and RRS-5 for the data site, plus storage for D-2 and access
for D-3.

**Run order:** after CoCoRaHS's Part 1, and before its Part 4.

## Query to refine

Using the earlier runs' records in web_search_results/ on CoCoRaHS (`*_cocorahs-about-pt1` and
`*_cocorahs-qc-formats-pt2`) and on NOAA NCEI (`2026-11-17_noaa-ncei-threats` and NCEI's A2 run, if it has run), how
resilient is the CoCoRaHS data site (cocorahs.org, the ViewData reports, the data.cocorahs.org export portal,
dex.cocorahs.org, wys.cocorahs.org, media.cocorahs.org and the data-entry system) as a home for the network's data?
Add to what those runs found rather than repeating it.

- **Who runs it (D-3):** who built and maintains the website, database and data-entry apps (Colorado Climate Center
  staff, CSU IT, students, or an outside developer), how many people, and whether it depends on one developer; how the
  site and its servers are paid for.
- **Storage and copies (D-2, RRS-1):** where the database and servers are hosted (on CSU's campus, a data center or a
  cloud provider) and where backups are kept; how and how often reports are sent to NOAA NCEI for GHCN-Daily and to the
  National Weather Service; whether the NCEI copy is complete (all report types or only daily precipitation) and
  whether the two are ever checked against each other.
- **Integrity and recovery (RRS-2, RRS-3):** any checksum, fixity or database-integrity checks; CSU's backup and
  disaster recovery policies that cover the Colorado Climate Center's systems; whether CoCoRaHS has its own recovery
  plan and has tested it.
- **Track record (RRS-5):** outages, slowdowns or data-entry failures since the network began, with dates and causes
  (the Wayback Machine and CoCoRaHS's own announcements are the main sources); how the site fared when federal awards
  ended (NOAA awards naming CoCoRaHS ran 2006–10 and 2010–15) or during federal shutdowns; any reports lost.

The RRS statements are worded as strengths, so "supports" means evidence of resilience. For each finding, say whether
it supports or contradicts RRS-1 "two or more geographically independent sites hold verified copies", RRS-2 "checksum
checks quarterly or more often", RRS-3 "disaster recovery plan tested in the past 2 years with documented results",
RRS-5 "has survived a major disruption without data loss", D-2 "storage at end of life or a single point of failure" or
D-3 "access infrastructure fragile or unfunded". Say plainly when nothing is published, which is likely for a
university-run site. Leave funding cuts and news from 2025 on to CoCoRaHS's Part 4. Use CoCoRaHS's, CSU's and NCEI's
own pages and the Wayback Machine ahead of news. With a time limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Smaller limits than a shared archive's A2.** A university-run site publishes little about its operations, so 30
  minutes and 240,000 tokens should be enough. "Nothing published" answers are evidence too.
- **Keep it standard tier.** No cuts or news are asked for.
- **NCEI's copy is the main RRS-1 evidence.** CoCoRaHS stations are about 40% of GHCN-Daily's entries
  (`2026-11-21_ghcn-daily-sources-pt5`), so a second copy exists at NCEI. The question is whether it is complete and
  current, and how reports get there.
- **Already known (CoCoRaHS site, read 2026-11-23):** none of the pages read state a host, platform, software or API;
  media are served from media.cocorahs.org; the Station Data Explorer and Water Year Summaries run on their own
  subdomains; the contact address is info@cocorahs.org.
- **Leads:** CSU's Division of IT and the Walter Scott, Jr. College of Engineering's IT pages (Claude's own knowledge,
  to confirm: the Colorado Climate Center sits in CSU's Department of Atmospheric Science, which the sponsors page also
  lists); CoCoRaHS's newsletters and "message of the day" archives for
  outage notices; the CoCoRaHS annual reports, if any.

### What the answer should give

- Who runs the site, how many people, and how it is paid for.
- Where the data are hosted and backed up, and how reports reach NCEI and the NWS.
- Any integrity, backup or disaster recovery practice, or a plain statement that none was found.
- A dated list of outages and their causes, and any data loss.
- A subcategory tag and stance on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ on CoCoRaHS (the `*_cocorahs-about-pt1`,
`*_cocorahs-qc-formats-pt2` and `*_cocorahs-people-funding-pt3` folders), on GHCN-Daily's sources
(2026-11-21_ghcn-daily-sources-pt5) and on NOAA NCEI (2026-11-17_noaa-ncei-threats and
2026-11-23_ghcn-daily-repository-resilience-pt9), how resilient is the CoCoRaHS data site (cocorahs.org, the ViewData
reports, the data.cocorahs.org export portal, dex.cocorahs.org, wys.cocorahs.org, media.cocorahs.org and the
data-entry system) as a home for the network's data? Build on those runs rather than repeating them.

- Who runs it (D-3): who built and maintains the website, database and data-entry apps (Colorado Climate Center staff,
  CSU IT, students or an outside developer), how many people, whether it depends on one developer, and how it is paid
  for.
- Storage and copies (D-2, RRS-1): where the database and servers are hosted and where backups are kept; how and how
  often reports reach NOAA NCEI for GHCN-Daily and the National Weather Service; whether NCEI's copy holds all report
  types or only daily precipitation, and whether the two are checked against each other.
- Integrity and recovery (RRS-2, RRS-3): any checksum, fixity or database-integrity checks; CSU's backup and disaster
  recovery policies covering the Colorado Climate Center; whether CoCoRaHS has its own plan and has tested it.
- Track record (RRS-5): outages, slowdowns or data-entry failures since the network began, with dates and causes; how
  the site fared when its NOAA awards (2006–10, 2010–15) ended and during federal shutdowns; any reports lost.

The RRS statements are worded as strengths and the D statements as risks, so "supports" means evidence for the
statement as worded. For each finding, say whether it supports or contradicts RRS-1 "two or more geographically
independent sites hold verified copies", RRS-2 "checksum checks quarterly or more often", RRS-3 "disaster recovery plan
tested in the past 2 years with documented results", RRS-5 "has survived a major disruption without data loss", D-2
"storage at end of life or a single point of failure" or D-3 "access infrastructure fragile or unfunded". Say plainly
when nothing is published; for a university-run site, that is evidence too. Leave funding and news from 2025 on to
CoCoRaHS's Part 4. Use CoCoRaHS's, CSU's and NCEI's own pages and the Wayback Machine ahead of news. With a time limit
of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** who runs the site and how it is paid for, where the data are hosted and backed up, how reports
reach NCEI and the NWS and whether NCEI's copy is complete, any integrity or recovery practice, and a dated list of
outages with causes and any data loss, each tagged with a subcategory and stance.

**What changed and why:**
- **Run order follows the run sheet:** this is run 4, after CoCoRaHS Parts 1–3, so the question now also names Part 3
  (people and funding), which answers part of "who runs it".
- **Folder names:** Parts 1–3 haven't run yet, so they're named by the run sheet's suggested suffixes. Once they've
  run, replace each `*_` pattern with the real folder name, or leave it; the run reads the whole folder anyway.
- **Replaced "NCEI's A2 run, if it has run"** with the GHCN-D resilience run (pt9), which has run and holds NCEI's copy
  practice. Added GHCN-D's sources run (pt5), which has the 40% share. If NCEI's own A2 run exists by then, the run will
  find it in the folder.
- **"Supports" for D-2 and D-3 is now defined** as evidence for the risk, since those two are worded as risks.
- **Cut** the context, leads, the already-known list and the answer list. The CoCoRaHS pages read on 2026-11-23 showed
  no host or platform, so the hosting question stays as it was.
- **Limits kept** at 30/240k, standard tier.

**How to reuse:** run it in its own session in this project after CoCoRaHS Parts 1–3, and before Parts 5 and 4.
