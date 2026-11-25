# GHCN-Daily: quality control, processing, software and formats (part 2)

NCEI quality-controls GHCN-Daily (current version 3.35) itself. Each time the dataset is rebuilt, a fully automated suite of about 20 tests flags suspect daily values with a one-letter quality flag. The flagged values stay in the files instead of being deleted. Some source networks, such as CoCoRaHS, run their own checks before their data reach NCEI. The processing and QC software is described in two peer-reviewed papers but is not published as code: the QC programs are Fortran 95, and the papers say users can get them through a contact. The data are offered in open, documented text formats, but no access route passes all four FAIR tests. Every route is partly FAIR, mainly because NCEI's own records state no licence and the files use NCEI's own element codes and scaled units. Overall confidence: high for QC and processing, moderate for "code not published" (an absence that couldn't be checked everywhere).

## Quality control

**Yes, QC is done, on every reprocessing, by NCEI** (high). Two steps run:
1. A "format checking program" looks for impossible dates and invalid characters, and "sets the offending records to missing".
2. A "comprehensive sequence of fully-automated quality assurance (QA) procedures" from [Durre et al. (2010)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf) then flags values.

NCEI says the system flags about 0.3% of nearly 2 billion values, and that 98–99% of those are true errors ([NCEI GHCNd product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)). The 2010 paper gives 0.24% of a smaller, earlier dataset. That is a difference in date and dataset size, not a conflict. [Menne et al. 2012](https://www.ncei.noaa.gov/pub/data/ushcn/papers/menne-etal2012.pdf) puts the base at "over 2 billion" values. That is a rounding difference from NCEI's "nearly 2 billion", and this answer uses NCEI's current wording. Each test was tuned to a false-positive rate of no more than 20%.

**The checks** listed on the [NCEI product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily), with the flag each sets in the [readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt):

| Check | What it flags | Flag |
|---|---|---|
| Trace flag consistency | a trace flag on a nonzero amount | not stated |
| Naught | max and min temperature both 0 °C (or both −17.8 °C at US stations) | N |
| Duplicate | data copied between years, months, or months within a year | D |
| World record exceedance | values outside the highest or lowest ever observed | X (bounds) |
| Streak | runs of identical values (for example 20+ days of temperature) | K |
| Frequent value | clusters of 5–9 identical moderate-to-heavy precipitation totals | K |
| Gap | values far from the rest of the station's distribution for that month | G |
| Climatological outlier (z-score, percentile) | temperature 6 standard deviations from the 15-day mean; precipitation a set factor above the 29-day 95th percentile | O |
| Internal temperature consistency | max, min and observation-time temperature that disagree within 3 days | I |
| Temporal consistency (spike or dip) | max or min more than 25 °C from both the day before and the day after | T |
| Lagged temperature range | max at least 40 °C above the minimums of nearby days | R |
| Pan vs air temperature | inconsistent evaporation-pan temperatures (flags the pan value) | not stated |
| Snow–temperature (warm) | snowfall when the minimum temperature is 7 °C or warmer | W |
| Snowfall vs snow-depth increase; snow vs precipitation ratio | snow-depth or snowfall totals that don't match each other or the precipitation | not stated |
| Spatial consistency (4 checks) | regression residuals; anomalies or precipitation disagreeing with neighbours; snow when every neighbour was warm | S |
| Megaconsistency | for example a max below the station's lowest min for the month; warm-season snow at stations with no cold-season snow | M |
| Date-based snow outlier | snow out of season (false-positive rate 50–75%, by NCEI's account) | not stated |
| Multiday period length | accumulation periods that are too long | L |
| Datzilla investigation | values flagged after an NCEI ticket review | Z |

The product page doesn't map each check to a letter. The letters above come from the readme's flag names, so a cell marked "not stated" is a gap in NCEI's documentation, not in this research.

**Automated or manual** (high). The tests are "fully automated", and they were "manually validated" only to set thresholds. The developers call manual verification "impractical" at this scale, so the system runs "unsupervised" ([Durre et al. 2010](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf); [Menne et al. 2012](https://www.ncei.noaa.gov/pub/data/ushcn/papers/menne-etal2012.pdf)). There is one human channel: NCEI's "Datzilla Gatekeeper" investigates values raised by tickets, and the outcome is flag Z ([NCEI slides for CoCoRaHS, 2022](https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf)). How Datzilla works is not publicly documented.

**Flagged, not removed** (moderate). Each value carries a QFLAG, and blank means "did not fail any quality assurance check" ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)). NCEI also publishes the failed values for US COOP, CoCoRaHS and ASOS/AWOS stations by NWS forecast office ([nws/ readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/nws/readme.txt)). No NCEI sentence says in so many words that flagged values are never deleted. Data are removed outright in two cases:
- malformed records, which the format check sets to missing;
- whole stations, which integration screening "quarantined", "eliminated" or "removed" ([Menne et al. 2012](https://www.ncei.noaa.gov/pub/data/ushcn/papers/menne-etal2012.pdf)).

**Who** (moderate). NCEI runs all GHCN-Daily QC. Some source networks check their data first:
- **CoCoRaHS** uses "a mix of automated and manual processes": checks on its entry forms, plus a daily review by headquarters staff and volunteer coordinators. CoCoRaHS data are "continually streamed" to NCEI, and a station enters GHCN-Daily once it has at least 100 values for one element. GHCN-Daily then applies its own checks ([CoCoRaHS QA/QC, 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf)).
- **US COOP:** NCEI's Summary of the Day file (DSI-3210) "contains flagged data that have been quality controlled by personnel at the NCDC" ([NCEI record C00314](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00314/html)).
- **Foreign national weather services:** what QC they do was not found.

GHCN-Daily is not homogenized: no bias adjustments are made ([NCEI product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)).

## Other processing

All of this is from NCEI's own documentation and Menne et al. 2012 (high).
- **Integration** ([product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily); [Menne et al. 2012](https://www.ncei.noaa.gov/pub/data/ushcn/papers/menne-etal2012.pdf)) runs in three steps:
  1. screen out stations with unknown or questionable locations;
  2. classify each source station as already in GHCNd or new: matched by ID, then cross-reference lists (NCEI's station history records), then data similarity (at least a 50% match and within 40 km);
  3. "mingle" the sources by a precedence hierarchy. Sources that have had the most scrutiny come first: COOP in the US, and official government exchange data over the "International Collection".

  The first two steps run when a new source arrives; mingling is part of the regular automated run.
- **Source tracking:** each value carries a source flag (SFLAG). The readme lists the codes and the priority order, and `mingle-list.txt` ranks each station's sources ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)).
- **Updates and versions:** the data are updated daily and rebuilt in full periodically. An older NCEI page says "each weekend", from "25-plus" sources ([NCEI 2020, Wayback copy](https://web.archive.org/web/20201218051149/https://www.ncdc.noaa.gov/ghcn-daily-description)). The version is "3.35-upd-2026111517" ([ghcnd-version.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt)), and the changes between versions are logged in [status.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt). Recent versions:
  - v3.33 (January 5, 2026) added the Synoptic Summary of the Day v2, derived from GHCNh;
  - v3.34 (January 23, 2026) added NWS "CF6" daily summaries;
  - v3.35 (October 1, 2026) resumed Environment Canada updates, with a weekly re-integration of the full period of record.

  Real-time data streams are "replaced by archive-ready data sources 45 to 60 days after the end of a month" ([product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)).
- **Output files:** per-station `.dly` files (all, GSN and HCN subsets), daily-updated `by_year` CSVs ([readme-by_year](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme-by_year.txt)), `by_station` CSVs, and `superghcnd` full and diff files. The diff files hold value-level update, insert and delete lists between versions ([superghcnd full](https://www.ncei.noaa.gov/pub/data/ghcn/daily/superghcnd/readme-superghcnd_full.txt), [diff](https://www.ncei.noaa.gov/pub/data/ghcn/daily/superghcnd/readme-superghcnd_diff.txt)).
- **Named software:** none is named beyond the "format checking program" and the QA system. The integration and file-writing programs have no public names.

## Can the public inspect and use the software?

| Software or algorithm | Code published? | Where it is described |
|---|---|---|
| QA tests (19 tests in 2010, about 20 now) | **No.** "written in FORTRAN 95 on a Linux platform"; users "may visit the GHCN-Daily Web page for the appropriate point of contact" | [Durre et al. 2010](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf), [Durre et al. 2008](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/) |
| Integration, mingling, format check, file production | **No.** Menne et al. say each version is archived "along with the latest processing source code", but give no public location | [Menne et al. 2012](https://www.ncei.noaa.gov/pub/data/ushcn/papers/menne-etal2012.pdf), [product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) |
| NCEI code locations checked | none hold GHCN-Daily code: the [GHCN-Daily folder](https://www.ncei.noaa.gov/pub/data/ghcn/daily/) and its [papers/](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/) folder; GitHub org [NCEI-NOAAGov](https://github.com/NCEI-NOAAGov) (11 repositories, none on GHCN) and org `ncei` (no public repositories) | — |
| For contrast, related NCEI code | GHCNm v4 source, "provided for inspection, but without any support" and pulled from NCEI's "internal Git" ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/v4/source_code/ghcnm_doc_readme.txt)); the PHA homogenization code ([52i](https://www.ncei.noaa.gov/pub/data/ghcn/v3/software/52i/readme.quick_start)). Neither states a licence | — |
| Third-party readers (not NOAA) | Yes: for example [rnoaa](https://github.com/ropensci/rnoaa) (MIT, being archived), a [Zenodo converter](https://zenodo.org/records/4518811) (CC BY 4.0), and many [GitHub readers](https://github.com/search?q=ghcnd&type=repositories) | — |

Confidence: moderate. Two places couldn't be checked: code.noaa.gov (the host didn't resolve, and the Wayback Machine has no copy) and the GitHub API (the sandbox refused it). So "not published" means not found in NCEI's folders, its GitHub organizations, or web and DuckDuckGo searches.

## Formats and access routes, rated FAIR

| Route | Formats | F | A | I | R | Rating |
|---|---|---|---|---|---|---|
| NCEI HTTPS: [/pub/data/ghcn/daily/](https://www.ncei.noaa.gov/pub/data/ghcn/daily/) and [/data/…-daily/](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/) | fixed-width `.dly`, CSV (by_year, by_station), superghcnd CSV, tar.gz | pass | pass | fails standard names | fails licence | partly FAIR (fails I, R) |
| [NCEI Access Data Service](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation) (`daily-summaries`) | CSV, SSV, JSON, PDF, NetCDF "Depending on the dataset" | pass (via DOI and NCEI catalog) | pass: no token; an anonymous JSON test worked | fails: element codes, no units in default output; netCDF came back empty in one test | fails licence | partly FAIR (fails I, R) |
| [CDO web services v2](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) | JSON | pass | **fails**: "An access token is required", got by email registration; limited to "five requests per second and 10,000 requests per day" | fails standard names | fails licence | partly FAIR (fails A, I, R) |
| [CDO search and order](https://www.ncdc.noaa.gov/cdo-web/faq) | orders (file formats not checked) | pass | **fails**: orders are "delivered to your email inbox", so it isn't a direct download | fails standard names | fails licence | partly FAIR (fails A, I, R) |
| [AWS noaa-ghcn-pds](https://registry.opendata.aws/noaa-ghcn/) | CSV, CSV.gz, Parquet | pass (registry entry) | pass: anonymous S3 or HTTPS (`--no-sign-request`) | partly: open formats, but the parquet schema and units aren't given in the [bucket readme](https://noaa-ghcn-pds.s3.amazonaws.com/readme.txt) or [NODD readme](https://github.com/NOAA-Big-Data-Program/bdp-data-docs/tree/main/GHCN-D) | pass: CC0-1.0 stated | partly FAIR (fails I) |
| [Google BigQuery](https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d) | BigQuery tables (SQL) | pass (Marketplace listing) | **fails**: needs a Google Cloud account and project ([Google](https://cloud.google.com/bigquery/public-data)); free up to 1 TB a month | partly: proprietary query service | partly: points to the data.gov policy, "AS IS" | partly FAIR (fails A; I and R partly) |

How the tests were judged:
- **Findable:** every route shares DOI [10.7289/V5D21VHZ](https://api.datacite.org/dois/10.7289/V5D21VHZ), which resolves to NCEI's ISO record [C00861](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html); the dataset is also on [data.gov](https://catalog.data.gov/dataset/global-historical-climatology-network-daily-ghcn-daily-version-3). The DataCite record is thin: its formats, subjects and rights fields are empty. data.gov shows `accessLevel` "non-public" and a 2012 modified date. Both are metadata faults, not access barriers.
- **Interoperable:** the formats are open and documented in NCEI readmes, but variables use NCEI element codes in scaled units ("PRCP = Precipitation (tenths of mm)", "TMAX = Maximum temperature (tenths of degrees C)"), not CF standard names ([readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)). Some documentation links are broken: `GHCND_sample.csv` returns 404, and `superghcnd/readme.txt` is missing.
- **Reusable:** provenance is strong on every NCEI route: per-value source and quality flags, the version file and the change log. The licence is the weak point (see the conflict below).

## Conflicting evidence: the licence

The [AWS registry](https://registry.opendata.aws/noaa-ghcn/) and [data.gov](https://catalog.data.gov/dataset/global-historical-climatology-network-daily-ghcn-daily-version-3) say CC0-1.0. NCEI's own [ISO record](https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C00861.xml) gives only a citation request and liability disclaimers, and the [DataCite record](https://api.datacite.org/dois/10.7289/V5D21VHZ) and [readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt) state no licence. No NCEI page found calls GHCN-Daily public domain. I treat CC0 as stated only on the AWS and data.gov routes. On NCEI's own routes the licence is unstated, so they fail R. US government works are generally public domain, but that is my reading, not NCEI's statement.

## Gaps and uncertainties

- **QC by foreign national weather services and by NWS COOP** before data reach NCEI: not found, and not searched for foreign services (time). The holders are the national services, through WMO exchange, and NWS.
- **The Datzilla procedure** (who sets flag Z, and whether values are corrected): unpublished. The NWS directive that mentions it returned HTTP 403 and has no Wayback copy. NCEI holds this; ask ncdc.ghcnd@noaa.gov.
- **Whether NCEI shares the GHCN-Daily code on request:** not known. Durre et al. point to a contact, and the GHCNm readme offers its code by email; the GHCN-Daily equivalent is ncdc.ghcnd@noaa.gov.
- **Not read:**
  - the netCDF output and CF names from the Access Data Service (one empty response);
  - the AWS parquet and BigQuery schemas;
  - the `access/` and `archive/` folders of NCEI's direct-download tree.
- Pages to open by hand are listed in `check-by-hand.md` (4 pages). The sandbox refused 6 hosts, listed in `sites-to-trust.md`; you can decide whether to add any of them to your allowed domains.
- The research stopped at the run's planned research stop (time), not at saturation.

## Sources

- [NCEI, Global Historical Climatology Network daily (GHCNd) product page](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)
- [NCEI, GHCN-Daily readme.txt, v3.35](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)
- [NCEI, nws/ readme (failed values by WFO)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/nws/readme.txt)
- [NCEI, ghcnd-version.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-version.txt)
- [NCEI, status.txt (version log)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/status.txt)
- [NCEI, readme-by_year.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme-by_year.txt)
- [NCEI, readme-superghcnd_full.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/superghcnd/readme-superghcnd_full.txt)
- [NCEI, readme-superghcnd_diff.txt](https://www.ncei.noaa.gov/pub/data/ghcn/daily/superghcnd/readme-superghcnd_diff.txt)
- [NCEI, /pub/data/ghcn/daily/ directory listing](https://www.ncei.noaa.gov/pub/data/ghcn/daily/)
- [NCEI, papers/ directory listing](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/)
- [NCEI, direct-download tree](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/)
- [NCEI, GHCN-Daily description page, 2020 (Wayback copy)](https://web.archive.org/web/20201218051149/https://www.ncdc.noaa.gov/ghcn-daily-description)
- [NCEI, ISO metadata record C00861 (Geoportal)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html)
- [NOAA, ISO metadata record C00861 (WAF XML)](https://data.noaa.gov/waf/NOAA/NESDIS/ncei/aim/iso/xml/C00861.xml)
- [NCEI, ISO record C00314, U.S. Daily Surface Data (COOP)](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00314/html)
- [NCEI, Access Data Service API documentation](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation)
- [NCEI, CDO web services v2](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)
- [NCEI, CDO FAQ](https://www.ncdc.noaa.gov/cdo-web/faq)
- [NCEI, GHCNm v4 source-code readme](https://www.ncei.noaa.gov/pub/data/ghcn/v4/source_code/ghcnm_doc_readme.txt)
- [NCEI, PHA 52i readme](https://www.ncei.noaa.gov/pub/data/ghcn/v3/software/52i/readme.quick_start)
- [NCEI, slides for CoCoRaHS WERA 2022 (Datzilla)](https://media.cocorahs.org/docs/WERA1012_2022_NCEI.pdf)
- [Durre, Menne, Gleason, Houston and Vose, 2010, Comprehensive automated quality assurance of daily surface observations, JAMC 49, doi:10.1175/2010JAMC2375.1 (NCEI copy)](https://www.ncei.noaa.gov/pub/data/ghcn/daily/papers/durre-menne-etal2010.pdf)
- [Menne, Durre, Vose, Gleason and Houston, 2012, An overview of the GHCN-Daily database, JTECH 29, doi:10.1175/JTECH-D-11-00103.1 (NCEI copy)](https://www.ncei.noaa.gov/pub/data/ushcn/papers/menne-etal2012.pdf)
- [CoCoRaHS, Data Quality Assurance and Quality Control, 2019](https://media.cocorahs.org/docs/CoCoRaHS_QA_QC_April_2019.pdf)
- [DataCite, record for 10.7289/V5D21VHZ](https://api.datacite.org/dois/10.7289/V5D21VHZ)
- [data.gov, GHCN-Daily Version 3 catalog entry](https://catalog.data.gov/dataset/global-historical-climatology-network-daily-ghcn-daily-version-3)
- [AWS Registry of Open Data, noaa-ghcn](https://registry.opendata.aws/noaa-ghcn/)
- [AWS, noaa-ghcn-pds bucket readme](https://noaa-ghcn-pds.s3.amazonaws.com/readme.txt)
- [NOAA NODD, GHCN-D readme on GitHub](https://github.com/NOAA-Big-Data-Program/bdp-data-docs/tree/main/GHCN-D)
- [Google Cloud Marketplace, GHCN Daily](https://console.cloud.google.com/marketplace/details/noaa-public/ghcn-d)
- [Google Cloud, BigQuery public datasets](https://cloud.google.com/bigquery/public-data)
- [GitHub, NCEI-NOAAGov organization](https://github.com/NCEI-NOAAGov)
- [GitHub, repository search "ghcnd"](https://github.com/search?q=ghcnd&type=repositories)
- [rOpenSci, rnoaa](https://github.com/ropensci/rnoaa)
- [Zenodo, record 4518811 (GHCN-D converter)](https://zenodo.org/records/4518811)

Saved in [`web_search_results/2026-11-19_ghcn-daily-about-pt2/`](./): this answer, `method.md`, `research-record.json`, `check-by-hand.md` and `sites-to-trust.md`.
