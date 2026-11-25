# Satellites and sensors behind GPCP Daily, with contribution dates

**Direct answer.** The two families draw on different satellites.
- **1DD V1.3 (Oct 1996 to present)** uses three satellite inputs directly, plus the GPCP Monthly V2.3 it is scaled to:
  - SSM/I on DMSP F13 (Oct 1996–Dec 2008), then SSMIS on DMSP F17 alone (Jan 2009 to present);
  - TOVS on unnumbered NOAA polar orbiters (Oct 1996–Dec 2002), then AIRS on Aqua (1 Jan 2003 to present);
  - geostationary IR from GOES, GMS/MTSAT and Meteosat, gathered by CPC, with AVHRR infrared gap-fill. No GPCP document numbers these geostationary satellites or dates them.
- **V3.x Daily (V3.3: Jan 1998–Dec 2025; V3.2: Jun 2000–Sep 2021)** takes:
  - TOVS (to Aug 2002) and AIRS (Sep 2002–Dec 2025) directly;
  - through IMERG, about 30 microwave satellites, each with its own dates: TRMM, GPM Core, DMSP F11–F19, Aqua AMSR-E, GCOM-W1, NOAA-15 to -21, MetOp-A/B/C, Suomi NPP and, in V3.2 only, Megha-Tropiques;
  - geostationary IR from GridSat-B1 (1998 to 6 Feb 2000, then CPC merged IR);
  - through the V3.x Monthly it is scaled to, F13 and F17 again, plus GridSat-B1's geostationary satellites (by way of PERSIANN-CDR), including FY-2C and FY-2E.

Confidence: **high** for the 1DD and V3.x direct inputs and the IMERG microwave dates, which come from algorithm documents and file metadata. **Moderate** for the geostationary satellites and their dates, which are given by year or only in sampled file headers. **Low** for which NOAA satellites carried TOVS.

## How satellites reach GPCP Daily

| Route | 1DD V1.3 | V3.2 / V3.3 Daily |
|---|---|---|
| Direct | SSM/I or SSMIS Tb (RSS CDR at NCEI), TOVS or AIRS, CPC 3-hourly geo-IR histograms (TMPI, 40°N–S) | TOVS or AIRS daily estimates, IMERG Final (Late for Oct–Dec 2025), within 55°N–S |
| Monthly it is scaled to | GPCP Monthly V2.3 | GPCP Monthly V3.2 / V3.3 |
| IMERG | not used | V06 for V3.2, V07 for V3.3 |
| CPC merged IR | through TMPI's IR (CPC histograms, not the 4-km product) | through IMERG from Feb 2000 |
| GridSat-B1 | not used | through IMERG from 1998 to 6 Feb 2000; through the Monthly via PERSIANN-CDR, 1983 on |

The routes come from the 1DD C-ATBD ([NOAA NCEI, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)), the V3.3 Daily ATBD ([NASA GES DISC](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)) and the V3.3 Monthly ATBD ([NASA GES DISC, 2026](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Monthly.pdf)). The V3.3 Daily ATBD states: "No primary sensor data are used in the V3.3 Daily".

## 1DD V1.3: satellites and dates

| Satellite | Sensor | Route | In 1DD |
|---|---|---|---|
| DMSP F13 | SSM/I | direct, and via Monthly V2.3 | Oct 1996 – Dec 2008 |
| DMSP F17 | SSMIS | direct, and via Monthly V2.3 | Jan 2009 – present (files to 2026-08-31) |
| NOAA polar orbiters (unnumbered) | TOVS (HIRS2/MSU) | direct, and via V2.3 | Oct 1996 – Dec 2002 (two satellites to Feb 1999, then one) |
| Aqua | AIRS (IR-only after the AMSU failure in late 2016) | direct, and via V2.3 | 1 Jan 2003 – present |
| GOES, GMS (then MTSAT), Meteosat | Imager IR (~10.7 µm) | direct (TMPI), and via V2.3 (GPI) | Oct 1996 – present; satellite numbers not given |
| Meteosat-5 (Indian Ocean) | IR | direct and via V2.3 | from 06 UTC 16 Jun 1998 |
| NOAA polar orbiters (unnumbered) | AVHRR IR (leo-IR GPI fill) | direct and via V2.3 | dates not given |

