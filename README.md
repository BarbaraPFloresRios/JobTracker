[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist II - AMZ10564056](https://www.amazon.jobs/en/jobs/10574837/data-scientist-ii-amz10564056) | amazon | US, CA, Culver City | 0.6238 | 2026-10-09 |
| [BIE I - FBA Analytics, FBA Analytics](https://www.amazon.jobs/en/jobs/10573882/bie-i-fba-analytics-fba-analytics) | amazon | US, WA, Bellevue | 0.5803 | 2026-10-09 |
| [Data Scientist II - AMZ10564056](https://www.amazon.jobs/jobs/10574837/data-scientist-ii--amz?cmpid=bsp-amazon-science) | amazon_science | US, CA, Culver City | 0.5803 | 2026-10-10 |
| [Applied Scientist Manager, Marketplace Intelligence](https://www.amazon.jobs/en/jobs/10575244/applied-scientist-manager-marketplace-intelligence) | amazon | US, VA, Arlington | 0.5722 | 2026-10-10 |
| [Senior Agentic WorkSpaces Specialist, Applied AI Solutions](https://www.amazon.jobs/en/jobs/10574939/senior-agentic-workspaces-specialist-applied-ai-solutions) | amazon | US, NY, New York | 0.5534 | 2026-10-09 |
| [Applied Scientist Manager, Marketplace Intelligence](https://www.amazon.jobs/jobs/10575244/applied-scientist-manager-marketplace-intelligence?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.5528 | 2026-10-10 |
| [Data Engineer, Product](https://job-boards.greenhouse.io/anthropic/jobs/5448481008) | anthropic | San Francisco, CA | 0.5494 | 2026-10-09 |
| [Sr. Physical Design Engineer, Annapurna Labs](https://www.amazon.jobs/en/jobs/10574284/sr-physical-design-engineer-annapurna-labs) | amazon | US, CA, Cupertino | 0.5449 | 2026-10-09 |
| [Business Intelligence Engineer II, Amazon Leo, Amazon LEO](https://www.amazon.jobs/en/jobs/10574266/business-intelligence-engineer-ii-amazon-leo-amazon-leo) | amazon | US, WA, Redmond | 0.5391 | 2026-10-09 |
| [Engagement Manager, Professional Services, AWS Strategic Industries](https://www.amazon.jobs/en/jobs/10574133/engagement-manager-professional-services-aws-strategic-industries) | amazon | US, TX, Houston | 0.5380 | 2026-10-09 |
| [Solutions Architecture Manager, Software and Technology Solutions Architecture](https://www.amazon.jobs/en/jobs/10575306/solutions-architecture-manager-software-and-technology-solutions-architecture) | amazon | US, CA, San Francisco | 0.5356 | 2026-10-10 |
| [Project Engineer, Data Center Construction](https://www.amazon.jobs/en/jobs/10575079/project-engineer-data-center-construction) | amazon | US, OR, Boardman | 0.5331 | 2026-10-10 |
| [Support Engineer, High Touch Support](https://www.amazon.jobs/en/jobs/10575160/support-engineer-high-touch-support) | amazon | US, WA, Bellevue | 0.5324 | 2026-10-10 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10574995/data-center-technician) | amazon | US, OR, Hermiston | 0.5313 | 2026-10-09 |
| [Data Engineer, Accounting](https://www.amazon.jobs/en/jobs/10574968/data-engineer-accounting) | amazon | US, VA, Arlington | 0.5303 | 2026-10-09 |
| [SAP Consultant, Professional Services - SAP ](https://www.amazon.jobs/en/jobs/10574947/sap-consultant-professional-services-sap) | amazon | US, TX, Dallas | 0.5301 | 2026-10-09 |
| [Clearable Network Infrastructure Engineer I, Amazon Dedicated Cloud (NIDD)](https://www.amazon.jobs/en/jobs/10574750/clearable-network-infrastructure-engineer-i-amazon-dedicated-cloud-nidd) | amazon | US, CO, Broomfield | 0.5277 | 2026-10-09 |
| [Clearable Network Infrastructure Engineer I, Amazon Dedicated Cloud (NIDD)](https://www.amazon.jobs/en/jobs/10574751/clearable-network-infrastructure-engineer-i-amazon-dedicated-cloud-nidd) | amazon | US, CO, Broomfield | 0.5251 | 2026-10-09 |
| [Sr. Manufacturing Engineer - Process Quality, Hardware Engineering - Manufacturing](https://www.amazon.jobs/en/jobs/10574156/sr-manufacturing-engineer-process-quality-hardware-engineering-manufacturing) | amazon | US, KY, Florence | 0.5229 | 2026-10-09 |
| [Software Development Engineer, Agentic AI, Velocity Labs](https://www.amazon.jobs/en/jobs/10573921/software-development-engineer-agentic-ai-velocity-labs) | amazon | US, WA, Seattle | 0.5220 | 2026-10-09 |
| [Data Center Chief Engineer ](https://www.amazon.jobs/en/jobs/10574842/data-center-chief-engineer) | amazon | US, OH, Jeffersonville | 0.5215 | 2026-10-09 |
| [Product Designer, AWS Events Tech Team & Marketer Experience](https://www.amazon.jobs/en/jobs/10573830/product-designer-aws-events-tech-team-marketer-experience) | amazon | US, NY, New York | 0.5213 | 2026-10-09 |
| [Sr. Software Development Engineer, Agentic AI, Velocity Labs](https://www.amazon.jobs/en/jobs/10573900/sr-software-development-engineer-agentic-ai-velocity-labs) | amazon | US, WA, Seattle | 0.5141 | 2026-10-09 |
| [Network Cable Installation Technician, Infra - GND](https://www.amazon.jobs/en/jobs/10573955/network-cable-installation-technician-infra-gnd) | amazon | US, VA, Chantilly | 0.5129 | 2026-10-09 |
| [Software Development Manager, Agentic AI, Velocity Labs](https://www.amazon.jobs/en/jobs/10573926/software-development-manager-agentic-ai-velocity-labs) | amazon | US, WA, Seattle | 0.5097 | 2026-10-09 |

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
