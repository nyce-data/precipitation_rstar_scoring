No single body does all the work. A small, long-standing team shares it. NASA funds and leads the current V3.x line through its MEaSUREs program, with Ali Behrangi (University of Arizona) as PI and George Huffman's group at NASA Goddard (Code 612, with SSAI contractors) doing the development. The University of Maryland's ESSIC, with Robert Adler as PI, computes the older 1DD V1.3 as a NOAA Climate Data Record for NCEI. GES DISC and NCEI archive and serve the data, and GEWEX/WCRP provides oversight. **Confidence: high** for the roles and people. **Low** for one point: who computes the V3.3 file that NCEI serves. Two official sources disagree on it (see below).

## Two product lines, two arrangements

**1DD V1.3 (1°, Oct 1996 on).**
- It is "currently computed by the University of Maryland and submitted to NCEI" ([NOAA NCEI C-ATBD, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)).
- NCEI's metadata names the processor as "UMD/ESSIC", and lists the dataset as "Ongoing" with monthly updates ([NCEI C00999](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00999), page last modified 2023-08-10).
- NCEI's live product page lists the PI as "Robert Adler, University of MD" ([NCEI, 2026](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily)).
- Continued production "is supported by the NOAA NCEI Climate Data Records (CDR) program" ([Huffman et al. 2023 poster](https://ntrs.nasa.gov/api/citations/20230012664/downloads/20230012664%20Huffman%20G%20poster.pdf)).
- Up to 2016, GPCP was "produced by a consortium of individual scientists". Moving it into the CDR Program was meant to "formalize its production under NOAA's commitment" (C-ATBD). **High.**

**V3.2/V3.3 Daily (0.5°, 1998 on).**
- It was "developed primarily under prior and current projects in the NASA … MEaSUREs program (PI: Ali Behrangi, University of Arizona)" ([V3.3 Daily ATBD, rev. June 2026](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)). MEaSUREs is "managed by Dr. Lucia Tsaoussi" ([README, May 2025](https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.3/doc/README.GPCPV3.3_Daily.pdf)).
- Huffman prepared the ATBD (NASA/GSFC Code 612). His Goddard bio says the V3 datasets "are computed at Goddard and archived in" GES DISC ([NASA GSFC](https://science.gsfc.nasa.gov/sci/bio/george.huffman)).
- NASA's CMR record gives GES DISC the role "ARCHIVER" ([CMR](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPCPDAY&version=3.3)). A 2022 GES DISC poster calls the datasets "archived and distributed at" GES DISC ([NTRS 2022](https://ntrs.nasa.gov/citations/20220018559)).
- No source says GES DISC runs the science processing. **High** for the lead and funding; **moderate** for GES DISC being host only.
- NCEI's V3.3 CDR (C01726, dated 2025-08-05, covering 1998-01-01 on) names Adler as PI, with Gu, Behrangi, Huffman, Bolvin and Nelkin, "and NOAA CDR Program" in the citation ([NCEI C01726](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01726)).

**The conflict over who computes V3.3:**
- NCEI's C01726 record says "The GPCP Daily V3.3 analysis is currently computed by the University of Maryland and submitted to NCEI", on "moderate-sized workstations at the University of Maryland". Its data.gov copy says the same ([data.gov](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-the-global-precipitation-climatology-project-gpcp-daily-ve)).
- NASA's documents put the V3 work at Goddard (the bio quoted above).
- The NCEI sentences repeat the V1.3 record word for word. The V1.3 record even says "GPCP Monthly" in its processing line. So the NCEI text may be boilerplate carried over. Another possibility is that UMD reprocesses NASA's V3.3 for the NOAA CDR.
- **Unresolved.** Asking gpcp_contacts@noaa.gov (the contact on NCEI's page) or Huffman would settle it.

## Who does what

| Institution | Role | Product | Source |
|---|---|---|---|
| NASA MEaSUREs (HQ) | Funds development; V3.2 award 80NSSC19M0006; "funded for 5 more years under the 2022 MEaSUREs" | V3.x, V4 | ATBD; Huffman 2023 poster |
| University of Arizona | MEaSUREs PI (Behrangi); co-authors Song, Kumah; leads V4 | V3.x, V4 | ATBD; UA news 2023 |
| NASA GSFC Code 612 + SSAI | Algorithm development and production (Huffman lead developer; Bolvin, Nelkin) | V3.x; also 1DD development | GSFC bio; README |
| UMD / ESSIC | Computes 1DD V1.3 for NCEI (PI Adler); Gu co-author; produces the Monthly ICDR | V1.3; V3.3 CDR (disputed) | C-ATBD; C00999; C01726 |
| NOAA NCEI (CDR Program) | Funds continued V1.3 production; archives and serves both CDRs; supplies GridSat IR to V3 | V1.3, V3.3 CDR | C-ATBD; poster; release notes |
| NASA GES DISC | Archive and distribution only (role "ARCHIVER"); data-access contact Zhong Liu | V3.x | CMR; README |
| NOAA CPC | Input supplier: geostationary IR "processed and provided by Pingping Xie" | V1.3 | C-ATBD |
| GPCC at DWD | Input supplier: gauges, through the GPCP Monthly; "the in situ component" of GPCP | both, indirectly | GPCC 2022 |
| GEWEX / WCRP (GDAP) | Oversight: GPCP is "under the auspices of" GDAP; GDAP coordinated next-generation development | both | NCEI page; MEaSUREs page |
| NCAR GDEX, Copernicus CDS | Hosts only (redistribute) | both | Part 1 run |

Sources by row are linked in the text above and in the Sources list.

Other inputs:
- **V1.3:** SSM/I and SSMIS brightness temperatures come from NCEI's RSS CDR, and TOVS data "obtained directly from Joel Susskind" (GSFC).
- **V3.3:** the inputs come from GSFC/GPCP (the Monthly), GSFC/SRT (TOVS) and GES DISC (AIRS, IMERG V07).
- **GPCC's role** is supplying gauges. It doesn't compute the daily product ([GPCC products, 2022](https://opendata.dwd.de/climate_environment/GPCC/PDF/GPCC_intro_products_lastversion.pdf)).
- **CPC's role** is documented only for V1.3. V3 replaces the CPC IR with IMERG.

The 2013 "centers" model is no longer described anywhere current ([Sapiano et al., AMS 2013](https://ams.confex.com/ams/93Annual/webprogram/Handout/Paper220154/Sapiano_GPCPcdr_AMS_jan13.pdf)). It had a Merge Center (Huffman, Adler), a Gauge Center (Becker and Schneider at GPCC), microwave centers (Ferraro at NESDIS, Chiu at GMU) and a Geosynchronous Center (Xie at CPC). **Moderate.**

## People and whether they're still active

- **Robert Adler** (UMD/ESSIC senior research scientist; 35 years at GSFC before 2008) is PI of both NCEI CDRs. He "has also led, and is still involved with" GPCP, and co-wrote ESSIC precipitation summaries dated 2026-01-27 and 2026-06-15 ([ESSIC 2026](https://essic.umd.edu/review-of-global-precipitation-for-2025/)). ESSIC's monthly GPCP summaries go on to one dated 2026-11-12, though the list doesn't show who wrote the June–October entries ([ESSIC, May 2026 summary](https://essic.umd.edu/global-precipitation-summary-for-may-2026/)). Active.
- **George Huffman** (NASA GSFC, Chief of Code 612, GPM Project Scientist since 2022) is lead developer of 1DD and V3, the contact for the release notes, and the author of the ATBD's June 2026 revision. Active.
- **Ali Behrangi** (University of Arizona) is MEaSUREs PI on a $3 million NASA award ([UA, 2023](https://has.arizona.edu/news/ali-behrangi-named-principal-investigator-new-3-million-nasa-grant-advance-global)) and serves on GEWEX GDAP. He leads V4 "targeting mid 2027", with Co-Is Huffman, Adler and Chris Funk (UCSB) ([Behrangi et al., IPWG 2026](https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf)). Active.
- **David Bolvin, Eric Nelkin** (SSAI at GSFC Code 612), **Guojun Gu** (UMD), and **Yang Song, Kingsley Kumah** (University of Arizona) are on the 2025–2026 author lists ([EGU26-5885](https://meetingorganizer.copernicus.org/EGU26/EGU26-5885.html); [release notes 2025](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)). Nelkin wrote the May 2025 ATBD revision. Active.
- **Jian-Jian Wang and Mathew Sapiano** (UMD) are 1DD V1.3 collaborators in 2017 (C00999). They are not on any 2025–2026 list; status unknown.
- **Pingping Xie** (CPC), **Andreas Becker and Udo Schneider** (GPCC): no 2024–2026 evidence of GPCP work. GPCC's 2025 gauge analysis names Markus Ziese as head ([DWD GPCC 2025](https://opendata.dwd.de/climate_environment/GPCC/html/gpcc_precipitation_analysis_monthly_v2025_doi_download.html)). GPCC's 2026 team (Rustemeier, Ziese, Schirmeister, Finger, Heller and others) presented its new gauge products, without naming GPCP in the part read ([EMS2026-174](https://meetingorganizer.copernicus.org/EMS2026/EMS2026-174.html), abstract).
- **The MEaSUREs PI conflict is settled as a difference in scope.** NASA's Earthdata page names "George Huffman, SSAI" as PI ([Earthdata](https://www.earthdata.nasa.gov/about/competitive-programs/measures/next-generation-global-precipitation-climatology-project)), but it describes the earlier V3-building award. Behrangi is PI of the 2022 award.

**Confidence: high** for the active core of 8.

## Staffing and computing

- **Staffing:** no published head count of scientists, programmers or technicians was found. The nearest evidence is the author lists:
  - 7 on the V3.3 release notes and ATBD;
  - 8 on the 2026 EGU and IPWG talks;
  - 6 named on NCEI's V3.3 CDR, plus "NOAA CDR Program";
  - the PI plus 5 collaborators on the 1DD V1.3 CDR.

  Huffman's bio cites a 2022 Goddard Group Award to the "GPCP Development Team", with no member list. **Moderate.**
- **Computing:**
  - NCEI's metadata says the daily is generated on UMD workstations (disputed for V3.3, above).
  - GES DISC serves V3.3 from NASA Earthdata Cloud, in AWS us-west-2 (CMR).
  - NOAA serves the CDR from NCEI and from the NODD bucket `noaa-cdr-precip-gpcp-daily-pds` in AWS us-east-1 ([AWS Open Data listing](https://aws.amazon.com/marketplace/pp/prodview-mmz4ve4u5cdui)). The listing doesn't say which version that bucket holds.
  - No source names the NASA-side production machines (Code 612 systems or NCCS). **Moderate.**

## Gaps

- **Who computes V3.3:** UMD or Goddard, for NCEI's CDR copy. Ask gpcp_contacts@noaa.gov or Huffman. Not found published.
- **Where V3.3 production is paused:** the release notes (2025-03-11) say March 2024, while NASA's Open Data page says September 2024. Part 1 found granules to 2025-12-31, so both statements are out of date.
- **Missing figures:** no staff count exists in public sources. No NESDIS role in either daily product was found. GSFC's current part in routine V1.3 production isn't stated after 2017.
- **Unread pages:** GPCC's IPWG12 talk is unread (the sandbox refused the host, WebFetch got a 404, and there is no Wayback copy). GEWEX pages were read only through WebFetch.
- **Not run:** the checking subagent (standard tier).

## Sources

- [NOAA NCEI, C-ATBD GPCP Daily CDR (CDRP-ATBD-0913), 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)
- [NOAA NCEI, ISO metadata C00999 (1DD V1.3), 2017, Wayback copy](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC00999)
- [NOAA NCEI, ISO metadata C01726 (V3.3 Daily CDR), 2025](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01726)
- [NOAA NCEI, Precipitation – GPCP Daily CDR product page, 2026](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily)
- [data.gov, NOAA CDR GPCP Daily V3.3](https://catalog.data.gov/dataset/noaa-climate-data-record-cdr-of-the-global-precipitation-climatology-project-gpcp-daily-ve)
- [NOAA NCEI, GPCP Clearinghouse](https://www.ncei.noaa.gov/products/global-precipitation-climatology-project)
- [NASA GES DISC, ATBD for GPCP V3.3 Daily, rev. 2026-06-12](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)
- [NASA GES DISC, README for GPCP V3.3 Daily, 2025](https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.3/doc/README.GPCPV3.3_Daily.pdf)
- [Huffman et al., GPCP V3.3 Release Notes, 2025](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)
- [NASA CMR, GPCPDAY 3.3 collection metadata](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPCPDAY&version=3.3)
- [NASA Open Data Portal, GPCPDAY V3.3](https://data.nasa.gov/dataset/gpcp-precipitation-level-3-daily-0-5-degree-v3-3-gpcpday-at-ges-disc-ccae7)
- [NASA Earthdata, Next-Generation GPCP (MEaSUREs project page)](https://www.earthdata.nasa.gov/about/competitive-programs/measures/next-generation-global-precipitation-climatology-project)
- [NASA Earthdata, High Latitude Improvement of GPCP (MEaSUREs 2017)](https://www.earthdata.nasa.gov/about/competitive-programs/measures/long-term-gpcp-precipitation)
- [NASA GSFC, George J. Huffman bio](https://science.gsfc.nasa.gov/sci/bio/george.huffman)
- [Huffman et al., GPCP V3.2 poster, NTRS 20230012664, 2023](https://ntrs.nasa.gov/api/citations/20230012664/downloads/20230012664%20Huffman%20G%20poster.pdf)
- [Liu et al., GPCP V3.2 at GES DISC, NTRS 20220018559, 2022](https://ntrs.nasa.gov/citations/20220018559)
- [University of Arizona HAS, Behrangi named PI on $3M NASA grant, 2023](https://has.arizona.edu/news/ali-behrangi-named-principal-investigator-new-3-million-nasa-grant-advance-global)
- [Behrangi et al., GPCP V3.3 and V4.0, IPWG 2026](https://ipwg12.imgw.pl/wp-content/uploads/2026/07/S3.4-BEHRANGI-IPWG2026.pdf)
- [Behrangi et al., EGU26-5885, 2026](https://meetingorganizer.copernicus.org/EGU26/EGU26-5885.html) (abstract)
- [Behrangi et al., EGU25-4886, 2025](https://meetingorganizer.copernicus.org/EGU25/EGU25-4886.html) (abstract)
- [ESSIC, Review of Global Precipitation for 2025, 2026](https://essic.umd.edu/review-of-global-precipitation-for-2025/)
- [ESSIC, Global Precipitation Summary for May 2026](https://essic.umd.edu/global-precipitation-summary-for-may-2026/)
- [ESSIC, Global Precipitation](https://essic.umd.edu/globalprecipitation/)
- [Sapiano et al., GPCP CDR poster, AMS 2013](https://ams.confex.com/ams/93Annual/webprogram/Handout/Paper220154/Sapiano_GPCPcdr_AMS_jan13.pdf)
- [DWD GPCC, Global Precipitation Analysis Products of the GPCC, 2022](https://opendata.dwd.de/climate_environment/GPCC/PDF/GPCC_intro_products_lastversion.pdf)
- [Rustemeier et al., GPCC new gridded analyses, EMS2026-174, 2026](https://meetingorganizer.copernicus.org/EMS2026/EMS2026-174.html) (abstract)
- [DWD GPCC, Precipitation Analysis Monthly V2025 DOI page](https://opendata.dwd.de/climate_environment/GPCC/html/gpcc_precipitation_analysis_monthly_v2025_doi_download.html)
- [GEWEX, GDAP Matured Datasets](https://www.gewex.org/panels/gewex-data-and-analysis-panel/gdap-matured-datasets/)
- [GEWEX, Data Sets: GPCP](https://www.gewex.org/data-sets-global-precipitation-climatology-project-gpcp/)
- [CEOS, Deliverable VC-25-13: GPCP v3.3 release](https://deliverables.ceos.org/task_manager/deliverables/890/)
- [AWS Open Data, NOAA Atmospheric CDRs listing](https://aws.amazon.com/marketplace/pp/prodview-mmz4ve4u5cdui)
