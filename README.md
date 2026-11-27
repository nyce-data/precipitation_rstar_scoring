# R* Scores for precipitation datasets

The site isn't published from this repo yet: it will be served, behind the workshop password, from a DigitalOcean
droplet. To view it on your own computer, see "View it" in `app/README.md`.

R* is a score for how likely a dataset is to stop being available in the near future. This project scores
precipitation datasets on R* from web research. It sorts what the research found into the R* subcategories as
evidence, and shows the evidence and scores on a website where a person can review each score and choose their own.

## How R* is scored

R* has four groups, with 19 subcategories in all:

| Group | Subcategories | Weight in R* |
|---|---|---|
| D: Data risk | D-1 to D-5 | 0.40 |
| P: People risk | P-1 to P-4 | 0.30 |
| RRS: Repository resilience | RRS-1 to RRS-5 | 0.20, counted as (100 − RRS) |
| DIRS: Dependent infrastructure resilience | DIRS-1 to DIRS-5 | 0.10 |

```
R* = 0.40 D + 0.30 P + 0.20 (100 − RRS) + 0.10 DIRS
```

Each group's score is the sum of its subcategory scores. A subcategory scores its full points or 0, set only by
high- and moderate-confidence evidence:

- only evidence **for** it: full points;
- only evidence **against** it: 0;
- both, or neither: **NA**, and a person decides.

If any subcategory is NA, its group and R* are NA too. Point values and the full rules are in
[rstar-pipeline/input/framework/how_to_score_rstar.md](rstar-pipeline/input/framework/how_to_score_rstar.md).

## Datasets

| Dataset | State |
|---|---|
| GHCN-Daily (Global Historical Climatology Network – Daily) | Categorized and on the site |
| GPCP Daily (Global Precipitation Climatology Project, V3.3) | Categorized and on the site (second pass, with the NASA GES DISC repository research) |
| IMERG Late Run (GPM IMERG Late, V07) | Categorized and on the site (third pass, with the people and NASA GES DISC + PPS repository research) |
| PERSIANN-CDR Daily | Categorized and on the site (second pass, with its people and calibration research and the UC Irvine CHRS repository research) |
| CoCoRaHS (Community Collaborative Rain, Hail and Snow Network) | Categorized and on the site (first pass, with its data-site repository research) |
| USCRN Daily and ASOS | Web research on the site; not categorized yet |

Most GHCN-Daily subcategories are still NA: the research found evidence on both sides, or none, so they need a
person's call. That is what the site is for.

## How it works

1. **Web research.** Each dataset, the repositories that hold it and the instruments that measure it are researched
   with a set of queries. Each run's answer cites its sources; the later runs also tag findings with subcategory
   codes.
2. **Categorizing.** A script per dataset sorts the findings into the 19 subcategories as evidence items, each tagged
   with a stance (for, against or context) and a confidence (high, moderate or low), plus a list of gaps the research
   didn't cover. It works out the score from the evidence.
3. **The website.** A build script turns the definitions, scoring rules, dataset details and categorizations into one
   data file for the site.
4. **Review.** On the site a person reads the evidence, picks a score for each subcategory, adds notes and saves their
   scores as a JSON file. Their choices stay in their own browser; nothing is sent anywhere.

## The website

- **Dashboard (landing page):** one card per dataset with search and filters; each card opens to the dataset's
  details and links to its overview, its web research and its R* scores. Archive and instrument pages hold the
  research on the repositories and instruments.
- **R* score page:** the dataset's details, its R* score, a key to the tags, and the four groups.
- **Group pages:** one card per subcategory with its definition, what counts as evidence, the evidence and gaps, and
  "Your score" and "Your notes".
- **Score graph:** the scores as a weighted network graph, with R* in the middle, optionally with a dot for every
  evidence item.
- **Save your scores:** downloads a JSON file in the format described by
  [app/schema/rstar-assessment.schema.json](app/schema/rstar-assessment.schema.json).

The site is plain HTML, CSS and JavaScript with no dependencies. To run it on your own computer:

```bash
cd app && python3 -m http.server 3000 --bind 127.0.0.1
```

Then open http://127.0.0.1:3000/. Details, tests and how to rebuild the data are in [app/README.md](app/README.md).

## What's in the repository

| Folder | What it holds |
|---|---|
| [rstar-pipeline/](rstar-pipeline/) | **Everything needed to rebuild the site's data**, as input → processing → output. Its [README](rstar-pipeline/README.md) explains the layout and the steps, so the process can be repeated for another project |
| [app/](app/) | The website and its Playwright tests. It reads only its own `app/data/` and `app/content/`, which the pipeline's scripts write |
| [datasets-gap-queries/](datasets-gap-queries/) | Notes from planning the follow-up research for each dataset (a one-off step) |
| [notes/](notes/) | Changes proposed to the saved-file format |

Good places to start:

- [rstar-pipeline/README.md](rstar-pipeline/README.md): how the folders fit together and the steps in order;
- [rstar-pipeline/input/framework/how_to_score_rstar.md](rstar-pipeline/input/framework/how_to_score_rstar.md): point
  values and the scoring formula;
- [rstar-pipeline/input/framework/rstar-categorization-decisions.md](rstar-pipeline/input/framework/rstar-categorization-decisions.md):
  the rules for filing evidence;
- [rstar-pipeline/processing/instructions/categorizing-web-searches_README.md](rstar-pipeline/processing/instructions/categorizing-web-searches_README.md):
  how to categorize a dataset and add it to the site;
- [rstar-pipeline/processing/research-queries/rstar-query-templates-guide.md](rstar-pipeline/processing/research-queries/rstar-query-templates-guide.md):
  how the research queries are designed and how to adapt them to other climate data.
