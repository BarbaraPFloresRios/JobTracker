[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

JobTracker automatically collects openings directly from company career pages, maintains historical records of job postings, and ranks opportunities using semantic similarity against a configurable candidate profile.

The project combines web scraping, data pipelines, automation, embeddings, and semantic search to help surface relevant opportunities from large job catalogs.

## Motivation

Company career pages are often the most up-to-date source of job openings, but manually checking multiple websites can be repetitive and time-consuming.

The goal of this project is to automate job discovery while exploring practical applications of semantic search and recommendation systems.

## Current Features

* Scrape job postings directly from company career pages
* Support multiple companies (currently Apple and Amazon)
* Detect newly discovered openings
* Track historical job data over time
* Run automatically using GitHub Actions
* Store structured datasets as CSV files
* Semantic job matching using sentence embeddings
* Configurable candidate profile for personalized ranking
* Cosine similarity scoring between jobs and candidate profile

## Pipeline Overview

```text
GitHub Actions (scheduled)
          |
          v
       main.py
          |
          v
   Company Scrapers
   (Apple, Amazon)
          |
          v
   Processing Pipeline
          |
          +------------------+
          |                  |
          v                  v
 Historical Storage   Semantic Matching
                           |
                           v
                 Candidate Profile
                           |
                           v
                 semantic_similarity
                           |
                           v
                     CSV Output
```

## Semantic Matching

Each job posting is converted into a text representation using all available job attributes.

The system:

1. Builds a textual representation of each job.
2. Generates embeddings using the `all-MiniLM-L6-v2` model.
3. Generates an embedding for a configurable candidate profile.
4. Computes cosine similarity between jobs and the profile.
5. Stores a `semantic_similarity` score for ranking opportunities.

This approach enables semantic matching beyond simple keyword filtering.

## Project Structure

```text
JobTracker
├── data
│   ├── profile
│   │   └── job_matching_profile.txt
│   └── raw
│       ├── amazon_jobs.csv
│       └── apple_jobs.csv
├── scrapers
│   ├── amazon.py
│   └── apple.py
├── src
│   ├── pipeline.py
│   └── scoring.py
├── main.py
└── requirements.txt
```

## Tech Stack

* Python
* Pandas
* Requests
* BeautifulSoup
* Sentence Transformers
* Scikit-learn
* PyTorch
* GitHub Actions

## Future Improvements

* Notification system for highly relevant new openings
* Additional company integrations
* Database storage (SQLite/PostgreSQL)
* Dashboard for exploring opportunities
* Recommendation feedback loop based on user preferences

## Status

Active personal project focused on job discovery, semantic search, and recommendation workflows.
