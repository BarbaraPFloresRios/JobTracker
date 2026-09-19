[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Engineer, Ring Agent Platforms](https://www.amazon.jobs/en/jobs/10553797/data-engineer-ring-agent-platforms) | amazon | US, CA, Hawthorne | 0.6553 | 2026-09-18 |
| [Principal Technical Account Manager, ES - NAMER - US-Frontier AI](https://www.amazon.jobs/en/jobs/10553420/principal-technical-account-manager-es-namer-us-frontier-ai) | amazon | US, CA, San Francisco | 0.6251 | 2026-09-18 |
| [Machine Learning - Compiler Engineer , AWS Neuron, Annapurna Labs](https://www.amazon.jobs/en/jobs/10552986/machine-learning-compiler-engineer-aws-neuron-annapurna-labs) | amazon | US, CA, Cupertino | 0.5989 | 2026-09-18 |
| [Data Center Facility Manager](https://www.amazon.jobs/en/jobs/10553816/data-center-facility-manager) | amazon | US, AZ, Mesa | 0.5922 | 2026-09-18 |
| [Data Scientist II, Amazon Travel & Events](https://www.amazon.jobs/jobs/10538046/data-scientist-ii-amazon-travel--events?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5884 | 2026-09-19 |
| [Principal Data Engineer](https://apply.careers.microsoft.com/careers/job/1970393556958759) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5623 | 2026-09-19 |
| [Business Intelligence Engineer II, Amazon Leo](https://www.amazon.jobs/en/jobs/10554122/business-intelligence-engineer-ii-amazon-leo) | amazon | US, WA, Bellevue | 0.5594 | 2026-09-19 |
| [Senior Delivery Consultant – AI/ML, WWPS ProServe](https://www.amazon.jobs/en/jobs/10553975/senior-delivery-consultant-ai-ml-wwps-proserve) | amazon | US, CO, Denver | 0.5578 | 2026-09-18 |
| [Senior Electrical Engineer Data Centers](https://apply.careers.microsoft.com/careers/job/1970393556956383) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.5545 | 2026-09-18 |
| [Delivery Practice Manager, WWPS ProServe](https://www.amazon.jobs/en/jobs/10553815/delivery-practice-manager-wwps-proserve) | amazon | US, MD, Jessup | 0.5543 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553567/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553582/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553566/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553570/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553562/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553585/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553596/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553593/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553594/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553592/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553563/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5534 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553555/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5527 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553573/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5527 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553556/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5527 | 2026-09-18 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10553569/infra-delivery-install-technician) | amazon | US, MS, Canton | 0.5527 | 2026-09-18 |

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
