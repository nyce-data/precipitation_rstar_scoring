# R* research query templates: a guide for datasets and archives

How the research queries for scoring climate datasets on the R* risk framework were built, what the templates are,
and how to adapt them to other datasets. Written 2026-11-23 from work on four precipitation datasets (GHCN-Daily, GPCP
Daily, IMERG Late Run, PERSIANN-CDR Daily) and one new one (CoCoRaHS).

## What the queries are for

The R* framework scores how much risk a dataset carries of becoming unavailable or unreliable. It has four groups and 19
subcategories:

| Group | Subcategories | Asks about |
|---|---|---|
| **P**, People risk | P-1 to P-4 | Succession plans, people near retirement, knowledge held by one person, single points of failure |
| **D**, Data risk | D-1 to D-5 | Defunding, storage single points of failure, fragile access systems, obsolete formats, political pressure |
| **DIRS**, Dependent infrastructure resilience | DIRS-1 to DIRS-5 | Calibration facilities, observing networks and satellites, upstream data feeds, outside processing, no alternative supplier |
| **RRS**, Repository resilience | RRS-1 to RRS-5 | Geographic copies, checksum checks, a tested disaster recovery plan, stable funding, a track record through disruptions |

P, D and DIRS describe **risks**. RRS describes **strengths**, so evidence "for" an RRS statement means resilience.

Each subcategory has a definition file with a Description and a "How to find" text (`rstar-pipeline/input/framework/definitions/`). The queries
gather web evidence for every subcategory. A person then reads the evidence and decides each one.

The research is done with two Claude Code skills:
- **`broad-web-research`** runs a question across many web sources, with a time limit and a token ceiling, and saves an
  answer and a research record.
- **`rewrite-research-query`** turns a rough draft into a well-formed question for that skill.

## What the first round taught

The first four datasets were researched with a single long "about the dataset" question, split by ChatGPT into five
parts. GHCN-Daily then needed four more gap runs, ten sessions in all. Reading the research records showed why:

1. **The token ceiling, not the time limit, decides when a run stops.** Runs stop at about 80% of the token ceiling and
   finish in 60–75% of the time given.

   | Limits given | Tier | Tokens used | Minutes used |
   |---|---|---|---|
   | 30 min / 240,000 | standard | 141,000–197,000 | 14–23 |
   | 40 min / 320,000 | deep | 213,000–288,000 | 26–29 |
   | 50 min / 400,000 | deep | 333,000–371,000 | 31–36 |

2. **Words about cuts, threats or layoffs make a run expensive.** The research skill picks its deep tier when a question
   involves a dispute. A funding question that left cuts to another run stayed standard.
3. **Some subcategories were never asked.** None of the 24 first-round runs asked about people's ages or retirement
   (P-2), checksums (RRS-2) or disaster recovery plans (RRS-3), and calibration labs (DIRS-1) came up rarely. The
   starting question simply didn't contain those questions.
4. **Funding, threats and news were split over two or three runs** that searched the same budget fights.
5. **Repository questions repeat across datasets.** One archive (NOAA NCEI) holds three of the five datasets, so asking
   about its checksums inside each dataset's research would search the same thing three times.

## The design

### Five parts per dataset

Each part's draft is written from the subcategories' "How to find" text, so every subcategory has a part that asks it.

| Part | Topic | Tier and limits | Main subcategories |
|---|---|---|---|
| 1 | Overview: where it is kept and served, its inputs, who makes it | standard, 30 min / 240,000 | RRS-1, D-2, DIRS-3, DIRS-4 |
| 2 | Quality control, calibration, code, formats (with FAIR tests) | standard, 30 min / 240,000 | D-4, P-3, DIRS-1, DIRS-4 |
| 3 | People (ORCID, estimated age, retirement eligibility), team, who pays | standard, 40 min / 320,000 | P-1, P-2, P-4 |
| 4 | Threats to the dataset, its producers and its hosts; news | deep, 50 min / 400,000 | D-1, D-3, D-5, RRS-4 |
| 5 | Threats to its inputs, and substitutes | deep, 40–50 min / 320,000–400,000 | DIRS-2, DIRS-3, DIRS-5 |

**Rules that keep the cost down:**
- Parts 1–3 say "leave cuts, threats and news to Part 4", so they stay standard tier.
- Part 4 is the dataset's only controversy run; Part 5 is the only one for its inputs.
- Later parts name the earlier runs' folders ("Using the earlier runs' records on …") and say "add to what those runs
  found rather than repeating it".
- Each part ends by asking the run to tag each finding with the subcategory it bears on, and to say whether it
  supports or contradicts that subcategory's statement. This makes sorting the evidence much faster.
- Shared wording carries across every query: the same rating scale (imminent / emerging / no current threat found),
  the same FAIR tests, the rule to count agency-wide actions only where a source ties them to the dataset, and the rule
  not to give a parent budget line's total as the dataset's own figure.

