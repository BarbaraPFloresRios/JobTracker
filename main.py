from src.pipeline import run_pipeline


if __name__ == "__main__":
    new_jobs = run_pipeline()

    if len(new_jobs) > 0:
        print("\nNew jobs found:")
        print(new_jobs[["title", "location", "url"]])
    else:
        print("\nNo new jobs found")