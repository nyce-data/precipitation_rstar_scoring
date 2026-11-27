# About USCRN Daily Part 5: Inputs R* Query for Claude

About dataset = USCRN Daily Part 5, threats to its instruments, stations and data path, and alternatives

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt5_inputs.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_uscrn-daily-inputs-pt5`.

**Subcategories this part answers:** DIRS-2, DIRS-3 and DIRS-5, plus threats to the calibration and maintenance team
for DIRS-1.

**Run order:** after Parts 1 and 2. It doesn't depend on Parts 3 or 4.

## Query to refine

Using the earlier runs' records (`*_uscrn-daily-about-pt1`, `*_uscrn-daily-qc-formats-pt2`) and the shared runs
(`2026-11-18_noaa-rain-gauge-threats`, `2026-11-18_noaa-satellite-precip-threats` and
`2026-11-23_ghcn-daily-infrastructure-pt8`), all in web_search_results/, which of USCRN Daily's inputs (its stations
and site agreements, the precipitation instruments and their makers, the dataloggers, the transmission path to NCEI,
the field maintenance and calibration team, and the organizations that run them) faced funding cuts, end of life, end
of manufacturer support, operational disruptions or news about these between January 2024 and November 2026? Check
these without assuming any is affected: station counts by region and year (including the Alaska build-out), the
Geonor T-200B gauge and its maker, the Vaisala DRD11A wetness sensor, the TB-3 tipping bucket, the dataloggers, the
satellite or other link the stations transmit over, and ATDD's field team. For each affected input: what happened and
when; whether it is enacted, proposed or reversed; how many stations it affects; and whether the daily01 files show
the effect (stations ending, gaps or missing days). If an input failed, is there a replacement, a second supplier or a
backup, and which datasets could replace USCRN Daily itself as reference-quality daily precipitation (such as ASOS,
COOP, state mesonets, SNOTEL or Canada's reference climate stations)? Rate each input, and the inputs overall,
imminent, emerging or no current threat found. Tag findings with DIRS-1 "depends on an external calibration service
that could be disrupted", DIRS-2 "upstream networks or platforms aging out or losing funding", DIRS-3 "upstream data
feeds vulnerable" or DIRS-5 "no alternative supplier". With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **The inputs are stations and instruments,** not other datasets. USCRN's "platform" (DIRS-2) is its stations; its
  supply chain (DIRS-3) is the instrument makers, the dataloggers and the transmission link.
- **Candidates, not facts.** List them "without assuming any is affected".
- **One gauge model network-wide could mean one supplier (DIRS-5).** Every station uses the same weighing gauge; ask
  whether more than one maker could supply a replacement, and whether NOAA has tested one, without assuming there is
  only one.
- **Already known; build on it:** the 139-tower transmitter upgrade finished April 25, 2026; 4 of 161 station rows were
  stale on November 18, 2026 (`2026-11-18_noaa-rain-gauge-threats`); ATDD's eight-person team makes the annual visits
  and its parent lab was proposed for closure (`2026-11-23_ghcn-daily-infrastructure-pt8`). If the stations send data
  through GOES DCS, the NOAA satellite run (`2026-11-18_noaa-satellite-precip-threats`) covers the GOES side.
- **Effects in the record.** Count stations with daily01 files by year and say whether any drop or gap shows.
- **Alternatives (DIRS-5).** Ask for each one's coverage, siting standard, whether it is quality-controlled to climate
  reference standards, and its status; say plainly if no network matches USCRN's reference quality.
- **Rating scale, the same in every R* query:** imminent, emerging, or no current threat found.
- **Limits.** 40 minutes and 320,000 tokens: one network with a few kinds of input.

### What the answer should give

- Station counts over time, by region.
- A table of inputs: what happened, when, its status, the stations affected, whether the daily files show it, and a
  rating.
- The instrument makers, support status and any second supplier.
- Substitutes for USCRN Daily, with coverage and status.
- An overall rating for the inputs.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ (`*_uscrn-daily-about-pt1`, `*_uscrn-daily-qc-formats-pt2`,
2026-11-18_noaa-rain-gauge-threats, 2026-11-18_noaa-satellite-precip-threats and
2026-11-23_ghcn-daily-infrastructure-pt8), which of USCRN Daily's inputs (the U.S. Climate Reference Network's daily01
product) faced funding cuts, end of life, end of manufacturer support, operational disruption or news about these
between January 2024 and November 2026, and what could replace them or the dataset?

Its inputs are its stations and instruments, not other datasets. Check these without assuming any is affected: the
stations and their site agreements (counts by region and year, including the Alaska build-out); the Geonor T-200B
gauge and its maker; the Vaisala DRD11A wetness sensor; the TB-3 tipping bucket; the dataloggers; the satellite or
other link the stations transmit over (if it is GOES DCS, the satellite run covers GOES itself); and ATDD's field
maintenance and calibration team. Already known: the 139-tower transmitter upgrade finished April 25, 2026, and 4 of
161 station rows were stale on November 18, 2026.

- **For each affected input:** what happened and when; whether it is enacted, proposed or reversed; how many stations
  it affects; and whether the daily01 files show it (count stations with files by year; look for stations ending, gaps
  or missing days).
- **Suppliers and backups:** whether more than one maker could supply a replacement gauge, and whether NOAA has tested
  one; any backup for the transmission link or the field team.
- **Substitutes for USCRN Daily** as reference-quality daily precipitation: check ASOS, COOP, state mesonets, SNOTEL
  and Canada's reference climate stations for coverage, siting standard, quality control to climate reference
  standards and status. Say plainly if none matches USCRN's reference quality.

Rate each input, and the inputs overall, imminent (enacted or happening), emerging (proposed or reported, not in
effect) or no current threat found. For each finding, say whether it supports or contradicts DIRS-1 "depends on an
external calibration service that could be disrupted", DIRS-2 "upstream networks or platforms aging out or losing
funding", DIRS-3 "upstream data feeds vulnerable" or DIRS-5 "no alternative supplier"; all four are worded as risks, so
"supports" means evidence the risk holds. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** station counts by region and year; for each input, what happened, when, its status, the stations
affected, whether the daily01 files show it, and a rating; the instrument makers, their support status and any second
supplier or tested replacement; substitutes for USCRN Daily with coverage, siting, QC and status, or a plain "none
matches"; an overall rating for the inputs; and each finding tagged DIRS-1, DIRS-2, DIRS-3 or DIRS-5 with a stance.
Expect a deep-tier run.

**What changed and why:**
- **Inputs defined as stations and instruments,** so the run doesn't look for upstream datasets: the stations are the
  "platform" (DIRS-2), the makers, dataloggers and link the supply chain (DIRS-3).
- **Candidates, not facts.** The instruments and the substitute networks are listed "without assuming any is
  affected" or matches.
- **Single supplier asked, not assumed.** Every station uses the same gauge model, so the question asks whether a
  second maker exists and whether NOAA has tested one (DIRS-5).
- **Known facts given once:** the transmitter upgrade and the 4 stale station rows from the rain-gauge run; the
  eight-person team and the closure proposal are in the pt8 record, which the run reads.
- **GOES left to the satellite run,** so this run doesn't redo it if the stations use GOES DCS.
- **Effects in the record:** the run counts stations with daily01 files by year.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 40 minutes and 320,000 tokens: one network with a few kinds of input.

**How to reuse:** run after Parts 1 and 2, in this project; it doesn't need Parts 3 or 4, and Part 4 reads its
record. Keep the two `*_…` patterns until those runs exist. If Parts 1 and 2 find nothing affected and the station
counts are steady, this run may be short; 30 minutes and 240,000 tokens would do.