**Order:** Part 1 first; Parts 2, 3 and 5 in any order; Part 4 last.

### Three kinds of repository

Repository questions go in their own runs, sorted by what kind of host it is:

| Kind | Examples | Runs |
|---|---|---|
| **Shared archive:** hosts datasets other groups make | NOAA NCEI, NASA GES DISC | **A1 threats** (deep, 50 min / 400,000) and **A2 resilience** (standard, 40 min / 320,000), once per archive |
| **Producer's own data site:** the group that makes the data also serves it | CoCoRaHS, UC Irvine CHRS, NASA PPS | **A2 only** (standard, 30–40 min), with questions about the site's own team. Its funding and threats go in the dataset's Part 4 |
| **Copy:** a mirror, cloud bucket or redistributor | NOAA's cloud buckets on AWS and Google, Earth Engine, community mirrors | **No run.** The dataset's own research checks whether each copy exists and is current |

Every dataset an archive holds cites that archive's A1 and A2 runs, so an archive is researched once. Keep a register
of repositories (which datasets each holds and which runs exist).

**Why not put repository questions inside the dataset parts?** The dataset parts already use nearly their whole token
budget; repository questions there never got asked; and shared archives would be searched again for every dataset.

### Shared instrument runs

Runs on families of instruments (for example a country's rain-gauge networks, or one agency's satellites) are also done
once and cited by every dataset that uses them, in Part 5.

**Session count:** a dataset whose archive already has A1 and A2 needs 5 sessions; one with its own data site needs 6;
one in a new shared archive needs 7, and the next dataset there needs 5.

### Filling gaps in research that already exists

For a dataset already researched another way, check its runs against the 19 subcategories (a coverage check), write a
short gaps note, and write one "people and production" gap query plus any missing repository runs. Categorize only
once, after the gap runs come back, so nothing is categorized twice.

## The files

| File | What it is |
|---|---|
All but the first are in this folder, `rstar-pipeline/processing/research-queries/`:

| File | What it is |
|---|---|
| `rstar-pipeline/input/framework/definitions/*.md` | The 19 subcategory definitions, one file per group |
| `templates/dataset/template-dataset-about_Rstar_query_pt1_overview.md` … `pt5_inputs.md` | The five dataset templates |
| `templates/archive/A1_Rstar_query_template-repository-threats.md` | A1 threats template, for a shared archive |
| `templates/archive/A2_Rstar_query_template-repository-resilience.md` | A2 resilience template, for both repository kinds |
| `templates/instrument/A4_Rstar_query_*.md` | The instrument queries (rain gauges, NASA and NOAA satellites); copy one as a model for a new instrument family |
| `dataset-query-5-part-plan.md` | The plan behind the five parts, with the measured run costs |
| `archive-query-plan.md` | The plan behind the repository runs, with the register and a worked case |
| `examples/` | Filled-in queries: CoCoRaHS's five parts and run sheet (`examples/cocorahs/`), and the A2 queries for NCEI, NASA GES DISC and PPS, UC Irvine CHRS and CoCoRaHS (`examples/archive/`) |

The templates and examples are copies (made 2026-11-25) from the separate `Rstar_query_results` project, where the
queries are rewritten and run: there the templates live under `queries/dataset_queries/about_dataset_queries/templates/`,
`queries/archive_queries/general_archive_queries/` and `queries/instrument_queries/`. If a template changes there,
copy it here again. Each finished run folder in `rstar-pipeline/input/web-research/` also keeps the exact query it ran.

**Every template has the same layout:**
- a header with its placeholders (`$DATASET`, `$HOSTS`, `$CANDIDATES`, `$NOW` …), the subcategories it answers and its
  run order;
- `## Query to refine`: the draft question, about five sentences, ending with the subcategory tags and the limits;
- `### Context for the rewrite`: notes for the rewrite skill, such as how to keep the tier down, where to look, and
  what not to search again;
- `### What the answer should give`;
- empty `## Claude web research skill query` and `## Claude comments about the rewritten query` sections, which the
  rewrite skill fills.

## How to use them for a new dataset

1. **Copy the five dataset templates** into a folder for the dataset and replace the placeholders. Leave the
   later parts' earlier-run names as patterns until those runs exist.
2. **Rewrite all the files in one session** with `/rewrite-research-query`, passing every file at once.
3. **Run Part 1** with `/broad-web-research`, in its own session.
4. **Sort Part 1's hosts** into the three repository kinds and check the register. Write A1 and A2 for a new shared
   archive, or A2 for a producer's own data site.
5. **Run Parts 2, 3 and 5 and the repository runs,** each in its own session; then **Part 4** last.
6. **Sort the evidence** into the 19 subcategories, using the dataset's own runs plus the shared repository and
   instrument runs that apply.

