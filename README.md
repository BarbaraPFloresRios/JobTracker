[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Principal Data Engineer](https://apply.careers.microsoft.com/careers/job/1970393556958759) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5963 | 2026-09-19 |
| [Director of Business Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556958758) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5705 | 2026-09-19 |
| [Sr Solution Engineer, Cloud & AI Infrastructure - CTJ - Top Secret](https://apply.careers.microsoft.com/careers/job/1970393556999949) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5645 | 2026-09-20 |
| [Business Intelligence Engineer II, Amazon Leo](https://www.amazon.jobs/en/jobs/10554122/business-intelligence-engineer-ii-amazon-leo) | amazon | US, WA, Bellevue | 0.5594 | 2026-09-19 |
| [Data Scientist II, Amazon Travel & Events](https://www.amazon.jobs/jobs/10538046/data-scientist-ii-amazon-travel--events?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5508 | 2026-09-19 |
| [Area Occupancy Planner, Regional Portfolio Management (RPM-AMER) GREF](https://www.amazon.jobs/en/jobs/10554213/area-occupancy-planner-regional-portfolio-management-rpm-amer-gref) | amazon | US, CA, Culver City | 0.5188 | 2026-09-20 |
| [Commercial Skilling Director - Global Skilling](https://apply.careers.microsoft.com/careers/job/1970393557000102) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5171 | 2026-09-19 |
| [Cloud Solution Architect- AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556983961) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5152 | 2026-09-20 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556990540) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5104 | 2026-09-20 |
| [Digital Solution Area Specialist-Cloud & AI](https://apply.careers.microsoft.com/careers/job/1970393556992011) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Texas, Dallas; United States, Georgia, Atlanta; United States, North Dakota, Fargo | 0.5102 | 2026-09-19 |
| [Technical Solution Manager - Security Strategy](https://apply.careers.microsoft.com/careers/job/1970393556999983) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5057 | 2026-09-19 |
| [Principal Technical Program Manager- Trust](https://apply.careers.microsoft.com/careers/job/1970393556956145) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5041 | 2026-09-19 |
| [Senior Sales Specialist -Cloud & AI Platforms](https://apply.careers.microsoft.com/careers/job/1970393556984110) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4996 | 2026-09-20 |
| [Solution Engineer - AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556984043) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4900 | 2026-09-20 |
| [Cloud & AI Solution Engineering Manager](https://apply.careers.microsoft.com/careers/job/1970393556955544) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Texas, Las Colinas; United States, District of Columbia, Washington D.C.; United States, Georgia, Atlanta; United States, Illinois, Chicago | 0.4859 | 2026-09-19 |
| [Technical Program Manager, Strategy & Transformation](https://apply.careers.microsoft.com/careers/job/1970393556994709) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4754 | 2026-09-20 |
| [Pre-Construction Manager, Data Center (AMERS)](https://apply.careers.microsoft.com/careers/job/1970393556981449) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4693 | 2026-09-19 |
| [Compute & Infrastructure Counsel, Real Estate](https://job-boards.greenhouse.io/anthropic/jobs/5427969008) | anthropic | San Francisco, CA | 0.4541 | 2026-09-19 |
| [Technical Program Manager-AI Business Solutions](https://apply.careers.microsoft.com/careers/job/1970393556994711) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4469 | 2026-09-19 |
| [Senior NPI TPM, Ops, Last Mile Delivery & Technology](https://www.amazon.jobs/en/jobs/10554135/senior-npi-tpm-ops-last-mile-delivery-technology) | amazon | US, WA, Bellevue | 0.4445 | 2026-09-19 |
| [CAIP Sales Excellence Lead](https://apply.careers.microsoft.com/careers/job/1970393557000704) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4388 | 2026-09-19 |
| [Bilingual Account Executive (AI Natives)](https://apply.careers.microsoft.com/careers/job/1970393556994771) | microsoft | United States, Texas, Dallas; United States, Texas, Austin; United States, Texas, Houston; United States, New Mexico, Sante Fe; United States, California, San Francisco; United States, Multiple Locations, Multiple Locations | 0.4372 | 2026-09-19 |
| [Applied Scientist, AWS Infrastructure Services Science](https://www.amazon.jobs/jobs/10554058/applied-scientist-aws-infrastructure-services-science?cmpid=bsp-amazon-science) | amazon_science | US, VA, Herndon | 0.4352 | 2026-09-19 |
| [Sales Motion Strategy Lead](https://apply.careers.microsoft.com/careers/job/1970393557001918) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4308 | 2026-09-19 |
| [Principal Applied Scientist, AAIS](https://www.amazon.jobs/jobs/10553806/principal-applied-scientist-aais?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.4289 | 2026-09-19 |

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
