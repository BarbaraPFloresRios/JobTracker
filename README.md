[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

| Title | Company | Location | Similarity | First Seen |
|---|---|---|---:|---|
| [Systems Integration Engineer, Fleet Remediation Engineering](https://www.amazon.jobs/en/jobs/10471935/systems-integration-engineer-fleet-remediation-engineering) | amazon | US, WA, Seattle | 0.4727 | 2026-07-13 |
| [Event Support Lead, Global Skilling](https://apply.careers.microsoft.com/careers/job/1970393556925926) | microsoft | United States, Multiple Locations, Multiple Locations | 0.4566 | 2026-07-12 |
| [Security Engineer Manager, SBS Specialized Detections](https://www.amazon.jobs/en/jobs/10471879/security-engineer-manager-sbs-specialized-detections) | amazon | US, NY, New York | 0.4541 | 2026-07-13 |
| [Decom Tech, ADC InfraOps Decom](https://www.amazon.jobs/en/jobs/10471854/decom-tech-adc-infraops-decom) | amazon | US, VA, Alexandria | 0.4165 | 2026-07-12 |
| [Decom Tech, ADC InfraOps Decom](https://www.amazon.jobs/en/jobs/10471853/decom-tech-adc-infraops-decom) | amazon | US, VA, Alexandria | 0.4165 | 2026-07-12 |
| [Manager, Engineering Program Manager, Apple Foundation Models, Engineering Tools](https://jobs.apple.com/en-us/details/200671839-0836/manager-engineering-program-manager-apple-foundation-models-engineering-tools?team=SFTWR) | apple | nan | 0.3300 | 2026-07-13 |
| [Regional Security Operations Lead](https://apply.careers.microsoft.com/careers/job/1970393556927710) | microsoft | United States, Multiple Locations, Multiple Locations | 0.3251 | 2026-07-12 |
| [Security and Safety Manager - Onsite, San Francisco](https://jobs.smartrecruiters.com/Canva/6000000001226603-security-and-safety-manager-onsite-san-francisco) | canva | San Francisco, , United States | 0.3135 | 2026-07-13 |
| [Principal Product Manager](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Principal-Product-Manager_JR2017591) | nvidia | US, CA, Santa Clara; US, NY, New York; US, WA, Seattle | 0.3037 | 2026-07-12 |
| [Manager, Executive Operations](https://www.metacareers.com/profile/job_details/2489823428107635) | meta | Menlo Park, CA | 0.2585 | 2026-07-12 |
| [Reliability & Asset Management](https://www.metacareers.com/profile/job_details/1603126411819671) | meta | Henrico, VA | 0.2487 | 2026-07-12 |
| [Certified Pharmacy Technician, Amazon Pharmacy](https://www.amazon.jobs/en/jobs/10471943/certified-pharmacy-technician-amazon-pharmacy) | amazon | US, MA, Wilmington | 0.2438 | 2026-07-13 |
| [Certified Pharmacy Technician, Amazon Pharmacy](https://www.amazon.jobs/en/jobs/10471940/certified-pharmacy-technician-amazon-pharmacy) | amazon | US, MA, Wilmington | 0.2438 | 2026-07-13 |
| [Certified Pharmacy Technician, Amazon Pharmacy](https://www.amazon.jobs/en/jobs/10471945/certified-pharmacy-technician-amazon-pharmacy) | amazon | US, MA, Wilmington | 0.2438 | 2026-07-13 |
| [Hardware Systems Design Electrical Engineer (iPhone)](https://jobs.apple.com/en-us/details/200672066-0836/hardware-systems-design-electrical-engineer-iphone?team=HRDWR) | apple | nan | 0.2339 | 2026-07-12 |
| [Certified Pharmacy Technician, Amazon Pharmacy](https://www.amazon.jobs/en/jobs/10471946/certified-pharmacy-technician-amazon-pharmacy) | amazon | US, PA, Imperial | 0.2245 | 2026-07-13 |
| [Senior Product Manager, Affordability](https://jobs.apple.com/en-us/details/200649834-0836/senior-product-manager-affordability?team=CORSV) | apple | nan | 0.2225 | 2026-07-13 |
| [Technical Program MGR - Audio](https://jobs.apple.com/en-us/details/200671443-0836/technical-program-mgr-audio?team=OPMFG) | apple | nan | 0.1555 | 2026-07-12 |

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
