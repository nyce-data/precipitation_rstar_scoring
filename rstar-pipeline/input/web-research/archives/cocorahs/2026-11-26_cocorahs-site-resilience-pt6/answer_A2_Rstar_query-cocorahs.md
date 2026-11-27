# How resilient is the CoCoRaHS data site as a home for the network's data?

**Direct answer:** The CoCoRaHS site is a working but thinly protected home. Since a move scheduled for 7 August 2020, everything runs in one commercial cloud, Microsoft Azure, with one Azure SQL primary database. It is built and run by essentially one CSU developer, and the money has always been short-term. Nothing published describes its backups, integrity checks or a disaster recovery plan. The best protection outside CoCoRaHS is NCEI's GHCN-Daily copy, but that copy holds only daily precipitation and snow. **Overall confidence: moderate.** Hosting and staffing rest on CoCoRaHS's own slides and its live server responses. The absences rest on searches that found nothing.

## The statements, one by one

| Statement (as worded) | Verdict | Main evidence |
|---|---|---|
| RRS-1 two or more geographically independent sites hold verified copies | **Partly supports, for daily precipitation and snow only** | NCEI copy since July 2010; no other report type shown outside CoCoRaHS; no reconciliation published |
| RRS-2 checksum checks quarterly or more often | **No evidence (nothing published)** | No fixity or integrity checks described anywhere |
| RRS-3 DR plan tested in the past 2 years with documented results | **Contradicts, on public evidence** | No CoCoRaHS plan published; CSU had no formal DR policy in FY2023 |
| RRS-5 survived a major disruption without data loss | **Partly supports** | Stored archive survived outages in 2011, 2013 and 2020; in 2011 about 500 daily reports were never entered |
| D-2 storage at end of life or a single point of failure | **Supports (single point of failure)** | One cloud provider, one primary database; earlier, one host's data centre |
| D-3 access infrastructure fragile or unfunded | **Supports** | One developer; volunteer-built apps abandoned; features cut for budget |

## Who runs it (D-3: supports; high confidence)

