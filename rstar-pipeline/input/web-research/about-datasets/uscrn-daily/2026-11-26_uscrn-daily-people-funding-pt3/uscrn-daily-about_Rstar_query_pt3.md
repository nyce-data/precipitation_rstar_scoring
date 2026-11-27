# About USCRN Daily Part 3: People R* Query for Claude

About dataset = USCRN Daily Part 3, people, team and the funding route

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt3_people.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_uscrn-daily-people-funding-pt3`.

**Subcategories this part answers:** P-1, P-2, P-4, and the funding baseline for D-1. It also supports P-3.

**Run order:** after Part 1; before or after Part 2; before Part 4, which builds on its funding route.

## Query to refine

Using the earlier runs' records (`*_uscrn-daily-about-pt1` and `*_uscrn-daily-qc-formats-pt2`, in
web_search_results/), who are the people critical to producing and quality-controlling USCRN Daily now (its program
manager, the NCEI scientists who run its processing and QC, the ATDD lead and the field team that maintains the
stations, and cooperative-institute staff who work on it), starting from Howard Diamond and the authors of the
network's papers? Give each one's role, employer, whether still active, ORCID iD and earliest publication year. For
each, estimate age (earliest publication year minus 25–30) and whether they are likely eligible to retire within 2
years under FERS (full retirement at 56–57 with 30 years of service, 60 with 20, 62 with 5), and mark estimates as
estimates. How big is the team, how long has it existed, who could step in if one person left, and is there any
written succession, workforce or knowledge-transfer plan? How is the work paid for: each route (the appropriation line
for station operations at OAR's Air Resources Laboratory, NESDIS/NCEI's line for the data, cooperative agreements and
contracts), with award numbers, amounts and years where published, and which people depend on each route? Leave cuts,
layoffs and news from 2025 on to Part 4. Tag findings with P-1 "no documented succession plan", P-2 "key personnel
retirement-eligible within 2 years", P-4 "a single person is a point of failure" or D-1 "program defunded or under
threat". With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** Cuts and layoffs go to Part 4, including the ARL closure proposals.
- **People to confirm, not facts.**
  - Howard Diamond is named as USCRN program manager in the metadata file (a ChatGPT answer) and is lead author of
    the 2013 BAMS paper; confirm his current role.
  - These come from Claude's own knowledge, not from the research: Michael Palecki (NCEI), Ronald Leeper (cooperative
    institute at NC State, working with NCEI) and Bruce Baker (ATDD). Confirm each one's current role, and add whoever
    the current pages and recent papers name.
- **Retirement rules.** FERS for NOAA staff. Cooperative-institute staff are university employees: give estimated ages
  and say whether a university rule is published; don't apply FERS.
- **A small field team is the P-4 question.** ATDD's eight technicians and engineers make the annual visits to every
  station (`2026-11-23_ghcn-daily-infrastructure-pt8`). Ask who leads it and who could replace them.
- **Confirm identities** by affiliation and co-authorship, and say which source gave each year (ORCID, OpenAlex,
  Google Scholar, Crossref, repository.library.noaa.gov).
- **Funding already searched:** `2026-11-18_noaa-rain-gauge-threats` found no budget line for USCRN in any budget
  document. Ask the run to look in older congressional justifications (USCRN had its own line in earlier NOAA
  budgets), NOAA's budget "blue books", USAspending.gov for cooperative agreements, and ARL's and NCEI's annual
  reports. Where an amount isn't published, say so; don't give the parent line's total as USCRN's figure.

### What the answer should give

- A table of people: role, employer, active or not, ORCID iD, earliest publication year and its source, estimated
  age, and a likely-eligible flag with the reasoning.
- The team's size and history, and any succession plan, or a plain statement that none was found.
- A table of funding routes with amounts, award numbers and years, and the people each pays for.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records (`*_uscrn-daily-about-pt1` and `*_uscrn-daily-qc-formats-pt2`, in
web_search_results/), who are the people critical to producing, quality-controlling and maintaining USCRN Daily (the
U.S. Climate Reference Network's daily01 product) now, how big is the team, and how is the work paid for?

- **People:** the program manager, the NCEI scientists who run its processing and QC, the ATDD lead and the leader of
  the field team that maintains the stations, and cooperative-institute staff who work on it. Start from Howard
  Diamond (reported as program manager) and the authors of the network's papers. Check Michael Palecki (NCEI), Ronald
  Leeper (NC State cooperative institute) and Bruce Baker (ATDD) as candidates, without assuming any is still
  involved, and add whoever the current pages and recent papers name. Confirm identities by affiliation and
  co-authorship.
- **For each person:** role, employer, whether still active, ORCID iD, and earliest publication year with the source
  that gave it (ORCID, OpenAlex, Google Scholar, Crossref, repository.library.noaa.gov). Estimate age as earliest
  publication year minus 25–30. For NOAA staff, say whether they are likely eligible to retire within 2 years under
  FERS (full retirement at 56–57 with 30 years of service, 60 with 20, 62 with 5). For cooperative-institute
  (university) staff, give the estimated age and say whether a university rule is published; don't apply FERS. Mark
  every estimate as an estimate.
- **Team:** its size and history, who could step in if one person left (above all in ATDD's eight-person field team,
  and who leads it), and any written succession, workforce or knowledge-transfer plan, or a plain statement that none
  was found.
- **Funding routes:** each route with award numbers, amounts and years where published, and which people depend on
  each: the ARL (OAR) line for station operations, NESDIS/NCEI's line for the data, cooperative agreements and
  contracts. Look in older NOAA congressional justifications (USCRN once had its own line), NOAA's budget "blue
  books", USAspending.gov, and ARL's and NCEI's annual reports. Say where no amount is published; don't give a parent
  line's total as USCRN's figure.

For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel
retirement-eligible within 2 years", P-4 "a single person is a point of failure" or D-1 "program defunded or under
threat"; all four are worded as risks, so "supports" means evidence the risk holds. Here D-1 is the funding baseline
only; leave developments since January 2025 to a later run. With a time limit of 40 minutes and a token ceiling of
320,000.

## Claude comments about the rewritten query

**What you'll get:** a list of USCRN Daily's key people with role, employer, active or not, ORCID iD, earliest
publication year and its source, estimated age and a likely-eligible flag with the reasoning (FERS for NOAA staff only);
the team's size and history, who could step in, and any succession plan or a statement that none was found; the
funding routes with amounts, award numbers and years, and the people each pays for; and each finding tagged P-1, P-2,
P-4 or D-1 with a stance. Expect a standard-tier run.

**What changed and why:**
- **Age proxy kept in full:** ORCID iD, earliest publication year, the minus 25–30 estimate and the FERS ages, with
  every estimate marked as one.
- **Kept standard tier.** "Cuts, layoffs and news from 2025 on" became "developments since January 2025", and D-1 is
  marked as the funding baseline only, so the wording doesn't push the run to deep. Part 4 covers the ARL closure
  proposals.
- **Names as candidates.** Howard Diamond (from the metadata file) and Palecki, Leeper and Baker (from my own
  knowledge, not the research) are to confirm, "without assuming any is still involved".
- **University staff kept off FERS,** as in your context notes.
- **Funding sources named.** The rain-gauge run found no USCRN line in recent budgets, so the question points at older
  justifications, the blue books, USAspending.gov and annual reports, and warns against using a parent line's total.
  I didn't restate the rain-gauge run's finding; the run reads that record first.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 40 minutes and 320,000 tokens, as in your draft: several people's ORCID and publication lookups plus
  the funding search.

**How to reuse:** run after Part 1, before or after Part 2, and before Part 4, in this project. Keep the two `*_…`
patterns until those runs exist. If Part 2 hasn't run yet, the run simply finds no record for it.
