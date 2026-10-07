[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist , Leo Customer Terminal](https://www.amazon.jobs/en/jobs/10569910/data-scientist-leo-customer-terminal) | amazon | US, WA, Redmond | 0.6622 | 2026-10-06 |
| [Product Marketing Manager - Tech, AWS Observability](https://www.amazon.jobs/en/jobs/10571777/product-marketing-manager-tech-aws-observability) | amazon | US, CA, San Francisco | 0.6013 | 2026-10-07 |
| [Applied Scientist III, AGI Responsible AI (RAI)](https://www.amazon.jobs/en/jobs/10571444/applied-scientist-iii-agi-responsible-ai-rai) | amazon | US, CA, Sunnyvale | 0.6013 | 2026-10-07 |
| [Talent Intelligence Analyst, Global Specialty Recruiting](https://www.amazon.jobs/en/jobs/10569918/talent-intelligence-analyst-global-specialty-recruiting) | amazon | US, NY, New York | 0.5931 | 2026-10-06 |
| [Clearable Data Center Technician, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10570706/clearable-data-center-technician-adc-infraops-dco) | amazon | US, CO, Aurora | 0.5745 | 2026-10-06 |
| [Software Development Engineer (Embedded Systems) Intern, Amazon Leo - Summer 2027 (USA)](https://www.amazon.jobs/en/jobs/10571374/software-development-engineer-embedded-systems-intern-amazon-leo-summer-2027-usa) | amazon | US, WA, Redmond | 0.5685 | 2026-10-07 |
| [Customer Experience Program Manager II](https://apply.careers.microsoft.com/careers/job/1970393557000021) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5666 | 2026-10-06 |
| [Manager I, Data Center Operations, Data Center Operations](https://www.amazon.jobs/en/jobs/10572024/manager-i-data-center-operations-data-center-operations) | amazon | US, MD, Frederick | 0.5644 | 2026-10-07 |
| [UX Designer , GOEST (Global Operations Enterprise Services - Tech)](https://www.amazon.jobs/en/jobs/10571101/ux-designer-goest-global-operations-enterprise-services-tech) | amazon | US, TX, Austin | 0.5634 | 2026-10-06 |
| [Data Center Nights Manager ](https://www.amazon.jobs/en/jobs/10571948/data-center-nights-manager) | amazon | US, NV, Sparks | 0.5624 | 2026-10-07 |
| [Data Center Nights Manager ](https://www.amazon.jobs/en/jobs/10571952/data-center-nights-manager) | amazon | US, NV, Sparks | 0.5624 | 2026-10-07 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10569948/data-center-technician-dcc-communities) | amazon | US, CA, Gilroy | 0.5579 | 2026-10-06 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10569979/data-center-technician-dcc-communities) | amazon | US, CA, Gilroy | 0.5579 | 2026-10-06 |
| [Manager, Strategy and Capture, ALG](https://www.amazon.jobs/en/jobs/10571287/manager-strategy-and-capture-alg) | amazon | US, VA, Arlington | 0.5528 | 2026-10-07 |
| [Startup Solutions Architect](https://www.amazon.jobs/en/jobs/10572259/startup-solutions-architect) | amazon | US, CA, San Francisco | 0.5526 | 2026-10-07 |
| [Sr. Technical Program Manager, Amazon Leo](https://www.amazon.jobs/en/jobs/10572018/sr-technical-program-manager-amazon-leo) | amazon | US, WA, Bellevue | 0.5522 | 2026-10-07 |
| [Finance Manager, WW Ops Finance - CF Support](https://www.amazon.jobs/en/jobs/10571788/finance-manager-ww-ops-finance-cf-support) | amazon | US, TN, Nashville | 0.5517 | 2026-10-07 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10569940/data-center-technician) | amazon | US, AZ, Glendales | 0.5486 | 2026-10-06 |
| [Finance Manager, WW Ops Finance - CF Support](https://www.amazon.jobs/en/jobs/10571800/finance-manager-ww-ops-finance-cf-support) | amazon | US, VA, Arlington | 0.5476 | 2026-10-07 |
| [Applied Scientist, TSI Science](https://www.amazon.jobs/jobs/10570705/applied-scientist-tsi-science?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5473 | 2026-10-07 |
| [Software Development Engineer, Ads AI Core Infrastructure (ACI), Ads AI Core Infrastructure](https://www.amazon.jobs/en/jobs/10570504/software-development-engineer-ads-ai-core-infrastructure-aci-ads-ai-core-infrastructure) | amazon | US, NY, New York | 0.5470 | 2026-10-06 |
| [Engineering Operations Technician, AWS Support](https://www.amazon.jobs/en/jobs/10569840/engineering-operations-technician-aws-support) | amazon | US, OR, Hermiston | 0.5464 | 2026-10-06 |
| [Infra Delivery Install Technician, AWS Support](https://www.amazon.jobs/en/jobs/10569981/infra-delivery-install-technician-aws-support) | amazon | US, MS, Ridgeland | 0.5389 | 2026-10-06 |
| [Infra Delivery Install Technician, AWS Support](https://www.amazon.jobs/en/jobs/10569952/infra-delivery-install-technician-aws-support) | amazon | US, MS, Ridgeland | 0.5386 | 2026-10-06 |
| [Senior Technical Program Manager, Data Center Engineering](https://www.amazon.jobs/en/jobs/10569983/senior-technical-program-manager-data-center-engineering) | amazon | US, WA, Seattle | 0.5380 | 2026-10-06 |

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
