# CoCoRaHS: run sheet for its six research queries

Written 2026-11-23. CoCoRaHS is researched as a dataset and as its own data site (`rstar-pipeline/processing/research-queries/archive-query-plan.md` in
precipitation_rstar_scoring). It is a producer's own data site, so it gets the five dataset parts plus one A2
repository run, and no A1 threats run.

| Order | File | Topic | Tier and limits | Suggested run folder |
|---|---|---|---|---|
| 1 | [cocorahs-about_Rstar_query_pt1.md](cocorahs-about_Rstar_query_pt1.md) | Overview: hosts, observers, gauges, organizations | standard, 30 min / 240,000 | `<date>_cocorahs-about-pt1` |
| 2 | [cocorahs-about_Rstar_query_pt2.md](cocorahs-about_Rstar_query_pt2.md) | QC, the gauge standard, software, formats | standard, 30 min / 240,000 | `<date>_cocorahs-qc-formats-pt2` |
| 3 | [cocorahs-about_Rstar_query_pt3.md](cocorahs-about_Rstar_query_pt3.md) | People and the funding route | standard, 40 min / 320,000 | `<date>_cocorahs-people-funding-pt3` |
| 4 | `../../../archive_queries/archive_specific_queries/A2_Rstar_query-cocorahs.md` | The data site: copies, backups, recovery, track record | standard, 30 min / 240,000 | `<date>_cocorahs-data-site-a2` |
| 5 | [cocorahs-about_Rstar_query_pt5.md](cocorahs-about_Rstar_query_pt5.md) | Threats to its observers, gauges and systems; substitutes | deep, 40 min / 320,000 | `<date>_cocorahs-inputs-pt5` |
| 6 | [cocorahs-about_Rstar_query_pt4.md](cocorahs-about_Rstar_query_pt4.md) | Threats to the network, its staff and its site; news | deep, 50 min / 400,000 | `<date>_cocorahs-threats-news-pt4` |

Parts 2 and 3 can swap; the A2 run and Part 5 can run any time after Part 1. Part 4 goes last so it can cite the
others.

## Steps

1. **Rewrite all five dataset parts in one session** with this prompt. The A2 data-site query was already rewritten
   (2026-11-23), so it is left out:

   ```text
   /my:rewrite-research-query queries/dataset_queries/about_dataset_queries/cocorahs/cocorahs-about_Rstar_query_pt1.md queries/dataset_queries/about_dataset_queries/cocorahs/cocorahs-about_Rstar_query_pt2.md queries/dataset_queries/about_dataset_queries/cocorahs/cocorahs-about_Rstar_query_pt3.md queries/dataset_queries/about_dataset_queries/cocorahs/cocorahs-about_Rstar_query_pt4.md queries/dataset_queries/about_dataset_queries/cocorahs/cocorahs-about_Rstar_query_pt5.md

   Rewrite all five files in one go. In each file, read the draft from "## Query to refine", including its "Context for the rewrite" and "What the answer should give" subsections. Write the rewritten question into "## Claude web research skill query", starting with the line "/my:broad-web-research", and write your notes into "## Claude comments about the rewritten query". Each of those sections replaces "(not written yet)"; leave the rest of the file as it is.

   Keep these in the questions, because they define the answer: in Part 3, the age proxy (ORCID iD where they publish, earliest publication year or career dates, and estimated age; the staff are Colorado State University employees, so ask whether a CSU or Colorado PERA retirement rule is published rather than applying FERS); in every query, the request to say whether each finding supports or contradicts the subcategory statements. Keep Parts 1–3 standard tier (no cuts, threats or news). Where a file names a run folder with a `*_cocorahs-...` pattern, keep the pattern; I will fill in the real folder name once that run exists.
   ```

   Rewrite Parts 4 and 5 again after Parts 1–3 have run if you want them to name those runs exactly.
2. **Run each in its own session,** in this project, in the order above (the A2 run uses the already-rewritten
   `## Claude web research skill query` section of `A2_Rstar_query-cocorahs.md`): paste the file's
   `## Claude web research skill query` section, starting with `/my:broad-web-research`.
3. **Copy the results** into precipitation_rstar_scoring: the dataset runs into
   `rstar-pipeline/input/web-research/about-datasets/cocorahs/`, and the A2 run into `rstar-pipeline/input/web-research/archives/cocorahs/`.
4. **Before categorizing,** convert the metadata Markdown (added 2026-11-25:
   `rstar-pipeline/input/dataset-metadata/markdown/cocorahs_dataset-metadata.md`) into
   `rstar-pipeline/input/dataset-metadata/cocorahs_dataset-metadata.json` (see that folder's README), so the website shows
   its card and full name. The dataset id used here is `cocorahs`.

## Notes

- **Refreshed 2026-11-25** from the new metadata file: Parts 1–3 now mention the Data Export Portal and its CSV
  route, the 2019 QA/QC document, the METplus page and the countries covered; the A2 query's host list now includes
  data.cocorahs.org. Still not rewritten or run, except the A2 query, which was already rewritten.

- **Names in Part 3 come from Claude's own knowledge** (Nolan Doesken, Henry Reges, Russ Schumacher), not from the
  research. The query asks the run to confirm them.
- **CoCoRaHS also bears on GHCN-Daily.** Its stations are about 40% of GHCN-Daily's entries, so CoCoRaHS's Part 5 and
  A2 findings are also evidence for GHCN-Daily's DIRS-2 and DIRS-3.
