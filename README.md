[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Senior Applied Scientist, Special Projects](https://www.amazon.jobs/en/jobs/10492852/senior-applied-scientist-special-projects) | amazon | US, WA, Seattle | 0.6340 | 2026-08-05 |
| [Sr. Applied Scientist, Prime Video - Personalization and Discovery Science](https://www.amazon.jobs/en/jobs/10491282/sr-applied-scientist-prime-video-personalization-and-discovery-science) | amazon | US, CA, Sunnyvale | 0.6170 | 2026-08-04 |
| [Principal Product Marketing Manager](https://www.amazon.jobs/en/jobs/10491024/principal-product-marketing-manager) | amazon | US, WA, Bellevue | 0.6048 | 2026-08-04 |
| [Applied Scientist, Fauna](https://www.amazon.jobs/en/jobs/10491116/applied-scientist-fauna) | amazon | US, NY, New York | 0.6034 | 2026-08-04 |
| [Head of Developer Enablement, Kiro](https://www.amazon.jobs/en/jobs/10492319/head-of-developer-enablement-kiro) | amazon | US, NY, New York | 0.5916 | 2026-08-05 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10490636/data-center-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5749 | 2026-08-04 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556949793) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5726 | 2026-08-04 |
| [Data Center Project Engineer, Data Center Construction](https://www.amazon.jobs/en/jobs/10492312/data-center-project-engineer-data-center-construction) | amazon | US, VA, Culpeper | 0.5663 | 2026-08-04 |
| [Pr. Worldwide Partner Specialist - Global System Integrators, Data & AI GTM ](https://www.amazon.jobs/en/jobs/10492186/pr-worldwide-partner-specialist-global-system-integrators-data-ai-gtm) | amazon | US, WA, Seattle | 0.5637 | 2026-08-04 |
| [Infra Delivery Install Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10492979/infra-delivery-install-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5634 | 2026-08-05 |
| [Senior Learning Architect, Employee Skilling, Skilling & Social Impact (SSI)](https://www.amazon.jobs/en/jobs/10493023/senior-learning-architect-employee-skilling-skilling-social-impact-ssi) | amazon | US, VA, Arlington | 0.5602 | 2026-08-05 |
| [Software Development Engineer III, Annapurna Labs](https://www.amazon.jobs/en/jobs/10493477/software-development-engineer-iii-annapurna-labs) | amazon | US, NY, New York | 0.5586 | 2026-08-05 |
| [Software Development Engineer II, Analytics ADC](https://www.amazon.jobs/en/jobs/10493531/software-development-engineer-ii-analytics-adc) | amazon | US, VA, Arlington | 0.5581 | 2026-08-05 |
| [Datacenter Engineering Telecom Engineer - AMER](https://apply.careers.microsoft.com/careers/job/1970393556950887) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5576 | 2026-08-04 |
| [Applied Scientist, Prime Video - Generative AI](https://www.amazon.jobs/en/jobs/10492458/applied-scientist-prime-video-generative-ai) | amazon | US, NY, New York | 0.5562 | 2026-08-05 |
| [Principal S&OP Planner, Infrastructure Capacity & S&OP Planning](https://www.amazon.jobs/en/jobs/10492008/principal-s-op-planner-infrastructure-capacity-s-op-planning) | amazon | US, WA, Seattle | 0.5552 | 2026-08-04 |
| [DCO Tech, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10491717/dco-tech-adc-infraops-dco) | amazon | US, CO, Aurora | 0.5530 | 2026-08-04 |
| [Marketing Manager, Energy, Industry Marketing ](https://www.amazon.jobs/en/jobs/10493532/marketing-manager-energy-industry-marketing) | amazon | US, NY, New York | 0.5519 | 2026-08-05 |
| [Construction Manager , ADC East ](https://www.amazon.jobs/en/jobs/10492818/construction-manager-adc-east) | amazon | US, MD, Jessup | 0.5486 | 2026-08-05 |
| [Data Center Operations Manager  , ATL DCO](https://www.amazon.jobs/en/jobs/10491480/data-center-operations-manager-atl-dco) | amazon | US, GA, Hampton | 0.5478 | 2026-08-04 |
| [Senior Solutions Architect, AGS Software and Technology (SWAT) ](https://www.amazon.jobs/en/jobs/10491379/senior-solutions-architect-ags-software-and-technology-swat) | amazon | US, NY, New York | 0.5477 | 2026-08-04 |
| [Senior Delivery Consultant - Cloud Infrastructure Architect AWS Professional Services, WWPS US Education and State & Local Government](https://www.amazon.jobs/en/jobs/10491520/senior-delivery-consultant-cloud-infrastructure-architect-aws-professional-services-wwps-us-education-and-state-local-government) | amazon | US, TX, Dallas | 0.5454 | 2026-08-04 |
| [Engineering Operations Technician, DCC Communities](https://www.amazon.jobs/en/jobs/10490683/engineering-operations-technician-dcc-communities) | amazon | US, VA, Sterling | 0.5446 | 2026-08-04 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556952567) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5415 | 2026-08-05 |
| [Data Center Infrastructure Delivery Manager](https://www.amazon.jobs/en/jobs/10492901/data-center-infrastructure-delivery-manager) | amazon | US, VA, Fredericksburg | 0.5386 | 2026-08-05 |

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
