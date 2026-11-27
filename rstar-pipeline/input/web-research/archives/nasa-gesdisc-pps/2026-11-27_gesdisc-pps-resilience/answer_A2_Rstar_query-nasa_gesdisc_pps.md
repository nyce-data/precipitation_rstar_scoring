# How resilient are GES DISC and PPS as homes for IMERG and GPCP data?

**Direct answer.** Neither repository publishes the evidence that would earn the four strength statements. GES DISC now
holds IMERG and GPCP V3.x in one AWS Region (us-west-2). ESDIS deliberately counts Availability Zones within that Region
as its "off-site" copy, and NASA's own inspector general recorded ESDIS calling one-vendor cloud storage "a single
point of failure". So GES DISC on its own contradicts RRS-1 and supports D-2. For IMERG, though, PPS's own archive at
Goddard is a second, geographically separate holder (it alone still serves IMERG V06), but no cross-check of the two is
published. PPS keeps near-real-time files for only two weeks and has had a hardware fault on its production archive.
ESDIS's own requirements call for checksums on transfer and a "capability to restore", but set no re-check interval
and require backups of products only "depending on need". Nothing is published on periodic checksum checks (RRS-2) or
a tested disaster recovery plan (RRS-3) for either repository. The outages on record ended without any reported data
loss, but also without any published accounting (RRS-5). Overall confidence: **moderate**. The documents found are NASA's own
and agree, but most of the verdicts rest on what NASA has *not* published.

## Scorecard

