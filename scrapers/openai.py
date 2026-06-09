import re
from html import unescape

import requests
import pandas as pd


SEARCH_URL = "https://api.ashbyhq.com/posting-api/job-board/openai"

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


def scrape_openai():
    jobs = []

    response = requests.get(
        SEARCH_URL,
        headers=HEADERS,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    current_jobs = [
        job
        for job in data.get("jobs", [])
        if job.get("isListed")
    ]

    if not current_jobs:
        return pd.DataFrame(jobs)

    print(f"OpenAI page 1: {len(current_jobs)} jobs")

    for job in current_jobs:
        addr = job.get(
            "address",
            {},
        ).get(
            "postalAddress",
            {},
        )

        secondary = job.get(
            "secondaryLocations",
            [],
        )

        all_locations = [job.get("location")] + [
            location.get("location")
            for location in secondary
            if location.get("location")
        ]

        all_locations = [
            location
            for location in all_locations
            if location
        ]

        jobs.append(
            {
                "title": job.get("title"),
                "team": job.get("team"),
                "location": (
                    "; ".join(all_locations)
                    if all_locations
                    else None
                ),
                "city": addr.get("addressLocality"),
                "state": addr.get("addressRegion"),
                "country": addr.get("addressCountry"),
                "posted_date": format_date(
                    job.get("publishedAt")
                ),

                "job_id": job.get("id"),
                "source": "openai",

                "department": job.get("department"),
                "employment_type": job.get(
                    "employmentType"
                ),
                "workplace_type": job.get(
                    "workplaceType"
                ),

                "url": job.get("jobUrl"),

                "description": clean_html_text(
                    job.get("descriptionHtml")
                ),
            }
        )

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