# IMERG Late Run gaps Part 7: People and production R* Query for Claude

About dataset = IMERG Late Run Part 7, gaps in People risk (P-1 to P-4), calibration (DIRS-1), outside processing
(DIRS-4), alternatives (DIRS-5) and copies (RRS-1)

Written 2026-11-23 from a coverage check of IMERG Late Run's six runs. Rewrite this with `/my:rewrite-research-query`,
then run the rewritten query with `/my:broad-web-research` in its own session. Repository resilience for NASA GES DISC and PPS is in the shared NASA A2
run, not here.

## Query to refine

Using the earlier runs' records on IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM, Late Run)
(2026-11-20_imerg-late-run-about-pt1, 2026-11-21_imerg-late-run-processing-qc-pt2,
2026-11-21_imerg-late-run-formats-people-pt3, 2026-11-21_imerg-late-run-funding-pt4, 2026-11-21_imerg-late-run-news-pt5
and 2026-11-21_imerg-late-run-inputs-pt6) and NASA's satellite precipitation run
(2026-11-18_nasa-satellite-precip-threats), all in web_search_results/, who are the people critical to producing the
Late Run now, how close is each to retirement, which contracts pay them and run the processing, who maintains its
calibration, and which of its copies are current? Add to what those runs found rather than repeating it.

- **People (P-1, P-2, P-4):** start from George J. Huffman (IMERG lead, GPM Project Scientist, NASA GSFC Code 612),
  David T. Bolvin, Robert Joyce and Eric J. Nelkin (SSAI), Jackson Tan (UMBC/GSFC), Owen A. Kelley, and Erich F. Stocker
  (PPS Project Manager), confirming each by affiliation and IMERG co-authorship, and add whoever runs the Late Run day to
  day at PPS. For each: current role and whether still active; ORCID iD; earliest publication year (say from which
  source); first year on GPM or TRMM work; estimated age (earliest publication year minus 25–30); and, for federal staff,
  whether likely eligible to retire within 2 years under FERS (56–57 with 30 years' service, 60 with 20, 62 with 5).
  Mark estimates as estimates. Also: team size at PPS and in Code 612's IMERG group; any written succession or
  knowledge-transfer plan; departures since 2024 (compare staff pages on the Wayback Machine); why Christopher Kidd
  (UMD) left the author list between 2023 and 2026.
- **Contracts and processing (P-3, P-4, DIRS-4, D-1):** which contract pays the SSAI IMERG staff now that SAMDA
  NNG17HP01C ended on May 31, 2025 (ATMOS, awarded to STC from November 3, 2025, is a candidate); which contract runs PPS
  and how PPS is funded; the George Mason University CEOSR contract that writes PPS job-control software; where PDIR-Now
  is computed, and whether V08 replaces it with GPROF-IR (an IMERG-team preprint presents GPROF-IR as V08's IR
  retrieval); whether the IMERG production code is shared on request.
- **Calibration (DIRS-1):** who maintains the X-CAL offset tables that put each microwave sensor on GMI's scale (the
  GPM X-CAL working group, Wesley Berg at CSU, GSICS), how they are funded, and their current versions; which L1C ATBD
  is current (pt2 says v1.6 from 2016, pt3 cites v1.9); whether the Late Run's gauge calibration, a climatology built
  from the Final Run's GPCC adjustment, is frozen since the V07 Final record ended on September 30, 2025; what would
  calibrate IMERG if GPM's GMI or DPR stopped (the DPR–GMI combined reference has been climatological since March 1,
  2026); whether near-real-time MetOp-C GPROF has the MetOp-B calibration-file error PPS found on November 20, 2026
  (standard processing was stopped, near-real-time continued); how GPCC's V2025 change reaches the Late Run's
  climatological calibration.
- **Inputs and alternatives (DIRS-2, DIRS-3, DIRS-5):** what PPS's near-real-time stream ingests now that SSMIS
  (September 30, 2026), NOAA's AMSR2 feed (September 2, 2026) and S-NPP ATMS (November 2, 2026) have ended, and whether
  the Late Run uses AMSR3; status of the JMA forecast (precipitation phase) input; whether the V07 Late Run uses NOAA's
  new Autosnow, which includes AMSR3; whether GEOS FP itself ended on May 31, 2026 or only FP-IT did; whether CPC's
  merged IR switched to Meteosat-12; substitutes for NOAA CPC's merged IR and for GMAO's GEOS FP fields if either
  stops; which datasets could replace the Late Run for near-real-time users.
