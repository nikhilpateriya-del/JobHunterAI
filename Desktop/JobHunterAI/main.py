from scripts.utils import print_header
from scripts.job_api import fetch_jobs
from scripts.job_filter import filter_jobs
from scripts.job_search import search_jobs
from scripts.resume_reader import read_resume

print_header("🚀 Welcome to JobHunterAI")

print("1. Fetch Jobs")
print("2. Filter Jobs")
print("3. Search Jobs")
print("4. Read Resume")
print("5. Exit")

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
    print("Good Bye 👋")

else:
    print("Invalid Choice")