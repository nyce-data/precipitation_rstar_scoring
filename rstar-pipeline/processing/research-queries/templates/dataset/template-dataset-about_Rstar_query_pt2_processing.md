# About $DATASET_SHORT Part 2: Processing R* Query for Claude

About dataset = $DATASET_SHORT Part 2, processing, quality control, calibration, code and formats

Template written 2026-11-23 from `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` in precipitation_rstar_scoring. To use it:
copy it into the dataset's folder as `<dataset>-about_Rstar_query_pt2.md`, replace every `$PLACEHOLDER`, rewrite it
with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session.

**Placeholders:**
- `$DATASET_SHORT`: the short name, such as GHCN-D.
- `$DATASET`: the short and full names.
- `$PART1_RUN`: the folder name of this dataset's Part 1 run, such as `2026-11-19_ghcn-daily-about-pt1`.
- `$CALIBRATION_EXAMPLES`: pick the line for the dataset's kind, from "Context for the rewrite" below.

**Subcategories this part answers:** D-4, P-3, DIRS-1, DIRS-4.

**Run order:** after Part 1. It can run before or after Part 3.

## Query to refine

Using Part 1's record ($PART1_RUN, in web_search_results/), how is $DATASET processed and quality-controlled: the
checks, whether automated or manual, how flags work, and who does each step, including checks done by input providers
before the data arrive? What calibration does it depend on, such as $CALIBRATION_EXAMPLES, and who runs each? What
software, algorithms and computing facilities produce it, who owns and runs them, and does any step need facilities
outside the producer's control? For each piece of code, is it published (where, under what license), only described in
papers, or unpublished, and is the documentation detailed enough for a newcomer to reproduce the dataset? Rate each
format and access route FAIR, partly FAIR or non-FAIR, and say whether any needs proprietary software. Leave cuts and
threats to later parts. Tag findings with D-4 "formats obsolete or proprietary", P-3 "critical knowledge undocumented",
DIRS-1 "depends on an external calibration service that could be disrupted" or DIRS-4 "needs outside processing
infrastructure". With a time limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats or news; Parts 4 and 5 cover them.
- **Calibration examples (`$CALIBRATION_EXAMPLES`), by kind of dataset.** No "about" run asked about calibration
  before, so name the kind of facility to look for:
  - **station or gauge data:** "instrument calibration labs and field technicians of the source networks (such as
    NWS's Sterling Field Support Center for ASOS), traceability to national standards (NIST), WMO Regional Instrument
    Centres and WMO gauge intercomparisons";
  - **satellite data:** "calibration against a reference sensor (such as GPM's GMI), the groups that run that
    calibration (such as the GPM X-CAL working group), the gauge analysis used to correct bias (such as GPCC), and
    validation sites";
  - **a blend of both:** use both lines.
- **FAIR tests, the same four for every dataset:**
  - findable: a persistent identifier such as a DOI, and metadata in a searchable catalog;
  - accessible: downloadable over a standard open protocol without a login;
  - interoperable: an open, documented format that common tools read, with standard variable names and units;
  - reusable: a stated license and provenance.

  Rate each format together with the route it is served by, and name the tests it fails.
- **Code, item by item.** Ask for each piece of software separately, and tell published code apart from methods
  only described in papers: a paper is not code someone can run.
- **Documentation for a newcomer (P-3).** Look for operations manuals, algorithm theoretical basis documents (ATBDs),
  READMEs and processing guides, and say whether they cover running the processing, or only describe the method.
- **Outside facilities (DIRS-4).** Include supercomputers, cloud platforms and processing centres run by another
  organization, such as NASA's Precipitation Processing System for IMERG or a cloud provider after a migration.

### What the answer should give

- The QC checks, one line each, with who does them and how flags work.
- A table of calibration dependencies, with who runs each.
- A table of software, algorithms and facilities: owner, operator, and whether the code is published.
- A FAIR rating for each format and access route.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
