import requests
import pandas as pd


def fetch_jobs():

    print("🚀 JobHunter AI Started...")

    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(url)

    if response.status_code != 200:
        print("❌ API Error:", response.status_code)
        return

    data = response.json()["data"]

    jobs = []

    for job in data:

        jobs.append({
            "Company": job.get("company_name"),
            "Title": job.get("title"),
            "Location": job.get("location"),
            "Remote": job.get("remote"),
            "Description": job.get("description"),
            "URL": job.get("url")
        })

    df = pd.DataFrame(jobs)

    df.to_csv("output/jobs.csv", index=False)

    print("=" * 50)
    print(f"✅ {len(df)} jobs saved successfully!")
    print("=" * 50)

    print(df.head())