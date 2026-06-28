from scripts.utils import print_header

print_header("🚀 Welcome to JobHunterAI")

print("1. Fetch Jobs")
print("2. Filter Jobs")
print("3. Exit")

choice = input("\nEnter your choice: ")
if choice == "1":
    print("Fetching Jobs...")

elif choice == "2":
    print("Filtering Jobs...")

elif choice == "3":
    print("Good Bye 👋")

else:
    print("Invalid Choice")