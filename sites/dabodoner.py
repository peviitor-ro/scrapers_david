from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url = "https://dabodoner.ro/ro/ro/joburi"
company = "Dabodoner"
scraper = Scraper()

scraper.get_from_url(url)

jobsElements = scraper.find("section", {"class": "jobs"}).find("div", {"class": "row"}).find_all("div", "col-lg-6")

jobs = []
city_aliases = {
    "cluj": "Cluj-Napoca",
    "constanta": "Constanta",
    "oradea": "Oradea",
    "roman": "Roman",
    "targoviste": "Targoviste",
    "timisoara": "Timisoara",
}


def get_city(job):
    location = job.find("div", {"class": "location"}).text.strip()
    if location:
        normalized_location = remove_diacritics(location).lower()
        if normalized_location in city_aliases:
            return city_aliases[normalized_location]

    job_text = remove_diacritics(job.get_text(" ", strip=True)).lower()
    job_link = remove_diacritics(job.find("a")["href"]).lower()

    for city_key, city_name in city_aliases.items():
        if city_key in job_text or city_key in job_link:
            return city_name

    return "Cluj-Napoca"

for job in jobsElements:
    job_title = job.find("div", {"class": "title"}).text.strip()
    job_link = job.find("a")["href"]
    country = "Romania"
    city = get_city(job)
    county = get_county(city)

    jobObj = create_job(
        job_title=job_title,
        job_link=job_link,
        city=city,
        county=county,
        country=country,
        company=company
    )

    jobs.append(jobObj)

publish(company, jobs)

publish_logo(company, 'https://dabodoner.ro/assets/images/logo.svg')
show_jobs(jobs)
