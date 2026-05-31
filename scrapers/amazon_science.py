import re
from html import unescape

import requests
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://www.amazon.science/careers"

MAX_PAGES = 10

HEADERS = {
    "User-Agent": "Mozilla/5.0",
}


def clean_html_text(text):
    if not text:
        return None

    text = unescape(text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_amazon_job_id(job_path):
    match = re.search(r"/jobs/(\d+)", job_path)
    return match.group(1) if match else None

def extract_location(text):
    if not text:
        return None

    match = re.search(
        r"\b(US,\s*[A-Z]{2},\s*.+?|IN,\s*[A-Z]{2},\s*.+?|IT,\s*.+?|GB,\s*.+?|IL,\s*.+?)\s+Job ID:",
        text,
    )

    if match:
        return match.group(1).strip()

    match = re.search(
        r"Job Location:\s*([^\.]+)",
        text,
    )

    if match:
        return match.group(1).strip()

    return None


def format_date(text):
    if not text:
        return None

    match = re.search(r"Posted ([A-Za-z]+ \d{1,2}, \d{4})", text)

    if not match:
        return None

    date = pd.to_datetime(match.group(1), errors="coerce")
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def scrape_amazon_science():
    jobs = []

    for page in range(1, MAX_PAGES + 1):
        response = requests.get(
            BASE_URL,
            params={"p": page},
            headers=HEADERS,
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        job_links = soup.select('a[href*="amazon.jobs/jobs/"]')

        if not job_links:
            break

        print(f"Amazon Science page {page}: {len(job_links)} jobs")

        for link in job_links:
            title = clean_html_text(link.get_text())
            job_path = link.get("href")

            if not title or not job_path:
                continue

            job_id = extract_amazon_job_id(job_path)

            container = link.find_parent("li")
            description_short = (
                clean_html_text(container.get_text(" "))
                if container
                else None
            )

            jobs.append({

                "title": title,
                "location": extract_location(description_short),
                "posted_date": format_date(description_short),

                "job_id": job_id,
                "source": "amazon_science",

                "url": job_path,

                "description_short": description_short,

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