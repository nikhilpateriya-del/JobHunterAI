import pandas as pd

def show_jobs():

    df = pd.read_csv("output/jobs.csv")

    print("=" * 80)
    print("AVAILABLE JOBS")
    print("=" * 80)

    jobs = df[["Company", "Title", "Location"]].head(20)

    for i, row in jobs.iterrows():
        print(f"{i+1}. {row['Title']}")
        print(f"   Company : {row['Company']}")
        print(f"   Location: {row['Location']}")
        print("-" * 80)

    choice = input("Select Job Number: ")

    try:
        choice = int(choice)

        selected = jobs.iloc[choice - 1]

        print("\n")
        print("=" * 80)
        print("SELECTED JOB")
        print("=" * 80)

        print("Title    :", selected["Title"])
        print("Company  :", selected["Company"])
        print("Location :", selected["Location"])

    except:
        print("Invalid Selection")