# A2 UC Irvine CHRS data site Repository resilience R* Query for Claude

About repository = UC Irvine CHRS data site, repository resilience (producer's own data site)

Written 2026-11-23 from `general_archive_queries/A2_Rstar_query_template-repository-resilience.md` and the PERSIANN-CDR
Daily coverage check (`datasets-gap-queries/` in precipitation_rstar_scoring). Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session in this
project.

**A producer's own data site.** UC Irvine's Center for Hydrometeorology and Remote Sensing (CHRS) makes PERSIANN-CDR
and serves its own copy. Its funding is the producer's funding, which PERSIANN-CDR's funding and news runs (pt3, pt4)
and its Part 7 gap run cover. So there is no A1 threats run, and this run adds questions about the site's own team.

**Datasets that cite this run:** PERSIANN-CDR Daily. CHRS also serves other PERSIANN products and PDIR-Now, which
IMERG uses as an input.

**Subcategories this run answers:** RRS-1, RRS-2, RRS-3, RRS-4 and RRS-5 for the CHRS site, plus storage for D-2 and
access for D-3.

## Query to refine

Using the earlier runs' records in web_search_results/ on PERSIANN-CDR Daily (2026-11-19_persiann-cdr-daily-about-pt1,
2026-11-19_persiann-cdr-daily-qc-formats-pt2, 2026-11-19_persiann-cdr-daily-about-pt3 and
2026-11-19_persiann-cdr-daily-news-pt4), how resilient is UC Irvine CHRS's own data site (the CHRS Data Portal at
chrsdata.eng.uci.edu, and persiann.eng.uci.edu over HTTPS and FTP) as a home for data? Add to what those runs found
rather than repeating it.

- **Who runs it (D-3):** who built and maintains the portal and servers (CHRS staff, students, or UC Irvine's Samueli
  School or OIT), how many people, and whether it depends on one developer; how the portal and servers are paid for.
- **Storage and copies (D-2, RRS-1):** what servers hold the data and where; whether CHRS or UC Irvine backs them up,
  and where the backup is kept; whether the CHRS copy is checked against NCEI's archive copy.
- **Integrity and recovery (RRS-2, RRS-3):** any checksum or fixity checks on the CHRS files, and whether checksums are
  published; UC Irvine's backup and disaster recovery policies that cover research servers in the Samueli School of
  Engineering, and whether CHRS has its own plan or has tested one.
- **Institutional support (RRS-4):** whether UC Irvine gives CHRS core support (space, IT, staff) beyond grants, since
  the runs found CHRS grant-funded with no core budget.
- **Track record (RRS-5):** the outage that left download links down until October 11, 2024, and why; why the 2024
  files were posted only in October 2025; why the portal's information tab dates from 2020; any data lost; how the site
  fared when grants ended or were terminated (NSF 2332263 was terminated, then reinstated).

The RRS statements are worded as strengths, so "supports" means evidence of resilience. For each finding, say whether it
supports or contradicts RRS-1 "two or more geographically independent sites hold verified copies", RRS-2 "checksum
checks quarterly or more often", RRS-3 "disaster recovery plan tested in the past 2 years with documented results",
RRS-4 "no imminent threat to the repository's funding", RRS-5 "has survived a major disruption without data loss", D-2
"storage at end of life or a single point of failure" or D-3 "access infrastructure fragile or unfunded". Say plainly
when nothing is published, which is likely for a small university site. Use CHRS's and UC Irvine's own pages, the
Wayback Machine for the site's history, and papers ahead of news. With a time limit of 30 minutes and a token ceiling
of 240,000.

### Context for the rewrite

- **Smaller limits than a shared archive's A2.** A university research site publishes little about its operations, so
  30 minutes and 240,000 tokens should be enough. Expect many "nothing published" answers; they are evidence too.
- **Keep it standard tier.** No cuts or news are asked for; pt3 and pt4 found none aimed at the dataset.
- **The Wayback Machine is the main track-record source.** Snapshots of the portal and the download pages show when
  links broke and when files appeared.
