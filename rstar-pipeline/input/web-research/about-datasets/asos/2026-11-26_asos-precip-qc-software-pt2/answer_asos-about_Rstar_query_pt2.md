# ASOS precipitation, Part 2: processing, QC, calibration, software and openness

ASOS precipitation is checked mostly by automation at the station and by NWS's AOMC, while NCEI does little precipitation-specific checking. NCEI passes the 1-minute data on "as received", and GHCNh's own tests leave precipitation out. Calibration of the two gauges is minimal, and its procedures sit in a handbook that isn't public. No outside calibration service was found, which contradicts DIRS-1. The station software (FAA), its hardware (a vendor) and the telecom links (FAA) lie outside NWS and NCEI, which supports DIRS-4. None of the production code is published, which supports P-3. The formats are open text that open decoders read, which mostly contradicts D-4. Overall confidence: **moderate**. The calibration and code findings rest partly on things not being found.

## QC by stage

| Stage | Who | Automated or manual | Flags | Risk |
|---|---|---|---|---|
| Station (Level 1) | ACU software, before transmission | Automated self-checks; bad data dropped | `$` maintenance indicator, which "does not necessarily mean that the data are erroneous" | contradicts P-3 (documented) |
| WFO (Level 2) | Forecast office staff, for an area about a state's size | Manual review within about 1–2 h | Observers may augment or back up reports; WFOs and FAA-certified observers can disable a sensor that gives bad data without a flag | contradicts P-3 |
| National (Level 3) | NWS AOMC, 24/7/365 | Automated plus staff | Late hourly reports (after H+15), `$` reports, remote dial-in, trouble reports | contradicts P-3 |
| 1-minute page 2 (DSI 6406) | NCEI | Basic QA only (record format, station ID) | none; "No attempt to edit data or correct" | supports P-3 (data unchecked downstream) |
| Hourly (ISD → GHCNh) | NCEI | Automated | ISD validated precipitation; GHCNh's own QC covers temperature, dew point, pressure and wind only, and precipitation keeps the legacy codes | partly supports P-3 |
| Daily (GHCN-Daily) | NCEI | Fully automated QA | Flags about 0.24% of values; false-positive rate under 5% for each element | contradicts P-3 |

