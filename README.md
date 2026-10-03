[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Delivery Consultant- AI/ML, Data & Machine Learning (DML)](https://www.amazon.jobs/en/jobs/10567886/delivery-consultant-ai-ml-data-machine-learning-dml) | amazon | US, VA, Arlington | 0.6449 | 2026-10-02 |
| [Senior Applied Scientist, ASCS AI Lab Team](https://www.amazon.jobs/en/jobs/10567981/senior-applied-scientist-ascs-ai-lab-team) | amazon | US, WA, Seattle | 0.6437 | 2026-10-02 |
| [Data Scientist, Amazon Ads Marketing Decision Science](https://www.amazon.jobs/en/jobs/10568249/data-scientist-amazon-ads-marketing-decision-science) | amazon | US, NY, New York | 0.6285 | 2026-10-02 |
| [Sr. Delivery Consultant - AI/ML, WWPS ProServe](https://www.amazon.jobs/en/jobs/10567894/sr-delivery-consultant-ai-ml-wwps-proserve) | amazon | US, VA, Arlington | 0.6222 | 2026-10-02 |
| [Data Scientist, Amazon Ads Marketing Decision Science](https://www.amazon.jobs/jobs/10568249/data-scientist-amazon-ads-marketing-decision-science?cmpid=bsp-amazon-science) | amazon_science | US, NY, New York | 0.6188 | 2026-10-03 |
| [Senior Data Scientist, AWS Central Econ and Science](https://www.amazon.jobs/en/jobs/10568149/senior-data-scientist-aws-central-econ-and-science) | amazon | US, NY, New York | 0.6162 | 2026-10-02 |
| [Software Development Engineer, ROBOTICS, Early Career - 2027](https://www.amazon.jobs/en/jobs/10567489/software-development-engineer-robotics-early-career-2027) | amazon | US, MA, North Reading | 0.6014 | 2026-10-02 |
| [Applied Scientist, PXT Central Science](https://www.amazon.jobs/jobs/10567408/applied-scientist-pxt-central-science?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5777 | 2026-10-02 |
| [Sr. Applied Scientist, AI & AGI Security](https://www.amazon.jobs/en/jobs/10567882/sr-applied-scientist-ai-agi-security) | amazon | US, NY, New York | 0.5743 | 2026-10-02 |
| [Sr Applied Scientist, Ring AI](https://www.amazon.jobs/en/jobs/10567915/sr-applied-scientist-ring-ai) | amazon | US, CA, Sunnyvale | 0.5741 | 2026-10-02 |
| [Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10567501/applied-scientist-fauna) | amazon | US, NY, New York | 0.5692 | 2026-10-02 |
| [Program Manager Data Center Operations, RNO](https://www.amazon.jobs/en/jobs/10567804/program-manager-data-center-operations-rno) | amazon | US, NV, Sparks | 0.5541 | 2026-10-02 |
| [Global Category Manager](https://www.amazon.jobs/en/jobs/10568426/global-category-manager) | amazon | US, CA, Cupertino | 0.5533 | 2026-10-03 |
| [Strategic Account Rep, Strategic Accounts ](https://www.amazon.jobs/en/jobs/10567425/strategic-account-rep-strategic-accounts) | amazon | US, WA, Seattle | 0.5520 | 2026-10-02 |
| [Program Manager III, Strategic Initiatives Team](https://www.amazon.jobs/en/jobs/10568006/program-manager-iii-strategic-initiatives-team) | amazon | US, TX, Austin | 0.5441 | 2026-10-02 |
| [Bus Intel Eng II AMZ1242164, Reputation Marketing & Insights](https://www.amazon.jobs/en/jobs/10567500/bus-intel-eng-ii-amz1242164-reputation-marketing-insights) | amazon | US, VA, Arlington | 0.5411 | 2026-10-02 |
| [Manager of Construction, Data Center Construction](https://www.amazon.jobs/en/jobs/10568167/manager-of-construction-data-center-construction) | amazon | US, IN, New Carlisle | 0.5360 | 2026-10-02 |
| [Engagement Manager, Professional Services](https://www.amazon.jobs/en/jobs/10568356/engagement-manager-professional-services) | amazon | US, GA, Atlanta | 0.5336 | 2026-10-02 |
| [Data Center Infrastructure Delivery Manager](https://www.amazon.jobs/en/jobs/10568288/data-center-infrastructure-delivery-manager) | amazon | US, TX, Wink | 0.5325 | 2026-10-02 |
| [Software Development Engineer – AI/ML Networking Disaggregated Inference, Annapurna Labs , Elastic Collectives](https://www.amazon.jobs/en/jobs/10567360/software-development-engineer-ai-ml-networking-disaggregated-inference-annapurna-labs-elastic-collectives) | amazon | US, CA, Cupertino | 0.5254 | 2026-10-02 |
| [Senior Security Engineer, AI & AGI Security](https://www.amazon.jobs/en/jobs/10567905/senior-security-engineer-ai-agi-security) | amazon | US, WA, Seattle | 0.5251 | 2026-10-02 |
| [Infra Delivery Technician ](https://www.amazon.jobs/en/jobs/10567889/infra-delivery-technician) | amazon | US, TX, Wilmer | 0.5229 | 2026-10-02 |
| [Sr. Customer Solutions Manager, ISV](https://www.amazon.jobs/en/jobs/10567354/sr-customer-solutions-manager-isv) | amazon | US, VA, Arlington | 0.5224 | 2026-10-02 |
| [Software Development Engineer (SDE2), AWS](https://www.amazon.jobs/en/jobs/10568432/software-development-engineer-sde2-aws) | amazon | US, WA, Seattle | 0.5193 | 2026-10-03 |
| [Cloud Solution Architect - Cloud & AI Applications](https://apply.careers.microsoft.com/careers/job/1970393557000185) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5170 | 2026-10-02 |

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
