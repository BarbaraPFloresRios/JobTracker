[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Principal Applied Scientist, WorkSpaces for AI Agents, Applied AI Solutions](https://www.amazon.jobs/en/jobs/10538705/principal-applied-scientist-workspaces-for-ai-agents-applied-ai-solutions) | amazon | US, WA, Seattle | 0.6107 | 2026-09-14 |
| [Recruiting Analytics Data Engineer ](https://job-boards.greenhouse.io/anthropic/jobs/5424111008) | anthropic | San Francisco, CA | 0.5816 | 2026-09-15 |
| [Delivery Consultant - AI/ML, AWS Professional Services WWPS Life Science](https://www.amazon.jobs/en/jobs/10538978/delivery-consultant-ai-ml-aws-professional-services-wwps-life-science) | amazon | US, GA, Atlanta | 0.5600 | 2026-09-14 |
| [Applied Scientist, Sponsored Products and Brands](https://www.amazon.jobs/en/jobs/10539382/applied-scientist-sponsored-products-and-brands) | amazon | US, WA, Seattle | 0.5487 | 2026-09-14 |
| [Data Center Chief Engineer](https://www.amazon.jobs/en/jobs/10539006/data-center-chief-engineer) | amazon | US, TX, Wilmer | 0.5479 | 2026-09-14 |
| [Data Center Chief Engineer](https://www.amazon.jobs/en/jobs/10539398/data-center-chief-engineer) | amazon | US, TX, Wilmer | 0.5479 | 2026-09-14 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556754360) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5401 | 2026-09-14 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556752185) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5339 | 2026-09-15 |
| [Worldwide Specialist Solutions Architect - GenAI, Data & AI GTM ](https://www.amazon.jobs/en/jobs/10539386/worldwide-specialist-solutions-architect-genai-data-ai-gtm) | amazon | US, NY, New York | 0.5325 | 2026-09-14 |
| [Data Center Engineering Operations Facility Manager, ADC InfraOps DCEO](https://www.amazon.jobs/en/jobs/10539234/data-center-engineering-operations-facility-manager-adc-infraops-dceo) | amazon | US, OH, Plain City | 0.5316 | 2026-09-14 |
| [Business Development Manager, AWS Cloud Intelligence , AWS Cloud Intelligence ](https://www.amazon.jobs/en/jobs/10539321/business-development-manager-aws-cloud-intelligence-aws-cloud-intelligence) | amazon | US, WA, Seattle | 0.5286 | 2026-09-14 |
| [Critical Infrastructure Mechanical Engineer, Field Engineering](https://www.amazon.jobs/en/jobs/10539077/critical-infrastructure-mechanical-engineer-field-engineering) | amazon | US, TX, San Antonio | 0.5262 | 2026-09-14 |
| [Solutions Architect, Greenfield, Automotive & Manufacturing](https://www.amazon.jobs/en/jobs/10539366/solutions-architect-greenfield-automotive-manufacturing) | amazon | US, MI, Detroit | 0.5237 | 2026-09-14 |
| [Software Development Engineer, CloudFront Console and Agentic Experience](https://www.amazon.jobs/en/jobs/10539081/software-development-engineer-cloudfront-console-and-agentic-experience) | amazon | US, WA, Seattle | 0.5229 | 2026-09-14 |
| [Engineering  Maintenance Technician](https://www.amazon.jobs/en/jobs/10538970/engineering-maintenance-technician) | amazon | US, CA, San Francisco | 0.5204 | 2026-09-14 |
| [Member of Technical Staff - Data Flywheel Infra, Frontier Models](https://apply.careers.microsoft.com/careers/job/1970393556982519) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5149 | 2026-09-14 |
| [Sourcing Recruiter, AWS Infrastructure Services (AIS) TA](https://www.amazon.jobs/en/jobs/10539236/sourcing-recruiter-aws-infrastructure-services-ais-ta) | amazon | US, WA, Seattle | 0.5118 | 2026-09-14 |
| [Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556984206) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5110 | 2026-09-14 |
| [Senior Developer Relations Manager, Capital Markets](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-NY-New-York/Senior-Developer-Relations-Manager--Capital-Markets_JR2017419-1) | nvidia | US, NY, New York; US, NY, Remote; US, CA, Remote; US, CA, Santa Clara | 0.5079 | 2026-09-14 |
| [Solution Area Specialist - AI Workforce](https://apply.careers.microsoft.com/careers/job/1970393556866170) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5072 | 2026-09-15 |
| [Bilingual Technical Customer Support, Ring, Ring](https://www.amazon.jobs/en/jobs/10539558/bilingual-technical-customer-support-ring-ring) | amazon | US, AZ, Virtual Location - Arizona | 0.5070 | 2026-09-14 |
| [GPU System Performance Architect](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-System-Performance-Architect_JR2025475) | nvidia | US, CA, Santa Clara; US, CO, Boulder; US, OR, Hillsboro | 0.5061 | 2026-09-14 |
| [Engineering Operations Technician](https://www.amazon.jobs/en/jobs/10539556/engineering-operations-technician) | amazon | US, PA, Berwick | 0.4949 | 2026-09-14 |
| [Engineering  Maintenance Technician](https://www.amazon.jobs/en/jobs/10538969/engineering-maintenance-technician) | amazon | US, CA, Hayward | 0.4946 | 2026-09-14 |
| [Solution Engineer - AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556866541) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4921 | 2026-09-15 |

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
