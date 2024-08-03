from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url = "https://stayfit.ro/cariere/"
company = "stayfit"
scraper = Scraper()
scraper.get_from_url(url)

jobsElements = scraper.find('div', {'class':'elementor-element-populated'}).find_all('div', {'class':'elementor-element'})[2:]

job_no=1
jobs=[]

for job in jobsElements:
    try:
        if 'elementor-hidden-desktop' not in job['class']:
            job_title = job.find('h2').text.strip()
            job_link = 'https://stayfit.ro/cariere/'+"#"+str(job_no)
            city=remove_diacritics(job_title.split(',')[-1].strip())
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
            job_no += 1
    except: pass


publish(company, jobs)

publish_logo(company, 'https://stayfit.ro/wp-content/uploads/2020/01/Logo-Stay-Fit-Gym-.png')

show_jobs(jobs)


