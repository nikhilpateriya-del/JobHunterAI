import fitz

def extract_skills():

    pdf_path = "resume/Nikhil CV v1.pdf"

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    text = text.lower()

    skills = [
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

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    print("=" * 50)
    print("SKILLS FOUND")
    print("=" * 50)

    if len(found) == 0:
        print("No skills found.")

    else:
        for skill in found:
            print("✅", skill.title())