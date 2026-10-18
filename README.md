[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Solution Engineering Manager - Cloud & AI Platform](https://apply.careers.microsoft.com/careers/job/1970393557040917) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5601 | 2026-10-17 |
| [Systems Development Engineer, Early Career – 2026 (US)](https://www.amazon.jobs/en/jobs/10581943/systems-development-engineer-early-career-2026-us) | amazon | US, WA, Seattle | 0.5563 | 2026-10-17 |
| [Product Manager, CoreAI](https://apply.careers.microsoft.com/careers/job/1970393557027388) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5332 | 2026-10-17 |
| [Applied Scientist II, Sponsored Products Bidding](https://www.amazon.jobs/en/jobs/10581930/applied-scientist-ii-sponsored-products-bidding) | amazon | US, WA, Seattle | 0.5238 | 2026-10-17 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393557026008) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5208 | 2026-10-17 |
| [Sr Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393557026792) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5013 | 2026-10-17 |
| [Senior Solution Engineering - AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556984074) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4886 | 2026-10-17 |
| [Cloud Endpoint Global Black Belt (GBB)](https://apply.careers.microsoft.com/careers/job/1970393557022785) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4778 | 2026-10-17 |
| [Customer Success Manager, Enterprise Tech](https://job-boards.greenhouse.io/anthropic/jobs/5454800008) | anthropic | New York City, NY | 0.4744 | 2026-10-17 |
| [Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393557027338) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4668 | 2026-10-17 |
| [Sr. Procurement Manager - Electrical & Mechanical](https://apply.careers.microsoft.com/careers/job/1970393556978143) | microsoft | United States, California, San Jose; United States, Multiple Locations, Multiple Locations; United States, Washington, Redmond | 0.4617 | 2026-10-17 |
| [Principal Penetration Tester](https://apply.careers.microsoft.com/careers/job/1970393557027335) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4587 | 2026-10-17 |
| [Senior Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393557027336) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4578 | 2026-10-17 |
| [Systems Development Engineer, OISL Test Automation](https://www.amazon.jobs/en/jobs/10582075/systems-development-engineer-oisl-test-automation) | amazon | US, WA, Redmond | 0.4515 | 2026-10-17 |
| [Applied Scientist, Personalization, DTx Science](https://www.amazon.jobs/jobs/10581936/applied-scientist-personalization-dtx-science?cmpid=bsp-amazon-science) | amazon_science | US, NY, New York | 0.4474 | 2026-10-17 |
| [Sales Excellence Lead, Cloud and AI Platform](https://apply.careers.microsoft.com/careers/job/1970393557039176) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4440 | 2026-10-18 |
| [Data Scientist - Intelligent Experiences, MLO](https://jobs.apple.com/en-us/details/200687787-0836/data-scientist-intelligent-experiences-mlo?team=MLAI) | apple | nan | 0.4425 | 2026-10-17 |
| [Cloud Solution Architect](https://apply.careers.microsoft.com/careers/job/1970393557026798) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4387 | 2026-10-17 |
| [Digital Cloud & AI Solution Engineer - Azure Platform](https://apply.careers.microsoft.com/careers/job/1970393557040185) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4374 | 2026-10-17 |
| [Software Engineer, Full Stack — Dots](https://jobs.ashbyhq.com/openai/dbe79b89-e593-44b3-8aec-c667f7134445) | openai | New York City | 0.4270 | 2026-10-17 |
| [Senior Director, Business Program Management - Non-AI Capacity Leader](https://apply.careers.microsoft.com/careers/job/1970393557026897) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4219 | 2026-10-17 |
| [Multidisciplinary Manager (Software Engineering) - FDE](https://apply.careers.microsoft.com/careers/job/1970393556939556) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Washington, Redmond; United States, California, Mountain View; United States, Texas, Houston; United States, Texas, Austin; United States, Illinois, Chicago; United States, Massachusetts, Cambridge; United States, New York, New York; United States, Georgia, Atlanta | 0.4216 | 2026-10-17 |
| [Research Scientist II, PXT Central Science](https://www.amazon.jobs/jobs/10581666/research-scientist-ii-pxt-central-science?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.4211 | 2026-10-17 |
| [Optical Engineer, Amazon Leo - OISL](https://www.amazon.jobs/en/jobs/10582043/optical-engineer-amazon-leo-oisl) | amazon | US, WA, Redmond | 0.4161 | 2026-10-17 |
| [HW Test Development Engineer, Amazon LEO](https://www.amazon.jobs/en/jobs/10581935/hw-test-development-engineer-amazon-leo) | amazon | US, WA, Redmond | 0.4061 | 2026-10-17 |

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
