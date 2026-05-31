import os
import pandas as pd
from src.scoring import add_semantic_scores
from scrapers.apple import scrape_apple
from scrapers.amazon import scrape_amazon
from scrapers.amazon_science import scrape_amazon_science


RAW_DATA_DIR = "data/raw"

APPLE_OUTPUT_PATH = f"{RAW_DATA_DIR}/apple_jobs.csv"
AMAZON_OUTPUT_PATH = f"{RAW_DATA_DIR}/amazon_jobs.csv"
AMAZON_SCIENCE_OUTPUT_PATH = f"{RAW_DATA_DIR}/amazon_science_jobs.csv"

def normalize_key(series):
    return (
        series
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)
        .str.strip()
    )


def save_jobs(current_jobs, output_path):

    today = pd.Timestamp.today().strftime("%Y-%m-%d")

    dedupe_key = "job_id" if "job_id" in current_jobs.columns else "url"

    current_jobs = current_jobs.copy()
    current_jobs[dedupe_key] = normalize_key(current_jobs[dedupe_key])

    current_jobs["last_seen_date"] = today

    if os.path.exists(output_path):
        old_jobs = pd.read_csv(output_path)

        # Support old CSV versions before job_id existed
        if dedupe_key in old_jobs.columns:
            old_jobs[dedupe_key] = normalize_key(old_jobs[dedupe_key])
        else:
            old_jobs[dedupe_key] = None

        if "first_seen_date" not in old_jobs.columns:
            old_jobs["first_seen_date"] = today

        if "last_seen_date" not in old_jobs.columns:
            old_jobs["last_seen_date"] = today

        old_keys = old_jobs[dedupe_key]

        new_jobs = current_jobs[
            ~current_jobs[dedupe_key].isin(old_keys)
        ].copy()

        old_jobs = old_jobs.drop_duplicates(
            subset=[dedupe_key],
            keep="last"
        )

        current_jobs["first_seen_date"] = current_jobs[dedupe_key].map(
            old_jobs.set_index(dedupe_key)["first_seen_date"]
        )

        current_jobs["first_seen_date"] = (
            current_jobs["first_seen_date"]
            .fillna(today)
        )

        jobs = pd.concat(
            [old_jobs, current_jobs],
            ignore_index=True
        )

        jobs = jobs.drop_duplicates(
            subset=[dedupe_key],
            keep="last"
        )

    else:
        current_jobs["first_seen_date"] = today
        new_jobs = current_jobs
        jobs = current_jobs


    if "posted_date" in jobs.columns:
        jobs["posted_date_sort"] = pd.to_datetime(
            jobs["posted_date"],
            errors="coerce"
        )

        jobs = (
            jobs
            .sort_values(
                by=["posted_date_sort", "last_seen_date"],
                ascending=[False, False]
            )
            .drop(columns=["posted_date_sort"])
        )

    jobs = add_semantic_scores(jobs)

    preferred_order = [
        "title",
        "team",
        "location",
        "city",
        "state",
        "posted_date",

        "job_id",
        "source",

        "first_seen_date",
        "last_seen_date",
        "semantic_similarity",

        "job_category",
        "job_family",
        "schedule_type",
        "updated_time",

        "url",

        "description_short",
        "basic_qualifications",
        "preferred_qualifications",
        "description",
    ]

    existing_cols = [c for c in preferred_order if c in jobs.columns]
    remaining_cols = [c for c in jobs.columns if c not in preferred_order]

    jobs = jobs[existing_cols + remaining_cols]

    jobs.to_csv(output_path, index=False)

    print(f"Found {len(current_jobs)} current jobs")
    print(f"Found {len(new_jobs)} truly new jobs")

    if len(new_jobs) > 0:
        print("New jobs:")
        for _, job in new_jobs.iterrows():
            title = job.get("title", "No title")
            location = job.get("location", "")
            url = job.get("url", "")

            print(f"- {title}")
            if location:
                print(f"  Location: {location}")
            if url:
                print(f"  URL: {url}")

    print(f"Saved {len(jobs)} total jobs to {output_path}")

    return new_jobs


def run_pipeline():

    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    apple_jobs = scrape_apple()
    amazon_jobs = scrape_amazon()
    amazon_science_jobs = scrape_amazon_science()


    save_jobs(apple_jobs, APPLE_OUTPUT_PATH)
    save_jobs(amazon_jobs, AMAZON_OUTPUT_PATH)
    save_jobs(amazon_science_jobs, AMAZON_SCIENCE_OUTPUT_PATH)