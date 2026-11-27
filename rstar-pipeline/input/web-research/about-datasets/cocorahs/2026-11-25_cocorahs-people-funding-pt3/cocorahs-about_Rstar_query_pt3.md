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
  lists now. Part 1 may name others. The metadata file (a ChatGPT answer, 2026-11-25) also names Doesken as founder and
  Reges as national coordinator, which is still not confirmation.
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

/my:broad-web-research

Using the earlier runs' records (`*_cocorahs-about-pt1` and `*_cocorahs-qc-formats-pt2`, in web_search_results/), who
are the people critical to running CoCoRaHS now, how big is its paid staff, and how is the network paid for?

- **People:** its founder, national coordinator, Colorado Climate Center and state climatologist staff, the developers
  who run the website and database, and the volunteer state coordinators. Check Nolan Doesken (founder, former Colorado
  State Climatologist), Henry Reges (national coordinator) and Russ Schumacher (Colorado State Climatologist) as
  candidates, without assuming each still holds that role, and add whoever CoCoRaHS's staff page and CSU's pages list
  now. Confirm identities by affiliation and co-authorship.
- **For each person:** role, employer, whether still active, ORCID iD where they publish, and earliest publication year
  with the source that gave it (ORCID, OpenAlex, Google Scholar, Crossref); for staff who don't publish, career dates
  from CSU staff pages, CVs or staff profiles. Estimate age as earliest publication year minus 25–30, or from career
  dates. The staff are Colorado State University employees, so don't apply FERS: say whether a CSU or Colorado PERA
  retirement rule is published, and if so whether each person is likely eligible within 2 years. Mark every estimate
  as an estimate.
- **Team:** the paid staff's size and how long they have been in place, who could step in if one person left (a small
  staff runs thousands of volunteers), and any written succession, workforce or knowledge-transfer plan, including how
  the founder's retirement was handled; or a plain statement that none was found.
- **Funding routes:** NOAA or NWS awards, NSF grants, Colorado State University support, state partners, sponsors and
  donations, with award numbers, amounts and years where published, and which staff depend on each. The rain-gauge run
  (2026-11-18_noaa-rain-gauge-threats) found NOAA awards for 2006–10 and 2010–15 and no current route; look for what it
  didn't find on USAspending.gov, NSF's award search, CSU's annual reports and the sponsors page. Say where no amount
  is published.

For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel
retirement-eligible within 2 years", P-4 "a single person is a point of failure" or D-1 "program defunded or under
threat"; all four are worded as risks, so "supports" means evidence the risk holds. Here D-1 is the funding baseline
only; leave developments since January 2025 to a later run. With a time limit of 40 minutes and a token ceiling of
320,000.

## Claude comments about the rewritten query

**What you'll get:** CoCoRaHS's key people with role, employer, active or not, ORCID iD or career dates, earliest
publication year and its source, and estimated age, with a likely-eligible flag only if a CSU or PERA rule is
published; the paid staff's size, who could step in, and any succession plan (including the founder's handover) or a
statement that none was found; the funding routes with amounts, award numbers and years, and the staff each pays for;
and each finding tagged P-1, P-2, P-4 or D-1 with a stance. Expect a standard-tier run.

**What changed and why:**
- **Age proxy kept in full:** ORCID iD where they publish, earliest publication year or career dates, and the minus
  25–30 estimate, every estimate marked as one.
- **CSU/PERA, not FERS.** The question asks whether a CSU or Colorado PERA rule is published and applies it only if
  so, since P-2 needs an eligibility judgment.
- **Kept standard tier.** "Cuts, layoffs and news from 2025 on" became "developments since January 2025", D-1 is
  marked as the funding baseline only, and "news profiles" became "staff profiles". Part 4 covers grant
  terminations.
- **Names as candidates.** Doesken, Reges and Schumacher come from my own knowledge (and the metadata file, a ChatGPT
  answer), so they are to confirm.
- **Funding builds on the rain-gauge run.** Its two NOAA awards ($1.17M and $1.25M) are in that record; the question
  names the run and asks for current routes.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 40 minutes and 320,000 tokens, as in your draft.

**How to reuse:** run after Part 1, before or after Part 2, and before Part 4 and the A2 data-site run, in this
project. Keep the two `*_…` patterns until those runs exist.
