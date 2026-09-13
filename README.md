[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556751888) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5731 | 2026-09-12 |
| [Sr. Program Manager, Delivery Intelligence](https://apply.careers.microsoft.com/careers/job/1970393556950877) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5702 | 2026-09-12 |
| [Sr Software Engineer/Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556929279) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.5684 | 2026-09-13 |
| [Developer Experience Engineer II and/or Senior Developer Experience Engineer](https://apply.careers.microsoft.com/careers/job/1970393556971398) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5672 | 2026-09-12 |
| [Applied Science Manager, AWS Startups](https://www.amazon.jobs/jobs/10537816/applied-science-manager-aws-startups?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5337 | 2026-09-12 |
| [Senior Product Designer, FDE](https://apply.careers.microsoft.com/careers/job/1970393556981031) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5313 | 2026-09-12 |
| [Principal Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556982563) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5197 | 2026-09-12 |
| [Sr. Software Development Engineer, Inference Team - AWS Neuron](https://www.amazon.jobs/en/jobs/10538171/sr-software-development-engineer-inference-team-aws-neuron) | amazon | US, WA, Seattle | 0.5124 | 2026-09-12 |
| [Business Program Manager - Capacity Demand Predictive Insights](https://apply.careers.microsoft.com/careers/job/1970393556978442) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.5123 | 2026-09-12 |
| [Software Engineer - FDE](https://apply.careers.microsoft.com/careers/job/1970393556939575) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5055 | 2026-09-13 |
| [Principal Technical Program Manager, Datacenter End-to-End Build Delivery](https://apply.careers.microsoft.com/careers/job/1970393556994747) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4962 | 2026-09-12 |
| [Cloud Solution Architect - CTJ - Top Secret](https://apply.careers.microsoft.com/careers/job/1970393556988179) | microsoft | United States, District of Columbia, Washington D.C.; United States, Virginia, Reston; United States, Maryland, Annapolis Junction; United States, Multiple Locations, Multiple Locations | 0.4921 | 2026-09-12 |
| [Business Architect](https://apply.careers.microsoft.com/careers/job/1970393556957827) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4823 | 2026-09-13 |
| [Enterprise Architect, Americas Markets & Industries Office of the CTO](https://apply.careers.microsoft.com/careers/job/1970393556981728) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4805 | 2026-09-13 |
| [Data Center Technician Night Shift](https://www.amazon.jobs/en/jobs/10538152/data-center-technician-night-shift) | amazon | US, AZ, Mesa | 0.4763 | 2026-09-12 |
| [Global GTM Business Architect - Microsoft Fabric](https://apply.careers.microsoft.com/careers/job/1970393556986874) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4668 | 2026-09-13 |
| [Sales Strategy Enablement Lead](https://apply.careers.microsoft.com/careers/job/1970393556957724) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4640 | 2026-09-13 |
| [Software Engineering II and Senior Software Engineer (CoreAI - Post Training)](https://apply.careers.microsoft.com/careers/job/1970393556994428) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4605 | 2026-09-13 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556992129) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4601 | 2026-09-13 |
| [Sr. Field Sales Operations Lead, US Specialist Org, NAMER Field Operations, NAMER Sales Operations](https://www.amazon.jobs/en/jobs/10538247/sr-field-sales-operations-lead-us-specialist-org-namer-field-operations-namer-sales-operations) | amazon | US, CA, San Francisco | 0.4589 | 2026-09-12 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556987131) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4564 | 2026-09-12 |
| [Principal Applied Scientist - AI for Life Sciences, AWS Applied AI Solutions - Life Sciences](https://www.amazon.jobs/jobs/10538102/principal-applied-scientist--ai-for-life-sciences-aws-applied-ai-solutions--life-sciences?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.4356 | 2026-09-12 |
| [Principal Product Manager, AI Infrastructure](https://apply.careers.microsoft.com/careers/job/1970393556995531) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4278 | 2026-09-12 |
| [Federal Resource Deployment Manager-CTJ-Top Secret](https://apply.careers.microsoft.com/careers/job/1970393556991292) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4256 | 2026-09-12 |
| [Cloud & AI Platform Solution Engineer Manager](https://apply.careers.microsoft.com/careers/job/1970393556994476) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4209 | 2026-09-12 |

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
