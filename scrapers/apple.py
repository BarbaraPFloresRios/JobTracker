import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://jobs.apple.com"
SEARCH_URL = "https://jobs.apple.com/en-us/search?location=united-states-USA"
MAX_PAGES = 5  # Covers the latest ~300 postings per run


def extract_apple_job_id(url):
    match = re.search(r"/details/(\d+)", url)
    return match.group(1) if match else None


def scrape_apple():

    jobs = []
    page = 1
    while page <= MAX_PAGES:
        url = f"{SEARCH_URL}&page={page}"

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.select(".job-list-item")

        if not job_cards:
            break

        print(f"Apple page {page}: {len(job_cards)} jobs")

        for card in job_cards:
            title_element = card.select_one("h3 a")

            if not title_element:
                continue

            team_element = card.select_one(".team-name")
            date_element = card.select_one(".job-posted-date")
            location_element = card.select_one(".table--advanced-search__location-sub")

            title = title_element.get_text(strip=True)
            relative_url = title_element["href"]
            job_url = BASE_URL + relative_url

            job_id = extract_apple_job_id(job_url)

            team = (
                team_element.get_text(strip=True)
                if team_element
                else None
            )

            posted_date_raw = (
                date_element.get_text(strip=True)
                if date_element
                else None
            )

            posted_date = pd.to_datetime(
                posted_date_raw,
                errors="coerce"
            )

            posted_date = (
                posted_date.strftime("%Y-%m-%d")
                if pd.notna(posted_date)
                else None
            )

            location = (
                location_element.get_text(strip=True)
                if location_element
                else None
            )

            jobs.append({
                "source": "apple",
                "job_id": job_id,
                "title": title,
                "team": team,
                "location": location,
                "posted_date": posted_date,
                "url": job_url,
            })

        page += 1


    df = pd.DataFrame(jobs)

    if df.empty:
        return df

    df = df.drop_duplicates(
        subset=["job_id"],
        keep="first"
    )

    df["posted_date"] = pd.to_datetime(
        df["posted_date"],
        errors="coerce"
    )

    one_week_ago = pd.Timestamp.today() - pd.Timedelta(days=7)

    df = df[df["posted_date"] >= one_week_ago]

    df = df.sort_values(
        "posted_date",
        ascending=False
    )

    df["posted_date"] = df["posted_date"].dt.strftime("%Y-%m-%d")

    return df