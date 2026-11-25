# GHCN-D gaps Part 6: People risk R* Query for Claude

About dataset = GHCN-D Part 6, gaps in People risk (P-1 to P-4)

Written 2026-11-22 from [ghcn-daily_categorization-gaps.md](../ghcn-daily_categorization-gaps.md). Rewrite this with
`/my:rewrite-research-query` (see [Rstar Precipitation Queries.md](../Rstar%20Precipitation%20Queries.md)), then run the
rewritten query with `/my:broad-web-research` in its own session.

## Query to refine

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily): about-pt1, about-pt2, funding-pt3 and threats-news-pt4, plus the NOAA NCEI threats run (all in web_search_results/), who are the people critical to producing and quality-controlling GHCN-Daily at NOAA NCEI now? How long has each worked on it, and how close is each to retirement eligibility? Is there a documented succession plan, knowledge-transfer process or enough documentation and code for someone else to keep it going? Add to what those runs found rather than repeating it.

- **People:** start from the principal investigators Matthew J. Menne and Imke Durre, the Version 3 citation authors (Vose, Gleason, Houston, Korzeniewski, McNeill, Thomas, Yin, Anthony, Ray) and Rennie and Stevens, and add anyone recent GHCN-Daily papers or NCEI pages show working on it now. For each: their current role and whether they are still at NCEI, their ORCID iD, their earliest publication year (from ORCID, OpenAlex or Google Scholar; say which), the first year they appear on GHCN work, an estimated career length and approximate age (earliest publication year minus 25–30), and whether they are likely eligible to retire within 2 years under FERS rules. Show the reasoning and mark estimates as estimates.
- **Team and succession:** GHCN-Daily team size; a current NCEI org chart; any NOAA or NCEI succession, workforce or knowledge-transfer plan; GAO or OIG findings on NOAA's workforce; and departures or retirements of anyone above since 2024.
- **Knowledge held by people:** who runs integration of new sources and the "Datzilla" ticket review; whether the GHCN-Daily processing and QC code is shared on request or held in an internal repository (including code.noaa.gov); and CISESS and contractor staff working on GHCN-Daily (CISESS reports 2023–2026).

For each finding, say whether it supports or contradicts these statements: P-1 "no documented succession plan", P-2 "key personnel retirement-eligible within 2 years", P-3 "critical knowledge undocumented", P-4 "a single person is a point of failure". Use NCEI's own pages, papers and ORCID or OpenAlex records ahead of news. With a time limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Who to look up.** The principal investigators are **Matthew J. Menne** and **Imke Durre** (NCEI ISO record
  C00861).
  - **Version 3 citation authors (2012):** Russell S. Vose, Byron E. Gleason, Timothy G. Houston, B. Korzeniewski,
    S. McNeill, K. Thomas, X. Yin, S. Anthony and R. Ray.
  - **Also named in part 4:** Rennie and Stevens. Part 4 gives surnames only; they are probably Jared Rennie and Scott
    Stevens, but confirm that they are and that they work on GHCN-Daily.
  - **Check whether these are the same people:** some initials may match more than one researcher. Confirm identity by
    affiliation (NCDC or NCEI, Asheville) and by GHCN co-authorship.
- **Age proxy: ORCID and earliest publication year.** Ages are not public, so estimate them from careers.
  - **Find each person's ORCID iD:** the ORCID public search at orcid.org, the ORCID API (pub.orcid.org), or the iD
    printed on recent papers.
  - **Find their earliest publication year:** use the ORCID record, OpenAlex (api.openalex.org, author search, then the
    oldest work), Google Scholar, Crossref, or the NOAA Institutional Repository (repository.library.noaa.gov). ORCID
    records are often incomplete, so check one of the others as well.
  - **Estimate an approximate birth year:** earliest publication year minus about 25 to 30 years (a first paper usually
    comes after a degree).
  - **Also record when they started on GHCN:** their first year on NCDC/NCEI staff or on a GHCN paper, from bios, CVs,
    LinkedIn or the papers' affiliations.
- **Federal retirement rules, to judge eligibility.** NCEI scientists are mostly federal employees under FERS, which
  allows full retirement at:
  - the minimum retirement age (56–57) with 30 years of service;
  - age 60 with 20 years;
  - age 62 with 5 years.

  Someone whose first paper was before about 1998 is likely to be eligible within 2 years. Treat this as an estimate,
  not a fact. Ask the run to state each person's numbers and the reasoning behind them.
