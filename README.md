[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Cloud Technical Account Manager, ES - Strategic Industries, ES - Strategic Industries](https://www.amazon.jobs/en/jobs/10568551/cloud-technical-account-manager-es-strategic-industries-es-strategic-industries) | amazon | US, NJ, Jersey City | 0.5885 | 2026-10-05 |
| [Account Manager - AI Natives](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Account-Manager---AI-Natives_JR2026699) | nvidia | US, CA, Santa Clara | 0.4914 | 2026-10-05 |
| [Work Based Learning Program Infrastructure Delivery Technician ](https://www.amazon.jobs/en/jobs/10568527/work-based-learning-program-infrastructure-delivery-technician) | amazon | US, MS, Canton | 0.4511 | 2026-10-05 |
| [Transportation Area Manager](https://www.amazon.jobs/en/jobs/10568499/transportation-area-manager) | amazon | US, IL, Rockford | 0.4484 | 2026-10-04 |
| [Machine Learning Engineer (Technical Leadership)](https://www.metacareers.com/profile/job_details/1619290696213069) | meta | Singapore | 0.4236 | 2026-10-05 |
| [Manager, Field Application Engineering - OEM Support](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-NC-Durham/Manager--Field-Application-Engineering---OEM-Support_JR2026481) | nvidia | US, NC, Durham | 0.4095 | 2026-10-05 |
| [Global Ad Sales Learning Enablement Manager](https://explore.jobs.netflix.net/careers/job/790318598901) | netflix | New York,New York,United States of America | 0.4070 | 2026-10-04 |
| [SDS Manager, NALA Sales Development](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-NC-Remote/SDS-Manager--NALA-Sales-Development_JR2026937) | nvidia | US, NC, Remote; US, CA, Remote | 0.3823 | 2026-10-05 |
| [Enterprise Account Executive - Healthcare & Life Science](https://job-boards.greenhouse.io/anthropic/jobs/5432590008) | anthropic | Seoul, South Korea | 0.3528 | 2026-10-05 |
| [Group Product Manager, Plans Innovation](https://explore.jobs.netflix.net/careers/job/790318601563) | netflix | Los Gatos,California,United States of America | 0.3134 | 2026-10-04 |
| [Senior Scale-Up Network System Architect](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Scale-Up-Network-System-Architect_JR2026652) | nvidia | US, CA, Santa Clara | 0.3105 | 2026-10-05 |
| [Account Manager (Spain) - Temporary Coverage](https://explore.jobs.netflix.net/careers/job/790318676145) | netflix | Madrid,Spain | 0.2866 | 2026-10-04 |
| [Account Manager (France)](https://explore.jobs.netflix.net/careers/job/790318752901) | netflix | Paris,France | 0.2860 | 2026-10-04 |
| [Enterprise Account Executive - Manufacturing](https://job-boards.greenhouse.io/anthropic/jobs/5443281008) | anthropic | Seoul, South Korea | 0.2797 | 2026-10-05 |
| [Market Planning & Operations Manager (EMEA - Sales Operations)](https://explore.jobs.netflix.net/careers/job/790318500566) | netflix | London,United Kingdom | 0.2678 | 2026-10-04 |
| [Security Engineer - Applied AI](https://www.metacareers.com/profile/job_details/1383588067176943) | meta | Menlo Park, CA | 0.2670 | 2026-10-05 |
| [Manager, Technical SEO Programs - Cupertino](https://jobs.apple.com/en-us/details/200687148-0836/manager-technical-seo-programs-cupertino?team=CORSV) | apple | nan | 0.2527 | 2026-10-04 |
| [Account Manager, Mid-Market (Hong Kong and Taiwan), SMB Group](https://www.metacareers.com/profile/job_details/837356059343551) | meta | Singapore | 0.2517 | 2026-10-05 |
| [DPU Networking Architect, Infrastructure Silicon](https://www.metacareers.com/profile/job_details/966396852519991) | meta | Sunnyvale, CA | 0.2494 | 2026-10-05 |
| [DPU IO Architect, Infrastructure Silicon](https://www.metacareers.com/profile/job_details/1469752631642156) | meta | Sunnyvale, CA | 0.2468 | 2026-10-05 |
| [Manager, Production Finance - Indonesia](https://explore.jobs.netflix.net/careers/job/790318751113) | netflix | Jakarta,Indonesia | 0.2421 | 2026-10-04 |
| [DPU Power Architect, Infrastructure Silicon](https://www.metacareers.com/profile/job_details/4384466011807153) | meta | Sunnyvale, CA | 0.2288 | 2026-10-05 |
| [Manager, Photo & Audio Visual Studio - Japan](https://explore.jobs.netflix.net/careers/job/790318500438) | netflix | Tokyo,Japan | 0.2105 | 2026-10-04 |
| [Content SEO Program Manager - Cupertino](https://jobs.apple.com/en-us/details/200687147-0836/content-seo-program-manager-cupertino?team=CORSV) | apple | nan | 0.2031 | 2026-10-04 |
| [Head of Cinematography, Lighting](https://explore.jobs.netflix.net/careers/job/790318686994) | netflix | Vancouver,Canada | 0.1830 | 2026-10-04 |

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
