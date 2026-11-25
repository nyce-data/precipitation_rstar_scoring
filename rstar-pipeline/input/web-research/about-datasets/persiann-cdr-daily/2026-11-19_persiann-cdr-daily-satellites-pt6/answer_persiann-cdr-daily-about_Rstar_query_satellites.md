# Satellites used in PERSIANN-CDR Daily, with their periods

PERSIANN-CDR Daily (1983–present) gets its satellite data two ways. Directly, it uses infrared images from about 36 geostationary weather satellites: GOES-1 and GOES-5 to -19, Meteosat-2 to -11, GMS-1 to -5, MTSAT-1R/-2, Himawari-8 and -9, and FY-2C/-2E. These come through GridSat-B1. Indirectly, GPCP's monthly analysis, used for bias adjustment, brings in microwave and sounder data from polar orbiters: DMSP F08, F11, F13 (SSM/I) and F17 (SSMIS), NOAA TOVS satellites, Aqua AIRS, and AVHRR on NOAA-7 and NOAA-9 for 1983–85. **Confidence: high** for which satellites are used. **Moderate** for exact start and end dates, because the official tables disagree by days to months and none is a GridSat-B1-specific list.

## How the satellites enter the dataset

- **Direct input: geostationary infrared.** The model's main input is GridSat-B1's infrared-window brightness temperature, gridded from ISCCP B1 data. GPCP monthly precipitation is "Ancillary Data" ([CHRS/NCEI C-ATBD, 2014](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf)).
  - PERSIANN-CDR's own documents name the satellites only by series: GOES, Meteosat, GMS and "the Chinese Fen-yung 2C (FY2) series" (same C-ATBD). No PERSIANN-CDR document lists individual satellites or their dates.
  - Each PERSIANN-CDR daily file lists the eight 3-hourly GridSat-B1 v02r01 files it was built from. For example, the 2011-07-01 file names `GRIDSAT-B1.2011.07.01.00.v02r01.nc` ([NCEI THREDDS header](https://www.ncei.noaa.gov/thredds/dodsC/cdr/persiann/2011/PERSIANN-CDR_v01r01_20110701_c20140523.nc.das)).
  - So the satellites in those GridSat files are the satellites in PERSIANN-CDR. **High.**
- **Where the satellite names come from.** Every GridSat-B1 file names its own satellites in a `Satellite_Name_satid` attribute.
  - I read the headers of 98 files: 1 January and 1 July of each year from 1983 to 2026, plus 12 extra dates.
  - The headers name 36 satellites ([NCEI THREDDS GridSat-B1 headers](https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/2008/GRIDSAT-B1.2008.01.01.00.v02r01.nc.das)). The sampled first and last dates are only as precise as that sampling. The exact dates in Table 1 come from NCEI's ISCCP B1 satellite table ([NCEI, ISCCP B1 page](https://www.ncei.noaa.gov/products/satellite/international-satellite-cloud-climatology-b1)), Knapp's 2008 table ([Knapp, 2008](https://isccp.giss.nasa.gov/products/JARS-ISCCP-B1.pdf)) and NCEI's day-by-day GIBBS availability pages for changes after 2018.
- **Indirect input: GPCP monthly.** GPCP's own inputs are listed in its CDR algorithm document ([NCEI GPCP C-ATBD Rev. 2, 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Monthly/AlgorithmDescription_01B-34.pdf)) (Table 2 below).
- **No satellite in training.** The neural network's parameters are trained on NCEP Stage IV radar data ([Ashouri et al., 2015](https://www.atmos.albany.edu/daes/atmclasses/atm305/2015/pdf/Ashouri_et_al_2015_BAMS.pdf)).

## Table 1. Geostationary satellites in GridSat-B1 (direct input)

Dates are ISCCP B1 periods of record from NCEI's table ("NCEI") and Knapp 2008 Table 1 ("K08", data as of October 2008), with each satellite's position. The last column is the first and last of the 98 sampled GridSat-B1 v02r01 headers that name the satellite (year-month). PERSIANN-CDR starts on 1983-01-01, so earlier dates are cut to its period.

| Position | Satellite | ISCCP B1 period of record | In sampled GridSat-B1 headers |
|---|---|---|---|
| US, 135°W/75°W | GOES-1 | K08: 12/01/1982–05/31/1983 (135°W); not in NCEI table | 1983-03 (one file) |
| | GOES-5 | NCEI: 1983/07/01–1984/07/30 (−75°); K08: 08/05/1981–07/30/1984 | 1983-01 to 1984-07 |
| | GOES-6 | NCEI: 1983/09/30–1989/01/24 (−135°); K08: 06/01/1983–01/19/1989 | 1983-01¹ to 1988-07 |
| | GOES-7 | NCEI: 1987/03/25–1996/01/17 (−100°) | 1987-07 to 1996-01 |
| | GOES-8 | NCEI: 1994/11/30–2003/03/31 (−75°) | 1995-07 to 2003-01 |
| | GOES-9 | NCEI: 1996/01/01–1998/07/27 (−135°), then 2003/04/25–2005/10/01 at 155° (lent to Japan); K08 gives 140ºE from 05/22/2003 | 1996-01 to 2005-07 |
| | GOES-10 | NCEI: 1998/07/21–2006/06/21 (−135°) | 1999-01 to 2011-01² |
| | GOES-11 | NCEI: 2006/06/21–2011/12/06 (−135°) | 2006-07 to 2011-07 |
| | GOES-12 | NCEI: 2003/04/01–2010/04/14 (−75°) | 2003-07 to 2013-07² |
| | GOES-13 | NCEI: 2010/04/14–2018/01/08 (−75°) | 2010-07 to 2018-01 |
| | GOES-14 | not in NCEI table | 2012-10 and 2013-06 only (stand-in) |
| | GOES-15 | NCEI: 2011/12/06–2020/03/02 (−135°) | 2012-01 to 2020-01 |
| | GOES-16 | NCEI: 2018/01/01–"current" (−75°); GIBBS: last listed 2025-04-07 | 2018-01 to 2025-01 |
| | GOES-17 | NCEI: 2018/12/04–"current" (−135°); GIBBS: still listed 2023-01-05, gone by 2023-01-10 | 2019-01 to 2023-01 |
| | GOES-18 | GIBBS: from 2023-01-04 | 2023-01 to 2026-07 |
| | GOES-19 | GIBBS: from 2025-04-07 | 2025-07 to 2026-07 |
| Europe/Africa 0°, Indian Ocean 63°E/41.5°E | Meteosat-2 | NCEI: 1983/08/31–"2020/03/02"³; K08: 09/03/1981–08/25/1988 | 1983-01 to 1988-07 |
| | Meteosat-3 | NCEI: 1988/08/24–1989/06/19 (0°), 1992/09/11–1995/01/29 (−70°, lent to NOAA); K08: 75ºW 09/12/1992–12/31/1994 | 1989-01 to 1994-07 |
| | Meteosat-4 | NCEI: 1989/06/19–1994/02/04 (0°) | 1989-07 to 1994-01 |
| | Meteosat-5 | NCEI: 1994/01/01–1997/02/01 (0°)³, 1998/06/01–2007/04/16 (63°, Indian Ocean); K08: 02/03/1994–02/13/1997 and 07/01/1998–04/16/2007 | 1994-07 to 2007-01 |
| | Meteosat-6 | NCEI: 1997/02/13–2000/01/20 (0°); K08: to 06/03/1998 | 1997-07 to 1998-01 |
| | Meteosat-7 | NCEI: 1998/05/31–2017/04/04 (0°); 2007/04/16–"current" (63°) | 1998-06 to 2017-01 |
| | Meteosat-8 | NCEI: 2005/01/01–2007/05/10 (0°); 2017/02/10–"current" (41.5°); GIBBS: replaced by Meteosat-9 about 2022-06-01 | 2005-01 to 2022-01 |
| | Meteosat-9 | NCEI: 2007/05/10–2013/01/20 (0°); GIBBS: at the Indian Ocean slot from 2022-06-01 | 2007-07 to 2026-07 |
| | Meteosat-10 | NCEI: 2013/01/20–2018/02/20 (0°); GIBBS: back as the only 0° satellite from 2023-03-22 | 2013-06 to 2026-07 |
| | Meteosat-11 | NCEI: 2018/02/20–"current" (0°); GIBBS: last listed 2023-03-21 | 2018-07 to 2023-01 |
| Japan 140°E | GMS-1 | NCEI: 1984/01/21–1984/06/29; K08: 03/01/1981–06/30/1984 | 1984-03 (one file) |
| | GMS-2 | NCEI: 1983/06/30–1984/09/26; K08: 07/01/1983–09/27/1984 | 1983-01 to 1984-07 |
| | GMS-3 | NCEI: 1984/09/27–1989/12/03 | 1985-01 to 1989-07 |
| | GMS-4 | NCEI: 1989/12/04–1995/06/12 | 1990-01 to 1995-01 |
| | GMS-5 | NCEI: 1995/06/13–2003/05/21 | 1995-07 to 2003-01 |
| | MTSAT-1R | NCEI ("MTS-1"): 2005/10/01–2010/06/30 | 2005-12 to 2015-07⁴ |
| | MTSAT-2 | NCEI ("MTS-2"): 2010/06/30–2015/07/06 | not named in any sampled header⁴ |
| | Himawari-8 | NCEI: 2015/07/07–"present" (141°); GIBBS: last listed 2022-12-13 | 2015-07 to 2022-07 |
| | Himawari-9 | GIBBS: from 2022-12-13 (sole Japanese satellite from 2022-12-14) | 2023-01 to 2026-07 |
| China 105°E | FY-2C | K08: 07/22/2005–"Current" (Oct 2008); not in NCEI table | 2005-12 to 2011-07 |
| | FY-2E | not in NCEI table or K08; GIBBS lists it 2011–2014 | 2012-10 (one file, "FY2-E") |

Sources by column: positions and NCEI dates from [NCEI's ISCCP B1 "Satellite Information" table](https://www.ncei.noaa.gov/products/satellite/international-satellite-cloud-climatology-b1); K08 from [Knapp 2008, Table 1, printed p. 3](https://isccp.giss.nasa.gov/products/JARS-ISCCP-B1.pdf); GIBBS dates from [NCEI GIBBS availability pages](https://www.ncei.noaa.gov/gibbs/availability/2023-01-04), read day by day; last column computed from the 98 [GridSat-B1 v02r01 headers](https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/2026/GRIDSAT-B1.2026.07.01.12.v02r01.nc.das). Each cell's source, file and passage are in `results.csv`. "Current" and "present" are as the tables print them.
¹ The 1983-01-01 headers name GOES-6, which launched on 1983/04/28 (NCEI). The early-1983 labels may be wrong.
² GOES-10 and GOES-12 stay in the files after their NCEI end dates. This fits the South America slot (60°W) that Brazil ran with retired GOES satellites ([obs4MIPs GridSat note, 2016](https://ncics.org/ncics/pdfs/obs4MIPs/GriddedSatelliteB1FCDR-MonthlyMeans_technical-note_final.pdf)). That is my reading, not a stated date.
³ Probable errors in NCEI's table: Meteosat-2's end date repeats GOES-15's, and Meteosat-5's 0° period starts before its printed launch date.
⁴ The sampled headers keep the name "MTSAT-1R" through 2015, although NCEI's table moves the 140°E slot to MTSAT-2 on 2010/06/30. Whether the header label or the table is right was not settled.

## Table 2. Satellites behind GPCP monthly (bias adjustment)

| Input (instrument) | Satellite | Period used in GPCP v2.3 |
|---|---|---|
| SSM/I microwave | DMSP F08 | Jul 1987 to Dec 1991 (excl. Dec 1987) |
| | DMSP F11 | Jan 1992 to May 1995 |
| | DMSP F13 | June 1995 to Dec 2008 |
| SSMIS microwave | DMSP F17 | Jan 2009 to present ("data only from F17") |
| TOVS sounder | NOAA polar orbiters (two until Feb 1999, then one, after NOAA-11 failed; NOAA-14 named) | Aug 1987 to Dec 2002 |
| AIRS sounder | Aqua | Jan 2003 to present (AIRS/AMSU to Aug 2016, AIRS infrared only from Sep 2016) |
| AVHRR (OPI) | NOAA-7 | 7 Sep 1981 to 4 Feb 1985 |
| | NOAA-9 | 5 Feb 1985 to 7 Nov 1988 (OPI used to Dec 1985, per Table 1) |
| Geostationary IR (GPI) | GOES, GMS/MTSAT, Meteosat (not itemized by satellite) | Jan 1986 onward (IR monthly, then 3-hourly from Jan 1997) |

Source: [NCEI GPCP C-ATBD Rev. 2, Tables 1–2, pp. 13–14](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Monthly/AlgorithmDescription_01B-34.pdf); the AMSU change is on p. 16 of the same document. TIROS-N and NOAA-6 (OPI, 1979–81) are earlier than PERSIANN-CDR.

## Conflicting and uncertain points

- **FY-2 (resolved).** A 2016 obs4MIPs note says the Chinese B1 data "were not incorporated into GridSat" ([obs4MIPs GridSat note](https://ncics.org/ncics/pdfs/obs4MIPs/GriddedSatelliteB1FCDR-MonthlyMeans_technical-note_final.pdf)). But [Knapp et al., 2011](https://myweb.fsu.edu/cdholmes/pubs/knapp2011.pdf) shows FY-2C in use on 1 Jan 2008. The current files settle it: the 2008-01-01 00Z header reads "GOES-12,Meteosat-7,MTSAT-1R,FY-2C,GOES-11". FY-2C appears in files from December 2005 to July 2011, and FY2-E on 2012-10-01. **High.**
- **Dates differ between the tables.** Examples are GOES-9's position in 2003–05 (155° or 140ºE), when Meteosat-2 ends, and when Meteosat-5 starts. Neither table is stated to be GridSat-B1's own use period. Dates are **moderate** to within weeks, and the sampled headers agree with them to within the sampling.
- **Which GPCP version.** The C-ATBD (2014) names GPCP version 2.2 ([C-ATBD](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf)). The file headers name `gpcp_m` files through April 2015 and `gpcpv23_m` files from July 2015 ([2015-07-01 header](https://www.ncei.noaa.gov/thredds/dodsC/cdr/persiann/2015/PERSIANN-CDR_v01r01_20150701_c20160324.nc.das)). [Sadeghi et al. 2019](https://repository.library.noaa.gov/view/noaa/65498) say version 2.3 data "replaced V2.2 data for the 2009–2013 period", yet the 2011-07-01 header still names `gpcp_m1107.bin`. Not resolved. Version 2.2's documentation dates the boundaries slightly differently: F13 from May 1995, and TOVS until April 2005 with AIRS from May 2005 ([GPCP v2.2 documentation, 2012](https://www2.dgeo.udec.cl/Public/gridded_products/noaa/gpcp/v2.2/V2.2_doc.pdf)).
- **Smaller date differences between documents.**
  - Meteosat-5's start over the Indian Ocean (63°E) is given as 1998/06/01 (NCEI), 07/01/1998 (Knapp 2008) and "06 UTC 16 June 1998" ([GPCP C-ATBD](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Monthly/AlgorithmDescription_01B-34.pdf)).
  - The loss of Aqua's AMSU is dated September 2016 in the GPCP C-ATBD, which this answer follows, and October 2016 in the [GPCP v2.3 technical note](https://esgf.nccs.nasa.gov/esgdoc/GPCP_precip_SG-V2.3_TechNote_180510.pdf).
  - A 2016 obs4MIPs note counts "nearly 30 satellites" in GridSat. The 36 here include those added since 2016 (GOES-16 to -19, Himawari-9, Meteosat-11), and GOES-14 and FY-2E, which each appear in only one or two sampled files.
- **Himawari-8 back in late 2025?** The checking subagent reports that WMO OSCAR lists Himawari-8 as primary again from 12 Oct to 26 Nov 2025. It read the page only through a fetch tool, and this run did not check it. Neither sampled 2025–26 GridSat header falls in that window. **Low.**
- **INSAT.** NCEI's metadata keywords list INSAT ([GridSat-B1 ISO metadata](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00829)). No ISCCP B1 table and no sampled header names an INSAT satellite. Treat it as not used. **Moderate.**
- **AVHRR to fill the Indian Ocean gap.** The C-ATBD says AVHRR on NOAA-7 to NOAA-14 "can be used to fill part of the gap before 1997". No source says PERSIANN-CDR did so, and the files list only GridSat and GPCP inputs. **Low** that AVHRR is a direct input.

## Gaps

- **Exact GridSat-B1 switch dates** for each satellite. These are in the `satid` variables of each 3-hourly file at NCEI ([guide: using_satid.pdf](https://www.ncei.noaa.gov/sites/default/files/2021-08/using_satid.pdf)). A full pass over the files' headers would date each change to the 3 hours. This run sampled 98 files.
- **Individual geostationary satellites in GPCP's GPI, and the NOAA satellite numbers behind TOVS.** These are not listed in GPCP's documents. They are held by NOAA CPC (GPI) and NASA GSFC (TOVS Pathfinder).

## Sources

Product and inputs:
- [CHRS/NCEI, PERSIANN-CDR C-ATBD (CDRP-ATBD-0464, 01B-16), 2014](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/PERSIANN/AlgorithmDescription_01B-16.pdf)
- [Ashouri et al., PERSIANN-CDR, BAMS, 2015](https://www.atmos.albany.edu/daes/atmclasses/atm305/2015/pdf/Ashouri_et_al_2015_BAMS.pdf)
- [Sadeghi et al., PERSIANN-CDR with GPCP V2.2 and V2.3, Remote Sensing, 2019](https://repository.library.noaa.gov/view/noaa/65498)
- [NCEI THREDDS, PERSIANN-CDR 2011-07-01 file header](https://www.ncei.noaa.gov/thredds/dodsC/cdr/persiann/2011/PERSIANN-CDR_v01r01_20110701_c20140523.nc.das)
- [NCEI THREDDS, PERSIANN-CDR 2015-07-01 file header](https://www.ncei.noaa.gov/thredds/dodsC/cdr/persiann/2015/PERSIANN-CDR_v01r01_20150701_c20160324.nc.das)

GridSat-B1 and ISCCP B1:
- [NCEI THREDDS, GridSat-B1 v02r01 file headers (98 sampled, 1983–2026), e.g. 2008-01-01 00Z](https://www.ncei.noaa.gov/thredds/dodsC/cdr/gridsat/2008/GRIDSAT-B1.2008.01.01.00.v02r01.nc.das)
- [NCEI, ISCCP B1 Data page, "Satellite Information" table](https://www.ncei.noaa.gov/products/satellite/international-satellite-cloud-climatology-b1)
- [Knapp, Scientific data stewardship of ISCCP B1, JARS, 2008](https://isccp.giss.nasa.gov/products/JARS-ISCCP-B1.pdf)
- [Knapp et al., Globally gridded satellite observations for climate studies, BAMS, 2011](https://myweb.fsu.edu/cdholmes/pubs/knapp2011.pdf)
- [NCICS, GridSat-B1 monthly means obs4MIPs technical note, 2016](https://ncics.org/ncics/pdfs/obs4MIPs/GriddedSatelliteB1FCDR-MonthlyMeans_technical-note_final.pdf)
- [NCEI, GridSat-B1 ISO metadata (C00829)](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00829)
- [NCEI, Identifying source satellites in GridSat-B1 (using_satid.pdf)](https://www.ncei.noaa.gov/sites/default/files/2021-08/using_satid.pdf)
- [NCEI GIBBS availability pages, e.g. 2023-01-04](https://www.ncei.noaa.gov/gibbs/availability/2023-01-04) (29 dates read)

GPCP:
- [NCEI, GPCP Monthly C-ATBD Rev. 2 (CDRP-ATBD-0848), 2017](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Precipitation_GPCP-Monthly/AlgorithmDescription_01B-34.pdf)
- [Huffman and Bolvin, GPCP V2.2 documentation, 2012](https://www2.dgeo.udec.cl/Public/gridded_products/noaa/gpcp/v2.2/V2.2_doc.pdf) (copy on a university server)

Saved in [`web_search_results/2026-11-19_persiann-cdr-daily-satellites/`](web_search_results/2026-11-19_persiann-cdr-daily-satellites/): this answer, the research record, `results.csv`, `check-by-hand.md`, `sites-to-trust.md` and the sampled GridSat-B1 header list (`work/gridsat_samples.csv`).
