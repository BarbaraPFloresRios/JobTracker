[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Delivery Consultant - Connect and Lex, Amazon Connect Center of  Delivery Excellence](https://www.amazon.jobs/en/jobs/10554930/delivery-consultant-connect-and-lex-amazon-connect-center-of-delivery-excellence) | amazon | US, GA, Atlanta | 0.5517 | 2026-09-21 |
| [Marketing Manager, Amazon Grocery, Amazon Grocery](https://www.amazon.jobs/en/jobs/10555270/marketing-manager-amazon-grocery-amazon-grocery) | amazon | US, TX, Austin | 0.5476 | 2026-09-21 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556990540) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5436 | 2026-09-20 |
| [Sr Solution Engineer, Cloud & AI Infrastructure - CTJ - Top Secret](https://apply.careers.microsoft.com/careers/job/1970393556999949) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5419 | 2026-09-20 |
| [Senior Solution Area Specialist - AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556983980) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5231 | 2026-09-21 |
| [Area Occupancy Planner, Regional Portfolio Management (RPM-AMER) GREF](https://www.amazon.jobs/en/jobs/10554213/area-occupancy-planner-regional-portfolio-management-rpm-amer-gref) | amazon | US, CA, Culver City | 0.5046 | 2026-09-20 |
| [Solution Engineer - AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556984043) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5019 | 2026-09-20 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556989685) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4980 | 2026-09-21 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10554491/data-center-technician) | amazon | US, PA, Berwick | 0.4922 | 2026-09-21 |
| [Senior Sales Specialist -Cloud & AI Platforms](https://apply.careers.microsoft.com/careers/job/1970393556984110) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4917 | 2026-09-20 |
| [Regional Data Center Manager](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-OR-Remote/Regional-Data-Center-Manager_JR2022565-1) | nvidia | US, OR, Remote | 0.4899 | 2026-09-21 |
| [Developer Relations Manager, Higher Education and Research - Foundational AI](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Developer-Relations-Manager--Higher-Education-and-Research---Foundational-AI_JR2026229) | nvidia | US, CA, Santa Clara; US, Remote | 0.4845 | 2026-09-21 |
| [Manager, Applied Science- Manipulation & Autonomy , Fauna](https://www.amazon.jobs/en/jobs/10555029/manager-applied-science-manipulation-autonomy-fauna) | amazon | US, NY, New York | 0.4836 | 2026-09-21 |
| [Software Development Engineer, Kiro](https://www.amazon.jobs/en/jobs/10554903/software-development-engineer-kiro) | amazon | US, WA, Seattle | 0.4791 | 2026-09-21 |
| [Cloud Solution Architect- AI Business Process](https://apply.careers.microsoft.com/careers/job/1970393556983961) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4773 | 2026-09-20 |
| [Technical Program Manager, Strategy & Transformation](https://apply.careers.microsoft.com/careers/job/1970393556994709) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4754 | 2026-09-20 |
| [Sr. Program Manager, Vendor Management, Worldwide Grocery Stores - Growth & Development](https://www.amazon.jobs/en/jobs/10554958/sr-program-manager-vendor-management-worldwide-grocery-stores-growth-development) | amazon | US, TX, Austin | 0.4695 | 2026-09-21 |
| [UX Designer, Amazon Delivery Customer Experience](https://www.amazon.jobs/en/jobs/10554899/ux-designer-amazon-delivery-customer-experience) | amazon | US, WA, Bellevue | 0.4666 | 2026-09-21 |
| [Applied AI Architect](https://job-boards.greenhouse.io/anthropic/jobs/5424310008) | anthropic | Bangalore, India | 0.4639 | 2026-09-21 |
| [Aerospace Manufacturing Engineer, Amazon Leo](https://www.amazon.jobs/en/jobs/10555286/aerospace-manufacturing-engineer-amazon-leo) | amazon | US, WA, Kirkland | 0.4606 | 2026-09-21 |
| [Account Executive, Higher Education](https://jobs.smartrecruiters.com/Canva/6000000001424458-account-executive-higher-education) | canva | Austin, , United States | 0.4529 | 2026-09-21 |
| [Sr. Enterprise Account Manager, Travel & Hospitality](https://www.amazon.jobs/en/jobs/10555109/sr-enterprise-account-manager-travel-hospitality) | amazon | US, IL, Chicago | 0.4524 | 2026-09-21 |
| [Data Center Network Deploy Technician, DCC Communities](https://www.amazon.jobs/en/jobs/10554919/data-center-network-deploy-technician-dcc-communities) | amazon | US, VA, Sterling | 0.4458 | 2026-09-21 |
| [Technical Program Manager, Business Operations Procurement Management](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-OR-Remote/Technical-Program-Manager--Business-Operations-Procurement-Management_JR2024039) | nvidia | US, OR, Remote; US, VA, Remote | 0.4429 | 2026-09-21 |
| [Sr. Software Development Engineer, Kiro](https://www.amazon.jobs/en/jobs/10554905/sr-software-development-engineer-kiro) | amazon | US, WA, Seattle | 0.4423 | 2026-09-21 |

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
