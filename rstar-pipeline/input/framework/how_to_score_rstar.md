# How to score subcategories

## R* score definition

R* is composed of 4 groups (D, P, RRS, DIRS)

It's a way to give a score value to a dataset to see what risk it has for not being available in the near future.

Core major categories that make up the R* score

1. D = Data risk
2. P = People risk
3. RRS = Repository resilience
4. DIRS = Dependent infrastructure resilience

These major categories have subcategories described below.

## Scoring formula for group nodes and R*

### R* score value calculation

```
rstar = d_total*0.40 + p_total*0.30 + (100 - rrs_total)*0.20 + dirs_total*0.10
```

Each variable with the subscript _total in the name represents the major category score that is the sum of all of it's subcategory scores.

For example, d_total is the total score of the Data Risk major category where each data risk subcategory gets a score value that is either a min or a max score in a set of values described below.

### subcategory scores

A subcategory's score comes from its evidence items. Only high- and moderate-confidence "for" and "against" items set it. Low-confidence items stay in the evidence, tagged low, but are left out of the score, and "context" items are ignored.

| High or moderate evidence | Score |
| --- | --- |
| "For" items and no "against" items | the max value in the subcategory set of values |
| "Against" items and no "for" items | the min value, which is 0 |
| Both "for" and "against" items | NA |
| None: only context, only low confidence, or no evidence | NA |

NA means there is not enough information to decide, and a person must choose the score (they may know things a web search can't find). A major category total is NA if any of its subcategories is NA, and R* is NA if any major category total is NA.

For RRS, "for" means the repository is resilient, so a full RRS score lowers R* through (100 - rrs_total).

The score is stored in each dataset's category JSON (`data-score` on the subcategory's div), written by `rstar-pipeline/processing/scripts/categorize/rstar_common.py`. The rules for filing evidence are in `rstar-pipeline/input/framework/rstar-categorization-decisions.md`.

### Data risk score values

Data risk subcategories have the format D-# defined in rstar-pipeline/input/framework/definitions/d-rstar-data_risk_queries.md

Score values

```
Subcategory D-# can only have score values in the following sets and the min score is always 0

Score sets for the subcategories of the major category Data Risk where d_1 represents the score of subcategory D-1, etc. And d_total represents the total score of the Data Risk major category.

d_1 = {0,30}
d_2 = {0,25}
d_3 = {0,20}
d_4 = {0,15}
d_5 = {0,10}

d_total = d_1 + d_2 + d_3 + d_4 + d_5

```

### People risk score values

People risk subcategories have the format P-# defined in rstar-pipeline/input/framework/definitions/p-rstar-people_risk_queries.md

Score values

```
Subcategory P-# can only have score values in the following sets and the min score is always 0

Score sets for the subcategories of the major category People Risk where p_1 represents the score of subcategory P-1, etc. And d_total represents the total score of the People Risk major category.

p_1 = {0,35}
p_2 = {0,25}
p_3 = {0,25}
p_4 = {0,15}

p_total = p_1 + p_2 + p_3 + p_4

```

### Repository resilience score values

Repository resilience subcategories have the format RRS-# defined in rstar-pipeline/input/framework/definitions/rrs-rstar-repository_reslience_queries.md

Score values

```
RRS-# can only have score values in the following sets and the min score is always 0

Score sets for the subcategories of the major category Repository resilience where rrs_1 represents the score of subcategory RRS-1, etc. And rrs_total represents the total score of the Repository resilience major category.

rrs_1 = {0,25}
rrs_2 = {0,20}
rrs_3 = {0,20}
rrs_4 = {0,20}
rrs_5 = {0,15}

rrs_total = rrs_1 + rrs_2 + rrs_3 + rrs_4 + rrs_5

```

### Dependent infrastructure resilience score values

Dependent infrastructure resilience subcategories have the format DIRS-# defined in rstar-pipeline/input/framework/definitions/dirs-rstar-dependent_infrastructure_reslience_queries.md

Score values

```
DIRS-# can only have score values in the following sets and the min score is always 0

Score sets for the subcategories of the major category Dependent infrastructure resilience where dirs_1 represents the score of subcategory DIRS-1, etc. And dirs_total represents the total score of the Dependent infrastructure resilience major category.

dirs_1 = {0,25}
dirs_2 = {0,25}
dirs_3 = {0,20}
dirs_4 = {0,15}
dirs_5 = {0,15}

dirs_total = dirs_1 + dirs_2 + dirs_3 + dirs_4 + dirs_5

```