Sources: [NWS ASOS User's Guide](https://www.weather.gov/media/asos/aum-toc.pdf); [NWSI 30-2111, 2025](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf); [NCEI DSI 6406 doc](https://www.ncei.noaa.gov/pub/data/asos-onemin/td6406.txt), [2022 doc](https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg2/doc/asos-1min-pg2_documentation.pdf) and [C00387 lineage](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00387/html); [GHCNh documentation](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf); [Lott, ISH QC](https://ncei.noaa.gov/pub/data/noaa/ISH-DVD2012/ish-qc.pdf); [Durre et al. 2010](https://ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf). No NCEI QC description was found for the 5-minute data. (High)

## Measurement issues

- **Heated tipping bucket (HTB):**
  - Software corrects high rain rates above 1.80 in/h (IEM quotes the manual's formula, C = A(1 + 0.60A)), but the HTB may still under-report above 10 in/h.
  - Heating evaporates or sublimates freezing and frozen precipitation.
  - Snow caps cause delayed false tips, and dew or frost causes spurious 0.01 in reports ([ASOS User's Guide](https://www.weather.gov/media/asos/aum-toc.pdf); [AWPAG plan](https://www.weather.gov/media/asos/ASOS%20Implementation/awpagimplan.pdf)).
  - The National Academies found 2–10% undercatch against manual gauges. They also found that the 1996 redesign helped but left about 10 years of undercatch in the climate record ([NRC 2012, App. E](https://www.nationalacademies.org/read/13216/chapter/13), read via extraction).
  - WMO-SPICE tested heated tipping-bucket gauges and produced undercatch adjustments for them ([Kochendorfer et al. 2020](https://repository.library.noaa.gov/view/noaa/29189)); the ASOS model isn't named in that paper. (High)
- **AWPAG (All Weather Precipitation Accumulation Gauge):**
  - It is an Ott weighing gauge. Its own firmware deals with evaporation, wind turbulence and sudden changes that aren't precipitation; after that, the ACU processes it exactly as it does the HTB ([release note v2.7B](https://www.weather.gov/media/asos/ASOS%20Implementation/relnoteawpag.pdf)).
  - In the 2003–04 winter test (53 events at Sterling, 47 at Johnstown), 81% of 100 event totals met NWS requirements and the 19% that failed were under-reports, against 60% for HTBs ([Greeney et al., AMS](https://ams.confex.com/ams/pdfpapers/82895.pdf)).
  - AWPAG hourly totals met the requirements 97% of the time that winter, against 81% the winter before. The paper puts the 16% improvement down to firmware adjustments.
  - The gauge is a container that fills up: ASOS raises a maintenance message above 42 inches, 80% of capacity ([release note](https://www.weather.gov/media/asos/ASOS%20Implementation/relnoteawpag.pdf)).
  - No SPICE result names the AWPAG. (Moderate)
- **Why 1-minute and hourly totals differ:**
  - A 1-minute value covers :24 to :23 seconds. An hourly METAR covers the period since the station's reset (for example 11:54:24–12:54:23), and the daily summary uses local standard time ([IEM note](https://mesonet.agron.iastate.edu/ASOS/precipnote.phtml); [FAA JO 7900.5E](https://www.faa.gov/documentLibrary/media/Order/Order_JO_7900.5E.pdf), "since the last METAR").
  - MADIS sums 1-minute data from :45 to :44 ([MADIS](https://madis.ncep.noaa.gov/omo_precip.shtml)).
  - Sums over different windows, plus NCEI's unedited 1-minute files, mean the two need not agree. (Moderate: IEM's note is a secondary account.)

## Calibration

- **NWS electronics technicians:** they do quarterly preventive maintenance, and "ASOS sensors require minimal calibration" ([NWSI 30-2111](https://www.weather.gov/media/directives/030_pdfs/pd03021111curr.pdf)). The schedules are in Engineering Handbook #11, "not available to the general public", and follow the manufacturers' quarterly, semiannual, annual and biennial intervals ([ASOS FAQ](https://www.weather.gov/asos/FAQ.html)). This supports P-3.
- **Sterling Field Support Center:** its four labs are pressure, hygrothermometer, environmental chambers and wind tunnel, with none for precipitation. In 2017 it was "investigating" becoming a WMO Regional Instrument Centre ([Childs poster 2017](https://ams.confex.com/ams/97Annual/webprogram/Handout/Paper315704/CHILDS_AMS_POSTER_2017v5.pdf); [SFSC](https://www.weather.gov/soic/)). Sterling did host the AWPAG qualification test.
- **WMO Regional Instrument Centres:** WMO's current list (updated 29 Oct 2026) names only Bridgetown (Barbados) for Region IV, so there is no US Regional Instrument Centre ([WMO](https://community.wmo.int/site/knowledge-hub/programmes-and-initiatives/instruments-and-methods-of-observation-programme-imop/regional-instrument-centres)).
- **NIST traceability:** none found for either gauge.
- **DIRS-1:** contradicted. No external calibration service could be found that the precipitation gauges rely on. What exists is NWS's own technicians working to manufacturers' intervals. (Moderate: the handbook wasn't read.)

## Software and facilities (DIRS-4 supported)

| Piece | Owner, operator | Code |
|---|---|---|
| ACU station software (pSOS on VME; PowerPC since 2002–03) | NWS/FAA tri-agency program; next-generation software developed by the FAA (C++ with OpenDDS) ([AMS 2017](https://ams.confex.com/ams/97Annual/webprogram/Manuscript/Paper315698/AMS%20Modernization%20of%20ASOS%20Hardware%20and%20Software%20Paper_FINAL.pdf); [processor upgrade](https://www.weather.gov/media/asos/ASOS%20Implementation/revprocessor0203.pdf)) | unpublished; described in release notes and papers |
| ASOS 2.0 hardware (ACU/DCP/SCA) | Campbell Scientific, under SLEP; says it delivered "all 1,529 units" by 2025, though its own parts list (700 ACUs, 799 DCPs, 50 SCAs) adds to 1,549 ([Campbell](https://www.campbellsci.com/us-asos-weather-network), vendor claim, read via extraction) | vendor |
| AWPAG firmware | Ott | proprietary firmware; described only |
| Site parameters and software configuration | NWS AOMC ([NWSI 30-2111](https://www.weather.gov/media/directives/030_pdfs/pd03021111curr.pdf)) | unpublished |
| Telecommunication | leased lines through the FAA ([FAA ASWON](https://www.faa.gov/air_traffic/weather/asos)) | n/a |
| NCEI 1-minute, 5-minute, ISD/GHCNh production | NCEI; GHCNh reportedly runs on AWS EC2 ([2024 NCEI slides](https://gcos.wmo.int/sites/default/files/6.4_ghcn-for-aopc-2024.pdf), search summary only, low) | no public repository found; GHCNh doc mentions "NCEI software" only |
| IEM processing | Iowa State University | published: [pyIEM](https://github.com/akrherz/pyIEM/blob/main/LICENSE) and [iem](https://github.com/akrherz/iem/blob/main/LICENSE), MIT-style licence text |

The FAA, a vendor and AWS are all outside NCEI's and NWS's control. This supports DIRS-4 and, given the unpublished code, P-3.

## Documentation

A newcomer could *read* every product: the ISD format document is byte-level ([ISD format](https://www.ncei.noaa.gov/pub/data/noaa/isd-format-document.pdf)), GHCNh's PSV layout is documented, and the DSI-6406 documentation labels a sample record. No one could *reproduce* the products, though, because the processing documents are either missing or not public:
- the ACU code;
- EHB-11;
- NCEI's and GHCNh's processing code;
- GHCNh's precipitation QC.

This supports P-3. (Moderate: q5 was searched thinly.)

## FAIR, by product and route

| Product, route | F (DOI, catalog) | A (open protocol, no login) | I (open format, standard names, units) | R (licence, provenance) | Rating |
|---|---|---|---|---|---|
| 1-minute page 2, NCEI directory | **fails DOI**; Geoportal and data.gov records | HTTPS, no login | 99-char fixed ASCII, inches, no standard names, no byte positions in 2022 doc | **licence unclear** (none in NCEI ISO, CC0 on data.gov); "as received" | partly FAIR |
| 5-minute, NCEI directory | DOI not checked | HTTPS directory; readme still gives anonymous FTP | METAR text in fixed records | no licence found | partly FAIR |
| GHCNh, NCEI | DOI [10.25921/jp3d-3v19](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01688/html); Geoportal | HTTPS | PSV/Parquet, named columns, mm; not CF names | CC0-1.0 in [ISO XML](https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C01688.xml); source codes kept | FAIR |
| GHCNh, AWS `noaa-ghcnh-pds` | AWS Registry; shares the DOI | anonymous S3 (`--no-sign-request`) | same | CC0-1.0 ([Registry](https://registry.opendata.aws/noaa-ghcnh/)) | FAIR |
| IEM ASOS/METAR and 1-minute | **fails**: no DOI or catalog record found | HTTP GET, no login | CSV/TSV, own names (`p01i`), inches, "M" mixes missing and QC-removed | public domain, attribution asked ([disclaimer](https://mesonet.agron.iastate.edu/disclaimer.php)); 1-minute re-served from NCEI ([help](https://mesonet.agron.iastate.edu/cgi-bin/request/asos1min.py?help)) | partly FAIR |
| GHCN-Daily (daily summaries) | not re-rated here (earlier GHCN-Daily runs) | | | | — |

Sources: [C00387 ISO](https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C00387.xml), [data.gov C00387](https://catalog.data.gov/dataset/1-minute-page-2-surface-weather-observations-from-the-automated-surface-observing-systems-), [DSI-6406 2022 doc](https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg2/doc/asos-1min-pg2_documentation.pdf), [5-minute readme](https://www.ncei.noaa.gov/pub/data/asos-fivemin/), [IEM download](https://mesonet.agron.iastate.edu/request/download.phtml), [NCEI open data policy](https://www.ncei.noaa.gov/sites/default/files/2023-12/NCEI%20PD-10-2-02%20-%20Open%20Data%20Policy%20Signed.pdf).

**Conflict:** the 1-minute product's licence. NCEI's ISO XML has no CC0 text, but the data.gov record harvested from it lists CC0. NCEI's policy says CC0 should apply, so CC0 is the likely intent, but the product's own NCEI record doesn't state it.

**Software:** no product needs proprietary software. Open METAR decoders exist:
- [python-metar](https://github.com/python-metar/python-metar) has a BSD-style licence ([LICENSE](https://github.com/python-metar/python-metar/blob/main/LICENSE)) and parses the US precipitation remarks (`P0013`).
- [MetPy](https://unidata.github.io/MetPy/latest/api/generated/metpy.io.parse_metar_file.html) has a BSD 3-Clause licence ([LICENSE](https://github.com/Unidata/MetPy/blob/main/LICENSE)), but leaves the remarks as raw text.

**D-4:** contradicted for every product, with one weak point. The DSI-6406 record layout is described only by a labelled sample line, and it uses non-SI units.

## Risk summary

| Risk | Verdict | Main evidence |
|---|---|---|
| D-4 formats obsolete or proprietary | mostly contradicted | open text formats, open decoders; weak spot: DSI-6406 layout and inches |
| P-3 critical knowledge undocumented | supported | EHB-11 not public; no published station, NCEI or GHCNh code; GHCNh precipitation QC undescribed; 1-minute data unedited |
| DIRS-1 external calibration service | contradicted (absence of evidence) | minimal calibration by NWS technicians; no precipitation lab at Sterling; no US Regional Instrument Centre; no NIST link found |
| DIRS-4 outside processing infrastructure | supported | FAA software and telecom, Campbell Scientific hardware, Ott firmware, AWS distribution (and reportedly processing) |

## Gaps

- **Engineering Handbook #11:** this NWS maintenance handbook holds the gauges' actual field-check and calibration steps. It isn't public; NWS's Office of Observations holds it, so getting it needs a records request.
- **GHCNh cloud processing:** the 2024 NCEI slides to the GCOS AOPC returned HTTP 404, and so did the Wayback copy tried. They are listed in `check-by-hand.md`.
- **Not checked:**
  - the 5-minute product's DOI and catalog record;
  - WMO-SPICE results for the AWPAG;
  - the DOT OIG audit av2001073;
  - observer edit logs (ASOS_OID);
  - which licence pyIEM uses. Its LICENSE file starts with MIT-style text, but a package index (not saved) lists Apache-2.0.
- **Documentation question (q5):** searched thinly.
- **Run limits:** the run clock was held by another live run, so stops were kept by hand and no token count is available.
- **Sandbox:** three hosts were refused (`sites-to-trust.md`); you can check whether to add any to your sandbox's allowed domains.

## Sources

NWS and FAA: [ASOS User's Guide](https://www.weather.gov/media/asos/aum-toc.pdf); [NWSI 30-2111 (2025)](https://www.weather.gov/media/directives/030_pdfs/pd03021011curr.pdf); [NWSI 30-2111 (sa2 copy)](https://www.weather.gov/media/directives/030_pdfs/pd03021111curr.pdf); [ASOS FAQ](https://www.weather.gov/asos/FAQ.html); [AWPAG release note v2.7B](https://www.weather.gov/media/asos/ASOS%20Implementation/relnoteawpag.pdf); [AWPAG implementation plan](https://www.weather.gov/media/asos/ASOS%20Implementation/awpagimplan.pdf); [Processor board upgrade](https://www.weather.gov/media/asos/ASOS%20Implementation/revprocessor0203.pdf); [ASOS 2.0 issue-report governance](https://weather.gov/media/asos/ASOS%20Issue%20Report%20-%20Governance%20v6.pdf); [SFSC](https://www.weather.gov/soic/); [FAA ASWON](https://www.faa.gov/air_traffic/weather/asos); [FAA JO 7900.5E](https://www.faa.gov/documentLibrary/media/Order/Order_JO_7900.5E.pdf); [MADIS one-minute precip](https://madis.ncep.noaa.gov/omo_precip.shtml) (extraction).

NCEI and NOAA: [DSI 6406 doc](https://www.ncei.noaa.gov/pub/data/asos-onemin/td6406.txt); [DSI-6406 2022 doc](https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg2/doc/asos-1min-pg2_documentation.pdf); [C00387 Geoportal](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00387/html); [C00387 ISO XML](https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C00387.xml); [C01688 Geoportal](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C01688/html); [C01688 ISO XML](https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C01688.xml); [GHCNh documentation](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh_DOCUMENTATION.pdf); [ISD format document](https://www.ncei.noaa.gov/pub/data/noaa/isd-format-document.pdf); [ISH QC paper](https://ncei.noaa.gov/pub/data/noaa/ISH-DVD2012/ish-qc.pdf); [Durre et al. 2010](https://ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf); [5-minute readme](https://www.ncei.noaa.gov/pub/data/asos-fivemin/); [NCEI Open Data Policy](https://www.ncei.noaa.gov/sites/default/files/2023-12/NCEI%20PD-10-2-02%20-%20Open%20Data%20Policy%20Signed.pdf); [NOAA CC0 component](https://data.noaa.gov/docucomp/xmlComponent/show/690539); [data.gov C00387](https://catalog.data.gov/dataset/1-minute-page-2-surface-weather-observations-from-the-automated-surface-observing-systems-); [NCEI GHCN slides for AOPC 2024](https://gcos.wmo.int/sites/default/files/6.4_ghcn-for-aopc-2024.pdf) (search summary only).

Papers and others: [Greeney et al., AWPAG winter test](https://ams.confex.com/ams/pdfpapers/82895.pdf); [AMS 2017 ASOS modernization](https://ams.confex.com/ams/97Annual/webprogram/Manuscript/Paper315698/AMS%20Modernization%20of%20ASOS%20Hardware%20and%20Software%20Paper_FINAL.pdf); [Childs SFSC poster 2017](https://ams.confex.com/ams/97Annual/webprogram/Handout/Paper315704/CHILDS_AMS_POSTER_2017v5.pdf); [Kochendorfer et al. 2020](https://repository.library.noaa.gov/view/noaa/29189); [NRC 2012 Appendix E](https://www.nationalacademies.org/read/13216/chapter/13) (extraction); [WMO Regional Instrument Centres](https://community.wmo.int/site/knowledge-hub/programmes-and-initiatives/instruments-and-methods-of-observation-programme-imop/regional-instrument-centres); [Campbell Scientific ASOS case study](https://www.campbellsci.com/us-asos-weather-network) (extraction); [AWS Registry GHCNh](https://registry.opendata.aws/noaa-ghcnh/); [IEM precipitation note](https://mesonet.agron.iastate.edu/ASOS/precipnote.phtml); [IEM download](https://mesonet.agron.iastate.edu/request/download.phtml); [IEM 1-minute help](https://mesonet.agron.iastate.edu/cgi-bin/request/asos1min.py?help); [IEM disclaimer](https://mesonet.agron.iastate.edu/disclaimer.php); [pyIEM LICENSE](https://github.com/akrherz/pyIEM/blob/main/LICENSE); [iem LICENSE](https://github.com/akrherz/iem/blob/main/LICENSE); [python-metar](https://github.com/python-metar/python-metar); [python-metar LICENSE](https://github.com/python-metar/python-metar/blob/main/LICENSE); [MetPy parse_metar_file](https://unidata.github.io/MetPy/latest/api/generated/metpy.io.parse_metar_file.html) (extraction); [MetPy LICENSE](https://github.com/Unidata/MetPy/blob/main/LICENSE); [DuckDuckGo results for GHCNh code](https://html.duckduckgo.com/html/?q=GHCNh+github+code+NCEI+hourly) (snippets).

Saved in [`web_search_results/2026-11-26_asos-precip-qc-software-pt2/`](./): this answer, `method.md`, `research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
