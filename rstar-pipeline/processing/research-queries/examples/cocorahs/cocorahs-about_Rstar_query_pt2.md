# About CoCoRaHS Part 2: Processing R* Query for Claude

About dataset = CoCoRaHS Part 2, processing, quality control, calibration, code and formats

Written 2026-11-23 from `templates/template-dataset-about_Rstar_query_pt2_processing.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_cocorahs-qc-formats-pt2`.

**Subcategories this part answers:** D-4, P-3, DIRS-1, DIRS-4.

**Run order:** after Part 1. It can run before or after Part 3.

## Query to refine

Using Part 1's record (`*_cocorahs-about-pt1`, in web_search_results/), how are CoCoRaHS's daily precipitation reports
quality-controlled: the automated checks on entry, the manual review (who does it: state or regional coordinators,
Colorado Climate Center staff, or the National Weather Service), how suspect reports are flagged, corrected or removed,
and what further checks NOAA NCEI applies when the reports enter GHCN-Daily? What does the network's "calibration" rest
on: the approved gauge and who sets that standard, observer training and the training material, and any comparison of
CoCoRaHS reports with NWS or other official gauges? What software produces and serves the data, who wrote and runs it,
and does any step need facilities outside the Colorado Climate Center's control? Is any of the code published, and is
the documentation (observer manuals, QC procedures, data-entry guides) detailed enough for someone new to keep the
network's data going? Rate each format and access route FAIR, partly FAIR or non-FAIR, and say whether any needs
proprietary software. Leave cuts and threats to later parts. Tag findings with D-4 "formats obsolete or proprietary",
P-3 "critical knowledge undocumented", DIRS-1 "depends on an external calibration service that could be disrupted" or
DIRS-4 "needs outside processing infrastructure". With a time limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats or news.
- **Calibration for a volunteer network** is the gauge standard and the people who check reports, not a calibration
  lab. Ask the run to say plainly if no comparison with official gauges is published.
- **FAIR tests, the same four for every dataset:**
  - findable: a persistent identifier such as a DOI, and metadata in a searchable catalog;
  - accessible: downloadable over a standard open protocol without a login;
  - interoperable: an open, documented format that common tools read, with standard variable names and units;
  - reusable: a stated license and provenance.

  The site's data use policy states CC BY 4.0 (reusable), but the ViewData page mentions no DOI or download format.
  The metadata file (a ChatGPT answer, 2026-11-25) names a CSV route through the Export Manager at data.cocorahs.org;
  rate that route on its own.
  GHCN-Daily's copy is a separate route with its own DOI; rate it separately.
- **Start from the QC document.** The metadata file points to "CoCoRaHS Data Quality Assurance and Quality Control"
  (April 2019, media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf). Ask the run to read it first, and to say
  whether a newer version exists.
- **Code, item by item.** Tell published code apart from software only described on the site.
- **Outside facilities (DIRS-4):** CSU's or a vendor's servers, and any outside developer or contractor that built the
  data-entry system or the Station Data Explorer.

### What the answer should give

- The QC steps, one line each, with who does them and how suspect reports are handled.
- The gauge standard, training, and any comparison with official gauges.
- A table of software and systems: owner, operator, and whether the code is published.
- A FAIR rating for each format and access route, including GHCN-Daily's copy.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
