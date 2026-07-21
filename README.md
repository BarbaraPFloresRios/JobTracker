[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Applied Scientist, GenAI Catalog Intelligence, PRISM](https://www.amazon.jobs/en/jobs/10480445/applied-scientist-genai-catalog-intelligence-prism) | amazon | US, CA, Sunnyvale | 0.6261 | 2026-07-21 |
| [Sr.  Applied Scientist, Amazon Customer Service](https://www.amazon.jobs/en/jobs/10480530/sr-applied-scientist-amazon-customer-service) | amazon | US, WA, Seattle | 0.6007 | 2026-07-21 |
| [Principal Account-Aligned FDE Data Science](https://apply.careers.microsoft.com/careers/job/1970393556940405) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5928 | 2026-07-21 |
| [Marketing Manager, Amazon Pickup Program , PARP Traffic ](https://www.amazon.jobs/en/jobs/10479240/marketing-manager-amazon-pickup-program-parp-traffic) | amazon | US, NY, New York | 0.5897 | 2026-07-20 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10478697/data-center-technician-dcc-communities) | amazon | US, IN, New Carlisle | 0.5823 | 2026-07-20 |
| [Sr. Storage Sales Specialist, Telco, Media, Entertainment, Games, Sports](https://www.amazon.jobs/en/jobs/10479257/sr-storage-sales-specialist-telco-media-entertainment-games-sports) | amazon | US, NY, New York | 0.5790 | 2026-07-20 |
| [Data Scientist, Security Issue Management](https://www.amazon.jobs/en/jobs/10478998/data-scientist-security-issue-management) | amazon | US, WA, Seattle | 0.5687 | 2026-07-20 |
| [Startup Growth PDM, Global Startup Team](https://www.amazon.jobs/en/jobs/10478726/startup-growth-pdm-global-startup-team) | amazon | US, NY, New York | 0.5606 | 2026-07-20 |
| [Principal Partner Enablement Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556939423) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5521 | 2026-07-21 |
| [Principal Games Industry Business Development Specialist, North America, Media & Entertainment, Games, Advertising and Sports Business Unit](https://www.amazon.jobs/en/jobs/10480640/principal-games-industry-business-development-specialist-north-america-media-entertainment-games-advertising-and-sports-business-unit) | amazon | US, CA, Santa Monica | 0.5456 | 2026-07-21 |
| [Sr. Manager, Hardware Development](https://www.amazon.jobs/en/jobs/10479095/sr-manager-hardware-development) | amazon | US, MA, N.reading | 0.5440 | 2026-07-20 |
| [Software Development Engineer, AWS Marketplace & Partner Services](https://www.amazon.jobs/en/jobs/10479999/software-development-engineer-aws-marketplace-partner-services) | amazon | US, WA, Seattle | 0.5353 | 2026-07-21 |
| [Construction Manager , AMER SE](https://www.amazon.jobs/en/jobs/10479460/construction-manager-amer-se) | amazon | US, VA, Chantilly | 0.5347 | 2026-07-21 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10479548/data-center-technician-dcc-communities) | amazon | US, GA, Covington | 0.5336 | 2026-07-21 |
| [Marketing Technology Program Manager, Global Channel Partner Sales](https://apply.careers.microsoft.com/careers/job/1970393556923404) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.5307 | 2026-07-21 |
| [Data Scientist II, AMZL, Central Learning Solutions Science](https://www.amazon.jobs/jobs/10479689/data-scientist-ii-amzl-central-learning-solutions-science?cmpid=bsp-amazon-science) | amazon_science | US, WA, Bellevue | 0.5282 | 2026-07-21 |
| [Delivery Consultant - AppDev AWS Professional Services, WWPS ProServe](https://www.amazon.jobs/en/jobs/10478671/delivery-consultant-appdev-aws-professional-services-wwps-proserve) | amazon | US, VA, Arlington | 0.5269 | 2026-07-20 |
| [Sr Solutions Architect, Amazon Web Services, AWS Federal Financials](https://www.amazon.jobs/en/jobs/10479214/sr-solutions-architect-amazon-web-services-aws-federal-financials) | amazon | US, VA, Arlington | 0.5257 | 2026-07-20 |
| [SAP MM & Logistics Architect, AWS SAP Team](https://www.amazon.jobs/en/jobs/10480042/sap-mm-logistics-architect-aws-sap-team) | amazon | US, WA, Seattle | 0.5252 | 2026-07-21 |
| [Infra Delivery Install Technician](https://www.amazon.jobs/en/jobs/10479252/infra-delivery-install-technician) | amazon | US, TX, Mansfield | 0.5217 | 2026-07-20 |
| [ID Storm Tech, ID Storm](https://www.amazon.jobs/en/jobs/10479639/id-storm-tech-id-storm) | amazon | US, VA, Herndon | 0.5206 | 2026-07-21 |
| [Sr. Account Manager-RRT, Startups](https://www.amazon.jobs/en/jobs/10479993/sr-account-manager-rrt-startups) | amazon | US, CA, San Francisco | 0.5196 | 2026-07-21 |
| [Sr. Account Manager-RRT, Startups](https://www.amazon.jobs/en/jobs/10479991/sr-account-manager-rrt-startups) | amazon | US, NY, New York | 0.5191 | 2026-07-21 |
| [Principal Execution Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556933153) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Illinois, Chicago; United States, Indiana, Indianapolis | 0.5178 | 2026-07-21 |
| [Account Manager-RRT, Startups](https://www.amazon.jobs/en/jobs/10479994/account-manager-rrt-startups) | amazon | US, CA, San Francisco | 0.5177 | 2026-07-21 |

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
