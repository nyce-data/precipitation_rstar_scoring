# About CoCoRaHS Part 3: People R* Query for Claude

About dataset = CoCoRaHS Part 3, people, team and the funding route

Written 2026-11-23 from `templates/template-dataset-about_Rstar_query_pt3_people.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_cocorahs-people-funding-pt3`.

**Subcategories this part answers:** P-1, P-2, P-4, and the funding baseline for D-1. It also supports P-3.

**Run order:** after Part 1; before or after Part 2; before Part 4, which builds on its funding route.

## Query to refine

Using the earlier runs' records (`*_cocorahs-about-pt1` and `*_cocorahs-qc-formats-pt2`, in web_search_results/), who
are the people critical to running CoCoRaHS now (its founder, national coordinator, Colorado Climate Center and state
climatologist staff, developers who run the website and database, and the volunteer state coordinators), with each
one's role, employer, whether still active, ORCID iD where they publish, and earliest publication year? For each, estimate
age (earliest publication year minus 25–30, or from career dates where they don't publish) and mark estimates as
estimates. How big is the paid staff, how long have they been in place, who could step in if one person left, and is
there any written succession, workforce or knowledge-transfer plan, including how the founder's retirement was handled?
How is the network paid for: each route (NOAA or NWS awards, NSF grants, Colorado State University support, state
partners, sponsors and donations), with award numbers, amounts and years where published, and which staff depend on
each route? Leave cuts, layoffs and news from 2025 on to Part 4. Tag findings with P-1 "no documented succession plan",
P-2 "key personnel retirement-eligible within 2 years", P-4 "a single person is a point of failure" or D-1 "program
defunded or under threat". With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** Cuts and layoffs go to Part 4.
- **People to confirm, not facts.** These names come from Claude's own knowledge, not from the research: Nolan Doesken
  (founder, former Colorado State Climatologist), Henry Reges (national coordinator) and Russ Schumacher (Colorado State
  Climatologist). Confirm each one's current role from CoCoRaHS's and CSU's pages, and add whoever the staff page
  lists now. Part 1 may name others.
- **No federal retirement rule applies.** The staff are Colorado State University employees. Give estimated ages and
  say whether a CSU or Colorado PERA rule is published; don't apply FERS.
- **Where to find ORCID iDs and earliest publication years:** ORCID (orcid.org, pub.orcid.org), OpenAlex
  (api.openalex.org), Google Scholar, Crossref. Some staff won't publish; use CSU staff pages, CVs and news profiles for
  career dates instead.
- **A small paid staff** runs a network of thousands of volunteers, so P-4 (single point of failure) is the key
  question.
- **Where to look for funding:** USAspending.gov (the rain-gauge run found NOAA awards of $1.17M for 2006–10 and $1.25M
  for 2010–15, and no current route), NSF's award search, CSU's annual reports and the Colorado Climate Center's pages,
  and the sponsors page. Where an amount isn't published, say so.

### What the answer should give

- A table of people: role, employer, active or not, ORCID iD or career dates, earliest publication year and its
  source, and estimated age.
- The paid staff's size, and any succession plan, or a plain statement that none was found.
- A table of funding routes with amounts, award numbers and years, and the staff each pays for.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
