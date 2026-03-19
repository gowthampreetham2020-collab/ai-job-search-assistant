import requests
from bs4 import BeautifulSoup, soup

def get_jobs(query):

    url = "https://realpython.github.io/fake-jobs/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    results = soup.find_all("h2", class_="title")

    for job in results:
        title = job.text.strip()
        jobs.append(title)
    print(len(jobs))
    return jobs
