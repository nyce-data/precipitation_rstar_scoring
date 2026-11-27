# ASOS Part 3: the people, teams and funding behind ASOS and its archived precipitation data

**Direct answer.** ASOS is run by a small NWS Office of Observations program office. Its 2024 documents name Kenneth Boutin as National Program Manager, Thomas Day as System Owner (the office of primary responsibility on the maintenance directive), Jonathan Adams as AOMC Chief, Joseph Devost as Maintenance Manager and Carl Diaz as Chief Engineer. NCEI's archived products name only one person: Matthew Menne, the sole principal investigator of GHCNh. The 1-minute, 5-minute and LCD records name only agencies and NCEI's Customer Engagement Branch. The only published team size is the field workforce: "a workforce equivalent of 63 ETs". The money comes through parent budget lines and a reimbursable tri-agency agreement, and ASOS's own share is never published.

For the risks:
- **P-4 (a single person is a point of failure):** partly supported.
- **P-2 (key people retirement-eligible within 2 years):** supported for Menne only, as an estimate.
- **P-1 (no documented succession plan):** supported for ASOS roles. NWS does have an agency-level human capital plan (2020).
- **D-1 (funding baseline):** partly supported. FAA's share is shrinking as it moves 206 of its ASOS to AWOS-C.

Overall confidence: moderate for the names and funding structure; low for whether people are still in post and for the age estimates.

## People

