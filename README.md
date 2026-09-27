[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10560963/data-center-technician-dcc-communities) | amazon | US, CA, Gilroy | 0.5282 | 2026-09-26 |
| [Applied Scientist, Tabular Foundational Model, AWS](https://www.amazon.jobs/jobs/10560684/applied-scientist-tabular-foundational-model-aws?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5258 | 2026-09-26 |
| [Data Center Technician, DCC Communities, DCO Tech](https://www.amazon.jobs/en/jobs/10560893/data-center-technician-dcc-communities-dco-tech) | amazon | US, GA, Lithia Springs | 0.5232 | 2026-09-26 |
| [Data Center Technician, DCC Communities, DCO Tech](https://www.amazon.jobs/en/jobs/10560896/data-center-technician-dcc-communities-dco-tech) | amazon | US, GA, Lithia Springs | 0.5232 | 2026-09-26 |
| [Data Center Technician, DCC Communities, DCO Tech](https://www.amazon.jobs/en/jobs/10560914/data-center-technician-dcc-communities-dco-tech) | amazon | US, GA, Lithia Springs | 0.5232 | 2026-09-26 |
| [Senior Solution Area Specialist - AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556866762) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5224 | 2026-09-26 |
| [Senior Cloud Solution Architect, Cloud & AI Business Solutions](https://apply.careers.microsoft.com/careers/job/1970393557002031) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5182 | 2026-09-26 |
| [Principal Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393557006854) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5115 | 2026-09-26 |
| [Mechanical Product Engineer, Mechanical Products and Services](https://www.amazon.jobs/en/jobs/10560929/mechanical-product-engineer-mechanical-products-and-services) | amazon | US, VA, Herndon | 0.5061 | 2026-09-26 |
| [Data Center Technician, DCC Communities, DCO Tech](https://www.amazon.jobs/en/jobs/10560909/data-center-technician-dcc-communities-dco-tech) | amazon | US, GA, Atlanta | 0.5029 | 2026-09-26 |
| [Technical Recruiter](https://jobs.ashbyhq.com/openai/0dc7f3f1-0f8c-4d71-8264-ae0f208efeb1) | openai | San Francisco | 0.4989 | 2026-09-26 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556958087) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4976 | 2026-09-26 |
| [Applied Scientist, RL post-training, AWS](https://www.amazon.jobs/jobs/10560685/applied-scientist-rl-posttraining-aws?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.4884 | 2026-09-26 |
| [Sr. Technical Account Manager, TAM ](https://www.amazon.jobs/en/jobs/10560891/sr-technical-account-manager-tam) | amazon | US, WA, Seattle | 0.4834 | 2026-09-26 |
| [Sr. Technical Account Manager, TAM ](https://www.amazon.jobs/en/jobs/10560897/sr-technical-account-manager-tam) | amazon | US, WA, Seattle | 0.4781 | 2026-09-26 |
| [Sr. Technical Account Manager, TAM ](https://www.amazon.jobs/en/jobs/10560895/sr-technical-account-manager-tam) | amazon | US, WA, Seattle | 0.4781 | 2026-09-26 |
| [AI Research Scientist 4 - Generative Models, Recommender Systems](https://explore.jobs.netflix.net/careers/job/790317917705) | netflix | Remote, United States | 0.4723 | 2026-09-26 |
| [Cloud Solution Architect Manager](https://apply.careers.microsoft.com/careers/job/1970393557007323) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4702 | 2026-09-26 |
| [Director of Sales Enablement](https://apply.careers.microsoft.com/careers/job/1970393557008025) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4662 | 2026-09-26 |
| [Software Engineering IC4](https://apply.careers.microsoft.com/careers/job/1970393557007484) | microsoft | United States | 0.4527 | 2026-09-26 |
| [Americas Sales Excellence Director, AI Business Solutions](https://apply.careers.microsoft.com/careers/job/1970393556962195) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4380 | 2026-09-26 |
| [Software I&T Engineer, Amazon Leo Optical Inter-Satellite Link ](https://www.amazon.jobs/en/jobs/10560946/software-i-t-engineer-amazon-leo-optical-inter-satellite-link) | amazon | US, CA, Northridge | 0.4360 | 2026-09-26 |
| [Network Deployment Manager I, Global Network Delivery](https://www.amazon.jobs/en/jobs/10560967/network-deployment-manager-i-global-network-delivery) | amazon | US, IN, New Carlisle | 0.4324 | 2026-09-26 |
| [Fiber Delivery Engineer](https://apply.careers.microsoft.com/careers/job/1970393556999388) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Arizona, Phoenix | 0.4245 | 2026-09-26 |
| [Business Manager](https://apply.careers.microsoft.com/careers/job/1970393557006415) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4231 | 2026-09-26 |

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
