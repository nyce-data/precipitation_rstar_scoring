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

/my:broad-web-research

Using the earlier runs' records in web_search_results/ (`*_cocorahs-about-pt1`, `*_cocorahs-qc-formats-pt2`,
2026-11-18_noaa-rain-gauge-threats and 2026-11-21_ghcn-daily-sources-pt5), which of CoCoRaHS's inputs (Community
Collaborative Rain, Hail and Snow Network) faced decline, disruption, end of supply or news about these between January
2024 and November 2026, and what could replace them or CoCoRaHS's data?

Its inputs are people and gauges, not satellites or other datasets: its observers are its "platform" and the gauge
and data-entry system its supply chain. Check these without assuming any is affected: observer and station counts by
year and by state; observer recruitment and retention; the approved gauge and its supplier or suppliers (whether more
than one maker produces it); the website and mobile-app platform and the hosting it runs on; and the NWS offices and
state coordinators who recruit and train observers. GHCN-Daily's inventory showed about 2,139 CoCoRaHS station IDs
with 2025 data and none in 2026, within normal turnover of 1,785–2,078 a year; say whether CoCoRaHS's own counts
agree.

- **For each affected input:** what happened and when; whether it is happening, proposed or reversed; what share of
  reports it affects; and whether CoCoRaHS's or GHCN-Daily's station counts show the effect.
- **Replacements:** a second gauge supplier, a backup for the data-entry system, or other recruiters if an input
  failed.
- **Substitutes for CoCoRaHS** as dense daily precipitation: check COOP, state mesonets and radar–gauge products for
  coverage, density, quality control and status, and say where none matches.

Rate each input, and the inputs overall, imminent (happening), emerging (proposed or reported, not in effect) or no
current threat found. For each finding, say whether it supports or contradicts DIRS-1 "depends on an external
calibration service that could be disrupted", DIRS-2 "upstream networks or platforms aging out or losing funding",
DIRS-3 "upstream data feeds vulnerable" or DIRS-5 "no alternative supplier"; all four are worded as risks, so
"supports" means evidence the risk holds. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** observer and station counts over time, by state where published, checked against GHCN-Daily's
inventory; for each input, what happened, when, its status, the share of reports affected and a rating; the gauge
supply and any second supplier; substitutes for CoCoRaHS data with coverage and status; an overall rating; and each
finding tagged DIRS-1, DIRS-2, DIRS-3 or DIRS-5 with a stance. Expect a deep-tier run.

**What changed and why:**
- **Inputs defined as people and gauges,** so the run doesn't look for upstream datasets.
- **Candidates, not facts.** The inputs and the substitutes are listed "without assuming any is affected"; the single
  gauge supplier is asked, not assumed (DIRS-5).
- **Station counts as evidence.** The GHCN-Daily turnover figures from the sources run are stated once, with a check
  against CoCoRaHS's own counts.
- **Gauge standard for DIRS-1:** the approved gauge is the network's "calibration", so a supply break there is the
  DIRS-1 question.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 40 minutes and 320,000 tokens: CoCoRaHS has few inputs compared with a satellite blend. If Parts 1 and 2
  find steady counts and one well-supplied gauge, 30 minutes and 240,000 tokens would do.

**How to reuse:** run after Parts 1 and 2, in this project; it doesn't need Parts 3 or 4. Keep the two `*_…` patterns
until those runs exist. Its station-count findings also bear on GHCN-Daily's DIRS-2 and DIRS-3, since CoCoRaHS is about
40% of GHCN-Daily's entries.