- **Copies (RRS-1, D-3):** who runs dynamical.org's IMERG copy (`s3://dynamical-nasa-imerg`), how it is funded, and
  whether it is current; whether Google Earth Engine's `NASA/GPM_L3/IMERG_V07` is current; how long PPS keeps Late Run
  files.

For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel
retirement-eligible within 2 years", P-3 "critical knowledge undocumented", P-4 "a single person is a point of
failure", D-1 "program defunded or under threat", DIRS-1 "depends on an external calibration service that could be
disrupted", DIRS-3 "upstream data feeds vulnerable", DIRS-4 "needs outside processing infrastructure", DIRS-5 "no
alternative supplier" or RRS-1 "two or more geographically independent sites hold verified copies" (RRS-1 is a
strength, so "supports" means resilience). Say so where nothing is published. Leave NASA's budget, cuts and news to the
earlier runs. Use NASA's own pages, contract databases (SAM.gov, USAspending, HigherGov), papers, and ORCID or OpenAlex
records ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

### Context for the rewrite

- **Keep it standard tier.** No cuts or threats are asked for. NASA's budget, the proposed end of GPM funding, Goddard's
  staff losses and the DAAC consolidation are in pt4, pt5 and the NASA satellite run.
- **CHRS people are in PERSIANN-CDR's Part 7.** UC Irvine's CHRS (Braithwaite, Hsu, Nguyen, Sorooshian) supplies the
  PDIR-Now method. If PERSIANN-CDR's Part 7 runs first, name its run so this one can cite it instead of looking them up
  again.
- **Retirement rules differ by employer.** FERS applies to NASA civil servants (Huffman, Stocker). For contractor and
  university staff (SSAI, UMBC), give the estimated age and say no federal rule applies.
- **Already found, don't search again (from the coverage check):**
  - no headcount is published for the IMERG team, PPS or GES DISC; the 13-author ATBD list is the only proxy (pt3);
  - the IMERG production code is not public (no repositories in the nasa GitHub organization); GPROF-NN is MIT-licensed
    on GitHub (pt3);
  - Huffman leads the algorithm; Stocker is PPS's NASA official (pt3);
  - GMI is the L1C X-CAL reference; quantile matching to the DPR–GMI combined product; GPCP ratio adjustment at high
    latitudes; the Late Run never reads gauges directly (pt2);
  - contracts from pt4: SAMDA NNG17HP01C (SSAI, ended 2025-05-31), ATMOS (STC, from 2025-11-03), EED-3 80GSFC21CA001
    (Raytheon, to 2027-01-31), HBG 80GSFC20C0044 (SSAI, being recompeted);
  - the status of every satellite input from 2024 to 2026 (pt6, NASA and NOAA satellite runs);
  - from pt6: WSF-M1 MWI near-real-time files in PPS since August 12, 2026 and AMSR3 1C from about August 25, 2026;
    GPM's estimate that losing SSMIS raises the Late Run's IR share from 9.9% to 22.9% (about 15.1% with MWI); PPS's
    V08 GPROF halt (September 18, 2026) and L3 recall (October 1, 2026); GEOS FP upgrades on February 26 and
    November 18, 2026.
