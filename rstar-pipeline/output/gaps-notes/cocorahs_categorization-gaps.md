# CoCoRaHS: what the research didn't search, by subcategory

- **Dataset:** CoCoRaHS (Community Collaborative Rain, Hail and Snow Network) daily precipitation reports, 1998 to
  present, from about 28,000 volunteers reading a manual 4-inch gauge. No DOI or version. Run by CoCoRaHS headquarters
  at the Colorado Climate Center, Colorado State University (CSU).
- **Categorized:** 2026-11-27, first pass.
- **Output:** [cocorahs_rstar-categories.json](../categories/cocorahs/cocorahs_rstar-categories.json), built by
  `rstar-pipeline/processing/scripts/categorize/build_cocorahs.py` (112 evidence items).
- **Research used:**
  - `about-datasets/cocorahs/`: about-pt1 (hosts, inputs, organizations), qc-formats-pt2 (QC, calibration, software,
    FAIR), people-funding-pt3 (staff, ages, funding before 2025), threats-news-pt4 (January 2025 – November 2026) and
    inputs-pt5 (observers, gauge makers, apps, NWS recruiters, substitutes);
  - `archives/cocorahs/2026-11-26_cocorahs-site-resilience-pt6` (the A2 run on CoCoRaHS's own data site);
  - `archives/noaa-ncei/`: the A1 threats run and the A2 resilience run, for NCEI's copy of the reports in GHCN-Daily;
  - `instruments/noaa-rain-gauges` (its CoCoRaHS row, and COOP as a substitute).
- **Not used:** both satellite runs (CoCoRaHS uses no satellite data). GHCN-Daily's own runs name CoCoRaHS only as a
  GHCN-Daily source (40% of entries, normal station turnover, no threat found); CoCoRaHS's own runs cover the same
  ground, so nothing was borrowed.
- **Coverage note:** none was written for CoCoRaHS (its queries were planned from the templates, not from a gaps note).

## Repositories (the JSON's `dataset` key)

| Repository | Role | Holds |
|---|---|---|
| CoCoRaHS database and data site | parent | The archive of record: one Azure SQL database, served through cocorahs.org ViewData, the data.cocorahs.org Export Manager (CSV, XML, SHEF), the Data Explorer and maps |
| NOAA NCEI (GHCN-Daily) | child | Daily precipitation, snowfall, snow depth and snow water equivalent since 12 July 2010 (source flag N), for stations with at least 100 values; Asheville, moving to AWS |

`producer_is_repository` is **true**: CoCoRaHS headquarters both makes the reports and holds the archive of record.

Not repositories: MADIS (nine states), the Iowa Environmental Mesonet, ACIS and the state climatologists using it
(copies of the GHCN-Daily copy), NWS offices (working copies), and GHCN-Daily's own cloud mirrors (AWS, Google), which
hold the GHCN-Daily format, not CoCoRaHS's.

## Scores

| Code | For | Against | Context | Score | Why |
|---|---|---|---|---|---|
| P-1 | 4 | 0 | 3 | **35** | No written plan found; documentation is for observers only; IT docs are future projects; no successor named for Doesken |
| P-2 | 1 | 1 | 3 | **NA** | Only age estimates (low): Hilberg likely past every threshold, the others unlikely |
| P-3 | 3 | 0 | 2 | **25** | No production code published; no written manual-QC criteria; IT docs not written |
| P-4 | 4 | 0 | 3 | **15** | One developer; one person does most QC; no backup named for Reges |
| D-1 | 2 | 3 | 4 | **NA** | NCEI's pending FY2027 cut (for) against record donations and no cut found for CoCoRaHS (against) |
| D-2 | 4 | 1 | 2 | **NA** | One cloud, one primary database, no published backup (for) against NCEI's copy of the core series (against) |
| D-3 | 5 | 0 | 3 | **20** | One developer; fragile parts; soft money; cost cutting; NCEI-copy outages |
| D-4 | 0 | 2 | 2 | **0** | CSV, XML, SHEF and GHCN-Daily's documented format are open |
| D-5 | 0 | 2 | 2 | **0** | No political pressure found; not on NOAA's retirement list |
| DIRS-1 | 1 | 2 | 2 | **0** | CoCoRaHS sets its own gauge standard; no outside calibration service (the "for" is low) |
| DIRS-2 | 2 | 1 | 4 | **NA** | Observers flat (against) vs NWS staff losses and coordinator gaps (for) |
| DIRS-3 | 0 | 2 | 1 | **0** | No outside data feed; apps replaced in-house |
| DIRS-4 | 2 | 0 | 3 | **15** | Azure and Carto vendor platforms; an outside vendor helps run them |
| DIRS-5 | 2 | 2 | 3 | **NA** | No Azure fallback and no dense substitute (for) vs gauge suppliers and the web entry route (against) |
| RRS-1 | 1 | 2 | 3 | **NA** | Two holders in separate places (for), but NCEI's copy is partial and never checked against the original (against) |
| RRS-2 | 0 | 2 | 1 | **0** | No integrity checks published at CoCoRaHS; NCEI checks only on ingest and retrieval |
| RRS-3 | 0 | 1 | 2 | **0** | No CoCoRaHS DR plan or test found |
| RRS-4 | 3 | 5 | 1 | **NA** | Record donations vs year-to-year money and NCEI's pending cut |
| RRS-5 | 4 | 1 | 3 | **NA** | Came through the 2015–17 grant endings and Azure move (for); NCEI's 8% Helene backlog (against) |

Category totals: P NA, D NA, DIRS NA, RRS NA, so **R* is NA** (8 of 19 subcategories NA).

## Judgment calls to double-check

- **"Or" statements (P-4, D-3).** Each statement lists alternatives ("production, QC, or distribution"; "grant-funded,
  maintained by a single developer, or at risk of going dark"). Where one alternative is shown true (one developer),
  evidence that another is false is filed as context, not "against":
  - P-4: the founder's 2017 handover (the run called it "contradicts P-4 for the founder") and "headquarters staff and
    a number of our volunteer coordinators review the data each day" are context, so P-4 = 15;
  - D-3: no outages and "99+ percent uptime" (the run rated D-3 contradicted) are context, so D-3 = 20.

  If you'd rather count them as "against", both go NA.
- **P-2 is NA, though Hilberg is the most likely retirement case found so far.** His B.S. is from 1974, he has already
  retired once (as Midwestern Regional Climate Center director) and he leads day-to-day QC. The rules make every age
  estimate low confidence, so this low "for" doesn't set the score. A person may well choose 25 here.
- **P-1: Doesken's death** (15 November 2026, no successor named) is a moderate "for". He was emeritus, not paid staff,
  so you could file it as context; P-1 stays 35 either way.
- **D-1: NCEI's FY2027 request** counts because NCEI hosts a copy (D-1 covers "the program that hosts and serves it").
  Without it D-1 would be 0 (against only: record donations, no cut found). The NSF IDEAL termination (April 2025) is
  context: it funded education research with CoCoRaHS as a partner, not the network.
- **D-2: NCEI's copy is a moderate "against"** (the core daily series would stay online if CoCoRaHS went down), which
  makes D-2 NA. The run itself said D-2 is supported "for the full dataset". If the partial copy shouldn't count, D-2 =
  25.
- **DIRS-2: NWS staff losses count** (moderate "for"), because NWS offices recruit observers and NWS staff are state
  coordinators in some states, though no effect on CoCoRaHS was shown. Coordinator gaps (New York 26 of 62 counties)
  are a moderate "for". The volunteers themselves are the observing network, so flat station counts are a high
  "against".
- **DIRS-5:** "no fallback host published" for Azure is a moderate "for" (as no-substitute is "for"); the gauge's
  single cheap maker is context, since approved alternatives exist.
- **RRS-1:** NCEI's copy being partial is an "against", like the "copies not current" precedent for GPCP; the two
  holders in separate places are a moderate "for", as for IMERG's PPS and GES DISC.
- **RRS-2 and RRS-3:** "nothing published" after targeted searches is a moderate "against", following the NASA GES DISC
  precedent (a not-found DR plan is "against").
- **RRS-5:** surviving the 2015–17 grant endings and the 2017 leadership change, with no loss reported, is a moderate
  "for"; the 2011 outage (about 500 reports never entered) is context, since it was an IT outage, not a funding or
  leadership disruption.
- **Repository roles:** NCEI's GHCN-Daily is filed as a child repository even though it reformats the reports into
  GHCN-Daily's own format. It is the archive the reports are "continually streamed" to, so it was kept as the one
  independent copy; MADIS, IEM and ACIS were not.
- **Open rules this dataset hits:** whether one station closing counts as a lost source (CoCoRaHS loses about 3,000
  observers a year, filed as context); repeating NCEI-wide facts (NCEI's budget and staff appear in D-1 and RRS-4).

## What the research never searched, or couldn't find, by subcategory

### People risk
- **P-1:** a written succession plan (searched, none found); who takes on Doesken's emeritus work. *Ask:*
  info@cocorahs.org.
- **P-2:** real ages, service dates and retirement plans (CSU personnel records); Talmadge's and Stolz's dates.
- **P-3:** internal runbooks and code repositories; written manual-QC criteria.
- **P-4:** FTEs and cover arrangements; who besides the developer can administer the Azure systems.

### Data risk
- **D-1:** whether CoCoRaHS is paid under the 2026–2031 NMP contract (KBR's subcontract lists; a USAspending subaward
  search for KBR or Synoptic to CSU); CSU's unit-level FY2027 cuts; the final FY2027 NCEI and NMP appropriations.
- **D-2:** the Azure region, backup settings and who holds the subscription; whether anyone holds the hail,
  condition-monitoring and ET reports outside CoCoRaHS.
- **D-3:** who pays for hosting now; short outages after 2020 (no public log); the 2026 Catch issues (PDFs, not read).
- **D-4:** column and flag documentation for the Export Manager; re3data registration (lookup refused by the sandbox).

### Dependent infrastructure resilience
- **DIRS-1:** a written NWS gauge specification; any paired comparison of CoCoRaHS with NWS gauges.
- **DIRS-2:** the 2025 count of stations whose last report was in 2025 (due in a 2027 deck); observer counts by state.
- **DIRS-4:** who holds the Azure subscription.
- **DIRS-5:** Stage IV as a substitute (its gauge inputs were not read); whether Darter took over the Stratus molds.

### Repository resilience
- **RRS-1:** CoCoRaHS's Azure region and backups; NCEI's AWS regions after the move; the NCEI transfer route (only an
  image in NCEI's 2022 slides).
- **RRS-2:** any CoCoRaHS integrity check; NCEI's SOP 60-6-015 (not public).
- **RRS-3:** any CoCoRaHS DR plan or test; NCEI's contingency-plan test results.
- **RRS-4:** who pays for hosting and the NMP amount; NCEI's FY2026 spend plan.
- **RRS-5:** how the sites fared through the 2014–15 award endings; outages after 2020.

Most of these are held by CoCoRaHS headquarters (info@cocorahs.org) or its developer, not published: an inquiry would
settle more than another web search.

## Conflicts between runs

- **Sponsors page vs award records:** the page lists NOAA "2006–present" and NSF "2010 – present", but USAspending and
  NSF show the grants ended in 2015 and 2017 (pt3, pt4). The award records are used; the page is likely stale since a
  December 2014 snapshot.
- **QC ticket system:** "integrated" after the Azure move (2021 minutes), "completely isolated" on its own MySQL stack
  (2024 IT slides), and "moved to CoCoRaHS web site as of 10/1/2024" (2026 slides). pt2 reads it as on CoCoRaHS's own
  servers by 2021 and part of the web site from October 2024.
- **Gauge standard:** GHCN-Daily's infrastructure run (pt8) found "no formal CoCoRaHS gauge standard"; CoCoRaHS pt2
  found the Approved Rain Gauges page. pt2 is used.
- **Doesken's date of death:** 15 November 2026 (CoCoRaHS, MPR News) or "Saturday" (BizWest). CoCoRaHS's own notice is
  used.

## Things to check by hand (no new web search)

- CoCoRaHS's approved-gauge page still names Productive Alternatives as the Stratus maker; worth telling HQ.
- The metadata file's `review_notes` (Doesken's death, Schumacher as a current lead).
- The pages listed in each run's `check-by-hand.md` (2014 NSF PI slides on the Web API, re3data, the Google Play
  listing, the IDEAL project's termination page, the wxforum.net thread).

## Evidence counts

112 items: P 24, D 32, DIRS 27, RRS 29. By stance: 38 for, 27 against, 47 context.
