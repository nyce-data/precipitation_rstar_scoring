# About CoCoRaHS Part 5: Inputs R* Query for Claude

About dataset = CoCoRaHS Part 5, threats to its inputs, and alternatives

Written 2026-11-23 from `templates/template-dataset-about_Rstar_query_pt5_inputs.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_cocorahs-inputs-pt5`.

**Subcategories this part answers:** DIRS-2, DIRS-3 and DIRS-5, plus threats to the gauge standard for DIRS-1.

**Run order:** after Parts 1 and 2. It doesn't depend on Parts 3 or 4.

## Query to refine

Using the earlier runs' records (`*_cocorahs-about-pt1`, `*_cocorahs-qc-formats-pt2`,
`2026-11-18_noaa-rain-gauge-threats` and `2026-11-21_ghcn-daily-sources-pt5`), all in web_search_results/, which of
CoCoRaHS's inputs (its volunteer observers, the approved gauge and its supply, the data-entry system and apps, the
hosting it runs on, and the organizations that recruit and train observers) faced decline, disruption, end of supply or
news about these between January 2024 and November 2026? Check these without assuming any is affected: observer and
station counts by year and by state, observer recruitment and retention, the gauge supplier or suppliers, the website
and mobile-app platform, and the NWS offices and state coordinators who recruit observers. For each affected input:
what happened and when; whether it is happening, proposed or reversed; what share of reports it affects; and whether
CoCoRaHS's or GHCN-Daily's station counts show the effect. If an input failed, is there a replacement or a second
supplier, and which datasets could replace CoCoRaHS itself for dense daily precipitation (such as COOP, mesonets or
radar–gauge products)? Rate each input, and the inputs overall, imminent, emerging or no current threat found. Tag
findings with DIRS-1 "depends on an external calibration service that could be disrupted", DIRS-2 "upstream networks
or platforms aging out or losing funding", DIRS-3 "upstream data feeds vulnerable" or DIRS-5 "no alternative
supplier". With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **The inputs are people and gauges,** not satellites or other datasets. A volunteer network's "observation
  platform" (DIRS-2) is its observers, and its supply chain (DIRS-3) is the gauge and the data-entry system.
- **One approved gauge could be a single supplier (DIRS-5).** Ask whether more than one maker produces the gauge
  CoCoRaHS requires, without assuming there is only one.
- **Station counts are evidence.** GHCN-Daily's inventory showed about 2,139 CoCoRaHS IDs with 2025 data and none in
  2026, within normal turnover of 1,785–2,078 a year (`2026-11-21_ghcn-daily-sources-pt5`). Ask whether CoCoRaHS's own
  counts agree.
- **Limits.** 40 minutes and 320,000 tokens; CoCoRaHS has few inputs compared with a satellite blend.
- **Rating scale, the same in every R* query:** imminent, emerging, or no current threat found.

### What the answer should give

- Observer and station counts over time, by state where published.
- A table of inputs: what happened, when, its status, the share of reports affected, and a rating.
- The gauge supply and any second supplier.
- Substitutes for CoCoRaHS data.
- An overall rating for the inputs.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
