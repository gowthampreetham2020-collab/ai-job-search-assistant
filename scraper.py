<<<<<<< HEAD
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
=======
import requests
from bs4 import BeautifulSoup

def get_jobs(query):

    url = "https://realpython.github.io/fake-jobs/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    results = soup.find_all("h2", class_="title")

    for job in results:
        title = job.text.strip()
        jobs.append(title)

    return jobs
>>>>>>> 9cbb982e6eaffc57e8bcc5b4c55b9b0086286193
