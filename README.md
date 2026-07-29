[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Data Scientist, Prime Video](https://www.amazon.jobs/en/jobs/10486917/data-scientist-prime-video) | amazon | US, WA, Seattle | 0.6385 | 2026-07-29 |
| [PD Methodology Engineer II, Annapurna Labs](https://www.amazon.jobs/en/jobs/10485401/pd-methodology-engineer-ii-annapurna-labs) | amazon | US, CA, Cupertino | 0.5962 | 2026-07-28 |
| [Sr. GenAI & ML Specialist Solutions Architect, ASPI Auto & Manufacturing](https://www.amazon.jobs/en/jobs/10486724/sr-genai-ml-specialist-solutions-architect-aspi-auto-manufacturing) | amazon | US, MI, Detroit | 0.5841 | 2026-07-28 |
| [Software Dev Engineer II - AMZ10243908](https://www.amazon.jobs/en/jobs/10486516/software-dev-engineer-ii-amz10243908) | amazon | US, CA, Santa Monica | 0.5808 | 2026-07-28 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556941428) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5741 | 2026-07-28 |
| [Senior Product Marketing Manager - Data Processing](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Product-Marketing-Manager---Data-Processing_JR2022150-1) | nvidia | US, CA, Santa Clara | 0.5639 | 2026-07-29 |
| [Sr. Go-to-Market Lead, AI Agent Platform](https://www.amazon.jobs/en/jobs/10485924/sr-go-to-market-lead-ai-agent-platform) | amazon | US, NY, New York | 0.5633 | 2026-07-28 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10487088/data-center-technician) | amazon | US, PA, Berwick | 0.5548 | 2026-07-29 |
| [Director, Go-To-Market Segment, Cloud & AI Platforms](https://apply.careers.microsoft.com/careers/job/1970393556926841) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5539 | 2026-07-29 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10487155/data-center-technician) | amazon | US, PA, Berwick | 0.5512 | 2026-07-29 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10487125/data-center-technician) | amazon | US, PA, Berwick | 0.5512 | 2026-07-29 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485594/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5510 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485589/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5510 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485598/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5510 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485595/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5510 | 2026-07-28 |
| [Pre-Construction Manager, AMER West Data Center Construction](https://www.amazon.jobs/en/jobs/10486503/pre-construction-manager-amer-west-data-center-construction) | amazon | US, TX, Dallas | 0.5509 | 2026-07-28 |
| [Data Center Technician, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10486124/data-center-technician-adc-infraops-dco) | amazon | US, TX, San Antonio | 0.5498 | 2026-07-28 |
| [SDE, MLA hardware/software co-design, Annapurna Labs Machine Learning Acceleration](https://www.amazon.jobs/en/jobs/10486046/sde-mla-hardware-software-co-design-annapurna-labs-machine-learning-acceleration) | amazon | US, TX, Austin | 0.5497 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485582/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5466 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485587/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5466 | 2026-07-28 |
| [Senior Software Engineer, Customer Data and Marketing AI](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-TX-Remote/Senior-Software-Engineer--Customer-Data-and-Marketing-AI_JR2022042) | nvidia | US, TX, Remote; US, CA, Remote; US, CA, Santa Clara | 0.5368 | 2026-07-28 |
| [Sr. Technical Program Manager, Leo CT Build](https://www.amazon.jobs/en/jobs/10487123/sr-technical-program-manager-leo-ct-build) | amazon | US, WA, Redmond | 0.5364 | 2026-07-29 |
| [Customer Solutions Manager, USAF](https://www.amazon.jobs/en/jobs/10486897/customer-solutions-manager-usaf) | amazon | US, VA, Arlington | 0.5362 | 2026-07-29 |
| [IT App Dev Engr II - AMZ27485.1](https://www.amazon.jobs/en/jobs/10486082/it-app-dev-engr-ii-amz27485-1) | amazon | US, TX, Austin | 0.5321 | 2026-07-28 |
| [Data Engineer, PV Prime Video TV - Tech](https://www.amazon.jobs/en/jobs/10486922/data-engineer-pv-prime-video-tv-tech) | amazon | US, WA, Seattle | 0.5294 | 2026-07-29 |

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
