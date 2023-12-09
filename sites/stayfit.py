#scoate din git ignore
from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url = "https://dabodoner.ro/ro/ro/joburi"
company = "stayfit"
scraper = Scraper()
scraper.get_from_url(url)

jobsElements = scraper.find('div', {'class':'elementor-col-100'}).find_all('div',{'class':'elementor-element'})
jobs=[]

for job in jobs:
    job_title = job.find('h2', {'class':'elementor-heading-title'}).text.strip()

    print(job_title)