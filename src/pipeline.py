import os
import pandas as pd

from scrapers.apple import scrape_apple
from scrapers.amazon import scrape_amazon

RAW_DATA_DIR = "data/raw"

APPLE_OUTPUT_PATH = f"{RAW_DATA_DIR}/apple_jobs.csv"
AMAZON_OUTPUT_PATH = f"{RAW_DATA_DIR}/amazon_jobs.csv"


def save_jobs(current_jobs, output_path):

    if os.path.exists(output_path):
        old_jobs = pd.read_csv(output_path)

        new_jobs = current_jobs[
            ~current_jobs["url"].isin(old_jobs["url"])
        ]

        jobs = pd.concat([old_jobs, current_jobs], ignore_index=True)
        jobs = jobs.drop_duplicates(subset=["url"])

    else:
        new_jobs = current_jobs
        jobs = current_jobs

    jobs.to_csv(output_path, index=False)

    print(f"Found {len(current_jobs)} current jobs")
    print(f"Found {len(new_jobs)} truly new jobs")
    print(f"Saved {len(jobs)} total jobs to {output_path}")

    return new_jobs


def run_pipeline():

    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    apple_jobs = scrape_apple()
    amazon_jobs = scrape_amazon()

    save_jobs(apple_jobs, APPLE_OUTPUT_PATH)
    save_jobs(amazon_jobs, AMAZON_OUTPUT_PATH)