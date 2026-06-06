import re
from html import unescape

import requests
import pandas as pd


BASE_URL = "https://boards-api.greenhouse.io/v1/boards/duolingo/jobs"

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
    date = pd.to_datetime(date_str, errors="coerce", utc=True)
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def get_metadata(metadata, name):
    for item in metadata or []:
        if item.get("name") == name:
            return item.get("value")
    return None


def scrape_duolingo():
    response = requests.get(
        BASE_URL,
        params={"content": "true"},
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()

    jobs_data = response.json().get("jobs", [])
    print(f"Duolingo: {len(jobs_data)} jobs")

    jobs = []
    for job in jobs_data:
        metadata = job.get("metadata", [])
        departments = job.get("departments", [])
        offices = job.get("offices", [])

        jobs.append({
            "title": job.get("title"),
            "team": departments[0]["name"] if departments else None,
            "location": job.get("location", {}).get("name"),
            "office": offices[0]["name"] if offices else None,
            "posted_date": format_date(job.get("first_published")),
            "updated_date": format_date(job.get("updated_at")),
            "job_id": str(job.get("id")),
            "requisition_id": job.get("requisition_id"),
            "source": "duolingo",
            "division": get_metadata(metadata, "Division"),
            "req_type": get_metadata(metadata, "Req Type"),
            "url": job.get("absolute_url"),
            "description": clean_html_text(job.get("content")),
        })

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(subset=["job_id"], keep="first")
    df = df.sort_values("posted_date", ascending=False, na_position="last")

    return df
