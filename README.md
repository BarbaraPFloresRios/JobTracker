[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist, Experience Analytics](https://www.amazon.jobs/jobs/10580770/data-scientist-experience-analytics?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.6562 | 2026-10-16 |
| [Data Scientist I, PXT Central Science](https://www.amazon.jobs/jobs/10579474/data-scientist-i-pxt-central-science?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.6052 | 2026-10-16 |
| [Specialist Solutions Architect – Data Lake and Semantics/Analytics (HCLS), Data Lake and Analytics](https://www.amazon.jobs/en/jobs/10581717/specialist-solutions-architect-data-lake-and-semantics-analytics-hcls-data-lake-and-analytics) | amazon | US, CA, San Francisco | 0.5990 | 2026-10-16 |
| [Software Development Manager, ADC Monitoring & Observability](https://www.amazon.jobs/en/jobs/10580970/software-development-manager-adc-monitoring-observability) | amazon | US, CO, Denver | 0.5990 | 2026-10-16 |
| [Ad Tech Consultant, Ad Tech Solutions](https://www.amazon.jobs/en/jobs/10581648/ad-tech-consultant-ad-tech-solutions) | amazon | US, NY, New York | 0.5894 | 2026-10-16 |
| [Applied Scientist III - AMZ10564053](https://www.amazon.jobs/jobs/10579121/applied-scientist-iii--amz?cmpid=bsp-amazon-science) | amazon_science | US, CA, Santa Monica | 0.5802 | 2026-10-16 |
| [Solution Engineering Manager - Cloud & AI Platform](https://apply.careers.microsoft.com/careers/job/1970393557040917) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5592 | 2026-10-17 |
| [Data Scientist II - AMZ10564077](https://www.amazon.jobs/jobs/10577453/data-scientist-ii--amz?cmpid=bsp-amazon-science) | amazon_science | US, CA, Sunnyvale | 0.5575 | 2026-10-16 |
| [Systems Development Engineer, Early Career – 2026 (US)](https://www.amazon.jobs/en/jobs/10581943/systems-development-engineer-early-career-2026-us) | amazon | US, WA, Seattle | 0.5563 | 2026-10-17 |
| [Category Analyst, Category Analytics](https://www.amazon.jobs/en/jobs/10581689/category-analyst-category-analytics) | amazon | US, TX, Austin | 0.5493 | 2026-10-16 |
| [Delivery Consultant - AI/ML, AWS Professional Services WWPS Healthcare and Life Science](https://www.amazon.jobs/en/jobs/10581850/delivery-consultant-ai-ml-aws-professional-services-wwps-healthcare-and-life-science) | amazon | US, VA, Arlington | 0.5426 | 2026-10-16 |
| [Data engineer, Decision Intelligence Technology](https://www.amazon.jobs/en/jobs/10581756/data-engineer-decision-intelligence-technology) | amazon | US, WA, Bellevue | 0.5416 | 2026-10-16 |
| [Applied Scientist II, Predictive Targeting](https://www.amazon.jobs/jobs/10580389/applied-scientist-ii-predictive-targeting?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5403 | 2026-10-16 |
| [Procurement Manager, Data Centers, Data Center Sourcing & Procurement](https://www.amazon.jobs/en/jobs/10581704/procurement-manager-data-centers-data-center-sourcing-procurement) | amazon | US, IL, Chicago | 0.5384 | 2026-10-16 |
| [Data Center Infrastructure Delivery Manager](https://www.amazon.jobs/en/jobs/10581897/data-center-infrastructure-delivery-manager) | amazon | US, MD, Frederick | 0.5378 | 2026-10-16 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10581828/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-16 |
| [Principal CX Program Manager](https://apply.careers.microsoft.com/careers/job/1970393557001406) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5317 | 2026-10-16 |
| [Product Manager, CoreAI](https://apply.careers.microsoft.com/careers/job/1970393557027388) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5259 | 2026-10-17 |
| [Applied Scientist II, Sponsored Products Bidding](https://www.amazon.jobs/en/jobs/10581930/applied-scientist-ii-sponsored-products-bidding) | amazon | US, WA, Seattle | 0.5238 | 2026-10-17 |
| [Software Engineer - Simulation, Fauna](https://www.amazon.jobs/en/jobs/10581340/software-engineer-simulation-fauna) | amazon | US, NY, New York | 0.5231 | 2026-10-16 |
| [Accounts Payable Analyst, FinOps, FinOps Support Center - HQ2](https://www.amazon.jobs/en/jobs/10581832/accounts-payable-analyst-finops-finops-support-center-hq2) | amazon | US, VA, Arlington | 0.5211 | 2026-10-16 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393557026008) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5195 | 2026-10-17 |
| [ICT Design Engineer, Data Center Design Engineering](https://www.amazon.jobs/en/jobs/10581923/ict-design-engineer-data-center-design-engineering) | amazon | US, VA, Herndon | 0.5162 | 2026-10-16 |
| [Data Center Facility Manager II - Nights](https://www.amazon.jobs/en/jobs/10581876/data-center-facility-manager-ii-nights) | amazon | US, OH, Jeffersonville | 0.5142 | 2026-10-16 |
| [Commissioning Engineer, AWS Commissioning](https://www.amazon.jobs/en/jobs/10581733/commissioning-engineer-aws-commissioning) | amazon | US, VA, Herndon | 0.5142 | 2026-10-16 |

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
