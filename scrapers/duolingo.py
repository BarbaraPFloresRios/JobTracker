import re
from html import unescape

import requests
import pandas as pd


SEARCH_URL = "https://boards-api.greenhouse.io/v1/boards/duolingo/jobs"

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
    date = pd.to_datetime(
        date_str,
        errors="coerce",
        utc=True,
    )

    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def get_metadata(metadata, name):
    for item in metadata or []:
        if item.get("name") == name:
            return item.get("value")

    return None


def scrape_duolingo():
    jobs = []

    response = requests.get(
        SEARCH_URL,
        params={"content": "true"},
        headers=HEADERS,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()
    current_jobs = data.get("jobs", [])

    if not current_jobs:
        return pd.DataFrame(jobs)

    print(f"Duolingo page 1: {len(current_jobs)} jobs")

    for job in current_jobs:
        metadata = job.get("metadata", [])
        departments = job.get("departments", [])
        offices = job.get("offices", [])

        jobs.append({
            "title": job.get("title"),
            "team": (
                departments[0].get("name")
                if departments
                else None
            ),
            "location": job.get("location", {}).get("name"),
            "posted_date": format_date(job.get("first_published")),

            "job_id": str(job.get("id")),
            "source": "duolingo",

            "office": (
                offices[0].get("name")
                if offices
                else None
            ),
            "requisition_id": job.get("requisition_id"),
            "division": get_metadata(metadata, "Division"),
            "req_type": get_metadata(metadata, "Req Type"),
            "updated_date": format_date(job.get("updated_at")),

            "url": job.get("absolute_url"),

            "description": clean_html_text(job.get("content")),
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