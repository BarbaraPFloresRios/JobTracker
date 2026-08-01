[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Engineer II, NAST CX Tech](https://www.amazon.jobs/en/jobs/10489805/data-engineer-ii-nast-cx-tech) | amazon | US, WA, Bellevue | 0.6097 | 2026-07-31 |
| [Data Scientist III - AMZ9976173](https://www.amazon.jobs/en/jobs/10488541/data-scientist-iii-amz9976173) | amazon | US, CA, Santa Clara | 0.5976 | 2026-07-31 |
| [Sr. GenAI/ML Specialist Solutions Architect, AGS Specialist Solutions Architects](https://www.amazon.jobs/en/jobs/10489300/sr-genai-ml-specialist-solutions-architect-ags-specialist-solutions-architects) | amazon | US, CA, San Francisco | 0.5957 | 2026-07-31 |
| [Data Scientist III - AMZ9976173](https://www.amazon.jobs/jobs/10488541/data-scientist-iii--amz?cmpid=bsp-amazon-science) | amazon_science | US, CA, Santa Clara | 0.5863 | 2026-07-31 |
| [Sr. Applied Scientist, PXT Central Science](https://www.amazon.jobs/jobs/10488615/sr-applied-scientist-pxt-central-science?cmpid=bsp-amazon-science) | amazon_science | US, CA, San Francisco | 0.5842 | 2026-07-31 |
| [Sr Customer Solutions Manager, Strategic Accounts](https://www.amazon.jobs/en/jobs/10489479/sr-customer-solutions-manager-strategic-accounts) | amazon | US, CA, Cupertino | 0.5764 | 2026-07-31 |
| [Data Engineer II - AMZ9956938](https://www.amazon.jobs/en/jobs/10488510/data-engineer-ii-amz9956938) | amazon | US, NY, New York | 0.5757 | 2026-07-31 |
| [Senior Go-to-Market Lead, NAMER Go-to-Market ](https://www.amazon.jobs/en/jobs/10489297/senior-go-to-market-lead-namer-go-to-market) | amazon | US, NY, New York | 0.5649 | 2026-07-31 |
| [Systems Engineer, Controls Fleet, Data Center Capacity Delivery](https://www.amazon.jobs/en/jobs/10489779/systems-engineer-controls-fleet-data-center-capacity-delivery) | amazon | US, WA, Seattle | 0.5570 | 2026-07-31 |
| [Sr. Partner Sales Manager, Enterprise](https://www.amazon.jobs/en/jobs/10489294/sr-partner-sales-manager-enterprise) | amazon | US, CO, Denver | 0.5467 | 2026-07-31 |
| [Program Manager II (ADBL197)](https://www.amazon.jobs/en/jobs/10489798/program-manager-ii-adbl197) | amazon | US, NJ, Newark | 0.5460 | 2026-07-31 |
| [Senior Data Scientist](https://apply.careers.microsoft.com/careers/job/1970393556938687) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5444 | 2026-08-01 |
| [Sr. Mechanical Design Engineer, Data Center Design Engineering](https://www.amazon.jobs/en/jobs/10489644/sr-mechanical-design-engineer-data-center-design-engineering) | amazon | US, VA, Herndon | 0.5410 | 2026-07-31 |
| [Sr Solution Engineer, Cloud & AI Infrastructure - CTJ - Top Secret](https://apply.careers.microsoft.com/careers/job/1970393556943774) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5405 | 2026-07-31 |
| [Senior Technical Program Manager (ADBL176)](https://www.amazon.jobs/en/jobs/10489626/senior-technical-program-manager-adbl176) | amazon | US, NJ, Newark | 0.5404 | 2026-07-31 |
| [Software Development Engineer III (ADBL189)](https://www.amazon.jobs/en/jobs/10489773/software-development-engineer-iii-adbl189) | amazon | US, NJ, Newark | 0.5403 | 2026-07-31 |
| [Software Development Engineer III (ADBL187)](https://www.amazon.jobs/en/jobs/10489752/software-development-engineer-iii-adbl187) | amazon | US, NJ, Newark | 0.5376 | 2026-07-31 |
| [Cloud Hardware Development Engineer, Cloud AI/ML/storage server teams](https://www.amazon.jobs/en/jobs/10489700/cloud-hardware-development-engineer-cloud-ai-ml-storage-server-teams) | amazon | US, CA, Cupertino | 0.5332 | 2026-07-31 |
| [Solutions Architect - AWS WWPS DOD, Joint DoD SA](https://www.amazon.jobs/en/jobs/10489793/solutions-architect-aws-wwps-dod-joint-dod-sa) | amazon | US, VA, Arlington | 0.5313 | 2026-07-31 |
| [Transportation Specialist Lead ](https://www.amazon.jobs/en/jobs/10489195/transportation-specialist-lead) | amazon | US, AZ, Tempe | 0.5224 | 2026-07-31 |
| [Applied Scientist, Alexa Connected Devices](https://www.amazon.jobs/jobs/10489844/applied-scientist-alexa-connected-devices?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5223 | 2026-08-01 |
| [Bid Intelligence & Automation Lead, Amazon Business - CPS](https://www.amazon.jobs/en/jobs/10489774/bid-intelligence-automation-lead-amazon-business-cps) | amazon | US, VA, Arlington | 0.5222 | 2026-07-31 |
| [Business Architect for Modernization & Sovereignty](https://apply.careers.microsoft.com/careers/job/1970393556950817) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5218 | 2026-07-31 |
| [Economist, Amazon Customer Service](https://www.amazon.jobs/jobs/10488853/economist-amazon-customer-service?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5207 | 2026-07-31 |
| [Project Engineer, Project Engineer](https://www.amazon.jobs/en/jobs/10489784/project-engineer-project-engineer) | amazon | US, LA, Shreveport | 0.5134 | 2026-07-31 |

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
