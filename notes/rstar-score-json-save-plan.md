# Plan: saving chosen R* scores to JSON files

Status: built 2026-11-23 with the user's answers below, except "Load a saved file" (not asked for yet) and the
analysis script. The format changes for the colleague are in `notes/rstar-json-format-changes.md`; the schema is
`app/schema/rstar-assessment.schema.json`.

## The user's answers (2026-11-23)

1. Save downloads the file to the scorer's computer. A server is for later.
2. The colleague's point values are right: P-3 = 25, DIRS-2 = 25, DIRS-4 = 15 (applied in
   `docs/scoring/how_to_score_rstar.md`).
3. NA is saved as `null`.
4. Keys may be added: an `assessor` block (name, email, role).
5. A notes box on each card, saved into the category's `justification`.
6. The colleague's definition wording (the extra sentences were added to D, P and RRS in `rstar_definitions/`).
7. `scoringMethod` is kept but left `""` (the colleague scored RRS another way and may add a value later).
8. `dataset.identifier` is the DOI, or a data endpoint URL when there is no DOI.
9. Saving with NA is allowed, with a note that NA values are included.
10. Research scores are left out of the file.

The sections below are the original plan; where they differ from the answers above, the answers win.

## Goal

The viewer shows the people scoring a dataset all the evidence. They then choose a final score for each subcategory
(full points, 0 or NA) from that evidence and from what they know that a web search couldn't find. Many people will
score the same datasets. Each person's choices need to be saved with a timestamp and collected later for analysis.

The saved file must use the format of a colleague's R* score form:
`docs/json_output/example_rstar_json.json`. Fields the viewer can't fill yet stay empty.

## Decisions for the user

Each has a recommendation. Details are in the sections below.

1. **Where saved files go** (the biggest decision). The site is static files, and a browser page can't write into a
   shared folder by itself. Recommended: start with **Save downloads a file** to the scorer's computer, and they send it
   to you (option A). Move to a small shared server (option B) if many people will score at once, for example at a
   workshop. See "Where the files go".
2. **Point values that differ from the colleague's form.** Three subcategories have different maximum points:

   | Subcategory | This project (`docs/scoring/how_to_score_rstar.md`) | Colleague's form |
   |---|---|---|
   | P-3 Critical undocumented knowledge | 20 | 25 |
   | DIRS-2 Observation network or sensor platform at risk | 20 | 25 |
   | DIRS-4 External processing infrastructure dependency | 20 | 15 |

   This project's P values add up to 95, not 100, so P-3 = 25 looks right. Which set should the viewer and the saved
   files use? Recommended: the colleague's, so the files can be compared, after updating `how_to_score_rstar.md`.
3. **How to save NA.** The form has no NA: each factor has `present` true or false. Recommended: save NA as
   `"present": null, "points": null`, and then the category's `rawScore`, `weightedContribution`, the composite
   score and the triage tier are `null` too. The alternative is the string `"NA"` in those fields, which is easier to
   read but makes the numbers columns mixed types for analysis.
4. **Whether extra keys can be added to the format.** The form has no place for who did the scoring. The ideas doc asks
   for it ("expert", "workshop participant" or "workshop as a group"). Recommended: add one top-level `assessor` block
   (`name`, `email`, `role`). If no keys may be added, the name and role can only go in the file name.
5. **Scorer's notes ("inside knowledge").** The form has one `justification` text per category. Recommended: a notes
   box on each subcategory card, saved into its category's `justification` as lines like `P-1: ...`. A per-factor
   `note` key would be cleaner but needs decision 4's "yes".
6. **Which definition text to save.** The colleague's D, P and RRS definitions each have one more sentence than this
   project's (for example "P makes it visible."). Recommended: save the colleague's text, so every file has the same
   definitions.
7. **`scoringMethod` value.** The example says `"rapid_assessment"`. Recommended: `"evidence_review"` for scores
   chosen in this viewer, if the colleague agrees to a second value. Otherwise keep `"rapid_assessment"`.
8. **`dataset.identifier`.** Recommended: the DOI, `10.7289/V5D21VHZ` for GHCN-Daily (from the dataset metadata).
   Our short id (`ghcn-daily`) goes in the file name.
9. **Saving with NA left.** Recommended: allow it, with a warning that says how many are NA. The ideas doc wants NA kept
   because the graph shows it.
10. **Keeping the research scores in the file.** Useful for analysis (how often people change the research score), but
   it needs decision 4's "yes". Recommended: leave it out for now. The research scores can be rebuilt from the
   categorization JSON at any time.

## What one saved file holds

One file per save, per dataset, per person. Field by field, against the example:

