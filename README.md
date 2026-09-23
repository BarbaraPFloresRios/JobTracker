[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist II, Device Economics](https://www.amazon.jobs/en/jobs/10556575/data-scientist-ii-device-economics) | amazon | US, CA, Sunnyvale | 0.6609 | 2026-09-22 |
| [AI Platform Data Engineer, Ring Agent Platform Org](https://www.amazon.jobs/en/jobs/10556787/ai-platform-data-engineer-ring-agent-platform-org) | amazon | US, CA, Hawthorne | 0.6512 | 2026-09-22 |
| [Principal Product Manager, Amazon Customer Service Data Intelligence](https://www.amazon.jobs/en/jobs/10556415/principal-product-manager-amazon-customer-service-data-intelligence) | amazon | US, WA, Seattle | 0.6502 | 2026-09-22 |
| [Applied Scientist, Customer360](https://www.amazon.jobs/en/jobs/10557022/applied-scientist-customer360) | amazon | US, WA, Seattle | 0.6420 | 2026-09-23 |
| [Applied Scientist, Catalog System Services Science](https://www.amazon.jobs/en/jobs/10557777/applied-scientist-catalog-system-services-science) | amazon | US, WA, Seattle | 0.6178 | 2026-09-23 |
| [Program Manager, Amazon Flex BOSS](https://www.amazon.jobs/en/jobs/10556260/program-manager-amazon-flex-boss) | amazon | US, TX, Austin | 0.5923 | 2026-09-22 |
| [Senior Business Analytics Specialist](https://apply.careers.microsoft.com/careers/job/1970393557002690) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5891 | 2026-09-23 |
| [Sr Solutions Architect, BDT](https://www.amazon.jobs/en/jobs/10556400/sr-solutions-architect-bdt) | amazon | US, WA, Seattle | 0.5737 | 2026-09-22 |
| [Senior Applied Scientist, Amazon Connect](https://www.amazon.jobs/en/jobs/10557099/senior-applied-scientist-amazon-connect) | amazon | US, NY, New York | 0.5735 | 2026-09-23 |
| [Systems Engineer, Controls Fleet, Data Center Capacity Delivery](https://www.amazon.jobs/en/jobs/10555490/systems-engineer-controls-fleet-data-center-capacity-delivery) | amazon | US, VA, Herndon | 0.5715 | 2026-09-22 |
| [Data Engineer, Decision Intelligence Technology](https://www.amazon.jobs/en/jobs/10557661/data-engineer-decision-intelligence-technology) | amazon | US, WA, Bellevue | 0.5670 | 2026-09-23 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556112/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556139/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556114/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556127/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556110/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556113/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556137/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556136/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556135/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556105/data-center-technician) | amazon | US, MS, Canton | 0.5651 | 2026-09-22 |
| [Logistics Manager II, Data Center Materials, Logistics - Data Center Operations](https://www.amazon.jobs/en/jobs/10556574/logistics-manager-ii-data-center-materials-logistics-data-center-operations) | amazon | US, GA, Lithia Springs | 0.5647 | 2026-09-22 |
| [Applied Scientist II— Robotics & Physical AI, Autonomous Lab, WW Sustainability](https://www.amazon.jobs/en/jobs/10556642/applied-scientist-ii-robotics-physical-ai-autonomous-lab-ww-sustainability) | amazon | US, WA, Seattle | 0.5630 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556104/data-center-technician) | amazon | US, MS, Canton | 0.5628 | 2026-09-22 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10556130/data-center-technician) | amazon | US, MS, Canton | 0.5628 | 2026-09-22 |

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
