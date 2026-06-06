import re
from html import unescape

import requests
import pandas as pd


BASE_URL = "https://api.lever.co/v0/postings/spotify"

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


def format_date(timestamp_ms):
    if not timestamp_ms:
        return None
    date = pd.to_datetime(timestamp_ms, unit="ms", errors="coerce")
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def extract_lists(lists):
    if not lists:
        return None
    parts = []
    for section in lists:
        title = section.get("text", "")
        content = clean_html_text(section.get("content", ""))
        if title and content:
            parts.append(f"{title}:\n{content}")
    return "\n\n".join(parts) if parts else None


def scrape_spotify():
    response = requests.get(
        BASE_URL,
        params={"mode": "json"},
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()

    jobs_data = response.json()
    print(f"Spotify: {len(jobs_data)} jobs")

    jobs = []
    for job in jobs_data:
        categories = job.get("categories", {})
        all_locations = categories.get("allLocations", [])

        jobs.append({
            "title": job.get("text"),
            "team": categories.get("team"),
            "location": "; ".join(all_locations) if all_locations else categories.get("location"),
            "posted_date": format_date(job.get("createdAt")),

            "job_id": job.get("id"),
            "source": "spotify",

            "department": categories.get("department"),
            "commitment": categories.get("commitment"),
            "workplace_type": job.get("workplaceType"),
            "country": job.get("country"),

            "url": job.get("hostedUrl"),

            "description": clean_html_text(job.get("description")),
            "description_body": clean_html_text(job.get("descriptionBody")),
            "additional": clean_html_text(job.get("additionalPlain")),
            "lists": extract_lists(job.get("lists")),
        })

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(subset=["job_id"], keep="first")
    df = df.sort_values("posted_date", ascending=False, na_position="last")

    return df
