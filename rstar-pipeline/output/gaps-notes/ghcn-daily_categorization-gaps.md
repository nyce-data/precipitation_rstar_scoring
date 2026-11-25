# GHCN-Daily: what the research didn't search, by subcategory

- **Dataset:** GHCN-Daily (GHCNd), NOAA NCEI. DOI 10.7289/V5D21VHZ, current version 3.35.
- **Categorized:** 2026-11-23 (third pass, adding the four gap runs and the NCEI A2 run; replaces the second pass of 2026-11-22).
- **Output:** [ghcn-daily_rstar-categories.json](../data-rstar-categories/datasets/ghcn-daily/ghcn-daily_rstar-categories.json). It was built by `rstar-pipeline/processing/scripts/categorize/build_ghcn-daily.py`.
- **Research used:** every answer file in `rstar-pipeline/input/web-research/` that bears on GHCN-Daily:
  - `about-datasets/ghcn-daily/`: about-pt1, about-pt2, about-pt3_combined, funding-pt3, threats-news-pt4 and sources-pt5,
    plus the gap runs people-pt6, repository-pt7, infrastructure-pt8 and repository-resilience-pt9;
  - `archives/noaa-ncei/2026-11-17_noaa-ncei-threats` and `archives/noaa-ncei/2026-11-23_A2_Rstar_query-noaa_ncei`;
  - `instruments/noaa-rain-gauges/2026-11-18_noaa-rain-gauge-threats`.
- **Not used:** the NASA and NOAA satellite runs. GHCN-Daily uses only station data, so they don't apply.

> **Update 2026-11-23: all four gap runs and the NCEI A2 run have come back.** They are in
> `rstar-pipeline/input/web-research/`: `about-datasets/ghcn-daily/2026-11-23_ghcn-daily-people-pt6`,
> `2026-11-22_ghcn-daily-repository-pt7`, `2026-11-23_ghcn-daily-infrastructure-pt8`,
> `2026-11-23_ghcn-daily-repository-resilience-pt9`, and `archives/noaa-ncei/2026-11-23_A2_Rstar_query-noaa_ncei`.
> The third categorization pass (2026-11-23) uses them. See **After the gap runs** at the end of this note for what each
> subcategory now has and what is still open. The sections in between are the gaps as they stood on 2026-11-22.

Each subcategory below lists the questions the research never asked, so a decision on it can't be made from what we have. "Partly covered" means there is evidence, but the subcategory's own question is still open. Each list ends with possible searches you could turn into queries.

## Summary

| Subcategory | Coverage | What's missing |
|---|---|---|
| P-1 Succession plan | Partly covered | Any written succession or knowledge-transfer plan; team size |
| P-2 Retirement-eligible | **Not searched** | Ages, ORCID, start dates of key people |
| P-3 Undocumented knowledge | Partly covered | Internal code and runbooks; the Datzilla procedure |
| P-4 Single point of failure | Partly covered | Who runs integration; staff roster |
| D-1 Program defunding | Covered | GHCN-Daily's own budget share; the NODD (cloud) program's funding |
| D-2 Storage single point | Partly covered | NCEI storage, backup and failover design; processing after the AWS move |
| D-3 Access fragile | Partly covered | Funding and staff of CDO, the Access Data Service and the NODD agreements |
| D-4 Format obsolescence | Covered | Parquet, BigQuery and NetCDF schemas only |
| D-5 Political sensitivity | Covered | — |
| DIRS-1 Calibration | **Not searched** | Calibration labs and standards for every contributing network |
| DIRS-2 Observation networks | Covered (US); thin abroad | Network health outside the US, Canada, Europe and Australia; ASOS climate-site list |
| DIRS-3 Upstream supply chain | Covered | SSODv2 back-fill; Canada cause; RCC contract after Oct 2026 |
| DIRS-4 External processing | Partly covered | Where processing runs after the AWS migration |
| DIRS-5 No alternative supplier | Partly covered | Substitute datasets for GHCN-Daily |
| RRS-1 Geographic redundancy | Partly covered | Verified copies; whether NCEI holds copies at two sites |
| RRS-2 Checksum verification | **Not searched** | Fixity and checksum policy; CoreTrustSeal |
| RRS-3 Disaster recovery plan | **Not searched** | COOP or DR plan and its last test |
| RRS-4 Stable funding | Covered (NCEI) | Funding of the AWS and Google copies (NODD) |
| RRS-5 Track record | Partly covered | Holdings and ingest delays before and after a disruption |

