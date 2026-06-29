import pandas as pd

def search_jobs():
    # Load jobs
    df = pd.read_csv("output/jobs.csv")

    # User input
    keyword = input("Enter keyword: ").lower()
    remote_only = input("Show only Remote jobs? (y/n): ").lower()

    # Search by keyword
    result = df[
        df["Title"].fillna("").str.lower().str.contains(keyword)
    ]

    # Filter only remote jobs
    if remote_only == "y":
        result = result[result["Remote"] == True]

    # Show results
    print("=" * 50)
    print(f"Jobs Found : {len(result)}")
    print("=" * 50)

    if len(result) > 0:
        print(result[["Company", "Title", "Location", "Remote"]].head(20))
    else:
        print("❌ No jobs found.")