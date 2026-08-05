[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Principal Product Marketing Manager](https://www.amazon.jobs/en/jobs/10491024/principal-product-marketing-manager) | amazon | US, WA, Bellevue | 0.6043 | 2026-08-04 |
| [Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10491116/applied-scientist-fauna) | amazon | US, NY, New York | 0.6036 | 2026-08-04 |
| [Head of Developer Enablement, Kiro](https://www.amazon.jobs/en/jobs/10492319/head-of-developer-enablement-kiro) | amazon | US, NY, New York | 0.5952 | 2026-08-05 |
| [Sr. Applied Scientist, Prime Video - Personalization and Discovery Science](https://www.amazon.jobs/en/jobs/10491282/sr-applied-scientist-prime-video-personalization-and-discovery-science) | amazon | US, CA, Sunnyvale | 0.5869 | 2026-08-04 |
| [Data Center Project Engineer, Data Center Construction](https://www.amazon.jobs/en/jobs/10492312/data-center-project-engineer-data-center-construction) | amazon | US, VA, Culpeper | 0.5795 | 2026-08-04 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10490636/data-center-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5749 | 2026-08-04 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556949793) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5737 | 2026-08-04 |
| [Pr. Worldwide Partner Specialist - Global System Integrators, Data & AI GTM ](https://www.amazon.jobs/en/jobs/10492186/pr-worldwide-partner-specialist-global-system-integrators-data-ai-gtm) | amazon | US, WA, Seattle | 0.5704 | 2026-08-04 |
| [Datacenter Engineering Telecom Engineer - AMER](https://apply.careers.microsoft.com/careers/job/1970393556950887) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5558 | 2026-08-04 |
| [Principal S&OP Planner, Infrastructure Capacity & S&OP Planning](https://www.amazon.jobs/en/jobs/10492008/principal-s-op-planner-infrastructure-capacity-s-op-planning) | amazon | US, WA, Seattle | 0.5549 | 2026-08-04 |
| [Senior Solutions Architect, AGS Software and Technology (SWAT) ](https://www.amazon.jobs/en/jobs/10491379/senior-solutions-architect-ags-software-and-technology-swat) | amazon | US, NY, New York | 0.5483 | 2026-08-04 |
| [Data Center Operations Manager  , ATL DCO](https://www.amazon.jobs/en/jobs/10491480/data-center-operations-manager-atl-dco) | amazon | US, GA, Hampton | 0.5468 | 2026-08-04 |
| [Engineering Operations Technician, DCC Communities](https://www.amazon.jobs/en/jobs/10490683/engineering-operations-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5444 | 2026-08-04 |
| [DCO Tech, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10491717/dco-tech-adc-infraops-dco) | amazon | US, CO, Aurora | 0.5399 | 2026-08-04 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10491713/data-center-technician-dcc-communities) | amazon | US, GA, Covington | 0.5239 | 2026-08-04 |
| [Senior Delivery Consultant - Cloud Infrastructure Architect AWS Professional Services, WWPS US Education and State & Local Government](https://www.amazon.jobs/en/jobs/10491520/senior-delivery-consultant-cloud-infrastructure-architect-aws-professional-services-wwps-us-education-and-state-local-government) | amazon | US, TX, Dallas | 0.5191 | 2026-08-04 |
| [Engineering Operations Technician](https://www.amazon.jobs/en/jobs/10491602/engineering-operations-technician) | amazon | US, VA, Herndon | 0.5182 | 2026-08-04 |
| [Engineering Operations Technician](https://www.amazon.jobs/en/jobs/10491606/engineering-operations-technician) | amazon | US, VA, Herndon | 0.5182 | 2026-08-04 |
| [System Development Engineer, AFT BI Content](https://www.amazon.jobs/en/jobs/10492131/system-development-engineer-aft-bi-content) | amazon | US, WA, Bellevue | 0.5131 | 2026-08-04 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10491112/data-center-technician-dcc-communities) | amazon | US, GA, Lithia Springs | 0.5101 | 2026-08-04 |
| [Cloud Sales Representative](https://www.amazon.jobs/en/jobs/10491716/cloud-sales-representative) | amazon | US, WA, Seattle | 0.5085 | 2026-08-04 |
| [Manager, Finance Operations, AWS](https://www.amazon.jobs/en/jobs/10491053/manager-finance-operations-aws) | amazon | US, VA, Arlington | 0.4995 | 2026-08-04 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10491451/data-center-technician) | amazon | US, PA, Berwick | 0.4992 | 2026-08-04 |
| [Night Data Center Technician ](https://www.amazon.jobs/en/jobs/10491474/night-data-center-technician) | amazon | US, PA, Berwick | 0.4978 | 2026-08-04 |
| [Senior Account Manager - CSP](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Account-Manager---CSP_JR2021680) | nvidia | US, CA, Santa Clara; US, WA, Seattle | 0.4960 | 2026-08-04 |

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
