import re
from html import unescape

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.amazon.science/careers"
MAX_PAGES = 10

HEADERS = {
    "User-Agent": "Mozilla/5.0",
}


def clean_text(text):
    if not text:
        return None
    text = unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


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
            title = clean_text(link.get_text())
            url = link.get("href")

            if not title or not url:
                continue

            job_id_match = re.search(r"/jobs/(\d+)", url)
            job_id = job_id_match.group(1) if job_id_match else None

            container = link.find_parent("li")
            text = clean_text(container.get_text(" ")) if container else ""

            jobs.append({
                "source": "amazon_science",
                "job_id": job_id,
                "title": title,
                "location": None,
                "posted_date": format_date(text),
                "description_short": text,
                "url": url,
            })

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(subset=["job_id"], keep="first")
    df = df.sort_values("posted_date", ascending=False, na_position="last")

    return df