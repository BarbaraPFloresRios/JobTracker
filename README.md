[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Business Intelligence Engineer, PXT, AWS Region Services](https://www.amazon.jobs/en/jobs/10485179/business-intelligence-engineer-pxt-aws-region-services) | amazon | US, VA, Arlington | 0.5931 | 2026-07-27 |
| [Principal Risk Manager, Analytics and Insights](https://www.amazon.jobs/en/jobs/10485077/principal-risk-manager-analytics-and-insights) | amazon | US, NY, New York | 0.5907 | 2026-07-27 |
| [Data Scientist, GTM Intelligence](https://jobs.ashbyhq.com/openai/3b70ebc9-9d9a-4930-ad7b-52c9229f6a52) | openai | San Francisco | 0.5895 | 2026-07-27 |
| [Data Center Technician, CLT DCO](https://www.amazon.jobs/en/jobs/10484550/data-center-technician-clt-dco) | amazon | US, NC, Hamlet | 0.5710 | 2026-07-27 |
| [Business Intel Engineer III - AMZ10543876](https://www.amazon.jobs/en/jobs/10485012/business-intel-engineer-iii-amz10543876) | amazon | US, VA, Arlington | 0.5510 | 2026-07-27 |
| [Sr. Solutions Architect, Enterprise (Retail, Restaurant & CPG)](https://www.amazon.jobs/en/jobs/10484914/sr-solutions-architect-enterprise-retail-restaurant-cpg) | amazon | US, CA, San Francisco | 0.5384 | 2026-07-27 |
| [Principal Tech Business Development Manager, Devices Business Development, Tech Licensing Business Development ](https://www.amazon.jobs/en/jobs/10484087/principal-tech-business-development-manager-devices-business-development-tech-licensing-business-development) | amazon | US, WA, Seattle | 0.5231 | 2026-07-26 |
| [Applied AI Solutions Architect - Public Sector, Amazon Connect ](https://www.amazon.jobs/en/jobs/10484772/applied-ai-solutions-architect-public-sector-amazon-connect) | amazon | US, VA, Herndon | 0.5223 | 2026-07-27 |
| [Sr. Engineer, Silicon Validation , Annapurna Labs](https://www.amazon.jobs/en/jobs/10484162/sr-engineer-silicon-validation-annapurna-labs) | amazon | US, CA, Cupertino | 0.5118 | 2026-07-26 |
| [PMT III - External Svcs - AMZ9971264](https://www.amazon.jobs/en/jobs/10484718/pmt-iii-external-svcs-amz9971264) | amazon | US, WA, Seattle | 0.5106 | 2026-07-27 |
| [Tech Writer-Tech III - AMZ10061234](https://www.amazon.jobs/en/jobs/10484708/tech-writer-tech-iii-amz10061234) | amazon | US, WA, Seattle | 0.5083 | 2026-07-27 |
| [Software Engineer II (Customer & Product Engineering)](https://apply.careers.microsoft.com/careers/job/1970393556938231) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5073 | 2026-07-26 |
| [Software Developer Engineer, Amazon WorkSpaces Core Managed Instances](https://www.amazon.jobs/en/jobs/10484212/software-developer-engineer-amazon-workspaces-core-managed-instances) | amazon | US, WA, Seattle | 0.5054 | 2026-07-27 |
| [Software Developer Engineer, Amazon WorkSpaces Core Managed Instances](https://www.amazon.jobs/en/jobs/10484211/software-developer-engineer-amazon-workspaces-core-managed-instances) | amazon | US, WA, Seattle | 0.5054 | 2026-07-27 |
| [Customer Acquisition Manager, Startups](https://www.amazon.jobs/en/jobs/10485147/customer-acquisition-manager-startups) | amazon | US, TX, Austin | 0.4931 | 2026-07-27 |
| [Qualitative Researcher, Employee Listening](https://explore.jobs.netflix.net/careers/job/790317331866) | netflix | USA - Remote | 0.4925 | 2026-07-26 |
| [Critical Facility Technician , DCEO ](https://www.amazon.jobs/en/jobs/10484701/critical-facility-technician-dceo) | amazon | US, MD, Jessup | 0.4910 | 2026-07-27 |
| [Software Development Engineer III, AWS Core Networking – Network Fabric Engineering, Core Networking - Edge Capacity](https://www.amazon.jobs/en/jobs/10484901/software-development-engineer-iii-aws-core-networking-network-fabric-engineering-core-networking-edge-capacity) | amazon | US, CA, Santa Clara | 0.4836 | 2026-07-27 |
| [Clearable Engineering Operations Tech, AWS Cleared Jobs](https://www.amazon.jobs/en/jobs/10484163/clearable-engineering-operations-tech-aws-cleared-jobs) | amazon | US, VA, Fredericksburg | 0.4833 | 2026-07-26 |
| [Technology Experience Specialist - Studio (12 months FTC)](https://explore.jobs.netflix.net/careers/job/790317314729) | netflix | Amsterdam,Netherlands | 0.4783 | 2026-07-26 |
| [Account-Based Marketing Manager , NAMER Strategic Customer and Partner Marketing](https://www.amazon.jobs/en/jobs/10485111/account-based-marketing-manager-namer-strategic-customer-and-partner-marketing) | amazon | US, VA, Arlington | 0.4711 | 2026-07-27 |
| [Technical Program Manager II, Region Services / AWS Modular Data Center](https://www.amazon.jobs/en/jobs/10485194/technical-program-manager-ii-region-services-aws-modular-data-center) | amazon | US, VA, Arlington | 0.4697 | 2026-07-27 |
| [Sr. Technical Program Manager, Amazon Selection and Catalog Systems](https://www.amazon.jobs/en/jobs/10485135/sr-technical-program-manager-amazon-selection-and-catalog-systems) | amazon | US, WA, Seattle | 0.4658 | 2026-07-27 |
| [Business Transformation Manager, Process Excellence & Analytics, Global Corporate Procurement ](https://www.amazon.jobs/en/jobs/10484929/business-transformation-manager-process-excellence-analytics-global-corporate-procurement) | amazon | US, VA, Arlington | 0.4639 | 2026-07-27 |
| [Clearable Engineering Operations Technician , AWS Cleared Jobs](https://www.amazon.jobs/en/jobs/10484164/clearable-engineering-operations-technician-aws-cleared-jobs) | amazon | US, VA, Stafford | 0.4637 | 2026-07-26 |

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
