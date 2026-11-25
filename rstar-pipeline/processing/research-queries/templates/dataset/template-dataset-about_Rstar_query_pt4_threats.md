# About $DATASET_SHORT Part 4: Threats R* Query for Claude

About dataset = $DATASET_SHORT Part 4, threats to the dataset, its producers and its hosts

Template written 2026-11-23 from `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` in precipitation_rstar_scoring. To use it:
copy it into the dataset's folder as `<dataset>-about_Rstar_query_pt4.md`, replace every `$PLACEHOLDER`, rewrite it
with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session.

**Placeholders:**
- `$DATASET_SHORT`: the short name, such as GHCN-D.
- `$DATASET`: the short and full names.
- `$EARLIER_RUNS`: the folder names of this dataset's Parts 1–3 runs.
- `$SHARED_RUNS`: the shared repository runs for each host in Part 1's list (A1 threats and A2 resilience), such as
  `2026-11-17_noaa-ncei-threats`. A producer's own data site has an A2 run but no A1.
- `$NOW`: the month the run happens, such as November 2026.

**Subcategories this part answers:** D-1, D-3, D-5 and RRS-4, plus staff losses for P-2 and P-4.

**Run order:** last of the five, after Part 3 and after the shared repository runs, so this run can build on them.

## Query to refine

Using the earlier runs' records ($EARLIER_RUNS) and the shared runs ($SHARED_RUNS), all in web_search_results/, has
funding for $DATASET, the groups that produce it and the systems that serve it been stable, cut or threatened between
January 1, 2025 and $NOW, including proposed termination or retirement of the dataset or its products and budget
uncertainty? What layoffs, buyouts, hiring freezes, reorganizations or contract changes have affected the people and
groups that produce or serve it? Has the dataset or its access systems faced outages, access limits, removal, alteration
or political pressure? What news from 2024 to $NOW names the dataset, its group or its people, and does each item name
them directly or only the parent agency? Rate each development imminent, emerging or no current threat found; count
agency-wide actions only where a source ties them to this dataset; and say what each could mean for its updates and
availability. Tag findings with D-1 "program defunded or under threat", D-3 "access infrastructure fragile or
unfunded", D-5 "subject to political suppression or alteration", RRS-4 "no imminent threat to the host's funding", P-2
"key personnel retirement-eligible" or P-4 "a single person is a point of failure". With a time limit of 50 minutes and
a token ceiling of 400,000.

### Context for the rewrite

- **This is the dataset's one controversy run.** Funding cuts, staff losses and news are all asked here, so they
  aren't searched twice. Earlier splits put funding and news in separate runs that searched the same budget fights.
- **Limits.** 50 minutes and 400,000 tokens. The deep runs at 40 minutes and 320,000 filled their ceilings, and
  GPCP's funding-and-news run needed the full 50 minutes.
- **Build on the shared runs.** The host's agency-wide budget and staff losses are in the A1 run. Ask this run to
  add only what ties to this dataset, its producers and its access systems, rather than finding the agency budget
  again.
- **Rating scale, the same in every R* query:** imminent (enacted, ordered or already happening), emerging (proposed
  or reported but not in effect), or no current threat found.
- **Check news against documents.** Use the agency's, Congress's, GAO's and court documents to check what news
  claims, and news for events.
- **Date ranges.** Funding and staff from January 1, 2025; news from January 2024. If a budget decision is pending
  (such as a continuing resolution's end date), ask for its outcome if decided.
- **Producer's own data site.** If the producer serves the data from its own site (such as CoCoRaHS, or CHRS for
  PERSIANN-CDR), ask about that site's funding, staff cuts and outages here, since there is no A1 threats run for it.
  Its practice (copies, checksums, disaster recovery, track record) goes in its A2 run.

### What the answer should give

- A dated table of funding developments, with figures and a rating each.
- Staff changes that touch the dataset's work, with numbers where published.
- A list of news items: outlet, date, headline, and whether each names the dataset or only the agency.
- What each development could mean for the dataset, and an overall rating.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
