# How resilient is UC Irvine CHRS's own data site?

CHRS's own site (the CHRS Data Portal and persiann.eng.uci.edu over HTTPS and FTP) is a small, research-group-run service, and it is fragile as a home for data. One listed system administrator runs it. The portal was built "mostly from discretionary sources", and no backup, second site, checksum or disaster recovery plan is published for it. Its one public outage notice and its 18-month gap in PERSIANN-CDR postings went unexplained. The site has stayed up and kept its files through 2024–2026, and the NSF award that was cut and then restored doesn't fund it. **Confidence: moderate.** Most of these findings rest on CHRS's and UC Irvine's own pages, and on the fact that they say nothing on these points.

For PERSIANN-CDR in particular, NCEI's copy is the independent one: the [2026-11-19 Part 1 run](../2026-11-19_persiann-cdr-daily-about-pt1/answer.md) found it there. PERSIANN, PDIR-Now and CCS-CDR have no copy outside CHRS that this run found.

## Scorecard

| Statement | Verdict | Main evidence |
|---|---|---|
| RRS-1: two or more independent sites hold verified copies | **Contradicts** for CHRS-only products. For PERSIANN-CDR it is only partly met: NCEI holds a copy, but no check of the two against each other was found | c2 |
| RRS-2: checksum checks quarterly or more often | **Contradicts** (no evidence; no checksums published) | c3 |
| RRS-3: DR plan tested in the past 2 years | **Contradicts** (no CHRS plan published; campus backup service is opt-in) | c4 |
| RRS-4: no imminent threat to funding | **Contradicts** (grant-funded School Center; no campus commitment published) | c5, c6 |
| RRS-5: survived a major disruption without data loss | **Partly supports** (outages and lags recovered with files present; nothing documents the cause or the losses) | c7, c8 |
| D-2: storage at end of life or a single point of failure | **Supports** (data produced and served on CHRS's own servers; no second site published) | c2 |
| D-3: access infrastructure fragile or unfunded | **Supports** (one admin; development from discretionary money; unexplained lags) | c1, c8 |

Claim IDs refer to `research-record.json`.

## Who runs it (D-3)

- **One administrator.** CHRS's directory lists one person under "Program & System Administrator", an Assistant Specialist ([CHRS Directory](https://chrs.web.uci.edu/chrs_directory.php)). It also lists four faculty, four postdocs and 11 PhD students, all in Civil and Environmental Engineering.
- **Built by CHRS itself.** The portal was "built in 2016 by a team of scientists and computer programmers at CHRS" ([Nguyen et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6326112/)). Its Info tab says "Financial resources for development of CHRS Data Portal came mostly from discretionary sources" ([CHRS Data Portal, Info tab](https://chrsdata.eng.uci.edu/)).
- **The named programmer has gone.** The same tab says the Army Corps' ICIWaRM paid for "a major part of support" for Dan Braithwaite, Programmer Analyst III. He is no longer in the directory, nor are three other programmer or developer authors of the 2019 paper (subagent's reading of the directory).
- **Not published:**
  - who maintains the servers today;
  - how the administrator post is paid for;
  - any role for Samueli School IT or campus OIT.

  OIT does host "co-located" research-group systems in its data center (DuckDuckGo snippet only), but no source places CHRS's servers there.

**Supports D-3** (moderate). On these pages the site depends on a very small CHRS team, and no source shows any money set aside for it.

## Storage and copies (D-2, RRS-1)

- **Where the data is made.** "CHRS's servers produce PERSIANN and PERSIANN-CDR by implementing the algorithms locally", and PERSIANN-CCS comes from a NOAA NESDIS server ([Nguyen et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6335616/)). The portal draws its map layers with MapServer.
- **Nothing published on backups.** No source says where the CHRS servers sit, whether they are backed up, or whether a second CHRS site exists. The paper doesn't mention backups or mirrors. A gap-pass search turned up only CHRS's own .eng.uci.edu hosts.
- **No check against NCEI's copy.** No source compares the CHRS copy of PERSIANN-CDR with NCEI's. The cloud copies that NCEI lists are NCEI's own distribution, not CHRS's (from the earlier runs' NCEI record, as read by the subagent).

**Supports D-2 and contradicts RRS-1** for the products only CHRS holds (low to moderate). This rests mostly on silence.

## Integrity and recovery (RRS-2, RRS-3)

- **No checksums published.** The PERSIANN-CDR daily folder lists 15,900 `.bin.gz` files and no md5, sha or manifest file ([daily index](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/)). The yearly and top-level folders are the same ([yearly index](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/yearly/)). No fixity practice is described anywhere. **Contradicts RRS-2.**
- **UC Irvine's backup service is opt-in.**
  - OIT sells a recharge-billed backup service, and says it "is not an archival storage service" ([UCI OIT](https://www.oit.uci.edu/services/infrastructure/data-backups/)).
  - Its SLA covers servers in on-campus data centers, keeps the backup equipment in the Science Library Data Center, and "makes secure offsite copies … to a remote location" ([OIT SLA, 2021](https://www.oit.uci.edu/files/2021/07/Data-Backup-and-Recovery-SLA.pdf)).
  - Subscribers' backups are encrypted (AES 256) and copied off site by default.
  - No source shows that CHRS subscribes. The SLA doesn't mention restore testing, and encryption is not a fixity check.
- **UC policy calls for tested plans.** UC's 2007 IS-12 says plans "should be tested on a periodic basis" ([UC IS-12, archived](https://security.ucop.edu/files/documents/policies/uc-is-12-archived.pdf)). Per a search snippet only, the 2021 revision asks for yearly backup testing at higher recovery levels. No CHRS plan or test is published. **Contradicts RRS-3.**

## Institutional support (RRS-4)

- **A School Center, not an ORU.** UC Irvine's Office of Research lists CHRS as a School Center: "an informal interdisciplinary group". It says "The majority of CHRS research activities are funded by NASA, NOAA, and NSF" ([UCI Office of Research, CHRS](https://research.uci.edu/center/center-for-hydrometeorology-and-remote-sensing-chrs/); extraction read). School Centers "are established by Deans for a defined period of time" ([UCI Centers & Institutes](https://research.uci.edu/centers-institutes/)). No campus funding, space or staff commitment is published.
- **An endowed chair, not tied to the site.** Founding director Sorooshian holds an endowed Henry Samueli Chair (2023), but no source ties it to the data site ([Samueli School, 2023](https://engineering.uci.edu/news/2023/8/two-new-samueli-chairs-engineering-announced); Wayback copy).
- **No current NSF award for the precipitation work.** All 13 of Sorooshian's NSF awards are inactive. The last, CyberSEES precipitation award 1331915 ($1,060,000), ended 08/31/2018 ([NSF API](https://api.nsf.gov/services/v1/awards.json?pdPIName=Soroosh+Sorooshian&printFields=id,title,startDate,expDate,fundsObligatedAmt,activeAwd)). NOAA and NASA funding was covered in [Part 3](../2026-11-19_persiann-cdr-daily-about-pt3/answer.md) and not updated here.
- **Campus-wide cuts.** For July 1 to February 17, UC Irvine's federal funding was down about $50M (11.7%) in 2026 against 2024/25, with about 200 fewer new awards. It reported 85 awards terminated and 14 suspended, with 56 reinstated and 11 suspensions lifted (March 2026). CHRS isn't named ([UCI Office of Research, March 2026](https://research.uci.edu/wp-content/uploads/or-update-march-2026.pdf)).

**Contradicts RRS-4** (moderate). The site rests on grants, and no campus support is published.

## Track record (RRS-5)

- **The 2024 outage.** The only outage record is the line "NOTICE: Download links available again 2024-10-11" ([portal home](https://chrsdata.eng.uci.edu/)). It gives no start date, no cause and nothing about the data.
  - The HTTP data directory answered normally on 2024-06-13 ([Wayback, /CHRSdata](https://web.archive.org/web/20240613193947/http://persiann.eng.uci.edu/CHRSdata/)).
  - The archive holds no captures of the portal between 2024-02-29 and 2025-08-21 ([Wayback CDX](https://web.archive.org/cdx/search/cdx?url=chrsdata.eng.uci.edu/&collapse=digest)). The 2025 capture shows an empty page, because the portal's content is drawn by scripts.
- **PERSIANN-CDR posting lags** ([daily index](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/), file last-modified dates):

  | Data | Files written |
  |---|---|
  | Last day of 2023 | 2024-04-15 |
  | 2024, days 1–274 | 2025-10-21 (after nothing for 18 months) |
  | 2024, days 275–366 | 2025-12-12 |
  | 2025 | 2025-12-13 to 2026-03-23 |
  | January–July 2026 | 2026-10-13 |

  The 2024 lag was out of pattern. The yearly CDR files for 2020–2023 were written 3–4 months after each year ended (2021-04-06, 2022-04-21, 2023-04-05, 2024-04-15). The 2024 file was written 2025-12-15, about 11.5 months after year end, the longest since at least 2016 ([yearly index](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/yearly/)). No CHRS source explains the lags. NCEI posts an undated notice that the CDR "is experiencing a pause in operations due to processing delays" ([NCEI](https://www.ncei.noaa.gov/node/8306)). The Wayback Machine first captured that notice on 2025-09-13, and it is still live today ([Wayback CDX](https://web.archive.org/cdx/search/cdx?url=www.ncei.noaa.gov/node/8306&output=json&collapse=digest)). It names no cause, and it sits beside NCEI's general cloud-migration warning. The lags support D-3. A file rewritten later would also show a later date.
- **The Info tab's 2020 date.** It isn't explained. Today's browser read of the tab shows no date. The portal's "What's New" lists August 2025 updates (CCS-CDR V2.0, IMERG V07B).
- **NSF 2332263.** It is a flood-protection infrastructure grant (PI AghaKouchak, now CHRS director) that doesn't mention PERSIANN. It was terminated 4/18/2025 and reinstated 6/30/2025 ([Thakur v. Trump, Dkt. 211-5](https://storage.courtlistener.com/recap/gov.uscourts.cand.450653/gov.uscourts.cand.450653.211.5.pdf)). NSF now lists it active to 10/31/2027 ([NSF API](https://api.nsf.gov/services/v1/awards/2332263.json)), but the court sheet gives 10/31/2026. This conflict is unresolved: an extension is likely, but no source says so.
- **The main site stayed up.** CHRS's main site has Wayback captures with status 200 through 2025 and shows no service notice ([Wayback CDX](https://web.archive.org/cdx/search/cdx?url=chrs.web.uci.edu/&collapse=digest)).
- **No data loss is recorded.**

**Partly supports RRS-5** (moderate): the site came back with its files. The disruptions are undocumented, though, so they show no tested recovery.

## Gaps

- **Server location, backup subscription and any DR plan or test.** Not published. CHRS holds this, and could answer on request (contacts on the portal's Info tab). UCI OIT would know whether CHRS uses its backup or co-location services.
- **The cause of the 2024 outage, the CDR posting lag and the 2020 Info-tab date.** Not published; held by CHRS.
- **Not read:**
  - the current (2021) UC IS-12;
  - CoreTrustSeal (re3data has no CHRS entry);
  - Samueli Engineering IT;
  - the later RainSphere and iRain papers;
  - the nature.com author-contributions section of the 2019 paper.
- **Leads from the checker's counter-searches.** These are search snippets only, not opened:
  - an NCAR EOL dataset entry (94.041) that links to the CHRS PERSIANN archive; it is unclear whether it holds a copy;
  - a Dryad record for PERSIANN-CCS-CDR that holds only a sample and points to the portal;
  - Google Earth Engine's PERSIANN-CDR catalog, listing coverage to 2024-09-30;
  - a 2022 OIT backup SLA, newer than the 2021 one used here;
  - a UCI IT recovery page that maps IS-12 levels to tiers, including servers at "an alternate data center";
  - a 2026 NTRS record for PERSIANN-Unet with NASA and NOAA grant numbers.

  None names a CHRS backup or second site. Each could change the RRS-1 or RRS-3 verdicts if opened.
- **Pages to check by hand.** See `check-by-hand.md`.
- **Sites to trust.** The sandbox refused one host: bpb-us-e2.wpmucdn.com, where OIT's PDF links redirect. See `sites-to-trust.md` for whether to add it to your allowed domains.
- **The time budget, not the evidence, ended the research.**

## Sources

- [CHRS Data Portal, home page and Info tab, read 2026-11-27](https://chrsdata.eng.uci.edu/)
- [CHRS Directory](https://chrs.web.uci.edu/chrs_directory.php)
- [CHRS, Index of /CHRSdata/PERSIANN-CDR/daily](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/daily/)
- [CHRS, Index of /CHRSdata/PERSIANN-CDR/yearly](https://persiann.eng.uci.edu/CHRSdata/PERSIANN-CDR/yearly/)
- [UCI Office of Research, CHRS center page](https://research.uci.edu/center/center-for-hydrometeorology-and-remote-sensing-chrs/) (extraction read)
- [UCI Office of Research, Centers & Institutes](https://research.uci.edu/centers-institutes/) (extraction read)
- [UCI Office of Research, update, March 2026](https://research.uci.edu/wp-content/uploads/or-update-march-2026.pdf)
- [UCI OIT, Data Backup and Recovery Service](https://www.oit.uci.edu/services/infrastructure/data-backups/)
- [UCI OIT, Data Backup and Recovery SLA, 2021](https://www.oit.uci.edu/files/2021/07/Data-Backup-and-Recovery-SLA.pdf)
- [UC Office of the President, IS-12 (2007, archived)](https://security.ucop.edu/files/documents/policies/uc-is-12-archived.pdf)
- [Samueli School of Engineering, Two New Samueli Chairs, 2023](https://engineering.uci.edu/news/2023/8/two-new-samueli-chairs-engineering-announced) (Wayback copy)
- [Nguyen et al., The CHRS Data Portal, Scientific Data, 2019 (PMC6326112)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6326112/)
- [Nguyen et al., 2019 (PMC6335616)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6335616/)
- [NSF Award 2332263 record](https://api.nsf.gov/services/v1/awards/2332263.json)
- [NSF awards API, PI Soroosh Sorooshian](https://api.nsf.gov/services/v1/awards.json?pdPIName=Soroosh+Sorooshian&printFields=id,title,startDate,expDate,fundsObligatedAmt,activeAwd)
- [Thakur v. Trump (N.D. Cal.), Dkt. 211-5](https://storage.courtlistener.com/recap/gov.uscourts.cand.450653/gov.uscourts.cand.450653.211.5.pdf)
- [NCEI, Precipitation - PERSIANN CDR processing delay (undated notice)](https://www.ncei.noaa.gov/node/8306)
- [CDX listing, NCEI PERSIANN CDR delay notice](https://web.archive.org/cdx/search/cdx?url=www.ncei.noaa.gov/node/8306&output=json&collapse=digest)
- [Index of /CHRSdata, 2024-06-13](https://web.archive.org/web/20240613193947/http://persiann.eng.uci.edu/CHRSdata/)
- [CDX listing, chrsdata.eng.uci.edu](https://web.archive.org/cdx/search/cdx?url=chrsdata.eng.uci.edu/&collapse=digest)
- [CDX listing, chrs.web.uci.edu](https://web.archive.org/cdx/search/cdx?url=chrs.web.uci.edu/&collapse=digest)

Saved in [`web_search_results/2026-11-27_uci-chrs-resilience/`](./): this answer, `method.md`, `research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
