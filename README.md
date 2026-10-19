[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Testing JSQs edits](https://www.amazon.jobs/en/jobs/10582189/testing-jsqs-edits) | amazon | US, WA, Bellevue | 0.5227 | 2026-10-18 |
| [Principal Threat Intelligence Analyst - CTJ - Top Secret](https://apply.careers.microsoft.com/careers/job/1970393557007277) | microsoft | United States, Virginia, Reston; United States, Multiple Locations, Multiple Locations | 0.5100 | 2026-10-18 |
| [Marketing Technology Operations Manager](https://apply.careers.microsoft.com/careers/job/1970393557024807) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5039 | 2026-10-19 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393557023190) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4770 | 2026-10-19 |
| [Business Program Manager, Culture & Transformation](https://apply.careers.microsoft.com/careers/job/1970393557026746) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4745 | 2026-10-19 |
| [Commissioning Technical Director - Americas](https://apply.careers.microsoft.com/careers/job/1970393557027327) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4660 | 2026-10-19 |
| [Sales Excellence Lead, Cloud and AI Platform](https://apply.careers.microsoft.com/careers/job/1970393557039176) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4553 | 2026-10-18 |
| [Senior Cloud Solution Architect - Cloud & AI Infrastructure, Azure Government Cloud](https://apply.careers.microsoft.com/careers/job/1970393557040543) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4505 | 2026-10-19 |
| [Senior Cloud Software Engineer](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Cloud-Software-Engineer_JR2027863) | nvidia | US, CA, Santa Clara; US, Remote; US, WA, Seattle | 0.4460 | 2026-10-19 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393557025706) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4414 | 2026-10-18 |
| [Cloud Hosting Finance Analyst](https://jobs.smartrecruiters.com/Canva/6000000001501262-cloud-hosting-finance-analyst) | canva | San Francisco, CA, United States | 0.4304 | 2026-10-19 |
| [Applied AI Engineer, Startups (Mandarin-speaking)](https://jobs.ashbyhq.com/openai/502fcf97-75b2-4e54-9957-a29cee8eb1ca) | openai | Singapore | 0.4291 | 2026-10-19 |
| [Senior Forward Deployed Engineer, Open Models](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Forward-Deployed-Engineer--Open-Models_JR2028008) | nvidia | US, CA, Santa Clara | 0.4276 | 2026-10-19 |
| [Customer Success Manager](https://job-boards.greenhouse.io/anthropic/jobs/5456491008) | anthropic | Tokyo, Japan | 0.4128 | 2026-10-19 |
| [Principal Engineer Capacity/Compute](https://job-boards.greenhouse.io/anthropic/jobs/5456405008) | anthropic | San Francisco, CA | 0.4047 | 2026-10-19 |
| [Principal Engineer Capacity/Compute](https://job-boards.greenhouse.io/anthropic/jobs/5456406008) | anthropic | San Francisco, CA | 0.4047 | 2026-10-19 |
| [Principal Engineer Capacity/Compute](https://job-boards.greenhouse.io/anthropic/jobs/5456039008) | anthropic | San Francisco, CA | 0.4047 | 2026-10-18 |
| [Senior Performance Creative](https://jobs.smartrecruiters.com/Canva/6000000001497054-senior-performance-creative) | canva | San Francisco, CA, United States | 0.4013 | 2026-10-19 |
| [Mobile User Acquisition Manager, Amazon Music](https://www.amazon.jobs/en/jobs/10582083/mobile-user-acquisition-manager-amazon-music) | amazon | US, CA, Culver City | 0.3846 | 2026-10-18 |
| [Community Engagement Manager, Data Centers (Indiana & Kentucky)](https://job-boards.greenhouse.io/anthropic/jobs/5454535008) | anthropic | Remote-Friendly US (Travel Required) | 0.3739 | 2026-10-18 |
| [Director of Sales Strategy Enablement](https://apply.careers.microsoft.com/careers/job/1970393557007602) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3603 | 2026-10-19 |
| [Process Assistant, CMH5](https://www.amazon.jobs/en/jobs/10582202/process-assistant-cmh5) | amazon | US, OH, West Jefferson | 0.3530 | 2026-10-19 |
| [Partner Technology Strategist](https://apply.careers.microsoft.com/careers/job/1970393557018950) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3452 | 2026-10-19 |
| [Lead Associate](https://www.amazon.jobs/en/jobs/10582432/lead-associate) | amazon | US, LA, New Orleans | 0.3414 | 2026-10-19 |
| [Business Architect for Security Usage Strategy](https://apply.careers.microsoft.com/careers/job/1970393557021834) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3409 | 2026-10-18 |

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
