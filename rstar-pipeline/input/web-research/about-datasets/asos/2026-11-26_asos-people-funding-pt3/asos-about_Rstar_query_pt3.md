# About ASOS Part 3: People R* Query for Claude

About dataset = ASOS Part 3, people, teams and the funding route

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt3_people.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_asos-people-funding-pt3`.

**Subcategories this part answers:** P-1, P-2, P-4, and the funding baseline for D-1. It also supports P-3.

**Run order:** after Part 1; before or after Part 2; before Part 4, which builds on its funding route.

## Query to refine

Using the earlier runs' records (`*_asos-about-pt1` and `*_asos-qc-formats-pt2`, in web_search_results/), who are the
people critical to running ASOS and producing its archived precipitation data now: the NWS ASOS program manager and
the program office in NWS's Office of Observations, the FAA's ASOS/AWOS program lead, the DoD counterparts, the heads
of the ASOS Operations and Monitoring Center and the Sterling Field Support Center, and the NCEI staff who produce the
1-minute, 5-minute, GHCNh and daily products? Give each one's role, employer, whether still active, ORCID iD where they
publish, and earliest publication year or career start. For each, estimate age (earliest publication year minus 25–30,
or from career dates) and whether they are likely eligible to retire within 2 years under FERS (full retirement at
56–57 with 30 years of service, 60 with 20, 62 with 5), and mark estimates as estimates. How big are the teams that
run, maintain and archive it (including the field electronics technicians), who could step in if one person left, and
is there any written succession, workforce or knowledge-transfer plan? How is the work paid for: each route (NWS's
Observations budget lines, the reimbursable tri-agency agreement, FAA facilities and equipment funds, DoD funds,
NCEI's budget for the archive, and any contracts), with award or contract numbers, amounts and years where published,
and which teams depend on each route? Leave cuts, layoffs and news from 2025 on to Part 4. Tag findings with P-1 "no
documented succession plan", P-2 "key personnel retirement-eligible within 2 years", P-4 "a single person is a point
of failure" or D-1 "program defunded or under threat". With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** Cuts and layoffs go to Part 4.
- **No names to start from.** The metadata file names only NCEI's Customer Engagement Branch as contact, and no
  earlier run named ASOS staff. Ask the run to find the current office heads from NWS, FAA and NCEI pages, org charts
  and directives (NWS directives name an office of primary responsibility).
- **A big program, so P-4 sits in the small teams.** The network has hundreds of technicians, but a single person may
  own one product at NCEI (such as the 1-minute processing) or one piece of station software. Ask about those.
- **Retirement rule:** FERS for federal staff. Contractors (such as FAA contract weather observers) have no federal
  rule; say so.
- **Confirm identities** by affiliation and co-authorship, and say which source gave each year (ORCID, OpenAlex,
  Google Scholar, Crossref, repository.library.noaa.gov). Many operations staff don't publish; use bios, directives,
  conference talks and news profiles for career dates.
- **Succession and workforce plans:** NWS and NOAA workforce plans, GAO or Commerce OIG reports on NWS staffing, and
  NCEI org charts.
- **Funding already known (`2026-11-18_noaa-rain-gauge-threats`):** NWS's operations line for Observations (ASOS,
  COOP, NEXRAD, buoys, radiosondes) was $266.8M actual FY2025 and $262.5M enacted FY2026; the procurement line for
  Observations, $36.2M actual FY2025 and $16.2M enacted FY2026. ASOS's own share was not given. Ask for what that run
  didn't find: the FAA and DoD shares and the tri-agency agreement itself.
- **No-share rule.** Where ASOS's share of a budget line isn't published, say so; don't give the parent line's total
  as ASOS's figure.

### What the answer should give

- A table of people: role, employer, active or not, ORCID iD or career dates, earliest publication year and its
  source, estimated age, and a likely-eligible flag with the reasoning.
- Team sizes, and any succession plan, or a plain statement that none was found.
- A table of funding routes with amounts, numbers and years, and the teams each pays for.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records (`*_asos-about-pt1` and `*_asos-qc-formats-pt2`, in web_search_results/), who are the
people critical to running ASOS and producing its archived precipitation data now, how big are the teams, and how is the
work paid for?

- **People:** no earlier run names any, so find the current holders from NWS, FAA and NCEI pages, org charts and
  directives (NWS directives name an office of primary responsibility): the NWS ASOS program manager and program office
  in the Office of Observations; the FAA's ASOS/AWOS program lead; the DoD counterparts; the heads of the ASOS
  Operations and Monitoring Center and the Sterling Field Support Center; and the NCEI staff who produce the 1-minute,
  5-minute, GHCNh and daily products. Look for single owners: one person running one NCEI product (such as the 1-minute
  processing) or one piece of station software. Confirm identities by affiliation and co-authorship.
- **For each person:** role, employer, whether still active, ORCID iD where they publish, and earliest publication year
  with the source that gave it (ORCID, OpenAlex, Google Scholar, Crossref, repository.library.noaa.gov); for staff who
  don't publish, career dates from bios, directives, talks or staff profiles. Estimate age as earliest publication year
  minus 25–30, or from career dates, and for federal staff whether they are likely eligible to retire within 2 years
  under FERS (full retirement at 56–57 with 30 years of service, 60 with 20, 62 with 5). For contractors, say no federal
  rule applies. Mark every estimate as an estimate.
- **Teams:** the size of the teams that run, maintain, monitor and archive it (including field electronics
  technicians), who could step in if one person left, and any written succession, workforce or knowledge-transfer plan
  (NWS and NOAA workforce plans, GAO or Commerce OIG reports on NWS staffing), or a plain statement that none was found.
- **Funding routes:** NWS's Observations budget lines, the reimbursable tri-agency agreement itself, FAA facilities and
  equipment funds, DoD funds, NCEI's budget for the archive, and any contracts, with award or contract numbers, amounts
  and years where published, and which teams depend on each. The rain-gauge run (2026-11-18_noaa-rain-gauge-threats)
  has NWS's Observations lines; find the FAA and DoD shares. Where ASOS's share isn't published, say so; don't give a
  parent line's total as ASOS's figure.

For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel
retirement-eligible within 2 years", P-4 "a single person is a point of failure" or D-1 "program defunded or under
threat"; all four are worded as risks, so "supports" means evidence the risk holds. Here D-1 is the funding baseline
only; leave developments since January 2025 to a later run. With a time limit of 40 minutes and a token ceiling of
320,000.

## Claude comments about the rewritten query

**What you'll get:** ASOS's key people with role, employer, active or not, ORCID iD or career dates, earliest
publication year and its source, estimated age and a likely-eligible flag with the reasoning (FERS for federal staff;
none for contractors); team sizes, who could step in, and any succession or workforce plan or a statement that none was
found; the funding routes with amounts, numbers and years, and the teams each pays for; and each finding tagged P-1,
P-2, P-4 or D-1 with a stance. Expect a standard-tier run.

**What changed and why:**
- **Age proxy kept in full:** ORCID iD, earliest publication year, the minus 25–30 estimate and the FERS ages, with
  career dates as the fallback for operations staff who don't publish, and every estimate marked as one.
- **Kept standard tier.** "Cuts, layoffs and news from 2025 on" became "developments since January 2025", and D-1 is
  marked as the funding baseline only. Part 4 covers staffing losses.
- **No names to start from,** so the question says where to find office heads (pages, org charts, directives) rather
  than naming candidates.
- **P-4 in the small teams.** The question asks for single owners of one product or one piece of software, since the
  network as a whole has hundreds of technicians.
- **Funding builds on the rain-gauge run.** Its NWS Observations figures ($266.8M/$262.5M operations, $36.2M/$16.2M
  procurement) are in that record; the question names the run and asks for what it didn't find (the FAA and DoD shares
  and the agreement itself), with the no-share rule.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 40 minutes and 320,000 tokens, as in your draft: three agencies' offices, several people's lookups, and
  the funding search.

**How to reuse:** run after Part 1, before or after Part 2, and before Part 4, in this project. Keep the two `*_…`
patterns until those runs exist. If the run finds few named people (operations staff often aren't named publicly),
that is itself evidence for P-1 and P-4; say so rather than rerunning.
