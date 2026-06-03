import re
import asyncio
from html import unescape

import pandas as pd
from playwright.async_api import async_playwright


BASE_URL = "https://www.metacareers.com"
JOBS_URL = f"{BASE_URL}/jobs/"

MAX_PAGES = 5
RESULTS_PER_PAGE = 20

US_KEYWORDS = [
    ", CA", ", NY", ", WA", ", TX", ", MA", ", IL", ", GA",
    ", CO", ", VA", ", FL", ", OR", ", AZ", ", NC", ", NJ",
    "Remote, US", "United States",
]


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
    if not date_value:
        return None

    date = pd.to_datetime(date_value, unit="s", errors="coerce")

    if pd.isna(date):
        date = pd.to_datetime(date_value, errors="coerce")

    return date.strftime("%Y-%m-%d") if pd.notna(date) else None


def is_us_job(locations):
    if not locations:
        return False

    return any(kw in loc for loc in locations for kw in US_KEYWORDS)


async def scrape_meta_async():
    all_jobs = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        async def handle_response(response):
            if "graphql" not in response.url:
                return

            try:
                friendly = response.request.headers.get("x-fb-friendly-name", "")

                if "CareersJobSearchResultsDataQuery" not in friendly:
                    return

                body = await response.json()
                page_jobs = (
                    body.get("data", {})
                    .get("job_search_with_featured_jobs", {})
                    .get("all_jobs", [])
                )

                if page_jobs:
                    all_jobs.extend(page_jobs)

            except Exception:
                pass

        page.on("response", handle_response)

        for i in range(MAX_PAGES):
            if i == 0:
                await page.goto(JOBS_URL, wait_until="networkidle")
                await page.wait_for_timeout(3000)
                print(f"Meta page 1: {len(all_jobs)} jobs")
            else:
                try:
                    btn = page.get_by_role("button", name="Load more jobs")
                    await btn.wait_for(timeout=5000)
                    await btn.click()
                    await page.wait_for_timeout(3000)
                    print(f"Meta page {i + 1}: {len(all_jobs)} jobs")
                except Exception:
                    break

        await browser.close()

    jobs = []
    seen = set()

    for job in all_jobs:
        job_id = str(job.get("id", ""))

        if not job_id or job_id in seen:
            continue

        seen.add(job_id)

        locations = job.get("locations", [])

        if not is_us_job(locations):
            continue

        teams = job.get("teams", [])
        sub_teams = job.get("sub_teams", [])

        jobs.append({
            "title": job.get("title"),
            "team": "; ".join(teams) if teams else None,
            "location": "; ".join(locations) if locations else None,
            "posted_date": format_date(
                job.get("created_time") or job.get("updated_time")
            ),

            "job_id": job_id,
            "source": "meta",

            "sub_team": "; ".join(sub_teams) if sub_teams else None,

            "url": f"{BASE_URL}/jobs/{job_id}/",

            "description": clean_html_text(job.get("description")),
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


def scrape_meta():
    return asyncio.run(scrape_meta_async())