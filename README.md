[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

An automated data pipeline for tracking new job openings directly from company career pages.

JobTracker periodically collects job postings, compares them against previously stored results, identifies newly published roles, and maintains a historical record of openings.

## Motivation

Company career pages are often the most reliable source of up-to-date job openings, but manually checking multiple websites is inefficient.

This project automates that process by monitoring selected companies directly, reducing noise from duplicated or outdated job listings commonly found on job aggregators.

## Features

- Automated scraping of company career pages
- Multi-company support (Apple, Amazon)
- Detection of newly added job postings
- Historical tracking using CSV storage
- Scheduled pipeline execution with GitHub Actions
- Automatic commits when new data is collected

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
   Historical Job Dataset
```

## Project Structure

```text
JobTracker
├── .github/workflows
│   └── scrape_jobs.yml
├── data
│   └── raw
│       ├── amazon_jobs.csv
│       └── apple_jobs.csv
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

## Future Improvements

- Email or Telegram notifications for matching roles
- Keyword and location-based filtering
- Database storage with SQLite/PostgreSQL
- Simple dashboard for exploring job trends

## Status

MVP completed.

The current version runs automatically on a schedule and tracks job openings from multiple companies.
Additional features will focus on notifications, filtering, and improved data storage.