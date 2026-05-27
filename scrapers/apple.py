import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

BASE_URL = "https://jobs.apple.com"
SEARCH_URL = "https://jobs.apple.com/en-us/search"


def scrape_apple():

    response = requests.get(SEARCH_URL)

    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.select(".job-list-item")

    jobs = []

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

        team = team_element.get_text(strip=True) if team_element else None
        posted_date = date_element.get_text(strip=True) if date_element else None
        location = location_element.get_text(strip=True) if location_element else None

        jobs.append({
            "title": title,
            "team": team,
            "location": location,
            "posted_date": posted_date,
            "url": job_url,
        })

    df = pd.DataFrame(jobs)

    df = df.drop_duplicates(subset=["url"])

    df["posted_date_parsed"] = pd.to_datetime(
        df["posted_date"],
        errors="coerce"
    )

    one_week_ago = datetime.today() - timedelta(days=7)

    df = df[df["posted_date_parsed"] >= one_week_ago]

    df = df.drop(columns=["posted_date_parsed"])

    return df