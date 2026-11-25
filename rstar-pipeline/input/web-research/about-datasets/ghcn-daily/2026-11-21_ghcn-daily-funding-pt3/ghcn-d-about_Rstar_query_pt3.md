# About GHCN-D Part 3 R* Query for Claude

About dataset = GHCN-D Part 3

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the GHCN-D (Global Historical Climatology Network daily) dataset.

## ChatGPT query

Research how the group or organization responsible for creating, maintaining, and processing the GHCN-D (Global Historical Climatology Network Daily) dataset is funded. Identify the responsible organization, its role in producing and maintaining the dataset, and its primary funding sources. Determine whether funding comes from federal government appropriations, grants, research institutions, or other sources. Assess the organization's overall funding structure and financial stability.

## Claude web research skill query

/my:broad-web-research

Using the earlier runs' records on GHCN-Daily (Global Historical Climatology Network–Daily), especially its combined funding-and-threats run, and on NOAA NCEI (in web_search_results/), how is the work of creating, maintaining and processing GHCN-Daily funded, and how stable is that funding structure? Spend the time on what those runs did not settle.

- **Who does the work:** the responsible organization and the unit or team inside it that runs GHCN-Daily, and any partners that do part of the work (such as the CISESS cooperative institute, contractors or other agencies), with each one's role.
- **Funding sources:** for each, the route that pays (appropriation line, program, cooperative agreement, contract, grant, or in-kind support from partner agencies or national weather services), with amounts, award or contract numbers and fiscal years where published. Where GHCN-Daily's own share is not published, say so rather than giving a parent line's total as its figure.
- **Structure and stability:** the NCEI line's enacted amounts and positions from FY2020 to FY2026, and how much of the work rests on one federal line, on annual or continuing-resolution funding, or on multi-year agreements. Rate the structure as stable (several sources or multi-year commitments, and steady enacted funding), narrow but steady (one main source, steady enacted funding), or unstable (enacted funding falling or lapsing).

Use NOAA's budget documents, award and contract databases, and Congress's and GAO's documents ahead of secondary accounts. Cuts, staff losses and news from 2025 on are a separate question. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** who does the GHCN-Daily work (NCEI's team and any partners, with roles); each route that pays for it, with amounts, award numbers and years where published; the NCEI line's enacted funding and positions from FY2020 to FY2026; and a rating of the funding structure (stable, narrow but steady, or unstable). Expect a standard-tier run.

**What I changed from your draft:**
- **Built on the combined run:** `2026-11-19_ghcn-daily-about-pt3_combined` already found that GHCN-Daily has no budget line of its own, sits inside the NESDIS NCEI line, and gets partner staff through CISESS. The question names that record so this run goes further: which NCEI unit runs it, what the CISESS agreements and NCEI's contracts pay for, and the multi-year trend, rather than finding the same line again.
- **"Responsible organization" made concrete:** NCEI is known, so the run looks for the unit or team inside it and the partners, which is where the combined run said nothing is published.
- **"Federal, grants, research institutions or other"** became one list of routes to check, including in-kind support such as national weather services sharing their data, which costs NCEI nothing but keeps the dataset going.
- **"Financial stability" defined:** a three-level rating of the structure, so the answer makes a judgment instead of describing it. Stability here means how the funding is built and its record through FY2026; cuts and threats from 2025 on are left to Part 4, so the two runs don't search the same budget fights.
- **No-share rule kept** from the combined query: NCEI's total is not offered as GHCN-Daily's figure.

**Order and reuse:** run this first of Parts 3–5, in this project. Part 4 uses its record. The combined run already answers the core of this question, so if you're short on usage, a time limit of 20 minutes and a token ceiling of 160,000 may be enough, or you could skip this part and run Part 4, which also covers the funding route. For another dataset, change the name, the parent line and the earlier runs it names.
