import os
import pandas as pd

from src.recent_jobs import build_recent_jobs
from src.generate_readme import generate_readme
from scrapers.mercadolibre import scrape_mercadolibre
from src.scoring import add_semantic_scores
from scrapers.apple import scrape_apple
from scrapers.amazon import scrape_amazon
from scrapers.amazon_science import scrape_amazon_science
from scrapers.nvidia import scrape_nvidia
from scrapers.microsoft import scrape_microsoft
from scrapers.netflix import scrape_netflix
from scrapers.openai import scrape_openai
from scrapers.anthropic import scrape_anthropic
from scrapers.meta import scrape_meta
from scrapers.duolingo import scrape_duolingo
from scrapers.spotify import scrape_spotify
from scrapers.reddit import scrape_reddit
from scrapers.discord import scrape_discord
from scrapers.canva import scrape_canva
from scrapers.uber import scrape_uber
from scrapers.airbnb import scrape_airbnb



RAW_DATA_DIR = "data/raw"

MERCADOLIBRE_OUTPUT_PATH = f"{RAW_DATA_DIR}/mercadolibre_jobs.csv"
APPLE_OUTPUT_PATH = f"{RAW_DATA_DIR}/apple_jobs.csv"
AMAZON_OUTPUT_PATH = f"{RAW_DATA_DIR}/amazon_jobs.csv"
AMAZON_SCIENCE_OUTPUT_PATH = f"{RAW_DATA_DIR}/amazon_science_jobs.csv"
NVIDIA_OUTPUT_PATH = f"{RAW_DATA_DIR}/nvidia_jobs.csv"
MICROSOFT_OUTPUT_PATH = f"{RAW_DATA_DIR}/microsoft_jobs.csv"
NETFLIX_OUTPUT_PATH = f"{RAW_DATA_DIR}/netflix_jobs.csv"
META_OUTPUT_PATH = f"{RAW_DATA_DIR}/meta_jobs.csv"
OPENAI_OUTPUT_PATH = f"{RAW_DATA_DIR}/openai_jobs.csv"
ANTHROPIC_OUTPUT_PATH = f"{RAW_DATA_DIR}/anthropic_jobs.csv"
DUOLINGO_OUTPUT_PATH = f"{RAW_DATA_DIR}/duolingo_jobs.csv"
SPOTIFY_OUTPUT_PATH = f"{RAW_DATA_DIR}/spotify_jobs.csv"
REDDIT_OUTPUT_PATH = f"{RAW_DATA_DIR}/reddit_jobs.csv"
DISCORD_OUTPUT_PATH = f"{RAW_DATA_DIR}/discord_jobs.csv"
CANVA_OUTPUT_PATH = f"{RAW_DATA_DIR}/canva_jobs.csv"
UBER_OUTPUT_PATH = f"{RAW_DATA_DIR}/uber_jobs.csv"
AIRBNB_OUTPUT_PATH = f"{RAW_DATA_DIR}/airbnb_jobs.csv"


def normalize_key(series):
    return (
        series
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)
        .str.strip()
    )


def print_section(title):
    width = 80
    print(f"\n{'═' * width}")
    print(f"SCRAPING {title.upper()}")
    print(f"{'═' * width}")


def print_phase(title):
    width = 80
    print(f"\n{'#' * width}")
    print(f"  {title.upper()}")
    print(f"{'#' * width}")


