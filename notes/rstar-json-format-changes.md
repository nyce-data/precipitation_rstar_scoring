# R* JSON: what the viewer's saved files change from the colleague's form

Written 2026-11-23 for the user to pass on. The viewer saves one JSON file per save in the format of
`rstar-pipeline/input/framework/assessment-form/example_rstar_json.json`, with these differences. The full shape is in
`app/schema/rstar-assessment.schema.json`.

## Added

- **`assessor`** (after `primaryDataCurator`): who chose the scores.

  ```json
  "assessor": { "name": "Jane Smith", "email": "jane@example.org", "role": "expert" }
  ```

  `role` is `"expert"`, `"workshop_participant"`, `"workshop_group"`, or `""` if none was picked. `email` may be `""`.

## Different values

- **NA scores are `null`.** When a scorer leaves a subcategory as NA (not enough evidence to decide):
  - the factor's `present` and `points` are `null`;
  - its component's `rawScore` and `weightedContribution` are `null`;
  - `rStarCompositeScore` and `triageTier` are `null` if any component is `null`.
- **`present`** is `true` when the factor gets its full points and `false` when it gets 0. For RRS factors, `true`
  means the resilient condition is met.
- **`justification`** holds the scorer's notes, one line per subcategory, for example
  `"P-1: Team of four; the lead retires in 2027.\nP-3: ..."`. It is `""` when there are no notes.
- **`scoringMethod`** is `""`. The key is kept for a later method value.
- **`dataset.identifier`** is the dataset's DOI (for example `"10.7289/V5D21VHZ"`), or a data endpoint URL when
  there is no DOI.
- **`primaryDataCurator.email`** is `""`: the dataset metadata has no curator email.

## Unchanged

- Top-level key order, the `formula` text and the `framework` block (copied from the example file).
- Component keys and order (`D`, `P`, `RRS`, `DIRS`), labels, weights and definitions.
- Factor keys, conditions and `maxPoints`. The viewer now uses the form's point values (P-3 = 25, DIRS-2 = 25,
  DIRS-4 = 15).
- `weightedContribution` is weight × `rawScore`, and for RRS weight × (100 − `rawScore`). Values are rounded to two
  decimals.
- `triageTier` thresholds: "Mirror now" at 70 or more, "Stabilize and mirror" from 40 up to 70, "Monitor" under 40.

## File names

`<dataset id>_rstar_<scorer name>_<UTC time>.json`, for example `ghcn-daily_rstar_jane-smith_2026-11-23T232937Z.json`.
Every save is a new file, so earlier saves are kept. The latest for a scorer and dataset is the one with the newest
`assessmentTimestamp`.