| Field | Filled from | Notes |
|---|---|---|
| `assessmentTimestamp` | The time Save is pressed | UTC, ISO 8601, for example `2026-11-23T23:29:37.353Z` |
| `dataset.name` | `datasets_metadata/json/<id>_dataset-metadata.json` → `dashboard.name` | |
| `dataset.identifier` | Same file → `identification.doi` | Decision 8 |
| `primaryDataCurator.name` | Same file → `dashboard.curator` | GHCN-Daily: "NOAA NCEI GHCNd Operations Team" |
| `primaryDataCurator.email` | `""` | No email is in the metadata |
| `rStarCompositeScore` | R* worked out from the chosen scores | `null` when NA (decision 3) |
| `triageTier` | From `framework.triageThresholds` | "Mirror now" (70 or more), "Stabilize and mirror" (40–69), "Monitor" (under 40); `null` when R* is NA |
| `formula` | Fixed text, as in the example | |
| `components.<D, P, RRS, DIRS>.label` | Category short title | "Data risk", "People risk", ... |
| `.definition` | Decision 6 | |
| `.rawScore` | Category total | `null` when NA |
| `.weight` | `how_to_score_rstar.md` | 0.4, 0.3, 0.2, 0.1 (they match the example) |
| `.weightedContribution` | weight × total; RRS: weight × (100 − total) | Matches the example: RRS 0 gives 20. `null` when NA |
| `.scoringMethod` | Decision 7 | |
| `.justification` | Notes boxes (decision 5) | `""` until notes exist |
| `.factors.<key>` | One per subcategory | Key is the subcategory title in snake_case. Checked: all 19 titles give exactly the example's keys |
| `.condition` | Subcategory title | Matches the example for all 19 |
| `.present` | Full points → `true`, 0 → `false`, NA → `null` | For RRS, `true` means the resilient condition is met |
| `.points` | The chosen score | `null` when NA |
| `.maxPoints` | Point value | Decision 2 |
| `framework` | Fixed block, copied from the example | Name, version 2.0, authors, Zenodo DOI, thresholds |
| `assessor` (new) | Name, email and role fields on the landing page | Decision 4 |

**File name:** `<dataset id>_rstar_<assessor name>_<timestamp>.json`, for example
`ghcn-daily_rstar_jsmith_2026-11-23T232937Z.json`. Colons are dropped from the time because some systems don't allow
them in file names. The name is cut down to letters, digits and hyphens.

## The Save control (landing page)

In the R* score section, under the score tiles:

- **Your name** (text), **Email** (optional), **Role** (Expert / Workshop participant / Workshop group). They are
  remembered in this browser, so a scorer types them once.
- A **Save scores** button. It is disabled until a name is filled in.
- After a save: "Saved at 18:30 (2026-11-23) as `ghcn-daily_rstar_jsmith_...json`." This message is in a live region,
  so screen readers read it.
- If any subcategory is NA, the message also says how many ("4 subcategories are NA; R* is NA").
- **Unsaved changes:** the page compares the choices with the last save and shows "Changes since your last save" when
  they differ.
- **Load a saved file** (optional): opens one of the person's own saved files and puts its choices back on the radio
  buttons, so they can carry on or fix a score later. It checks that the file is for the same dataset.

## Where the files go

**A. Download to the scorer's computer (recommended to start).** Save builds the JSON in the page and downloads it.
Scorers send their files to you by email or a shared drive. It needs no server and works from GitHub Pages, a shared
folder, or a page opened from disk. The cost is collecting the files by hand.

**B. A small server that stores the files.** A short Python web app (Flask or FastAPI) serves the site and accepts
saves at `POST /api/scores`. It writes each one to `scores/<dataset id>/<file name>.json` and never overwrites a file.
You download the whole folder as a zip from one page. This suits a workshop where everyone scores at once. The costs:
somewhere to host it (a lab server or a small cloud machine), a way to stop strangers posting (a shared workshop code
is enough for a start), and backups.

**C. A hosted form service.** For example, a Google Apps Script web app that writes each save into a Google Drive
folder. It needs no server of your own, but the data sits in a third-party account and cross-site requests need
setting up.

The page builds the file in one function (`buildAssessment()`). Only the last step ("download" or "send") would
change between A, B and C, so starting with A doesn't block the others.

## History and the latest version

- Every save is a new file with its own timestamp. Nothing is overwritten, so every version is kept.
- "The latest" for a person and a dataset is the file with the newest `assessmentTimestamp`. The analysis script
  (below) picks it. The viewer doesn't need to.
- The ideas doc asks whether each subcategory choice needs its own timestamp. Not planned: the form has no place for
  it, and one timestamp per save plus keeping every file gives the same history.

## Analysis later (not part of this step)

`scripts/analyze/collect_rstar_scores.py` would read a folder of saved files and write one CSV row per file and
factor (dataset, assessor, role, timestamp, factor, present, points, maxPoints), plus one row per file for the
category totals and R*. From there, the expert, group and single-person versions the ideas doc mentions for workshops
can be compared.

## Building it (order of work, after the decisions)

1. Update `docs/scoring/how_to_score_rstar.md` if decision 2 changes point values, re-run `build_data.py`, and check
   the GHCN-Daily scores.
2. Add the colleague's definitions and the `framework` block to the data that `build_data.py` writes (decision 6), or
   keep them as constants in `app.js`.
3. Write `buildAssessment()` in `app.js`, using `currentScores()` for the numbers.
4. Add the name, email and role fields, the Save button and the status message to the landing page.
5. Add notes boxes to the cards if decision 5 is yes.
6. Add "Load a saved file" if wanted.
7. Write a JSON Schema for the format (`docs/json_output/rstar_assessment.schema.json`) from the example, so files can
   be checked.
8. e2e tests: Save downloads a file (Playwright's download event), the file matches the schema, its numbers match the
   panel, NA saves as `null`, and a loaded file sets the radios.
9. Update `app/README.md` and `HANDOFF.md`.
