from scraper.Scraper import Scraper
from utils import (publish, publish_logo, show_jobs)
from getCounty import get_county

url='https://edukiwi.ro/cariere'
company='edukiwi'
scraper=Scraper()
scraper.get_from_url(url)

jobsElements=scraper.find_all("div", {"class":"col-md-9"})

jobs=[]

for job in jobsElements:
    job_title=job.find("div", {"class":"title-post-cariera"}).text.strip()
    job_link=job.find('a')['href']
    country='Romania'
    city='Timisoara'
    county=get_county(city)

    jobs.append(
        {
            'job_title': job_title,
            'job_link': job_link,
            'city': city,
            'county': county,
            'country': country,
            'company': company,
        }
    )

for version in [1, 4]:
    publish(company, jobs)
    publish_logo(company, 'https://edukiwi.ro/wp-content/themes/wp-bootstrap-4/img/logo-verde-new.svg')

show_jobs(jobs)