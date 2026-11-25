# Why R* categories are hard to apply: follow-up

As of 2026-11-23. This follows up on [why-rstar-categories-are-hard-to-apply.md](why-rstar-categories-are-hard-to-apply.md).
That file keeps the first round of questions and your `<reply>` answers as a record. This file covers:

- what was decided;
- the explanations you asked for (suggestions 8 and 12, and "where" in the producer-and-repository question);
- follow-up questions where an answer left something open;
- open questions 2 to 6 from [first_pass_to_categorize.md](first_pass_to_categorize.md).

Answer the same way as before: write `<reply>` under a question and your answer below it. Nothing in the project has
been changed for these decisions yet. The changes are listed at the end.

## What was decided

| Topic | Decision |
| --- | --- |
| Scope sentences | Add one to every group, like the one DIRS has. Drafts are in follow-up question 1 |
| Storage and access | D-2 and D-3 cover the dataset and its repository, because the dataset is served by the repository. D-2 includes the repository going offline |
| Repeating evidence | Repeat a fact in every subcategory it bears on. No cross-references. R* is a starting score, not an exact split |
| How direct a link must be | A fact counts only if a source names the dataset, or something on its documented source list, input list or team. Anything one step removed (agency-wide losses, NIST capacity) stays as context |
| Name of the "neutral" stance | Rename it to "context" |
| RRS wording | Keep it. "For" in RRS means resilient, and (100 − RRS) turns a higher RRS into lower risk |
| Evidence status | Add status tags (found; searched and none found; not public; not searched) as well as the stance tags |
| Scoring a subcategory | Context items are ignored. High or moderate "for" items and no "against" items: full points. "Against" items and no "for" items: 0. Both, only context, or no evidence: NA |
| Showing scores | Each subcategory card shows its score, very visible and not gray |
| Missing evidence | Scores NA, and R* is then NA. Users can fill in what they know from other sources, such as talking to people |
| Later web form | Users fill in the final scores. The research fills in what it can, and NA items are marked as needing a decision |
| NA in the graph | Shown in a color such as black, with the value NA |
| Compilations | A risk to any one source is a risk to the dataset, however small the source |
| Proposed vs enacted cuts | Both count as "for" |
| RRS and several repositories | Pooled: one verdict from the evidence for all of them. "For" from one repository and "against" from another gives NA. Each RRS card says whether the dataset has one repository or several |
| Producer and repository the same | Count its funding and staff once, and say that they are the same organization. You asked where; see below |
| Data quality | Not part of R*. The formula is fixed, and no subcategories can be added. R* assumes good quality; an interruption or a drop in quality is evidence of risk |

## What the new scoring rule does to GHCN-Daily

I counted GHCN-Daily's 210 items by stance and confidence and applied the rule. The counts come from the current
file, before the "directly tied" test moves some items to context.

| Result | Subcategories |
| --- | --- |
| NA ("for" and "against" items both present) | P-1, P-3, P-4, D-1 to D-5, DIRS-1 to DIRS-5, RRS-1, RRS-4, RRS-5 |
| 0 ("against" items only) | RRS-2, RRS-3 |
| Depends on how low-confidence items count | P-2: 1 high or moderate "for", 1 low "for", 1 low "against" |

So 17 of the 19 subcategories, and R*, would be NA. Well-researched datasets will nearly always have items on both
sides, so most subcategories will need a person's decision. Follow-up question 5 asks whether that is what you want.

## Explanations you asked for

### Suggestion 8: thresholds for compilations

GHCN-Daily is built from about 30 station networks of very different sizes. CoCoRaHS supplies about 40% of station
entries. USCRN is small but is a reference network used to check the others. Argentina's weather service, which
dismissed 140 staff in April 2026, supplies a small share. The suggestion was a rule for when one source's trouble
counts as the dataset's trouble. For example: "a source counts if it supplies at least 5% of stations or values, or is
a reference network." Under that rule, the Argentina cuts would be context and a threat to CoCoRaHS would be "for".

Your answer to the compilation question settles this: any source counts, whatever its size, because the dataset as
defined is the sum of all its sources. So no threshold is needed. Follow-up question 4 asks one remaining point: what
counts as a source.

### Suggestion 12: "counts / doesn't count" examples

