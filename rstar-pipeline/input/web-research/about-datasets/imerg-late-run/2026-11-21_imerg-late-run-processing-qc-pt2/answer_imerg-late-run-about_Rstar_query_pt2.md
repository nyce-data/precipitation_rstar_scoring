# How the IMERG Late Run is produced and quality-controlled (Part 2)

NASA's Precipitation Processing System (PPS) runs one shared IMERG code in its Real Time system. It takes passive-microwave (PMW) brightness temperatures, intercalibrates them to GMI (Level 1C), and turns them into rain rates with GPROF. It then calibrates those rates to the GPM radar-radiometer product (CORRA), fills the gaps between satellite passes with PDIR-Now infrared estimates and a Kalman-filter morphing scheme, and finally applies a climatological adjustment toward the gauge-adjusted Final Run. No gauge data enter the Late Run directly. Quality control is almost entirely automated, with no routine manual inspection, and the files carry a quality index and a random-error field but no QC flag. Overall confidence: **high** for the processing chain and the differences between Runs, which come from the developers' ATBD (August 2026). **Moderate** for the current "hybrid" setup and for Late-Run-specific validation.

## The processing chain (current version: V07B, "hybrid" since March 2026)

| Step | What it is | Measured or computed | Run by |
|---|---|---|---|
| 1. Level 1C intercalibration | Level 1B PMW brightness temperatures from each provider are converted to intercalibrated Level 1C (GMI is the reference; X-CAL offset tables give Tc = Tb + offset) | direct satellite measurements, corrected | PPS (L1CXCAL software), X-CAL working group tables |
| 2. GPROF retrievals | Level 2 precipitation from each PMW sensor (GPROF2021 in V07; GPROF V08 inputs since 2026) | computed (Bayesian retrieval) | GPROF team (CSU) code, run at PPS |
| 3. Intercalibration to CORRA | gridded PMW estimates matched to CORRA by quantile (probability) matching over a trailing 45-day window; GPCP ratio adjustment over high-latitude oceans | computed | IMERG code at PPS |
| 4. IR estimates | PDIR-Now (UC Irvine CHRS) from CPC's merged, zenith-corrected geostationary IR, re-calibrated against IMERG PMW; it replaced PERSIANN-CCS in V07 | IR Tb measured; rain rate computed | CPC (IR), IMERG/PDIR code at PPS |
| 5. Morphing and Kalman filter | PMW moved forward and backward in time along motion vectors from GEOS FP (PRECTOT, then TQL, then TQV), combined with IR by a Kalman filter (from CMORPH), plus SHARPEN | computed | IMERG code at PPS |
| 6. Gauge step | Late: a "Final climatological" calibration by month and location, new in V07; no gauges are read. Final: adjusted to the monthly GPCC satellite-gauge combination | computed (from the Final's gauge-based climatology) | IMERG code at PPS |

Sources: [Huffman et al., ATBD V07, 2026](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf) §3.2.1 and Table 3; [GPM L1C ATBD v1.6, 2016](https://gpm.nasa.gov/sites/default/files/2020-05/L1C_ATBD_v1.6_V04_0.pdf); [IMERG Technical Documentation, 2023](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf); [IMERG V07 Release Notes, 2024](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf); [Nguyen et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8216223/) (PDIR-Now).

The ATBD states that "all of the Runs share a common code". PPS installs a separate copy for each Run: Early and Late run in its Real Time system and Final in its Production system. The Real Time system can't reprocess, so retrospective Late data are computed in Production ([ATBD, 2026](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf)). **High.** No published source names the IMERG code package beyond "the IMERG algorithm". GES DISC archives and distributes the data and has no stated processing role.

**Hybrid mode.** Since 2026, IMERG V07 Early and Late have used "the IMERG V07 algorithm but ingesting GPROF V08". From 1 March 2026, the CORRA calibration in these Runs is set to seasonal climatological values. The April notice expected the switch to V08 for Early and Late "no sooner than fall of 2026". The August update moved this to "no sooner than winter of 2026", and the later date is the current one ([GPM, V08 transition schedule, Apr 2026](https://gpm.nasa.gov/data/news/imerg-v08-transition-schedule); [GPM, Aug 2026 update](https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026)). V07 Early/Late processing itself began on 3 June 2024, once the climatological calibrations to the Final had been computed ([Release Notes](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf)). **Moderate:** only news items describe this setup.

## Where the Late Run differs from Early and Final

ATBD Table 3 lists the differences ([ATBD, 2026](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf)). **High.**

| | Early | **Late** | Final |
|---|---|---|---|
| Latency | 4 h | **12 h** (14 h in the ATBD text) | 3.5 months |
| GPROF product / share of PMW sensors | near-real-time / 95% | **near-real-time / 100%** | climate / 100% |
| CORRA product; calibration window | near-real-time; trailing 45-day | **research; trailing 45-day** | research; centred 45-day |
| Motion vectors | GEOS FP | **GEOS FP** | MERRA-2 |
| PMW propagation | forward only | **forward and backward** | forward and backward |
| Kalman correlation window | trailing 3-month | **trailing 3-month** | 3-month, one month off-centre |
| Gauge adjustment | Final climatological | **Final climatological** | GPCC analysis |
| Liquid-phase source | JMA forecast | **JMA forecast** | ERA5 |
| Manual inspection | none | **none** | visual inspection; bad PMW and IR flagged manually for removal |

On latency, the Technical Documentation gives a nominal 14 h but says recent practice is "more like 12". PPS "waits about 11 hours" to collect the "next overpass" data that the backward propagation needs. In the Kalman filter, IR is used only where no PMW estimate lies within ±30 minutes ([Tech Doc, 2023](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf); [ATBD App. 9](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf)).

## Quality control

QC is done mostly by automated screening of the inputs. In the Late Run, nobody inspects the output routinely.

- **Level 1C flags (automated; GPROF preprocessor, CSU code):** fatal Level 1C errors set brightness temperatures to missing. GPROF records `qualityFlag` (0–3) and `pixelStatus` ([GPROF2021 ATBD, 2022](https://gpm.nasa.gov/sites/default/files/2022-06/ATBD_GPM_V7_GPROF.pdf)). No published source says which `qualityFlag` values IMERG excludes.
- **SPEEDe (automated, plus manual review of its hits; IMERG team):** an auto-encoder that finds GPROF orbits with anomalously high values. It is now run as a post-processor on GPROF orbits. It "is not designed to catch cases where the GPROF estimates are unphysically low". Its 162 bad orbits led to the V07B reprocessing ([Release Notes, 2024](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf)).
- **IR artifact masking (automated in V07; IMERG team):** cold stripes and arcs in the IR field are masked. Arcs are found where pixels below 182 K sit next to missing pixels, and GOES-17 noise where a pixel differs from its neighbours by more than 150 K in total. Before V07 this needed manual work in the Final Run. The Tech Doc introduces the 150 K screen for "post-real-time" V06 "and now V07". Elsewhere it says the GOES-West noise is dealt with in "all V07 Runs", but it never states outright that the Late Run uses this screen. CPC also filters the merged IR before delivering it ([Release Notes](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf); [Tech Doc](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf)).
- **Input-stream screening (PPS):** since July 2023, PPS has screened faulty near-real-time MetOp granules (12 of 16 known cases). It also keeps public anomaly tables for GMI and the partner sensors ([Tech Doc](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf); [PPS partner anomalies](https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/partner_anomalous.html)).
- **Manual handling, case by case:** bad real-time data are stopped by hand. For example, NOAA-19 MHS artifacts went into Early and Late for almost 24 h in October 2017, and those hours were not reprocessed. F17 SSMIS 37V is left out of GPROF ([Tech Doc](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf)). **High.**
- **Recalls:** the October 2026 recall of L3 GPROF V08 (a `precipitationYesNoFlag` bug) says nothing about any effect on IMERG ([Earthdata, 2026](https://www.earthdata.nasa.gov/data/alerts-outages/all-l3-gprof-data-gpm-v08-being-recalled)).

**Fields in the files.** The files carry `precipitation`, `precipitationUncal`, `randomError`, `MWprecipitation`, `MWprecipSource` (sensor index), `MWobservationTime`, `IRprecipitation`, `IRinfluence` (the IR's weight in the Kalman filter, in percent), `probabilityLiquidPrecipitation` and `precipitationQualityIndex`. There is no QC-flag field ([Tech Doc](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf); [PPS File Spec V7.18, 2024](https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/new/filespec.GPM.V7.pdf)). **High.**
- The half-hourly quality index is built from the Kalman-filter correlations of each input against GMI/TMI. Over frozen surfaces it is reduced using NOAA Autosnow. It is set to 0 where only IR within ±12 h fills a gap. Suspect values are left in the files: the user decides whether to discard "red" values ([ATBD App. 9](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf); [V07 FAQ, 2025](https://gpm.nasa.gov/sites/default/files/2025-02/FAQ%20for%20IMERG%20V07%20Applications%20Users_202502.pdf)).
- **Conflict on thresholds:** the 2023 Tech Doc gives 0.4 and 0.6 as the "stoplight" cut-offs, while the 2025 FAQ and the 2026 ATBD give 0.5 and 0.75. I rely on the newer pair.
- No Late-specific QI formula is published. Backward-propagated PMW is "not available for Early", so the Late Run's index can include it.

## Validation against gauges and radar

The IMERG team and NASA's GPM Ground Validation program evaluate the product. They use MRMS radar, the Validation Network and Kwajalein radars, CPC and GPCC gauges, IPWG sites, Pacific atolls and buoys ([ATBD §4](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf); [Tech Doc](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf)). IPWG's daily validation pages include IMERG near-real-time Late ([IPWG Japan site](https://www-ipwg.kugi.kyoto-u.ac.jp/IPWG/python/dailyval.2024.html)). The results feed version upgrades, such as the V06 geolocation error fixed in V07, rather than file-level QC. **Moderate.**

Late-Run-specific results:
- **Developers:** V07 Late test data showed "an appreciable increase in Heidke Skill Score and correlation" and a smaller bias against GV-MRMS (CONUS, Jun–Aug 2014). The numbers are only in a figure ([Release Notes App. 2](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf)).
- **Independent studies:**
  - Sichuan, 723 stations, 2014–21: V07 Late detects precipitation days well ([Li et al., 2025](https://link.springer.com/article/10.1007/s00704-025-05569-x), abstract).
  - Guangxi, 91 gauges, 2014–20: V07, "particularly the Late Run", detects better day to day. Across V07 as a whole (not the Late Run alone), the share of systematic positive bias rose to 67.2–68.9%, from 62.3–64.8% in V06. The study also finds that V07's climatological calibration improved dry-season estimates but "failed during wet season" ([Yang et al., 2026](https://www.mdpi.com/2072-4292/18/17/2867), abstract).

**Moderate.** The NASA Validation Network ocean-radar study covers the Final Run only.

## Documents

| Document | Date |
|---|---|
| [IMERG V07 ATBD](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf) (QI in Appendix 9) | 13 Aug 2026 |
| [IMERG Technical Documentation](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf) | 13 Jul 2023 (latest) |
| [IMERG V07 Release Notes](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf) (also covers V07B) | 20 Nov 2024 |
| [V07 FAQ for applications users](https://gpm.nasa.gov/sites/default/files/2025-02/FAQ%20for%20IMERG%20V07%20Applications%20Users_202502.pdf) | Feb 2025 |
| [PPS File Specification V7.18](https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/new/filespec.GPM.V7.pdf) | 5 Sep 2024 |
| [GPROF2021 ATBD](https://gpm.nasa.gov/sites/default/files/2022-06/ATBD_GPM_V7_GPROF.pdf) | Jun 2022 |
| [Level 1C ATBD v1.6](https://gpm.nasa.gov/sites/default/files/2020-05/L1C_ATBD_v1.6_V04_0.pdf) | 2016 (latest listed) |
| [V08 transition news](https://gpm.nasa.gov/data/news/imerg-v08-transition-schedule) and [Aug 2026 update](https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026) | Apr and Aug 2026 |
| [PPS documentation index](https://arthurhou.pps.eosdis.nasa.gov/GPMprelimdocs.html) | updated 31 Aug 2026 |

## Not published, and other gaps

- **The 2026 hybrid Late Run:** news items only. It isn't in the ATBD, the Tech Doc or the release notes. There is no separate V07B note and no standalone V07 QI document.
- **Level 1C:** no Level 1C ATBD newer than 2016, and no list of the current XCAL table versions.
- **Sensors:** no published list of the sensors active in the current Late Run.
- **Not stated anywhere:** which GPROF `qualityFlag` values IMERG rejects; whether SPEEDe runs before each Late Run or after it; what the 2026 GPROF V08 recall did to the Late Run. The IMERG team at NASA GSFC would hold these, and they may appear in the V08 release notes.
- **GES DISC README:** read through its Wayback copy (Apr 2026). It is a generic GPM README, last revised in 2017, with no IMERG processing or QC detail.
- **Not read in full:**
  - the Wang and Wolff (2025) MRMS study (in preparation);
  - the release notes' figure values;
  - the full texts of the two regional studies (abstracts only).
- **Sandbox:** one host was refused (`www.mdpi.com`; listed in `sites-to-trust.md`). You can decide whether to add it to your sandbox's allowed domains.

## Sources

- NASA GPM / IMERG team: [ATBD V07, 13 Aug 2026](https://gpm.nasa.gov/sites/default/files/2026-08/IMERG_V07_ATBD_final_260813.pdf); [ATBD landing page](https://gpm.nasa.gov/resources/documents/imerg-v07-atbd); [Technical Documentation, 13 Jul 2023](https://gpm.nasa.gov/sites/default/files/2023-07/IMERG_TechnicalDocumentation_final_230713.pdf); [Tech Doc landing page](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation); [V07 Release Notes, 20 Nov 2024](https://gpm.nasa.gov/sites/default/files/2024-12/IMERG_V07_ReleaseNotes_241126.pdf); [FAQ for IMERG V07 Applications Users, Feb 2025](https://gpm.nasa.gov/sites/default/files/2025-02/FAQ%20for%20IMERG%20V07%20Applications%20Users_202502.pdf); [IMERG V08 Transition Schedule, Apr 2026](https://gpm.nasa.gov/data/news/imerg-v08-transition-schedule); [Update to the V08 Transition Schedule, Aug 2026](https://gpm.nasa.gov/data/news/update-imerg-v08-transition-schedule-aug-2026); [GPM Validation page](https://gpm.nasa.gov/science/ground-validation/validation)
- PPS and GPROF: [Level 1C ATBD v1.6, 2016](https://gpm.nasa.gov/sites/default/files/2020-05/L1C_ATBD_v1.6_V04_0.pdf); [L1C ATBD landing page](https://gpm.nasa.gov/resources/documents/gpm-level-1c-algorithm-theoretical-basis-document-atbd); [GPROF2021 ATBD, 2022](https://gpm.nasa.gov/sites/default/files/2022-06/ATBD_GPM_V7_GPROF.pdf); [PPS File Specification V7.18, 2024](https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/new/filespec.GPM.V7.pdf); [PPS documentation index, 2026](https://arthurhou.pps.eosdis.nasa.gov/GPMprelimdocs.html); [PPS partner anomalies table](https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/partner_anomalous.html); [Earthdata, L3 GPROF V08 recall, 2026](https://www.earthdata.nasa.gov/data/alerts-outages/all-l3-gprof-data-gpm-v08-being-recalled)
- Archive: [Earthdata catalog, GPM_3IMERGHHL V07](https://www.earthdata.nasa.gov/data/catalog/ges-disc-gpm-3imerghhl-07); [GES DISC GPM README](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf) (read via Wayback copy)
- Studies: [Nguyen et al., PDIR-Now, J. Hydrometeor. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8216223/); [Li et al., Theor. Appl. Climatol. 2025](https://link.springer.com/article/10.1007/s00704-025-05569-x) (abstract only); [Yang et al., Remote Sens. 2026](https://www.mdpi.com/2072-4292/18/17/2867) (abstract only); [IPWG daily validation, Japan site](https://www-ipwg.kugi.kyoto-u.ac.jp/IPWG/python/dailyval.2024.html) (read by extraction)

Saved in [web_search_results/2026-11-21_imerg-late-run-processing-qc-pt2/](web_search_results/2026-11-21_imerg-late-run-processing-qc-pt2/): this answer, `research-record.json`, `method.md`, `sites-to-trust.md` and `check-by-hand.md`.