Sources: the C-ATBD's Table 1 ("F13: 1996 to 2008"; SSMIS "data only from F17") ([NCEI, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)). The file attributes in nine 1DD V1.3 files, sampled from 1996-10-01 to 2026-08-31, name the platforms and sensors, never the satellite numbers. They switch from SSMI to SSMIS on 2009-01-01, and from TIROS/TOVS to Aqua/AIRS on 2003-01-01 ([NCEI files](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2002/gpcp_v01r03_daily_d20021231_c20170530.nc)). The obs4MIPs technical note confirms "F13 SSMI and F17 SSMIS" and the "switch to AIRS in January 2003" ([NASA, 2018](https://esgf.nccs.nasa.gov/esgdoc/GPCP_precip_1DD-V1.3_TechNote_180510.pdf)).

**Through Monthly V2.3, inside the 1DD period:** the same F13, F17, TOVS, AIRS and geo-IR. V2.3's other satellites predate Oct 1996, so they never reach the 1DD: SSM/I F08 (Jul 1987–Dec 1991), F11 (Jan 1992–May 1995), and OPI from TIROS-N and NOAA-6, -7 and -9, used only before 1986 ([NCEI V2.3 C-ATBD, 2016](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-monthly/doc/CDPR-ATBD-0848%20Rev%201%20Precipitation%20-%20GPCP%20Monthly%20C-ATBD%20(01B-34)%20(DSR-1083).pdf)). **High.**

## V3.x Daily: direct inputs and the V3.x Monthly

| Satellite | Sensor | Route | In V3.3 Daily (V3.2 Daily where different) |
|---|---|---|---|
| NOAA polar orbiters (only NOAA-11 named) | TOVS | direct, and via Monthly | Jan 1998 – Aug 2002 (V3.2: Jun 2000 – Aug 2002); one satellite from Mar 1999 |
| Aqua | AIRS IR-only V6 | direct, and via Monthly | Sep 2002 – Dec 2025 |
| DMSP F13 | SSM/I | via Monthly | Jan 1998 – Dec 2008 (Monthly: May 1995 – Dec 2008) |
| DMSP F17 | SSMIS | via Monthly | Jan 2009 – Dec 2025 (F17 only) |
| GridSat-B1 geostationary satellites | IR window | via Monthly (PERSIANN-CDR, 60°N–S) | 1998 – 2025 (Monthly from 1983) |

Sources: [V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf), [V3.3 Monthly ATBD, Table 1](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Monthly.pdf), [V3.2 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf), and the CMR records ([NASA CMR](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPCPDAY&provider=GES_DISC)): V3.3 Daily runs 1998-01-01 to 2025-12-31, V3.2 Daily 2000-06-01 to 2021-09-30.
- **F08 is not used in V3.x:** "significant problems" prevent GPROF from using it.
- **Undated lists:** the CMR records list DMSP, NOAA POES, Aqua, GOES-15/16, Meteosat, GMS, MTSAT-1R/2 and Himawari-8 without dates. They don't list GPM, TRMM or FY-2, though IMERG and GridSat bring those in.

**High.**

## Through IMERG (V3.x Daily only)

