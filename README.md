[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Business Intelligence Engineer, PXT, AWS Region Services](https://www.amazon.jobs/en/jobs/10485179/business-intelligence-engineer-pxt-aws-region-services) | amazon | US, VA, Arlington | 0.6080 | 2026-07-27 |
| [Principal Risk Manager, Analytics and Insights](https://www.amazon.jobs/en/jobs/10485077/principal-risk-manager-analytics-and-insights) | amazon | US, NY, New York | 0.6051 | 2026-07-27 |
| [Business Intelligence Engineer, PXT, AWS Region Services](https://www.amazon.jobs/en/jobs/10485383/business-intelligence-engineer-pxt-aws-region-services) | amazon | US, VA, Arlington | 0.5975 | 2026-07-27 |
| [Data Scientist, GTM Intelligence](https://jobs.ashbyhq.com/openai/3b70ebc9-9d9a-4930-ad7b-52c9229f6a52) | openai | San Francisco | 0.5895 | 2026-07-27 |
| [PD Methodology Engineer II, Annapurna Labs](https://www.amazon.jobs/en/jobs/10485401/pd-methodology-engineer-ii-annapurna-labs) | amazon | US, CA, Cupertino | 0.5798 | 2026-07-28 |
| [Data Center Technician, CLT DCO](https://www.amazon.jobs/en/jobs/10484550/data-center-technician-clt-dco) | amazon | US, NC, Hamlet | 0.5707 | 2026-07-27 |
| [Sr. Go-to-Market Lead, AI Agent Platform](https://www.amazon.jobs/en/jobs/10485924/sr-go-to-market-lead-ai-agent-platform) | amazon | US, NY, New York | 0.5633 | 2026-07-28 |
| [SDE, MLA hardware/software co-design, Annapurna Labs Machine Learning Acceleration](https://www.amazon.jobs/en/jobs/10486046/sde-mla-hardware-software-co-design-annapurna-labs-machine-learning-acceleration) | amazon | US, TX, Austin | 0.5525 | 2026-07-28 |
| [Pre-Construction Manager, AMER West Data Center Construction](https://www.amazon.jobs/en/jobs/10486503/pre-construction-manager-amer-west-data-center-construction) | amazon | US, TX, Dallas | 0.5509 | 2026-07-28 |
| [Software Dev Engineer II - AMZ10243908](https://www.amazon.jobs/en/jobs/10486516/software-dev-engineer-ii-amz10243908) | amazon | US, CA, Santa Monica | 0.5503 | 2026-07-28 |
| [Data Center Technician, ADC InfraOps DCO](https://www.amazon.jobs/en/jobs/10486124/data-center-technician-adc-infraops-dco) | amazon | US, TX, San Antonio | 0.5498 | 2026-07-28 |
| [Business Intel Engineer III - AMZ10543876](https://www.amazon.jobs/en/jobs/10485012/business-intel-engineer-iii-amz10543876) | amazon | US, VA, Arlington | 0.5432 | 2026-07-27 |
| [Sr. Solutions Architect, Enterprise (Retail, Restaurant & CPG)](https://www.amazon.jobs/en/jobs/10484914/sr-solutions-architect-enterprise-retail-restaurant-cpg) | amazon | US, CA, San Francisco | 0.5417 | 2026-07-27 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485582/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5383 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485598/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5383 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485595/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5383 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485594/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5383 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485589/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5383 | 2026-07-28 |
| [Data Center Controls Engineer, Deployment](https://www.amazon.jobs/en/jobs/10485587/data-center-controls-engineer-deployment) | amazon | US, VA, Fredericksburg | 0.5383 | 2026-07-28 |
| [PMT III - External Svcs - AMZ9971264](https://www.amazon.jobs/en/jobs/10484718/pmt-iii-external-svcs-amz9971264) | amazon | US, WA, Seattle | 0.5325 | 2026-07-27 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10485814/data-center-technician-dcc-communities) | amazon | US, GA, Covington | 0.5261 | 2026-07-28 |
| [Data Center Technician, DCC Communities ](https://www.amazon.jobs/en/jobs/10485876/data-center-technician-dcc-communities) | amazon | US, GA, Covington | 0.5261 | 2026-07-28 |
| [Program Manager, Books, Risk and Policy, TLC, Risk and Policy, TLC](https://www.amazon.jobs/en/jobs/10486574/program-manager-books-risk-and-policy-tlc-risk-and-policy-tlc) | amazon | US, SC, Charleston | 0.5253 | 2026-07-28 |
| [Tech Writer-Tech III - AMZ10061234](https://www.amazon.jobs/en/jobs/10484708/tech-writer-tech-iii-amz10061234) | amazon | US, WA, Seattle | 0.5240 | 2026-07-27 |
| [Sr. Physical Design Engineer, Annapurna Labs](https://www.amazon.jobs/en/jobs/10485342/sr-physical-design-engineer-annapurna-labs) | amazon | US, TX, Austin | 0.5212 | 2026-07-27 |

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
