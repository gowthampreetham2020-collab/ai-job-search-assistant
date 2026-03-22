import requests
from bs4 import BeautifulSoup

def get_jobs(query):

    url = f"https://www.naukri.com/{query}-jobs"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.select(".jobTuple")[:10]:

        title = job.select_one(".title")
        company = job.select_one(".companyInfo")

        if title and company:
            jobs.append(f"{title.text.strip()} - {company.text.strip()}")

    return jobs
