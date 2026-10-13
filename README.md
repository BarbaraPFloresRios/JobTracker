[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Systems Development Engineer, Analytics ADC](https://www.amazon.jobs/en/jobs/10575807/systems-development-engineer-analytics-adc) | amazon | US, CO, Denver | 0.5891 | 2026-10-12 |
| [Senior APN Programs Lead, Scalable GTM and Funding Programs ](https://www.amazon.jobs/en/jobs/10576437/senior-apn-programs-lead-scalable-gtm-and-funding-programs) | amazon | US, VA, Arlington | 0.5769 | 2026-10-13 |
| [Software Dev Engineer, Prime Video Personalization & Discovery ](https://www.amazon.jobs/en/jobs/10576161/software-dev-engineer-prime-video-personalization-discovery) | amazon | US, NY, New York | 0.5738 | 2026-10-12 |
| [Senior Healthcare Solutions Architect, AI Solutions](https://www.amazon.jobs/en/jobs/10576576/senior-healthcare-solutions-architect-ai-solutions) | amazon | US, CA, San Francisco | 0.5594 | 2026-10-13 |
| [Category Manager, GPO Tech Category](https://www.amazon.jobs/en/jobs/10576077/category-manager-gpo-tech-category) | amazon | US, TX, Austin | 0.5521 | 2026-10-12 |
| [Data Center Logistics Specialist, DCC Communities](https://www.amazon.jobs/en/jobs/10576577/data-center-logistics-specialist-dcc-communities) | amazon | US, IN, New Carlisle | 0.5497 | 2026-10-13 |
| [Network Deployment Technician, GND-NASA-Deploy](https://www.amazon.jobs/en/jobs/10576323/network-deployment-technician-gnd-nasa-deploy) | amazon | US, TX, Dallas | 0.5481 | 2026-10-12 |
| [Demand Generation Manager, Digital Acquisition](https://www.amazon.jobs/en/jobs/10576138/demand-generation-manager-digital-acquisition) | amazon | US, VA, Arlington | 0.5408 | 2026-10-12 |
| [Security Engineer, Leo Security](https://www.amazon.jobs/en/jobs/10575820/security-engineer-leo-security) | amazon | US, VA, Herndon | 0.5264 | 2026-10-12 |
| [HR Partner, Human Resources, NACF](https://www.amazon.jobs/en/jobs/10575433/hr-partner-human-resources-nacf) | amazon | US, NY, Liverpool | 0.5229 | 2026-10-12 |
| [Sr. Life Sciences Business Development Lead, AI Solutions](https://www.amazon.jobs/en/jobs/10576622/sr-life-sciences-business-development-lead-ai-solutions) | amazon | US, CA, San Francisco | 0.5221 | 2026-10-13 |
| [ASIC Engineer Early Career - 2027, Project Leo](https://www.amazon.jobs/en/jobs/10576621/asic-engineer-early-career-2027-project-leo) | amazon | US, WA, Redmond | 0.5081 | 2026-10-13 |
| [Financial Analyst](https://www.amazon.jobs/en/jobs/10576260/financial-analyst) | amazon | US, TX, Irving | 0.5059 | 2026-10-12 |
| [Industrial Engineer II, Layout](https://www.amazon.jobs/en/jobs/10576010/industrial-engineer-ii-layout) | amazon | US, PA, Pittsburgh | 0.5035 | 2026-10-12 |
| [ASIC Engineer Intern, Summer 2027](https://www.amazon.jobs/en/jobs/10576619/asic-engineer-intern-summer-2027) | amazon | US, CA, Sunnyvale | 0.5024 | 2026-10-13 |
| [Data Center Technician - Night Shift](https://www.amazon.jobs/en/jobs/10575746/data-center-technician-night-shift) | amazon | US, GA, Covington | 0.5020 | 2026-10-12 |
| [Data Center Technician - Night Shift](https://www.amazon.jobs/en/jobs/10575752/data-center-technician-night-shift) | amazon | US, GA, Covington | 0.5020 | 2026-10-12 |
| [Network Deployment Lead, DCC Communities ](https://www.amazon.jobs/en/jobs/10576314/network-deployment-lead-dcc-communities) | amazon | US, GA, Covington | 0.4972 | 2026-10-12 |
| [Network Deployment Lead, DCC Communities ](https://www.amazon.jobs/en/jobs/10576305/network-deployment-lead-dcc-communities) | amazon | US, GA, Covington | 0.4972 | 2026-10-12 |
| [Data Scientist, Product](https://www.metacareers.com/profile/job_details/4374182922893050) | meta | Bangalore, India | 0.4966 | 2026-10-12 |
| [Engineering Operation Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10575858/engineering-operation-technician-dcc-communities) | amazon | US, OH, New Albany | 0.4965 | 2026-10-12 |
| [Engineering Operation Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10575861/engineering-operation-technician-dcc-communities) | amazon | US, OH, New Albany | 0.4965 | 2026-10-12 |
| [Engineering Operation Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10575859/engineering-operation-technician-dcc-communities) | amazon | US, OH, New Albany | 0.4965 | 2026-10-12 |
| [Engineering Operation Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10575857/engineering-operation-technician-dcc-communities) | amazon | US, OH, New Albany | 0.4965 | 2026-10-12 |
| [Network Deployment Lead, DCC Communities ](https://www.amazon.jobs/en/jobs/10576324/network-deployment-lead-dcc-communities) | amazon | US, TX, Dallas | 0.4962 | 2026-10-12 |

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
