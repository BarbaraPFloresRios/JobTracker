import re
from html import unescape

import pandas as pd
import requests


SEARCH_URL = "https://boards-api.greenhouse.io/v1/boards/reddit/jobs"

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


def metadata_to_dict(metadata):
    result = {}

    for item in metadata or []:
        name = item.get("name")
        value = item.get("value")

        if not name:
            continue

        key = (
            name
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
        )

        result[key] = value

    return result


def format_date(date_value):
    date = pd.to_datetime(date_value, errors="coerce")
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def scrape_reddit():
    response = requests.get(
        SEARCH_URL,
        params={"content": "true"},
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()

    current_jobs = response.json().get("jobs", [])

    print(f"Reddit: {len(current_jobs)} jobs")

    jobs = []

    for job in current_jobs:
        metadata = metadata_to_dict(job.get("metadata"))

        departments = job.get("departments") or []
        offices = job.get("offices") or []

        department = (
            departments[0].get("name")
            if departments
            else metadata.get("department")
        )

        office = (
            offices[0].get("name")
            if offices
            else None
        )

        jobs.append({
            "title": job.get("title"),
            "team": department,
            "location": job.get("location", {}).get("name"),
            "posted_date": format_date(job.get("first_published")),

            "job_id": job.get("id"),
            "internal_job_id": job.get("internal_job_id"),
            "requisition_id": job.get("requisition_id"),
            "position_id": metadata.get("position_id"),
            "source": "reddit",

            "management_level": metadata.get("management_level"),
            "job_profile": metadata.get("job_profile"),
            "job_family": metadata.get("job_family"),
            "worker_sub_type": metadata.get("worker_sub_type"),
            "worker_type": metadata.get("worker_type"),
            "time_type": metadata.get("time_type"),
            "pay_rate_type": metadata.get("pay_rate_type"),
            "scheduled_weekly_hours": metadata.get("scheduled_weekly_hours"),
            "cost_center": metadata.get("cost_center"),
            "company_name": job.get("company_name"),

            "recruiting_start_date": format_date(
                metadata.get("recruiting_start_date")
            ),
            "target_hire_date": format_date(
                metadata.get("target_hire_date")
            ),
            "target_hire_end_date": format_date(
                metadata.get("target_hire_end_date")
            ),
            "updated_time": job.get("updated_at"),
            "application_deadline": format_date(
                job.get("application_deadline")
            ),

            "url": job.get("absolute_url"),

            "description_short": None,
            "description": clean_html_text(job.get("content")),
            "office": office,
        })

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df["job_id"] = df["job_id"].astype(str)

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