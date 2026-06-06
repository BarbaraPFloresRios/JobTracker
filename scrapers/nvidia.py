import re
from html import unescape

import pandas as pd
import requests


BASE_URL = "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite"
SEARCH_URL = "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs"

MAX_PAGES = 5
RESULTS_PER_PAGE = 20

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Origin": "https://nvidia.wd5.myworkdayjobs.com",
    "Referer": BASE_URL,
}

US_LOCATION_ID = "2fcb99c455831013ea52fb338f2932d8"


def clean_html_text(text):
    if not text:
        return None

    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\s+", " ", text)

    return unescape(text).strip()


def fetch_nvidia_job_detail(external_path):
    detail_url = (
        "https://nvidia.wd5.myworkdayjobs.com"
        "/wday/cxs/nvidia/NVIDIAExternalCareerSite"
        + external_path
    )

    response = requests.get(
        detail_url,
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()

    return response.json().get("jobPostingInfo", {})


def extract_nvidia_job_id(job):
    bullet_fields = job.get("bulletFields", [])

    if bullet_fields:
        return bullet_fields[0]

    external_path = job.get("externalPath", "")
    match = re.search(r"_(JR\d+)", external_path)

    return match.group(1) if match else None


def format_posted_date(posted_on):
    if not posted_on:
        return None

    today = pd.Timestamp.today().normalize()

    if posted_on == "Posted Today":
        return today.strftime("%Y-%m-%d")

    if posted_on == "Posted Yesterday":
        return (
            today - pd.Timedelta(days=1)
        ).strftime("%Y-%m-%d")

    match = re.search(
        r"Posted (\d+) Days Ago",
        posted_on,
    )

    if match:
        days_ago = int(match.group(1))

        return (
            today - pd.Timedelta(days=days_ago)
        ).strftime("%Y-%m-%d")

    return None


def scrape_nvidia():
    jobs = []

    for page in range(MAX_PAGES):
        offset = page * RESULTS_PER_PAGE

        payload = {
            "appliedFacets": {
                "locationHierarchy1": [US_LOCATION_ID]
            },
            "limit": RESULTS_PER_PAGE,
            "offset": offset,
            "searchText": "",
        }

        response = requests.post(
            SEARCH_URL,
            json=payload,
            headers=HEADERS,
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()
        current_jobs = data.get("jobPostings", [])

        if not current_jobs:
            break

        print(
            f"NVIDIA page {page + 1}: "
            f"{len(current_jobs)} jobs"
        )

        for job in current_jobs:
            external_path = job.get("externalPath")

            if not external_path:
                continue

            try:
                detail = fetch_nvidia_job_detail(
                    external_path
                )
            except Exception:
                detail = {}

            job_id = (
                detail.get("jobReqId")
                or extract_nvidia_job_id(job)
            )

            additional_locations = detail.get(
                "additionalLocations",
                [],
            )

            location = (
                detail.get("location")
                or job.get("locationsText")
            )

            if additional_locations:
                location = "; ".join(
                    [
                        loc
                        for loc in [location]
                        + additional_locations
                        if loc
                    ]
                )

            jobs.append(
                {
                    "title": (
                        detail.get("title")
                        or job.get("title")
                    ),
                    "location": location,
                    "posted_date": format_posted_date(
                        detail.get("postedOn")
                        or job.get("postedOn")
                    ),
                    "job_id": job_id,
                    "source": "nvidia",
                    "schedule_type": detail.get(
                        "timeType"
                    ),
                    "url": (
                        detail.get("externalUrl")
                        or BASE_URL + external_path
                    ),
                    "description_short": None,
                    "description": clean_html_text(
                        detail.get("jobDescription")
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