import fitz

def resume_match():

    pdf_path = "resume/Nikhil CV v1.pdf"

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    text = text.lower()

    # Skills present in Resume
    resume_skills = [
        "excel",
        "power bi",
        "sql",
        "python",
        "tableau",
        "pandas",
        "numpy",
        "dashboard",
        "data analysis",
        "business analysis",
        "vba",
        "power query",
        "google sheets",
        "statistics",
        "mysql"
    ]

    # Sample Job Skills
    job_skills = [
        "excel",
        "sql",
        "power bi",
        "dashboard",
        "python"
    ]

    matched = []
    missing = []

    for skill in job_skills:

        if skill in text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(job_skills)) * 100)

    print("=" * 50)
    print("RESUME MATCH REPORT")
    print("=" * 50)

    print(f"Match Score : {score}%")

    print("\nMatched Skills")
    print("-" * 20)

    if matched:
        for skill in matched:
            print("✅", skill.title())
    else:
        print("No matched skills")

    print("\nMissing Skills")
    print("-" * 20)

    if missing:
        for skill in missing:
            print("❌", skill.title())
    else:
        print("None")