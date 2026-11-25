# About $DATASET_SHORT Part 3: People R* Query for Claude

About dataset = $DATASET_SHORT Part 3, people, team and the funding route

Template written 2026-11-23 from `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` in precipitation_rstar_scoring. To use it:
copy it into the dataset's folder as `<dataset>-about_Rstar_query_pt3.md`, replace every `$PLACEHOLDER`, rewrite it
with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session.

**Placeholders:**
- `$DATASET_SHORT`: the short name, such as GHCN-D.
- `$DATASET`: the short and full names.
- `$EARLIER_RUNS`: the folder names of this dataset's Part 1 and Part 2 runs.
- `$PEOPLE`: the people Part 1 and the dataset's citation name (principal investigators, developers, maintainers,
  citation authors). Leave it out if Part 1 named none.
- `$RETIREMENT_RULES`: the employer's retirement rules. For US federal staff: "FERS (full retirement at 56–57 with 30
  years of service, 60 with 20, 62 with 5)". For university staff, say the run should note when no rule applies.

**Subcategories this part answers:** P-1, P-2, P-4, and the funding baseline for D-1. It also supports P-3.

**Run order:** after Part 1. It can run before or after Part 2. Run it before Part 4, which builds on its funding
route.

## Query to refine

Using the earlier runs' records ($EARLIER_RUNS, in web_search_results/), who are the people critical to producing and
quality-controlling $DATASET now (its principal investigators, developers and maintainers, starting from $PEOPLE), with
each one's role, employer, whether still active, ORCID iD and earliest publication year? For each, estimate age
(earliest publication year minus 25–30) and whether they are likely eligible to retire within 2 years under
$RETIREMENT_RULES, and mark estimates as estimates. How big is the team, how long has it existed, who could step in if
one person left, and is there any written succession, workforce or knowledge-transfer plan? How is the work paid for:
each route (appropriation line, program, grant, cooperative agreement or contract), with award numbers, amounts and
years where published, and which people depend on each route? Leave cuts, layoffs and news from 2025 on to Part 4. Tag
findings with P-1 "no documented succession plan", P-2 "key personnel retirement-eligible within 2 years", P-4 "a
single person is a point of failure" or D-1 "program defunded or under threat". With a time limit of 40 minutes and a
token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** The funding route is a fact-finding question. Cuts and layoffs go to Part 4, so the
  skill doesn't pick its costly deep tier. GHCN-Daily's funding run stayed standard this way.
- **Limits.** 40 minutes and 320,000 tokens, because the ORCID lookups and the funding route are two searches in one
  run. If the first Part 3 for a dataset stops well under the ceiling, use 30 minutes and 240,000 next time.
- **Confirm identities.** Initials can match more than one researcher. Confirm each person by affiliation and by
  co-authorship on the dataset's papers.
- **Where to find ORCID iDs and earliest publication years:**
  - ORCID public search (orcid.org) or the ORCID API (pub.orcid.org);
  - OpenAlex (api.openalex.org, author search, then the oldest work);
  - Google Scholar, Crossref, or an agency repository (such as repository.library.noaa.gov or NASA's NTRS).

  ORCID records are often incomplete, so check one other source as well. Say which source gave each year.
- **Start year on the dataset.** Record each person's first year on the dataset's papers or staff, from bios, CVs
  or paper affiliations.
- **Succession and workforce plans.** Look for the agency's or university's workforce and succession plans, GAO or
  Inspector General reports on the agency's workforce, a current org chart, and cooperative institute annual reports
  that name the dataset's staff.
- **No-share rule for funding.** Where the dataset's own share of a budget line isn't published, say so. Don't
  give the parent line's total as the dataset's figure.
- **Where to look for funding:** the agency's budget documents (congressional justifications), USAspending.gov,
  the agency's award databases (such as NASA's NSPIRES or NSF's award search), SAM.gov, and the dataset's own
  acknowledgments.

### What the answer should give

- A table of people with their role, employer, ORCID iD, earliest publication year (and its source), estimated age,
  and a likely-eligible flag, with the reasoning.
- The team size and history, and any succession plan, or a plain statement that none was found.
- A table of funding routes with amounts, award numbers and years, and the people each pays for.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
