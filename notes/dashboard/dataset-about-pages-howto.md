# How the dataset about pages are built (and how to add more)

Built 2026-11-20 (session 9) in the workshop dashboard project, whose
paths this note still uses in places: `scripts/` is now
`rstar-pipeline/processing/scripts/dashboard/`, and the research root is
now `rstar-pipeline/input/web-research/about-datasets/`. The agreed format
is in `notes/dashboard/dataset-about-pages-plan.md`; the user's original
spec was in that project's `my_docs/` (archived outside this project).

## The pieces

| File | What it does |
|---|---|
| `app/data/dataset_pages.json` | **The list to edit.** One entry per dataset: `id` (as in `datasets.json`), `research_folder` (folder under the research root), `parts` (`part` number + short `topic`, and optionally `folder`), in part order. `folder` names the run folder when the `-pt<N>` ending doesn't pick one: when one query file held two runs, Run 2 gets the next part number and its own folder (for example `{ "part": 8, "topic": "…", "folder": "2026-11-24_gpcp-daily-calibration-copies-pt7" }`, and part 7 names `…-people-production-pt7`). |
| `scripts/import_dataset_pages.py` | Reads that list and copies each part's answer and questions into `app/content/datasets/<id>/`. Since 2026-11-25 `build_datasets.py` (run after it) sets `about_url` on the cards from the same list. |
| `scripts/research_text.py` | `strip_tool_notes()` (removes "(read via WebFetch)" etc.) and `tool_mentions()` (finds lines still naming a tool). Also used by `import_archive_page.py`. |
| `scripts/import_archive_page.py` | Its `clean()` (drops "Saved in …" and everything after, "Pages to check by hand"/"Sandbox" bullets, sentences naming research files such as `check-by-hand.md`, and tool notes) is reused by the dataset script. |
| `app/content/datasets/<id>/pt<N>.md` | Answer text, cleaned, with its first `# ` heading removed. Generated: don't edit by hand, re-run the script. |
| `app/content/datasets/<id>/pt<N>.json` | `{ "question": …, "searched_on": [ … ] }` from `query_questions.txt`. Generated. |
| `app/dataset.html`, `app/dataset.js` | The page. `dataset.html?id=<id>` = summary page; `&part=<N>` = one part's page. |
| `app/dataset-search.js` | The search box: searches this one dataset's parts (see "Search" below). |
| `app/markdown.js` | `renderMarkdown(text, { headingIds: true })` gives headings ids (`sec-<slug>`); `markdownPlainText()` and `markdownHeadingIds()` let the search index use the same text and ids. |
| `app/app.js` (`aboutHref`) | The panel's "Dataset web research" link adds the search/filters and `open=<id>` to a `dataset.html?…` about_url. |
| `app/styles.css` section 13c | Dataset page styles (reuses the archive page's `.prose`, `.research-scope`, `.searched-on`). |

Research root: `rstar-pipeline/input/web-research/about-datasets/` (was the old project's `my_docs/` copy). Since
2026-11-27 every run folder there has a reworded `query_questions.txt`; `notes/dashboard/web-research-prep-howto.md`
covers copying new runs in and preparing their question files, and lists what still blocks a re-run (two pt7
folders in GPCP and IMERG; GHCN-Daily's `about-pt3_combined`).
Each part folder is `<research_folder>/<date>_<anything>-pt<N>/` and holds one
`answer*.md` and a `query_questions.txt`:

```
<Question>

The main question?

<Searched on>

First searched-on question?

Second one?
```

## Page layout (what dataset.js renders)

- Header: "← Back to dashboard" (→ `index.html?<search/filters>&open=<…,id>#dataset-<id>`,
  so the card is open and scrolled to), label line, `<h1>`, subtitle, meta line.
  - Title: card name before the first ": " + ": Web research" (summary) or
    + ": <topic>" (part). Subtitle: the card name after ": " (none if no colon).
- Summary: one `<section>` per part: `<h2>` topic, link "Read the web research: <topic>",
  Question, "Searched on" (`<h3>`) list.
- Part: "← Back to <short name> web research" link, "Question" `<h2>` with the
  question as a paragraph, "Searched on" `<h3>` and list,
  the answer (its `##` sections render as `<h2>`), then previous/next links.
- Every link between these pages carries the dashboard's q/category/coverage/open.

## Search (session 9)

- A search box under the header on the summary and part pages. It searches
  only this dataset's research: every part's question, "Searched on" list
  and answer text (link labels, not link addresses).
- Each part is split into sections at its headings ("Introduction" = text
  before the first heading; "Question and Searched on" = the .json). A
  section matches when it contains every typed word, as substrings, case
  ignored (same rule as the dashboard search; "goes" also matches "GOES").
  At least 2 characters; 200 ms after typing stops.
- The parts' files are fetched on the first search and kept.
- Results replace the page content: grouped by part, one line per section
  with a match count and a snippet with `<mark>` highlights; "Sources"
  sections last. A screen-reader status says "Found in N sections on M
  pages".
- A result opens `dataset.html?id=…&part=N&rq=<words>#sec-<slug>`: the
  part page highlights the words, shows "Matches for … are highlighted.
  Back to search results", and scrolls to the first match in that section.
  Previous/next links keep `rq`; clearing the box removes highlights and
  `rq`. On the summary page, `rq` in the URL shows the results at once.
- "Back to dashboard" drops `rq` (only q/category/coverage/open go back).
- New parts are searchable as soon as the import script has run.

## Adding research

### A new part for a dataset that already has pages

1. Make sure the new folder ends in `-pt<N>` and has one `answer*.md` and a
   `query_questions.txt`.
2. Check `query_questions.txt`: every line under `<Question>` and
   `<Searched on>` must be a question (rewrite and save in the user's file;
   work any bracket note after the "?" into the sentence).
3. Add `{ "part": N, "topic": "<short topic>" }` to that dataset's `parts`
   in `app/data/dataset_pages.json`, in part-number order. Reuse topic names
   already in use where they fit (Overview; Quality control and formats;
   Processing and quality control; Formats and people; People; Funding;
   News; Funding and news; Threats and news; Threats to inputs; Satellites;
   People and production; Calibration and copies; Repository;
   Infrastructure; Repository resilience) and ask the user for new ones.
   ("Funding and threats" was GHCN-Daily's old pt3, the combined run, retired
   2026-11-27.)
4. From the project folder: `python3 scripts/import_dataset_pages.py`
   (`PYTHONPYCACHEPREFIX=$PWD/.work/pyc` keeps `__pycache__` out of `scripts/`).
5. Read the `check:` lines it prints. Lines that still mention WebFetch or a
   subagent inside a sentence (usually in "Gaps") are left as is unless the
   user says otherwise; if a new kind of bracketed tool note slips through,
   extend the patterns in `scripts/research_text.py`.
6. Check in the browser: summary page, the new part, prev/next links,
   "Back to dashboard". Remind the user to hard-reload (Cmd+Shift+R).

### A new dataset

1. Find its `id` in its metadata file in `rstar-pipeline/input/dataset-metadata/`
   (the user tells which research folder maps to which dataset name).
2. Add an entry to `app/data/dataset_pages.json` (`id`, `research_folder`,
   `parts`), then steps 2–6 above, then run `build_datasets.py`. It sets
   the dataset's `about_url` to `dataset.html?id=<id>`, which turns the
   panel's "Dataset web research: NA" into a link.

### Re-running

The script rewrites every listed part each time; it is safe to re-run
after the user edits an answer or a question file. It no longer writes
`datasets.json` (`build_datasets.py` does).

## Things to watch for

- Folder dates don't follow part order (queries were run out of order):
  only the `-pt<N>` ending matters, unless the part names its `folder`.
- GPCP and IMERG each have two `-pt7` folders (Run 1 and Run 2 of one query
  file). The script stops on those unless both parts name their `folder`;
  Run 2 is shown as part 8 (user's choice, 2026-11-27).
- Answer files may be named differently (`answer.md` vs `answer_*.md`);
  the script takes the one `answer*.md` in the folder and stops if there
  are zero or several.
- Bullet labels change between runs: GPCP pt6 (2026-11-20) wrote
  "**Pages to check by hand.**" and "**Hosts refused.**" (period, not
  colon), which left empty bullets until they were added to
  `DROP_ITEM_PREFIXES` in `scripts/import_archive_page.py`. After each
  import, look at the end of "Gaps" for a bullet cut short.
- At the user's request (2026-11-20), "**The token budget ended the
  research**…" bullets (GPCP pt6, GHCN-D pt3) are dropped by a
  `DROP_ITEM_PREFIXES` entry.
- Research-file and sandbox notes (2026-11-27, `import_archive_page.py`):
  bullets that start with `` `check-by-hand.md` ``, `` `sites-to-trust.md` ``
  or a link to either are dropped, and so is any bullet telling the reader to
  check "your (sandbox's) allowed domains". When a sentence naming a research
  file is removed, a bullet's `**Label:**` is kept if other text remains.
  After an import, grep `app/content/datasets` for `check-by-hand`,
  `sites-to-trust`, `allowed domains` and lines starting `- md\``.
- Notes on how a run stopped (time or token budget, "research stop") are
  kept, except "**The token budget ended the research**" bullets; GHCN-Daily
  pt2/pt4/pt5, GPCP pt2 and IMERG pt3 have some.
- Links to `./` or `web_search_results/` (research-project files) are
  reported as `check:` lines; fix by hand or with a `--replace`-style edit.
- Tool notes left in prose on purpose (2026-11-20): GPCP pt3 "Gaps"
  (WebFetch 404, checking subagent not run), GPCP pt5 "No checking subagent
  was run", PERSIANN pt2 maturity-matrix note, PERSIANN pt4 note under the
  ratings table, PERSIANN pt6 "The checking subagent reports…", NCEI archive
  page line 34 "the article or the extract".
