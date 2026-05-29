[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

🚧 An MVP data pipeline for tracking job openings directly from company career pages.

JobTracker automatically collects job postings, compares them against previously stored results, and keeps a historical record of openings over time.

The long-term goal is to build a lightweight job monitoring system that can notify users when relevant new opportunities appear.

## Motivation

Company career pages are often the closest source to real-time openings, but manually checking multiple websites is time-consuming.

This project explores how to automate that workflow by collecting job data directly from selected companies and reducing noise from repeated listings.

## Current Features

- Scrape job postings from company career pages
- Support multiple companies (Apple, Amazon)
- Detect newly added openings
- Store historical job data locally
- Run automatically using GitHub Actions
- Commit updated datasets after scheduled runs

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
          v
   Historical CSV Storage
```

## Project Structure

```text
JobTracker
├── .github/workflows
│   └── scrape_jobs.yml
├── data/raw
│   ├── amazon_jobs.csv
│   └── apple_jobs.csv
├── scrapers
│   ├── amazon.py
│   └── apple.py
├── src
│   └── pipeline.py
├── main.py
└── requirements.txt
```

## Tech Stack

- Python
- Requests
- BeautifulSoup
- Pandas
- GitHub Actions

## Planned Improvements

- Email or Telegram alerts for matching roles
- Keyword and location filters
- Better historical tracking (first seen / last seen dates)
- Database storage (SQLite/PostgreSQL)
- Simple dashboard for exploring openings

## Status

🚧 Functional MVP.

The current version runs automatically and tracks openings from selected companies. Future iterations will focus on notifications, filtering, and improving data storage.