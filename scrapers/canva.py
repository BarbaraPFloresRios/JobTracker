import re
from html import unescape

import pandas as pd
import requests


SEARCH_URL = "https://api.smartrecruiters.com/v1/companies/Canva/postings"

MAX_PAGES = 5
RESULTS_PER_PAGE = 100

HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0",
}

US_COUNTRY_VALUES = {
    "us",
    "usa",
    "united states",
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


def format_date(date_value):
    date = pd.to_datetime(date_value, errors="coerce")
    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def custom_fields_to_dict(custom_fields):
    result = {}

    for item in custom_fields or []:
        label = item.get("fieldLabel")
        value = item.get("valueLabel")

        if not label:
            continue

        key = (
            label
            .lower()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("-", "_")
        )

        result[key] = value

    return result


def get_section_text(job, section_name):
    sections = (
        job
        .get("jobAd", {})
        .get("sections", {})
    )

    section = sections.get(section_name, {})

    return clean_html_text(section.get("text"))


def fetch_canva_job_detail(job_id):
    response = requests.get(
        f"{SEARCH_URL}/{job_id}",
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()

    return response.json()


def scrape_canva():
    jobs = []

    for page in range(MAX_PAGES):
        offset = page * RESULTS_PER_PAGE

        response = requests.get(
            SEARCH_URL,
            params={
                "limit": RESULTS_PER_PAGE,
                "offset": offset,
            },
            headers=HEADERS,
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()
        current_jobs = data.get("content", [])

        if not current_jobs:
            break

        print(f"Canva page {page + 1}: {len(current_jobs)} jobs")

        for job_summary in current_jobs:
            location_summary = job_summary.get("location") or {}
            country = str(location_summary.get("country", "")).lower()

            if country not in US_COUNTRY_VALUES:
                continue

            job_id = job_summary.get("id")

            if not job_id:
                continue

            try:
                job = fetch_canva_job_detail(job_id)
            except requests.exceptions.RequestException as e:
                print(f"Canva detail failed for {job_id}: {e}")
                job = job_summary

            custom_fields = custom_fields_to_dict(
                job.get("customField")
            )

            location = job.get("location") or {}
            function = job.get("function") or {}
            employment_type = job.get("typeOfEmployment") or {}
            experience_level = job.get("experienceLevel") or {}
            industry = job.get("industry") or {}
            company = job.get("company") or {}

            description_parts = [
                get_section_text(job, "companyDescription"),
                get_section_text(job, "jobDescription"),
                get_section_text(job, "qualifications"),
                get_section_text(job, "additionalInformation"),
            ]

            description = "\n\n".join(
                part for part in description_parts if part
            )

            jobs.append({
                "title": job.get("name"),
                "team": (
                    custom_fields.get("group")
                    or function.get("label")
                ),
                "location": location.get("fullLocation"),
                "city": location.get("city"),
                "state": location.get("region"),
                "posted_date": format_date(job.get("releasedDate")),

                "job_id": job.get("id"),
                "internal_job_id": job.get("jobId"),
                "requisition_id": job.get("refNumber"),
                "position_id": job.get("uuid"),
                "source": "canva",

                "management_level": custom_fields.get("role_level"),
                "job_profile": custom_fields.get("subspecialty"),
                "job_category": function.get("label"),
                "job_family": custom_fields.get("specialty"),

                "worker_type": custom_fields.get("worker_type"),
                "worker_sub_type": custom_fields.get(
                    "contingent_worker_type"
                ),
                "schedule_type": employment_type.get("label"),
                "time_type": employment_type.get("label"),

                "company_name": company.get("name"),
                "cost_center": custom_fields.get("org"),
                "office": custom_fields.get("supergroup"),

                "country": custom_fields.get("country_region"),
                "brand": custom_fields.get("brands"),
                "industry": industry.get("label"),
                "experience_level": experience_level.get("label"),
                "remote": location.get("remote"),
                "hybrid": location.get("hybrid"),

                "url": (
                    job.get("postingUrl")
                    or job.get("applyUrl")
                    or job.get("ref")
                ),

                "description_short": None,
                "description": description,
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