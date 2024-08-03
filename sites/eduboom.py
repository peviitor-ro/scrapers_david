from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url = "https://eduboom.ro/cariere"
company = "eduboom"
scraper = Scraper()
scraper.get_from_url(url)

jobsElements = scraper.find('section', {'id':'jobs-list'}).find('div', {'class':'col-md-8'}).find_all('div',{'class':'job-offers'})
jobs=[]

for job in jobsElements:
    job_title = job.find('div', {'class':'job-offer-title'}).text.strip()
    job_link=job.find('a')['href']
    country='Romania'
    city='Bucuresti'
    county=get_county(city)
    remote="Remote"

    jobs.append(
        {
            'job_title': job_title,
            'job_link': job_link,
            'city': city,
            'county': county,
            'country': country,
            'company': company,
            'remote': remote
        }
    )

for version in [1, 4]:
    publish(company, jobs)
publish_logo(company, 'https://static.eduboom.ro/assets/base/images/eduboom-logo-l.svg')

show_jobs(jobs)