[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Sr. Applied Scientist, Prime Video - Personalization and Discovery Science](https://www.amazon.jobs/en/jobs/10491282/sr-applied-scientist-prime-video-personalization-and-discovery-science) | amazon | US, CA, Sunnyvale | 0.5869 | 2026-08-04 |
| [Principal Product Marketing Manager](https://www.amazon.jobs/en/jobs/10491024/principal-product-marketing-manager) | amazon | US, WA, Bellevue | 0.5816 | 2026-08-04 |
| [Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10491116/applied-scientist-fauna) | amazon | US, NY, New York | 0.5758 | 2026-08-04 |
| [Data Center Supply Chain Manager, Data Center Supply Solutions](https://www.amazon.jobs/en/jobs/10490499/data-center-supply-chain-manager-data-center-supply-solutions) | amazon | US, VA, Herndon | 0.5642 | 2026-08-03 |
| [Business Analyst II ](https://www.amazon.jobs/en/jobs/10490982/business-analyst-ii) | amazon | US, WA, Seattle | 0.5616 | 2026-08-03 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10490636/data-center-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5597 | 2026-08-04 |
| [Data Center Logistics Specialist, DCC Communities](https://www.amazon.jobs/en/jobs/10490723/data-center-logistics-specialist-dcc-communities) | amazon | US, IN, New Carlisle | 0.5552 | 2026-08-03 |
| [Data Center Technician - Night Shift, DCC Communities ](https://www.amazon.jobs/en/jobs/10490612/data-center-technician-night-shift-dcc-communities) | amazon | US, IN, New Carlisle | 0.5545 | 2026-08-03 |
| [Data Center Technician - Night Shift, DCC Communities ](https://www.amazon.jobs/en/jobs/10490626/data-center-technician-night-shift-dcc-communities) | amazon | US, IN, New Carlisle | 0.5545 | 2026-08-03 |
| [Senior Storage AI Specialist Solution Architect , AGS Specialist Solutions Architecture Team](https://www.amazon.jobs/en/jobs/10490504/senior-storage-ai-specialist-solution-architect-ags-specialist-solutions-architecture-team) | amazon | US, VA, Herndon | 0.5510 | 2026-08-03 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10490974/data-center-technician) | amazon | US, PA, Berwick | 0.5504 | 2026-08-03 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556949793) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5441 | 2026-08-04 |
| [Software Development Engineer, Conversational Ads Experience](https://www.amazon.jobs/en/jobs/10490604/software-development-engineer-conversational-ads-experience) | amazon | US, NY, New York | 0.5363 | 2026-08-03 |
| [Software Development Engineer, AWS OpenSearch Service](https://www.amazon.jobs/en/jobs/10490514/software-development-engineer-aws-opensearch-service) | amazon | US, TX, Austin | 0.5361 | 2026-08-03 |
| [Sr. Mechanical Design Engineer, Data Center Design Engineering](https://www.amazon.jobs/en/jobs/10490813/sr-mechanical-design-engineer-data-center-design-engineering) | amazon | US, VA, Herndon | 0.5312 | 2026-08-03 |
| [Network Deployment Engineer, Amazon Dedicated Cloud (NIDD)](https://www.amazon.jobs/en/jobs/10490620/network-deployment-engineer-amazon-dedicated-cloud-nidd) | amazon | US, VA, Culpeper | 0.5252 | 2026-08-03 |
| [Network Deployment Engineer, Amazon Dedicated Cloud (NIDD)](https://www.amazon.jobs/en/jobs/10490600/network-deployment-engineer-amazon-dedicated-cloud-nidd) | amazon | US, VA, Culpeper | 0.5252 | 2026-08-03 |
| [Data Center Technician, CLT DCO](https://www.amazon.jobs/en/jobs/10490999/data-center-technician-clt-dco) | amazon | US, NC, Hamlet | 0.5193 | 2026-08-03 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10491112/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5101 | 2026-08-04 |
| [Mechanical Product Design Engineer, Data Center Eng, Mech Products and Services](https://www.amazon.jobs/en/jobs/10490980/mechanical-product-design-engineer-data-center-eng-mech-products-and-services) | amazon | US, VA, Herndon | 0.5080 | 2026-08-03 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556950788) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5049 | 2026-08-03 |
| [Electrical Design Engineer, Data Center Engineering ](https://www.amazon.jobs/en/jobs/10490799/electrical-design-engineer-data-center-engineering) | amazon | US, VA, Herndon | 0.5040 | 2026-08-03 |
| [Sr. Electrical Engineer, Data Center Engineering ](https://www.amazon.jobs/en/jobs/10490785/sr-electrical-engineer-data-center-engineering) | amazon | US, VA, Herndon | 0.5032 | 2026-08-03 |
| [PR Specialist, AI Optimism and Industries](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PR-Specialist--AI-Optimism-and-Industries_JR2022339) | nvidia | US, CA, Santa Clara | 0.5031 | 2026-08-03 |
| [Technical Business Development Manager – Infrastructure](https://jobs.ashbyhq.com/openai/c0cfe3a1-f5a5-40f9-8365-b14a213e4148) | openai | San Francisco | 0.5024 | 2026-08-03 |

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