The definition files in `rstar_definitions/` say what each subcategory means and how to search for it. They do not
show where the line falls. The suggestion is to add a short list under each "How to find", with cases on both sides of
the line, taken from a station compilation (GHCN-Daily) and a satellite product (IMERG). For DIRS-2 it might read:

> **Counts:** USCRN's maintaining lab is proposed for closure (a GHCN-Daily source network). AMSR2 has run past its 5-year
> design life and JAXA is ending its data (an IMERG input).
>
> **Doesn't count (context):** NWS-wide technician losses with no network named. NOAA's budget as a whole.
>
> **Goes elsewhere:** the 1,371 foreign stations that still run but stopped reporting are a lost route, so DIRS-3. The
> NCEI archive moving to AWS is the repository, so D-2.

The examples would record the decisions above (the "directly tied" test, proposed cuts count, any source counts), so
the next dataset is sorted the same way. The viewer shows the definition files on the category pages, so the examples
would show there too unless they go in a separate section that the viewer skips. Follow-up question 9 asks which you
want.

### "Where" in the producer-and-repository question

NCEI produces, stewards and archives GHCN-Daily, so one NCEI fact often fits several subcategories, and inside one
subcategory it can come up twice: once for NCEI as producer and once for NCEI as repository. Take NCEI's FY2027 budget
request, 25% below its base:

- **D-1** asks about the program that produces the dataset and the program that hosts it. NCEI is both.
- **D-3** asks whether access is funded.
- **RRS-4** asks whether the repository's funding is stable.
- **P-1 and P-2**, if the cut is tied to staff.

"Where" meant: if the fact counts once, which of these gets it? Your other answers say to repeat facts across
subcategories, so I read "count once" as follows. Inside each subcategory the fact is one item, not one for the
producer and one for the repository. The item says NCEI is both. It still appears in D-1, D-3 and RRS-4. Follow-up
question 2 asks you to confirm this.

## Follow-up questions

1. **Scope sentences.** Here are drafts for the three groups that don't have one yet, rewritten to fit your answers
   (D now includes the repository). Do these read right?
   - **P:** "P covers the people who produce this dataset: its own team, including contractors, at the producer. Staff
     losses at the wider agency, or at a source network, are context here unless a source names this team." (Staff
     losses at a source network can still count in DIRS-2.)
   - **D:** "D covers the dataset as a product and the places that serve it: the programs that produce and host it,
     where it is stored and how users reach it (including the repository going offline), its formats, and political
     pressure on it."
   - **RRS:** "RRS covers each repository that holds a copy of the dataset, judged as an institution: its redundancy,
     integrity checks, disaster recovery, funding and track record. 'For' means the repository is resilient."

<reply>
yes

2. **Counting the producer-and-repository organization once.** Does "count once" mean one item per subcategory that
   says NCEI is both, with the fact still repeated across subcategories (as above)? And where should "the producer and
   repository are the same organization" be said: in each such item, once on the dataset's details on the landing
   page, or both?

<reply>
I think "count once" doesn't help clarify after all. Repeat the fact across subcategories. When I see more datasets categoriezed, I'll follow up if a change needs to be made.

Say "the producer and repository are the same organization" on the landing page. Make this a separate sentence so it stands out and a user will see it.


3. **What "directly tied" covers.**
   - a. **The producer as an organization.** Is the producer's own organization part of the dataset's "team"? NCEI's
     58 departures in 2025 name NCEI, but no source says any were on the GHCN-Daily team. Count or context?
   - b. **The agency that runs a source.** NWS runs COOP and ASOS, both GHCN-Daily sources. Do NWS-wide technician
     losses count for DIRS-2 because they name the agency that runs a source, or only when a source names COOP or
     ASOS?
   - c. **Repository facts.** For D-2, D-3 and RRS, I assume a fact about the repository counts directly, because the
     repository holds the dataset. For example, NCEI's offsite tape copy names NCEI's archive, not GHCN-Daily. Is that
     right?

<reply>

For a), use as context since it no source said they were specifically for the GHCN-Daily team

for b) Since it can't be separated like you explained with both being GHCN-Daily sources, count it as "for" evidence.

for c) yes, that's correct.


