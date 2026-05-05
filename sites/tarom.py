import requests
from bs4 import BeautifulSoup

from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url = "https://www.tarom.ro/despre-noi/compania-tarom/cariere"
company = "Tarom"
response = requests.get(url)
scraper = BeautifulSoup(response.text, "html.parser")

jobs = []

city_aliases = {
    "bucuresti": "Bucuresti",
    "check-in": "Otopeni",
    "henri coanda": "Otopeni",
    "otopeni": "Otopeni",
    "resurse umane": "Otopeni",
}


def get_job_city(job_title):
    normalized_title = remove_diacritics(job_title).lower()

    for alias, city in city_aliases.items():
        if alias in normalized_title:
            return city

    return "Otopeni"


job_links = scraper.find("div", {"class": "ta-business"}).find_all("a")

for job in job_links:
    job_title = job.get_text(" ", strip=True)

    if "Anunț de recrutare" not in job_title:
        continue

    job_title = job_title.split("–", 1)[-1].strip()
    job_link = job["href"]
    country = "Romania"
    city = get_job_city(job_title)
    county = get_county(city)

    jobs.append(
        create_job(
            job_title=job_title,
            job_link=job_link,
            country=country,
            city=city,
            county=county,
            company=company,
        )
    )

publish(company, jobs)

publish_logo(company, 'https://www.tarom.ro/wp-content/themes/tarom-child/images/logo.svg')
show_jobs(jobs)