## Adapting to other climate data

The templates were written for precipitation. Most of the wording is general, but these parts need changing for other
kinds of climate data (temperature, sea ice, ocean, atmospheric composition, reanalysis, model output):

- **Kinds of dataset (Part 1):** the templates name three (one instrument, a compilation of station networks, a blend
  of satellites and gauges). Add the kinds you meet, such as reanalysis (a model fed by many observations), model
  output, or a derived index.
- **Calibration examples (Part 2):** there is one line for station data and one for satellites. Add the right kind of
  facility, such as reference labs for gas standards (for example NOAA's Global Monitoring Laboratory), ocean float and
  buoy calibration, or ice-core and tree-ring dating labs.
- **Retirement rules (Part 3):** the US federal FERS rule is written in. Use the employer's rules (other countries'
  public services, universities), or ask only for estimated ages where none is published.
- **Candidate inputs (Part 5):** list the networks, satellites, floats, models or input datasets for your dataset. Keep
  the phrase "without assuming any is affected".
- **Agencies, documents and dates:** the threat parts name US sources (Congress, GAO, inspectors general, USAspending)
  and the window January 2025 to now. Swap in the producer's own government, funders and document types, and the window
  you care about.
- **The definitions themselves:** if a subcategory doesn't fit your data, change its "How to find" text first; the
  templates follow from it.
- **Limits:** start with the limits above, then adjust from your own runs' records (tokens used against the ceiling).

## Prompt to start with

Paste this into a new Claude Code session opened in the repository, after replacing the bracketed parts. It asks Claude
to read the design, adapt the templates to your field, and write the first dataset's queries.

```text
I want to score climate datasets on the R* risk framework using web research. Read
rstar-pipeline/processing/research-queries/rstar-query-templates-guide.md first, then rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md, rstar-pipeline/processing/research-queries/archive-query-plan.md, every
file in rstar-pipeline/input/framework/definitions/, and the templates in rstar-pipeline/processing/research-queries/templates/. Use the files in rstar-pipeline/processing/research-queries/examples/ as models of filled-in queries.

My datasets are: [list each dataset with its full name and a link, e.g. "HadCRUT5 (Met Office Hadley Centre / CRU
global temperature) https://..."]. They are [kind of climate data, e.g. surface temperature compilations].

1. Tell me which parts of the templates and definitions don't fit these datasets (kinds of dataset, calibration
   examples, retirement rules, candidate inputs, agencies and date windows), and propose changes. Ask me before
   changing any subcategory definition.
2. After I agree, update the templates, keeping their layout, the five-part split, the tier rules (no cuts, threats or
   news in Parts 1-3 and A2) and the subcategory tags.
3. Then, for the first dataset only, copy the five templates into a folder named for it, fill in every placeholder,
   and write a run sheet: the order of the runs, the limits for each, and a suggested run folder name.
4. Don't run any research yet. Mark any name or fact you add from your own knowledge, rather than from a source, as
   "to confirm".
```

**After Part 1 runs,** use this to set up the repository runs:

```text
Part 1 for [dataset] has run; its record is in [folder]. Sort every host it lists into the three kinds in
rstar-pipeline/processing/research-queries/archive-query-plan.md (shared archive, producer's own data site, copy), add them to the register of
repositories, and write the A1 and A2 queries each new repository needs from
rstar-pipeline/processing/research-queries/templates/archive/. Then update the
dataset's run sheet.
```

**For a dataset that already has research,** use this instead:

```text
[Dataset] already has research in [folder]. Check its runs against the 19 subcategories in rstar-pipeline/input/framework/definitions/ and write
a coverage note: what is covered, partly covered or never searched, per subcategory, and what the later runs shouldn't
search again. Then write only the gap queries needed, following the five-part plan and the archive plan (one "people and
production" query plus any missing repository runs), and a run sheet.
```

## What your friend needs besides the files

- **The two research skills,** `broad-web-research` and `rewrite-research-query`. They are custom skills, not part of
  Claude Code, so they must be shared and installed in his Claude Code setup (for example in his `~/.claude/skills/`
  folder or as a plugin). The skill folders are `~/.my-claude-plugins/my/skills/broad-web-research/` and
  `~/.my-claude-plugins/my/skills/rewrite-research-query/` on the original machine. Installed in a plugin named `my`,
  they are called as `/my:broad-web-research` and `/my:rewrite-research-query`, which is how the example files call
  them. Without them, the prompts above still work for writing queries, but the research runs need another way to run.
- **A separate research project** (a folder where the research skill saves its runs), so that later queries can name
  earlier runs' folders.
- **Time and usage:** a deep run at 50 minutes and 400,000 tokens is the largest single cost. Five or six sessions per
  dataset is the target.
