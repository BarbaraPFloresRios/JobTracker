import re
from html import unescape

import pandas as pd
import requests


SEARCH_URL = "https://boards-api.greenhouse.io/v1/boards/anthropic/jobs?content=true"

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0",
}


def clean_html_text(text):
    if not text:
        return None

    text = unescape(text)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def format_date(date_value):
    date = pd.to_datetime(date_value, errors="coerce")
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def join_names(items):
    if not items:
        return None

    names = [item.get("name") for item in items if item.get("name")]
    return "; ".join(names) if names else None


def get_metadata_value(metadata, name):
    if not metadata:
        return None

    for item in metadata:
        if item.get("name") == name:
            return item.get("value")

    return None


def scrape_anthropic():
    try:
        response = requests.get(
            SEARCH_URL,
            headers=HEADERS,
            timeout=30,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Anthropic scraper failed: {e}")
        return pd.DataFrame()

    data = response.json()
    jobs = data.get("jobs", [])

    results = []

    for job in jobs:
        metadata = job.get("metadata", [])

        workplace_type = get_metadata_value(
            metadata,
            "Workplace Type",
        )

        results.append({
            "title": job.get("title"),
            "team": join_names(job.get("departments")),
            "location": join_names(job.get("offices")),
            "posted_date": format_date(job.get("updated_at")),

            "job_id": job.get("id"),
            "source": "anthropic",

            "worker_type": get_metadata_value(
                metadata,
                "Employment Type",
            ),

            "remote": workplace_type == "Remote",
            "hybrid": workplace_type == "Hybrid",

            "url": job.get("absolute_url"),

            "description_short": None,
            "description": clean_html_text(job.get("content")),
        })

    print(f"Found {len(results)} Anthropic jobs")

    df = pd.DataFrame(results)

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