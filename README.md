[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Applied Science II, Edge Technology](https://www.amazon.jobs/en/jobs/10480876/applied-science-ii-edge-technology) | amazon | US, CA, Sunnyvale | 0.6848 | 2026-07-22 |
| [Applied Scientist II, Data Intelligence and Governance](https://www.amazon.jobs/en/jobs/10480925/applied-scientist-ii-data-intelligence-and-governance) | amazon | US, CA, Sunnyvale | 0.6401 | 2026-07-22 |
| [Applied Science II, Edge Technology](https://www.amazon.jobs/jobs/10480876/applied-science-ii-edge-technology?cmpid=bsp-amazon-science) | amazon_science | US, CA, Sunnyvale | 0.6228 | 2026-07-22 |
| [Sr Business Intelligence Engineer III, Community Operations](https://www.amazon.jobs/en/jobs/10481672/sr-business-intelligence-engineer-iii-community-operations) | amazon | US, WA, Bellevue | 0.6093 | 2026-07-22 |
| [Principal Software Engineer - (Vector Search/Information Retrieval)](https://apply.careers.microsoft.com/careers/job/1970393556940586) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5980 | 2026-07-23 |
| [EFA Network Software Engineer I, Annapurna Labs](https://www.amazon.jobs/en/jobs/10481932/efa-network-software-engineer-i-annapurna-labs) | amazon | US, WA, Seattle | 0.5934 | 2026-07-22 |
| [Sr. Product Marketing Manager, Amazon Supply Chain Services Marketing](https://www.amazon.jobs/en/jobs/10481168/sr-product-marketing-manager-amazon-supply-chain-services-marketing) | amazon | US, NY, New York | 0.5921 | 2026-07-22 |
| [Applied Scientist , Amazon Customer Service](https://www.amazon.jobs/jobs/10480526/applied-scientist--amazon-customer-service?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5867 | 2026-07-22 |
| [Facility Manager, Infraops AG](https://www.amazon.jobs/en/jobs/10481546/facility-manager-infraops-ag) | amazon | US, VA, Warrenton | 0.5750 | 2026-07-22 |
| [Senior Technical Program Manager](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Senior-Technical-Program-Manager_JR2021406) | nvidia | US, CA, Remote; US, GA, Remote; US, NC, Remote; US, TX, Remote; US, NY, Remote; US, FL, Remote | 0.5719 | 2026-07-22 |
| [Sr. Solutions Architect, Software and Technology](https://www.amazon.jobs/en/jobs/10482090/sr-solutions-architect-software-and-technology) | amazon | US, CA, San Francisco | 0.5717 | 2026-07-23 |
| [Sr. Applied Scientist - Perception (SLAM/VIO), Fauna](https://www.amazon.jobs/en/jobs/10481505/sr-applied-scientist-perception-slam-vio-fauna) | amazon | US, NY, New York | 0.5694 | 2026-07-22 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556941613) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5668 | 2026-07-23 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556941920) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5668 | 2026-07-23 |
| [Applied Scientist, Sponsored Products and Brands](https://www.amazon.jobs/en/jobs/10482056/applied-scientist-sponsored-products-and-brands) | amazon | US, CA, Palo Alto | 0.5643 | 2026-07-23 |
| [Software Development Engineer](https://www.amazon.jobs/en/jobs/10481902/software-development-engineer) | amazon | US, WA, Seattle | 0.5521 | 2026-07-22 |
| [Automation Mechanical Engineer, Manufacturing Automation Design & Engineering](https://www.amazon.jobs/en/jobs/10482003/automation-mechanical-engineer-manufacturing-automation-design-engineering) | amazon | US, TX, Austin | 0.5510 | 2026-07-23 |
| [Principal Solution Engineer - Software Development & Platform](https://apply.careers.microsoft.com/careers/job/1970393556938175) | microsoft | United States, Texas, Dallas; United States, Georgia, Atlanta; United States, North Dakota, Fargo; United States, North Carolina, Charlotte; United States, Multiple Locations, Multiple Locations | 0.5470 | 2026-07-22 |
| [AI Principal Product Manager-Tech, Amazon Customer Service](https://www.amazon.jobs/en/jobs/10482051/ai-principal-product-manager-tech-amazon-customer-service) | amazon | US, WA, Seattle | 0.5469 | 2026-07-23 |
| [Construction Manager, Data Center Construction](https://www.amazon.jobs/en/jobs/10481842/construction-manager-data-center-construction) | amazon | US, IN, New Carlisle | 0.5422 | 2026-07-22 |
| [Applied Scientist, AWS Automated Reasoning](https://www.amazon.jobs/jobs/10480215/applied-scientist-aws-automated-reasoning?cmpid=bsp-amazon-science) | amazon_science | US, TX, Austin | 0.5358 | 2026-07-22 |
| [Data Center Technician , DCC Communities ](https://www.amazon.jobs/en/jobs/10480979/data-center-technician-dcc-communities) | amazon | US, GA, Covington | 0.5339 | 2026-07-22 |
| [Technical Infrastructure Program Manager - Long Haul, Fiber Deployment, GCID](https://www.amazon.jobs/en/jobs/10481286/technical-infrastructure-program-manager-long-haul-fiber-deployment-gcid) | amazon | US, CO, Denver | 0.5313 | 2026-07-22 |
| [Data Scientist II - AMZ27596.1](https://www.amazon.jobs/jobs/10474326/data-scientist-ii--amz?cmpid=bsp-amazon-science) | amazon_science | US, TX, Irving | 0.5309 | 2026-07-22 |
| [Solution Architect, AGS Automotive & Manufacturing](https://www.amazon.jobs/en/jobs/10482339/solution-architect-ags-automotive-manufacturing) | amazon | US, CO, Denver | 0.5238 | 2026-07-23 |

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
