[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Sr Software Engineer/Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556929279) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.5884 | 2026-09-13 |
| [Member of Technical Staff - Data Flywheel Infra, Frontier Models](https://apply.careers.microsoft.com/careers/job/1970393556982519) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5149 | 2026-09-14 |
| [Software Engineer - FDE](https://apply.careers.microsoft.com/careers/job/1970393556939575) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5077 | 2026-09-13 |
| [GPU System Performance Architect](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-System-Performance-Architect_JR2025475) | nvidia | US, CA, Santa Clara; US, CO, Boulder; US, OR, Hillsboro | 0.5061 | 2026-09-14 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556992129) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4836 | 2026-09-13 |
| [Business Architect](https://apply.careers.microsoft.com/careers/job/1970393556957827) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4834 | 2026-09-13 |
| [Enterprise Architect, Americas Markets & Industries Office of the CTO](https://apply.careers.microsoft.com/careers/job/1970393556981728) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4801 | 2026-09-13 |
| [Software Engineering II and Senior Software Engineer (CoreAI - Post Training)](https://apply.careers.microsoft.com/careers/job/1970393556994428) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4735 | 2026-09-13 |
| [Sales Strategy Enablement Lead](https://apply.careers.microsoft.com/careers/job/1970393556957724) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4678 | 2026-09-13 |
| [Global GTM Business Architect - Microsoft Fabric](https://apply.careers.microsoft.com/careers/job/1970393556986874) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4676 | 2026-09-13 |
| [Senior Systems Software Engineer - Machine Learning](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Systems-Software-Engineer---Machine-Learning_JR2024968) | nvidia | US, CA, Santa Clara; US, NC, Durham | 0.4590 | 2026-09-13 |
| [General Program Manager (L5) - Developer Enablement](https://explore.jobs.netflix.net/careers/job/790317910029) | netflix | Warsaw,Poland | 0.4244 | 2026-09-13 |
| [Windows Specialist Manager](https://apply.careers.microsoft.com/careers/job/1970393556981109) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4231 | 2026-09-14 |
| [Senior Product Manager](https://apply.careers.microsoft.com/careers/job/1970393556958196) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4166 | 2026-09-13 |
| [Senior Software Engineer - Embedded Platform](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Software-Engineer---Embedded-Platform_JR2025588) | nvidia | US, CA, Santa Clara | 0.4145 | 2026-09-13 |
| [Software Engineer 5 - iOS](https://explore.jobs.netflix.net/careers/job/790318041034) | netflix | USA - Remote | 0.4005 | 2026-09-13 |
| [Services Account Manager](https://apply.careers.microsoft.com/careers/job/1970393556958197) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3932 | 2026-09-13 |
| [Senior Business Program Manager - Channel Programs Readiness](https://apply.careers.microsoft.com/careers/job/1970393556988040) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Washington, Redmond | 0.3927 | 2026-09-13 |
| [Software Engineer II](https://apply.careers.microsoft.com/careers/job/1970393556989680) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3790 | 2026-09-13 |
| [Sr. Creative Executive, MGM Alternative , MGM Alternative ](https://www.amazon.jobs/en/jobs/10538432/sr-creative-executive-mgm-alternative-mgm-alternative) | amazon | US, CA, Culver City | 0.3776 | 2026-09-14 |
| [Forward Deployed Engineer](https://job-boards.greenhouse.io/anthropic/jobs/5423029008) | anthropic | London, UK | 0.3749 | 2026-09-14 |
| [Regional Partner Commercial Leader - Industry Solutions Delivery (Americas)](https://apply.careers.microsoft.com/careers/job/1970393556982881) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3722 | 2026-09-13 |
| [Senior System Software Engineer, Software-Defined Networking](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Senior-System-Software-Engineer--Software-Defined-Networking_JR2025345-1) | nvidia | US, CA, Remote; US, NC, Remote; US, TX, Remote; US, CO, Remote; US, WA, Remote | 0.3721 | 2026-09-13 |
| [Manager, Ad Ops Solutions APAC](https://explore.jobs.netflix.net/careers/job/790318351030) | netflix | Singapore,Singapore | 0.3683 | 2026-09-13 |
| [Customer Success Account Manager (CSAM)](https://apply.careers.microsoft.com/careers/job/1970393556978550) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3683 | 2026-09-13 |

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
