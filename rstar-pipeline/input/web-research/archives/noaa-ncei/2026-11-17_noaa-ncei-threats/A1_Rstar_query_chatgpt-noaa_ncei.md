# A1 R* Query

Archive = NOAA NCEI

## Query to refine

Stable institutional funding [Repository resilience]

No imminent political, budgetary, or administrative threat to operations

## ChatGPT query

/my:broad-web-research Rewrite this as a question for this skill; don't run it yet:

$REPO = "NOAA NCEI"

Conduct an evidence-based assessment of whether there is an imminent or emerging threat to the continued operation, funding, institutional support, or administrative independence of the climate science data repository/archive `$REPO`.

Investigate potential threats across the following categories:

1. **Political threats:** Government actions, executive orders, legislative proposals, political directives, policy changes, or other political developments that could affect the repository's operations, mission, or continued existence.
2. **Budgetary and funding threats:** Proposed or enacted budget reductions, funding freezes, grant cancellations, appropriations changes, contract terminations, staffing cuts, or other financial developments that could impair the repository's ability to operate.
3. **Administrative and institutional threats:** Agency reorganizations, leadership directives, changes in institutional oversight, proposed transfers or consolidations, staffing reductions, changes in data-management responsibilities, or plans to discontinue or restructure the repository.
4. **Operational threats:** Actions or circumstances that could result in reduced data access, interrupted services, discontinued data collection or preservation, loss of technical infrastructure, restricted public access, or termination of repository functions.


## Claude web research skill query

/my:broad-web-research

Is there an imminent or emerging threat to the continued operation, funding, institutional support or administrative independence of NOAA's National Centers for Environmental Information (NCEI)? Cover January 2025 to the present. Count actions aimed at NOAA or NESDIS as a whole only where a source ties them to NCEI. Check for four kinds of threat:
- **political:** executive orders, directives, bills;
- **budgetary:** budget requests and enacted appropriations, freezes, contract terminations, staffing cuts;
- **institutional:** reorganizations, transfers or consolidations, changes in oversight or data-management duties;
- **operational:** datasets or products retired, services interrupted, data collection or preservation stopped, infrastructure lost, public access restricted.

Check each kind without assuming a threat exists. Rate each one:
- **imminent:** enacted, ordered or already happening;
- **emerging:** proposed or reported but not in effect;
- **no current threat found.**

For each, give dates and figures (dollars, staff, datasets affected), and say whether it is proposed, enacted, blocked or reversed. Where no figure is published, say so. Use NOAA's, Commerce's, Congress's and GAO's own documents ahead of news reports, and use news for events. Explain where sources disagree about scale or status. Thorough mode, with a time limit of 50 minutes and a token ceiling of 400,000.


## Claude comments about the rewritten query

**What you'll get:** one rating for each of the four kinds of threat, each with dated evidence and its status, plus an overall answer with a confidence level. Expect a deep-tier run, because the topic involves proposed cuts.

**What I changed from your draft:**
- **Time frame:** I set "January 2025 to the present", since your draft had none. Change it if you want a different window.
- **NOAA-wide actions:** I added the rule about actions aimed at NOAA or NESDIS as a whole. Without it, the run could count every NOAA-wide cut as a threat to NCEI.
- **Rating scale:** I defined "imminent" and "emerging" so the four kinds get rated the same way.
- **Your lists:** I shortened them to short candidate lines. The skill plans its own searches.

To use the question for another archive, replace the name and parent agencies in the first two sentences, and the list of preferred sources.


