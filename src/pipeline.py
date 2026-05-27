import os
import pandas as pd

from scrapers.apple import scrape_apple

OUTPUT_PATH = "data/jobs.csv"


def run_pipeline():
    os.makedirs("data", exist_ok=True)

    current_jobs = scrape_apple()

    if os.path.exists(OUTPUT_PATH):
        old_jobs = pd.read_csv(OUTPUT_PATH)

        new_jobs = current_jobs[
            ~current_jobs["url"].isin(old_jobs["url"])
        ]

        jobs = pd.concat([old_jobs, current_jobs], ignore_index=True)
        jobs = jobs.drop_duplicates(subset=["url"])
    else:
        new_jobs = current_jobs
        jobs = current_jobs

    jobs.to_csv(OUTPUT_PATH, index=False)

    print(f"Found {len(current_jobs)} current jobs")
    print(f"Found {len(new_jobs)} truly new jobs")
    print(f"Saved {len(jobs)} total jobs to {OUTPUT_PATH}")

    return new_jobs