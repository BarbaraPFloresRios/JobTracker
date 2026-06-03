import re
from html import unescape
import time

import requests
import pandas as pd


BASE_URL = "https://apply.careers.microsoft.com"
SEARCH_URL = f"{BASE_URL}/api/pcsx/search"
DETAIL_URL = f"{BASE_URL}/api/pcsx/position_details"

MAX_PAGES = 2
RESULTS_PER_PAGE = 10
SLEEP_SECONDS = 5
MAX_RETRIES = 3
REQUEST_TIMEOUT = 30  # seconds

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


def format_date(timestamp):
    date = pd.to_datetime(timestamp, unit="s", errors="coerce")
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def join_list(values):
    if not values:
        return None
    return "; ".join(values)


def fetch_with_retry(url, params):
    """GET request with timeout, retry, and exponential back-off on 429."""
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(
                url,
                params=params,
                headers=HEADERS,
                timeout=REQUEST_TIMEOUT,
            )
        except requests.exceptions.Timeout:
            wait = SLEEP_SECONDS * (2 ** attempt)
            print(f"Timeout on attempt {attempt + 1}, retrying in {wait}s…")
            time.sleep(wait)
            continue

        if response.status_code == 429:
            wait = SLEEP_SECONDS * (2 ** attempt)
            print(f"Rate limited, waiting {wait}s before retry…")
            time.sleep(wait)
            continue

        response.raise_for_status()
        return response

    return None  # all retries exhausted


def fetch_microsoft_job_detail(position_id):
    params = {
        "position_id": str(position_id).replace(".0", ""),
        "domain": "microsoft.com",
        "hl": "en",
    }
    response = fetch_with_retry(DETAIL_URL, params)
    if response is None:
        print(f"Microsoft detail failed after {MAX_RETRIES} retries for {position_id}")
        return {}
    return response.json().get("data", {})


def scrape_microsoft():
    jobs = []

    for page in range(MAX_PAGES):
        start = page * RESULTS_PER_PAGE

        params = {
            "domain": "microsoft.com",
            "query": "",
            "location": "United States",
            "start": start,
        }

        response = fetch_with_retry(SEARCH_URL, params)
        if response is None:
            print(f"Microsoft search failed on page {page + 1}, stopping.")
            break

        data = response.json()
        current_jobs = data.get("data", {}).get("positions", [])

        if not current_jobs:
            break

        print(f"Microsoft page {page + 1}: {len(current_jobs)} jobs")

        for job in current_jobs:
            position_id = job.get("id")
            if not position_id:
                continue

            try:
                detail = fetch_microsoft_job_detail(position_id)
            except requests.exceptions.RequestException as e:
                print(f"Microsoft detail failed for {position_id}: {e}")
                detail = {}
            finally:
                time.sleep(SLEEP_SECONDS)

            jobs.append({
                "title": detail.get("name") or job.get("name"),
                "team": detail.get("department") or job.get("department"),
                "location": join_list(detail.get("locations") or job.get("locations")),
                "posted_date": format_date(detail.get("postedTs") or job.get("postedTs")),
                "job_id": detail.get("displayJobId") or job.get("displayJobId"),
                "position_id": position_id,
                "source": "microsoft",
                "job_category": join_list(detail.get("efcustomTextCurrentProfession")),
                "job_family": join_list(detail.get("efcustomTextTaDisciplineName")),
                "schedule_type": join_list(detail.get("efcustomTextEmploymentType")),
                "work_location_option": detail.get("workLocationOption"),
                "role_type": join_list(detail.get("efcustomTextRoletype")),
                "required_travel": join_list(detail.get("efcustomTextRequiredTravel")),
                "url": detail.get("publicUrl") or BASE_URL + job.get("positionUrl", ""),
                "description_short": clean_html_text(job.get("name")),
                "description": clean_html_text(detail.get("jobDescription")),
            })

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(subset=["job_id"], keep="first")
    df = df.sort_values("posted_date", ascending=False, na_position="last")

    return df