# Create R* JSON with information supporting subcategories

## Break down Answer files by R* category

### Structure

There are 4 top categories called "People risk", "Data risk", "Dependent infrastructure resilience", and "Repository resilience".

As an example of the format of each top category, the overall definition of the "People risk" category is described under the header "## People Risk defined" in rstar-pipeline/input/framework/definitions/p-rstar_people_risk_queries.md and definitions of the subcategories of people risk are under the header "## Subcategories". The subcategories are in the H3 headers under the H2 Subcategories header, e.g. "### P-1" for the P-1 subcategory. The description for a subcategory to match on is under "#### Description" and ideas on how to find matches are described under the header "#### How to find".

The subcategories of the People risk category are P-1, P-2, P-3, and P-4.

The subcategories of the Data risk category are D-1, D-2, D-3, D-4, and D-5.

The subcategories of the Dependent infrastructure resilience category are DIRS-1, DIRS-2, DIRS-3, DIRS-4, and DIRS-5.

The subcategories of the Repository resilience category are RRS-1, RRS-2, RRS-3, RRS-4, and RRS-5.


### Goal

Looking for background information for each subcategory so that a decision can be made as to whether the subcategory statement is true or false or unknown or partially known. So any background information that can help make a decision about the subcategory definition should be included. There are categories and subcategories about 1) the data repositories the datasets are stored in (Repository resilience), 2) the instruments, platforms, and programs that are used to take the data and process it (Dependent infrastructure resilience), 3) the people involved with the dataset (People), and 4) the data themselves and how it is measured/created, processed, and quality checked.

For each dataset in the folder rstar-pipeline/input/web-research/about-datasets/, reformat the text in the files of the form answer_*.md in each dataset folder into text that fits each subcategory defined above. Add text to a subcategory even if it is of low confidence as long as it is relevant to a subcategory. Some subcategories may not have relevant text, in that case, leave it empty. Some text from the web research may not fit any category, in that case, leave it out.

Save the results as a JSON file in the folder rstar-pipeline/output/categories/ and the corresponding dataset folder, e.g. GHCN Daily is ghcn-daily/.

The JSON file will have four top level keys people_risk, data_risk, dep_infra_resilience, and repo_resilience. Then for the people_risk key, there will be JSON with the keys P-1, P-2, P-3, and P-4, and a similar pattern for the other subcategories. For each subcategory key, there will be a value containing the reformatted text as html inside a div with a class using the lowercase name of the subcategory key, e.g. `<div class="p-1">`.


### Tags, scores and the dataset key (added 2026-11-23)

The rules for filing evidence are in `rstar-pipeline/input/framework/rstar-categorization-decisions.md`, and
`rstar-pipeline/processing/scripts/categorize/rstar_common.py` writes this format.

- **Subcategory div:** `<div class="p-1" data-score="35" data-score-basis="for-only" data-status="found">`.
  - `data-score` is the points, 0 or `NA` (see `rstar-pipeline/input/framework/how_to_score_rstar.md`).
  - `data-score-basis` says why: `for-only`, `against-only`, `both` or `none`.
  - `data-status` is `found` when there is any evidence; otherwise the strongest gap status.
  - RRS divs also have `data-repositories`, the dataset's repositories and their roles.
- **Evidence item:** `<li data-stance="for" data-confidence="high" data-source="<run folder>">`.
  - `data-stance` is `for`, `against` or `context` (formerly `neutral`).
  - RRS items also have `data-repository`, the repository the item is about.
- **Gap item:** `<li data-status="not-public">`, with status `searched-none-found`, `not-public` or `not-searched`.
- **`dataset` key** (a fifth top-level key): `producer`, `producer_is_repository` (true or false) and `repositories`,
  a list of `{"name", "role"}` with role `parent`, `child` or `producer site`.
