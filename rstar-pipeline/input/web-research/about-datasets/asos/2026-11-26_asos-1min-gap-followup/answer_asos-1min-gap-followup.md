# ASOS 1-minute gap (Aug–Sep 2025): follow-up to Part 4

**Direct answer.** NCEI's own copy is empty for all four month-pages: page 1 and page 2, for August and September 2025. That includes page 1 for September, which the Part 4 run hadn't checked. The observations themselves are not lost, though. The Iowa Environmental Mesonet (IEM) serves 1-minute precipitation for both months at Central Park (NYC) and JFK, with coverage close to the neighbouring months. No NCEI statement about the gap or a refill was found. Confidence is high for NCEI's listings and IEM's data at these two stations, but these are the only stations checked, so this is moderate evidence for the network as a whole.

## Findings

**NCEI page 1, September 2025: empty.** Every file in the listing is 0 bytes. KNYC's reads `asos-1min-pg1-KNYC-202509.dat | 2025-09-03 18:40 | 0`, and no file has a non-zero size ([NCEI listing](https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg1/access/2025/09/), fetched today). Combined with Part 4, all four month-pages (page 1 and page 2, August and September 2025) are empty on NCEI.

**IEM has the data.**
- IEM's 1-minute page says NCEI "provides an archive of one minute interval data from the ASOS sites", that IEM "processes this information and provides it for download", and that the archive runs to 25 Nov 2026 ([IEM](https://mesonet.agron.iastate.edu/request/asos/1min.phtml)).
- IEM's documented download service returned these rows (counted with a script; [request](https://mesonet.agron.iastate.edu/cgi-bin/request/asos1min.py?station=NYC&station=JFK&vars=precip&sts=2025-07-25T00:00Z&ets=2025-10-05T00:00Z&sample=1min&what=view&tz=UTC)):

| Station | Period | Minutes in period | Rows returned | Rows with a precip value | Precip sum (in) |
|---|---|---|---|---|---|
| NYC | 25–31 Jul 2025 | 10,080 | 7,442 | 7,417 | 0.01 |
| NYC | Aug 2025 | 44,640 | 30,727 | 30,638 | 1.21 |
| NYC | Sep 2025 | 43,200 | 31,979 | 31,894 | 2.59 |
| NYC | 1–4 Oct 2025 | 5,760 | 3,878 | 3,865 | 0.00 |
| JFK | 25–31 Jul 2025 | 10,080 | 8,663 | 7,845 | 0.13 |
| JFK | Aug 2025 | 44,640 | 37,256 | 33,718 | 1.70 |
| JFK | Sep 2025 | 43,200 | 38,183 | 36,453 | 2.96 |
| JFK | 1–4 Oct 2025 | 5,760 | 5,760 | 5,735 | 0.00 |

"Minutes in period" is computed from the calendar. The other columns are from the saved IEM response, counted by `work/code/count_iem.py`. NYC returns about 69–74% of minutes in every period, and JFK about 83–100%. So August and September show no hole at IEM that the neighbouring months don't also show.

IEM doesn't say where it got August and September 2025, given that NCEI's files were written empty on 3 September 2025. This could be an earlier NCEI copy or another feed. The sources don't settle it.

**NCEI statement on the gap or a refill:** none found. Neither the Part 4 run's searches of NCEI notices and alerts nor this pass found one.

**Synoptic incident: unrelated.** The page describes Synoptic's own configuration error: "A DNS PTR record update … conflicted with the server's local hostname configuration", which interrupted feeds including "NOAA operational data (such as HADS and ASOS/AWOS)". It was detected after an alert "at 9:27 PM ET on Friday" and recovered by 14 Dec 2025 (marked Resolved 15 Dec 2025; postmortem 5 Jan 2026) ([Synoptic, 2026](https://status.synopticdata.com/incidents/g7nhdhgkqmlc)). That is December 2025, at a private aggregator, so it has nothing to do with NCEI's August–September files.

