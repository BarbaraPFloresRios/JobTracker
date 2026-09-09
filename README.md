[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Principal Applied Scientist, CX Science](https://www.amazon.jobs/en/jobs/10531329/principal-applied-scientist-cx-science) | amazon | US, CA, Santa Clara | 0.7125 | 2026-09-08 |
| [Principal Technologist, 6G and AI, Telco Tech, AWS Industries](https://www.amazon.jobs/en/jobs/10532820/principal-technologist-6g-and-ai-telco-tech-aws-industries) | amazon | US, TX, Dallas | 0.6425 | 2026-09-08 |
| [Applied Scientist II, Console Science](https://www.amazon.jobs/en/jobs/10532623/applied-scientist-ii-console-science) | amazon | US, CA, Santa Clara | 0.6399 | 2026-09-08 |
| [Principal Technical Account Manager, AWS Enterprise Support, NAMER-Sp](https://www.amazon.jobs/en/jobs/10535213/principal-technical-account-manager-aws-enterprise-support-namer-sp) | amazon | US, NY, New York | 0.6372 | 2026-09-09 |
| [Data Center Operations Manager - Swing Shift](https://www.amazon.jobs/en/jobs/10531606/data-center-operations-manager-swing-shift) | amazon | US, IN, New Carlisle | 0.6102 | 2026-09-08 |
| [Data Center Operations Manager - Swing Shift](https://www.amazon.jobs/en/jobs/10531622/data-center-operations-manager-swing-shift) | amazon | US, IN, New Carlisle | 0.6102 | 2026-09-08 |
| [Applied Scientist (GenAI/LLM), Sandstone](https://www.amazon.jobs/en/jobs/10532200/applied-scientist-genai-llm-sandstone) | amazon | US, CA, San Diego | 0.6059 | 2026-09-08 |
| [Data Center Materials Spec I (WH),  Logistics and Imaging Team (LIT)](https://www.amazon.jobs/en/jobs/10532804/data-center-materials-spec-i-wh-logistics-and-imaging-team-lit) | amazon | US, WA, Renton | 0.6029 | 2026-09-08 |
| [Sr. Product Manager Technical, Business Data Technologies](https://www.amazon.jobs/en/jobs/10532232/sr-product-manager-technical-business-data-technologies) | amazon | US, MI, Detroit | 0.6016 | 2026-09-08 |
| [Data Center Cluster Operations Leader, AMER North East DC Ops](https://www.amazon.jobs/en/jobs/10532092/data-center-cluster-operations-leader-amer-north-east-dc-ops) | amazon | US, PA, Berwick | 0.6015 | 2026-09-08 |
| [Overnight Data Center Operations Manager ](https://www.amazon.jobs/en/jobs/10531637/overnight-data-center-operations-manager) | amazon | US, IN, New Carlisle | 0.5969 | 2026-09-08 |
| [Overnight Data Center Operations Manager ](https://www.amazon.jobs/en/jobs/10531648/overnight-data-center-operations-manager) | amazon | US, IN, New Carlisle | 0.5969 | 2026-09-08 |
| [Data Center Operations Manager](https://www.amazon.jobs/en/jobs/10531289/data-center-operations-manager) | amazon | US, IN, New Carlisle | 0.5941 | 2026-09-08 |
| [Data Center Operations Manager](https://www.amazon.jobs/en/jobs/10531293/data-center-operations-manager) | amazon | US, IN, New Carlisle | 0.5935 | 2026-09-08 |
| [Sr. GenAI/ML Specialist Solutions Architect, AGS Specialist Solutions Architects](https://www.amazon.jobs/en/jobs/10532699/sr-genai-ml-specialist-solutions-architect-ags-specialist-solutions-architects) | amazon | US, CA, San Francisco | 0.5932 | 2026-09-08 |
| [Sr. Global Supply Chain Manager, Amazon Custom Modules](https://www.amazon.jobs/en/jobs/10534690/sr-global-supply-chain-manager-amazon-custom-modules) | amazon | US, WA, Seattle | 0.5930 | 2026-09-09 |
| [Data Center Operations Manager](https://www.amazon.jobs/en/jobs/10531297/data-center-operations-manager) | amazon | US, IN, New Carlisle | 0.5926 | 2026-09-08 |
| [Data Center Operations Manager](https://www.amazon.jobs/en/jobs/10531295/data-center-operations-manager) | amazon | US, IN, New Carlisle | 0.5926 | 2026-09-08 |
| [Senior Data Center Category Manager, Data Center Sourcing & Procurement](https://www.amazon.jobs/en/jobs/10531653/senior-data-center-category-manager-data-center-sourcing-procurement) | amazon | US, VA, Arlington | 0.5869 | 2026-09-08 |
| [Sr. Database Specialist Solutions Architect, AGS Database Specialist Solutions Architects](https://www.amazon.jobs/en/jobs/10532206/sr-database-specialist-solutions-architect-ags-database-specialist-solutions-architects) | amazon | US, TX, Dallas | 0.5813 | 2026-09-08 |
| [Program Manager, Amazon Flex BOSS](https://www.amazon.jobs/en/jobs/10532300/program-manager-amazon-flex-boss) | amazon | US, WA, Bellevue | 0.5783 | 2026-09-08 |
| [Developer Experience Engineer, AWS Developer Experience](https://www.amazon.jobs/en/jobs/10532815/developer-experience-engineer-aws-developer-experience) | amazon | US, WA, Seattle | 0.5772 | 2026-09-08 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10532577/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5740 | 2026-09-08 |
| [GenAI Experiences Demo Architect , AWS Professional Services](https://www.amazon.jobs/en/jobs/10532069/genai-experiences-demo-architect-aws-professional-services) | amazon | US, VA, Arlington | 0.5698 | 2026-09-08 |
| [Bus Analyst II – AMZ010578](https://www.amazon.jobs/en/jobs/10534246/bus-analyst-ii-amz010578) | amazon | US, NY, New York | 0.5686 | 2026-09-09 |

## Companies tracked

JobTracker currently pulls openings directly from the career pages / official APIs of:

* MercadoLibre
* Apple
* Amazon
* Amazon Science
* NVIDIA
* Microsoft
* Netflix
* Meta
* OpenAI
* Anthropic
* Duolingo
* Spotify
* Reddit
* Discord
* Canva
* Uber
* Airbnb

## How it works

1. A scraper per company collects current openings straight from the source.
2. Each company's postings are stored as a CSV under `data/raw/`, keeping a history with `first_seen_date` and `last_seen_date` for every job.
3. Recently discovered roles (first seen today or yesterday) are exported to `data/recent_jobs.csv`.
4. Each recent job is scored by semantic similarity against a configurable candidate profile, and the top matches are surfaced in the table above.
5. A GitHub Action runs the whole pipeline every 3 hours and commits the refreshed data automatically.

If one company's site or API changes and its scraper fails, the pipeline logs the error, keeps that company's previous data, and continues with the rest — so a single broken source never stops the run.

## Run it locally

Requires Python 3.11+.

```bash
# 1. Clone the repo
git clone https://github.com/BarbaraPFloresRios/JobTracker.git
cd JobTracker

# 2. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install the browser used by some scrapers
playwright install --with-deps chromium

# 5. Run the full pipeline
python main.py
```

This regenerates `data/raw/*.csv`, `data/recent_jobs.csv`, and this `README.md`.

## Personalize the ranking

Semantic matching is driven by a plain-text profile at [`data/profile/job_matching_profile.txt`](data/profile/job_matching_profile.txt). Edit that file to describe the roles, skills, and seniority you're targeting, then run `python main.py` again — the similarity scores and the "Latest Jobs" ranking will reflect your profile.

## Current Features

* Scrape job postings directly from company career pages
* Support multiple companies
* Detect newly discovered openings
* Track historical job data over time
* Run automatically using GitHub Actions
* Fault-tolerant pipeline: a failing scraper never stops the others
* Store structured datasets as CSV files
* Export recent jobs from today and yesterday
* Semantic job matching using sentence embeddings
* Configurable candidate profile for personalized ranking
* Cosine similarity scoring between jobs and candidate profile

## Status

Active personal project focused on job discovery, semantic search, and recommendation workflows.
