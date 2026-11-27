## The short answer

daily01 comes from one NCEI-owned pipeline:
- the stations send their data over NESDIS's GOES satellite data collection system;
- NCEI's ingest software decodes the records, flags bad values automatically and computes precipitation with the published "Official Algorithm for Precipitation" (OAP) 2.0/2.1. That algorithm takes a weighted average of the Geonor gauge's three vibrating wires, with the wetness sensor deciding whether small changes count;
- the results go into the USCRN database, which writes the fixed-width text files.

ATDD calibrates the gauges in the field with brass weights. Those weights were compared with a NIST-traceable standard, but every procedure document found dates from 2002–2003.

The algorithm and the file formats are documented well enough to re-implement. The code, the QC parameter files and the station-metadata system (ISIS) are not public.

The NCEI route is partly FAIR: it has a DOI, an open protocol and open text formats, but no stated licence and no CF variable names. The Copernicus copy is partly FAIR too: it has a DOI, NetCDF and a CC-BY licence, but it needs a login, and its download form was closed on 26 Nov 2026.

Overall confidence: moderate. The documents are direct, but many are old, and a "not found" can't prove absence.

## Processing and QC

- **The 5-minute precipitation algorithm** (confidence: high):
  - OAP 2.0 replaced the 2005 pairwise method. The Configuration Control Board approved it in CCR 46 on 21 April 2014.
    - The daily01 README dates the switch in daily01 to 17 Aug 2015.
    - NCEI's catalog dates "a new version of the USCRN database", which updated precipitation for all data and products, to 2015-10-15 ([C00546 record](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00546)).
    - These may be two steps, the algorithm's start and then the reprocessing. That is unconfirmed.
  - The algorithm computes wire weights "as a function of the average delta variance" ([NCEI, OAP 2.0/2.1 calculation system, 2016](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2016-05/USCRN_OAP2.0+2.1_Weighted_Average_Precipitation_Calculation_System.pdf)).
  - Its constants include MIN_PRECIP 0.2 mm, DELTA_THRESHOLD 0.5 mm, GIANTSTEP 25 mm and a wetness threshold of 500.
  - It computes nothing when the logger door is open, when fewer than two wires are healthy, or when the gauge is over capacity (600 or 1000 mm, depending on location) ([NCEI, OAP 2.0 Description, 2015](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2015-09/USCRN_OAP2.0.Description_PrecipChanges.pdf)).
  - OAP 2.1 fixed wetness range checks that 2.0 had missed, and capped the residual carried over at 0.3 mm ([NCEI, OAP 2.1, rev. 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2017-06/USCRN_OAP2.1.Description_PrecipChanges.pdf)).
  - The method is peer-reviewed (Leeper, Palecki and Davis 2015, JTECH, appended to the OAP 2.0 Description). It was developed by NCICS's Leeper with NCEI staff ([NCICS](https://ncics.org/portfolio/observing-systems/uscrn-precipitation-data/)). The 2005 pairwise note had contractor co-authors ([TN05-001](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/technotes/TN05001GeonorAlgorithm.pdf)).
- **From 5-minute values to daily** (moderate):
  - P_DAILY_CALC is the "Total amount of precipitation, in mm" over the station's 24-hour LST day.
  - It has no quality flag: values built from flagged raw data are "reported as missing" ([daily01 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt)). Hourly P_CALC is the same ([hourly02 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/hourly02/README.txt)).
  - The ingest computes hourly (P_OFFICIAL), 5-minute and 15-minute Geonor totals ([ingest spec](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/CRN_Ingest_Functional_Spec.pdf)).
  - **No public document found gives the rule that sums those totals into the daily value**, for example how many missing hours make a day missing.
  - The 2007 requirements set precipitation accuracy at ±0.25 mm or ±2% of the reported value, whichever is greater ([Functional Requirements, 2007](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X040_d0.pdf)).
  - The README calls the gauge sensors "load cell sensors", but the algorithm documents describe vibrating wires. The README's wording is loose.
- **Checks and flags** (moderate):
  - The ingest system flags RANGE, DELTA, DOOR, FROZEN and SENSOR errors, and leaves flagged values out of the calculations ([NCEI ingest specification, 2013](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/CRN_Ingest_Functional_Spec.pdf)).
  - Its limits are held in internal CSV parameter files and in ISIS. Neither is published.
  - The subhourly flags are 0 (good), 1 (field overflow) and 3 (erroneous), and there is no precipitation flag column ([subhourly01 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/subhourly01/README.txt)).
