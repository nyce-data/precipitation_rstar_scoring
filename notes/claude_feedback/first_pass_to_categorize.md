# Categorize GHCN-Daily

## The GHCN-Daily file
- **File:** [ghcn-daily_rstar-categories.json](data-rstar-categories/datasets/ghcn-daily/ghcn-daily_rstar-categories.json). It has the four top keys and 19 subcategory keys you specified, and each value is a `<div class="p-1">` and so on. The structure and HTML check out.
- **Inside each div:** an Evidence list and a Gaps list. Each item has `data-confidence` (high, moderate or low) and `data-source` (the run folder it came from), plus inline source links. Anything that is my own inference is labelled as one.
- **Empty:** only RRS-2. Thin: DIRS-1, RRS-3 and P-2.
- **Left out:** how GHCN-Daily relates to GHCN-Monthly and GHCNh (except where it matters for D-5), conflicting station-count definitions, and the details of each QC test.
- **Not committed yet.** The script that built the file is in my scratch folder, not the project, because it only holds hand-sorted text.

## What was hard to categorize
1. **There's no Data subcategory for data quality.** Your Goal section says Data risk covers how the data are measured, processed and quality checked, but D-1 to D-5 cover funding, storage, access, format and politics. The large QC and processing sections of part 2 had nowhere natural to go, so I spread them across P-3, P-4 and DIRS-1.
2. **The producer and the repository are the same here.** NCEI both makes and hosts GHCN-Daily, so D-1, D-3 and RRS-4 draw on the same budget evidence. I repeated it where it was relevant.
3. **Several subcategories run together:**
   - P-1 and P-3 both rely on documentation; P-2 and P-4 both rely on who the key people are.
   - DIRS-2 (sensors) and DIRS-3 (data feeds): GSOD's end is a feed loss, but it hits national networks.
   - DIRS-1's "How to find" asks who does processing and QC, which is really DIRS-4. Nothing in it is about calibration.
4. **The research never asked several questions.** No query covered succession plans (P-1), ages or ORCID (P-2), calibration (DIRS-1), checksums or CoreTrustSeal (RRS-2), a disaster recovery plan (RRS-3), or holdings before and after a disruption (RRS-5). The "How to find" text exists, but no query followed it.
5. **"Unknown" scores differently by category.** Your graph notes say a subcategory defaults to 0 when evidence is missing. For P, D and DIRS that counts as no risk. For RRS it counts as no resilience, so missing evidence makes a repository look risky (it's scored as 100 − score). That's also why RRS is worded the other way round: "≥2 sites hold copies" is good, while "single point of failure" is bad.
6. **The research files have a few mix-ups.**
   - Two runs are both called "pt3": `about-pt3_combined` from 11-19 and `funding-pt3` from 11-21.
   - Cross-links in the answers point to `answer.md` files that don't exist.
   - Part 4 relies on the archive and instrument runs, which are outside `about-datasets/`.

## What I need from you
1. **Can I use the other research folders?** Should RRS and DIRS also draw on `archives/noaa-ncei/` and `instruments/noaa-rain-gauges/`? They probably hold the evidence for RRS-2, RRS-3 and DIRS-1.
2. **How should multiple repositories be handled?** GHCN-Daily lives at NCEI, AWS and Google. Should `repo_resilience` be split by repository, which your graph notes hint at, or stay pooled as now?
3. **Where does QC evidence go?** Do you want a data-quality subcategory, or should it stay spread out as I did?
4. **Should evidence be repeated or cross-referenced?** Shared budget evidence is currently repeated in each subcategory; a "see D-1" reference is the alternative.
5. **Is the format right?** That means the file name, the Evidence and Gaps lists, the confidence and source attributes, and whether my labelled inferences should stay in.
6. **Do you want the time window enforced?** D-1 and RRS-4 say 2025 to present. I also kept the FY2020–2024 budget history as context for RRS-5.

