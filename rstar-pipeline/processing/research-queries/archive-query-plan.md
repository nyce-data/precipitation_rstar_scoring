# Plan: a general archive search, and where repository questions belong

Written 2026-11-23. It goes with `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` and settles where repository questions live: in
**separate repository runs (A1 and A2), not inside the dataset parts.** The CoCoRaHS archive is worked through as the
first new case.

## Three kinds of repository

The coverage checks of GPCP Daily, IMERG Late Run and PERSIANN-CDR Daily found more than 15 places that serve the four datasets.
They fall into three kinds, and each kind needs different research:

| Kind | Examples | Runs | Why |
|---|---|---|---|
| **Shared archive:** hosts datasets that other groups make | NOAA NCEI, NASA GES DISC | **A1 threats** (deep, 50 min / 400,000) and **A2 resilience** (standard, 40 min / 320,000), once per archive | Its budget and practice are the same for every dataset it holds, so one pair of runs serves them all |
| **Producer's own data site:** the group that makes the dataset also serves it | CoCoRaHS (cocorahs.org), CHRS at UC Irvine, NASA PPS | **A2 only** (standard, 30–40 min). Add questions about the site's own team | Its funding is the producer's funding, which the dataset's Part 4 already covers. A small site can depend on one developer (D-3) |
| **Copy:** a mirror, cloud bucket or redistributor with no budget of its own for the data | NODD buckets on AWS, Google and Azure; Earth Engine; dynamical.org; IRI; Data Rescue Project; NCAR GDEX; Copernicus CDS | **No run.** The dataset's own run checks whether each copy exists and is current (RRS-1) | It matters only as a second copy. The parent archive's A2 covers the contracts behind the NODD buckets |

The templates are in `Rstar_query_results/queries/archive_queries/general_archive_queries/`:
- `A1_Rstar_query_template-repository-threats.md` (new; generalized from the NCEI threats query);
- `A2_Rstar_query_template-repository-resilience.md` (updated with the two kinds).

## How to search a new archive

1. **Start from the dataset's Part 1 host list.** Part 1 names every repository, mirror and copy, and which one is the
   archive of record.
2. **Sort each host into one of the three kinds** above, and check the register below. If the archive already has its
   runs, the dataset's Part 4 and gap runs just cite them.
3. **For a new shared archive,** write A2 and A1 from the templates. Run A2 first (it lists the systems and who pays
   for them), then A1.
4. **For a producer's own data site,** write A2 with `$THREATS_RUN` set to the dataset's Part 4, and ask Part 4 to
   include the site's funding and outages.
5. **For a copy,** add it to the dataset's copies question (whether it is current, and who runs it).
6. **Run the repository runs before the dataset's Part 4,** so Part 4 can cite them.
7. **Copy the results** into `rstar-pipeline/input/web-research/archives/<repository>/`. The categorization of every dataset
   that repository hosts uses them for RRS and for D-2 and D-3.

## Register of repositories

