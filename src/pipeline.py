import os
import pandas as pd

from scrapers.apple import scrape_apple

OUTPUT_PATH = "data/jobs.csv"


def run_pipeline():
    os.makedirs("data", exist_ok=True)

    new_jobs = scrape_apple()

    if os.path.exists(OUTPUT_PATH):
        old_jobs = pd.read_csv(OUTPUT_PATH)
        jobs = pd.concat([old_jobs, new_jobs], ignore_index=True)
        jobs = jobs.drop_duplicates(subset=["url"])
    else:
        jobs = new_jobs

    jobs.to_csv(OUTPUT_PATH, index=False)

    print(f"Found {len(new_jobs)} new/current jobs")
    print(f"Saved {len(jobs)} total jobs to {OUTPUT_PATH}")