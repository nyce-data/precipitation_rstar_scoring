# About $DATASET_SHORT Part 5: Inputs R* Query for Claude

About dataset = $DATASET_SHORT Part 5, threats to its inputs, and alternatives

Template written 2026-11-23 from `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` in precipitation_rstar_scoring. To use it:
copy it into the dataset's folder as `<dataset>-about_Rstar_query_pt5.md`, replace every `$PLACEHOLDER`, rewrite it
with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session.

**Placeholders:**
- `$DATASET_SHORT`: the short name, such as GHCN-D.
- `$DATASET`: the short and full names.
- `$EARLIER_RUNS`: the folder names of this dataset's Part 1 and Part 2 runs.
- `$SHARED_RUNS`: the shared instrument runs that apply (A4), such as `2026-11-18_noaa-rain-gauge-threats` or the
  NOAA and NASA satellite runs.
- `$CANDIDATES`: the inputs to check, from Part 1's list. For a station dataset, its networks and national weather
  services; for a satellite dataset, its satellites and sensors. Add the calibration facilities from Part 2.
- `$NOW`: the month the run happens, such as November 2026.
- `$LIMITS`: "50 minutes and a token ceiling of 400,000" for a dataset with many inputs (15 or more, such as GPCP Daily
  or IMERG); "40 minutes and a token ceiling of 320,000" for one with a few.

**Subcategories this part answers:** DIRS-2, DIRS-3 and DIRS-5, plus threats to the calibration facilities for DIRS-1.

**Run order:** after Parts 1 and 2. It doesn't depend on Parts 3 or 4.

## Query to refine

Using the earlier runs' records ($EARLIER_RUNS) and the shared runs ($SHARED_RUNS), all in web_search_results/, which
of $DATASET's inputs (networks, satellites and sensors, input datasets, ancillary fields, calibration facilities, and
the organizations that run them) faced funding cuts, termination, end of life, operational disruptions or news about
these between January 2024 and $NOW? Check $CANDIDATES without assuming any is affected, and spend most of the time on
inputs the shared runs didn't cover. For each affected input: what happened and when; whether it is enacted, proposed
or reversed; what share of the dataset it supplies; and whether the dataset's own record shows the effect. If an input
failed, is there a replacement, a backup source or a substitute, and which datasets could replace $DATASET itself?
Rate each input, and the inputs overall, imminent, emerging or no current threat found. Tag findings with DIRS-1
"depends on an external calibration service that could be disrupted", DIRS-2 "upstream networks or platforms aging
out or losing funding", DIRS-3 "upstream data feeds vulnerable" or DIRS-5 "no alternative supplier". With a time limit
of $LIMITS.

### Context for the rewrite

- **Candidates, not facts.** List the inputs "without assuming any is affected", so the run checks each one rather
  than hunting for a threat to each.
- **Build on the shared runs.** The A4 runs cover NOAA's rain gauges and NOAA's and NASA's satellites. Point this
  run at the inputs those runs didn't check: networks abroad, input datasets, ancillary fields and calibration
  facilities.
- **Effects in the dataset's own record.** For a station dataset, station counts and gaps in the inventory; for a
  satellite dataset, the input list in the version notes or file metadata. This is the evidence that a threat has
  reached the dataset.
- **Alternatives (DIRS-5).** Ask for substitutes for each lost input and for the dataset as a whole, with coverage
  and status. This was never searched for GHCN-Daily in its first runs.
- **Rating scale, the same in every R* query:** imminent (enacted, ordered or already happening), emerging (proposed
  or reported but not in effect), or no current threat found.
- **Sources.** Use operators' own notices and the dataset's files ahead of news, and news for events.
- **If it's too big for one run,** split it into two runs (US inputs and non-US inputs, or satellites and gauges),
  each at 30 minutes and 240,000 tokens.

### What the answer should give

- A table of inputs: what happened, when, its status, its share of the dataset, whether the effect shows in the
  dataset's files, and a rating.
- Substitutes for lost inputs and for the dataset itself.
- An overall rating for the inputs.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
