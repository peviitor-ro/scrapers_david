from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county
import requests

url='https://careers.unicredit.eu/en_GB/jobsuche/SearchJobs/?1286=%5B1887%5D&1286_format=1068&listFilterMode=1&jobRecordsPerPage=15&#'
company='UnicreditTiriac'
scraper=Scraper()
scraper.get_from_url(url)

jobsElements=scraper.find('div', {'class':'open__vacancies'}).find_all('h3', {'class':'article__header__text__title'})

jobs=[]

for job in jobsElements:
    job_title = job.find('a').text.strip()
    job_link = job.find('a')["href"]
    country = "Romania"
    city = job.find('a', {'class''button__view-more'})
    city.click()
    city=job.find('h3')['p'].text.strip
    print(city)
    # county = get_county(city)
print(job_link)
#     jobs.append(
#         {
#             'job_title': job_title,
#             'job_link': job_link,
#             'city': city,
#             'county': county,
#             'country': country,
#             'company': company
#         }
#     )

# for version in [1, 4]:
    # publish(version, company, jobs, 'DAVIDMONDOC')

# publish_logo(company, 'https://www.unicredit.ro/etc/designs/cee2020-pws-ro/img/logos/logo_ro.svg')
#
# show_jobs(jobs)