[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Center Manager - Night Shift, Data Center Operations](https://www.amazon.jobs/en/jobs/10537046/data-center-manager-night-shift-data-center-operations) | amazon | US, NC, Hamlet | 0.6045 | 2026-09-11 |
| [Data Engineer, SPTC](https://www.amazon.jobs/en/jobs/10537982/data-engineer-sptc) | amazon | US, WA, Seattle | 0.5828 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537013/data-center-technician) | amazon | US, PA, Berwick | 0.5754 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537012/data-center-technician) | amazon | US, PA, Berwick | 0.5754 | 2026-09-11 |
| [Principal Applied Scientist - AI for Life Sciences, AWS Applied AI Solutions - Life Sciences](https://www.amazon.jobs/en/jobs/10538102/principal-applied-scientist-ai-for-life-sciences-aws-applied-ai-solutions-life-sciences) | amazon | US, WA, Seattle | 0.5710 | 2026-09-11 |
| [Sr. Program Manager, Delivery Intelligence](https://apply.careers.microsoft.com/careers/job/1970393556950877) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5689 | 2026-09-12 |
| [Senior Manager, Applied Science](https://www.amazon.jobs/en/jobs/10537980/senior-manager-applied-science) | amazon | US, WA, Seattle | 0.5684 | 2026-09-11 |
| [Transportation Analyst , Vendor Flex](https://www.amazon.jobs/en/jobs/10537932/transportation-analyst-vendor-flex) | amazon | US, TN, Nashville | 0.5673 | 2026-09-11 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556751888) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5625 | 2026-09-12 |
| [Data Center Facility Operations Manager, DCEO Operations Team](https://www.amazon.jobs/en/jobs/10537596/data-center-facility-operations-manager-dceo-operations-team) | amazon | US, NC, Hamlet | 0.5583 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537781/data-center-technician) | amazon | US, PA, Berwick | 0.5536 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537728/data-center-technician) | amazon | US, PA, Berwick | 0.5536 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537592/data-center-technician) | amazon | US, PA, Berwick | 0.5536 | 2026-09-11 |
| [Data Center Technician, DCO](https://www.amazon.jobs/en/jobs/10536951/data-center-technician-dco) | amazon | US, PA, Berwick | 0.5534 | 2026-09-11 |
| [Sr Product Manager-Technical, SCOT Forecasting & Labs](https://www.amazon.jobs/en/jobs/10537791/sr-product-manager-technical-scot-forecasting-labs) | amazon | US, NY, New York | 0.5523 | 2026-09-11 |
| [Forward Deployed AI Integrator, Field Engineering](https://www.amazon.jobs/en/jobs/10537396/forward-deployed-ai-integrator-field-engineering) | amazon | US, VA, Herndon | 0.5489 | 2026-09-11 |
| [Developer Experience Engineer II and/or Senior Developer Experience Engineer](https://apply.careers.microsoft.com/careers/job/1970393556971398) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5460 | 2026-09-12 |
| [Solution Engineer - Cloud & AI Data Platform](https://apply.careers.microsoft.com/careers/job/1970393556958402) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5448 | 2026-09-11 |
| [Engineering Operations Technician, Amazon Ads BLX](https://www.amazon.jobs/en/jobs/10537367/engineering-operations-technician-amazon-ads-blx) | amazon | US, NV, Sparks | 0.5400 | 2026-09-11 |
| [Applied Science Manager, AWS Startups](https://www.amazon.jobs/jobs/10537816/applied-science-manager-aws-startups?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5337 | 2026-09-12 |
| [Learning Exp Designer, Amazon Flex WW Learning](https://www.amazon.jobs/en/jobs/10538003/learning-exp-designer-amazon-flex-ww-learning) | amazon | US, TX, Austin | 0.5329 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10536956/data-center-technician) | amazon | US, PA, Berwick | 0.5302 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537011/data-center-technician) | amazon | US, PA, Berwick | 0.5302 | 2026-09-11 |
| [Software Development Manager, Leo Security](https://www.amazon.jobs/en/jobs/10537052/software-development-manager-leo-security) | amazon | US, VA, Arlington | 0.5286 | 2026-09-11 |
| [Engineering Operations Technician](https://www.amazon.jobs/en/jobs/10537839/engineering-operations-technician) | amazon | US, NV, Sparks | 0.5248 | 2026-09-11 |

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
