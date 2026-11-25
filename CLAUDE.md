## Project overview

The app/ folder will be used to create an app using web research information on precipitation datasets to create a weighted network graph and/or knowledge graph for relationships of datasets metadata.

## File locations

The folder rstar-pipeline/ holds everything needed to rebuild the data the website shows, as input → processing → output (reorganized 2026-11-25; its README.md explains the layout and the steps):

- rstar-pipeline/input/web-research/ contains web research on precipitation datasets (about-datasets/), their data repositories (archives/), and instruments used to measure precipitation (instruments/).
- rstar-pipeline/input/framework/ holds what R* is: the subcategory definitions (definitions/), the scoring rules (how_to_score_rstar.md), the filing rules (rstar-categorization-decisions.md) and the colleague's form format (assessment-form/).
- rstar-pipeline/input/dataset-metadata/ contains metadata about each dataset.
- rstar-pipeline/processing/instructions/ holds the categorizing steps: Claude's step-by-step (categorize-dataset-instructions.md), my prompts (categorizing-web-searches_README.md) and the category JSON format (create_rstar_node_files.md).
- rstar-pipeline/processing/research-queries/ holds the research query templates and their design notes (copied from the Rstar_query_results project, where the queries are run).
- rstar-pipeline/processing/scripts/ holds the scripts: categorize/ (one build_<id>.py per dataset with the hand-sorted evidence), site-data/build_data.py (rebuilds the site's app/data/rstar-data.js) and dashboard/ (fills the dashboard's pages in app/data/ and app/content/).
- rstar-pipeline/output/categories/ stores the web research reformatted into subcategories, one JSON file per dataset in a folder named by dataset id (for example ghcn-daily/); rstar-pipeline/output/gaps-notes/ has each dataset's gaps note (what the research never searched, per subcategory).

The folder datasets-gap-queries/ stores, for each dataset, the coverage note, the gap query files for new web searches, and the run sheet for rewriting and running them (a one-off process, kept outside rstar-pipeline/).

The folder app/ contains the website: the dataset dashboard is its landing page (index.html, moved in from the precip_workshop_dashboard project on 2026-11-24), and each dataset card links to its R* score pages (scores.html, the category pages and graph.html), which show the categorizations. The site reads only its own app/data/ and app/content/, which the pipeline's scripts write.

The folder docs/ will be for me to add documentation for the project (now only docs/ideas/, git-ignored).

The folder notes/ is for Claude to store project notes and plans.

## Creating categories from web research

For creating categories applying @/Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/rstar-pipeline/processing/instructions/create_rstar_node_files.md, you can use all files in /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/rstar-pipeline/input/web-research

Follow the steps and prompts in rstar-pipeline/processing/instructions/categorizing-web-searches_README.md for categorizing a dataset, adding it to the website, writing gap queries, and adding new research; Claude's detailed steps are in rstar-pipeline/processing/instructions/categorize-dataset-instructions.md.


## Handoff doc

Before you compact a session and at the end of a session, update a HANDOFF.md file stored in the top folder with notes on the project and the steps to do next for the project so that the project goals can be remembered as it progresses through new sessions.

This repo is private, so CLAUDE.md, HANDOFF.md, notes/ and .claude/launch.json are committed with the rest. docs/ideas/ stays git-ignored: it is my notes for you to read, and I'll remove it when I'm finished.

It has two GitHub copies, both private: the agency's `nyce-data/precipitation_rstar_scoring` (the agency owns the code; I'm a collaborator) and my own `lmerchant/precipitation_rstar_scoring`. The remote `origin` fetches from mine and pushes to both, so `git push origin main` updates both. Neither is a public website. I push only main; the sandbox can't reach github.com, so I run the pushes.

This project started fresh on 2026-11-25 from a copy of `/Users/claude/SIDE_WORK/NYCE_project/Rstar_precipitation-relationships`, which stays as it is, public, for my colleagues. Don't change anything there; its git history (and its `local-notes` branch) is kept in that folder.

Commits use my GitHub noreply address, set for this repo with `git config user.email`.

## At the end of a session

I will tell you when I will be starting a new session, and when that happens, update all docs as needed and make a commit on the develop branch.

## Skills to use

Use the frontend-ui-engineering skill found in ~/.my-claude-plugins to apply accessibility settings and the playwright-expert skill found in ~/.my-claude-plugins to use playwright to view the web pages.

## Viewing the website

After each big change, show me the command to start the server so I can view the app in my browser:

```bash
cd /Users/claude/SIDE_WORK/NYCE_project/precipitation_rstar_scoring/app && python3 -m http.server 3000 --bind 127.0.0.1
```

Then open http://127.0.0.1:3000/

