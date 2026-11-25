# GHCN-Daily gap queries

This page is a run sheet for four web research queries, one per R* category. They fill the gaps in
[ghcn-daily_categorization-gaps.md](ghcn-daily_categorization-gaps.md): the questions the first six GHCN-Daily runs never
asked. Written 2026-11-22.

**The workflow:**
1. **One session** rewrites all four queries.
2. **Four sessions**, one per query, run the research.
3. **Back here**, the results go into the categories.

## The query files

The four files are in [ghcn-daily_gap-queries/](ghcn-daily_gap-queries/). They use the same layout as your earlier query
files: `## Query to refine`, `## Claude web research skill query` and `## Claude comments about the rewritten query`.

The `Query to refine` section of each file holds three things:
- the draft query;
- context on how to search (for example ORCID and earliest publication year as an age proxy, the FERS retirement rules,
  and report numbers to look for);
- what the answer should give.

| Part | File | Category | Subcategories | Limits in the draft |
|---|---|---|---|---|
| 6 | [ghcn-d-gaps_Rstar_query_pt6_people.md](ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt6_people.md) | People risk | P-1 to P-4 | 30 min, 240,000 tokens |
| 7 | [ghcn-d-gaps_Rstar_query_pt7_data.md](ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt7_data.md) | Data risk | D-1 to D-5 | 40 min, 320,000 tokens |
| 8 | [ghcn-d-gaps_Rstar_query_pt8_infrastructure.md](ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt8_infrastructure.md) | Dependent infrastructure resilience | DIRS-1 to DIRS-5 | 40 min, 320,000 tokens |
| 9 | [ghcn-d-gaps_Rstar_query_pt9_repository.md](ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt9_repository.md) | Repository resilience | RRS-1 to RRS-5 | 40 min, 320,000 tokens |

## Step 1: rewrite all four queries in one session

Open a session in this project and paste this as one message:

```text
/my:rewrite-research-query datasets-gap-queries/ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt6_people.md datasets-gap-queries/ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt7_data.md datasets-gap-queries/ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt8_infrastructure.md datasets-gap-queries/ghcn-daily_gap-queries/ghcn-d-gaps_Rstar_query_pt9_repository.md

Rewrite all four files in one go. In each file, read the draft from "## Query to refine", including its "Context for the rewrite" and "What the answer should give" subsections. Write the rewritten question into "## Claude web research skill query", starting with the line "/my:broad-web-research", and write your notes into "## Claude comments about the rewritten query". Each of those sections replaces "(not written yet)"; leave the rest of the file as it is.

Keep these in the questions, because they define the answer:
- in Part 6 (people), the age proxy: each person's ORCID iD, earliest publication year, estimated age and whether they are likely to be retirement-eligible within 2 years under the FERS rules;
- in every part, the request to say whether each finding supports or contradicts the subcategory statements.

The earlier runs the drafts name will be in web_search_results/ where the research runs. If a question should be split into two runs, put both in the same section, labelled "Run A" and "Run B", and say why in the notes.
```

**When it's done:**
- Each file has its question under `## Claude web research skill query`.
- Read the notes under `## Claude comments about the rewritten query`, especially any suggested split or change of
  limits. Part 8 (infrastructure) is the most likely to be split, into calibration and the rest.

## Step 2: run each query in its own session

The four runs don't depend on each other, so they can go in any order, or at the same time in parallel sessions. Part 6
(people) and Part 9 (repository) are the most useful first, because P-2, RRS-2 and RRS-3 were never searched.

For each part:
1. **Open a new session** in the project where you run `/my:broad-web-research`, the one that saves results to
   `web_search_results/`.
2. **Check that the earlier runs are in its `web_search_results/`.** The questions build on them instead of repeating
   them:
   - the six GHCN-Daily runs: about-pt1, about-pt2, about-pt3_combined, funding-pt3, threats-news-pt4 and sources-pt5;
   - `2026-11-17_noaa-ncei-threats`;
   - `2026-11-18_noaa-rain-gauge-threats`.

   In this project they are under `rstar-pipeline/input/web-research/`.
3. **Paste the file's `## Claude web research skill query` section,** starting with `/my:broad-web-research`.
4. **Name the run folder to match the earlier runs:**
   - `2026-11-DD_ghcn-daily-gaps-people-pt6`
   - `2026-11-DD_ghcn-daily-gaps-data-pt7`
   - `2026-11-DD_ghcn-daily-gaps-infrastructure-pt8`
   - `2026-11-DD_ghcn-daily-gaps-repository-pt9`

## Step 3: bring the results back

1. Copy each run folder into `rstar-pipeline/input/web-research/about-datasets/ghcn-daily/`.
2. Put the matching query file in each folder, as the earlier runs have.
3. Ask me, in this project, to add the new evidence to the GHCN-Daily categories. I'll do the following:
   - update `rstar-pipeline/processing/scripts/categorize/build_ghcn-daily.py`;
   - tag each new item For, Against or Neutral;
   - rebuild the JSON and the viewer data;
   - update [ghcn-daily_categorization-gaps.md](ghcn-daily_categorization-gaps.md).