- **Succession and documentation.** Look for:
  - NOAA or NCEI workforce plans and succession plans;
  - GAO and Commerce OIG reports on NOAA's workforce;
  - a current NCEI org chart (the latest found is February 2023);
  - CISESS annual reports (2023–2026) that name GHCN-Daily staff or tasks;
  - recent GHCN-Daily papers, which show who works on it now;
  - anything on the "Datzilla" ticket review and whether NCEI shares the GHCN-Daily code on request (also try
    code.noaa.gov, which didn't resolve last time).

### What the answer should give

- A table of people with their ORCID iDs, earliest publication years, estimated ages and a likely-eligible flag.
- The current team as far as it is public.
- Whatever succession or workforce planning exists, or a plain statement that none was found.
- A stance (supports or contradicts) for each finding.

If the sandbox blocks ORCID or OpenAlex, the run will fall back to Google Scholar and paper affiliations. It lists blocked
hosts in `sites-to-trust.md`.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily) (2026-11-19_ghcn-daily-about-pt1, 2026-11-19_ghcn-daily-about-pt2, 2026-11-21_ghcn-daily-funding-pt3 and 2026-11-21_ghcn-daily-threats-news-pt4) and on NOAA NCEI (2026-11-17_noaa-ncei-threats), all in web_search_results/, who are the people critical to producing and quality-controlling GHCN-Daily at NOAA NCEI now, how close is each to retirement eligibility, and could someone else keep it going? Add to what those runs found rather than repeating it.

- **People:** start from the principal investigators Matthew J. Menne and Imke Durre, the Version 3 (2012) authors (Vose, Gleason, Houston, Korzeniewski, McNeill, Thomas, Yin, Anthony, Ray) and Rennie and Stevens, confirming each identity by NCDC/NCEI Asheville affiliation and GHCN co-authorship, and add anyone recent papers or NCEI pages show working on it now. For each: current role and whether still at NCEI; ORCID iD; earliest publication year (say from which source); first year on GHCN work; estimated age (earliest publication year minus 25–30); and whether likely eligible to retire within 2 years under FERS (age 56–57 with 30 years' service, 60 with 20, 62 with 5). Show the reasoning and mark estimates as estimates.
- **Team and succession:** team size; any NOAA or NCEI succession, workforce or knowledge-transfer plan; GAO or Commerce OIG findings on NOAA's workforce; departures or retirements of the people above since 2024.
- **Knowledge held by people:** who integrates new sources and reviews Datzilla tickets; whether the processing and QC code is shared on request or held internally (including code.noaa.gov); CISESS or contractor staff on GHCN-Daily (CISESS reports 2023–2026).

For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel retirement-eligible within 2 years", P-3 "critical knowledge undocumented" and P-4 "a single person is a point of failure", and say so where nothing is published. Use NCEI's own pages, papers and ORCID or OpenAlex records ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** a row per person (role, still at NCEI or not, ORCID iD, earliest publication year and its source, first GHCN year, estimated age, likely-eligible flag with the reasoning), the current team as far as it is public, whatever succession, workforce or knowledge-transfer planning exists (or a plain "none found"), who holds the source-integration, Datzilla and code knowledge, and a supports/contradicts stance on P-1 to P-4 for each finding.

**What I changed from your draft:**
- **Earlier runs named by folder,** so the run reads exactly those records first.
- **Your context folded in:** the identity check (affiliation and co-authorship, since initials can match other researchers), the age proxy and the three FERS rules are now in the question itself; the "before about 1998" rule of thumb is left out because the run applies the FERS rules directly.
- **Rennie and Stevens kept as surnames,** with the identity check, so the run confirms rather than assumes Jared Rennie and Scott Stevens.
- **Time raised from 30 to 40 minutes (320,000 tokens):** about 14 people, each needing ORCID and publication lookups, puts this near the size where the skill picks the deep tier, and 30 minutes would leave little for the succession and code parts. Use 30/240,000 if you'd rather keep the run short; the people table is what it would thin.
- **Left out:** the answer-table layout (the skill has its own) and the source walkthrough (it picks its own).

**Hosts:** orcid.org, openalex.org (added 2026-11-22) and crossref.org are in `.claude/settings.local.json`, so the run can check publication years in two places. scholar.google.com and linkedin.com are not; the run lists any blocked hosts in `sites-to-trust.md`.

**Order and reuse:** run in this project after the GHCN-D Parts 1–4 runs (all done); it doesn't depend on Parts 7–9. For another dataset, swap the name, the people and the earlier runs it names.
