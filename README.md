[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Business Analyst, Talent Acquisition Analytics](https://www.amazon.jobs/en/jobs/10536521/business-analyst-talent-acquisition-analytics) | amazon | US, WA, Seattle | 0.5735 | 2026-09-10 |
| [Data Center Manager - Night Shift, Data Center Operations](https://www.amazon.jobs/en/jobs/10537046/data-center-manager-night-shift-data-center-operations) | amazon | US, NC, Hamlet | 0.5657 | 2026-09-11 |
| [Senior Engagement Manager, AWS ProServe EDU & SLG](https://www.amazon.jobs/en/jobs/10536565/senior-engagement-manager-aws-proserve-edu-slg) | amazon | US, TX, Dallas | 0.5510 | 2026-09-10 |
| [Systems Development Engineer II, AWS Commerce Platform-ADC](https://www.amazon.jobs/en/jobs/10536416/systems-development-engineer-ii-aws-commerce-platform-adc) | amazon | US, VA, Herndon | 0.5510 | 2026-09-10 |
| [Construction Manager , Data Center Construction](https://www.amazon.jobs/en/jobs/10536782/construction-manager-data-center-construction) | amazon | US, OR, Boardman | 0.5417 | 2026-09-10 |
| [Construction Manager , Data Center Construction](https://www.amazon.jobs/en/jobs/10536765/construction-manager-data-center-construction) | amazon | US, OR, Boardman | 0.5417 | 2026-09-10 |
| [Construction Manager , Data Center Construction](https://www.amazon.jobs/en/jobs/10536789/construction-manager-data-center-construction) | amazon | US, OR, Boardman | 0.5417 | 2026-09-10 |
| [Construction Manager , Data Center Construction](https://www.amazon.jobs/en/jobs/10536795/construction-manager-data-center-construction) | amazon | US, OR, Boardman | 0.5417 | 2026-09-10 |
| [Construction Manager , Data Center Construction](https://www.amazon.jobs/en/jobs/10536762/construction-manager-data-center-construction) | amazon | US, OR, Boardman | 0.5417 | 2026-09-10 |
| [Construction Manager , Data Center Construction](https://www.amazon.jobs/en/jobs/10536778/construction-manager-data-center-construction) | amazon | US, OR, Boardman | 0.5417 | 2026-09-10 |
| [Construction Manager , Data Center Construction](https://www.amazon.jobs/en/jobs/10536773/construction-manager-data-center-construction) | amazon | US, OR, Boardman | 0.5417 | 2026-09-10 |
| [Solution Engineer - Cloud & AI Data Platform](https://apply.careers.microsoft.com/careers/job/1970393556958402) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5408 | 2026-09-11 |
| [Forward Deployed AI Integrator, Field Engineering](https://www.amazon.jobs/en/jobs/10537396/forward-deployed-ai-integrator-field-engineering) | amazon | US, VA, Herndon | 0.5407 | 2026-09-11 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10535922/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5400 | 2026-09-10 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10535928/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5397 | 2026-09-10 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10535936/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5397 | 2026-09-10 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10535941/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5396 | 2026-09-10 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10535947/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5396 | 2026-09-10 |
| [Manager of Construction, ADC - Data Center Construction](https://www.amazon.jobs/en/jobs/10536421/manager-of-construction-adc-data-center-construction) | amazon | US, VA, Culpeper | 0.5389 | 2026-09-10 |
| [Data Center Technician, DCO](https://www.amazon.jobs/en/jobs/10536951/data-center-technician-dco) | amazon | US, PA, Berwick | 0.5327 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537012/data-center-technician) | amazon | US, PA, Berwick | 0.5317 | 2026-09-11 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10537013/data-center-technician) | amazon | US, PA, Berwick | 0.5317 | 2026-09-11 |
| [Software Development Engineer II , Amazon Web Services (AWS) ](https://www.amazon.jobs/en/jobs/10536764/software-development-engineer-ii-amazon-web-services-aws) | amazon | US, WA, Seattle | 0.5265 | 2026-09-10 |
| [Software Development Manager, Leo Security](https://www.amazon.jobs/en/jobs/10537052/software-development-manager-leo-security) | amazon | US, VA, Arlington | 0.5251 | 2026-09-11 |
| [Machine Learning Engineer, Prime Video ML Platform](https://www.amazon.jobs/en/jobs/10535739/machine-learning-engineer-prime-video-ml-platform) | amazon | US, WA, Seattle | 0.5233 | 2026-09-10 |

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