- **One developer.** CSU's Atmospheric Science staff list names Julian Turner as "Web developer and database administrator for the CoCoRaHS ... Network" ([CSU ATS, staff list](https://www.atmos.colostate.edu/people/research/)).
- He was already "Julian, our Web developer" in an April 2011 newsletter ([CoCoRaHS, The Catch, 22 Apr 2011](https://media.cocorahs.org/docs/TheCatch_2010-04-22.pdf)).
- His 2021 IT update put CoCoRaHS's capacity at "One developer => 50 Work weeks a year", with about 25% of that taken by operations ([Turner, WERA 2021](https://media.cocorahs.org/docs/Turner-WERA21.pdf)).
- **Outside help is limited by money.** An outside vendor, Solliance, did the Azure migration and then helped with monitoring at $150 an hour. CSU caps any one vendor at $150K, and Turner added "not that we have the budget for it" (same deck).
- **Parts of the system lean on volunteers or are fragile.** The original mobile apps were "created by an observer years ago", and he no longer wanted to maintain them. The QC ticketing system runs on its own MySQL database and is "fragile". The data export "is having a harder time keeping up", and the maps slow down at peak use ([Turner, WERA 2024](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf); [CoCoRaHS app page](https://www.cocorahs.org/Content.aspx?page=app-install)).
- No source gives a staff count or names a second developer. The other CoCoRaHS staff on CSU's list are the project manager (Steve Hilberg, QA/QC) and Henry Reges, who supports coordinators and "network operations". Neither is described as an IT role ([CSU ATS, staff list](https://www.atmos.colostate.edu/people/research/)).
- **How it was paid for (before 2025):**
  - A 2003 NSF grant hired the first "Web developer" ([CoCoRaHS, 25 years](https://www.cocorahs.org/Content.aspx?page=25years)).
  - NSF and NOAA support for "staff, coordination and web development costs" was "coming to an end this next year" in December 2013 ([The Catch, 22 Dec 2013](https://media.cocorahs.org/docs/TheCatch_2013-12-22.pdf)).
  - Microsoft's AI for Earth grant was extended "to include operational hosting expenses" in 2020 ([Turner, WERA 2020](https://media.cocorahs.org/docs/JulianWERA20.pdf); [The Catch, 28 Jul 2020](https://mailchi.mp/cocorahs/newsletter_the-catch_july_2020)).
  - By 2024 the watershed maps had been turned off "for budget reasons" ([WERA 2024](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf)).
  - Who pays for hosting now is not published. Funding from 2025 on is in Part 4.

## Storage and copies (D-2: supports; RRS-1: partly supports)

**Hosting (high confidence).**
- The July 2020 Catch scheduled a move of "all of CoCoRaHS to the Microsoft Azure cloud" for 7 August 2020. It said the last major upgrade had been "over five years" before ([The Catch, 28 Jul 2020](https://mailchi.mp/cocorahs/newsletter_the-catch_july_2020)).
- By 2021 "All CoCoRaHS Cyberinfrastructure is running in Azure". The architecture slide labels an "Azure SQL Database" as the "Primary CoCoRaHS DB", with media and bulk files in Blob Storage ([WERA 2021](https://media.cocorahs.org/docs/Turner-WERA21.pdf)).
- On 26 November 2026, www, data, dex, wys and media.cocorahs.org all answered through Azure Front Door (`x-azure-ref` header). www and data also set Azure App Service `ARRAffinity` cookies (headers saved in this run; [www.cocorahs.org](https://www.cocorahs.org/), [data.cocorahs.org](https://data.cocorahs.org/)).
- Before Azure, a commercial host ran the site and database: in 2013 CoCoRaHS wrote of "the company that hosts our website and database" ([The Catch, 9 Apr 2013](https://media.cocorahs.org/docs/TheCatch_2013-04-09.pdf)).
- The site has never been on CSU servers, as far as the sources show. So CSU's own backup services are not evidence for it: ETS backs up college file servers nightly to tape ([CSU Engineering ETS](https://www.engr.colostate.edu/ets/policies/)), and Campus Cloud gives Tier 1 virtual machines 14-day backups ([CSU Campus Cloud](https://campuscloud.colostate.edu/explanation.aspx)).

**Backups.** The 2021 architecture slide lists Key Vault, a Web Application Firewall, SSL certificates and Azure DevOps, Repos and Pipelines, but no backup component ([WERA 2021](https://media.cocorahs.org/docs/Turner-WERA21.pdf)). Not published: the Azure region, geo-redundancy, retention and restore testing. Azure SQL keeps automatic backups by default, but that is the vendor's default, not evidence of CoCoRaHS's settings. The vendor page couldn't be read (the sandbox refused learn.microsoft.com).

**Copies outside CoCoRaHS.**
- **NCEI, GHCN-Daily (moderate confidence).** CoCoRaHS was added to GHCN-Daily "Effective 12 July 2010", with source flag "N". Multiday precipitation followed in version 3.27, released 16 May 2019 ([NCEI, GHCN-Daily status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)).
  - CoCoRaHS's 2019 QA/QC document says all data since 1998 are "continually streamed to NCDC" and "retrieved by GHCN-Daily on a daily basis" ([CoCoRaHS QA/QC, Apr 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf)).
  - GHCN-Daily includes only CoCoRaHS stations with "at least 100 individual data values" for at least one element (same document). A short-lived station's reports exist only at CoCoRaHS.
  - NCEI's pages name only precipitation, snowfall, snow depth and snow water equivalent elements. NCEI's own data centre is a separate site run by a separate body. That is the one independent copy, and it covers only these elements.
- **NWS.** Significant-weather reports go to NWS offices in real time under the AWIPS header DENCCRAHS ([WERA 2024 SigWx](https://media.cocorahs.org/docs/WERA_2024_6_SigWx_Gimmestad.pdf)).
- **MADIS.** NOAA's MADIS carries a CoCoRaHS feed for nine states only ([MADIS hydro](https://madis.ncep.noaa.gov/madis_hydro.shtml)).
- **No copy found outside CoCoRaHS** for hail, condition monitoring or ET reports, or for observer and station records.
- **Checking the copies against each other.**
  - NCEI compares CoCoRaHS with NWS COOP submissions: 345 GHCN-Daily stations were affected in 2022 ([NCEI, WERA 2022](https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf)).
  - NCEI also publishes the values that fail its QC checks ([NCEI nws/readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/nws/readme.txt)).
  - No source describes a check of NCEI's copy against the CoCoRaHS database. So the NCEI copy is independent, but no source says it has been checked against the original.

## Integrity and recovery (RRS-2: no evidence; RRS-3: contradicts on public evidence)

- **CoCoRaHS publishes nothing on its own safeguards** (moderate confidence that none is published). Searches of CoCoRaHS, CSU, NCEI and Wayback pages found no checksums, fixity checks, database-integrity checks, a DR or continuity plan, or a test.
  - The 2024 IT deck lists "Review Database Data Versioning" only as a possible future project ([WERA 2024](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf)).
  - For a university-run site whose own slides go into architecture detail, saying nothing about backups is itself a weak sign.
- **CSU's policy context.** Colorado's state auditor found in FY2023 that "CSU IT had not established a formalized IT policy for the development, documentation, and dissemination of disaster planning" ([State Auditor, CSU System FY2023](https://content.leg.colorado.gov/sites/default/files/documents/audits/2316f-a_colorado_state_university_system_fy23.pdf)).
  - The finding was Partially Implemented in FY2024 ([FY2024](https://content.leg.colorado.gov/sites/default/files/documents/audits/2416f-a_colorado_state_university_system_fy_24_23-accessible.pdf)) and Implemented in FY2025 ([FY2025](https://content.leg.colorado.gov/sites/default/files/documents/audits/2516f-a-colorado-state-university-system-fy25-accessible.pdf)).
  - These audits covered Kuali, Oracle and Banner, not the Colorado Climate Center's Azure systems.

## Track record (RRS-5: partly supports; moderate confidence)

| Date | What happened | Cause | Data lost? | Source |
|---|---|---|---|---|
| 7 Apr 2011 | "Service Unavailable"; no viewing or entry | The web host's firewall took site-to-database traffic for an attack | Stored data no; about 500 daily reports never entered after back-filling | [Catch 22 Apr 2011](https://media.cocorahs.org/docs/TheCatch_2010-04-22.pdf) |
| 9 Apr 2013 | Site down for at least 3 hours in the morning | "intermittent power issue" at the host's data centre | Not stated; "over 1200 e-mails" came in, and observers were asked to type their reports in themselves | [Catch 9 Apr 2013](https://media.cocorahs.org/docs/TheCatch_2013-04-09.pdf) |
| Late 2013 | "painfully slow" for weeks | Unknown ("not the database ... not the web server") | Not stated | [Catch 22 Dec 2013](https://media.cocorahs.org/docs/TheCatch_2013-12-22.pdf) |
| Oct 2013 shutdown | Site up (Wayback, 6 Oct 2013) | n/a | Not found | [Wayback 2013](https://web.archive.org/web/20131006064617/http://www.cocorahs.org:80/) |
| Jan 2019 shutdown | Site up; 8,615 daily reports for 5 Jan 2019 | n/a | Not found | [Wayback 2019](https://web.archive.org/web/20190106011850/https://www.cocorahs.org/) |
| 7 Aug 2020 | Planned migration to Azure, "a few hours of downtime" | Planned | Not found | [Catch 28 Jul 2020](https://mailchi.mp/cocorahs/newsletter_the-catch_july_2020) |
| Before 1 Dec 2020 | NCEI's daily CoCoRaHS updates interrupted | "an issue with the provider" | Not stated | [NCEI status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt) |

- **NCEI's copy during shutdowns.** NCEI announced on 1 October 2013 and 22 January 2018 that GHCN-Daily "will continue to update automatically" during the shutdowns, but would not be monitored. NCEI's side has had its own pauses: hardware from 17 November 2019, ftp on 10–13 October 2020, a failed update on 6 January 2021, maintenance on 30–31 January 2021 and hardware again in April 2021 ([NCEI status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)). None was reported as losing CoCoRaHS data.
- **The NOAA award endings.**
  - The Catch said in December 2013 that NSF and NOAA support was ending. The site kept running through 2014–15 (Part 3 covers the awards), but no source describes how it fared.
  - No outage or loss is reported for the 2010 award transition.
- **After 2020.** No outage was found from 2021 to 2026, but CoCoRaHS publishes no status log, so this is an absence of reports, not proof of uptime.

## What this means

- **The weak points are concentrated:** one developer, one cloud provider and one primary database, with no published backup or DR practice. That fits D-2 and D-3 and leaves RRS-2 and RRS-3 unmet as far as anyone can verify.
- **The NCEI copy guards the core daily precipitation and snow record.** It is the main reason a failure at CoCoRaHS would not wipe out the network's most-used data.
- **Not guarded:** the other report types, the observer and station metadata, and reports not yet pulled by NCEI.

## Gaps

- **Azure backup set-up** (region, geo-redundant backup storage, retention, restore tests): not published. The Colorado Climate Center holds it. Asking Julian Turner or info@cocorahs.org is the only route found.
- **NCEI transfer route and protocol:** not documented. The 2022 NCEI data-flow diagram is only an image (slide 35 of [WERA 2022](https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf)).
- **Whether NCEI or anyone else holds hail, condition monitoring or ET reports:** not stated. NCEI could confirm on request.
- **No 2025 or 2026 CoCoRaHS IT update found** (the committee became WCC 1012 in 2025).
- **Outages after 2020:** none found; there is no public log.
- **Unread:** one forum thread (wxforum.net) behind a bot check, with no Wayback copy. It is listed in `check-by-hand.md`.
- **Sandbox:** one host was refused (learn.microsoft.com). It is listed in `sites-to-trust.md`; you can check whether to add it to the sandbox's allowed domains.
- Part 2's and Part 4's answers are not contradicted by this run. The `query_answers` copies of Parts 1–5 are unaffected.

## Sources

- **CoCoRaHS**
  - [Turner, WERA 1012 2020 CoCoRaHS IT Update](https://media.cocorahs.org/docs/JulianWERA20.pdf)
  - [Turner, WERA 1012 2021 CoCoRaHS IT Update](https://media.cocorahs.org/docs/Turner-WERA21.pdf)
  - [Turner, WERA 1012 2024 CoCoRaHS IT Update](https://media.cocorahs.org/docs/WERA_2024_10_IT_Update_Turner.pdf)
  - [The Catch, 22 Apr 2011](https://media.cocorahs.org/docs/TheCatch_2010-04-22.pdf)
  - [The Catch, 9 Apr 2013](https://media.cocorahs.org/docs/TheCatch_2013-04-09.pdf)
  - [The Catch, 22 Dec 2013](https://media.cocorahs.org/docs/TheCatch_2013-12-22.pdf)
  - [The Catch, 28 Jul 2020](https://mailchi.mp/cocorahs/newsletter_the-catch_july_2020)
  - [CoCoRaHS QA/QC, April 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf)
  - [CoCoRaHS, 25 years](https://www.cocorahs.org/Content.aspx?page=25years)
  - [CoCoRaHS, app install page](https://www.cocorahs.org/Content.aspx?page=app-install)
  - [Gimmestad, WERA 2024 SigWx](https://media.cocorahs.org/docs/WERA_2024_6_SigWx_Gimmestad.pdf)
  - Response headers, 26 Nov 2026: [www.cocorahs.org](https://www.cocorahs.org/), [data.cocorahs.org](https://data.cocorahs.org/), [dex.cocorahs.org](https://dex.cocorahs.org/), [wys.cocorahs.org](https://wys.cocorahs.org/), [media.cocorahs.org](https://media.cocorahs.org/)
  - Wayback captures: [cocorahs.org, 6 Oct 2013](https://web.archive.org/web/20131006064617/http://www.cocorahs.org:80/), [cocorahs.org, 6 Jan 2019](https://web.archive.org/web/20190106011850/https://www.cocorahs.org/)
- **CSU and Colorado**
  - [CSU Atmospheric Science, research staff](https://www.atmos.colostate.edu/people/research/)
  - [CSU Engineering ETS policies](https://www.engr.colostate.edu/ets/policies/)
  - [CSU Campus Cloud](https://campuscloud.colostate.edu/explanation.aspx)
  - Colorado Office of the State Auditor, CSU System audits: [FY2023](https://content.leg.colorado.gov/sites/default/files/documents/audits/2316f-a_colorado_state_university_system_fy23.pdf), [FY2024](https://content.leg.colorado.gov/sites/default/files/documents/audits/2416f-a_colorado_state_university_system_fy_24_23-accessible.pdf), [FY2025](https://content.leg.colorado.gov/sites/default/files/documents/audits/2516f-a-colorado-state-university-system-fy25-accessible.pdf)
- **NOAA**
  - [NCEI, GHCN-Daily status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)
  - [NCEI, GHCN-Daily nws/readme.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/nws/readme.txt)
  - [NCEI, WERA 1012 2022 slides](https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf)
  - [MADIS Hydrological Surface Dataset](https://madis.ncep.noaa.gov/madis_hydro.shtml)

Saved in [`web_search_results/2026-11-26_cocorahs-site-resilience-pt6/`](web_search_results/2026-11-26_cocorahs-site-resilience-pt6/answer.md): this answer, `method.md`, `research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
