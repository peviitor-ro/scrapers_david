from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs, translate_city)
from getCounty import get_county, remove_diacritics

url='https://www.transavia.ro/lucreaza-cu-noi'
company = "transavia"
scraper = Scraper()
scraper.get_from_url(url)

jobElements=scraper.find('section', {'id':'locuri-de-munca'}).find('div', {'class':'jobs-wrapper'}).find_all('article', {'class':'item'})
jobs=[]

for job in jobElements:
    job_title=job.find('span').text.strip()
    job_link='https://www.transavia.ro'+job.find('a')['href']
    city=remove_diacritics(translate_city(job.find('div', {'class':'city'}).text.split(' ')[0].replace(',','').strip()))
    county=get_county(city)
    country='Romania'

    if 'Trimite-ne CV-ul tău!' not in job_title:

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
    publish(version, company, jobs, 'DAVIDMONDOC')
publish_logo(company, 'https://www.transavia.ro/sites/default/files/logo_0.png')

show_jobs(jobs)