| Repository | Kind | Datasets | A1 threats | A2 resilience |
|---|---|---|---|---|
| NOAA NCEI | Shared archive | GHCN-Daily, GPCP Daily (1DD V1.3, V3.3 CDR), PERSIANN-CDR Daily, ASOS and USCRN Daily (both added 2026-11-25); also holds CoCoRaHS reports inside GHCN-Daily | Done: `2026-11-17_noaa-ncei-threats` | Done: `2026-11-23_A2_Rstar_query-noaa_ncei` |
| NASA GES DISC | Shared archive | IMERG Late Run, GPCP Daily (V3.x) | Not planned: IMERG's funding and news runs and the NASA satellite run cover NASA's data-systems budget | Done, with PPS: `2026-11-27_gesdisc-pps-resilience` (query `A2_Rstar_query-nasa_gesdisc_pps.md`) |
| NASA PPS | Producer's site | IMERG Late Run | — (IMERG's Part 4 runs) | In the GES DISC run |
| UC Irvine CHRS | Producer's site | PERSIANN-CDR Daily (and PDIR-Now, an IMERG input) | — (PERSIANN-CDR's pt3 and pt4) | Done: `2026-11-27_uci-chrs-resilience` (query `A2_Rstar_query-uci_chrs.md`) |
| CoCoRaHS (Colorado Climate Center, CSU) | Producer's site | CoCoRaHS (new dataset) | — (CoCoRaHS's Part 4) | Written: `A2_Rstar_query-cocorahs.md`; the five dataset parts are in `dataset_queries/about_dataset_queries/cocorahs/` with a run sheet |
| NODD buckets, Earth Engine, dynamical.org, IRI, Data Rescue Project, NCAR GDEX, Copernicus CDS, Iowa Environmental Mesonet (IEM) | Copies | various (IEM: ASOS) | — | — (checked in the datasets' gap runs, or for ASOS and USCRN Daily in their Part 1) |

ASOS and USCRN Daily (queries written 2026-11-25, in `dataset_queries/about_dataset_queries/asos/` and `uscrn-daily/`,
each with a run sheet) need only their five dataset parts, since NCEI's A1 and A2 runs are done. If ASOS's Part 1
finds that IEM, NWS or FAA keeps a full archive of its own, or USCRN's finds that ATDD serves a full copy, that host
would need an A2 run.

GDEX and the Copernicus CDS are run by large institutions and could become shared archives if a future dataset's
archive of record is there. For GPCP they only hold copies.

## CoCoRaHS, worked through

You chose to research CoCoRaHS as a dataset and its archive. CoCoRaHS (Community Collaborative Rain, Hail and Snow
Network) is a producer's own data site, so it gets **the five dataset parts plus one A2 run: six sessions.**

**What is known already** (from the CoCoRaHS site, read 2026-11-23, and the GHCN-Daily and rain-gauge runs):
- **Who runs it:** it started at the Colorado Climate Center at Colorado State University in 1998; every page carries
  the Colorado Climate Center's copyright. NOAA and NSF are named as major sponsors, with a longer sponsor list
  (cocorahs.org About and Sponsors pages).
- **The data site:** daily precipitation, snow, hail, condition monitoring, soil moisture and evapotranspiration
  reports, a Station Data Explorer (dex.cocorahs.org) and Water Year Summaries (wys.cocorahs.org). The pages don't
  mention download formats, an API, a DOI or a data version. Data are free under CC BY 4.0, "as is" (cocorahs.org
  ViewData and data use policy pages).
- **A second copy exists at NCEI:** CoCoRaHS stations make up about 40% of GHCN-Daily's entries
  (`2026-11-21_ghcn-daily-sources-pt5`). That is RRS-1 evidence for CoCoRaHS, and NCEI's A2 run applies to that copy.
- **Funding:** the last NOAA awards naming CoCoRaHS on USAspending were $1.17M (2006–10) and $1.25M (2010–15); the
  current route was not found, and no threat was found (`2026-11-18_noaa-rain-gauge-threats`).

**What the five parts should ask, beyond the templates:**
- **Part 1:** each product line and its access routes; whether any bulk download, API or web service exists; where
  the data flow (NWS, GHCN-Daily, state climatologists, the Drought Monitor); the observers' numbers, as inputs.
- **Part 2:** CoCoRaHS's QC of volunteer reports (who reviews them, and how); the gauge standard as its "calibration"
  (DIRS-1): who sets it and whether there is one approved gauge; the code behind the site and its QC.
- **Part 3:** the Colorado Climate Center and CoCoRaHS staff (state climatologist, national coordinator, developers),
  using university rules, not FERS.
- **Part 4:** NOAA, NWS and NSF sponsorship from 2025 on; CSU's support; the Colorado Climate Center's own funding;
  and the data site's outages. The rain-gauge run is a starting point, not a substitute.
- **Part 5:** the volunteers themselves (recruitment and retention trends), the gauge supply (whether only one
  supplier makes the approved gauge, which is DIRS-5), and the site's hosting provider if CSU doesn't host it.
- **A2 (CoCoRaHS data site):** who builds and runs cocorahs.org and its subdomains, where it is hosted and backed up,
  checksums and disaster recovery (likely unpublished), and its outage history from the Wayback Machine. Point it at
  NCEI's GHCN-Daily copy for RRS-1.

## Should repository questions move into the dataset parts? No

| Reason | Evidence |
|---|---|
| The dataset parts are already full | Standard dataset runs used 141,000–197,000 tokens against a research stop of 195,000. Adding the five RRS questions would push them to the deep tier's size or squeeze out dataset questions |
| Dataset runs never got to them | None of the four datasets' first 24 runs asked about checksums or disaster recovery. GHCN-Daily's pt7 asked about storage and found NCEI-wide facts, which apply to every NCEI dataset |
| Shared archives would be searched again and again | NCEI holds 3 of the 4 datasets, and a copy of the fifth (CoCoRaHS). GES DISC holds 2. Separate runs save 3 sessions now, and more with each new NCEI or GES DISC dataset |
| Producer sites lose nothing by being separate | The A2 run is the one extra session a producer site needs either way. Folding it into Part 1 or 2 would overfill those runs |

**What changes in the dataset templates:** Part 1 now sorts each host into one of the three kinds, and Part 4 asks
about a producer site's funding and outages. Both lines are added to the templates.

## Session count

| | Sessions |
|---|---|
| New dataset hosted by an archive that already has A1 and A2 | 5 |
| New dataset with its own data site (like CoCoRaHS) | 5 + 1 (A2) = 6 |
| New dataset whose archive of record is a new shared archive | 5 + 2 (A1, A2) = 7, and later datasets in that archive need only 5 |
