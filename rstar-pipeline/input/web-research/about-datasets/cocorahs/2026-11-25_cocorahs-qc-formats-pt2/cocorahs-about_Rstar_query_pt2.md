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

/my:broad-web-research

Using Part 1's record (`*_cocorahs-about-pt1`, in web_search_results/), how are CoCoRaHS's daily precipitation reports
quality-controlled, what does the network's "calibration" rest on, what software produces and serves the data, and how
open are its formats and access routes? Start from "CoCoRaHS Data Quality Assurance and Quality Control" (April 2019,
media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf), and say whether a newer version exists.

- **QC:** the automated checks on entry; the manual review and who does it (state or regional coordinators, Colorado
  Climate Center staff, or the National Weather Service); how suspect reports are flagged, corrected or removed; and
  what further checks NOAA NCEI applies when the reports enter GHCN-Daily.
- **Calibration:** for a volunteer network this is the approved gauge and who sets that standard, observer training and
  its material, and any published comparison of CoCoRaHS reports with NWS or other official gauges. Say plainly if no
  comparison is published.
- **Software and facilities:** what produces and serves the data (data-entry system and apps, database, Export Manager,
  Station Data Explorer), who wrote and runs each, and any step needing facilities outside the Colorado Climate
  Center's control (CSU's or a vendor's servers, an outside developer or contractor). For each: code published (where,
  what licence), or software only described on the site.
- **Documentation:** whether observer manuals, QC procedures and data-entry guides are detailed enough for someone new
  to keep the network's data going.
- **FAIR:** rate each format and access route separately (ViewData, the Export Manager's CSV route, any API, and
  GHCN-Daily's copy) FAIR, partly FAIR or non-FAIR, and name the tests it fails: findable (a persistent identifier such
  as a DOI, and metadata in a searchable catalog); accessible (a standard open protocol, no login); interoperable (an
  open, documented format common tools read, with standard variable names and units); reusable (a stated licence and
  provenance). Say whether any needs proprietary software.

For each finding, say whether it supports or contradicts D-4 "formats obsolete or proprietary", P-3 "critical
knowledge undocumented", DIRS-1 "depends on an external calibration service that could be disrupted" or DIRS-4 "needs
outside processing infrastructure"; all four are worded as risks, so "supports" means evidence the risk holds. Leave
people, funding and recent developments to later runs. Use CoCoRaHS's and NCEI's own documents ahead of secondary
accounts. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** the QC steps with who does each and how suspect reports are handled, including NCEI's checks in
GHCN-Daily; the gauge standard, training, and any comparison with official gauges or a plain "none published"; the
software and systems with owner, operator and code status; whether the documentation would let a newcomer keep the
data going; a FAIR rating per route, GHCN-Daily's copy included; and each finding tagged D-4, P-3, DIRS-1 or DIRS-4
with a stance. Expect a standard-tier run.

**What changed and why:**
- **Kept standard tier.** "Cuts and threats" became "recent developments".
- **Starts from the 2019 QA/QC document,** as your context note asks, with a check for a newer version.
- **Calibration defined for a volunteer network:** the gauge standard, training and comparisons, not a lab.
- **FAIR tests written out,** one line each, the same four as in the other R* queries, with the Export Manager's CSV
  route and GHCN-Daily's copy rated on their own. I left out the CC BY 4.0 and "no DOI on ViewData" notes so the run
  rates each route from what it finds; both are in Part 1's record if it confirms them.
- **Code item by item and outside facilities** kept as short candidate lists.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 30 minutes and 240,000 tokens, as in your draft.

**How to reuse:** run after Part 1, in this project; before or after Part 3. Keep the `*_cocorahs-about-pt1` pattern
until Part 1 has run, then put in its folder name.
