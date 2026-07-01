from scripts.resume_skills import extract_resume_skills
from scripts.job_skill_extractor import extract_job_skills


def calculate_ats_score():

    print("\nSelect a Job to Compare With Your Resume\n")

    resume_skills = extract_resume_skills(return_skills=True)

    job_skills = extract_job_skills(return_skills=True)

    if not job_skills:
        print("❌ No Job Skills Found.")
        return

    matched = []
    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = round((len(matched) / len(job_skills)) * 100)

    print("\n" + "=" * 60)
    print("ATS MATCH REPORT")
    print("=" * 60)

    print(f"ATS Score : {score}%")

    print("\nMatched Skills")
    print("-" * 30)

    if matched:
        for skill in matched:
            print(f"✅ {skill}")
    else:
        print("None")

    print("\nMissing Skills")
    print("-" * 30)

    if missing:
        for skill in missing:
            print(f"❌ {skill}")
    else:
        print("None")