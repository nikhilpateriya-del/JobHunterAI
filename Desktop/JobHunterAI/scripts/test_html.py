import pandas as pd
from scripts.html_cleaner import clean_html


def test_html():

    df = pd.read_csv("output/jobs.csv")

    keyword = input("Enter job keyword: ").lower()

    jobs = df[
        df["Title"].fillna("").str.lower().str.contains(keyword)
    ]

    if len(jobs) == 0:
        print("No jobs found")
        return

    jobs = jobs.reset_index(drop=True)

    for i, row in jobs.iterrows():
        print(f"{i+1}. {row['Title']}")

    choice = int(input("Select Job Number: "))

    description = jobs.iloc[choice - 1]["Description"]

    print("=" * 80)
    print(clean_html(description))