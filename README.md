[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Senior Data Scientist](https://apply.careers.microsoft.com/careers/job/1970393556938687) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5444 | 2026-08-01 |
| [Applied Scientist, Alexa Connected Devices](https://www.amazon.jobs/jobs/10489844/applied-scientist-alexa-connected-devices?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.5231 | 2026-08-01 |
| [Senior Data Scientist - LATAM Content](https://explore.jobs.netflix.net/careers/job/790317556026) | netflix | Mexico City,Mexico | 0.4932 | 2026-08-02 |
| [Industrial Compute](https://jobs.ashbyhq.com/openai/6d7ece77-bf25-4f5e-9a84-c5ce26e18c37) | openai | Remote - US | 0.4927 | 2026-08-01 |
| [Software Engineer 5 - Platform Data Products](https://explore.jobs.netflix.net/careers/job/790317589519) | netflix | USA - Remote | 0.4911 | 2026-08-01 |
| [Applied Scientist, Amazon Connect Talent](https://www.amazon.jobs/jobs/10489858/applied-scientist-amazon-connect-talent?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.4882 | 2026-08-01 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556938609) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4876 | 2026-08-01 |
| [Sr. PMT, DTD Capacity Planning, Amazon Leo](https://www.amazon.jobs/en/jobs/10489807/sr-pmt-dtd-capacity-planning-amazon-leo) | amazon | US, WA, Redmond | 0.4868 | 2026-08-01 |
| [Software Development Engineer II - Amazon MSK, Managed Streaming Kafka (MSK)](https://www.amazon.jobs/en/jobs/10489822/software-development-engineer-ii-amazon-msk-managed-streaming-kafka-msk) | amazon | US, WA, Seattle | 0.4777 | 2026-08-01 |
| [Senior Software Engineer, AIOps and Observability](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Software-Engineer--AIOps-and-Observability_JR2022104) | nvidia | US, CA, Santa Clara | 0.4753 | 2026-08-01 |
| [Analytics Engineer 5 - New Content Experiences DSE](https://explore.jobs.netflix.net/careers/job/790317597274) | netflix | USA - Remote | 0.4684 | 2026-08-01 |
| [Sr. Manager, Solutions Architecture, US Advertising and Marketing ](https://www.amazon.jobs/en/jobs/10489157/sr-manager-solutions-architecture-us-advertising-and-marketing) | amazon | US, NY, New York | 0.4676 | 2026-08-01 |
| [Senior Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556943150) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4527 | 2026-08-01 |
| [Construction Manager, Industrial Compute](https://jobs.ashbyhq.com/openai/60b4b0f0-c5f1-48af-ad9b-716f2b5ce040) | openai | San Francisco; Seattle; Remote - US | 0.4451 | 2026-08-01 |
| [Senior Engineering Manager - Agent Platform, AI Platform](https://explore.jobs.netflix.net/careers/job/790317607391) | netflix | USA - Remote | 0.4419 | 2026-08-02 |
| [Data Center Engineering Operations Technician ](https://www.amazon.jobs/en/jobs/10489912/data-center-engineering-operations-technician) | amazon | US, VA, Sterling | 0.4418 | 2026-08-02 |
| [Bus Hardware Engineering Manager, Amazon Leo](https://www.amazon.jobs/en/jobs/10489853/bus-hardware-engineering-manager-amazon-leo) | amazon | US, WA, Redmond | 0.4381 | 2026-08-01 |
| [Contract Manager, Alexa](https://www.amazon.jobs/en/jobs/10489827/contract-manager-alexa) | amazon | US, CA, Sunnyvale | 0.4344 | 2026-08-01 |
| [Avionics Manager, Spacecraft Mechanical](https://www.amazon.jobs/en/jobs/10489840/avionics-manager-spacecraft-mechanical) | amazon | US, WA, Redmond | 0.4341 | 2026-08-01 |
| [Global Supply Chain & Procurement Manager, AWS Infrastructure and Supply Chain - Energy Storage, AWS Infrastructure Supply Chain & Procurement](https://www.amazon.jobs/en/jobs/10489812/global-supply-chain-procurement-manager-aws-infrastructure-and-supply-chain-energy-storage-aws-infrastructure-supply-chain-procurement) | amazon | US, WA, Seattle | 0.4332 | 2026-08-01 |
| [AI Networking](https://apply.careers.microsoft.com/careers/job/1970393556629398) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4313 | 2026-08-01 |
| [Sr. Software Engineer - CTJ - Secret](https://apply.careers.microsoft.com/careers/job/1970393556942025) | microsoft | United States, Washington, Redmond; United States, Multiple Locations, Multiple Locations | 0.4305 | 2026-08-02 |
| [Commercial Executive](https://apply.careers.microsoft.com/careers/job/1970393556947594) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4186 | 2026-08-01 |
| [Senior Director, Operating Unit Partner Sales, Americas](https://apply.careers.microsoft.com/careers/job/1970393556953643) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4182 | 2026-08-01 |
| [Director of Business Programs](https://apply.careers.microsoft.com/careers/job/1970393556949557) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4175 | 2026-08-01 |

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
