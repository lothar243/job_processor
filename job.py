import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("TARGET_URL", "http://google.com")
LOG_FILE = os.getenv("LOG_FILE", "/home/jeff/job_processor/job.log")

def download_page():
    response = requests.get(URL)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"/home/jeff/job_processor/pages/page_{timestamp}.html"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)

    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] Downloaded {URL} -> {file_path}\n")

if __name__ == "__main__":
    download_page()
