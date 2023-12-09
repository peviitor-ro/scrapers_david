#scoate din git ignore
from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county
import requests

url='https://www.aeroportulsatumare.ro/cariere.html'
company='Aeroportul International Satu Mare'
scraper=Scraper()
scraper.get_from_url(url)

jobElements=scraper.find('div', {'class':'pageconentleft'}).find('div',{'class':'maincontent'}).find_all('p')

jobs=[]

for job in jobElements:
    try:
        if job.find("a").text.__contains__("un post de "):
            job_title = job.find("a").text.split(" ")[1]
            print(job_title)