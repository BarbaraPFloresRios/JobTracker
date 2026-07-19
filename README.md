[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Economist, People Experience and Technology Central Science](https://www.amazon.jobs/jobs/10478045/economist-people-experience-and-technology-central-science?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.5250 | 2026-07-18 |
| [Field Sales Ops Lead, FinServ , NAMER Sales Operations](https://www.amazon.jobs/en/jobs/10477987/field-sales-ops-lead-finserv-namer-sales-operations) | amazon | US, NY, New York | 0.5120 | 2026-07-18 |
| [Psychometrician, AWS Training & Certification](https://www.amazon.jobs/jobs/10477964/psychometrician-aws-training--certification?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.5098 | 2026-07-18 |
| [Sr. Enterprise Account Manager, Automotive & Manufacturing](https://www.amazon.jobs/en/jobs/10478020/sr-enterprise-account-manager-automotive-manufacturing) | amazon | US, CA, San Francisco | 0.4984 | 2026-07-18 |
| [Senior Systems Software Engineer - NVLink](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Systems-Software-Engineer---NVLink_JR2007807) | nvidia | US, CA, Santa Clara; US, Remote | 0.4815 | 2026-07-19 |
| [Manager - Site Deployment , OneMHS](https://www.amazon.jobs/en/jobs/10477988/manager-site-deployment-onemhs) | amazon | US, OH, Cincinnati | 0.4808 | 2026-07-18 |
| [Senior Backend Platform Engineer](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Backend-Platform-Engineer_JR2021162) | nvidia | US, CA, Santa Clara | 0.4797 | 2026-07-18 |
| [Senior Technical Program Manager](https://apply.careers.microsoft.com/careers/job/1970393556850761) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4750 | 2026-07-18 |
| [Software Engineering IC4](https://apply.careers.microsoft.com/careers/job/1970393556926994) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4657 | 2026-07-18 |
| [Senior Software Engineer](https://apply.careers.microsoft.com/careers/job/1970393556926865) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4625 | 2026-07-18 |
| [Manager III, Applied Science, PXT Central Science](https://www.amazon.jobs/jobs/10478042/manager-iii-applied-science-pxt-central-science?cmpid=bsp-amazon-science) | amazon_science | US, VA, Arlington | 0.4461 | 2026-07-18 |
| [Director, Go-To-Market Management for Security Programs](https://apply.careers.microsoft.com/careers/job/1970393556938889) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4400 | 2026-07-18 |
| [Financial Analyst, International Stores FP&A](https://www.amazon.jobs/en/jobs/10478081/financial-analyst-international-stores-fp-a) | amazon | US, WA, Seattle | 0.4395 | 2026-07-18 |
| [Applied Scientist, Sponsored Products Off-Search Auction](https://www.amazon.jobs/jobs/10477372/applied-scientist-sponsored-products-offsearch-auction?cmpid=bsp-amazon-science) | amazon_science | US, WA, Seattle | 0.4232 | 2026-07-18 |
| [Principal Conn. Systems Engr., Connectivity Systems](https://www.amazon.jobs/en/jobs/10478028/principal-conn-systems-engr-connectivity-systems) | amazon | US, CA, Sunnyvale | 0.4181 | 2026-07-18 |
| [JR41525 Technology Experience Specialist (12 months FTC)](https://explore.jobs.netflix.net/careers/job/790317166063) | netflix | Amsterdam,Netherlands | 0.4140 | 2026-07-19 |
| [Senior Manager, Security Incident Response](https://www.amazon.jobs/en/jobs/10477982/senior-manager-security-incident-response) | amazon | US, CA, San Francisco | 0.4065 | 2026-07-18 |
| [Senior Planning and Landing Lead](https://apply.careers.microsoft.com/careers/job/1970393556934082) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4050 | 2026-07-18 |
| [IS&T Early Career Engineering Program Manager Opportunities](https://jobs.apple.com/en-us/details/200672968-0157/is-t-early-career-engineering-program-manager-opportunities?team=SFTWR) | apple | nan | 0.4039 | 2026-07-18 |
| [Principal Account Manager, Enterprise, CPG](https://www.amazon.jobs/en/jobs/10478021/principal-account-manager-enterprise-cpg) | amazon | US, TX, Houston | 0.4005 | 2026-07-18 |
| [Senior System Software Engineer - AV Platform](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-System-Software-Engineer---AV-Platform_JR2021284) | nvidia | US, CA, Santa Clara | 0.3930 | 2026-07-18 |
| [Director, Partner Success](https://apply.careers.microsoft.com/careers/job/1970393556927642) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3853 | 2026-07-18 |
| [Machine Learning Engineer, Wallet Intelligence and Machine Learning](https://jobs.apple.com/en-us/details/200672668-0157/machine-learning-engineer-wallet-intelligence-and-machine-learning?team=MLAI) | apple | nan | 0.3749 | 2026-07-18 |
| [QA/DevOps Engineer](https://job-boards.greenhouse.io/discord/jobs/8637648002) | discord | San Francisco Bay Area | 0.3684 | 2026-07-18 |
| [Engineering Manager, Growth](https://job-boards.greenhouse.io/anthropic/jobs/5361472008) | anthropic | New York City, NY; San Francisco, CA; Seattle, WA | 0.3626 | 2026-07-18 |

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
