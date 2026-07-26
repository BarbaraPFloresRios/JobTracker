[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist](https://apply.careers.microsoft.com/careers/job/1970393556941429) | microsoft | United States, Multiple Locations, Multiple Locations | 0.6335 | 2026-07-25 |
| [Principal Software Engineer - Architect](https://apply.careers.microsoft.com/careers/job/1970393556941614) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Washington, Redmond | 0.5817 | 2026-07-25 |
| [Cloud Solution Architect - Cloud & AI Platforms (CAIP) Factory](https://apply.careers.microsoft.com/careers/job/1970393556861682) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5421 | 2026-07-25 |
| [Applied Scientist, AWS Automated Reasoning](https://www.amazon.jobs/jobs/10484024/-applied-scientist-aws-automated-reasoning?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.5270 | 2026-07-25 |
| [Software Development Engineer - Silicon Development Infrastructure](https://www.amazon.jobs/en/jobs/10483953/software-development-engineer-silicon-development-infrastructure) | amazon | US, TX, Austin | 0.5178 | 2026-07-25 |
| [Sr Manager, Data Science & AI, R2L](https://www.amazon.jobs/jobs/10483501/sr-manager-data-science--ai-rl?cmpid=bsp-amazon-science) | amazon_science | US, WA, Bellevue | 0.5162 | 2026-07-25 |
| [Sr. Engineer, Silicon Validation , Annapurna Labs](https://www.amazon.jobs/en/jobs/10484162/sr-engineer-silicon-validation-annapurna-labs) | amazon | US, CA, Cupertino | 0.5118 | 2026-07-26 |
| [Principal Tech Business Development Manager, Devices Business Development, Tech Licensing Business Development ](https://www.amazon.jobs/en/jobs/10484087/principal-tech-business-development-manager-devices-business-development-tech-licensing-business-development) | amazon | US, WA, Seattle | 0.5098 | 2026-07-26 |
| [Software Engineer II (Customer & Product Engineering)](https://apply.careers.microsoft.com/careers/job/1970393556938231) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5073 | 2026-07-26 |
| [Senior Solution Area Specialist - Cloud & AI Platform](https://apply.careers.microsoft.com/careers/job/1970393556938805) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4960 | 2026-07-25 |
| [Senior Applied Scientist, PXT](https://www.amazon.jobs/jobs/10483516/senior-applied-scientist-pxt-?cmpid=bsp-amazon-science) | amazon_science | US, NY, New York | 0.4957 | 2026-07-25 |
| [Qualitative Researcher, Employee Listening](https://explore.jobs.netflix.net/careers/job/790317331866) | netflix | USA - Remote | 0.4939 | 2026-07-26 |
| [Principal Software Engineer - Full stack](https://apply.careers.microsoft.com/careers/job/1970393556941466) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Washington, Redmond | 0.4840 | 2026-07-25 |
| [Technology Experience Specialist - Studio (12 months FTC)](https://explore.jobs.netflix.net/careers/job/790317314729) | netflix | Amsterdam,Netherlands | 0.4775 | 2026-07-26 |
| [Applied Scientist, AWS Identity](https://www.amazon.jobs/jobs/10484023/applied-scientist-aws-identity?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.4739 | 2026-07-25 |
| [AI Business Process Digital Solution Area Specialist](https://apply.careers.microsoft.com/careers/job/1970393556941642) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Texas, Dallas; United States, North Dakota, Fargo; United States, Illinois, Chicago; United States, Texas, Houston; United States, Texas, Austin; United States, Colorado, Denver; United States, Arizona, Phoenix; United States, California, San Diego; United States, California, Los Angeles; United States, Washington, Seattle | 0.4670 | 2026-07-25 |
| [Senior Skilling Strategy Manager, Delivery & Program Operations](https://apply.careers.microsoft.com/careers/job/1970393556944434) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4659 | 2026-07-25 |
| [Clearable Engineering Operations Technician , AWS Cleared Jobs](https://www.amazon.jobs/en/jobs/10484164/clearable-engineering-operations-technician-aws-cleared-jobs) | amazon | US, VA, Stafford | 0.4595 | 2026-07-26 |
| [Head of Media, Amazon Gaming - Luna](https://www.amazon.jobs/en/jobs/10483948/head-of-media-amazon-gaming-luna) | amazon | US, CA, Culver City | 0.4586 | 2026-07-25 |
| [Applied Scientist, AWS Identity](https://www.amazon.jobs/en/jobs/10484023/applied-scientist-aws-identity) | amazon | US, VA, Arlington | 0.4480 | 2026-07-25 |
| [Data Visualization Engineer 5 - Member Insights Engineering](https://explore.jobs.netflix.net/careers/job/790317397849) | netflix | USA - Remote | 0.4473 | 2026-07-26 |
| [Clearable Engineering Operations Tech, AWS Cleared Jobs](https://www.amazon.jobs/en/jobs/10484163/clearable-engineering-operations-tech-aws-cleared-jobs) | amazon | US, VA, Fredericksburg | 0.4460 | 2026-07-26 |
| [ Applied Scientist, AWS Automated Reasoning](https://www.amazon.jobs/en/jobs/10484024/applied-scientist-aws-automated-reasoning) | amazon | US, VA, Arlington | 0.4410 | 2026-07-25 |
| [Windows Specialist Manager](https://apply.careers.microsoft.com/careers/job/1970393556943225) | microsoft | United States, Multiple Locations, Multiple Locations; United States, Multiple Locations, Multiple Locations | 0.4391 | 2026-07-25 |
| [Machine Learning Engineer, AI Safety](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Machine-Learning-Engineer--AI-Safety_JR2021784-1) | nvidia | US, CA, Santa Clara; US, CA, Remote | 0.4387 | 2026-07-25 |

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
