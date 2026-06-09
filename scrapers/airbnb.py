import re
from html import unescape
import time

import requests
import pandas as pd
from bs4 import BeautifulSoup


BASE_URL = "https://careers.airbnb.com"
POSITIONS_URL = f"{BASE_URL}/positions/"

MAX_PAGES = 2
SLEEP_SECONDS = 1
REQUEST_TIMEOUT = 30

HEADERS = {
    "User-Agent": "Mozilla/5.0",
}


def clean_html_text(text):
    if not text:
        return None

    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = unescape(text)

    return text.strip()


def extract_airbnb_job_id(url):
    match = re.search(r"/positions/(\d+)/", url)
    return match.group(1) if match else None


def parse_listing_card(card):
    text = card.get_text(" ", strip=True)

    title_element = card.find("a", href=True)
    if not title_element:
        return None

    url = title_element["href"]
    if url.startswith("/"):
        url = BASE_URL + url

    job_id = extract_airbnb_job_id(url)

    parts = text.split(" • ", 1)
    team = parts[0].strip() if len(parts) > 1 else None

    remainder = parts[1].strip() if len(parts) > 1 else text

    workplace_type = None
    for value in [
        "Live and Work Anywhere",
        "Hybrid - Be close to an office",
        "Onsite",
    ]:
        if remainder.startswith(value):
            workplace_type = value
            remainder = remainder.replace(value, "", 1).strip()
            break

    title = title_element.get_text(" ", strip=True)
    location = remainder.replace(title, "", 1).strip() or None

    return {
        "title": title,
        "team": team,
        "location": location,
        "job_id": job_id,
        "source": "airbnb",
        "workplace_type": workplace_type,
        "url": url,
    }


def fetch_airbnb_job_detail(url):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    detail = soup.find("div", class_="job-detail active")
    description = (
        detail.get_text("\n", strip=True)
        if detail
        else None
    )

    office = None
    if detail:
        for paragraph in detail.find_all("p"):
            text = paragraph.get_text(" ", strip=True)
            if text.startswith("Offices:"):
                office = text.replace("Offices:", "", 1).strip()
                break

    return {
        "description": clean_html_text(description),
        "office": office,
    }


def scrape_airbnb():
    jobs = []

    for page in range(1, MAX_PAGES + 1):
        url = (
            POSITIONS_URL
            if page == 1
            else f"{POSITIONS_URL}page/{page}/"
        )

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        current_jobs = soup.select("ul.job-list li")

        if not current_jobs:
            break

        print(f"Airbnb page {page}: {len(current_jobs)} jobs")

        for card in current_jobs:
            job = parse_listing_card(card)

            if not job or not job.get("job_id"):
                continue

            try:
                detail = fetch_airbnb_job_detail(job["url"])
            except Exception as e:
                print(f"Airbnb detail failed for {job['url']}: {e}")
                detail = {}

            jobs.append({
                "title": job.get("title"),
                "team": job.get("team"),
                "location": job.get("location"),
                "posted_date": None,
                "job_id": job.get("job_id"),
                "source": "airbnb",

                "workplace_type": job.get("workplace_type"),
                "office": detail.get("office"),

                "url": job.get("url"),
                "description_short": None,
                "description": detail.get("description"),
            })

            time.sleep(SLEEP_SECONDS)

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(subset=["job_id"], keep="first")
    df = df.sort_values("job_id", ascending=False, na_position="last")

    return df