## People risk

### P-1: No documented succession plan
- **Not searched:**
  - any succession plan, workforce plan or knowledge-transfer procedure for GHCN-Daily or for NCEI's Climatic Science & Services Division;
  - the size of the GHCN-Daily team;
  - an NCEI org chart newer than February 2023.
- **Possible searches:**
  - "NCEI workforce plan" and "NOAA succession planning" (also OIG and GAO reports on NOAA workforce);
  - "NCEI organizational chart 2025" and "2026";
  - "GHCNd Operations Team" staff;
  - CISESS task reports that name GHCN-Daily staff.

### P-2: Key personnel retirement-eligible
- **Not searched (nothing collected):**
  - ages and retirement eligibility of the key people;
  - when each joined NCEI/NCDC;
  - ORCID IDs and earliest publication years.

  The only proxy is that Durre and Menne have published on GHCN-Daily since at least 2008–2010.
- **People to look up:**
  - the principal investigators, Matthew J. Menne and Imke Durre;
  - Russell S. Vose;
  - the other Version 3 citation authors: Korzeniewski, McNeill, Thomas, Yin, Anthony, Ray, Gleason and Houston;
  - Rennie and Stevens, named in part 4.
- **Possible searches:**
  - ORCID or Google Scholar profiles, with the earliest publication year;
  - an NCEI staff page or bio for each person;
  - the 2023 NWS seminar bios;
  - "retired" together with each name.

### P-3: Critical undocumented knowledge
- **Not searched or not reachable:**
  - whether NCEI shares the GHCN-Daily code on request;
  - whether NCEI has internal runbooks for integrating sources and writing files;
  - how the Datzilla ticket review works and who staffs it. The NWS directive that mentions it returned HTTP 403.
  - code.noaa.gov, which didn't resolve;
  - the GitHub API, which the sandbox refused.
- **Possible searches:**
  - "Datzilla NCEI";
  - "GHCN-Daily source code";
  - code.noaa.gov GHCN;
  - the NWS directive on Datzilla (10-13xx series).

### P-4: Single person is point of failure
- **Not searched:**
  - who runs integration of a new source;
  - how many people can run the weekly rebuild;
  - whether anyone covers the PIs' roles;
  - what CISESS staff and the contractors (Alpha Omega, Consolidated Safety Services) actually do for GHCN-Daily.
- **Possible searches:**
  - CISESS annual reports for 2023–2026, with their GHCN tasks;
  - USAspending or HigherGov descriptions of NCEI's support contracts;
  - recent GHCN-Daily papers, to see who the current co-authors are.

## Data risk

### D-1: Active or threatened program termination or defunding
- **Covered:** the NCEI budget line for FY2025–FY2027, and the CISESS agreement.
- **Not searched:**
  - funding of NOAA's Open Data Dissemination (NODD) program, which places the AWS and Google copies;
  - whether CPO's Climate Observations and Monitoring support continued after 2021;
  - GHCN-Daily's own share of any budget, which is unpublished (FOIA or ncdc.ghcnd@noaa.gov).
- **Watch:** the FY2027 law, or the next continuing resolution, after December 11, 2026.

### D-2: Storage system end-of-life or single point of failure
- **Not searched:**
  - NCEI's storage hardware and its age;
  - its backup sites and failover;
  - whether GHCN-Daily is stored at both Asheville and Boulder;
  - whether GHCN-Daily *processing* (not just storage) moves to AWS, and who runs it after Spring 2027.
- **Possible searches:**
  - the NCEI cloud migration plan and FAQ details;
  - OIG-24-034-A (NESDIS cloud);
  - NCEI's archive system (for example "NCEI archive storage system" and "Common Ingest").

### D-3: Access infrastructure fragile or unfunded
- **Not searched:**
  - staffing and funding of Climate Data Online and the Access Data Service;
  - the terms and funding of the NODD agreements with AWS and Google;
  - whether the May 2026 NCEI fee schedule applies to GHCN-Daily routes.
- **Possible searches:**
  - "NOAA Open Data Dissemination funding" and "NODD contract";
  - "Climate Data Online retirement" or "CDO modernization";
  - the NCEI fee schedule in the Federal Register (2026).

