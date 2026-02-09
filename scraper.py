scraper_code = """
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "jobs.csv"

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_jobs(html):
    soup = BeautifulSoup(html, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []

    for job in job_cards:
        title = job.find("h2", class_="title")
        company = job.find("h3", class_="company")
        location = job.find("p", class_="location")
        link = job.find("a", string="Apply")

        jobs.append({
            "title": title.text.strip() if title else "N/A",
            "company": company.text.strip() if company else "N/A",
            "location": location.text.strip() if location else "N/A",
            "link": link["href"] if link else "N/A"
        })

    return jobs

def save_to_csv(jobs, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "company", "location", "link"])
        writer.writeheader()
        writer.writerows(jobs)

def main():
    html = fetch_page(URL)
    jobs = parse_jobs(html)
    save_to_csv(jobs, OUTPUT_FILE)
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
"""

with open("scraper.py", "w") as f:
    f.write(scraper_code)