[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Delivery Consultant - AI/ML, Professional Services, AWS Industries ](https://www.amazon.jobs/en/jobs/10579915/delivery-consultant-ai-ml-professional-services-aws-industries) | amazon | US, IL, Chicago | 0.6188 | 2026-10-15 |
| [Delivery Consultant - Data , Professional Services, AWS Industries ](https://www.amazon.jobs/en/jobs/10579918/delivery-consultant-data-professional-services-aws-industries) | amazon | US, VA, Arlington | 0.6041 | 2026-10-15 |
| [Business Intelligence Engineer - AWS, AWS DC Construction](https://www.amazon.jobs/en/jobs/10579778/business-intelligence-engineer-aws-aws-dc-construction) | amazon | US, WA, Seattle | 0.5994 | 2026-10-15 |
| [Software Development Manager, ADC Monitoring & Observability](https://www.amazon.jobs/en/jobs/10580970/software-development-manager-adc-monitoring-observability) | amazon | US, CO, Denver | 0.5867 | 2026-10-16 |
| [Senior Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10580777/senior-applied-scientist-fauna) | amazon | US, CA, Sunnyvale | 0.5801 | 2026-10-15 |
| [Data Center Facility Manager II- Nights](https://www.amazon.jobs/en/jobs/10580763/data-center-facility-manager-ii-nights) | amazon | US, OH, Jeffersonville | 0.5736 | 2026-10-15 |
| [Data Center Facility Manager, Data Center Community](https://www.amazon.jobs/en/jobs/10579820/data-center-facility-manager-data-center-community) | amazon | US, IN, New Carlisle | 0.5725 | 2026-10-15 |
| [Infra Delivery Technician ](https://www.amazon.jobs/en/jobs/10579308/infra-delivery-technician) | amazon | US, TX, Wink | 0.5595 | 2026-10-15 |
| [Consultant, Agentic Delivery Acceleration, Professional Services, Professional Services](https://www.amazon.jobs/en/jobs/10579370/consultant-agentic-delivery-acceleration-professional-services-professional-services) | amazon | US, GA, Atlanta | 0.5580 | 2026-10-15 |
| [Data Scientist II - AMZ10564077](https://www.amazon.jobs/jobs/10577453/data-scientist-ii--amz?cmpid=bsp-amazon-science) | amazon_science | US, CA, Sunnyvale | 0.5574 | 2026-10-16 |
| [Senior Data Engineer , AWS Infrastructure Supply Chain Intelligence](https://www.amazon.jobs/en/jobs/10580107/senior-data-engineer-aws-infrastructure-supply-chain-intelligence) | amazon | US, WA, Bellevue | 0.5446 | 2026-10-15 |
| [Principal Solutions Architect, Retail, Consumer Goods & Restaurants, AWS](https://www.amazon.jobs/en/jobs/10580795/principal-solutions-architect-retail-consumer-goods-restaurants-aws) | amazon | US, OR, Portland | 0.5445 | 2026-10-15 |
| [Customer Solutions Manager, Media & Entertainment, TMEGS](https://www.amazon.jobs/en/jobs/10580783/customer-solutions-manager-media-entertainment-tmegs) | amazon | US, CA, San Francisco | 0.5444 | 2026-10-15 |
| [Software Development Engineer](https://www.amazon.jobs/en/jobs/10579435/software-development-engineer) | amazon | US, WA, Seattle | 0.5417 | 2026-10-15 |
| [Senior Manager, Hardware Engineering, Robotics Technical Services](https://www.amazon.jobs/en/jobs/10579864/senior-manager-hardware-engineering-robotics-technical-services) | amazon | US, MA, North Reading | 0.5411 | 2026-10-15 |
| [Global Datacenter Engineer Sr Lease Program Manager-AI](https://apply.careers.microsoft.com/careers/job/1970393557023015) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5400 | 2026-10-15 |
| [Senior Networking Solutions Architect, AWS Strategic Accounts](https://www.amazon.jobs/en/jobs/10579335/senior-networking-solutions-architect-aws-strategic-accounts) | amazon | US, WA, Seattle | 0.5383 | 2026-10-15 |
| [Energy Procurement Manager, AWS Energy Team](https://www.amazon.jobs/en/jobs/10579851/energy-procurement-manager-aws-energy-team) | amazon | US, WA, Seattle | 0.5356 | 2026-10-15 |
| [Sr. Delivery Consultant – Modernization, Professional Services, AWS Industries](https://www.amazon.jobs/en/jobs/10579919/sr-delivery-consultant-modernization-professional-services-aws-industries) | amazon | US, VA, Arlington | 0.5337 | 2026-10-15 |
| [Senior Engagement Manager, AWS ProServe](https://www.amazon.jobs/en/jobs/10579795/senior-engagement-manager-aws-proserve) | amazon | US, CO, Denver | 0.5318 | 2026-10-15 |
| [Principal Software Engineer, Storage Infrastructure](https://apply.careers.microsoft.com/careers/job/1970393557024780) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.5259 | 2026-10-15 |
| [Software Dev Manager, Amazon EMR](https://www.amazon.jobs/en/jobs/10579396/software-dev-manager-amazon-emr) | amazon | US, CA, East Palo Alto | 0.5232 | 2026-10-15 |
| [Manager III, Network Development Engineering, Bespoke Solutions](https://www.amazon.jobs/en/jobs/10580380/manager-iii-network-development-engineering-bespoke-solutions) | amazon | US, VA, Arlington | 0.5231 | 2026-10-15 |
| [Principal, Organization Effectiveness Specialist, Ads, IMDb & Grand Challenge](https://www.amazon.jobs/en/jobs/10579821/principal-organization-effectiveness-specialist-ads-imdb-grand-challenge) | amazon | US, WA, Seattle | 0.5197 | 2026-10-15 |
| [Senior Financial Analyst, NACF](https://www.amazon.jobs/en/jobs/10580279/senior-financial-analyst-nacf) | amazon | US, NY, New York City | 0.5190 | 2026-10-15 |

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
