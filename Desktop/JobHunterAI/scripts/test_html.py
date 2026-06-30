import pandas as pd
from scripts.html_cleaner import clean_html


def test_html():

    df = pd.read_csv("output/jobs.csv")

    description = df.iloc[0]["Description"]

    clean_text = clean_html(description)

    print("=" * 80)
    print("CLEAN JOB DESCRIPTION")
    print("=" * 80)

    print(clean_text[:2000])