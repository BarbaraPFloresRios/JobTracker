[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Sr Data Scientist, Amazon - Vertical Ads](https://www.amazon.jobs/en/jobs/10566181/sr-data-scientist-amazon-vertical-ads) | amazon | US, CA, Palo Alto | 0.6456 | 2026-10-01 |
| [Software Development Engineer, ROBOTICS, Early Career - 2027](https://www.amazon.jobs/en/jobs/10567489/software-development-engineer-robotics-early-career-2027) | amazon | US, MA, North Reading | 0.6018 | 2026-10-02 |
| [ISV Marketing Manager , NAMER Strategic Customer and Partner Marketing](https://www.amazon.jobs/en/jobs/10566918/isv-marketing-manager-namer-strategic-customer-and-partner-marketing) | amazon | US, TX, Austin | 0.5863 | 2026-10-01 |
| [Senior Product Manager - Tech, PV Commerce & International Product](https://www.amazon.jobs/en/jobs/10566994/senior-product-manager-tech-pv-commerce-international-product) | amazon | US, WA, Seattle | 0.5824 | 2026-10-01 |
| [Senior ML Compiler Engineer, Neuron](https://www.amazon.jobs/en/jobs/10566149/senior-ml-compiler-engineer-neuron) | amazon | US, WA, Seattle | 0.5824 | 2026-10-01 |
| [Sr Data Scientist, Amazon - Vertical Ads](https://www.amazon.jobs/jobs/10566181/sr-data-scientist-amazon--vertical-ads?cmpid=bsp-amazon-science) | amazon_science | US, CA, Palo Alto | 0.5767 | 2026-10-01 |
| [Sr. Applied Scientist, Prime Video - Title Lifecycle Presentation](https://www.amazon.jobs/en/jobs/10567257/sr-applied-scientist-prime-video-title-lifecycle-presentation) | amazon | US, WA, Seattle | 0.5692 | 2026-10-01 |
| [Solutions Architect, Engineering, Construction, Real Estate, and Transportation](https://www.amazon.jobs/en/jobs/10566717/solutions-architect-engineering-construction-real-estate-and-transportation) | amazon | US, VA, Arlington | 0.5673 | 2026-10-01 |
| [Strategic Account Rep, Strategic Accounts ](https://www.amazon.jobs/en/jobs/10567425/strategic-account-rep-strategic-accounts) | amazon | US, WA, Seattle | 0.5582 | 2026-10-02 |
| [Data Center Technician, DCC Communities, DCO Tech](https://www.amazon.jobs/en/jobs/10567270/data-center-technician-dcc-communities-dco-tech) | amazon | US, GA, Lithia Springs | 0.5462 | 2026-10-01 |
| [Business Intel Engineer III - AMZ10540501](https://www.amazon.jobs/en/jobs/10567307/business-intel-engineer-iii-amz10540501) | amazon | US, WA, Seattle | 0.5459 | 2026-10-01 |
| [Senior Product Manager - Tech, Private Pricing Programs & Experiences (3PX)](https://www.amazon.jobs/en/jobs/10567011/senior-product-manager-tech-private-pricing-programs-experiences-3px) | amazon | US, NY, New York | 0.5450 | 2026-10-01 |
| [Manager, Applied Science, Sales AI](https://www.amazon.jobs/jobs/10565896/manager-applied-science-sales-ai?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5378 | 2026-10-01 |
| [Data Center Regional Chief Engineer, PHX/RNO](https://www.amazon.jobs/en/jobs/10566567/data-center-regional-chief-engineer-phx-rno) | amazon | US, NV, Sparks | 0.5360 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566892/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566906/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566905/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566883/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566884/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566899/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566893/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566895/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566885/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Data Center Facility Manager II](https://www.amazon.jobs/en/jobs/10566903/data-center-facility-manager-ii) | amazon | US, OH, Jeffersonville | 0.5357 | 2026-10-01 |
| [Sr. Solutions Architect, Cross-Industry Greenfield](https://www.amazon.jobs/en/jobs/10566669/sr-solutions-architect-cross-industry-greenfield) | amazon | US, NY, New York | 0.5325 | 2026-10-01 |

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
