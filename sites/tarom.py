from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url="https://www.tarom.ro/despre-noi/compania-tarom/cariere"
company="Tarom"
scraper=Scraper()

scraper.get_from_url(url)

jobsElements=scraper.find("div", {"class":"ta-business"}).find_all("p")

jobs = []

for job in jobsElements:
    try:
        if job.find("a").text.__contains__("Anunt de recrutare"):
            job_title = job.find("a").text.split("-")[1]
            job_link = job.find("a")["href"]
            country = "Romania"
            city = ["Bucuresti", "Cluj-Napoca", "Otopeni"]
            county= ["Bucuresti", "Cluj", "Ilfov"]
            jobs.append(
                {
                    "job_title": job_title,
                    "job_link": job_link,
                    "country": country,
                    "city": city,
                    "county": county,
                    "company": company
                })
    except: continue

publish(company, jobs)

publish_logo(company, 'https://www.tarom.ro/sites/all/themes/tarom/static/dist//images/logo-tarom@2x.png')
show_jobs(jobs)

