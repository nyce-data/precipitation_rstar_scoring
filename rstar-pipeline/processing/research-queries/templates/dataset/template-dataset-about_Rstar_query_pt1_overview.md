# About $DATASET_SHORT Part 1: Overview R* Query for Claude

About dataset = $DATASET_SHORT Part 1, overview: hosts, inputs and producers

Template written 2026-11-23 from `rstar-pipeline/processing/research-queries/dataset-query-5-part-plan.md` in precipitation_rstar_scoring. To use it:
copy it into the dataset's folder as `<dataset>-about_Rstar_query_pt1.md`, replace every `$PLACEHOLDER`, rewrite it
with `/my:rewrite-research-query`, then run the rewritten query with `/my:broad-web-research` in its own session.

**Placeholders:**
- `$DATASET_SHORT`: the short name, such as GHCN-D.
- `$DATASET`: the short and full names, such as "GHCN-Daily (Global Historical Climatology Network–Daily)".
- `$RELATED`: related products to mention only to say how they differ, such as GHCN-Monthly, or IMERG Early and Final.

**Subcategories this part feeds:** RRS-1 (copies and mirrors), D-2 (who serves it), DIRS-3 (input list), DIRS-4
(outside groups), P-4 (which groups do the work).

**Run order:** first. Parts 2, 3, 4 and 5 all use this run's record.

## Query to refine

Research the $DATASET dataset, current version only; mention $RELATED only to say how they differ. Where is it stored
and served: every repository, mirror, cloud copy and group website that holds a copy, with URLs, which one is the
archive of record, and whether each is a shared archive, the producer's own data site, or a copy of another host's
data? What kind of dataset is it (one instrument or platform, a compilation of station networks, or a blend
of satellites, gauges and other datasets)? Name each input (networks, satellites and sensors, datasets, ancillary or
reanalysis fields) with its dates and share where published, and say how the inputs are combined, which values are
measured directly and which come from algorithms, and how often it is updated. Which organizations produce, process,
host and pay for it, and what does each do, including cooperative institutes, contractors and other outside groups?
Leave quality control, people, funding amounts, and any cuts or threats to later parts. Tag findings with the
subcategory they bear on: RRS-1 "two or more geographically independent copies", D-2 "storage is a single point of
failure", DIRS-3 "depends on external data feeds" or DIRS-4 "needs outside processing infrastructure". With a time
limit of 30 minutes and a token ceiling of 240,000.

### Context for the rewrite

- **Keep it standard tier.** Don't add words about cuts, threats, layoffs or news. The research skill picks its
  costly deep tier when the question involves a dispute, and Part 4 covers those topics.
- **"Derived" is three kinds, not two.** A station compilation (GHCN-Daily) is neither a single instrument nor a
  satellite blend. Ask the run to say which of the three kinds the dataset is.
- **Merging, by kind of dataset:**
  - for a station compilation: which networks supply how many stations, and how duplicates and overlapping records
    are resolved;
  - for a satellite or gauge–satellite blend: which satellites and sensors over which dates, which gauge analysis
    it is scaled to, and the merging algorithm by name.
- **Hosts list.** List every copy, including cloud copies (such as NOAA's Open Data Dissemination copies on AWS and
  Google) and the producer's own website. Later parts and the shared repository runs (A1, A2) start from this list.
  The three kinds of host (shared archive, producer's own data site, copy) decide which repository runs are needed;
  see `rstar-pipeline/processing/research-queries/archive-query-plan.md` in precipitation_rstar_scoring.
- **Organizations, not people.** Name the groups and what each does. Named people, staff counts and ages are
  Part 3's job.

### What the answer should give

- A table of hosts and access points, with URLs and which is the archive of record.
- The kind of dataset, and a table of inputs with dates and shares.
- How the inputs are combined, and the update schedule.
- A table of organizations and their roles.
- A subcategory tag on each finding.

## Claude web research skill query

(not written yet)

## Claude comments about the rewritten query

(not written yet)