### D-4: Format obsolescence
- **Not read:** the AWS Parquet schema and units, the BigQuery table schema, and NetCDF output with CF names. The one NetCDF request came back empty.

### D-5: Political sensitivity
- Nothing major is missing. One open item is which "at least 20" datasets NOAA decommissioned (from the update owed under S. Rept. 119-44).

## Dependent infrastructure resilience

### DIRS-1: Calibration facility dependency
- **Not searched (no run asked about calibration):**
  - who calibrates the gauges and thermometers of COOP, ASOS, CoCoRaHS, SNOTEL, RAWS and USCRN;
  - which reference standards or labs they rely on (for example NIST-traceable calibration, or NWS's Sterling field support center);
  - whether any inter-comparison program (WMO or GCOS) is involved;
  - how foreign national services calibrate their networks.

  The definition's "How to find" text asks who does processing and QC, which the research did cover; but the subcategory itself is about calibration.
- **Possible searches:**
  - "ASOS sensor calibration NWS Sterling";
  - "COOP rain gauge calibration";
  - "USCRN calibration ATDD";
  - "SNOTEL sensor calibration NRCS";
  - "WMO instrument intercomparison precipitation gauge";
  - "Regional Instrument Centre".

### DIRS-2: Observation network or sensor platform at risk
- **Covered:** US networks (COOP, ASOS, USCRN, CoCoRaHS, SNOTEL, RAWS); thin for networks abroad.
- **Not searched:**
  - network health and funding for national services outside the US, Canada, Europe and Australia, which have only general WMO-level evidence;
  - which ASOS-to-AWOS sites are GHCN-Daily climate sites;
  - the outcome of the COOP right-sizing (watch SAM.gov 1305M2-COOP).
- **Possible searches:**
  - national weather service budget cuts for the countries with the largest station losses (Russia, China, Indonesia, Argentina, Algeria);
  - the NWS AWOS-C conversion site list.

### DIRS-3: Upstream data supply chain at risk
- **Open questions (searched but not settled):**
  - whether SSODv2's full period of record was integrated;
  - why Canada's feed stopped in 2024;
  - whether the 174 Alberta stations removed by ECCC reach GHCN-Daily;
  - the RCC contract after October 16, 2026.
- **Not searched:** GHCNh's own stability, now that SSODv2 is derived from it.

### DIRS-4: External processing infrastructure dependency
- **Not searched:**
  - where GHCN-Daily processing will run after the AWS migration, and who operates it;
  - whether the CISESS cloud prototype went into production;
  - NCEI's computing platform for the Fortran QC.
- **Possible searches:**
  - "GHCN-Daily cloud processing";
  - CISESS reports from 2023–2026;
  - "NCEI cloud migration processing".

### DIRS-5: No alternative supplier
- **Not searched:**
  - datasets that could stand in for GHCN-Daily if it stopped, for example national archives, ECA&D, Berkeley Earth's daily data, HadISD, or the Copernicus C3S station data;
  - whether any foreign station has a second route into GHCN-Daily besides the synoptic stream.

## Repository resilience

The repositories are NCEI, the AWS copy (noaa-ghcn-pds) and the Google BigQuery copy.

### RRS-1: Geographic redundancy
- **Not searched:**
  - whether the copies are verified against each other;
  - whether NCEI keeps GHCN-Daily at both Asheville and Boulder (and, after the move, in more than one AWS region);
  - the update chain from NCEI to the AWS and Google copies.

### RRS-2: Regular backup integrity verification
- **Not searched (no evidence collected):**
  - NCEI's fixity and checksum practice, and how often it runs;
  - CoreTrustSeal or ISO 16363 certification;
  - whether the AWS and Google copies are checked;
  - the content of NESDIS's 2021 stewardship maturity review DSMR-00227, which was found but not read for this.
- **Possible searches:**
  - "NCEI CoreTrustSeal";
  - "NCEI fixity checksum archive";
  - "NOAA NAO 212-15 archive";
  - DSMR-00227;
  - "NCEI ISO 16363".

### RRS-3: Disaster recovery plan tested
- **Not searched:**
  - NCEI's continuity-of-operations (COOP) or disaster recovery plan, and when it was last tested;
  - lessons-learned reports after Hurricane Helene;
  - the two Commerce OIG reports that were found but not opened: OIG-24-034-A (NESDIS cloud) and OIG-16-043-A (NESDIS cyber incident).
- **Possible searches:**
  - "NCEI continuity of operations plan";
  - "NCEI Helene recovery report";
  - "NESDIS disaster recovery OIG".

### RRS-4: Stable institutional funding
- **Covered:** NCEI.
- **Not searched:**
  - funding and terms of the AWS and Google copies (NODD), and whether the cloud vendors' no-cost hosting can end;
  - whether NCEI actually received its FY2026 $69.0M (the spend plan is not public).

### RRS-5: Track record through prior disruption
- **Not searched:**
  - NCEI's holdings and ingest before and after a disruption: dataset counts, ingest backlogs or delays after Helene, the 2025 staff losses and the 2025 shutdown, and earlier events such as the 2013 and 2018–19 shutdowns.
- **Possible searches:**
  - "NCEI archive holdings petabytes 2024 2025";
  - "NCEI ingest backlog";
  - "NCDC shutdown 2013 data".

## Changes from the first pass

- **Added two runs outside the GHCN-Daily folder:** the NCEI run (21 evidence items) and the rain-gauge run (10), as CLAUDE.md now allows.
- **Re-read all six GHCN-Daily runs** and re-sorted their evidence (151 items in all, up from 114).
- **RRS-2 is no longer empty:** it has thin evidence.
- **DIRS-1 now draws on gauge maintenance and USCRN evidence.**
- **Same JSON format as before:** an Evidence list and a Gaps list, with `data-confidence` and `data-source` attributes. Gaps in the JSON are short; this note holds the full list.

## After the gap runs (2026-11-23)

Checked against the five new runs: people-pt6, repository-pt7, infrastructure-pt8, repository-resilience-pt9 and the
NCEI A2 run. Every subcategory that was **not searched** now has evidence. What's left is mostly unpublished: NCEI,
NESDIS or OPM hold it, so it needs an email, a FOIA request or a page read by hand, not another web search.

| Subcategory | Now | Main new evidence | Still open |
|---|---|---|---|
| P-1 Succession plan | Covered | No GHCN-Daily, NCEI or NESDIS plan published; NAO 202-1103 lists succession only as a "possible strategy" (pt6) | NOAA's 2012 succession toolkit and Commerce's 2022 guide (unread; generic) |
| P-2 Retirement-eligible | Covered (low confidence) | ORCID/OpenAlex estimates: Vose likely already eligible, Menne possibly by Nov 2028; Durre left 30 Apr 2025 (pt6) | Real service dates and ages (OPM records, not public) |
| P-3 Undocumented knowledge | Covered | DSMR-00227: "not currently under Configuration Management"; no public code (pt6) | Code-sharing policy (ask ncdc.ghcnd@noaa.gov) |
| P-4 Single point of failure | Covered | Menne is the one named federal scientist left; hands-on staff are Riverside Technology contractors; Datzilla gatekeeper may be one contractor (unverified) (pt6) | Who replaced Durre; current status of Gleason, Houston, Korzeniewski, Kantor |
| D-1 Program defunding | Covered | No CPO COM support found after 2021 (pt7) | GHCN-Daily's own budget share (unpublished) |
| D-2 Storage single point | Covered | Two tape copies, the offsite one 12.5 miles from Asheville (pt9); AWS lift-and-shift by spring 2027 run by contractors; NCCF single region (OIG-24-034-A) (pt7) | Where GHCN-Daily sits after the move; whether tapes are kept |
| D-3 Access fragile | Covered | "Data Access Delays" alert 16–30 Nov 2026; NODD on 2019 contracts with no published end; fee rule doesn't touch online GHCN-Daily (pt7) | NODD contract records for AWS and Google; CDO/ADS staff and funding |
| D-4 Format obsolescence | Covered | All routes open formats; no published Parquet or BigQuery schema (pt7) | Schemas and ADS NetCDF attributes (read by hand) |
| D-5 Political sensitivity | Covered | None of the 2025–26 NCEI retirements is a GHCN-Daily route (pt7) | The Senate's list of "at least 20" (unpublished) |
| DIRS-1 Calibration | Covered | ATDD's 8-person USCRN team, parent ARL proposed for closure FY26 and FY27; Sterling SFSC running; WMO RICs being reformed (pt8) | ARL/ATDD's FY2026 status (spend plan not public) |
| DIRS-2 Observation networks | Covered | NWS electronics technicians down ≥16%; SMN Argentina dismissals and station closures; NRCS snow-survey warnings (pt8) | Which SMN stations close; AWOS-C climate-site list (FAA) |
| DIRS-3 Upstream supply chain | Covered | SSODv2 full record still not confirmed; GHCNh now upstream; Canada restored Oct 2026; RCCs re-awarded to 2031 (pt8) | SSODv2 integration (spot-check source flags or ask NCEI); GHCNh funding |
| DIRS-4 External processing | Covered (by absence) | Where processing runs after the AWS move is unpublished (pt7, pt8) | NCEI holds it |
| DIRS-5 No alternative supplier | Covered | HadISD stopped; ECA&D, C3S and WIS2 current but none is a global QC'd daily archive (pt8) | — |
| RRS-1 Geographic redundancy | Covered | Asheville's two copies are 12.5 miles apart; Boulder has dispersed copies only of its own holdings; AWS and BigQuery single-region (pt9, NCEI A2) | AWS regions and copy count after the move |
| RRS-2 Checksum verification | Covered | Checksums at ingest, retrieval and order, not on a schedule; size-only comparisons between copies; NCEI CoreTrustSeal valid to 2028-01-29 (pt9, NCEI A2) | SOP 60-6-015 (not public) |
| RRS-3 Disaster recovery plan | Covered (by absence) | NESDIS requires annual tests; no test or result is public; NCEI's contingency plan "cannot be shared outside the US Government" (pt9, NCEI A2) | Test results (FOIA) |
| RRS-4 Stable funding | Covered | FY2026 enacted, no rescission; NODD copies have no guaranteed term (pt9) | NCEI's FY2026 spend plan |
| RRS-5 Track record | Covered | Helene: holdings safe, 92% of ingest backlog recovered, 8% unaccounted; no shutdown loss found (pt9, NCEI A2) | Final Helene loss count |

### Conflicts to settle when categorizing

- **OIG-24-034-A:** pt7 says recommendations 3, 9 and 10 were open in Sept 2025; pt9 and NCEI A2 found them, and
  recommendation 11 (single region), "Closed" on Oversight.gov with no date or action. Use the later finding.
- **NODD term:** the 2023 slides give a ten-year term to about Sept 2029 (inference), while two 2019 Big Data Project
  IDIQs on USAspending ended 2025-09-19. They may be different instruments (pt9, low).
- **NCCF regions:** a 2021 prototype briefing says "cross-region replication"; OIG found one region in 2024 (NCEI A2).
- **Pt9's cross-links** point to `../<run>/answer.md`, which here is named `answer_<query>.md`.

### Left for checking by hand (no new web search planned)

- the AWS per-station files: a checker lead says they haven't been written since 2025-02-09; check object dates in
  `noaa-ghcn-pds` (pt9);
- SSODv2's full-record integration: spot-check station `.dly` files for source flag "2" (pt8);
- the Parquet footer and BigQuery schema tab (pt7);
- the 2022 WERA1012 slides naming the "Datzilla Gatekeeper" (pt6);
- each run's `check-by-hand.md` in `Rstar_query_results/web_search_results/` (not copied here).

## Changes from the second pass (2026-11-23)

- **Added the five new runs:** 73 evidence items (people-pt6 17, repository-pt7 16, infrastructure-pt8 20,
  repository-resilience-pt9 14, NCEI A2 6).
- **Dropped 10 items** that only said a topic was "not searched" or "not read", now that a run has searched it (for
  example the P-2, DIRS-1, RRS-2 and RRS-3 placeholders, and the unread fee rule and OIG reports).
- **DIRS kept to the dataset's own dependencies:** four DIRS-4 items about NCEI as a whole (the archive's move to
  AWS, NCEI's support contracts, Hurricane Helene, the migration contractors) were removed; each is already under
  D-2, D-3, P-4 or RRS. That leaves 210 items in all.
- **Every Gaps list rewritten** to what is still open after the gap runs (the table above).
- **The script now keeps each item's stance next to it** (a fourth tuple field) instead of in a separate table of
  letters, so items can be added or removed without shifting the others' stances. The second-pass output was rebuilt
  byte-identical before any evidence changed.
- **Older items kept as they were** even where a later run adds to them, for example the rain-gauge run's "Congress
  rejected" ARL closure for FY2026, next to pt8's finding that the enacted statement doesn't name ARL.
