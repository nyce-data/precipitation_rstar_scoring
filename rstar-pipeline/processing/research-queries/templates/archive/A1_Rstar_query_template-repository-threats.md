# A1 $REPOSITORY_SHORT Repository threats R* Query for Claude

About repository = $REPOSITORY_SHORT, threats to its operation and funding (shared run, once per repository)

Template written 2026-11-23 from the NCEI threats query (`archive_specific_queries/A1_Rstar_query_chatgpt-noaa_ncei.md`),
which ran as `2026-11-17_noaa-ncei-threats`, and from `rstar-pipeline/processing/research-queries/archive-query-plan.md` in precipitation_rstar_scoring.
To use it: copy it into `archive_queries/archive_specific_queries/` as `A1_Rstar_query-<repository>.md`, replace every
`$PLACEHOLDER`, rewrite it with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research`
in its own session.

**Use it only for a shared archive** that hosts datasets other groups make (such as NOAA NCEI or NASA GES DISC). When
the producer serves its own data (such as CoCoRaHS, CHRS or NASA PPS), the dataset's Part 4 already covers the
producer's funding and threats, so skip A1 and ask Part 4 to include the data site.

**Placeholders:**
- `$REPOSITORY_SHORT`: the short name, such as NOAA NCEI or NASA GES DISC.
- `$REPOSITORY`: the full name, such as "NASA's Goddard Earth Sciences Data and Information Services Center (GES DISC)".
- `$PARENTS`: its parent agencies or programs, such as "NASA, its Earth Science Division or the ESDIS project".
- `$A2_RUN`: the folder name of its A2 resilience run, if it ran first. Leave it out otherwise.
- `$SOURCES`: the parent agency's own document types, such as "NASA's budget requests, ESDIS reports, Congress's and
  GAO's documents".
- `$NOW`: the month the run happens, such as November 2026.

**Subcategories this run answers:** RRS-4, and D-1, D-3 and D-5 for the host. Every dataset the repository hosts
cites it.

**Run order:** after the repository's A2 run if possible (A2 lists its systems and who pays for them), and before
the Part 4 runs of the datasets it hosts.

## Query to refine

Using the earlier run's record on $REPOSITORY ($A2_RUN, in web_search_results/), is there an imminent or emerging
threat to its continued operation, funding, institutional support or administrative independence between January 1,
2025 and $NOW? Count actions aimed at $PARENTS as a whole only where a source ties them to $REPOSITORY_SHORT. Check four
kinds of threat without assuming any exists: political (executive orders, directives, bills); budgetary (budget
requests and enacted appropriations, freezes, contract terminations, staffing cuts); institutional (reorganizations,
transfers or consolidations, changes in oversight or data-management duties); and operational (datasets or products
retired, services interrupted, preservation stopped, infrastructure lost, public access restricted). For each, give
dates and figures (dollars, staff, datasets affected), say whether it is proposed, enacted, blocked or reversed, and rate
it imminent (enacted, ordered or already happening), emerging (proposed or reported but not in effect) or no current
threat found. Tag findings with RRS-4 "no imminent threat to the repository's funding", D-1 "program defunded or under
threat", D-3 "access infrastructure fragile or unfunded" or D-5 "subject to political suppression or alteration". Use
$SOURCES ahead of news reports, and news for events. With a time limit of 50 minutes and a token ceiling of 400,000.

### Context for the rewrite

- **This is the repository's controversy run,** so it will be deep tier. The NCEI run at 50 minutes and 400,000
  tokens used 348,000 tokens in 36 minutes.
- **The parent-agency rule matters.** Without it, every agency-wide cut counts as a threat to the repository.
- **RRS-4 points the other way.** RRS describes strengths, so evidence of a threat contradicts RRS-4.
- **Leave resilience practice to A2:** copies, checksums, disaster recovery and track record.
- **Explain where sources disagree** about the scale or status of a cut.

### What the answer should give

- A rating for each of the four kinds of threat, with dated evidence and its status.
- Figures where published, and a plain statement where none are.
- An overall rating with a confidence level.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
