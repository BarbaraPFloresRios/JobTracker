import requests
import pandas as pd

BASE_URL = "https://www.amazon.jobs"
SEARCH_URL = "https://www.amazon.jobs/en/search.json"

HEADERS = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0",
}


def scrape_amazon():
    jobs = []

    for offset in range(0, 50, 10):  # first 5 pages
        params = {
            "country": "USA",
            "sort": "recent",
            "offset": offset,
            "result_limit": 10,
        }

        response = requests.get(SEARCH_URL, params=params, headers=HEADERS)
        response.raise_for_status()

        data = response.json()

        for job in data.get("jobs", []):
            job_path = job.get("job_path")

            if not job_path:
                continue

            jobs.append({
                "title": job.get("title"),
                "team": job.get("business_category"),
                "job_category": job.get("job_category"),
                "location": job.get("location"),
                "posted_date": job.get("posted_date"),
                "description": job.get("description_short"),
                "url": BASE_URL + job_path,
                "source": "amazon",
            })

    df = pd.DataFrame(jobs)

    df = df.drop_duplicates(subset=["url"])

    return df