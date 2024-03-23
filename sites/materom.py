from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs, translate_city)
from getCounty import get_county, remove_diacritics

url='https://www.materom.ro/cariera/'
company='materom'
scraper=Scraper()
scraper.get_from_url(url)

jobElements=scraper.find('div', {'id':'pgc-4415-3-0'})

jobs=[]

for element in jobElements:
    job=element.find('div', {'class':'open-position'})
    job_title=job.find('h4').text.split("-")[0].strip()
    job_link=url+'#'+element['id']
    city = remove_diacritics(translate_city(job.find('h4').text.split("-")[-1].split(",")[0].strip()))
    if city ==' Napoca':
        city ='Cluj-Napoca'
    if 'Mures' in city:
        city='Targu-Mures'
    if "Bucuresti Mogosoaia" in city:
        city = 'Mogosoaia'
    if city =='Bucuresti Militari' or  city == 'Bucuresti Colentina':
        city ='Bucuresti'
    if city == 'Cristesti':
        county='Mures'
    elif city == 'Iasi':
        county = 'Iasi'
    else:
        county=get_county(city)
    country="Romania"

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

publish_logo(company, 'https://www.materom.ro/wp-content/uploads/logo/logo-materom.png')

show_jobs(jobs)
