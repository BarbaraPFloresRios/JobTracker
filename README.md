[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Senior Data Engineer , Amazon Customer Service](https://www.amazon.jobs/en/jobs/10452121/senior-data-engineer-amazon-customer-service) | amazon | US, WA, Seattle | 0.6968 | 2026-06-17 |
| [Applied Scientist III- Recruiting AI Agents, Recruiting Agents & Candidate Voice](https://www.amazon.jobs/en/jobs/10451701/applied-scientist-iii-recruiting-ai-agents-recruiting-agents-candidate-voice) | amazon | US, WA, Seattle | 0.6793 | 2026-06-17 |
| [Applied Scientist, Amazon Customer Service](https://www.amazon.jobs/jobs/10450781/applied-scientist-amazon-customer-service?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5905 | 2026-06-17 |
| [Senior Solutions Architect, WWPS Global Defense Partners](https://www.amazon.jobs/en/jobs/10452685/senior-solutions-architect-wwps-global-defense-partners) | amazon | US, VA, Virtual Location - Virginia | 0.5879 | 2026-06-18 |
| [Senior Applied Scientist, Industrial Robotics Group](https://www.amazon.jobs/en/jobs/10452124/senior-applied-scientist-industrial-robotics-group) | amazon | US, WA, Seattle | 0.5865 | 2026-06-17 |
| [Solutions Architect, WWPS Global Defense Partners](https://www.amazon.jobs/en/jobs/10452684/solutions-architect-wwps-global-defense-partners) | amazon | US, CT, Virtual Location - Connecticut | 0.5862 | 2026-06-18 |
| [Sr. Region Planner, DC Planning - AMER](https://www.amazon.jobs/en/jobs/10452980/sr-region-planner-dc-planning-amer) | amazon | US, VA, Herndon | 0.5705 | 2026-06-18 |
| [Data Center Cluster Operations Leader, DCC Communities ](https://www.amazon.jobs/en/jobs/10451456/data-center-cluster-operations-leader-dcc-communities) | amazon | US, IN, Wheatfield | 0.5627 | 2026-06-17 |
| [Professional Services III - AMZ10515301](https://www.amazon.jobs/en/jobs/10452156/professional-services-iii-amz10515301) | amazon | US, TX, Irving | 0.5625 | 2026-06-17 |
| [Principal PMT, Prime Video Personalization & Discovery](https://www.amazon.jobs/en/jobs/10451505/principal-pmt-prime-video-personalization-discovery) | amazon | US, WA, Seattle | 0.5622 | 2026-06-17 |
| [Applied Scientist I, Sponsored Products and Brands Agent](https://www.amazon.jobs/en/jobs/10451121/applied-scientist-i-sponsored-products-and-brands-agent) | amazon | US, NY, New York | 0.5608 | 2026-06-17 |
| [Applied Scientist, TSI - Science](https://www.amazon.jobs/jobs/10450492/applied-scientist-tsi--science?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5537 | 2026-06-17 |
| [Sr. Principal Tech Lead, AWS Transform](https://www.amazon.jobs/en/jobs/10452405/sr-principal-tech-lead-aws-transform) | amazon | US, CA, Santa Clara | 0.5518 | 2026-06-18 |
| [Senior Research Scientist, Ad Measurements Science ](https://www.amazon.jobs/en/jobs/10452390/senior-research-scientist-ad-measurements-science) | amazon | US, NY, New York | 0.5514 | 2026-06-18 |
| [Solutions Architect, WWPS Global Defense Partners](https://www.amazon.jobs/en/jobs/10452682/solutions-architect-wwps-global-defense-partners) | amazon | US, VA, Arlington | 0.5478 | 2026-06-18 |
| [Senior UX Researcher, Applied AI Solution](https://www.amazon.jobs/en/jobs/10452074/senior-ux-researcher-applied-ai-solution) | amazon | US, VA, Herndon | 0.5470 | 2026-06-17 |
| [Program Manager, Amazon Selling Partner API](https://www.amazon.jobs/en/jobs/10451579/program-manager-amazon-selling-partner-api) | amazon | US, TX, Irving | 0.5435 | 2026-06-17 |
| [Senior Worldwide Partner Specialist Solutions Architect, Applied AI Partner Solutions Architecture](https://www.amazon.jobs/en/jobs/10451625/senior-worldwide-partner-specialist-solutions-architect-applied-ai-partner-solutions-architecture) | amazon | US, WA, Seattle | 0.5435 | 2026-06-17 |
| [Sr. Account Manager, Startups](https://www.amazon.jobs/en/jobs/10452715/sr-account-manager-startups) | amazon | US, NY, New York | 0.5421 | 2026-06-18 |
| [Staff Machine Learning Engineer - Applied AI](https://www.uber.com/global/en/careers/list/145860/) | uber | Sunnyvale, California, United States; San Francisco, California, United States; Seattle, Washington, United States | 0.5339 | 2026-06-17 |
| [Global Events Scale Manager, APN, AWS Partner Core Enablement Shared Services-Foundations](https://www.amazon.jobs/en/jobs/10451589/global-events-scale-manager-apn-aws-partner-core-enablement-shared-services-foundations) | amazon | US, WA, Seattle | 0.5338 | 2026-06-17 |
| [Software Development Engineer, Measurement, AdTech, and Data Science (MADS)](https://www.amazon.jobs/en/jobs/10451105/software-development-engineer-measurement-adtech-and-data-science-mads) | amazon | US, WA, Seattle | 0.5272 | 2026-06-17 |
| [Director, Sales Learning Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556875890) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5251 | 2026-06-17 |
| [Applied Scientist III- Recruiting AI Agents, Recruiting Agents & Candidate Voice](https://www.amazon.jobs/jobs/10451701/applied-scientist-iii-recruiting-ai-agents-recruiting-agents--candidate-voice?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5217 | 2026-06-18 |
| [Principal Product Management Manager](https://apply.careers.microsoft.com/careers/job/1970393556855306) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5169 | 2026-06-18 |

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
