# Dataset metadata JSON

One file per dataset, made from the "## ChatGPT answer" section of the
matching file in `../markdown/` (converted 2026-11-21, schema 0.1). Every
file has the same top-level keys in the same order; a field with nothing
to say is `""` or `[]`.

## Where each part goes

| Key | Use |
| --- | --- |
| `dashboard` | Drop-in object with exactly the keys of an entry in `app/data/datasets.json` (card + dropdown panel). Values are the current dashboard values, updated with ChatGPT's where it adds something; changes are listed in `review_notes`. |
| everything else | Overview page (and other projects). |

## Keys

| Key | Contents |
| --- | --- |
| `schema_version` | `"0.1"` |
| `id` | Dataset id (same as the dashboard `id`) |
| `source` | Markdown file, section and date converted |
| `dashboard` | See above |
| `identification` | Full name, abbreviations, version, DOI + link, provider, dataset type, description, citation (when given) |
| `archives[]` | `name`, `role` (`primary`, `mirror`, `project`, `access-service`, `secondary`), `description` |
| `access_endpoints[]` | `name`, `url`, `role` (`primary`, `alternative`, `documentation` — the dashboard uses the first two), `type` (`landing-page`, `download`, `cloud`, `doi`, `metadata`, …), optional `purpose`, `details` |
| `access_note` | Free-text note on access (warnings, registration) |
| `people` | `curator` {name, organization, role}, `leads[]` {name, organization, role}, `contributors[]`, `note` |
| `instruments` | `summary`, `categories[]` {name, type, role}, optional `platforms[]`, `input_products[]`, `processing_chain[]`, `legacy_inputs`, `gauge_adjustment`, `note` |
| `temporal` | `start` / `end` (ISO date, `YYYY-MM`, or `"present"`), `frequency`, `update_frequency`, `latency`, notes and extras |
| `spatial` | `coverage`, `extent` {lat_min, lat_max, lon_min, lon_max} in degrees, `land_ocean`, `resolution`, `grid` (null for station data), notes |
| `data_format` | `format`, `units`, optional `variable` |
| `status` | `state` (`Ongoing` / `Legacy`), `label`, `evidence[]` |
| `versions[]` | `version`, `status` (`current`, `superseded`, `legacy`), `doi`, optional `resolution`, `start` |
| `related_products[]` | Related datasets, e.g. IMERG Final vs Late |
| `references[]` | `title`, `url`, `type`, optional `doi` |
| `review_notes[]` | Things to check: conflicts with the dashboard, doubtful ChatGPT claims, edits made in conversion. Not for display. |

ChatGPT's stray source labels (e.g. a lone "NCEI" line) were dropped, and
`utm_source=chatgpt.com` was removed from URLs. Every URL in these files
comes from the markdown, the earlier `datasets.json`, or a link the user gave.