- **Manual review:**
  - The OAP documents describe a Configuration Control Board-approved "exception procedure" for removing or restoring gauge data.
  - A 2003 draft handbook has a human analyst supplementing the automated QC ([NCEI, Manual Monitoring Handbook, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/ManualMonitoringHandbook.pdf)).
  - Who does either today isn't stated.
- **Who does what:**
  - NCEI runs ingest, QC and the products ([USCRN Data Management Plan, 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN_Data_Management_Plan-August_2017.pdf)).
  - ATDD does installation, maintenance and calibration ([X041 maintenance plan, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X041_d0.pdf)).

## Calibration

- **Who and how** (moderate):
  - "The Geonor precipitation gauges are calibrated in the field using calibration weights that were compared to a NIST traceable standard weight" ([X041, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X041_d0.pdf)).
  - ATDD's 2002 manual names machined brass weights of 1000.0 g, a "Troemner certified calibration weight – 1000g" and an A&D precision scale. It fits each wire's frequency to depth ([ATDD/NCDC manual, 2002](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/NOAA%20NCDC%20DOCUMENTATION%2007192002.doc)).
  - The annual visit includes "Calibrate rain gauge", with verification before and after using 1000 mL of water ([Installation Guide, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN%20Installation%20Guide.pdf)). X041 also lists a monthly verification.
  - The coefficients of each wire are stored in NCEI's ISIS station record ([ISIS event, 2007](https://www.ncei.noaa.gov/access/isis/event.htm?display=ALLCHANGES&eventid=908)). ARL still describes calibrating the gauges at every annual visit ([ARL](https://arl.noaa.gov/uscrn-at-arl)).
  - The 2003 calibration sheet labels its weight column "(mg)", which is probably a misprint for grams (unresolved).
- **The reference is ATDD's own weight, not an outside service.**
  - Who certifies the Troemner weight, and how often, is not stated.
  - No source ties USCRN's gauge calibration to a WMO Regional Instrument Centre or to a NIST calibration service.
  - The WMO-SPICE recommendations of 2012 (not about USCRN) relay Geonor's view that its "factory calibration … does not change significantly over time", and say wires out of calibration go back to Geonor ([WMO SPICE, 2012](https://old.wmo.int/extranet/pages/prog/www/IMOP/intercomparisons/SPICE/Docs/SPICE%20GEONOR%20Calibration%20and%20Configuration%20Recommendations%20Dec%205,%202012.pdf.pdf)).
  - SPICE also recommends an empty-bucket check, with a new coefficient if a wire's empty-bucket frequency is off by more than 10 Hz.
  - ATDD's 2003 plan puts the chance of a Geonor wire failure at 3% a year ([X041](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X041_d0.pdf)).
  - USCRN's own 2002 test found 19 of 20 wires stable ([Duchon 2002](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/research/Geonor-Lab-Test-Report.doc)).
- **No wetness-sensor calibration was found.**

## Software and facilities

