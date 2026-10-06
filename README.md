[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist , Leo Customer Terminal](https://www.amazon.jobs/en/jobs/10569910/data-scientist-leo-customer-terminal) | amazon | US, WA, Redmond | 0.6632 | 2026-10-06 |
| [Applied Scientist, Advertiser Growth Engine](https://www.amazon.jobs/en/jobs/10569394/applied-scientist-advertiser-growth-engine) | amazon | US, NY, New York | 0.6501 | 2026-10-05 |
| [Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10569713/applied-scientist-fauna) | amazon | US, NY, New York | 0.6035 | 2026-10-05 |
| [Cloud Technical Account Manager, ES - Strategic Industries, ES - Strategic Industries](https://www.amazon.jobs/en/jobs/10568551/cloud-technical-account-manager-es-strategic-industries-es-strategic-industries) | amazon | US, NJ, Jersey City | 0.6029 | 2026-10-05 |
| [Software Development Engineer](https://www.amazon.jobs/en/jobs/10569781/software-development-engineer) | amazon | US, NY, New York | 0.5964 | 2026-10-05 |
| [Talent Intelligence Analyst, Global Specialty Recruiting](https://www.amazon.jobs/en/jobs/10569918/talent-intelligence-analyst-global-specialty-recruiting) | amazon | US, NY, New York | 0.5937 | 2026-10-06 |
| [Senior Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10569789/senior-applied-scientist-fauna) | amazon | US, NY, New York | 0.5921 | 2026-10-05 |
| [Clearable Data Center Technician, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10570706/clearable-data-center-technician-adc-infraops-dco) | amazon | US, CO, Aurora | 0.5687 | 2026-10-06 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10569948/data-center-technician-dcc-communities) | amazon | US, CA, Gilroy | 0.5588 | 2026-10-06 |
| [Data Center Network Deploy Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10569788/data-center-network-deploy-technician-dcc-communities) | amazon | US, VA, Manassas | 0.5583 | 2026-10-05 |
| [Inference Engineer, AGI](https://www.amazon.jobs/en/jobs/10569698/inference-engineer-agi) | amazon | US, CA, Sunnyvale | 0.5559 | 2026-10-05 |
| [Network Development Engineer, ADC Networking](https://www.amazon.jobs/en/jobs/10568870/network-development-engineer-adc-networking) | amazon | US, VA, Arlington | 0.5542 | 2026-10-05 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10569437/data-center-technician) | amazon | US, AZ, Mesa | 0.5520 | 2026-10-05 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10569443/data-center-technician) | amazon | US, AZ, Mesa | 0.5515 | 2026-10-05 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10569940/data-center-technician) | amazon | US, AZ, Glendales | 0.5489 | 2026-10-06 |
| [Cloud Sales Representative](https://www.amazon.jobs/en/jobs/10569617/cloud-sales-representative) | amazon | US, VA, Arlington | 0.5472 | 2026-10-05 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10569442/data-center-technician) | amazon | US, AZ, Glendale | 0.5467 | 2026-10-05 |
| [Bus Development Manager, Scale Sales, CSC, CSC SMB ](https://www.amazon.jobs/en/jobs/10568950/bus-development-manager-scale-sales-csc-csc-smb) | amazon | US, VA, Arlington | 0.5462 | 2026-10-05 |
| [DC Design Manager for Region (AMER), Data Center Engineering, DCDE - AMER](https://www.amazon.jobs/en/jobs/10569760/dc-design-manager-for-region-amer-data-center-engineering-dcde-amer) | amazon | US, TX, Austin | 0.5459 | 2026-10-05 |
| [Engineering Operations Technician, AWS Support](https://www.amazon.jobs/en/jobs/10569840/engineering-operations-technician-aws-support) | amazon | US, OR, Hermiston | 0.5441 | 2026-10-06 |
| [UX Designer , GOEST (Global Operations Enterprise Services - Tech)](https://www.amazon.jobs/en/jobs/10571101/ux-designer-goest-global-operations-enterprise-services-tech) | amazon | US, TX, Austin | 0.5409 | 2026-10-06 |
| [Infra Delivery Install Technician, AWS Support](https://www.amazon.jobs/en/jobs/10569952/infra-delivery-install-technician-aws-support) | amazon | US, MS, Ridgeland | 0.5398 | 2026-10-06 |
| [Software Development Engineer, Ads AI Core Infrastructure (ACI), Ads AI Core Infrastructure](https://www.amazon.jobs/en/jobs/10570504/software-development-engineer-ads-ai-core-infrastructure-aci-ads-ai-core-infrastructure) | amazon | US, NY, New York | 0.5396 | 2026-10-06 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10569444/data-center-technician) | amazon | US, AZ, Chandler | 0.5374 | 2026-10-05 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10569438/data-center-technician) | amazon | US, AZ, Chandler | 0.5364 | 2026-10-05 |

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
