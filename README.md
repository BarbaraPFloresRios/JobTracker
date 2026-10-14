[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist II - AMZ10564077](https://www.amazon.jobs/en/jobs/10577453/data-scientist-ii-amz10564077) | amazon | US, CA, Sunnyvale | 0.6134 | 2026-10-13 |
| [Software Development Engineer , Ads Data Manager](https://www.amazon.jobs/en/jobs/10577607/software-development-engineer-ads-data-manager) | amazon | US, NY, New York | 0.6025 | 2026-10-13 |
| [Senior APN Programs Lead, Scalable GTM and Funding Programs ](https://www.amazon.jobs/en/jobs/10576437/senior-apn-programs-lead-scalable-gtm-and-funding-programs) | amazon | US, VA, Arlington | 0.5871 | 2026-10-13 |
| [Data Engineer II - AMZ10595704](https://www.amazon.jobs/en/jobs/10577490/data-engineer-ii-amz10595704) | amazon | US, CO, Denver | 0.5846 | 2026-10-13 |
| [Data Center Manager](https://www.amazon.jobs/en/jobs/10577646/data-center-manager) | amazon | US, MS, Ridgeland | 0.5770 | 2026-10-13 |
| [Data Center Manager](https://www.amazon.jobs/en/jobs/10578053/data-center-manager) | amazon | US, MS, Ridgeland | 0.5770 | 2026-10-14 |
| [Hardware Development Engineer Intern,  Summer 2027](https://www.amazon.jobs/en/jobs/10578090/hardware-development-engineer-intern-summer-2027) | amazon | US, CA, Sunnyvale | 0.5765 | 2026-10-14 |
| [Sr. Customer Solutions Manager, Auto and Manufacturing ](https://www.amazon.jobs/en/jobs/10577677/sr-customer-solutions-manager-auto-and-manufacturing) | amazon | US, GA, Atlanta | 0.5678 | 2026-10-13 |
| [Data Center Logistics Specialist, DCC Communities](https://www.amazon.jobs/en/jobs/10576577/data-center-logistics-specialist-dcc-communities) | amazon | US, IN, New Carlisle | 0.5566 | 2026-10-13 |
| [Senior AppMod GTM Specialist, Media & Entertainment , Media and Entertainment - ASPI](https://www.amazon.jobs/en/jobs/10577688/senior-appmod-gtm-specialist-media-entertainment-media-and-entertainment-aspi) | amazon | US, NY, New York | 0.5535 | 2026-10-13 |
| [Senior Healthcare Solutions Architect, AI Solutions](https://www.amazon.jobs/en/jobs/10576576/senior-healthcare-solutions-architect-ai-solutions) | amazon | US, CA, San Francisco | 0.5497 | 2026-10-13 |
| [Sr. Product Manager, NAS Ship Cost Optimization ](https://www.amazon.jobs/en/jobs/10578026/sr-product-manager-nas-ship-cost-optimization) | amazon | US, WA, Seattle | 0.5468 | 2026-10-13 |
| [Data Center Technician III, DCO](https://www.amazon.jobs/en/jobs/10577167/data-center-technician-iii-dco) | amazon | US, OR, Boardman | 0.5463 | 2026-10-13 |
| [Cloud Technical Account Manager , ES - Strategic Industries](https://www.amazon.jobs/en/jobs/10578036/cloud-technical-account-manager-es-strategic-industries) | amazon | US, TX, Dallas | 0.5425 | 2026-10-13 |
| [DCO Tech (Night), DCO](https://www.amazon.jobs/en/jobs/10576966/dco-tech-night-dco) | amazon | US, NV, Sparks | 0.5387 | 2026-10-13 |
| [Sr. Product Lifecycle Mechanical Engineer, DCE - Mechanical Products & Services (MPS) ](https://www.amazon.jobs/en/jobs/10577780/sr-product-lifecycle-mechanical-engineer-dce-mechanical-products-services-mps) | amazon | US, VA, Herndon | 0.5347 | 2026-10-13 |
| [Engineering Operations Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10576566/engineering-operations-technician-dcc-communities) | amazon | US, OR, Boardman | 0.5336 | 2026-10-13 |
| [ASIC Engineer Early Career - 2027, Project Leo](https://www.amazon.jobs/en/jobs/10576621/asic-engineer-early-career-2027-project-leo) | amazon | US, WA, Redmond | 0.5316 | 2026-10-13 |
| [Principal Technical Program Manager, AI Supercomputer Operations](https://apply.careers.microsoft.com/careers/job/1970393557027420) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5251 | 2026-10-13 |
| [Sr. Tech Infra Program Manager, Capacity Delivery Planning](https://www.amazon.jobs/en/jobs/10577203/sr-tech-infra-program-manager-capacity-delivery-planning) | amazon | US, WA, Seattle | 0.5243 | 2026-10-13 |
| [Senior Solutions Architect, National Security Solutions Architecture Team](https://www.amazon.jobs/en/jobs/10576968/senior-solutions-architect-national-security-solutions-architecture-team) | amazon | US, VA, Herndon | 0.5237 | 2026-10-13 |
| [Sr. Life Sciences Business Development Lead, AI Solutions](https://www.amazon.jobs/en/jobs/10576622/sr-life-sciences-business-development-lead-ai-solutions) | amazon | US, CA, San Francisco | 0.5208 | 2026-10-13 |
| [Senior Engagement Manager, Professional Services, AWSI](https://www.amazon.jobs/en/jobs/10577746/senior-engagement-manager-professional-services-awsi) | amazon | US, NY, New York | 0.5180 | 2026-10-13 |
| [Sr. Mechanical Product Engineer, Data Center Eng, MPS](https://www.amazon.jobs/en/jobs/10577753/sr-mechanical-product-engineer-data-center-eng-mps) | amazon | US, TX, Austin | 0.5169 | 2026-10-13 |
| [ASIC Engineer Intern, Summer 2027](https://www.amazon.jobs/en/jobs/10576619/asic-engineer-intern-summer-2027) | amazon | US, CA, Sunnyvale | 0.5156 | 2026-10-13 |

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