4. **What counts as a source of a compilation.** Is the unit a network (one of GHCN-Daily's source flags, such as
   CoCoRaHS or a national weather service), or does one station closing also count? GHCN-Daily has over 100,000
   stations, and some close every year, so counting single stations would make DIRS-2 "for" for every compilation.

<reply>
This is a good point. For now, if a source stops, count that as "for" evidence. And list this as a question in the next follow up document so I can clarify it with colleagues.

5. **The scoring rule.**
   - a. **Low-confidence items.** Are they ignored, like context? And what about P-2, where there is one high or
     moderate "for", one low "for" and one low "against"? If low items are ignored, P-2 scores 25; if they count, P-2
     is NA. Inferences are always low, so this also decides whether inferences can change a score.
   - b. **Low-confidence "against" items.** Does one of those block full points, or only high and moderate ones?
   - c. **Mostly NA.** Most subcategories will be NA (17 of 19 for GHCN-Daily). Is that what you want, so that a person
     decides each one on the web form? Or should the card also show the balance (for example "9 for, 4 against") to
     help them decide, without changing the NA?
   - d. **Partial R\*.** When R* is NA, should the app also show the part it can work out, or the range R* could fall
     in (from all NA items at 0 to all at full points)? Or only NA?

<reply>
for a) If it's low confidence, then don't include it when determining a score. But keep it tagged as low confidence and don't make it context.

for b) keep "low-confidence" items out of the score determination.

for c) Keep them as NA and I will show the users so they can decide what to do. NA stands for not enough information to make a decision and needs user input. At the top of each landing page, make a table of what the tags mean and how scores were determined. So users can let me know later if they want a different scoring decision matrix.

for d) good idea. Have the app show the parts that have a score and the parts that have NA. Display this on the landing page for each dataset "R* categorizations". Display the total R* score (and NA if that's what it is). And also show the 4 category scores (and NA if that's what it is). Then have a drop down panel with an arrow saying score details, and show each subcategory score (either a number of NA).

6. **Status tags.** Status describes absence ("searched and none found", "not public", "not searched"), and evidence
   items are all "found" by definition. My plan:
   - every evidence item is "found";
   - each Gaps item gets one of the other three;
   - each subcategory card shows a summary (for example "found" or "not searched").

   Is that what you meant, or do you want a status on each evidence item? One case is unclear: NCEI's
   disaster-recovery plan exists but "cannot be shared outside the US Government". Is that a found item (a plan
   exists, stance context) plus a "not public" gap (whether it was tested), or only a "not public" gap?

<reply>
go with your plan.

7. **Conflicting sources and rejected proposals.**
   - a. **Conflicts.** Two sources disagree: OIG-24-034-A's recommendations are open (September 2025) or "Closed"
     (Oversight.gov). Under the new rule this gives one "for" and one "against", so the subcategory is NA. Is NA the
     right result, rather than picking a source (such as the latest primary one)?
   - b. **Rejected proposals.** ARL's closure was proposed for FY2026, Congress rejected it, and it was proposed again
     for FY2027. Does a proposal that was later rejected still count as "for"? Or only while it is pending?

<reply>

for a) if sources disagree, keep the subcategory NA and let the user decide because they may have verbal and insider information that can't be found through a web search to determine which source is the most recent and correct.

for b) keep it a "for" when it's pending again. Keep it as context if there was a proposal but it was rejected.

