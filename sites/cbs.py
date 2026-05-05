import re

from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url='https://www.cbs-ee.ro/joburi/'
company='cbs'
scraper=Scraper()
scraper.get_from_url(url)

jobsElements=scraper.find('div',{'id':'accordionCompliant'}).find_all('div', {'class':'card'})

jobs=[]
company_cities = ['Sibiu', 'Brasov', 'Timisoara', 'Cluj-Napoca']
city_aliases = {
    'cluj': 'Cluj-Napoca',
    'timisoara': 'Timisoara',
    'brasov': 'Brasov',
    'sibiu': 'Sibiu',
}
used_links = {}


def get_unique_link(job_link):
    count = used_links.get(job_link, 0)
    used_links[job_link] = count + 1
    if count == 0:
        return job_link
    return f'{job_link}#{count}'


def get_job_cities(job):
    job_text = remove_diacritics(job.get_text(' ', strip=True)).lower()
    found_cities = []

    for city_key, city_name in city_aliases.items():
        if re.search(rf'\b{re.escape(city_key)}\b', job_text):
            found_cities.append(city_name)

    if found_cities:
        return found_cities

    return company_cities

for job in jobsElements:
    job_title = job.find('h5').text.strip()
    job_link = get_unique_link(url+'#'+job.find('div', {'class':'card-header'})['id'])
    city = get_job_cities(job)
    county = [get_county(city_name) for city_name in city]
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

publish(company, jobs)

publish_logo(company, 'https://www.cbs-ee.ro/static/imagini/logo.png')
show_jobs(jobs)
