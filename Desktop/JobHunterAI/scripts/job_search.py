print("Program Started")import requests
import pandas as pd
from bs4 import BeautifulSoup

print("=" * 50)
print("       JOBHUNTER AI v1.0")
print("=" * 50)

url = "https://remoteok.com/remote-data+analyst-jobs"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Website Status:", response.status_code)

if response.status_code == 200:
    print("Connection Successful")
else:
    print("Connection Failed")
    