**H.R. 5089** (the "Weather Act Reauthorization Act of 2025", Rep. Lucas):
- Introduced on 2 Sep 2025.
- On 10 Sep 2025, House Science "Ordered to be Reported (Amended) by Voice Vote". No floor action has followed ([Congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/5089/all-actions)).
- Congress.gov's related-bills list for it doesn't include S. 3923 ([Congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/5089/related-bills)).
- So House Science did approve it, but no official record calls it S. 3923's companion. Its amended text wasn't read.

**WTTW (CNN, 14 May 2025):** of 155 posts NWS sought to fill by voluntary reassignment, "16 electronics technicians, who repair Doppler Radars" were among them ([WTTW/CNN, 2025](https://news.wttw.com/2025/05/14/after-staff-cuts-national-weather-service-now-works-fill-155-critical-vacancies-ahead)). ASOS isn't named.

**Washington Post (6 Dec 2025):** not read. The browser got HTTP 403, as WebFetch did in Part 4.

## Effect on the Part 4 answer

- **Row 9 and D-3:** D-3 stays supported. NCEI's archive has an unannounced two-month hole in its 1-minute data, now confirmed for all four month-pages. But the impact is smaller than Part 4 implied: at the two stations checked, the observations survive in IEM's copy. The rating stays imminent (it already happened), and the wording changes from data "missing from the national archive" to "missing from NCEI's copy; available from IEM".
- **Row 5 (S. 3923):** no change in rating (emerging). The answer now records that House Science approved H.R. 5089 in September 2025, and that Congress.gov doesn't link it to S. 3923.
- **Staff section:** adds the May 2025 count of 16 ET reassignment slots (context; not ASOS-specific). No criterion changes.
- **Synoptic lead:** closed as unrelated.

## Gaps

- IEM was checked at two stations only. A network-wide check would compare IEM row counts with NCEI's July and October files across many stations.
- IEM's source for August–September 2025 isn't stated. IEM's maintainer (Iowa State) could say.
- Whether NCEI will refill its files isn't known; NCEI (ncei.orders@noaa.gov) could say.
- The amended text of H.R. 5089 (whether it has ASOS language) wasn't read. Congress.gov will carry it once the committee files its report.
- The Washington Post article is still unread.

## Sources

- [NCEI, 1-minute page 1, 2025/09 listing](https://www.ncei.noaa.gov/data/automated-surface-observing-system-one-minute-pg1/access/2025/09/)
- [Iowa Environmental Mesonet, ASOS 1-minute download page](https://mesonet.agron.iastate.edu/request/asos/1min.phtml)
- [Iowa Environmental Mesonet, 1-minute data request, NYC and JFK, Jul–Oct 2025](https://mesonet.agron.iastate.edu/cgi-bin/request/asos1min.py?station=NYC&station=JFK&vars=precip&sts=2025-07-25T00:00Z&ets=2025-10-05T00:00Z&sample=1min&what=view&tz=UTC)
- [Synoptic Data, LDM-based data aggregation disruption, 2025–2026](https://status.synopticdata.com/incidents/g7nhdhgkqmlc)
- [Congress.gov, H.R. 5089 actions](https://www.congress.gov/bill/119th-congress/house-bill/5089/all-actions)
- [Congress.gov, H.R. 5089 related bills](https://www.congress.gov/bill/119th-congress/house-bill/5089/related-bills)
- [WTTW (CNN), 155 'Critical' Vacancies, 2025](https://news.wttw.com/2025/05/14/after-staff-cuts-national-weather-service-now-works-fill-155-critical-vacancies-ahead)

Saved in [`web_search_results/2026-11-26_asos-1min-gap-followup/`](web_search_results/2026-11-26_asos-1min-gap-followup/answer.md): this answer and `method.md`. The saved pages and the counting script are in `work/`.
