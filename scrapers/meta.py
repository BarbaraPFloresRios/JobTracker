import re
import asyncio
from html import unescape

import pandas as pd
from playwright.async_api import async_playwright


BASE_URL = "https://www.metacareers.com"
SEARCH_URL = f"{BASE_URL}/jobsearch/"

MAX_PAGES = 5


def clean_html_text(text):
    if not text:
        return None

    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"<.*?>", "", text)
    text = unescape(text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def extract_meta_job_id(url):
    match = re.search(r"/profile/job_details/(\d+)", url)
    return match.group(1) if match else None


def build_meta_url(href):
    if not href:
        return None

    if href.startswith("http"):
        return href

    return BASE_URL + href


async def scrape_meta_async():
    jobs = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        for page_number in range(1, MAX_PAGES + 1):
            url = f"{SEARCH_URL}?page={page_number}"

            await page.goto(
                url,
                wait_until="networkidle",
                timeout=60000,
            )

            await page.wait_for_timeout(3000)

            job_links = page.locator(
                "a[href*='/profile/job_details/']"
            )

            count = await job_links.count()

            if count == 0:
                break

            print(f"Meta page {page_number}: {count} jobs")

            for i in range(count):
                link = job_links.nth(i)

                href = await link.get_attribute("href")
                text = await link.inner_text()

                if not href or not text:
                    continue

                job_url = build_meta_url(href)
                job_id = extract_meta_job_id(job_url)

                parts = [
                    part.strip()
                    for part in text.splitlines()
                    if part.strip()
                ]

                title = parts[0] if len(parts) > 0 else None
                location = parts[1] if len(parts) > 1 else None

                tags = [
                    part
                    for part in parts[2:]
                    if part != "⋅"
                    and not part.startswith("Multiple Locations")
                ]

                jobs.append({
                    "title": title,
                    "team": "; ".join(tags) if tags else None,
                    "location": location,
                    "posted_date": None,

                    "job_id": job_id,
                    "source": "meta",

                    "url": job_url,

                    "description_short": clean_html_text(text),
                    "description": None,
                })

        await browser.close()

    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(
        subset=["job_id"],
        keep="first",
    )

    return df


def scrape_meta():
    return asyncio.run(scrape_meta_async())