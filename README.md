[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Marketing Manager, Amazon Pickup Program , PARP Traffic ](https://www.amazon.jobs/en/jobs/10479240/marketing-manager-amazon-pickup-program-parp-traffic) | amazon | US, NY, New York | 0.5897 | 2026-07-20 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10478697/data-center-technician-dcc-communities) | amazon | US, IN, New Carlisle | 0.5823 | 2026-07-20 |
| [Data Scientist, Security Issue Management](https://www.amazon.jobs/en/jobs/10478998/data-scientist-security-issue-management) | amazon | US, WA, Seattle | 0.5700 | 2026-07-20 |
| [Sr. Storage Sales Specialist, Telco, Media, Entertainment, Games, Sports](https://www.amazon.jobs/en/jobs/10479257/sr-storage-sales-specialist-telco-media-entertainment-games-sports) | amazon | US, NY, New York | 0.5609 | 2026-07-20 |
| [Principal Account-Aligned FDE Data Science](https://apply.careers.microsoft.com/careers/job/1970393556940405) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5585 | 2026-07-21 |
| [Startup Growth PDM, Global Startup Team](https://www.amazon.jobs/en/jobs/10478726/startup-growth-pdm-global-startup-team) | amazon | US, NY, New York | 0.5547 | 2026-07-20 |
| [Principal Partner Enablement Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556939423) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5521 | 2026-07-21 |
| [Research Lead, AWS Economic Development](https://www.amazon.jobs/en/jobs/10478999/research-lead-aws-economic-development) | amazon | US, VA, Arlington | 0.5369 | 2026-07-20 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10479548/data-center-technician-dcc-communities) | amazon | US, GA, Covington | 0.5336 | 2026-07-21 |
| [Construction Manager , AMER SE](https://www.amazon.jobs/en/jobs/10479460/construction-manager-amer-se) | amazon | US, VA, Chantilly | 0.5329 | 2026-07-21 |
| [Sr. Manager, Hardware Development](https://www.amazon.jobs/en/jobs/10479095/sr-manager-hardware-development) | amazon | US, MA, N.reading | 0.5319 | 2026-07-20 |
| [Data Scientist II, AMZL, Central Learning Solutions Science](https://www.amazon.jobs/jobs/10479689/data-scientist-ii-amzl-central-learning-solutions-science?cmpid=bsp-amazon-science) | amazon_science | US, WA, Bellevue | 0.5282 | 2026-07-21 |
| [ID Storm Tech, ID Storm](https://www.amazon.jobs/en/jobs/10479639/id-storm-tech-id-storm) | amazon | US, VA, Herndon | 0.5206 | 2026-07-21 |
| [Sr. Data Scientist, OTS - Data ANCHOR Team](https://www.amazon.jobs/jobs/10478504/sr-data-scientist-ots--data-anchor-team?cmpid=bsp-amazon-science) | amazon_science | US, TX, Austin | 0.5201 | 2026-07-21 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10479252/infra-delivery-install-technician) | amazon | US, TX, Mansfield | 0.5174 | 2026-07-20 |
| [Principal Account-Aligned FDE TPM](https://apply.careers.microsoft.com/careers/job/1970393556940399) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5166 | 2026-07-20 |
| [Delivery Consultant - AppDev AWS Professional Services, WWPS ProServe](https://www.amazon.jobs/en/jobs/10478671/delivery-consultant-appdev-aws-professional-services-wwps-proserve) | amazon | US, VA, Arlington | 0.5159 | 2026-07-20 |
| [Associate Solutions Architect, National Security Solutions Architecture Team](https://www.amazon.jobs/en/jobs/10478571/associate-solutions-architect-national-security-solutions-architecture-team) | amazon | US, VA, Herndon | 0.5155 | 2026-07-20 |
| [Software Development Engineer, Network Product Development](https://www.amazon.jobs/en/jobs/10479116/software-development-engineer-network-product-development) | amazon | US, CA, Cupertino | 0.5145 | 2026-07-20 |
| [Senior Applied Scientist, Selling Partner Selection Success](https://www.amazon.jobs/jobs/10479599/senior-applied-scientist-selling-partner-selection-success?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5093 | 2026-07-21 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10479557/data-center-technician-dcc-communities) | amazon | US, GA, Covington | 0.5074 | 2026-07-21 |
| [Engineering Operations Technician , DCEO](https://www.amazon.jobs/en/jobs/10478827/engineering-operations-technician-dceo) | amazon | US, GA, Atlanta | 0.5018 | 2026-07-20 |
| [Engineering Manager, AI Developer Technology](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Engineering-Manager--AI-Developer-Technology_JR1995883) | nvidia | US, CA, Santa Clara; US, MA, Westford; US, TX, Austin; US, OR, Hillsboro; US, NC, Durham | 0.4969 | 2026-07-21 |
| [Manager, Strategic Sourcing , Silicon Operations](https://www.amazon.jobs/en/jobs/10479701/manager-strategic-sourcing-silicon-operations) | amazon | US, CA, Sunnyvale | 0.4969 | 2026-07-21 |
| [Sr Solutions Architect, Amazon Web Services, AWS Federal Financials](https://www.amazon.jobs/en/jobs/10479214/sr-solutions-architect-amazon-web-services-aws-federal-financials) | amazon | US, VA, Arlington | 0.4914 | 2026-07-20 |

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
