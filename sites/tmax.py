from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county

url='https://tmaxgroup.com/ro/cariere/'
company='tmax'
scraper=Scraper()
scraper.get_from_url(url)

jobElements=scraper.find('div', {'class':'elementor-posts-container'}).find_all('article',{'class':'elementor-grid-item'})

jobs=[]

for job in jobElements:
    jobTitle=job.find('a').text.strip()
    jobLink=job.find('a')['href']
    country = "Romania"
    city = 'Cristian'
    county='Sibiu'

    jobs.append(
        {
            'job_title': jobTitle,
            'job_link': jobLink,
            'city': city,
            'county': county,
            'country': country,
            'company': company
        }
    )

for version in [1, 4]:
    publish(version, company, jobs, 'DAVIDMONDOC')

publish_logo(company, 'https://tmaxgroup.com/wp-content/themes/wordpress-tmax/images/logo.svg')
show_jobs(jobs)