V3.2 uses IMERG V06 (with PERSIANN-CCS IR); V3.3 uses IMERG V07 (with PDIR IR). The table gives IMERG V07's periods of record, clipped to the years each V3.x version covers (V3.3 from Jan 1998, V3.2 from Jun 2000). They come from the V07 Technical Documentation's day-level tables ([NASA PPS, 2023](https://arthurhou.pps.eosdis.nasa.gov/Documents/IMERG_TechnicalDocumentation_final.pdf)) and the V07 ATBD ([NASA, 2026](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf)). IMERG V07 Final ends in September 2025, so V3.3 used IMERG V07 Late for Oct–Dec 2025.

| Satellite | Sensor | In IMERG V07 (V3.3 Daily) | Mission life where it differs |
|---|---|---|---|
| TRMM | TMI; PR (combined) | TMI Jan 1998 – Apr 2015; PR useful to 7 Oct 2014 (plus 12 Feb – 1 Apr 2015) | launched 27 Nov 1997 |
| GPM Core | GMI; DPR (combined) | GMI from Mar 2014, DPR-GMI from Apr 2014, to Sep 2025 | launched 27 Feb 2014 |
| DMSP F11 | SSM/I | 1 Jan 1998 – 16 May 2000 (V07 only) | — |
| DMSP F13 | SSM/I | 1 Jan 1998 – 30 Nov 2009 | — |
| DMSP F14 | SSM/I | 1 Jan 1998 – 23 Aug 2008 | — |
| DMSP F15 | SSM/I | 23 Feb 2000 – 14 Aug 2006 (RADCAL beacon) | flew to about 2020 |
| DMSP F16 | SSMIS | 20 Nov 2005 – "ongoing" | launched Oct 2003 |
| DMSP F17 | SSMIS | 19 Mar 2008 – "ongoing" | launched Nov 2006 |
| DMSP F18 | SSMIS | 8 Mar 2010 – "ongoing" | — |
| DMSP F19 | SSMIS | 1 Dec 2014 – 11 Feb 2016 | — |
| Aqua | AMSR-E | 19 Jun 2002 – 3 Oct 2011 | — |
| GCOM-W1 | AMSR2 | from Jun or Jul 2012 (documents differ) | AMSR2 start 10 Aug 2012 in OSCAR |
| NOAA-15 | AMSU-B | 1 Jan 2000 – 14 Sep 2010 | data from 26 Oct 1998, unusable (RFI) |
| NOAA-16 | AMSU-B | 4 Oct 2000 – 30 Apr 2010 (last used) | — |
| NOAA-17 | AMSU-B | 28 Jun 2002 – 17 Dec 2009 | — |
| NOAA-18 | MHS | 25 May 2005 – 20 Oct 2018 | — |
| NOAA-19 | MHS | 25 Feb 2009 – end disputed (2019 to 2023) | products stopped 16 Jun 2025; decommissioned 13 Aug 2025 |
| MetOp-A | MHS | 5 Dec 2006 – 5 Dec 2019 (Final Run) | retired 15 Nov 2021 |
| MetOp-B | MHS | 1 Apr 2013 – ongoing | — |
| MetOp-C | MHS | 10 Nov 2019 – ongoing | — |
| Suomi NPP | ATMS | 10 Dec 2011 – ongoing | retired 1 Sep 2026; EOL 1 Nov 2026 |
| NOAA-20 | ATMS | 29 Nov 2017 – ongoing | — |
| NOAA-21 | ATMS | 1 Feb 2023 (Table 6) or 14 Jun 2023 (Early/Late runs) – ongoing | launched 10 Nov 2022 |
| Megha-Tropiques | SAPHIR | V06 only (so V3.2): 13 Oct 2011 – 15 Dec 2018, 27 Jun 2019 – 23 Mar 2022; "not used in V07" | — |

Mission lives: [WMO OSCAR](https://space.oscar.wmo.int/satellites/view/snpp) pages for SNPP, [NOAA-19](https://space.oscar.wmo.int/satellites/view/noaa_19), [MetOp-A](https://space.oscar.wmo.int/satellites/view/metop_a), [TRMM](https://space.oscar.wmo.int/satellites/view/trmm) and [GCOM-W](https://space.oscar.wmo.int/satellites/view/gcom_w), and the [SSM/I instrument page](https://space.oscar.wmo.int/instruments/view/ssm_i).
- **"Ongoing" end dates.** The documents give bracketed estimated end dates; IMERG V07 Final itself stops at Sep 2025. FNMOC planned to cut the operational SSMIS flow on 30 Jun 2025, which "would suspend the use of F16, F17, and F18" ([NASA GPM](https://gpm.nasa.gov/data/news/end-ssmis-data-coming-gpm-near-real-time-products)).
- **V3.2 (IMERG V06)** uses the same list from Jun 2000, without F11, and with SAPHIR ([IMERG V06 doc, 2020](https://gpm.nasa.gov/sites/default/files/2020-10/IMERG_doc_201006.pdf)).

**High** for the start dates; **moderate** for the end dates.

## Geostationary satellites

- **CPC merged 4-km IR**, IMERG's IR source from Feb 2000 (V3.2 for its whole record, V3.3 from 6 Feb 2000). CPC's Table 12 gives the satellites by year only ([CPC via GES DISC, 2025](https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/CPC-4kmIR-Sats.pdf)):
  - Japan position: GMS-5 (1998–2002), GOES-9 (2003–), MTSAT-1R (2005–), MTSAT-2 (from 1 Jul 2010 per IMERG), Himawari-8 (2015), Himawari-9 (2025).
  - GOES-West: GOES-10, -11 (2006), -15 (2011), -17 (2019), -18 (2023).
  - GOES-East: GOES-8, -12 (2003), -13 (2010), -16 (2017); GOES-19 is placed under West in 2025.
  - Europe: Meteosat-7, then MSG-1 (2004), MSG-2 (2007), MSG-3 (2012), MSG-4 (2019), MSG-3 again (2023).
  - Indian Ocean: Meteosat-5 (1998–), Meteosat-7 (2007), MSG-1 (2017), MSG-2 (2022).
  - No FY-2 or INSAT. **Moderate.**
- **GridSat-B1 inside IMERG V07 (V3.3 only, 1998 to 6 Feb 2000):** file headers list GMS-5, GOES-8, GOES-9, GOES-10, Meteosat-5 (from mid-1998), Meteosat-6 (early 1998) and Meteosat-7 ([NCEI GridSat headers](https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/1998/GRIDSAT-B1.1998.01.01.12.v02r01.nc.das)).
- **GridSat-B1 through the V3.x Monthly (PERSIANN-CDR), Jan 1998 to Dec 2025.** PERSIANN-CDR files from 1983 to 2026 list GridSat-B1 files as their sources ([NCEI ERDDAP](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.das)). Satellites, with the first and last header in which each was found (the samples are 1 Jan and 1 Jul; [NCEI](https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/)):
  - GOES: GOES-8 to 2003, GOES-9 to 2005, GOES-10 1999–2011, GOES-11 2006–2011, GOES-12 2003–2013, GOES-13 2010–2018, GOES-14 2012–2013, GOES-15 2012–2020, GOES-16 2018–2025, GOES-17 2019–2023, GOES-18 2023–, GOES-19 2025–.
  - Meteosat: Meteosat-5 to 2007, Meteosat-6 to Jan 1998, Meteosat-7 1998–2017, Meteosat-8 2005–2022, Meteosat-9 2007–, Meteosat-10 2013–, Meteosat-11 2018–2023.
  - Japan: GMS-5 to 2003, MTSAT-1R 2005–2015, Himawari-8 2015–2022, Himawari-9 2023–.
  - China: FY-2C 2005–2011, FY-2E (Oct 2012 sample).
  - Satellites that appear only before 1998 (GOES-1, -5, -6, -7; Meteosat-2 to -4; GMS-1 to -4) reach the V3.x Monthly but not V3.x Daily.
  - **Moderate:** these are sampled headers, not documented dates.
- **1DD V1.3:** CPC's GPCP histogram data set. The C-ATBD names "GOES, GMS, MTSat and Meteosat", and the files say only "GOES, GMS, METEOSAT". CPC's page lists the operators as JMA, EUMETSAT, IMD and NOAA ([CPC](https://www.cpc.ncep.noaa.gov/products/global_precip/html/wpage.gspdc.shtml)). **Listed without dates.**

## Overlaps and single-satellite periods

- **The 1DD has one satellite of each kind throughout:**
  - one microwave imager at a time, F13 then F17, with no overlap;
  - one sounder at a time: two TOVS satellites to Feb 1999, then one TOVS, then Aqua AIRS alone since 2003;
  - so it has relied on F17 SSMIS alone since Jan 2009 and on Aqua AIRS alone since 2003.
- **V3.x direct and Monthly inputs follow the same pattern:** F13 alone (to Dec 2008), then F17 alone; one TOVS satellite Mar 1999–Aug 2002; Aqua alone from Sep 2002 to Dec 2025.
- **IMERG gives V3.x many overlapping satellites.**
  - 1998–2000: TRMM with F11/F13/F14 (and F15 from Feb 2000) plus NOAA-15 from 2000.
  - About 2010–2014: TRMM, F16–F18, AMSR-E (to Oct 2011), AMSR2, four to five MHS, and SNPP ATMS.
  - About 2023–2025: GPM, F16–F18, AMSR2, MetOp-B/-C, NOAA-19 (per the 2026 ATBD), and ATMS on SNPP, NOAA-20 and NOAA-21.
- **Only one precipitation radar at a time:** TRMM PR (to 2014/15), then GPM DPR (2014–). TRMM and GPM overlapped from Mar 2014 to Apr 2015.
  - TRMM PR had a gap from an electronics failure, 29 May to 19 Jun 2009.
  - IMERG V07 Final's TRMM-era processing runs to 2014-05-31, and its GPM era starts 2014-06-01 ([IMERG V07 tech doc, Table 13](https://arthurhou.pps.eosdis.nasa.gov/Documents/IMERG_TechnicalDocumentation_final.pdf)).
- **Sounder gaps in V3.3 Daily:** TOVS was "partially denied for the period 10-18 September 2001". On days with no TOVS or AIRS data, areas outside 55°N–S are missing, for example 1–18 Nov 2003 ([V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)).
- **Geostationary handovers in IMERG's IR**, by date:
  - GMS-5 to GOES-9 at 01 UTC on 22 May 2003;
  - MTSAT-1R from 17 Nov 2005;
  - MTSAT-2 from 1 Jul 2010;
  - Himawari-8 from 02 UTC on 7 Jul 2015;
  - Meteosat-8 replaced Meteosat-7 on 1 Feb 2017.
- **F17's 37V channel** was set to missing in IMERG for 5 Apr – 18 May 2016 and from 9 Mar 2017 on. That is one channel, not the satellite.
- **Geostationary:** one satellite per position, with handovers. The Indian Ocean had no coverage before Meteosat-5 (16 Jun 1998); the 1DD filled it with AVHRR leo-IR. CPC's record has a MTSAT-1R gap from 17 Nov 2005 to 22 Mar 2006.

## Conflicting dates, and why

1. **When AIRS replaced TOVS.** The cause is versions.
   - 1DD V1.2 and Monthly V2.2 used TOVS through Apr 2005.
   - 1DD V1.3 and V2.3 switch on 1 Jan 2003 ([obs4MIPs note](https://esgf.nccs.nasa.gov/esgdoc/GPCP_precip_1DD-V1.3_TechNote_180510.pdf); [Adler et al., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6043897/); the files).
   - V3.x switches in Sep 2002.
   - The V2.3 C-ATBD text still says "2005", carried over from V2.2.
   - AIRS "available" in May 2002 (C-ATBD) and from Aug 2002 (OSCAR) refer to availability, not first use.
2. **The single TOVS satellite.** It starts in March 1999 in the V3.3 Daily ATBD and in February 1999 (27 Feb) in the Monthly ATBD. The Path A README has NOAA-11 stopping in Dec 1998. Unresolved; the dates are weeks apart.
3. **F13.** GPCP ATBDs say it "failed in September 2009"; OSCAR has its tape recorder failing on 19 Nov 2009; IMERG uses it to 30 Nov 2009. GPCP had stopped using F13 in Dec 2008 in any case. Its start in the Monthly is June 1995 (V2.3) against May 1995 (V3.3), both before the daily records.
4. **IMERG end dates move between editions** because they are estimates. NOAA-19 MHS ends in Sep 2019 (V06), "current" (2023) or [Dec 2023] (2026). MetOp-A's Final Run use stopped after 5 Dec 2019 (change log), though its Table 8 says 30 Nov 2021. NOAA-21 starts in Feb or Jun 2023, AMSR2 in Jun or Jul 2012. The change log's dated entries are the most specific.
5. **GridSat to CPC IR:** "6 February 2000" (V3.3 ATBD) against CPC's uniform record from 17 Feb 2000. The ATBD date is the producer's.
   - CPC extended its merged IR back to 1 Jan 1998. CPC's own document gives the month as April 2025 ([CPC, 2025](https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/CPC-4kmIR-Sats.pdf)); the [Earthdata GPM_MERGIR page](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpm-mergir-1) says June 2025. I rely on CPC's date.
   - No document says whether IMERG or GPCP uses the 1998–2000 part of CPC's record; IMERG V07 used GridSat for that period.
6. **FY-2:** an obs4MIPs note says the Chinese satellites were not used in GridSat, but GridSat's file headers name FY-2C and FY-2E ([obs4MIPs, 2016](https://ncics.org/ncics/pdfs/obs4MIPs/GriddedSatelliteB1FCDR-MonthlyMeans_technical-note_final.pdf)). The file metadata wins.
7. **Smaller inconsistencies inside single documents.** These were found by the checking pass:
   - The 1DD C-ATBD gives TOVS as "March 1999 – December 2002" in one place and "TOVS data are used for 1999 – 2002" in another, though the record starts in Oct 1996.
   - The IMERG V07 tech doc gives SNPP ATMS as "since 28 October 2011" (launch) in its text and from 10 Dec 2011 (first use) in its table.
   - Its summary table gives bracketed end dates for F16/F17/F18 ([Dec 24], [Dec 25], [Mar 26]) where the main table says "ongoing".
   - An Earthdata IMERG V07 catalog snippet still says "June 2000 to the present", which is stale against the 1998 extension.
8. **V3.3's end:** "paused at March 2024" (release notes), "September 2024" (Earthdata) and 1998–2024 (EGU26) all predate the May 2025 extension. The CMR records and the ATBDs run to 2025-12-31.

## Gaps

- **TOVS satellites.** No GPCP document names the NOAA satellites behind TOVS (only NOAA-11, for its failure). The TOVS Path A README lists NOAA-10/-11/-12/-14 periods but doesn't tie them to GPCP. The AVHRR leo-IR fill satellites aren't named either. GPCP's team at NASA GSFC holds this; ask gpcp_contacts@noaa.gov.
- **1DD geostationary satellites.** Their numbers and dates are not documented. CPC holds the histogram records.
- **1DD's SSMIS feed.** Which feed 1DD has used since the RSS SSMIS CDR ended in 2023, and after FNMOC's 2025 change, is not documented. Files still name DMSP/SSMIS through 2026-08-31.
- **V3.x file attributes.** The V3.x files' "Source" attribute values were not read (Earthdata login).
- **Unread paper.** Huffman et al. 2023 (J. Climate) returned HTTP 403; only its abstract was read.
- **The token budget ended the research**, at 09:22, not the evidence running out. The research subagents hit their token share at 09:11, so no follow-up subagent was sent. The DuckDuckGo gap pass ran only 2 queries.
- **Pages to check by hand.** `check-by-hand.md` lists 3 pages.
- **Hosts refused.** The sandbox refused 3 hosts, listed in `sites-to-trust.md`; you can decide whether to add any to the allowed domains.

## Sources

- [NOAA NCEI, GPCP Daily C-ATBD CDRP-ATBD-0913, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Daily/AlgorithmDescription_01B-35.pdf)
- [NOAA NCEI, GPCP 1DD V1.3 netCDF files (sampled headers)](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/2002/gpcp_v01r03_daily_d20021231_c20170530.nc)
- [NOAA NCEI, GPCP Monthly C-ATBD CDRP-ATBD-0848 Rev. 1, 2016](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-monthly/doc/CDPR-ATBD-0848%20Rev%201%20Precipitation%20-%20GPCP%20Monthly%20C-ATBD%20(01B-34)%20(DSR-1083).pdf)
- [Adler et al., GPCP Monthly V2.3, Atmosphere, 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6043897/)
- [NASA, GPCP 1DD V1.3 Technical Note (obs4MIPs), 2018](https://esgf.nccs.nasa.gov/esgdoc/GPCP_precip_1DD-V1.3_TechNote_180510.pdf)
- [NASA GES DISC, GPCP V3.3 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Daily.pdf)
- [NASA GES DISC, GPCP V3.2 Daily ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf)
- [NASA GES DISC, GPCP V3.3 Monthly ATBD, 2026](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.3_Monthly.pdf)
- [NASA GES DISC, GPCP V3.2 Monthly ATBD](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Monthly.pdf)
- [NASA GES DISC, GPCP V3.3 Release Notes](https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.3.pdf)
- [NASA CMR, GPCPDAY collection records](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPCPDAY&provider=GES_DISC)
- [NASA CMR, GPCPMON collection records](https://cmr.earthdata.nasa.gov/search/collections.umm_json?short_name=GPCPMON&provider=GES_DISC)
- [NASA Earthdata, GPCPMON V3.3 catalog page](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpcpmon-3.3)
- [Copernicus EGU26-5885 abstract, GPCP V3.3](https://meetingorganizer.copernicus.org/EGU26/EGU26-5885.html) (abstract only)
- [Huffman et al., GPCP V3.2, J. Climate, 2023](https://experts.arizona.edu/en/publications/the-new-version-32-global-precipitation-climatology-project-gpcp-/) (abstract only)
- [NASA PPS, IMERG V07 Technical Documentation, 2023](https://arthurhou.pps.eosdis.nasa.gov/Documents/IMERG_TechnicalDocumentation_final.pdf)
- [NASA, IMERG V07 ATBD, 2026](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf)
- [NASA, IMERG V06 Technical Documentation, 2020](https://gpm.nasa.gov/sites/default/files/2020-10/IMERG_doc_201006.pdf)
- [NASA GPM, End of SSMIS data coming to GPM near-real-time products](https://gpm.nasa.gov/data/news/end-ssmis-data-coming-gpm-near-real-time-products)
- [NOAA CPC via GES DISC, CPC Merged 4-km IR satellites, 2025](https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/CPC-4kmIR-Sats.pdf)
- [NOAA CPC, GPCP Geostationary Satellite Precipitation Data Centre](https://www.cpc.ncep.noaa.gov/products/global_precip/html/wpage.gspdc.shtml)
- [NOAA NCEI, GridSat-B1 file headers (THREDDS)](https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/)
- [NOAA NCEI, GridSat-B1 1998-01-01 header](https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/1998/GRIDSAT-B1.1998.01.01.12.v02r01.nc.das)
- [NOAA NCEI, PERSIANN-CDR ERDDAP attributes](https://www.ncei.noaa.gov/erddap/griddap/cdr_persiann_by_time_lon_lat.das)
- [NCICS, GridSat-B1 obs4MIPs technical note, 2016](https://ncics.org/ncics/pdfs/obs4MIPs/GriddedSatelliteB1FCDR-MonthlyMeans_technical-note_final.pdf)
- [NASA GES DISC, TOVS Pathfinder Path A README](https://acdisc.gesdisc.eosdis.nasa.gov/data/TOVS/TOVSAMNE.02/doc/README.TOVS.Pathfinder.PathA.v2.pdf)
- [WMO OSCAR, Suomi NPP](https://space.oscar.wmo.int/satellites/view/snpp)
- [WMO OSCAR, NOAA-19](https://space.oscar.wmo.int/satellites/view/noaa_19)
- [WMO OSCAR, MetOp-A](https://space.oscar.wmo.int/satellites/view/metop_a)
- [WMO OSCAR, TRMM](https://space.oscar.wmo.int/satellites/view/trmm)
- [WMO OSCAR, GCOM-W](https://space.oscar.wmo.int/satellites/view/gcom_w)
- [WMO OSCAR, SSM/I instrument](https://space.oscar.wmo.int/instruments/view/ssm_i)

Saved in [`web_search_results/2026-11-20_gpcp-daily-satellites-pt6/`](./): this answer, `method.md`, `research-record.json`, `check-by-hand.md`, `sites-to-trust.md` and `left-out.md`.
