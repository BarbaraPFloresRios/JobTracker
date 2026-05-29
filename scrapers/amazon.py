import re
import requests
import pandas as pd

BASE_URL = "https://www.amazon.jobs"
SEARCH_URL = "https://www.amazon.jobs/en/search.json"

MAX_PAGES = 5  # Covers latest 50 postings per run
RESULTS_PER_PAGE = 10

HEADERS = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0",
}


def extract_amazon_job_id(job_path):
    match = re.search(r"/jobs/(\d+)", job_path)
    return match.group(1) if match else None


def scrape_amazon():

    jobs = []

    for page in range(MAX_PAGES):

        offset = page * RESULTS_PER_PAGE

        params = {
            "country": "USA",
            "sort": "recent",
            "offset": offset,
            "result_limit": RESULTS_PER_PAGE,
        }

        response = requests.get(
            SEARCH_URL,
            params=params,
            headers=HEADERS
        )

        response.raise_for_status()

        data = response.json()

        current_jobs = data.get("jobs", [])

        if not current_jobs:
            break

        print(
            f"Amazon page {page + 1}: {len(current_jobs)} jobs"
        )

        for job in current_jobs:

            job_path = job.get("job_path")

            if not job_path:
                continue

            job_id = extract_amazon_job_id(job_path)

            posted_date_raw = job.get("posted_date")

            posted_date = pd.to_datetime(
                posted_date_raw,
                errors="coerce"
            )

            posted_date = (
                posted_date.strftime("%Y-%m-%d")
                if pd.notna(posted_date)
                else None
            )

            jobs.append({
                "source": "amazon",
                "job_id": job_id,
                "title": job.get("title"),
                "team": job.get("business_category"),
                "job_category": job.get("job_category"),
                "location": job.get("location"),
                "posted_date": posted_date,
                "description": job.get("description_short"),
                "url": BASE_URL + job_path,
            })


    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(
        subset=["job_id"],
        keep="first"
    )

    df = df.sort_values(
        "posted_date",
        ascending=False
    )

    return df