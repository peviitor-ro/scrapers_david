from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county

url='https://jobs.ropardo.ro/'
company='Ropardo'
scraper=Scraper()
scraper.get_from_url(url)

jobsElements=scraper.find('div', {'class':'jobs-wrapper'}).find_all('div', {'class':'list-item'})

jobs=[]

for job in jobsElements:
    job_title = job.find("h4").text.strip()
    job_link = job.find('a')["href"]
    country = "Romania"
    city = job.find('div', {'class':'meta-location'}).text.strip()
    county = get_county(city)
    job_type = job.find("div", {"class":"meta-shedule-duration"}).text.strip()
    remote=[]
    if "Remote" in job_type:
        remote.append("Remote")

    jobs.append(
        {
        'job_title':job_title,
         'job_link':job_link,
         'city':city,
         'county':county,
         'country':country,
         'company':company,
         'remote': remote
        }
    )

publish(company, jobs)

publish_logo(company, 'https://jobs.ropardo.ro/wp-content/themes/jobs-platform/images/logo.png')

show_jobs(jobs)
