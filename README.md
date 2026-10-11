[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Applied Scientist Manager, Marketplace Intelligence](https://www.amazon.jobs/en/jobs/10575244/applied-scientist-manager-marketplace-intelligence) | amazon | US, VA, Arlington | 0.5722 | 2026-10-10 |
| [Data Scientist II - AMZ10564056](https://www.amazon.jobs/jobs/10574837/data-scientist-ii--amz?cmpid=bsp-amazon-science) | amazon_science | US, CA, Culver City | 0.5676 | 2026-10-10 |
| [Solutions Architecture Manager, Software and Technology Solutions Architecture](https://www.amazon.jobs/en/jobs/10575306/solutions-architecture-manager-software-and-technology-solutions-architecture) | amazon | US, CA, San Francisco | 0.5356 | 2026-10-10 |
| [Project Engineer, Data Center Construction](https://www.amazon.jobs/en/jobs/10575079/project-engineer-data-center-construction) | amazon | US, OR, Boardman | 0.5331 | 2026-10-10 |
| [Support Engineer, High Touch Support](https://www.amazon.jobs/en/jobs/10575160/support-engineer-high-touch-support) | amazon | US, WA, Bellevue | 0.5324 | 2026-10-10 |
| [Applied Scientist Manager, Marketplace Intelligence](https://www.amazon.jobs/jobs/10575244/applied-scientist-manager-marketplace-intelligence?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.5251 | 2026-10-10 |
| [Principal Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556957800) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5040 | 2026-10-10 |
| [Principal Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556749366) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Washington, Redmond | 0.4935 | 2026-10-10 |
| [Senior Software Engineer - Azure Compute Next Gen Platform](https://apply.careers.microsoft.com/careers/job/1970393557024859) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4917 | 2026-10-10 |
| [Business Analyst Intern – Summer 2027](https://www.amazon.jobs/en/jobs/10575250/business-analyst-intern-summer-2027) | amazon | US, WA, Bellevue | 0.4860 | 2026-10-10 |
| [Senior Program Manager, APM Video](https://www.amazon.jobs/en/jobs/10575227/senior-program-manager-apm-video) | amazon | US, TX, Austin | 0.4858 | 2026-10-10 |
| [Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393557027422) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4843 | 2026-10-10 |
| [Software Development Engineer , Cryptography and Identity Management](https://www.amazon.jobs/en/jobs/10575067/software-development-engineer-cryptography-and-identity-management) | amazon | US, WA, Seattle | 0.4830 | 2026-10-10 |
| [Sr. TIPM, Data Center Network Build, BaND](https://www.amazon.jobs/en/jobs/10575081/sr-tipm-data-center-network-build-band) | amazon | US, VA, Herndon | 0.4798 | 2026-10-10 |
| [Sr. TIPM, Data Center Network Build, BaND](https://www.amazon.jobs/en/jobs/10575095/sr-tipm-data-center-network-build-band) | amazon | US, VA, Herndon | 0.4798 | 2026-10-10 |
| [Dir Category](https://apply.careers.microsoft.com/careers/job/1970393557026797) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4776 | 2026-10-11 |
| [Principal Product Manager](https://apply.careers.microsoft.com/careers/job/1970393556956535) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4769 | 2026-10-10 |
| [Software Development Engineer](https://www.amazon.jobs/en/jobs/10575340/software-development-engineer) | amazon | US, WA, Seattle | 0.4764 | 2026-10-10 |
| [General Marketing Specialist Intern – Summer 2027](https://www.amazon.jobs/en/jobs/10575256/general-marketing-specialist-intern-summer-2027) | amazon | US, WA, Seattle | 0.4671 | 2026-10-10 |
| [Supply Chain Manager Intern - Summer 2027](https://www.amazon.jobs/en/jobs/10575291/supply-chain-manager-intern-summer-2027) | amazon | US, WA, Seattle | 0.4665 | 2026-10-10 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10575080/infra-delivery-install-technician) | amazon | US, VA, Manassas | 0.4658 | 2026-10-10 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10575290/infra-delivery-install-technician) | amazon | US, VA, Ashburn | 0.4614 | 2026-10-10 |
| [Azure Solution Engineering Manager](https://apply.careers.microsoft.com/careers/job/1970393557025773) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4613 | 2026-10-11 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10575285/infra-delivery-install-technician) | amazon | US, VA, Aldie | 0.4607 | 2026-10-10 |
| [Senior Tech Bus Dev Manager, APM Twitch](https://www.amazon.jobs/en/jobs/10575228/senior-tech-bus-dev-manager-apm-twitch) | amazon | US, TX, Austin | 0.4593 | 2026-10-10 |

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