8. **Which places count as repositories.** For the "one or several repositories" label on each RRS card, which of
   these count for GHCN-Daily?
   - the archive of record (NCEI);
   - cloud copies under contract (AWS `noaa-ghcn-pds`, Google BigQuery);
   - a volunteer snapshot (Data Rescue Project);
   - a producer's own website (for IMERG, PPS's site next to GES DISC);
   - third-party reformatted copies (dynamical.org's Zarr, Google Earth Engine).

   Should each RRS evidence item also say which repository it is about, so you can see which repository the "for" and
   "against" items come from?

<reply>
A volunteer snapshot shouldn't count because they may only have a data file and not the metadata that goes with the data file. NCEI is the parent repository. Copies and mirrors are child repositories. A producers own site is a repository. Third-party reformatted copies don't count because it isn't being served in an original format and there is no guarantee the third-party has retained the dataset's metadata. A lot of times, the dataset file is displayed on a source web page with metadata as text and images plus a download link to the dataset. The dataset file itself may or may not contain the same information on the web page. So that's why third party and reformatted versions don't count.

yes, each RRS evidence item should say what repository it is about.


9. **Data quality evidence that is already filed.** QC-process items, such as "NCEI runs automated QC tests" or "no
   homogenization", are now in DIRS-1 and D-4. Should they:
   - a. stay where they are, as context;
   - b. move to where they show a risk (QC that can't be redone without one person goes to P-3 or P-4; QC run on
     outside systems goes to DIRS-4); or
   - c. be dropped?

   For signs of a drop in quality, I would file them where the cause is: a lost network in DIRS-2, lost calibration in
   DIRS-1, an outage in D-2 or D-3. Does that fit what you meant?

<reply>
do option b where they show a risk. And if not a risk but it adds context, make it context.

10. **"Counts / doesn't count" examples (suggestion 12).** Do you want them? If so, should they go in the definition
    files (shown on the category pages), or in a separate guide for whoever categorizes, such as a section of
    `docs/categorizing-web-searches_README.md`?

<reply>
put them in a separate guide like you suggested.

11. **Renaming "neutral" to "context".** Should the value in the data change too (`data-stance="context"`, and the
    stance `"C"` instead of `"N"` in the build scripts), or only the label on the website? Changing both keeps them the
    same; it means editing the GHCN-Daily build script, the viewer and the e2e tests.

<reply>
change both to keep them the same.

## Open questions from the first pass

These are questions 2 to 6 from [first_pass_to_categorize.md](first_pass_to_categorize.md).

| # | Question | Status |
| --- | --- | --- |
| 2 | Split `repo_resilience` by repository, or keep it pooled? | Answered: pooled, with a one-or-several label (follow-up question 8 asks what counts) |
| 3 | A data-quality subcategory? | Answered: no. Follow-up question 9 asks what to do with the QC items already filed |
| 4 | Repeat shared evidence, or cross-reference it? | Answered: repeat |
| 5 | Is the JSON and HTML format right? | Not answered yet (below) |
| 6 | Enforce the 2025-to-present window in D-1 and RRS-4 strictly? | Not answered yet (below) |

12. **The format (first-pass question 5).** Each subcategory is now an HTML `<div>` in one JSON file per dataset,
    holding an Evidence list and a Gaps list. Each evidence item has these attributes:
    - `data-confidence`: high, moderate or low;
    - `data-source`: the research run it came from;
    - `data-stance`: "for", "against" or "context".

    Inferences are kept and labelled. The decisions above would add:
    - a status on Gaps items;
    - a score and a status for each subcategory;
    - possibly a repository on RRS items.

    Is that format still right? Should the score live in the JSON, or be worked out by `app/scripts/build_data.py` from
    the stances?


<reply>
the score can live in the JSON

13. **The time window (first-pass question 6).** D-1 and RRS-4 ask about 2025 to the present. Should older events,
    such as Hurricane Helene (September 2024) or the FY2020 to 2024 budget history, be:
    - a. left out of those two subcategories;
    - b. kept as context there; or
    - c. counted as "for" or "against"?

    They would still count in RRS-5 (track record), which has no window.

<reply>
keep older events as context and still count in RRS-5


## Changes to make once the answers are in

Not started. Each change waits on the follow-up question named in brackets.

1. **Scope sentences:** add them to the P, D and RRS definition files (question 1).
2. **Rename "neutral" to "context":** in the viewer, and in the data if you say so (question 11).
3. **Status tags:** add them to the build script, the JSON and the viewer (question 6).
4. **Scoring rule:**
   - write the NA rule into `docs/scoring/how_to_score_rstar.md` (question 5);
   - have `app/scripts/build_data.py` work out each subcategory's score;
   - show the score on each card, clear and not gray, with NA when it is NA.
5. **RRS cards:** add the one-or-several-repositories label (question 8).
6. **Re-sort GHCN-Daily** under the "directly tied" test. Items one step removed become context, for example NCEI's 58
   departures in P-1 and P-2, depending on question 3.
7. **Re-run the e2e tests** in Firefox and WebKit after the viewer changes.
8. **Later:** the web form for final scores, and NA shown in black in the graph.
