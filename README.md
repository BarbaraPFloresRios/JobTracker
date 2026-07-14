[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Principal AI Scientist, Telco Tech, AWS Industries](https://www.amazon.jobs/en/jobs/10473304/principal-ai-scientist-telco-tech-aws-industries) | amazon | US, TX, Dallas | 0.6186 | 2026-07-14 |
| [Applied Scientist II, Machine Learning Accelerator - Annapurna Labs](https://www.amazon.jobs/en/jobs/10473260/applied-scientist-ii-machine-learning-accelerator-annapurna-labs) | amazon | US, TX, Austin | 0.6092 | 2026-07-14 |
| [Senior Data Engineer, AWS GameTech Cortex](https://www.amazon.jobs/en/jobs/10474555/senior-data-engineer-aws-gametech-cortex) | amazon | US, CA, San Diego | 0.5993 | 2026-07-14 |
| [Associate Delivery Consultant – AIML, A2C ProServe Shared Delivery (SDT)](https://www.amazon.jobs/en/jobs/10473725/associate-delivery-consultant-aiml-a2c-proserve-shared-delivery-sdt) | amazon | US, VA, Arlington | 0.5786 | 2026-07-14 |
| [Principal Product Manager - Technical, AI/ML & Accelerated Computing ](https://www.amazon.jobs/en/jobs/10473081/principal-product-manager-technical-ai-ml-accelerated-computing) | amazon | US, WA, Seattle | 0.5771 | 2026-07-13 |
| [Associate Delivery Consultant – AIML, A2C ProServe Shared Delivery (SDT)](https://www.amazon.jobs/en/jobs/10473722/associate-delivery-consultant-aiml-a2c-proserve-shared-delivery-sdt) | amazon | US, VA, Arlington | 0.5697 | 2026-07-14 |
| [Data Center Logistics Specialist, DCC Communities](https://www.amazon.jobs/en/jobs/10473348/data-center-logistics-specialist-dcc-communities) | amazon | US, IN, New Carlisle | 0.5659 | 2026-07-14 |
| [Sr DC Capex Procurement Manager - Energy infrastructure, Data Center Sourcing and Procurement](https://www.amazon.jobs/en/jobs/10472905/sr-dc-capex-procurement-manager-energy-infrastructure-data-center-sourcing-and-procurement) | amazon | US, WA, Seattle | 0.5639 | 2026-07-13 |
| [Data Center Technician - Night Shift, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10473209/data-center-technician-night-shift-adc-infraops-dco) | amazon | US, MD, Severn | 0.5586 | 2026-07-13 |
| [Customer Success Manager, Consumables - Grocery](https://www.amazon.jobs/en/jobs/10473091/customer-success-manager-consumables-grocery) | amazon | US, WA, Seattle | 0.5544 | 2026-07-13 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10474318/data-center-technician) | amazon | US, AZ, Avondale | 0.5531 | 2026-07-14 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10474320/data-center-technician) | amazon | US, AZ, Mesa | 0.5531 | 2026-07-14 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10474332/data-center-technician) | amazon | US, AZ, Mesa | 0.5531 | 2026-07-14 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10474351/data-center-technician) | amazon | US, AZ, Mesa | 0.5531 | 2026-07-14 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10474331/data-center-technician) | amazon | US, AZ, Mesa | 0.5531 | 2026-07-14 |
| [ Materials Manager, Power & Cooling (PAC)](https://www.amazon.jobs/en/jobs/10474144/materials-manager-power-cooling-pac) | amazon | US, WA, Seattle | 0.5517 | 2026-07-14 |
| [Data Center Technician](https://www.amazon.jobs/en/jobs/10474329/data-center-technician) | amazon | US, AZ, Glendale | 0.5490 | 2026-07-14 |
| [Sr. Delivery Practice Manager, HCLS, AWS Professional Services, Healthcare & Life Sciences](https://www.amazon.jobs/en/jobs/10473672/sr-delivery-practice-manager-hcls-aws-professional-services-healthcare-life-sciences) | amazon | US, VA, Arlington | 0.5457 | 2026-07-14 |
| [Sr. Delivery Practice Manager, HCLS, AWS Professional Services, Healthcare & Life Sciences](https://www.amazon.jobs/en/jobs/10473673/sr-delivery-practice-manager-hcls-aws-professional-services-healthcare-life-sciences) | amazon | US, VA, Arlington | 0.5457 | 2026-07-14 |
| [Program Execution Manager, Public Sector, National Security Programs ](https://www.amazon.jobs/en/jobs/10473041/program-execution-manager-public-sector-national-security-programs) | amazon | US, MD, Jessup | 0.5448 | 2026-07-13 |
| [Data Center Facilities Manager](https://www.amazon.jobs/en/jobs/10474356/data-center-facilities-manager) | amazon | US, NV, Sparks | 0.5372 | 2026-07-14 |
| [Data Center Facilities Manager](https://www.amazon.jobs/en/jobs/10474357/data-center-facilities-manager) | amazon | US, NV, Sparks | 0.5372 | 2026-07-14 |
| [Data Center Facilities Manager](https://www.amazon.jobs/en/jobs/10474361/data-center-facilities-manager) | amazon | US, NV, Sparks | 0.5372 | 2026-07-14 |
| [Data Center Facilities Manager](https://www.amazon.jobs/en/jobs/10474373/data-center-facilities-manager) | amazon | US, NV, Sparks | 0.5372 | 2026-07-14 |
| [Engineering Operations Technician - Night Shift, DCC Communities](https://www.amazon.jobs/en/jobs/10473315/engineering-operations-technician-night-shift-dcc-communities) | amazon | US, IN, New Carlisle | 0.5368 | 2026-07-14 |

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
