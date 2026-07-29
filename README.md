[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Sr. Applied Scientist,  Pricing Science](https://www.amazon.jobs/en/jobs/10487538/sr-applied-scientist-pricing-science) | amazon | US, WA, Seattle | 0.6501 | 2026-07-29 |
| [Data Scientist, Prime Video](https://www.amazon.jobs/en/jobs/10486917/data-scientist-prime-video) | amazon | US, WA, Seattle | 0.6415 | 2026-07-29 |
| [Data Engineer, Data Platform Management, World Wide Grocery Tech](https://www.amazon.jobs/en/jobs/10487395/data-engineer-data-platform-management-world-wide-grocery-tech) | amazon | US, TX, Austin | 0.6314 | 2026-07-29 |
| [Senior Applied Scientist, PXT ](https://www.amazon.jobs/en/jobs/10487510/senior-applied-scientist-pxt) | amazon | US, WA, Seattle | 0.6281 | 2026-07-29 |
| [Applied Scientist II, ASCS AI Lab Team](https://www.amazon.jobs/en/jobs/10487564/applied-scientist-ii-ascs-ai-lab-team) | amazon | US, CA, Sunnyvale | 0.6061 | 2026-07-29 |
| [PD Methodology Engineer II, Annapurna Labs](https://www.amazon.jobs/en/jobs/10485401/pd-methodology-engineer-ii-annapurna-labs) | amazon | US, CA, Cupertino | 0.5962 | 2026-07-28 |
| [Sr. GenAI & ML Specialist Solutions Architect, ASPI Auto & Manufacturing](https://www.amazon.jobs/en/jobs/10486724/sr-genai-ml-specialist-solutions-architect-aspi-auto-manufacturing) | amazon | US, MI, Detroit | 0.5874 | 2026-07-28 |
| [Data Center Facility Manager, ADC InfraOps AG](https://www.amazon.jobs/en/jobs/10487734/data-center-facility-manager-adc-infraops-ag) | amazon | US, VA, Warrenton | 0.5871 | 2026-07-29 |
| [Software Dev Engineer II - AMZ10243908](https://www.amazon.jobs/en/jobs/10486516/software-dev-engineer-ii-amz10243908) | amazon | US, CA, Santa Monica | 0.5754 | 2026-07-28 |
| [Sr. Go-to-Market Lead, AI Agent Platform](https://www.amazon.jobs/en/jobs/10485924/sr-go-to-market-lead-ai-agent-platform) | amazon | US, NY, New York | 0.5743 | 2026-07-28 |
| [Principal Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556941428) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5741 | 2026-07-28 |
| [Data Center Facility Manager, ADC InfraOps AG](https://www.amazon.jobs/en/jobs/10487739/data-center-facility-manager-adc-infraops-ag) | amazon | US, VA, Fairfax | 0.5731 | 2026-07-29 |
| [Pre-Construction Manager, AMER West Data Center Construction](https://www.amazon.jobs/en/jobs/10486503/pre-construction-manager-amer-west-data-center-construction) | amazon | US, TX, Dallas | 0.5713 | 2026-07-28 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10487567/data-center-technician) | amazon | US, PA, Berwick | 0.5671 | 2026-07-29 |
| [Manager, Data and AI Engineering](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Manager--Data-and-AI-Engineering_JR2016861) | nvidia | US, CA, Santa Clara | 0.5669 | 2026-07-29 |
| [Senior Product Marketing Manager - Data Processing](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Product-Marketing-Manager---Data-Processing_JR2022150-1) | nvidia | US, CA, Santa Clara | 0.5639 | 2026-07-29 |
| [Customer Solutions Manager, USAF](https://www.amazon.jobs/en/jobs/10486897/customer-solutions-manager-usaf) | amazon | US, VA, Arlington | 0.5627 | 2026-07-29 |
| [SDE, MLA hardware/software co-design, Annapurna Labs Machine Learning Acceleration](https://www.amazon.jobs/en/jobs/10486046/sde-mla-hardware-software-co-design-annapurna-labs-machine-learning-acceleration) | amazon | US, TX, Austin | 0.5562 | 2026-07-28 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10487735/data-center-technician) | amazon | US, PA, Berwick | 0.5548 | 2026-07-29 |
| [Principal PMT-ES, SSO](https://www.amazon.jobs/en/jobs/10487411/principal-pmt-es-sso) | amazon | US, CA, Santa Clara | 0.5548 | 2026-07-29 |
| [Data Center Technician ](https://www.amazon.jobs/en/jobs/10487088/data-center-technician) | amazon | US, PA, Berwick | 0.5548 | 2026-07-29 |
| [Director, Go-To-Market Segment, Cloud & AI Platforms](https://apply.careers.microsoft.com/careers/job/1970393556926841) | microsoft | United States, Multiple Locations, Multiple Locations | 0.5539 | 2026-07-29 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485587/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5522 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485582/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5522 | 2026-07-28 |
| [Business Intel Engineer II - AMZ9890743](https://www.amazon.jobs/en/jobs/10486440/business-intel-engineer-ii-amz9890743) | amazon | US, CA, Culver City | 0.5522 | 2026-07-29 |

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
