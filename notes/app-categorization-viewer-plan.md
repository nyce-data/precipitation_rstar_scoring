# Plan: R* categorization viewer (app/)

A static website for reading the R* categorizations in a local browser.
Written 2026-11-22. Covers the first version only; the network and knowledge graph app comes later. The weighted network graph was added on 2026-11-24 as `app/graph.html` (see `app/README.md` and
`notes/score-graph-evidence-nodes-plan.md`); the knowledge graph is still to come.

## Constraints

- **Opens straight from disk.** You open `app/index.html` by double-clicking it (`file://`), with no server. Browsers block `fetch()` of local JSON files on `file://`. So a build script turns the JSON and markdown into one JavaScript data file that the pages load with a plain `<script>` tag.
- **The sources stay where they are.** The definitions stay in `rstar_definitions/*.md`, the categorizations in `data-rstar-categories/datasets/<dataset>/*.json`, the point values and weights in `docs/scoring/how_to_score_rstar.md`, and the dataset names in `datasets_metadata/json/`. Re-run the build script after any of them change.
- **No dependencies.** Plain HTML, CSS and JavaScript, plus Python's standard library for the build step. Nothing to install.

## Files

```
app/
  index.html                       landing page
  people-risk.html                 one page per category (thin shells)
  data-risk.html
  dependent-infrastructure.html
  repository-resilience.html
  assets/styles.css                shared styles (light and dark)
  assets/app.js                    renders the landing and category pages
  data/rstar-data.js               GENERATED: window.RSTAR_DATA = {...}
  scripts/build_data.py            builds data/rstar-data.js
  README.md                        how to build and open
```

## Data the build script collects

- **Categories (4):** the key (`people_risk`, ...), the title, the "defined" paragraph, the group weight in the R* formula (0.40 D, 0.30 P, 0.20 RRS, 0.10 DIRS) and the page file.
- **Subcategories (19):** the ID, a short title (the first line under `#### Description`), the description, the "How to find" text and the point value (for example P-1 = 35).
- **Datasets:** every folder in `data-rstar-categories/datasets/` that has a JSON file. Each gets its display name from the dataset metadata, and its subcategory HTML. Folders without a JSON file (gpcp-daily, persiann-cdr-daily for now) are listed as "not categorized yet".

## Landing page (`index.html`)

1. **Header:** "R* categorizations", plus a dataset selector (only GHCN-Daily has data now). The choice is kept in the URL (`?dataset=ghcn-daily`), so every link carries it.
2. **Dataset strip:** name, archive, DOI, curator and update status, from the dataset metadata.
3. **Four category cards in a grid**, one per category. Each card shows:
   - the title and its weight in R*;
   - the definition paragraph;
   - its subcategory IDs as chips, each marked filled, thin (1–3 evidence items) or empty for the chosen dataset;
   - a link to the category page.

## Category page (for example `people-risk.html?dataset=ghcn-daily`)

1. **Breadcrumb** back to the landing page, plus the category title, definition and weight.
2. **A toolbar** with Expand all and Collapse all buttons, and links to the other three categories.
3. **One horizontal card per subcategory, stacked full width.** The card header (a button) shows:
   - the ID badge (P-1) and short title ("No documented succession plan"), with the point value;
   - **Description** and **How to find**, side by side on wide screens and stacked on phones;
   - a coverage line: "9 evidence items · 1 gap", or "No evidence found";
   - a chevron arrow on the right that turns when the card is open.
4. **Clicking the card** (or pressing Enter or Space on it) opens a panel below it with the categorization HTML:
   - Evidence and Gaps lists, as written in the JSON;
   - each evidence item has a confidence badge (high, moderate or low, colour-coded) and a small tag naming its source run (for example `about-pt1`, with the full folder name on hover);
   - links open in a new tab.
5. **Deep links:** `#P-3` opens and scrolls to that card, so you can bookmark or share a subcategory.

## Accessibility and layout

- Each card header is a `<button aria-expanded>` that controls its panel region. It works with the keyboard and screen readers.
- Readable text width, works at phone width, light and dark themes follow the system setting, and visible focus outlines.

## Later (not in this version)

- Filter by confidence, or show only gaps.
- Side-by-side comparison of datasets for one subcategory.
- Score entry for each subcategory (0 or the point value), feeding the R* formula.
