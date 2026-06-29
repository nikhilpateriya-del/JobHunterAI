import pandas as pd

def filter_jobs():
    # Load jobs
    df = pd.read_csv("output/jobs.csv")

    # Keywords we want
    keywords = [
        "data analyst",
        "business analyst",
        "reporting analyst",
        "bi analyst",
        "analytics",
        "excel"
    ]

    # Filter function
    filtered = df[
        df["Title"].fillna("").str.lower().apply(
            lambda x: any(keyword in x for keyword in keywords)
        )
    ]

    # Save filtered jobs
    filtered.to_csv("output/filtered_jobs.csv", index=False)

    print("=" * 50)
    print(f"Total Jobs Found : {len(df)}")
    print(f"Filtered Jobs    : {len(filtered)}")
    print("=" * 50)

    print(filtered[["Company", "Title"]].head(10))