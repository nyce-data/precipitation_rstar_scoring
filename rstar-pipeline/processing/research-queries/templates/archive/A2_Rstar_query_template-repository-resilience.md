# A2 $REPOSITORY_SHORT Repository resilience R* Query for Claude

About repository = $REPOSITORY_SHORT, repository resilience (shared run, once per repository)

Template written 2026-11-23 from `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` in precipitation_rstar_scoring. To use it:
copy it into `archive_queries/archive_specific_queries/` as `A2_Rstar_query-<repository>.md`, replace every
`$PLACEHOLDER`, rewrite it with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research`
in its own session.

This run is about the repository as a whole, not one dataset. Every dataset the repository hosts cites it, so run it
once per repository. For NOAA NCEI, it serves GHCN-Daily, GPCP Daily and PERSIANN-CDR Daily. GHCN-Daily's gap query
pt9 asks many of the same questions about NCEI; reuse its context when writing NCEI's A2.

**Placeholders:**
- `$REPOSITORY_SHORT`: the short name, such as NOAA NCEI or NASA GES DISC.
- `$REPOSITORY`: the full name, such as "NOAA's National Centers for Environmental Information (NCEI)".
- `$A1_RUN`: the folder name of this repository's threats run (A1), such as `2026-11-17_noaa-ncei-threats`, if it
  ran first. Leave it out otherwise.
- `$COPIES`: other copies of its holdings named in the datasets' Part 1 runs, such as the AWS and Google copies under
  NOAA's Open Data Dissemination program, or GHCN-Daily's copy of CoCoRaHS reports.
- `$THREATS_RUN`: where cuts and news are covered. For a shared archive, "the A1 run". For a producer's own data site
  (CoCoRaHS, CHRS, NASA PPS), "the dataset's Part 4 run", since the producer's funding is the site's funding.

**Two kinds of repository** (see `rstar-pipeline/processing/research-queries/archive-query-plan.md` in precipitation_rstar_scoring):
- **Shared archive** (NCEI, GES DISC): run A2 and A1. Every dataset it hosts cites both.
- **Producer's own data site** (CoCoRaHS, CHRS, NASA PPS): run A2 only. Add questions about the site's own team
  (who builds and runs it, and how many people), because a small site can depend on one developer (D-3).

**Subcategories this run answers:** RRS-1, RRS-2, RRS-3 and RRS-5, plus storage for D-2 and access systems for D-3.

**Run order:** before the repository's A1 run, if it has one, and before the Part 4 runs of the datasets it hosts.
NCEI's ran the other way round (A1 first), which also works.

## Query to refine

Using the earlier run's record on $REPOSITORY ($A1_RUN, in web_search_results/), how resilient is it as a home for
data? Does it hold copies at two or more geographically separate sites, including $COPIES, and check them against each
other? How often does it run fixity or checksum checks, and is it certified (CoreTrustSeal or ISO 16363)? Does it have
a disaster recovery or continuity-of-operations plan, when was the plan last tested, and with what results? What are
its storage and backup design and its access systems (portals, APIs, cloud copies), and who pays for and staffs them?
Through which past funding, leadership or physical disruptions has it kept or lost data, and how did its holdings and
ingest delays look before and after? Leave budget cuts and news from 2025 on to $THREATS_RUN. The statements are worded as
strengths, so "supports" means evidence of resilience; tag findings with RRS-1 "two or more geographically independent
sites hold verified copies", RRS-2 "checksum checks quarterly or more often", RRS-3 "disaster recovery plan tested in
the past 2 years with documented results", RRS-5 "has survived a major disruption without data loss", D-2 "storage at
end of life or a single point of failure" or D-3 "access infrastructure fragile or unfunded". With a time limit of 40
minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** Cuts and threats are in $THREATS_RUN, so leave them out here; the skill picks its costly
  deep tier when the question involves a dispute.
- **RRS points the other way.** P, D and DIRS describe risks, but RRS describes strengths. The question says so, so
  "supports" is read the right way.
- **Where to look:**
  - certification: CoreTrustSeal's list of certified repositories, ISO 16363 audits, World Data System membership;
  - policy: the agency's archive and records directives (for NOAA, NAO 212-15 and its procedures), data management
    plans and stewardship maturity reviews;
  - audits: GAO and Inspector General reports on the repository's systems, cloud moves and cyber incidents;
  - disasters: after-action reports on storms, fires, outages or shutdowns that hit the repository's sites.
- **Track record (RRS-5).** Ask for holdings (dataset counts, petabytes) and ingest backlogs before and after each
  disruption, and any data loss. Government shutdowns and earlier budget cuts count.
- **Cloud copies.** Ask whether the cloud providers verify their copies, which regions they use, and whether
  no-cost hosting agreements can end.

### What the answer should give

- A table of copies and sites, and whether they are checked against each other.
- The fixity or checksum policy and certification status, or a plain statement that none was found.
- The disaster recovery plan, its last test and its results, or a plain statement that none was found.
- Storage, backup and access systems, with who pays for and staffs them.
- A dated list of past disruptions, with holdings and delays before and after, and any data loss.
- A subcategory tag and stance on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
