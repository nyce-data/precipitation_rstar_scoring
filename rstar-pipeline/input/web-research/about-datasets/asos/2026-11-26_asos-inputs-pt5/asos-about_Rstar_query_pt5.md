# About ASOS Part 5: Inputs R* Query for Claude

About dataset = ASOS Part 5, threats to its sensors, stations and data path, and alternatives

Written 2026-11-25 from `templates/template-dataset-about_Rstar_query_pt5_inputs.md`. Rewrite this with
`/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session. Suggested
run folder: `<date>_asos-inputs-pt5`.

**Subcategories this part answers:** DIRS-2, DIRS-3 and DIRS-5, plus threats to the calibration and maintenance
facilities for DIRS-1.

**Run order:** after Parts 1 and 2. It doesn't depend on Parts 3 or 4.

## Query to refine

Using the earlier runs' records (`*_asos-about-pt1`, `*_asos-qc-formats-pt2`) and the shared runs
(`2026-11-18_noaa-rain-gauge-threats`, `2026-11-21_ghcn-daily-sources-pt5` and
`2026-11-23_ghcn-daily-infrastructure-pt8`), all in web_search_results/, which of ASOS's inputs (its stations, the
precipitation sensors and their makers, the station processors, the communications path to NWS and NCEI, the
monitoring center, the calibration and maintenance facilities, and the organizations that run them) faced funding
cuts, end of life, end of manufacturer support, operational disruptions or news about these between January 2024 and
November 2026? Check these without assuming any is affected: station counts by agency and year, the FAA sites moving
to AWOS-C, the heated tipping bucket and the All Weather Precipitation Accumulation Gauge (who makes each, whether
still supported, and whether a sensor replacement is planned), the ASOS 2.0 processors, FAA and NWS
telecommunications, the ASOS Operations and Monitoring Center, the Sterling Field Support Center, and the field
technicians. For each affected input: what happened and when; whether it is enacted, proposed or reversed; how many
stations or what share of observations it affects; and whether ASOS's archived record shows the effect (stations
dropping out of the 1-minute, GHCNh or GHCN-Daily records). If an input failed, is there a replacement, a second
supplier or a backup, and which datasets could replace ASOS itself for hourly and sub-hourly precipitation (such as
AWOS, USCRN, COOP, state mesonets, the National Mesonet Program, or radar–gauge products such as MRMS)? Rate each
input, and the inputs overall, imminent, emerging or no current threat found. Tag findings with DIRS-1 "depends on an
external calibration service that could be disrupted", DIRS-2 "upstream networks or platforms aging out or losing
funding", DIRS-3 "upstream data feeds vulnerable" or DIRS-5 "no alternative supplier". With a time limit of 40 minutes
and a token ceiling of 320,000.

### Context for the rewrite

- **The inputs are stations and sensors,** not other datasets. ASOS's "platform" (DIRS-2) is its sites and sensor
  suite; its supply chain (DIRS-3) is the sensor makers, the processors and the communications path.
- **Candidates, not facts.** List them "without assuming any is affected".
- **Already known; build on it (`2026-11-18_noaa-rain-gauge-threats`, `2026-11-23_ghcn-daily-infrastructure-pt8`):**
  206–207 FAA sites move to AWOS-C in 2025–2029, and no list marks which are climate stations (the NWS equipment
  spreadsheet of 3/18/2025 has no such column); all 1,529 ASOS 2.0 processor units were delivered by 2025; NWS is
  replacing the temperature/dew-point sensors with Vaisala HMP155E probes; the FY2027 request says "Over half of NWS
  major observing systems and capabilities are beyond or reaching end-of-life"; site gauge outages are documented at
  Springfield IL, Augusta ME and Houston IAH; no SFSC cut was found. Ask for what those runs didn't check: the
  precipitation sensors' makers and support, the station counts in the archived record, and the monitoring center.
- **Effects in the record.** Count ASOS stations reporting in the archived products by year (or GHCN-Daily's W-flag
  stations), and say whether any drop shows.
- **Alternatives (DIRS-5).** Ask for each one's coverage, time resolution, whether it is quality-controlled to
  climate standards, and its status; say plainly where AWOS falls short for climate records.
- **Rating scale, the same in every R* query:** imminent, emerging, or no current threat found.
- **Limits.** 40 minutes and 320,000 tokens: one network with a few kinds of input, though many sites.

### What the answer should give

- Station counts over time, by agency, and in the archived products.
- A table of inputs: what happened, when, its status, the stations or share affected, whether the record shows it, and
  a rating.
- The precipitation sensors' makers, support status and any second supplier.
- Substitutes for ASOS precipitation data, with coverage and status.
- An overall rating for the inputs.
- A subcategory tag on each finding.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records in web_search_results/ (`*_asos-about-pt1`, `*_asos-qc-formats-pt2`,
2026-11-18_noaa-rain-gauge-threats, 2026-11-21_ghcn-daily-sources-pt5 and 2026-11-23_ghcn-daily-infrastructure-pt8),
which of ASOS's inputs (Automated Surface Observing System) faced funding cuts, end of life, end of manufacturer
support, operational disruption or news about these between January 2024 and November 2026, and what could replace
them or ASOS's precipitation data?

Its inputs are its stations and sensors, not other datasets. Check these without assuming any is affected: station
counts by agency and year; the FAA sites moving to AWOS-C; the heated tipping bucket and the All Weather Precipitation
Accumulation Gauge (who makes each, whether still supported, any planned replacement); the ASOS 2.0 processors; FAA
and NWS telecommunications; the ASOS Operations and Monitoring Center; the Sterling Field Support Center; and the
field technicians. Already known: 206–207 FAA sites move to AWOS-C in 2025–2029 and no list marks which are climate
stations; all 1,529 ASOS 2.0 processors were delivered by 2025; temperature/dew-point sensors are being replaced; the
FY2027 request says over half of NWS's major observing systems are beyond or reaching end of life; gauge outages are
documented at Springfield IL, Augusta ME and Houston IAH.

- **For each affected input:** what happened and when; whether it is enacted, proposed or reversed; how many stations
  or what share of observations it affects; and whether the archived record shows it (count ASOS stations reporting in
  the 1-minute data, GHCNh or GHCN-Daily's W-flag stations by year, and say whether any drop shows).
- **Suppliers and backups:** a second supplier or tested replacement for each precipitation sensor; backups for the
  processors, communications and monitoring center.
- **Substitutes for ASOS precipitation data,** hourly and sub-hourly: check AWOS, USCRN, COOP, state mesonets, the
  National Mesonet Program and radar–gauge products such as MRMS for coverage, time resolution, quality control to
  climate standards and status. Say plainly where AWOS falls short for climate records.

Rate each input, and the inputs overall, imminent (enacted or happening), emerging (proposed or reported, not in
effect) or no current threat found. For each finding, say whether it supports or contradicts DIRS-1 "depends on an
external calibration service that could be disrupted", DIRS-2 "upstream networks or platforms aging out or losing
funding", DIRS-3 "upstream data feeds vulnerable" or DIRS-5 "no alternative supplier"; all four are worded as risks, so
"supports" means evidence the risk holds. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:** station counts by agency and year, and in the archived products; for each input, what happened,
when, its status, the stations or share affected, whether the record shows it, and a rating; the precipitation
sensors' makers, support status and any second supplier; substitutes for ASOS precipitation data with coverage,
resolution, QC and status, and where AWOS falls short; an overall rating; and each finding tagged DIRS-1, DIRS-2,
DIRS-3 or DIRS-5 with a stance. Expect a deep-tier run.

**What changed and why:**
- **Inputs defined as stations and sensors,** so the run doesn't look for upstream datasets: the sites and sensor
  suite are the "platform" (DIRS-2), the sensor makers, processors and communications the supply chain (DIRS-3).
- **Candidates, not facts.** The inputs and the substitutes are listed "without assuming any is affected" or matches.
- **Known facts given once,** from the rain-gauge and pt8 runs, so the run spends its time on what they didn't check:
  the precipitation sensors' makers and support, the station counts in the archived record, and the monitoring
  center. I shortened the Vaisala HMP155E detail to "temperature/dew-point sensors are being replaced"; it is in the
  pt8 record. "No SFSC cut was found" is left to that record too.
- **Effects in the record:** the run counts reporting stations by year in the archived products.
- **Cut** the answer tables; the skill sets its own format.
- **Limits:** 40 minutes and 320,000 tokens: one network with a few kinds of input, though many sites.

**How to reuse:** run after Parts 1 and 2, in this project; it doesn't need Parts 3 or 4, and Part 4 reads its
record. Keep the two `*_…` patterns until those runs exist. Its station-count findings also bear on GHCN-Daily's
DIRS-2 (ASOS is about 1.7% of GHCN-Daily's entries), and its USCRN findings on USCRN Daily's substitutes.
