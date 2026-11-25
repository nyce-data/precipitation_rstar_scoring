# Dataset about pages: agreed format (2026-11-20)

Source spec (user's): `my_docs/about_data/rstar_query_results/dataset_answers/about_dataset_queries/about_pages_format.md`.
Research folders: `.../about_dataset_queries/<folder>/<date>_<topic>-pt<N>/`, each with
`query_questions.txt` (`<Question>` and `<Searched on>`) and an `answer_*.md`
(PERSIANN pt2's is `answer.md`).

## Datasets

| Folder | Dataset (card name) | id in `datasets.json` |
|---|---|---|
| `ghcn-daily` | GHCN-D: Global Historical Climatology Network Daily | `ghcn-d` |
| `gpcp-daily` | GPCP Daily v3.3: Global Precipitation Climatology Project | `gpcp-daily-v3-3` |
| `persiann-cdr-daily` | PERSIANN-CDR v1r1 Daily | `noaa-ncei-persiann-cdr-v1r1` |

The panel's "About dataset: NA" becomes an "About dataset" link (`about_url`)
for these three.

## Decisions

- **Summary page title:** "<short name>: Web research" (short name = card name
  before the colon, e.g. "GPCP Daily v3.3: Web research"), full name as the
  subtitle (e.g. "Global Precipitation Climatology Project"), label line
  "Precipitation workshop / Dataset" like the archive pages. PERSIANN has no
  colon in its name: title "PERSIANN-CDR v1r1 Daily: Web research", no subtitle.
- **Part names:** short topic names, used as the summary-page header and in the
  part page title "<short name>: <topic>". The answer file's own `# ...`
  heading is dropped. Parts in part-number order:
  - GHCN-D: 1 Overview, 2 Quality control and formats, 3 Funding and threats
  - GPCP Daily v3.3: 1 Overview, 2 Quality control and formats, 3 People,
    4 Funding and news, 5 Threats to inputs
  - PERSIANN-CDR v1r1 Daily: 1 Overview, 2 Quality control and formats,
    3 Funding, 4 News, 5 Threats to inputs, 6 Satellites
- **Summary page:** per part: header, link to the part page, "Question: ...",
  "Searched on" list.
- **Part page:** title, "Question: ...", "Searched on" list, then the answer
  with the "Saved in ..." paragraph removed. No R* query box.
- **Links:** "← Back to dashboard" at the top of every page (reopens that
  dataset's card, search/filters kept, as the archive links do); on part
  pages also a link back to the summary page above the content; previous /
  next part links at the bottom of each part page.
- **Questions:** every `<Question>` and `<Searched on>` line is phrased as a
  question; rewrite the ones that aren't and save them in the user's
  `query_questions.txt` files (user said save without review). Bracket notes
  after a question's "?" are worked into the question sentence.
- **Tool notes:** remove "(read via WebFetch)", "WebFetch only", "(WebFetch
  extract)", "(read by extraction)" and similar notes from the answers.

## Open

- Whether to strip the same tool notes from the archive/instrument pages too.