def save_jobs(current_jobs, output_path, company=""):

    width = 80
    print(f"\n{'═' * width}")
    print(f"RESULTS {company.upper()}")
    print(f"{'═' * width}")

    today = pd.Timestamp.today().strftime("%Y-%m-%d")

    dedupe_key = "job_id" if "job_id" in current_jobs.columns else "url"

    current_jobs = current_jobs.copy()
    current_jobs[dedupe_key] = normalize_key(current_jobs[dedupe_key])
    current_jobs["last_seen_date"] = today

    if os.path.exists(output_path):
        old_jobs = pd.read_csv(output_path)

        if "position_id" in old_jobs.columns:
            old_jobs["position_id"] = (
                old_jobs["position_id"]
                .astype(str)
                .str.replace(r"\.0$", "", regex=True)
            )

        if dedupe_key in old_jobs.columns:
            old_jobs[dedupe_key] = normalize_key(old_jobs[dedupe_key])
        else:
            old_jobs[dedupe_key] = None

        if "first_seen_date" not in old_jobs.columns:
            old_jobs["first_seen_date"] = today

        if "last_seen_date" not in old_jobs.columns:
            old_jobs["last_seen_date"] = today

        old_keys = old_jobs[dedupe_key]

        new_jobs = current_jobs[
            ~current_jobs[dedupe_key].isin(old_keys)
        ].copy()

        old_jobs = old_jobs.drop_duplicates(
            subset=[dedupe_key],
            keep="last",
        )

        current_jobs["first_seen_date"] = current_jobs[dedupe_key].map(
            old_jobs.set_index(dedupe_key)["first_seen_date"]
        )

        current_jobs["first_seen_date"] = (
            current_jobs["first_seen_date"]
            .fillna(today)
        )

        jobs = pd.concat(
            [old_jobs, current_jobs],
            ignore_index=True,
        )

        jobs = jobs.drop_duplicates(
            subset=[dedupe_key],
            keep="last",
        )

    else:
        current_jobs["first_seen_date"] = today
        new_jobs = current_jobs
        jobs = current_jobs

    if "posted_date" in jobs.columns:
        jobs["posted_date_sort"] = pd.to_datetime(
            jobs["posted_date"],
            errors="coerce",
        )

        jobs = (
            jobs
            .sort_values(
                by=["posted_date_sort", "last_seen_date"],
                ascending=[False, False],
            )
            .drop(columns=["posted_date_sort"])
        )

    jobs = add_semantic_scores(jobs)

    preferred_order = [
        "title",
        "team",
        "location",
        "city",
        "state",
        "posted_date",
        "job_id",
        "internal_job_id",
        "requisition_id",
        "position_id",
        "source",
        "first_seen_date",
        "last_seen_date",
        "semantic_similarity",
        "management_level",
        "job_profile",
        "job_category",
        "job_family",
        "worker_type",
        "worker_sub_type",
        "schedule_type",
        "time_type",
        "pay_rate_type",
        "scheduled_weekly_hours",
        "company_name",
        "education",
        "cost_center",
        "office",
        "country",
        "brand",
        "industry",
        "experience_level",
        "remote",
        "hybrid",
        "recruiting_start_date",
        "target_hire_date",
        "target_hire_end_date",
        "application_deadline",
        "updated_time",
        "url",
        "description_short",
        "basic_qualifications",
        "preferred_qualifications",
        "description",
    ]

    existing_cols = [c for c in preferred_order if c in jobs.columns]
    remaining_cols = [c for c in jobs.columns if c not in preferred_order]

    jobs = jobs[existing_cols + remaining_cols]

    if "position_id" in jobs.columns:
        jobs["position_id"] = (
            jobs["position_id"]
            .astype(str)
            .str.replace(r"\.0$", "", regex=True)
        )

    jobs.to_csv(output_path, index=False)

    print(f"\nFound {len(current_jobs)} current jobs")
    print(f"Found {len(new_jobs)} truly new jobs")

    if len(new_jobs) > 0:
        print("\nNew jobs:")

        for _, job in new_jobs.iterrows():
            title = job.get("title", "No title")
            url = job.get("url", "")

            print(f"\n- {title}")

            if url:
                print(f"  {url}")

    print(f"\nSaved {len(jobs)} total jobs to {output_path}")

    return new_jobs


def run_pipeline():

    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    scrapers = [
        ("MercadoLibre", scrape_mercadolibre, MERCADOLIBRE_OUTPUT_PATH),
        ("Apple", scrape_apple, APPLE_OUTPUT_PATH),
        ("Amazon", scrape_amazon, AMAZON_OUTPUT_PATH),
        ("Amazon Science", scrape_amazon_science, AMAZON_SCIENCE_OUTPUT_PATH),
        ("NVIDIA", scrape_nvidia, NVIDIA_OUTPUT_PATH),
        ("Microsoft", scrape_microsoft, MICROSOFT_OUTPUT_PATH),
        ("Netflix", scrape_netflix, NETFLIX_OUTPUT_PATH),
        ("Meta", scrape_meta, META_OUTPUT_PATH),
        ("OpenAI", scrape_openai, OPENAI_OUTPUT_PATH),
        ("Anthropic", scrape_anthropic, ANTHROPIC_OUTPUT_PATH),
        ("Duolingo", scrape_duolingo, DUOLINGO_OUTPUT_PATH),
        ("Spotify", scrape_spotify, SPOTIFY_OUTPUT_PATH),
        ("Reddit", scrape_reddit, REDDIT_OUTPUT_PATH),
        ("Discord", scrape_discord, DISCORD_OUTPUT_PATH),
        ("Canva", scrape_canva, CANVA_OUTPUT_PATH),
        ("Uber", scrape_uber, UBER_OUTPUT_PATH),
        ("Airbnb", scrape_airbnb, AIRBNB_OUTPUT_PATH),
    ]

    scraped_jobs = []

    for company, scraper, output_path in scrapers:
        print_section(company)
        jobs = scraper()
        scraped_jobs.append((company, jobs, output_path))

    print_phase("Processing results")

    for company, jobs, output_path in scraped_jobs:
        save_jobs(jobs, output_path, company)

    print_phase("Exporting recent jobs")

    recent_jobs = build_recent_jobs()
    recent_jobs.to_csv("data/recent_jobs.csv", index=False)

    print(f"Saved {len(recent_jobs)} recent jobs to data/recent_jobs.csv")
    print_phase("Updating README")

    generate_readme()
    print("Updated README.md")