- **Not for this run:** JAXA's AMSR2 notices and EUMETSAT's Metop-B and Meteosat-9 end dates. Pt6 rated those inputs,
  and the sandbox refuses their hosts (see pt6's `check-by-hand.md` and `sites-to-trust.md`).
- **Leads:** the PPS project page (science.gsfc.nasa.gov/earth/projects/212); the GSICS microwave deliverable page
  (gsics.atmos.umd.edu), unreachable last time; the L1C ATBD v1.9 on arthurhou.pps.eosdis.nasa.gov; the unread
  "Details" links on the PPS home page (pps.gsfc.nasa.gov) for September 30, October 28 and November 20, 2026; the
  Earthdata Forum thread on GMAO_FP (forum.earthdata.nasa.gov/viewtopic.php?p=26053), down last time; the V07 ATBD
  (August 13, 2026) for the GPCC climatology. The Late Run file headers list their inputs but need a PPS sign-up, so
  say where that would settle a question rather than signing up.

### What the answer should give

- A table of people: role, employer, active or not, ORCID iD, earliest publication year and its source, estimated age,
  and a likely-eligible flag where a rule applies.
- Team sizes, any succession plan, and departures since 2024.
- A table of contracts: number, holder, dates, and what each pays for.
- Who maintains the calibration, its funding and versions, and what would replace GPM as the reference.
- Substitutes for inputs and for the Late Run.
- A table of copies: who runs each, its funding, and whether it is current.
- A stance for each finding against the subcategory statements.

## Claude web research skill query

### Run 1: people, contracts and processing

/my:broad-web-research

Using the earlier runs' records on IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM, Late Run) (2026-11-20_imerg-late-run-about-pt1, 2026-11-21_imerg-late-run-processing-qc-pt2, 2026-11-21_imerg-late-run-formats-people-pt3, 2026-11-21_imerg-late-run-funding-pt4, 2026-11-21_imerg-late-run-news-pt5 and 2026-11-21_imerg-late-run-inputs-pt6) and NASA's satellite precipitation run (2026-11-18_nasa-satellite-precip-threats), all in web_search_results/, who are the people critical to producing the Late Run now, how close is each to retirement, and which contracts pay them and run its processing? Add to what those runs found rather than repeating it.

- **People:** start from George J. Huffman (IMERG lead, NASA GSFC Code 612), David T. Bolvin, Robert Joyce and Eric J. Nelkin (SSAI), Jackson Tan (UMBC/GSFC), Owen A. Kelley, and Erich F. Stocker (PPS Project Manager), confirming each by affiliation and IMERG co-authorship, and add whoever runs the Late Run day to day at PPS. For each: current role and whether still active; ORCID iD; earliest publication year and its source; first year on GPM or TRMM work; estimated age (earliest publication year minus 25–30). For NASA civil servants, say whether each is likely eligible to retire within 2 years under FERS (56–57 with 30 years' service, 60 with 20, 62 with 5); for contractor and university staff, give the estimated age and say no federal rule applies. Mark estimates as estimates.
- **Team and succession:** team sizes at PPS and in Code 612's IMERG group; any written succession or knowledge-transfer plan; departures since 2024, from staff pages on the Wayback Machine; why Christopher Kidd (UMD) left the author list between 2023 and 2026.
- **Contracts and processing:** which contract pays the SSAI IMERG staff since SAMDA NNG17HP01C ended on May 31, 2025 (check ATMOS, awarded to STC from November 3, 2025, as a candidate); which contract runs PPS and how PPS is funded; the George Mason University CEOSR contract that writes PPS job-control software; where PDIR-Now is computed, and whether V08 replaces it with GPROF-IR; whether the IMERG production code is shared on request.

The earlier runs already have the 13-author ATBD list as the only headcount proxy, Huffman's and Stocker's roles, the unpublished production code, and contracts EED-3 80GSFC21CA001 and HBG 80GSFC20C0044; build on them. The PPS project page (science.gsfc.nasa.gov/earth/projects/212) is an unread lead. For each finding, say whether it supports or contradicts P-1 "no documented succession plan", P-2 "key personnel retirement-eligible within 2 years", P-3 "critical knowledge undocumented", P-4 "a single person is a point of failure", D-1 "program defunded or under threat" or DIRS-4 "needs outside processing infrastructure", and say so where nothing is published. This asks about current staff and contracts; leave NASA's budget, cuts and news to the earlier runs. Use NASA's own pages, contract databases (SAM.gov, USAspending), papers and ORCID or OpenAlex records ahead of news, and check ORCID against one other source. With a time limit of 40 minutes and a token ceiling of 320,000.

### Run 2: calibration, inputs, alternatives and copies

/my:broad-web-research

Using the same earlier runs' records on IMERG Late Run and NASA's satellite precipitation run, all in web_search_results/, who maintains the Late Run's calibration today, what does it ingest now that several feeds have ended, what could replace its inputs or the dataset itself, and which of its copies are current? Add to what those runs found rather than repeating it.

- **Calibration:** who maintains the X-CAL offset tables that put each microwave sensor on GMI's scale (check the GPM X-CAL working group, Wesley Berg at CSU and GSICS), how they are funded, and their current versions; which L1C ATBD is current (pt2 says v1.6 of 2016, pt3 cites v1.9); whether the Late Run's climatological gauge calibration has been frozen since the V07 Final record ended on September 30, 2025, and how GPCC's V2025 change reaches it; what would calibrate IMERG if GMI or DPR stopped (the DPR–GMI combined reference has been climatological since March 1, 2026); whether near-real-time MetOp-C GPROF has the MetOp-B calibration-file error PPS reported on November 20, 2026.
- **Inputs:** what PPS's near-real-time stream ingests since SSMIS (September 30, 2026), NOAA's AMSR2 feed (September 2, 2026) and S-NPP ATMS (November 2, 2026) ended, and whether the Late Run uses AMSR3; the status of the JMA forecast input for precipitation phase; whether the V07 Late Run uses NOAA's new Autosnow; whether GEOS FP itself ended on May 31, 2026 or only FP-IT; whether CPC's merged IR switched to Meteosat-12. Where only the Late Run file headers (behind a PPS sign-up) would settle a point, say so rather than signing up.
- **Alternatives:** substitutes for CPC's merged IR and for GMAO's GEOS FP fields if either stops; which datasets could replace the Late Run for near-real-time users, with latency, coverage and status.
- **Copies:** how long PPS keeps Late Run files, and which other copies of the Late Run outside PPS and GES DISC are current.

Unread leads from the earlier runs: the GSICS microwave page (gsics.atmos.umd.edu), the L1C ATBD v1.9 on arthurhou.pps.eosdis.nasa.gov, the "Details" links on pps.gsfc.nasa.gov for September 30, October 28 and November 20, 2026, the Earthdata Forum GMAO_FP thread and the V07 ATBD of August 13, 2026. Don't revisit JAXA's AMSR2 notices or EUMETSAT's Metop-B and Meteosat-9 dates; pt6 rated those. For each finding, say whether it supports or contradicts DIRS-1 "depends on an external calibration service that could be disrupted", DIRS-3 "upstream data feeds vulnerable", DIRS-5 "no alternative supplier" or RRS-1 "two or more geographically independent sites hold verified copies" (RRS-1 is a strength, so "supports" means resilience), and say so where nothing is published. This asks what is in place now; leave cuts and news to the earlier runs. Use NASA's and PPS's own pages, the ATBDs, X-CAL and GSICS documents and the hosts' own catalogs ahead of news. With a time limit of 40 minutes and a token ceiling of 320,000.

## Claude comments about the rewritten query

**What you'll get:**
- **Run 1 (people, contracts, processing):** a row per person (role, employer, active or not, ORCID iD, earliest publication year and its source, first GPM/TRMM year, estimated age, a FERS flag for Huffman and Stocker only), team sizes as far as they are public, any succession plan, departures since 2024 and Kidd's, a list of contracts with holder, dates and what each pays for, where PDIR-Now is computed, and a stance on P-1 to P-4, D-1 and DIRS-4.
- **Run 2 (calibration, inputs, alternatives, copies):** who keeps X-CAL and at what version, the current L1C ATBD, the state of the gauge climatology, the post-GPM reference question, what the near-real-time stream ingests now, substitutes for CPC IR, GEOS FP and the Late Run itself, the copies' status, and a stance on DIRS-1, DIRS-3, DIRS-5 and RRS-1.

**What I changed from your draft:**
- **Split into two runs.** Your draft has five bullets with about 25 separate checks. People and contracts live in ORCID, papers and contract databases; calibration, inputs and copies live in ATBDs, PPS notices and catalogs. One 40-minute run would leave every part thin. Neither run needs the other, so either order works.
- **"Already found" folded in** as one sentence in Run 1 and as "pt2 says / pt3 cites" in Run 2, so the runs build on the earlier records.
- **Leads kept, as one short sentence per run,** because they are specific pages the earlier runs couldn't read; the PPS project page went to Run 1, the rest to Run 2.
- **"Not for this run" kept** as one sentence (JAXA, EUMETSAT), so Run 2 doesn't spend time on hosts the sandbox refuses.
- **Blocked hosts left out:** HigherGov from the contract databases, and dynamical.org's copy and Earth Engine's from the copies bullet. None of their hosts is in `.claude/settings.local.json`. The copies bullet now asks only how long PPS keeps files and which other copies are current.
- **CHRS people:** left out, as your context says. If PERSIANN-CDR's Part 7 Run 1 runs first, add its folder to Run 1's list of earlier runs so this run can cite it on PDIR-Now's method.
- **Standard tier:** both questions say they are about current arrangements. Run 2 lists several feeds that have ended, which is the part most likely to push the skill toward deep; if it does, the limits still hold.

**Limits:** both at 40 minutes and 320,000 tokens. Run 2 has the most separate checks of any of the three Part 7s. To save usage, Run 2 could take 30 minutes and 240,000; the alternatives and copies would be thinnest.

**One-run version:** put all eight bullets under Run 1's opening question, with all ten statements, at 40 minutes and 320,000 tokens (your draft's limits). It gives up most of the calibration and input checks: the people and contracts would take most of the time.

**Hosts:** the NASA, PPS, SAM.gov, USAspending, UMD (GSICS) and CSU hosts the questions name fall under the `.gov` and `.edu` rules. The open "which other copies" question may still lead the run to a refused host; it would list any in `sites-to-trust.md`.

**Order and reuse:** run both in this project, after the IMERG runs (all done). Don't add "Don't use earlier runs."; both depend on them. GPCP's Part 7 overlaps on Huffman, Bolvin and Nelkin, so whichever runs second can name the first one's record.