| Statement (as worded) | GES DISC (archive of record; Earthdata Cloud) | PPS (makes IMERG; serves the Late Run) |
|---|---|---|
| RRS-1 two or more geographically independent sites with verified copies | **Contradicts** for GES DISC alone (one Region; multi-AZ counted as off-site; on-premises archive a pass-through; backups of products required only "depending on need"). Moderate | **Partly supports, for IMERG only:** PPS (Goddard, Maryland) and GES DISC (AWS Oregon) both hold V07, and PPS alone holds V06. "Verified" is not supported, since no cross-check is published. Moderate |
| RRS-2 checksum checks quarterly or more often | **Not supported:** checksums required at ingest, archive and distribution, but no re-check interval; granule metadata carries no checksum; a 2024 empty-file fault in an IMERG input was found by a user. Moderate | **Not published.** Moderate |
| RRS-3 DR plan tested in the past 2 years, with documented results | **Not published.** A "capability to restore" is required, but no test of it is published; the only documented exercise is Earthdata Login's failover test on Feb 12, 2026. Moderate | **Not published;** no backup site found. Moderate |
| RRS-5 survived a major disruption without data loss | **Weak support:** 2025 shutdown and Oct 28–30, 2026 ingest pause, no loss reported. Moderate | **Weak support:** Jan–Feb 2025 archive fault "restarted, tested and verified"; no loss statement. Low |
| D-2 storage at end of life or a single point of failure | **Supports** (single Region, single vendor). Moderate–high | **Partly supports** (one NRT system; no backup site published). Low |
| D-3 access infrastructure fragile or unfunded | **Supports:** successor contract (ENX) still unawarded; Earthdata Login token generation degraded for over five days in December 2025, with shorter spells in 2026. Moderate | **Not assessed** (PPS's own servers and contractor not found). Low |

*Sources by row are cited in the sections below. "Not published" means nothing was found after the searches listed in
`research-record.json`. It is a finding about the public record, not proof that no plan or check exists.*

## Copies (RRS-1, D-2)

- **GES DISC holds its data in one AWS Region.** GES DISC staff answered on Sept 3, 2026 that "GES DISC data are
  stored in the AWS region US West (Oregon), or us-west-2"
  ([GES DISC, Earthdata Forum, 2026](https://forum.earthdata.nasa.gov/viewtopic.php?t=8190)). The CMR record for an
  IMERG Late Run (GPM_3IMERGHHL.07) granule lists a single S3 location in `gesdisc-cumulus-prod-protected`
  ([NASA CMR, 2026](https://cmr.earthdata.nasa.gov/search/granules.umm_json?short_name=GPM_3IMERGHHL&version=07&page_size=1)).
  GES DISC said that by September 30, 2026 its on-premises archives "will only maintain a 'rolling' archive",
  with Earthdata Cloud "the primary host of all GES DISC data". It added: "Data will not be accessible publicly via the
  on-premises server, only via Earthdata Cloud/Cumulus"
  ([GES DISC migration guidance](https://github.com/nasa/gesdisc-tutorials/blob/main/user-guidance/GES_DISC_Migration_to_Earthdata_Website_and_Earthdata_Cloud.md)).
  Our reading: whatever stays on premises is a rolling pass-through, not a second public or verified archive.
- **ESDIS's strategy is one Region by design.** ESDIS's March 2026 slides meet the "1 copy located off-site" rule with
  "AWS Availability Zones in a Region … up to 60 miles" apart and "multi-AZ cloud storage" for disasters. In place of
  extra copies they use S3 versioning (a "lazy backup") and object lock, and they say "We have work to do in detecting
  accidental/malicious deletions". They ask "Why do we have an on-premises copy instead of a cloud backup with a
  different vendor?" and note "We are wary of renting storage as opposed to owning it". They also say "We are not conventional. Our budgets are not in lock-step with our data growth"
  ([ESDIS, WGISS-61, 2026](https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-61/8.7%20WGISS-61%20NASA_s%20evolving%20Archive%20Guidelines%20for%20the%20cloud.pdf)).
  The slides carry a "subject to change" disclaimer. **Moderate.**
- **The backup tool stays in the same Region.** Cumulus's backup component, ORCA, "maintains a cloud ready backup"
  in Glacier or Deep Archive storage, best placed in a separate Disaster Recovery account. The guide's generic setup
  command creates the bucket in `us-west-2`
  ([ORCA deployment guide](https://nasa.github.io/cumulus-orca/docs/developer/deployment-guide/deployment-s3-bucket)).
  Whether GES DISC runs ORCA, and in which Region, is not published. As documented, the tool gives a copy in another
  account, not necessarily in another Region.
- **The 2020 warning is still the latest word.** NASA OIG reported that "According to ESDIS, this introduces the risk
  of a single point of failure because all Earth science data will be stored with one vendor", and that ESDIS was
  "investigating a long-term archive backup solution"
  ([NASA OIG, IG-20-011, 2020](https://oig.nasa.gov/docs/IG-20-011.pdf), pp. 15–16). No later document says that backup
  was built. The audit's recommendation 1 (an independent analysis of the cloud's long-term financial sustainability
  while keeping the DAAC footprint) was still open on October 15, 2026
  ([NASA OIG open recommendations, 2026](https://oig.nasa.gov/wp-content/uploads/2026/10/or-10-26.pdf), row 3). **High.**
- **PPS** keeps near-real-time data "for the most recent 2 weeks". This is stated on its 2A DPR NRT page
  ([GPM/PPS](https://gpm.nasa.gov/node/2527)); a separate figure for IMERG Late files was not found. PPS's long-term
  "arthurhou" production archive and IMERG at GES DISC are two copies of the same products in different places. When
  arthurhou failed in 2025, PPS sent users to GES DISC for IMERG V07B
  ([PPS, 2025](https://gpm.nasa.gov/data/news/important-ppss-arthurhou-gpm-production-data-archive-temporarily-unavailable)).
  The traffic also runs the other way. When GES DISC stopped distributing IMERG V06 in July 2024, it said "IMERG
  version 06 will continue to be available from the Precipitation Processing System"
  ([GES DISC alert, 2024](https://disc.gsfc.nasa.gov/information/alerts?title=End%20of%20support%20for%20IMERG%20Final%20version%2006)).
  So IMERG V07 sits at two separate sites, and V06 now has only one named holder. No source says the two copies are
  checked against each other, or how long arthurhou keeps files. GPCP V3.x has no PPS copy in what was read.
- **What ESDIS requires.** ESDIS's DAAC requirements (ADURD 423-10-69 Rev B, effective March 2017) ask each DAAC to
  keep "an off-site backup copy of all other data that would be impossible or difficult to recover". The list covers
  products only as "selected data products, depending on need", and the backup may sit "in a NASA Cloud archive"
  ([ESDIS, ADURD Rev B](https://www.earthdata.nasa.gov/s3fs-public/imported/423-10-69_ADURD_RevB.pdf), §2.3.2 item 9).
  The copy read lists an "Expiration Date: March 2022", so a later revision may exist. The only standing second copy it
  names is Level 0: for "some missions", EDOS keeps "a backup of the Level 0 data" at White Sands, NM (item 8). No
  mission is named, so it is not shown to cover GPM. Cumulus, the software behind
  Earthdata Cloud, has backup tasks (LZARDS and ORCA), but the LZARDS task "is not automatically deployed"
  ([Cumulus docs](https://nasa.github.io/cumulus/docs/workflow_tasks/lzards_backup/)). Its overview page needs a NASA
  login. Whether GES DISC runs either tool is not public. **Moderate.**

## Integrity (RRS-2) and certification

- **No checksum algorithm or check frequency is published** for GES DISC, PPS or Earthdata Cloud. The IMERG Late
  granule record has only `"Name": "Not provided"` and a size under ArchiveAndDistributionInformation, and no checksum
  field ([NASA CMR](https://cmr.earthdata.nasa.gov/search/granules.umm_json?short_name=GPM_3IMERGHHL&version=07&page_size=1);
  one granule checked). ORCA's design notes plan a reconciliation comparing "Key, LastModified, ETag, and Size" "on a
  regular schedule" with no interval given. That page was read only through a fetch tool's extraction
  ([ORCA reconciliation notes](https://nasa.github.io/cumulus-orca/docs/developer/research/research-reconciliation)).
  NASA's Preservation Content Specification defines what content to preserve and sets no fixity rule
  ([ESDIS](https://www.earthdata.nasa.gov/about/esdis/esco/standards-practices/nasa-earth-science-data-preservation-content-specification);
  landing page only). NASA OIG found ESDIS rated DAAC data integrity below NIST's "moderate" level, partly because it
  could "reprocess data internally in the event data integrity was compromised", a reason NIST warns against
  ([IG-20-011](https://oig.nasa.gov/docs/IG-20-011.pdf), p. 20). **Moderate.**
- **Checksums are required for transfers, not for re-checks.** ADURD says each DAAC system "shall ensure data
  integrity through the use of checksums in order to satisfy interface requirements with external systems", at
  ingest, archive and distribution, and gives no re-verification interval
  ([ESDIS, ADURD Rev B](https://www.earthdata.nasa.gov/s3fs-public/imported/423-10-69_ADURD_RevB.pdf)). The
  Preservation Content Specification (Rev C, 2022) treats fixity as "implementation details (i.e., how)"
  ([ESDIS, 423-SPEC-001 Rev C](https://www.earthdata.nasa.gov/s3fs-public/2022-06/NASA_ESD_Preservation_Spec_C.pdf?VersionId=nLDSU6awu0KGWq6o.YzEhLvK0tG.8l6_)).
  Cumulus can "Add checksums to files in S3 which don't have one"
  ([Cumulus tasks](https://nasa.github.io/cumulus/docs/next/tasks/)). No published NASA document requires RRS-2's
  quarterly re-check. **Moderate** (ADURD may have been revised).
- **A fault found by a user.** A user found empty files in GPM_MERGIR, the infrared input to IMERG, for April 22–23,
  2024; GES DISC's alert is dated Aug 15, 2025, and doesn't say when the user found them. GES DISC re-acquired the data, "replaced in our archive", and only then added "a check for empty files"
  ([GES DISC alert, Aug 15, 2025](https://disc.gsfc.nasa.gov/information/alerts?title=Reprocessing%20of%20the%20NCEP%2FCPC%20L3%20Half%20Hourly%204km%20Global%20(60S%20-%2060N)%20Merged%20IR%20(GPM_MERGIR))).
  This is a content defect that fixity checks on stored bytes would not catch either. It shows repair after the fact,
  not routine checking. **High** for the facts.
- **Certification.** GES DISC is **not** on CoreTrustSeal's current list of certified repositories. Five other NASA
  data centers are: ASDC, GHRC, PO.DAAC, LAADS DAAC (also at Goddard) and SEDAC
  ([CoreTrustSeal, read 2026-11-27](https://amt.coretrustseal.org/certificates/)). GES DISC "has been a WDS Regular
  Member since September 2014" ([World Data System](https://worlddatasystem.org/member-highlight-goddard-earth-sciences-data-and-information-services-center/)).
  No certification of any kind was found for PPS, and ISO 16363 was not searched. **High** for the CoreTrustSeal
  finding.

## Recovery (RRS-3)

- No continuity-of-operations or disaster recovery plan, and no record of a recovery test, is published for ESDIS,
  GES DISC or PPS. ESDIS requires each DAAC system to have "the capability to restore its archive to avoid permanent
  loss of archived data" (ADURD §2.3.2 item 10), but no test of that capability is published. No PPS backup site or failover for the near-real-time system was found.
- **The two oversight reports named in the question don't cover data systems.** IG-26-005 reviews Goddard's building
  relocations and closures, and finds they "have not impacted Goddard's ability to execute its responsibilities"
  ([NASA OIG, IG-26-005, 2026](https://oig.nasa.gov/office-of-inspector-general-oig/letters-to-congress/review-of-goddard-space-flight-centers-transformation-efforts/)).
  GAO-26-108556 assesses major projects' cost, schedule and workforce, and its full text has no mention of EOSDIS,
  ESDIS, contingency or backup ([GAO, 2026](https://files.gao.gov/reports/GAO-26-108556/index.html)).
- **The one documented exercise is for logins, not data.** Earthdata Login ran a "failover plan … contingency exercise"
  on February 12, 2026, from 11:18 to 11:57 AM, with reduced functionality ([Earthdata Status](https://status.earthdata.nasa.gov/client_applications/21/history)). No
  results were published, and it covers authentication, not stored data. **Moderate.**

## Storage and access (D-2, D-3)

- **Contracts.** The successor to the EED-3 contract (to January 31, 2027, as the question states and earlier runs
  found), ESDIS Next (ENX), is still a sources-sought notice. The SAM.gov record, re-published Jan 23, 2026 and last
  versioned 2026-10-23, is "Inactive" and says "No solicitation exists"
  ([SAM.gov, RFI-NASA-GSFC-ENX](https://sam.gov/workspace/contract/opp/155dc55f43934efe8e91537863f990b7/view)).
  This is against a forecast award in Q3 FY26 ([HigherGov forecast, 2025](https://www.highergov.com/contract-forecast/earth-science-data-and-information-system-esdis-1121962)).
  No award was found, so about two months before EED-3 ends no successor is public. **Moderate.**
- **Earthdata Login** stands in front of downloads. Its status history shows degraded service on Dec 22, 23 and 26,
  2025, Feb 13, 2026 (09:05 AM–12:48 PM), Jun 7, Sept 24 (three spells) and Nov 19, 2026
  ([Earthdata Status](https://status.earthdata.nasa.gov/client_applications/21/history); page 1 of 16). These are
  mostly short outages. One was not short: token generation was degraded from "December 16, 2025 06:20 AM - December
  21, 2025 05:40 PM", with user-authorization problems from December 18 to 19
  ([Earthdata Status, page 2](https://status.earthdata.nasa.gov/client_applications/21/history?page=2)). The status
  page calls these "degraded", not full outages, and gives no failure rate. Its funding was not found.
- **PPS's own storage.** PPS moved its NRT data to a "new storage system" in January 2026
  ([PPS, 2026](https://gpm.nasa.gov/data/news/upcoming-gpm-near-real-time-maintenance)). Its hardware age and its
  contractor were not found.

## Track record (RRS-5)

- **PPS, Jan 31–Feb 5, 2025.** PPS "detected hardware issues" on its production archive and "reported file length
  discrepancies". It suspended access and archiving, then reported all services "restarted, tested and verified"
  ([PPS, 2025](https://gpm.nasa.gov/data/news/important-ppss-arthurhou-gpm-production-data-archive-temporarily-unavailable);
  [PPS, 2025](https://gpm.nasa.gov/data/news/ppss-arthurhou-gpm-production-data-archive-back-online)). Neither notice
  says whether any files were lost or regenerated.
- **PPS, Apr 16, 2025:** "hardware updates on the GPM NRT and SDPS processing and network environment", with downtime
  "estimated at 20 minutes" ([PPS, 2025](https://gpm.nasa.gov/data/news/equipment-updates-april-16-2025-will-impact-access-gpm-nrt-servers)).
- **PPS, Jan 20, 2026** was a *planned* shutdown of about 14 hours to finish moving data to new storage. "During this
  14 hours no new data will be produced or ingested", and jsimpson stayed reachable with no new files
  ([PPS, 2026](https://gpm.nasa.gov/data/news/upcoming-gpm-near-real-time-maintenance)). No after-action notice
  (actual duration, Late Run latency, files regenerated) was found.
- **GES DISC, Oct 28–30, 2026** was a planned pause in ingest for the Consolidated Ingest and Archive migration, from
  October 28, 5:00 p.m. to October 30, 9:00 a.m. ET. Search and download were "expected to remain operational", and
  the alert was marked resolved on Nov. 2, 2026
  ([Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/ingest-archive-migration-interrupt-data-ingestion-oct.-28-30);
  [alert history](https://www.earthdata.nasa.gov/data/alerts-outages/content/data-alert-history/17367)).
- **2025 shutdown.** Earthdata posted only that "NASA is not updating this website" (Oct 1–10, 2025)
  ([Earthdata](https://www.earthdata.nasa.gov/data/alerts-outages/federal-government-shutdown)). ESDIS's weekly
  metrics list one shutdown-caused delay, to OMI-AURA on Oct 10, 2025
  ([ESDIS metrics](https://www.earthdata.nasa.gov/about/data-metrics/esdis-metrics/weekly-metrics/10-20-2025)). GES
  DISC posted the same banner on Oct 1, 2025, yet its alerts list shows items posted on Oct 6–9, 2025, mostly relayed
  ESA notices ([GES DISC banner](https://disc.gsfc.nasa.gov/information/alerts?title=Due%20to%20the%20lapse%20in%20federal%20government%20funding%2C%20NASA%20is%20not%20updating%20this%20website.%20We%20sincerely%20regret%20this%20inconvenience.);
  [alerts page 6](https://disc.gsfc.nasa.gov/information/alerts?page=6)). No GES DISC or PPS data gap was reported.
- **IMERG's own move.** GES DISC moved the OPeNDAP services for 7 IMERG V07 collections to the cloud from May 11 to
  May 13, 2026, with Giovanni variables unavailable "for some time"
  ([GES DISC alert, 2026](https://disc.gsfc.nasa.gov/information/alerts?title=GPM_3IMERG%20v07%20variables%20will%20be%20temporarily%20unavailable%20May%2011-13)).
- **The 2026 cloud migration.** GES DISC's alerts page announced that HTTPS access to its on-premises servers "will
  be discontinued no earlier than September 30, 2026". Its alerts from Aug 24 to Nov 10, 2026 (page 1 of 414) list
  service retirements and three GPM V08 data recalls (two of them for incorrect input data or an incorrect setting; the
  third gives no reason in its first line), but no lost or missing granules
  ([GES DISC alerts](https://disc.gsfc.nasa.gov/information/alerts)). The October 28–30 pause is not on that page. No data loss is reported for
  any of these events, but none has a published after-action report, so "survived without loss" rests on silence.
  **Low to moderate.**

## Gaps and what would close them

- **Checksum and fixity practice, DR plans and test results** for ESDIS, GES DISC and PPS: not published. ESDIS and
  GES DISC (NASA Goddard) hold them, for example in EOSDIS operations documents and the system security plans OIG
  reviewed in 2020. They could be obtained by asking GES DISC user services or by a FOIA request to NASA; no
  publication date is known.
- **Whether GES DISC runs ORCA, or holds any copy outside us-west-2:** ESDIS holds this; not public.
- **PPS:** retention on arthurhou, any cross-check with GES DISC, a backup site, and after-action notes for 2025 and
  January 2026 are not published. PPS (GSFC Code 610.2) holds them, and might answer through the GPM data news list or
  on request.
- **ENX award:** watch SAM.gov notice RFI-NASA-GSFC-ENX for a solicitation; none is out.
- **Whether ADURD Rev B (2017, "Expiration Date: March 2022") has a newer revision:** ESDIS's configuration-management
  library holds it and is not public. ESDIS's implementation guidance for preservation (ESDS-RFC-042) was not found as
  a PDF.
- **Not read:**
  - the LZARDS overview (needs a NASA login) and Cumulus's sync-granule README (GitHub returned 503);
  - GES DISC alerts pages 4 and 7–17 (pages 1–3, 5 and 6 were searched);
  - pages 3–16 of the Earthdata Login history;
  - NASA OIG reports beyond the October 2026 open-recommendations list.
  They are listed in `check-by-hand.md`.
- **Follow-up pass:** run the same day (05:25–05:45), adding sources s28–s38 and claims c9–c16. `method.md` gives the details.
- `sites-to-trust.md` lists the hosts the sandbox refused (7). You can check whether to add any of them to your allowed
  domains.

## Sources

**NASA, ESDIS, GES DISC and PPS**
- [ESDIS (D. Newman), Evolving Archive guidelines for the cloud, WGISS-61, 2026](https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-61/8.7%20WGISS-61%20NASA_s%20evolving%20Archive%20Guidelines%20for%20the%20cloud.pdf)
- [GES DISC, In which AWS region do GES DISC data reside?, Earthdata Forum, 2026](https://forum.earthdata.nasa.gov/viewtopic.php?t=8190)
- [GES DISC, Alerts (page 1 of 414, read 2026-11-27)](https://disc.gsfc.nasa.gov/information/alerts)
- [GES DISC, Migration to Earthdata Website and Earthdata Cloud (user guidance)](https://github.com/nasa/gesdisc-tutorials/blob/main/user-guidance/GES_DISC_Migration_to_Earthdata_Website_and_Earthdata_Cloud.md)
- [NASA CMR, UMM-G granule record GPM_3IMERGHHL.07](https://cmr.earthdata.nasa.gov/search/granules.umm_json?short_name=GPM_3IMERGHHL&version=07&page_size=1)
- [NASA Cumulus ORCA, Creating the Archive Bucket](https://nasa.github.io/cumulus-orca/docs/developer/deployment-guide/deployment-s3-bucket)
- [NASA Cumulus ORCA, Reconciliation research notes](https://nasa.github.io/cumulus-orca/docs/developer/research/research-reconciliation) (read via fetch-tool extraction only)
- [ESDIS, NASA Earth Science Data Preservation Content Specification](https://www.earthdata.nasa.gov/about/esdis/esco/standards-practices/nasa-earth-science-data-preservation-content-specification) (landing page only)
- [PPS, 2A DPR PPS FTP NRT](https://gpm.nasa.gov/node/2527)
- [PPS, "arthurhou" Production Data Archive Temporarily Unavailable, 2025](https://gpm.nasa.gov/data/news/important-ppss-arthurhou-gpm-production-data-archive-temporarily-unavailable)
- [PPS, "arthurhou" Production Data Archive Back Online, 2025](https://gpm.nasa.gov/data/news/ppss-arthurhou-gpm-production-data-archive-back-online)
- [PPS, Upcoming GPM Near Real-time Maintenance, 2026](https://gpm.nasa.gov/data/news/upcoming-gpm-near-real-time-maintenance)
- [Earthdata, Ingest & Archive Migration to Interrupt Data Ingestion on Oct. 28-30, 2026](https://www.earthdata.nasa.gov/data/alerts-outages/ingest-archive-migration-interrupt-data-ingestion-oct.-28-30)
- [Earthdata, Data alert history](https://www.earthdata.nasa.gov/data/alerts-outages/content/data-alert-history/17367)
- [Earthdata, Federal Government Shutdown alert, 2025](https://www.earthdata.nasa.gov/data/alerts-outages/federal-government-shutdown)
- [ESDIS, Weekly metrics 10-20-2025](https://www.earthdata.nasa.gov/about/data-metrics/esdis-metrics/weekly-metrics/10-20-2025)
- [Earthdata Status, Earthdata Login degraded service events](https://status.earthdata.nasa.gov/client_applications/21/history)
- [Earthdata Status, Earthdata Login degraded service events, page 2](https://status.earthdata.nasa.gov/client_applications/21/history?page=2)
- [ESDIS, Archiving, Distribution and User Services Requirements in EOSDIS (ADURD), 423-10-69 Rev B, 2017](https://www.earthdata.nasa.gov/s3fs-public/imported/423-10-69_ADURD_RevB.pdf)
- [ESDIS, NASA Earth Science Data Preservation Content Specification, 423-SPEC-001 Rev C, 2022](https://www.earthdata.nasa.gov/s3fs-public/2022-06/NASA_ESD_Preservation_Spec_C.pdf?VersionId=nLDSU6awu0KGWq6o.YzEhLvK0tG.8l6_)
- [NASA Cumulus, Cumulus Tasks](https://nasa.github.io/cumulus/docs/next/tasks/)
- [NASA Cumulus, LZARDS Backup](https://nasa.github.io/cumulus/docs/workflow_tasks/lzards_backup/)
- [GES DISC, End of support for IMERG Final version 06, 2024](https://disc.gsfc.nasa.gov/information/alerts?title=End%20of%20support%20for%20IMERG%20Final%20version%2006)
- [GES DISC, Reprocessing of GPM_MERGIR, 2025](https://disc.gsfc.nasa.gov/information/alerts?title=Reprocessing%20of%20the%20NCEP%2FCPC%20L3%20Half%20Hourly%204km%20Global%20(60S%20-%2060N)%20Merged%20IR%20(GPM_MERGIR))
- [GES DISC, funding-lapse banner, 2025](https://disc.gsfc.nasa.gov/information/alerts?title=Due%20to%20the%20lapse%20in%20federal%20government%20funding%2C%20NASA%20is%20not%20updating%20this%20website.%20We%20sincerely%20regret%20this%20inconvenience.)
- [GES DISC, Alerts page 6](https://disc.gsfc.nasa.gov/information/alerts?page=6)
- [GES DISC, GPM_3IMERG v07 variables temporarily unavailable May 11-13, 2026](https://disc.gsfc.nasa.gov/information/alerts?title=GPM_3IMERG%20v07%20variables%20will%20be%20temporarily%20unavailable%20May%2011-13)
- [PPS, Equipment Updates on April 16, 2025](https://gpm.nasa.gov/data/news/equipment-updates-april-16-2025-will-impact-access-gpm-nrt-servers)

**Oversight and procurement**
- [NASA OIG, NASA's Management of Distributed Active Archive Centers (IG-20-011), 2020](https://oig.nasa.gov/docs/IG-20-011.pdf)
- [NASA OIG, Open Recommendations as of October 15, 2026](https://oig.nasa.gov/wp-content/uploads/2026/10/or-10-26.pdf)
- [NASA OIG, Review of Goddard Space Flight Center's Transformation Efforts (IG-26-005), 2026](https://oig.nasa.gov/office-of-inspector-general-oig/letters-to-congress/review-of-goddard-space-flight-centers-transformation-efforts/) (text from an earlier run's saved copy)
- [GAO, NASA: Assessments of Major Projects (GAO-26-108556), 2026](https://files.gao.gov/reports/GAO-26-108556/index.html)
- [GAO, GAO-26-108556 Highlights, 2026](https://www.gao.gov/assets/gao-26-108556-highlights.pdf)
- [SAM.gov, ESDIS Next (ENX) RFI, RFI-NASA-GSFC-ENX](https://sam.gov/workspace/contract/opp/155dc55f43934efe8e91537863f990b7/view)
- [HigherGov, ESDIS Next (ENX) contract forecast, 2025](https://www.highergov.com/contract-forecast/earth-science-data-and-information-system-esdis-1121962) (aggregator)

**Certifiers**
- [CoreTrustSeal, Current certified data repositories (read 2026-11-27)](https://amt.coretrustseal.org/certificates/)
- [World Data System, Member Highlight: GES DISC](https://worlddatasystem.org/member-highlight-goddard-earth-sciences-data-and-information-services-center/)

Saved in [`web_search_results/2026-11-27_gesdisc-pps-resilience/`](./): this answer, `method.md`,
`research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
