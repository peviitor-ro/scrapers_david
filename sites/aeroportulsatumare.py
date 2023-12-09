from scraper.Scraper import Scraper
from utils import (publish, publish_logo, show_jobs)

url='https://www.aeroportulsatumare.ro/cariere.html'
company='AeroportulInternationalSatuMare'
scraper=Scraper()
scraper.get_from_url(url)

jobElements=scraper.find_all('ul')[-1].find_all('li')

print(jobElements)

jobs=[]
job_number=1

for job in jobElements:
    job_title = job.text
    job_link='https://www.aeroportulsatumare.ro/cariere.html'+'/#'+str(job_number)
    city='Satu Mare'
    county='Satu Mare'
    country = 'Romania'

    jobs.append(
        {
            "job_title": job_title,
            "job_link": job_link,
            "country": country,
            "city": city,
            "county": county,
            "company": company
        })
    job_number+=1

for version in [1, 4]:
    publish(version, company, jobs, 'DAVIDMONDOC')

publish_logo(company, 'https://www.cjsm.ro/storage/scci/lili/logouri-modificate/aerportulsatumarelogo-475x267_jpg.webp')
show_jobs(jobs)