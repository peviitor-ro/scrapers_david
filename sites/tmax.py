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

publish(company, jobs)

publish_logo(company, 'https://media.licdn.com/dms/image/C4D0BAQFDkByde-vzEg/company-logo_200_200/0/1630527230431/tmax_sibiu_srl_logo?e=1730332800&v=beta&t=NKsN_jFj6HCxYAbZgbhL9Sx5p7a8Sz-rrRLrvB4aNfw')
show_jobs(jobs)