| Person | Role (source date) | Employer | Still active? | ORCID / earliest publication | Age and retirement (estimates) |
|---|---|---|---|---|---|
| Kenneth Boutin | ASOS National Program Manager ([governance draft, Aug–Sep 2024](https://weather.gov/media/asos/ASOS%20Issue%20Report%20-%20Governance%20v6.pdf); [PNS 24-48, Jul 2024](https://www.weather.gov/media/notification/pdf_2023_24/pns24-48_re-commence_ote_asos_temp_dew_sensor_replacement.pdf); Program Management Branch, Surface and Upper Air Division ([FPAW talk, May 2023](https://fpaw.aero/sites/default/files/163/2-boutin-decadal-look-asos-lifecycle-upgrades.pdf), read via Wayback)) | NWS (federal) | Uncertain. HigherGov last saw him in a solicitation in Sept 2025. A LinkedIn snippet reads "Six years as the National ASOS Program Manager". An undated LinkedIn snippet names Christine Smith (Schultz) as "ASOS Program Manager at NOAA National Weather Service" ([search snippets](https://html.duckduckgo.com/html/?q=%22Kenneth+Boutin%22+ASOS)) | none found | Not estimable (no dates; a veteran, per the snippet, so military service may count) |
| Thomas Day ("T. Day") | ASOS System Owner; OPR W/OBS32 on [NWSI 30-2111 (1 Jan 2025)](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf) | NWS | In post at Jan 2025 | none (the one ORCID by that name is someone else) | Not estimable |
| M. Hopkins | Certifier, W/OBS3 (division level) on the same directive | NWS | Jan 2025 | none | Not estimable |
| Jonathan Adams | AOMC Chief (governance draft, 2024) | NWS | Uncertain. The AOMC Section Chief post was [advertised 6–19 Nov 2026](https://www.usajobs.gov/job/891863400) (GS-14, permanent, College Park, now under the Office of Systems) | none | Not estimable |
| Joseph Devost, Carl Diaz | Maintenance Manager; Chief Engineer (2024) | NWS | 2024 only | none | Not estimable |
| Eugene Nolen, Steven Thompson | AOMC system admins (2024) | NWS | 2024 only | none | Not estimable |
| Raymond Nelson | Entered all three 2024 governance revisions for the ASOS SLEP 2.0 engineering team (OBS34) | NWS | 2024 only | none | Not estimable |
| Steve Kim | "FAA AWOS PM" ([NWS ASOS FAQ](https://www.weather.gov/asos/FAQ.html), undated) | FAA | unconfirmed | none | Not estimable |
| Matthew J. Menne | Sole PI of [GHCNh v1](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01688/html) | NOAA NCEI (federal) | Yes (metadata modified Oct 2026) | [0000-0001-9725-248X](https://api.openalex.org/works?filter=author.id:A5025236587&sort=publication_year:asc&per-page=5). Earliest work 1991 (OpenAlex, no affiliation shown); first NOAA/NCDC-affiliated work 2000 | **Estimate:** about 60–65. Federal since at least 2000, so 26+ years. Likely already eligible for FERS at 60 with 20 years, or eligible within 2 years. Supports P-2 |
| Nancy W. Casey | GHCNh co-author; NCEI "Scientific Programmer/Analyst" since 2019-09-16 ([ORCID](https://pub.orcid.org/v3.0/0009-0001-7709-889X/employments)) | Riverside Technology (contractor) | Yes (no end date) | 0009-0001-7709-889X; earliest work 2002 (ORCID) | **Estimate:** about 49–54. Contractor, so no federal rule applies |
| Shelley McNeill | GHCNh co-author | Riverside Technology (contractor, per the earlier GHCN-D people run) | Yes | [0000-0001-8000-6813](https://pub.orcid.org/v3.0/0000-0001-8000-6813/works); earliest work 2011 (ORCID) | **Estimate:** about 40–45. Contractor, so no federal rule applies |
| Kantor, Orcutt, Cunningham, Risavi | GHCNh co-authors (NCEI) | not found | 2023 | Kantor: 3 OpenAlex works (2024 shown). Orcutt's profile is merged with another person. None for the other two | Not estimable |

Sources by column: roles and dates as linked in each row. Ages are the earliest publication year minus 25–30, worked out against 2026.

- **Station software:** the 2017 [AMS paper on ASOS modernization](https://ams.confex.com/ams/97Annual/webprogram/Manuscript/Paper315698/AMS%20Modernization%20of%20ASOS%20Hardware%20and%20Software%20Paper_FINAL.pdf) was written mainly by CyberData Technologies contractor staff (Hays, Brewer), with NWS Office of Observations staff (Dover, Szynborski). No current single owner of the ACU/DCP software or the precipitation algorithm was found.
- **Not found:** the head of the Sterling Field Support Center (its pages give only a phone line and group email), and any Air Force or Navy counterpart.

## Teams

- **Field maintenance:** NWS has "integrated the ASOS maintenance workload into the general ET staff". "A workforce equivalent of 63 ETs maintains ASOS", with "a regional ASOS specialist … in each regional headquarters". The AOMC, the National Reconditioning Center (NRC), the National Logistics Support Center (NLSC) and the NWS Training Center (NWSTC) get extra resources ([NWSI 30-2111](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf)).
  - Because the work is spread across all ETs, the field side has many people who could step in. This contradicts P-4 there.
  - **High.**
- **AOMC:** it gives 24/7/365 monitoring, and its staff work shifts. No headcount is published. Its chief's post was open in November 2026 ([USAJOBS](https://www.usajobs.gov/job/891863400)).
  - Before the 2024 governance draft, the public's only channel for reporting ASOS problems was the program manager's inbox, which the draft says could "overload the inbox of the PM". That is a single-person bottleneck (supports P-4).
- **Not published:** headcounts for SFSC, FAA Tech Ops or the NCEI ASOS products.
- **Plans:**
  - GAO says NWS vacancies rose from about 5% (FY2010) to 11% (FY2016). As of January 2020, NWS "had completed its strategic human capital plan" ([GAO-17-364](https://www.gao.gov/products/gao-17-364)).
  - Commerce's OIG said in its FY2024 challenges report that NWS vacancy rates "were the same or increasing" and hiring took almost twice OPM's 80-day benchmark ([OIG FY2024 TMC](https://www.oig.doc.gov/wp-content/OIGPublications/Top_Management_Challenges_Department_of_Commerce_FY_2024_SECURED.pdf)).
  - No ASOS-specific succession or knowledge-transfer plan was found. For ASOS roles this supports P-1 (absence of evidence); the agency-level plan partly contradicts it.
  - **Moderate.**

## Funding routes (baseline, FY2024)

| Route | What is published | ASOS share |
|---|---|---|
| NWS ORF Observations | $249,962K enacted FY2024; 712 positions, 692 FTE ([NOAA FY2026 CJ](https://www.noaa.gov/organization/budget-finance-performance/budget-and-reports), Control Table-3) | not published |
| NWS PAC Systems Acquisition, Observations | $16,200K enacted FY2024 (same CJ) | not published |
| Tri-agency reimbursable agreement | The CJ says the 308 NWS, 570 FAA and 78 DoD ASOS units are run "under a reimbursable funding agreement". NWSI 30-2111 says the tri-agency parties "fund the center" (the AOMC) | The agreement's text and amounts were not found |
| FAA F&E | Capital line "ASWON – Sustainment 2" ([FAA CIP FY25–29](https://www.faa.gov/air_traffic/publications/cip/cip-overview-fy25-fy29.pdf)). It covers ASOS, AWOS-C, SWS, SAWS and DASI and will "Replace 206 ASOS with AWOS-C" ([FAA, Sept 2025](https://www.faa.gov/air_traffic/weather/aswon)) | amount not found |
| DoD | The Air Force left ASOS around 2011. The Navy funds NWS to send METARs at 5 Southern Region offices, and the Army's 6–7 sites are kept under an MOA ([Murphy, 2023](https://www.weather.gov/media/lix/gcaws/Presentation1Murphy.pdf)) | no amount found |
| NCEI (archive) | $70,000K enacted FY2024; 202 positions, 184 FTE (NOAA FY2026 CJ) | not published |
| Contracts | ASOS-SLEP: Campbell Scientific was selected in 2019 and delivered all 1,529 units by 2025; no number or value is published ([Campbell](https://www.campbellsci.com/us-asos-weather-network)). Vaisala IDV 1305M223DNWWG0082 (NWS-funded barometers) shows $3,109,939 obligated of a $9,850,000 ceiling, from 9/30/23 ([HigherGov](https://www.highergov.com/idv/1305M223DNWWG0082), an aggregator) | n/a |

Status: the FY2024 lines are enacted amounts. The table gives no parent line's total as ASOS's figure.

Which teams depend on each route:
- The NWS lines pay for the program office, the AOMC (with the tri-agency partners) and the ETs.
- FAA F&E pays for FAA-owned hardware.
- NCEI's line pays for the archive.

For D-1, the published baseline shows no defunding. However, the [NWS FAQ](https://www.weather.gov/asos/FAQ.html) says FAA's budget for the upgrade "is insufficient to recondition all 570 FAA ASOS locations". FAA's move to AWOS-C was "a budgetary decision", which supports D-1 for FAA-owned sites. **Moderate.** Changes since January 2025 (for example NCEI's FY2026 request of $52,000K) are left to the later run.

## Conflicting evidence

NOAA's CJ counts 78 DoD ASOS units, but the 2023 NWS slides say the Air Force left around 2011. The CJ probably counts Navy and Army sites only. This is unresolved; I rely on the slides for who takes part and on the CJ for the count.

Three more differences, none explained by its source:
- **Unit counts:** the CJ and the FAQ give 570 FAA and 308 NWS ASOS, while the 2023 slides say about 650 FAA and 350 NWS "of the nearly 1000 ASOS sites in the CONUS" (rounded, and CONUS only). I use the CJ.
- **AWOS-C replacements:** the FAA page and the FAQ heading say 206 ASOS go to AWOS-C; the FAQ's question text says 207.
- **Campbell units:** the case study gives 1,529 units, but its listed parts (700 ACU, 799 DCP, 50 SCA) add to 1,549. That figure was read only as a WebFetch extract.

## Gaps

- **Ages and FERS eligibility for the NWS and FAA staff:** no career dates are published. The Office of Observations holds them; OPM's FedScope gives only aggregates.
- **Current holders:**
  - No document after January 2025 confirms Boutin, Adams, Devost or Diaz in post, and the Christine Smith (Schultz) snippet is unconfirmed.
  - The 6–19 Nov 2026 AOMC posting suggests a change at the top of the AOMC.
  - To settle these, ask the ASOS program office (suad.asos.pmo@noaa.gov).
- **Amounts:**
  - FAA ASWON Sustainment 2 is in FAA's budget justifications on transportation.gov, which refused the download (HTTP 403, including its Wayback copy).
  - The tri-agency MOA text and its reimbursement amounts sit with NWS and FAA; a FOIA request is the route.
  - The ASOS-SLEP contract number is in FPDS/USAspending.
- **Not read:** the 2020 NWS Strategic Human Capital Plan (reported by GAO; text not found), and the OIG's Nov 2026 staffing evaluation (OIG-27-004-I, after the baseline).
- `check-by-hand.md` lists 5 pages. `sites-to-trust.md` lists 2 hosts the sandbox refused (s.campbellsci.com, fpaw.aero); check whether to add either to the allowed domains.

## Sources

- Official, NWS: [ASOS Issue Report Governance v6 (2024)](https://weather.gov/media/asos/ASOS%20Issue%20Report%20-%20Governance%20v6.pdf); [PNS 24-48 (2024)](https://www.weather.gov/media/notification/pdf_2023_24/pns24-48_re-commence_ote_asos_temp_dew_sensor_replacement.pdf); [NWSI 30-2111 ASOS Maintenance (2025)](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf); [ASOS FAQ](https://www.weather.gov/asos/FAQ.html); [Murphy, ASOS update (2023)](https://www.weather.gov/media/lix/gcaws/Presentation1Murphy.pdf); [Boutin, FPAW briefing (2023), read via Wayback](https://fpaw.aero/sites/default/files/163/2-boutin-decadal-look-asos-lifecycle-upgrades.pdf); [USAJOBS NWS-27-13108102-ST (2026)](https://www.usajobs.gov/job/891863400)
- Official, NOAA and NCEI: [NOAA FY2026 Congressional Justification](https://www.noaa.gov/organization/budget-finance-performance/budget-and-reports); [GHCNh v1 metadata C01688](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01688/html); [ASOS 1-minute page 1 metadata C00386](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00386/html); [ASOS 5-minute metadata C00418](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00418/xml)
- Official, FAA: [ASWON page (2025)](https://www.faa.gov/air_traffic/weather/aswon); [CIP FY2025–2029](https://www.faa.gov/air_traffic/publications/cip/cip-overview-fy25-fy29.pdf)
- Oversight: [GAO-17-364 (2017)](https://www.gao.gov/products/gao-17-364); [Commerce OIG FY2024 Top Management Challenges](https://www.oig.doc.gov/wp-content/OIGPublications/Top_Management_Challenges_Department_of_Commerce_FY_2024_SECURED.pdf)
- Registries: [ORCID, Casey employments](https://pub.orcid.org/v3.0/0009-0001-7709-889X/employments); [ORCID, McNeill works](https://pub.orcid.org/v3.0/0000-0001-8000-6813/works); [OpenAlex, Menne works](https://api.openalex.org/works?filter=author.id:A5025236587&sort=publication_year:asc&per-page=5)
- Other:
  - [AMS 2017 ASOS modernization paper](https://ams.confex.com/ams/97Annual/webprogram/Manuscript/Paper315698/AMS%20Modernization%20of%20ASOS%20Hardware%20and%20Software%20Paper_FINAL.pdf)
  - [Campbell Scientific ASOS case study](https://www.campbellsci.com/us-asos-weather-network) (vendor; read via WebFetch extract)
  - [HigherGov IDV 1305M223DNWWG0082](https://www.highergov.com/idv/1305M223DNWWG0082) (aggregator; WebFetch extract)
  - DuckDuckGo snippets, read as snippets only: [Boutin](https://html.duckduckgo.com/html/?q=%22Kenneth+Boutin%22+ASOS) and [ASOS PM 2026](https://html.duckduckgo.com/html/?q=%22ASOS+Program+Manager%22+NWS+2026)

Saved in [`web_search_results/2026-11-26_asos-people-funding-pt3/`](./): this answer, `method.md`, the research record, `check-by-hand.md` and `sites-to-trust.md`.
