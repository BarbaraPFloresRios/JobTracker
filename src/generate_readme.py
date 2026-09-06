import pandas as pd


README_PATH = "README.md"
RECENT_JOBS_PATH = "data/recent_jobs.csv"

# Companies currently tracked (kept in sync with the scrapers list in
# src/pipeline.py). Update both places when adding or removing a company.
COMPANIES = [
    "MercadoLibre",
    "Apple",
    "Amazon",
    "Amazon Science",
    "NVIDIA",
    "Microsoft",
    "Netflix",
    "Meta",
    "OpenAI",
    "Anthropic",
    "Duolingo",
    "Spotify",
    "Reddit",
    "Discord",
    "Canva",
    "Uber",
    "Airbnb",
]


def make_companies_list():
    return "\n".join(f"* {company}" for company in COMPANIES)


def make_jobs_table(max_rows=25):
    df = pd.read_csv(RECENT_JOBS_PATH)

    if df.empty:
        return "_No recent jobs found._"

    df = df.sort_values(
        "semantic_similarity",
        ascending=False
    ).head(max_rows)

    rows = [
        "| Title | Company | Location | Similarity | First Seen |",
        "|---|---|---|---:|---|",
    ]

    for _, job in df.iterrows():
        title = str(job.get("title", "")).replace("|", "\\|")
        company = str(job.get("company", "")).replace("|", "\\|")
        location = str(job.get("location", "")).replace("|", "\\|")
        score = job.get("semantic_similarity", "")
        first_seen = job.get("first_seen_date", "")
        url = job.get("url", "")

        try:
            score = f"{float(score):.4f}"
        except (TypeError, ValueError):
            score = ""

        title_cell = f"[{title}]({url})" if url else title

        rows.append(
            f"| {title_cell} | {company} | {location} | {score} | {first_seen} |"
        )

    return "\n".join(rows)


def generate_readme():
    jobs_table = make_jobs_table()
    companies_list = make_companies_list()

    content = f"""[![Scrape Jobs](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml/badge.svg)](https://github.com/BarbaraPFloresRios/JobTracker/actions/workflows/scrape_jobs.yml)

# JobTracker

A lightweight job monitoring and semantic matching system built in Python.

## Why this exists

The job market is tough right now, and the postings that matter most are the **newly opened** ones: applying early, before a role gets flooded with applicants, is one of the few things a candidate can actually control. JobTracker watches company career pages several times a day, flags the openings that appeared **today and yesterday**, and ranks them by how well they match your own profile — so you spend your energy applying to fresh, relevant roles instead of refreshing career pages by hand.

# Latest Jobs

_Updated automatically from `data/recent_jobs.csv`._

{jobs_table}

## Companies tracked

JobTracker currently pulls openings directly from the career pages / official APIs of:

{companies_list}

## How it works

1. A scraper per company collects current openings straight from the source.
2. Each company's postings are stored as a CSV under `data/raw/`, keeping a history with `first_seen_date` and `last_seen_date` for every job.
3. Recently discovered roles (first seen today or yesterday) are exported to `data/recent_jobs.csv`.
4. Each recent job is scored by semantic similarity against a configurable candidate profile, and the top matches are surfaced in the table above.
5. A GitHub Action runs the whole pipeline every 3 hours and commits the refreshed data automatically.

If one company's site or API changes and its scraper fails, the pipeline logs the error, keeps that company's previous data, and continues with the rest — so a single broken source never stops the run.

## Run it locally

Requires Python 3.11+.

```bash
# 1. Clone the repo
git clone https://github.com/BarbaraPFloresRios/JobTracker.git
cd JobTracker

# 2. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install the browser used by some scrapers
playwright install --with-deps chromium

# 5. Run the full pipeline
python main.py
```

This regenerates `data/raw/*.csv`, `data/recent_jobs.csv`, and this `README.md`.

## Personalize the ranking

Semantic matching is driven by a plain-text profile at [`data/profile/job_matching_profile.txt`](data/profile/job_matching_profile.txt). Edit that file to describe the roles, skills, and seniority you're targeting, then run `python main.py` again — the similarity scores and the "Latest Jobs" ranking will reflect your profile.

## Current Features

* Scrape job postings directly from company career pages
* Support multiple companies
* Detect newly discovered openings
* Track historical job data over time
* Run automatically using GitHub Actions
* Fault-tolerant pipeline: a failing scraper never stops the others
* Store structured datasets as CSV files
* Export recent jobs from today and yesterday
* Semantic job matching using sentence embeddings
* Configurable candidate profile for personalized ranking
* Cosine similarity scoring between jobs and candidate profile

## Status

Active personal project focused on job discovery, semantic search, and recommendation workflows.
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    generate_readme()
    print("Updated README.md")