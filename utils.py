import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

domain = os.environ.get("DOMAIN")


def get_token():
    """
    Returnează token-ul necesar pentru a face request-uri către API.
    :return: token-ul necesar pentru a face request-uri către API
    """
    endpoint = os.environ.get("TOKEN_ROUTE")
    email = os.environ.get("EMAIL")
    url = f"{domain}{endpoint}"
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    response = requests.post(url, json={"email": email}, headers=headers)
    return response.json()["access"]

def create_job(**kwargs):
    job = {}
    job.update(kwargs)
    return job


def publish(company, data):
    route = os.environ.get("ADD_JOBS_ROUTE")
    url = f"{domain}{route}"
    token = os.environ.get("TOKEN") if os.environ.get("TOKEN") else get_token()

    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {token}",
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    requests.post(url, headers=headers, json=data)

def publish_logo(company, logo_url):
    content_type = "application/json"
    requests.post("https://api.peviitor.ro/v1/logo/add/", headers={"Content-Type": content_type}, json=[{
        "id": company,
        "logo": logo_url
    }])

def show_jobs(data):
    print(json.dumps(data, indent=4))

def translate_city(city):
    cities = {
        # This is general for all scrapers
        "bucharest": "Bucuresti",
        "cluj": "Cluj-Napoca",
        "cristești, mureș":"Cristesti",
        "alba": "Alba Iulia",
       


        ############################
    }
    
    if cities.get(city.lower()):
        return cities.get(city.lower())
    else:
        return city
    
def acurate_city_and_county(**kwargs):
    city_and_county = {}
    city_and_county.update(kwargs)

    return city_and_county