| Piece | Owner and operator | Code status |
|---|---|---|
| Datalogger (Campbell CR3000) and TX320 GOES transmitter | ATDD in the field ([NCEI instruments](https://www.ncei.noaa.gov/access/crn/instruments.html)) | logger program: not checked |
| GOES Data Collection System, Wallops receive station, LRGS/NOAAPort feeds | NESDIS (outside NCEI and ATDD) | not applicable |
| Ingest decoder, QC flagging, OAP calculation (Java classes RecordDecoder, SoilCalc) | NCEI; spec written by an ERT Inc. contractor | described only (ingest spec, OAP documents); unpublished |
| "linux box running USCRN and LRGS interpreter software", the USCRN database, product generation | NCEI, under NCEI configuration management ([C00546 record](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00546); DMP 2017) | unpublished; no NOAA repository found |
| ISIS station metadata, QC parameter CSVs | NCEI | internal |

Logger files downloaded directly on site are a fallback path ([ingest spec](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/CRN_Ingest_Functional_Spec.pdf)). The 2007 requirements say "the detailed quality control software code shall be made available to users" ([Functional Requirements, 2007](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X040_d0.pdf)). No such release was found. The only GitHub hits were third-party readers (one MIT-licensed).

## Documentation

NCEI keeps a public library ([documentation page](https://www.ncei.noaa.gov/access/crn/documentation.html); [program folder](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/)):
- the requirements;
- the maintenance, commissioning and data-management plans;
- the installation guide;
- the ingest spec;
- the OAP descriptions with their constants and steps;
- the product READMEs.

That is enough to re-implement the precipitation algorithm and to read the files, but not to run the processing. Missing from it are:
- the code and the QC parameter files;
- ISIS;
- the CCRs after CCR 36 of 2008 ([CCRs folder](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/CCRs/)), including CCR 46, which approved OAP 2.0;
- the daily summation rule;
- any current ATDD maintenance manual.

Most of the library dates from 2002–2007, and several files are .doc or .xls.

## FAIR, per route

| Route and format | F | A | I | R | Rating |
|---|---|---|---|---|---|
| NCEI directory (`/pub/data/uscrn/products/daily01/`), fixed-width ASCII | DOI 10.7289/V5H13007 and an NCEI catalog record ([DataCite](https://api.datacite.org/dois/10.7289/V5H13007)) | open HTTPS/FTP, no login | open text with a column README; own names (P_DAILY_CALC), not CF; units stated | **fails: no licence**, only a citation request and a liability notice; DataCite rightsList is empty; lineage given | partly FAIR |
| NCEI catalog and portal (C00546 landing page, NCEI Data Search) | same DOI; ISO record | open, no login (the live page gave HTTP 503 during this run) | lists only "ASCII Text" | same: no licence | partly FAIR |
| Copernicus CDS copy, NetCDF4 or CSV (CDM-Obs-Core) | its own DOI 10.24381/cds.d1f4864d | **fails: login and licence acceptance required**; the form was "temporarily closed" on 2026-11-26 | open NetCDF and CSV, SI units, C3S CDM-Obs names (CF conformance not stated) | CC-BY plus the USCRN data policy; source given as NCEI | partly FAIR |
| NOAA Open Data Dissemination (NODD) cloud copy | none found | – | – | – | not found |

Sources for the CDS row: [CDS page](https://cds.climate.copernicus.eu/datasets/insitu-observations-near-surface-temperature-us-climate-reference-network?tab=download) and [DataCite](https://api.datacite.org/dois/10.24381/cds.d1f4864d).

- The USCRN data policy says "USCRN data are open for the users", asks users to cite Diamond et al. 2013, and names no licence ([data policy](https://object-store.os-api.cci2.ecmwf.int/cci2-prod-catalogue/licences/uscrn-data-policy/uscrn-data-policy_c37d84a0040855c6c0698de99889a39acd806cceb92273f5a3d9cf293171e960.pdf), read via its Wayback copy).
- No route needs proprietary software.
- The CDS overview says the copy is updated "Every year", but its year picker stops at 2022 (unresolved).

## The four risks

| Risk | Verdict | Evidence |
|---|---|---|
| D-4 formats obsolete or proprietary | **contradicted** | open fixed-width ASCII with READMEs; NetCDF and CSV at the CDS; no proprietary software. Only some program documents are old .doc/.xls files |
| P-3 critical knowledge undocumented | **partly supported** | the algorithm, file formats and calibration method are documented. Undocumented or unpublished: the code (despite FRD 7.3.1), the QC parameter files, ISIS, the CCRs after 2008, the daily summation rule, who does manual review now, and any calibration procedure after 2003 |
| DIRS-1 external calibration service that could be disrupted | **mostly contradicted** | ATDD calibrates in house against its own certified weights. The only outside links are the weight's certification (by whom not stated) and Geonor's factory recalibration of faulty wires |
| DIRS-4 outside processing infrastructure | **partly supported** | processing and computing are NCEI's own. Routine data delivery depends on NESDIS's GOES DCS and Wallops, with on-site logger downloads as a slow fallback. Part 1 said DIRS-4 was contradicted; this run qualifies that for data delivery |

## Gaps

- **The daily summation and completeness rule:** not published. NCEI's USCRN team holds it (ask ncei.orders@noaa.gov).
- **Current calibration procedure**, the weight's certification interval and wetness-sensor calibration: not found. ATDD holds these; ISIS annual-maintenance events are a lead.
- **Not checked:** whether the datalogger program is published, and where NCEI now runs the processing (on-premises or in the cloud).
- **Not read:** the X030–X039 plans and the Site Information Handbook.
- **No NODD copy, THREDDS endpoint or open re3data entry was confirmed.**

## Sources

- NCEI program documents:
  - [OAP 2.0/2.1 Weighted Average Calculation System, 2016](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2016-05/USCRN_OAP2.0+2.1_Weighted_Average_Precipitation_Calculation_System.pdf)
  - [OAP 2.0 Description, 2015](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2015-09/USCRN_OAP2.0.Description_PrecipChanges.pdf)
  - [OAP 2.1 Description, 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/maintenance/2017-06/USCRN_OAP2.1.Description_PrecipChanges.pdf)
  - [TN05-001, 2005](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/technotes/TN05001GeonorAlgorithm.pdf)
  - [Ingest Functional Spec, 2013](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/CRN_Ingest_Functional_Spec.pdf)
  - [Functional Requirements X040, 2007](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X040_d0.pdf)
  - [Field Site Maintenance Plan X041, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/X041_d0.pdf)
  - [Manual Monitoring Handbook, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/ManualMonitoringHandbook.pdf)
  - [Installation Guide, 2003](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN%20Installation%20Guide.pdf)
  - [ATDD/NCDC Documentation Manual, 2002](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/NOAA%20NCDC%20DOCUMENTATION%2007192002.doc)
  - [Data Management Plan, 2017](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/USCRN_Data_Management_Plan-August_2017.pdf)
  - [Duchon, Geonor lab test, 2002](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/research/Geonor-Lab-Test-Report.doc)
  - [CCRs folder](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/CCRs/)
  - [Program folder](https://www.ncei.noaa.gov/pub/data/uscrn/documentation/program/)
  - [Documentation page](https://www.ncei.noaa.gov/access/crn/documentation.html)
- NCEI products and catalog:
  - [daily01 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt)
  - [hourly02 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/hourly02/README.txt)
  - [subhourly01 README](https://www.ncei.noaa.gov/pub/data/uscrn/products/subhourly01/README.txt)
  - [Instruments](https://www.ncei.noaa.gov/access/crn/instruments.html)
  - [C00546 ISO record](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00546) (read via its Wayback copy of 2025-10-09)
  - [ISIS annual maintenance event, 2007](https://www.ncei.noaa.gov/access/isis/event.htm?display=ALLCHANGES&eventid=908)
- ATDD and NCICS:
  - [ARL, USCRN at ARL](https://arl.noaa.gov/uscrn-at-arl)
  - [NCICS, Improving USCRN Precipitation](https://ncics.org/portfolio/observing-systems/uscrn-precipitation-data/)
- WMO:
  - [SPICE Geonor recommendations, 2012](https://old.wmo.int/extranet/pages/prog/www/IMOP/intercomparisons/SPICE/Docs/SPICE%20GEONOR%20Calibration%20and%20Configuration%20Recommendations%20Dec%205,%202012.pdf.pdf)
- Registries and copies:
  - [DataCite 10.7289/V5H13007](https://api.datacite.org/dois/10.7289/V5H13007)
  - [DataCite 10.24381/cds.d1f4864d](https://api.datacite.org/dois/10.24381/cds.d1f4864d)
  - [CDS dataset page](https://cds.climate.copernicus.eu/datasets/insitu-observations-near-surface-temperature-us-climate-reference-network?tab=download)
  - [CDS STAC record](https://cds.climate.copernicus.eu/api/catalogue/v1/collections/insitu-observations-near-surface-temperature-us-climate-reference-network)
  - [USCRN data policy](https://object-store.os-api.cci2.ecmwf.int/cci2-prod-catalogue/licences/uscrn-data-policy/uscrn-data-policy_c37d84a0040855c6c0698de99889a39acd806cceb92273f5a3d9cf293171e960.pdf) (Wayback copy)
  - [ECMWF PUGS](https://confluence.ecmwf.int/spaces/CKB/pages/358884472/Near-surface+temperature+from+US+Climate+Reference+Network+since+2006+onward+Product+User+Guide+and+Specification+PUGS)
