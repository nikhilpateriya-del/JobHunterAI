from scripts.utils import print_header
from scripts.job_api import fetch_jobs
from scripts.job_filter import filter_jobs
from scripts.job_search import search_jobs
from scripts.resume_reader import read_resume
from scripts.resume_skills import extract_resume_skills
from scripts.resume_match import resume_match
from scripts.job_details import show_jobs
from scripts.test_html import test_html
from scripts.job_skill_extractor import extract_job_skills
from scripts.ats_score import calculate_ats_score

print_header("🚀 Welcome to JobHunterAI")

print("1. Fetch Jobs")
print("2. Filter Jobs")
print("3. Search Jobs")
print("4. Read Resume")
print("5. Extract Resume Skills")
print("6. Resume Match Score")
print("7. Show Available Jobs")
print("8. Test HTML Cleaner")
print("9. Extract Job Skills")
print("10. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    fetch_jobs()

elif choice == "2":
    filter_jobs()

elif choice == "3":
    search_jobs()

elif choice == "4":
    read_resume()

elif choice == "5":
    extract_resume_skills()

elif choice == "6":
    calculate_ats_score()

elif choice == "7":
    show_jobs()

elif choice == "8":
    test_html()

elif choice == "8":
    test_html()

elif choice == "9":
    extract_job_skills()

elif choice == "10":
    print("Good Bye 👋")
else:
    print("Invalid Choice")