- **Already found, don't search again (from the coverage check):**
  - CHRS serves raw `.bin.gz` files, with GeoTIFF, ArcGrid and NetCDF on request (pt1, pt2);
  - production runs on CHRS's own servers (pt1);
  - download links were down until October 11, 2024; the 2024 files were posted in October 2025; the portal's
    information tab dates from 2020 (pt1);
  - CHRS is grant-funded with no core budget found, and its NOAA CPO grant NA23OAR4310443 ended on August 31, 2026
    (pt3).
- **Leads:** UC Irvine OIT's and the Samueli School's IT policies and service pages; CHRS's README for the data
  (not read by earlier runs); CHRS's contact pages.

### What the answer should give

- Who runs the site and how it is paid for.
- Where the data are stored and backed up.
- Any checksum, backup or disaster recovery practice, or a plain statement that none was found.
- UC Irvine's institutional support for CHRS.
- A dated list of outages and late postings, with causes where known, and any data loss.
- A subcategory tag and stance on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ on PERSIANN-CDR Daily (the 2026-11-19
`persiann-cdr-daily-*` folders) and the GHCN-Daily repository resilience run on NCEI
(2026-11-23_ghcn-daily-repository-resilience-pt9), how resilient is UC Irvine CHRS's own data site (the CHRS Data Portal
at chrsdata.eng.uci.edu, and persiann.eng.uci.edu over HTTPS and FTP) as a home for data? Build on those runs rather
than repeating them.

- Who runs it (D-3): who built and maintains the portal and servers (CHRS staff, students, or UC Irvine's engineering
  school or central IT), how many people, whether it depends on one developer, and how it is paid for.
- Storage and copies (D-2, RRS-1): which servers hold the data and where; whether they are backed up, and where; whether
  the CHRS copy is checked against NCEI's.
- Integrity and recovery (RRS-2, RRS-3): any checksum or fixity checks, and whether checksums are published; UC Irvine's
  backup and disaster recovery policies for research servers; whether CHRS has its own plan and has tested it.
- Institutional support (RRS-4): whether UC Irvine gives CHRS space, IT or staff beyond grants.
- Track record (RRS-5): why download links were down until October 11, 2024; why the 2024 files were posted only in
  October 2025; why the portal's information tab dates from 2020; how the site fared between grants (NSF 2332263 was
  terminated, then reinstated); any data lost.

The RRS statements are worded as strengths and the D statements as risks, so "supports" means evidence for the
statement as worded. For each finding, say whether it supports or contradicts RRS-1 "two or more geographically
independent sites hold verified copies", RRS-2 "checksum checks quarterly or more often", RRS-3 "disaster recovery plan
tested in the past 2 years with documented results", RRS-4 "no imminent threat to the repository's funding", RRS-5 "has
survived a major disruption without data loss", D-2 "storage at end of life or a single point of failure" or D-3
"access infrastructure fragile or unfunded". Say plainly when nothing is published; for a small university site, that
is evidence too. Use CHRS's and UC Irvine's own pages, the Wayback Machine for the site's history, and papers ahead of
news. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** who runs the CHRS site and how it is paid for, where the data are stored and backed up, any
integrity or recovery practice, UC Irvine's support, and a dated list of outages and late postings with causes where
known, each tagged with a subcategory and stance. Expect many "nothing published" answers.

**What changed and why:**
- **Added the GHCN-D resilience run** (pt9), which ran after this draft was written: it holds NCEI's copy practice, so
  the run can judge the CHRS-versus-NCEI check without searching NCEI again.
- **"Supports" for D-2 and D-3 is now defined** as evidence for the risk, since those two are worded as risks.
- **PERSIANN-CDR runs named by pattern** instead of four folder names; the run reads the whole folder anyway.
- **Cut** the context, leads, the already-found list and the answer list. The facts the questions rest on (the 2024
  outage, the late 2024 files, the 2020 information tab, the NSF grant) stay in the questions.
- **Tier:** the NSF grant is phrased as a track-record question so the skill keeps the standard tier. Limits kept at
  30/240k.

**How to reuse:** run it in its own session in this project; every run it needs exists.
