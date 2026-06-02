import re
from html import unescape

import requests
import pandas as pd


BASE_URL = "https://explore.jobs.netflix.net"
SEARCH_URL = f"{BASE_URL}/api/apply/v2/jobs"
DETAIL_URL = f"{BASE_URL}/api/apply/v2/jobs"

MAX_PAGES = 5
RESULTS_PER_PAGE = 20

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0",
}


def clean_html_text(text):
    if not text:
        return None

    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"<.*?>", "", text)
    text = unescape(text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def format_date(date_str):
    date = pd.to_datetime(date_str, errors="coerce")
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def fetch_netflix_job_detail(job_id):
    response = requests.get(
        f"{DETAIL_URL}/{job_id}",
        headers=HEADERS,
    )
    response.raise_for_status()

    return response.json()


def extract_posting_date(detail):
    try:
        date_str = detail.get("custom_JD", {}).get("data_fields", {}).get("posting_date", [None])[0]
        return format_date(date_str)
    except (IndexError, TypeError):
        return None


def scrape_netflix():
    jobs = []

    for page in range(MAX_PAGES):
        start = page * RESULTS_PER_PAGE

        params = {
            "domain": "netflix.com",
            "start": start,
            "num": RESULTS_PER_PAGE,
            "exclude_pid": "",
            "is_acquired_talent": "false",
        }

        response = requests.get(
            SEARCH_URL,
            params=params,
            headers=HEADERS,
        )
        response.raise_for_status()

        data = response.json()
        current_jobs = data.get("positions", [])

        if not current_jobs:
            break

        print(f"Netflix page {page + 1}: {len(current_jobs)} jobs")

        for job in current_jobs:
            job_id = job.get("id")

            if not job_id:
                continue

            try:
                detail = fetch_netflix_job_detail(job_id)
            except requests.exceptions.RequestException as e:
                print(f"Netflix detail failed for {job_id}: {e}")
                detail = {}

            locations = job.get("locations", [])

            jobs.append({
                "title": job.get("name"),
                "team": job.get("department"),
                "location": "; ".join(locations) if locations else job.get("location"),
                "posted_date": extract_posting_date(detail),

                "job_id": job.get("display_job_id"),
                "source": "netflix",

                "business_unit": job.get("business_unit"),
                "work_location_option": job.get("work_location_option"),

                "url": job.get("canonicalPositionUrl"),

                "description": clean_html_text(detail.get("job_description")),
            })

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(
        subset=["job_id"],
        keep="first",
    )

    df = df.sort_values(
        "posted_date",
        ascending=False,
        na_position="last",
    )

    return df