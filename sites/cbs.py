from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county

url='https://www.cbs-ee.ro/joburi/'
company='CBS Eastern Europe'
scraper=Scraper()
scraper.get_from_url(url)

jobsElements=scraper.find('div',{'id':'accordionCompliant'}).find_all('div', {'class':'card'})

jobs=[]

for job in jobsElements:
    job_title = job.find('h5').text.strip()
    job_link =url+'#'+job.find('div', {'class':'card-header'})['id']
    city='Sibiu'
    county=get_county(city)
    country='Romania'

    jobs.append(
        {
            'job_title': job_title,
            'job_link': job_link,
            'city': city,
            'county': county,
            'country': country,
            'company': company
        }
    )
for version in [1, 4]:
    publish(version, company, jobs, 'DAVIDMONDOC')

publish_logo(company, 'https://www.cbs-ee.ro/static/imagini/logo.png')
show_jobs(jobs)