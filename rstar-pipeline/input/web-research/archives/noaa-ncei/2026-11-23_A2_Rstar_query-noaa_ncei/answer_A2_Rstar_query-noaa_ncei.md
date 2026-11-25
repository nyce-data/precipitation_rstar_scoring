# How resilient is NCEI as a home for GPCP Daily, PERSIANN-CDR Daily and its holdings?

**Direct answer.** Beyond what the GHCN-Daily run (pt9) found, NCEI's own documents confirm that checksums are verified at ingest, on retrieval and on order, not on a schedule (contradicts RRS-2). Outside Asheville, they document verified copies only for Boulder's own holdings and for CLASS data in AWS. GPCP Daily also appears in NCEI's new cloud archive bucket, but no source says how many copies exist, in which regions, or that they are verified. So RRS-1 is not shown for either CDR; both are archived in Asheville. Nothing on disaster-recovery tests is published (RRS-3), and no data loss has been reported since 2015 but none has been ruled out either (RRS-5 not shown). Overall confidence: moderate. Most of this rests on what NCEI's documents leave out, and the 2026 cloud move, which runs to spring 2027, is changing where the copies sit.

## Integrity (RRS-2: checksum checks quarterly or more often)

- **The stewardship maturity scores contradict RRS-2 (high).**
  - GPCP Daily v1.3 ([DSMR-00163](https://repository.library.noaa.gov/view/noaa/34101/noaa_34101_DS1.pdf)) and PERSIANN-CDR v1r1 ([DSMR-00012](https://repository.library.noaa.gov/view/noaa/33336)) were both assessed in March 2018 and last modified in 2021. Each scores "Data Integrity - 3.5" out of 5.
  - The justification is word for word the same in both: checksums are "generated at ingest" and "verified when customer orders data". Neither report gives a re-verification schedule.
  - Both reports score Preservability 4.5. Control/Monitoring scores 2.5 for GPCP and 1.5 for PERSIANN.
  - The GPCP report adds "No known external audits of the archive performed at this time."
  - GPCP Daily v1.3 has since been superseded by v3.3. No maturity report for v3.3 was found.
- **NCEI's CoreTrustSeal application, read in full for the first time here, falls short of RRS-2 (high).** It was read through [DataverseNL](https://dataverse.nl/api/access/datafile/469675); it uses the 2020–2022 requirements and the certification runs to 29 January 2028. Under R9 it says:
  - an MD5 checksum is held in the catalog, and "Any time a file is pulled either from primary or offsite, the file's checksum is checked";
  - scripts "on a routine basis" compare file *sizes* between the primary and offsite copies;
  - tapes are refreshed "every few years".
  - Size comparisons are not checksum checks, and no frequency is given. Both reviewers rated R9 at level 4 without comment.
  - The procedure behind all this (SOP 60-6-015) is not public.
- **Nothing published says the cloud (NODD) copies are checked against NCEI's archive (moderate).**
  - The bucket listings for `noaa-cdr-precip-gpcp-daily-pds` and `noaa-cdr-precip-persiann-pds` show only S3 ETags ([AWS listing](https://noaa-cdr-precip-gpcp-daily-pds.s3.amazonaws.com/?list-type=2&max-keys=5), read through WebFetch).
  - The [AWS Registry entry](https://registry.opendata.aws/noaa-cdr-atmospheric/) and [NCEI's NODD page](https://www.ncei.noaa.gov/products/ncei-data-noaa-open-dissemination-program) say nothing about integrity.
  - The [NODD FAQ](https://www.noaa.gov/big-data-project-frequently-asked-questions) says only that a Data Broker helps "ensure end-to-end data integrity".
  - The one documented check of cloud copies against the archive is for NEXRAD: NCEI publishes a daily inventory with checksums and sizes ([NOAA, 2022](https://repository.library.noaa.gov/view/noaa/46543/noaa_46543_DS1.pdf)).

## Copies (RRS-1: two or more geographically independent sites hold verified copies)

- **Boulder holds archive data, but no source says it holds Asheville's (moderate).**
  - In March 2024, NOAA told its Science Advisory Board that NCEI's archive "resides on-prem in Boulder, CO" (StorNext) and in Asheville (AMS and HPSS). CLASS, "roughly half of its holdings", already had a copy in AWS ([NOAA response to SAB DAARWG, 2024](https://sab.noaa.gov/wp-content/uploads/SAB_Report_March2024_NOAA-Response_DAARWG_Common-Cloud-Framework.pdf), read from a 2024 Wayback copy).
  - The CoreTrustSeal application (R15) says "A copy of NCEI-CO archive is stored in two separate and geographically dispersed locations." That supports RRS-1 for Boulder's holdings only.
  - For Asheville, the same application (R9) describes two tape copies, with the offsite one "several kilometers away". That is consistent with pt9's 12.5 miles, and it is not geographically independent.
  - Both CDRs are "Archived at NOAA NCEI-NC" (the Asheville site), per their maturity reports. No source names a copy of them in Boulder, Silver Spring or Stennis.
  - After Hurricane Helene, "Data loss was mitigated with support from NCEI's Boulder, CO location" ([State of the Services FY25 Q1](https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf)). That shows Boulder can serve as a fallback, but not what it holds.
- **GPCP Daily already has an archive copy in NCEI's own cloud bucket (low).** The [NCEI archive S3 listing](https://archive.data.noaa.gov/climatedatarecords#UMD_ESSIC/GPCP/Daily/GPCP-D-CDR_01B-35/) (bucket `climatedatarecords`, linked from data.gov) shows year folders 1998–2025. This copy is separate from the NODD bucket. Only the top folder could be listed, so its region, the number of copies and any checksum files were not seen. The version behind the folder name "CDR_01B-35" is also unconfirmed.
- **The AWS move: nothing is published on the copies (moderate).**
  - NESDIS is moving all Asheville and Boulder data to AWS "through Spring 2027", as a "lift and shift" ([NCEI cloud migration](https://www.ncei.noaa.gov/news/cloud-migration); [FAQ](https://www.ncei.noaa.gov/news/cloud-migration-FAQ)).
  - No source gives the AWS regions, the storage class, the number of copies, or whether the on-premises tapes are kept or retired. The [FY23 NCCF summary](https://www.nesdis.noaa.gov/s3dl?path=%2Fs3%2F2024-04%2FFY23-NCCF-Summary-and-Future-Plans.pdf) is silent on these as well.
  - The SAB's 2022 working group asked whether NOAA would keep "an on-premises disaster recovery copy of data just in case, for example on tape" ([SAB DAARWG report](https://repository.library.noaa.gov/view/noaa/61393/noaa_61393_DS1.pdf)). NOAA's 2024 response and slides do not answer it.
- **OIG's single-region recommendation is closed, but how it was closed is not published (high).**
  - It is recommendation 11 of [OIG-24-034-A](https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf).
  - OIG found the NCCF "resides in a single region" and runs in two facilities within it, with disruptions "roughly every 2 years". It asked NESDIS to add a multi-region option to its analysis of alternatives and to document a risk- and cost-based decision. NOAA's target date was September 2025.
  - [Oversight.gov](https://www.oversight.gov/reports/audit/lack-program-management-controls-and-attention-it-security-threatens-success-noaas-10) lists it "Closed" (read from a December 2025 Wayback copy), with no date or action. Two gap-pass searches found no closing document.
  - **Conflict, unresolved:** a [2021 NOAA briefing on the cloud-archive prototype](https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-51/3.Thursday/2021.04.22_NOAA_Data_Preservation-Stewardship.pdf) described "cross-region replication", but OIG found a single region in 2024. They differ in date and scope: a prototype design against the production platform. Which describes production now is not published.

## Track record (RRS-5: survived a major disruption without data loss; RRS-3: DR plan tested in the past 2 years)

- **No data loss is reported, but none is ruled out (moderate).** The [State of the Services](https://www.ncei.noaa.gov/services/state-of-the-services) reports read were FY25 Q1–Q3, the [FY25 annual](https://www.ncei.noaa.gov/sites/default/files/2025-12/SOS_FY2025_Executive_Summary.pdf) and the [FY26 annual](https://www.ncei.noaa.gov/sites/default/files/2026-10/SOS_FY2026_Executive_Summary.pdf). None gives a holdings volume, a statement that no data were lost, or a DR test. FY25 Q4, FY26 Q2 and FY26 Q3 are not posted.
  - **2015 merger:** NCDC said "no products or services are currently slated to be cut or reduced" ([NCDC, 2015](https://www.ncdc.noaa.gov/news/coming-soon-national-centers-environmental-information), Wayback copy). No loss or backlog was reported. Holdings were 28.6 PB by 2017 ([Hammer, AMS 2017](https://www.ncei.noaa.gov/sites/default/files/greg-hammer-ams-2017-presentation-becoming-the-national-centers-for-environmental-information.pdf)).
  - **Helene (27 September 2024):** the Asheville headquarters lost power, water and communications. Ingest was restored by 11 December and "92% of the ingest backlog was recovered". The other 8% is not accounted for, which weakens RRS-5.
  - **2025:** three products were decommissioned. For those, "Existing data … will remain open and available" ([FY25 Q3](https://www.ncei.noaa.gov/sites/default/files/2025-08/FY2025%20Q3%20SOS%20Executive%20Summary.pdf)). The only staffing mention is "recent staff changes".
  - **2026 migration:** the [FAQ](https://www.ncei.noaa.gov/news/cloud-migration-FAQ) says "No datasets will be retired as part of the cloud migration", but adds that "several NCEI datasets were retired over the last 18 months", without naming them. Separately, a severity-high [NCEI alert](https://www.ncei.noaa.gov/alerts) (16–30 Nov 2026) says "Many access portals, interactive maps, and data folders are currently unavailable" and to "Expect delayed data archival". That is a disruption still under way, with no statement on loss.
  - In June 2026, NCEI staff described a "Multi-Year Backlog" for IOOS ocean data ([IOOS DMAC slides](https://cdn.ioos.noaa.gov/attachments/2026/Full%20Stream%20Ahead%2C%20Updates%20to%20NCEI%20Archiving%20of%20IOOS%20Data%20%28Kristen%20Sauby%20and%20Ana%20Krelling%2C%20NOAA%29.pdf)). That covers one data stream, not the CDRs.
  - **Older record (context):** before NCEI existed, [GAO (1991)](https://www.gao.gov/assets/imtec-91-11.pdf) reported "Some irreplaceable data have already been lost". It also found over 230,000 tapes, more than 370 million film records and 76 million paper records stored under poor conditions.
- **RRS-3: nothing is published (high).** The CoreTrustSeal application (R16) describes an Information System Contingency Plan with an annual Business Impact Analysis, daily and weekly off-site backups for WDS data, and COOP plans. The plan "cannot be shared outside the US Government", and no test date or result appears anywhere.

## What it means

Against the statements as worded: RRS-2 is contradicted for both CDRs and for NCEI as a whole. RRS-1 is supported only for Boulder-held and CLASS data, and is not shown for GPCP Daily or PERSIANN-CDR Daily. RRS-3 has no public evidence. RRS-5 is not shown: Helene and 2025 passed with no reported loss, but with an 8% backlog unaccounted for, and the 2026 migration is still in progress. Whether the AWS move brings verified copies in more than one region is the open question that matters most, and NOAA has not published the answer.

## Gaps

- **Not published; NESDIS and NCEI hold these:**
  - the decision that closed OIG recommendation 11, and its date (NESDIS's analysis of alternatives, or OIG's closure memo, by records request);
  - the production AWS regions and storage class, and what happens to the tapes (the NCCF archive design documents);
  - SOP 60-6-015 and the ISCP test results (not public, per NCEI);
  - the FY25 Q4 and FY26 Q2–Q3 State of the Services reports (not posted).
- The archive.data.noaa.gov S3 Explorer copy of GPCP Daily needs a browser. It is one of the pages in `check-by-hand.md`.
- Two hosts were refused by the sandbox (ams.confex.com, and the S3 bucket host); see `sites-to-trust.md`. You can check whether to add either to the sandbox's allowed domains.

## Sources

**NOAA, NESDIS and NCEI**
- [NCEI, State of the Services FY25 Q1, 2025](https://www.ncei.noaa.gov/sites/default/files/2025-01/FY2025%20Q1%20SOS%20Executive%20Summary.pdf)
- [NCEI, State of the Services FY25 Q3, 2025](https://www.ncei.noaa.gov/sites/default/files/2025-08/FY2025%20Q3%20SOS%20Executive%20Summary.pdf)
- [NCEI, State of the Services FY25 Annual, 2025](https://www.ncei.noaa.gov/sites/default/files/2025-12/SOS_FY2025_Executive_Summary.pdf)
- [NCEI, State of the Services FY26 Annual, 2026](https://www.ncei.noaa.gov/sites/default/files/2026-10/SOS_FY2026_Executive_Summary.pdf)
- [NCEI, State of the Services index](https://www.ncei.noaa.gov/services/state-of-the-services)
- [NCEI, Alerts, 2026](https://www.ncei.noaa.gov/alerts)
- [NCEI, Cloud migration, 2026](https://www.ncei.noaa.gov/news/cloud-migration)
- [NCEI, Cloud migration FAQ, 2026](https://www.ncei.noaa.gov/news/cloud-migration-FAQ)
- [NESDIS, DSMR-00163 GPCP Daily maturity report, 2021](https://repository.library.noaa.gov/view/noaa/34101/noaa_34101_DS1.pdf)
- [NESDIS, DSMR-00012 PERSIANN-CDR maturity report, 2021](https://repository.library.noaa.gov/view/noaa/33336)
- [NOAA, Response to SAB DAARWG on the Common Cloud Framework, 2024](https://sab.noaa.gov/wp-content/uploads/SAB_Report_March2024_NOAA-Response_DAARWG_Common-Cloud-Framework.pdf) (read via Wayback)
- [NOAA SAB, DAARWG report on the NCCF, 2022](https://repository.library.noaa.gov/view/noaa/61393/noaa_61393_DS1.pdf)
- [NESDIS, FY23 NCCF Summary and Future Plans, 2024](https://www.nesdis.noaa.gov/s3dl?path=%2Fs3%2F2024-04%2FFY23-NCCF-Summary-and-Future-Plans.pdf)
- [NOAA, Data Preservation and Stewardship (CEOS WGISS-51), 2021](https://ceos.org/document_management/Working_Groups/WGISS/Meetings/WGISS-51/3.Thursday/2021.04.22_NOAA_Data_Preservation-Stewardship.pdf)
- [NOAA, NODD FAQ](https://www.noaa.gov/big-data-project-frequently-asked-questions)
- [NCEI, NODD page](https://www.ncei.noaa.gov/products/ncei-data-noaa-open-dissemination-program)
- [NOAA, NEXRAD Big Data Partnership, 2022](https://repository.library.noaa.gov/view/noaa/46543/noaa_46543_DS1.pdf)
- [NCDC, Coming Soon: NCEI, 2015](https://www.ncdc.noaa.gov/news/coming-soon-national-centers-environmental-information) (read via Wayback)
- [Hammer, Becoming NCEI, AMS 2017](https://www.ncei.noaa.gov/sites/default/files/greg-hammer-ams-2017-presentation-becoming-the-national-centers-for-environmental-information.pdf)
- [IOOS/NCEI, Full Stream Ahead, 2026](https://cdn.ioos.noaa.gov/attachments/2026/Full%20Stream%20Ahead%2C%20Updates%20to%20NCEI%20Archiving%20of%20IOOS%20Data%20%28Kristen%20Sauby%20and%20Ana%20Krelling%2C%20NOAA%29.pdf)

**Oversight and certification**
- [Commerce OIG, OIG-24-034-A, 2024](https://www.oig.doc.gov/wp-content/OIGPublications/NOAANC_2.pdf)
- [Oversight.gov, OIG-24-034-A recommendation 11](https://www.oversight.gov/reports/audit/lack-program-management-controls-and-attention-it-security-threatens-success-noaas-10) (read via Wayback)
- [GAO, IMTEC-91-11, 1991](https://www.gao.gov/assets/imtec-91-11.pdf) (read via Wayback, OCR text)
- [CoreTrustSeal, NCEI assessment 2020–2022 (DataverseNL), 2025](https://dataverse.nl/api/access/datafile/469675)

**Cloud provider**
- [NCEI, archive S3 listing for GPCP Daily (climatedatarecords bucket), 2026](https://archive.data.noaa.gov/climatedatarecords#UMD_ESSIC/GPCP/Daily/GPCP-D-CDR_01B-35/) (read in the browser)
- [AWS, Registry of Open Data: NOAA CDR Atmospheric](https://registry.opendata.aws/noaa-cdr-atmospheric/)
- [AWS, S3 listing of noaa-cdr-precip-gpcp-daily-pds](https://noaa-cdr-precip-gpcp-daily-pds.s3.amazonaws.com/?list-type=2&max-keys=5) (read via WebFetch)
- [AWS, S3 listing of noaa-cdr-precip-persiann-pds](https://noaa-cdr-precip-persiann-pds.s3.amazonaws.com/?list-type=2&max-keys=5) (read via WebFetch)

Saved in [`web_search_results/2026-11-23_ncei-gpcp-persiann-resilience/`](./): this answer, `method.md`, `research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
