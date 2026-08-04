[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Principal Product Marketing Manager](https://www.amazon.jobs/en/jobs/10491024/principal-product-marketing-manager) | amazon | US, WA, Bellevue | 0.6052 | 2026-08-04 |
| [Sr. Applied Scientist, Prime Video - Personalization and Discovery Science](https://www.amazon.jobs/en/jobs/10491282/sr-applied-scientist-prime-video-personalization-and-discovery-science) | amazon | US, CA, Sunnyvale | 0.5869 | 2026-08-04 |
| [Data Center Project Engineer, Data Center Construction](https://www.amazon.jobs/en/jobs/10492312/data-center-project-engineer-data-center-construction) | amazon | US, VA, Culpeper | 0.5795 | 2026-08-04 |
| [Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10491116/applied-scientist-fauna) | amazon | US, NY, New York | 0.5758 | 2026-08-04 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10490636/data-center-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5752 | 2026-08-04 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556949793) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5722 | 2026-08-04 |
| [Pr. Worldwide Partner Specialist - Global System Integrators, Data & AI GTM ](https://www.amazon.jobs/en/jobs/10492186/pr-worldwide-partner-specialist-global-system-integrators-data-ai-gtm) | amazon | US, WA, Seattle | 0.5704 | 2026-08-04 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10490974/data-center-technician) | amazon | US, PA, Berwick | 0.5646 | 2026-08-03 |
| [Data Center Supply Chain Manager, Data Center Supply Solutions](https://www.amazon.jobs/en/jobs/10490499/data-center-supply-chain-manager-data-center-supply-solutions) | amazon | US, VA, Herndon | 0.5645 | 2026-08-03 |
| [Business Analyst II ](https://www.amazon.jobs/en/jobs/10490982/business-analyst-ii) | amazon | US, WA, Seattle | 0.5643 | 2026-08-03 |
| [Data Center Logistics Specialist, DCC Communities](https://www.amazon.jobs/en/jobs/10490723/data-center-logistics-specialist-dcc-communities) | amazon | US, IN, New Carlisle | 0.5564 | 2026-08-03 |
| [Senior Storage AI Specialist Solution Architect , AGS Specialist Solutions Architecture Team](https://www.amazon.jobs/en/jobs/10490504/senior-storage-ai-specialist-solution-architect-ags-specialist-solutions-architecture-team) | amazon | US, VA, Herndon | 0.5552 | 2026-08-03 |
| [Principal S&OP Planner, Infrastructure Capacity & S&OP Planning](https://www.amazon.jobs/en/jobs/10492008/principal-s-op-planner-infrastructure-capacity-s-op-planning) | amazon | US, WA, Seattle | 0.5549 | 2026-08-04 |
| [Data Center Technician - Night Shift, DCC Communities ](https://www.amazon.jobs/en/jobs/10490626/data-center-technician-night-shift-dcc-communities) | amazon | US, IN, New Carlisle | 0.5548 | 2026-08-03 |
| [Data Center Technician - Night Shift, DCC Communities ](https://www.amazon.jobs/en/jobs/10490612/data-center-technician-night-shift-dcc-communities) | amazon | US, IN, New Carlisle | 0.5548 | 2026-08-03 |
| [Datacenter Engineering Telecom Engineer - AMER](https://apply.careers.microsoft.com/careers/job/1970393556950887) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5547 | 2026-08-04 |
| [Data Center Operations Manager  , ATL DCO](https://www.amazon.jobs/en/jobs/10491480/data-center-operations-manager-atl-dco) | amazon | US, GA, Hampton | 0.5537 | 2026-08-04 |
| [Software Development Engineer, AWS OpenSearch Service](https://www.amazon.jobs/en/jobs/10490514/software-development-engineer-aws-opensearch-service) | amazon | US, TX, Austin | 0.5479 | 2026-08-03 |
| [Senior Solutions Architect, AGS Software and Technology (SWAT) ](https://www.amazon.jobs/en/jobs/10491379/senior-solutions-architect-ags-software-and-technology-swat) | amazon | US, NY, New York | 0.5470 | 2026-08-04 |
| [Engineering Operations Technician, DCC Communities](https://www.amazon.jobs/en/jobs/10490683/engineering-operations-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5448 | 2026-08-04 |
| [Data Center Technician, CLT DCO](https://www.amazon.jobs/en/jobs/10490999/data-center-technician-clt-dco) | amazon | US, NC, Hamlet | 0.5420 | 2026-08-03 |
| [DCO Tech, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10491717/dco-tech-adc-infraops-dco) | amazon | US, CO, Aurora | 0.5399 | 2026-08-04 |
| [Software Development Engineer, Conversational Ads Experience](https://www.amazon.jobs/en/jobs/10490604/software-development-engineer-conversational-ads-experience) | amazon | US, NY, New York | 0.5345 | 2026-08-03 |
| [Sr. Mechanical Design Engineer, Data Center Design Engineering](https://www.amazon.jobs/en/jobs/10490813/sr-mechanical-design-engineer-data-center-design-engineering) | amazon | US, VA, Herndon | 0.5334 | 2026-08-03 |
| [Network Deployment Engineer, Amazon Dedicated Cloud (NIDD)](https://www.amazon.jobs/en/jobs/10490620/network-deployment-engineer-amazon-dedicated-cloud-nidd) | amazon | US, VA, Culpeper | 0.5317 | 2026-08-03 |

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

JobTracker automatically collects openings directly from company career pages, maintains historical records of job postings, and ranks opportunities using semantic similarity against a configurable candidate profile.

## Current Features

* Scrape job postings directly from company career pages
* Support multiple companies
* Detect newly discovered openings
* Track historical job data over time
* Run automatically using GitHub Actions
* Store structured datasets as CSV files
* Export recent jobs from today and yesterday
* Semantic job matching using sentence embeddings
* Configurable candidate profile for personalized ranking
* Cosine similarity scoring between jobs and candidate profile

## Status

Active personal project focused on job discovery, semantic search, and recommendation workflows.
