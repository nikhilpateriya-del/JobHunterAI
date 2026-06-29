import pandas as pd

def search_jobs():
    df = pd.read_csv("output/jobs.csv")

    keyword = input("Enter keyword: ").lower()

    result = df[
        df["Title"].fillna("").str.lower().str.contains(keyword)
    ]

    print("=" * 50)
    print(f"Jobs Found : {len(result)}")
    print("=" * 50)

    print(result[["Company", "Title"]].head(20))