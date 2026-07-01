import pandas as pd

from scripts.html_cleaner import clean_html
from scripts.skill_dictionary import SKILLS


def extract_job_skills(return_skills=False):

    df = pd.read_csv("output/jobs.csv")

    keyword = input("Enter job keyword (example: data, analyst): ").lower()

    jobs = df[
        df["Title"].fillna("").str.lower().str.contains(keyword)
    ]

    if len(jobs) == 0:
        print("❌ No matching jobs found.")
        return []

    print("=" * 60)
    print("MATCHING JOBS")
    print("=" * 60)

    jobs = jobs.reset_index(drop=True)

    for i, row in jobs.iterrows():
        print(f"{i+1}. {row['Title']}")
        print(f"   Company : {row['Company']}")
        print("-" * 60)

    choice = int(input("\nSelect Job Number: "))

    description = jobs.iloc[choice - 1]["Description"]

    text = clean_html(description).lower()

    found_skills = []

    for skill, keywords in SKILLS.items():

        for keyword in keywords:

            if keyword.lower() in text:
                found_skills.append(skill)
                break

    if return_skills:
        return found_skills

    print("\n" + "=" * 60)
    print("JOB SKILLS FOUND")
    print("=" * 60)

    if len(found_skills) == 0:
        print("❌ No skills found from dictionary.")
    else:
        for skill in found_skills:
            print(f"✅ {skill}")

    return found_skills