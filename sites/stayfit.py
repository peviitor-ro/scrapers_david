from scraper.Scraper import Scraper
from utils import (publish, publish_logo, create_job, show_jobs)
from getCounty import get_county, remove_diacritics

url = "https://stayfit.ro/cariere/"
company = "stayfit"
scraper = Scraper()
scraper.get_from_url(url)

jobs = []
job_no = 1

city_aliases = {
    "arad": "Arad",
    "aurora bacau": "Bacau",
    "bacau": "Bacau",
    "balotesti": "Balotesti",
    "bartolomeu retail park brasov": "Brasov",
    "bartolomeu": "Brasov",
    "bega timisoara centru": "Timisoara",
    "bucuresti": "Bucuresti",
    "cluj": "Cluj-Napoca",
    "cocor": "Bucuresti",
    "colosseum": "Bucuresti",
    "constanta": "Constanta",
    "craiova": "Craiova",
    "crevedia": "Crevedia",
    "dorobanti": "Bucuresti",
    "dorobantii": "Bucuresti",
    "esplanada pantelimon": "Bucuresti",
    "esplanada": "Bucuresti",
    "floresti": "Floresti",
    "galati": "Galati",
    "ghencea": "Bucuresti",
    "giroc": "Giroc",
    "iasi": "Iasi",
    "iulius mall": "Iasi",
    "lake view constanta": "Constanta",
    "lemon park": "Bucuresti",
    "liberty": "Bucuresti",
    "mercur": "Craiova",
    "miroslava": "Miroslava",
    "mosnita noua": "Mosnita Noua",
    "mosnita": "Mosnita Noua",
    "nord timisoara": "Timisoara",
    "otopeni": "Otopeni",
    "pacurari": "Iasi",
    "palas campus": "Iasi",
    "palas mall": "Iasi",
    "pallady": "Bucuresti",
    "petre ispirescu": "Bucuresti",
    "pitesti": "Pitesti",
    "ploiesti nord": "Ploiesti",
    "ploiesti": "Ploiesti",
    "popesti leordeni": "Popesti Leordeni",
    "promenada": "Sibiu",
    "promenada craiova": "Craiova",
    "promenada sibiu": "Sibiu",
    "rahova": "Bucuresti",
    "romana": "Bucuresti",
    "shopping city sibiu": "Sibiu",
    "shopping city": "Sibiu",
    "sibiu": "Sibiu",
    "silk": "Iasi",
    "stay fit arad": "Arad",
    "stay fit floresti cluj": "Floresti",
    "stay fit gym bacau": "Bacau",
    "stay fit gym brasov bartolomeu": "Brasov",
    "stay fit gym crevedia": "Crevedia",
    "stay fit gym focsani": "Focsani",
    "stay fit gym ghencea": "Bucuresti",
    "stay fit gym ploiesti": "Ploiesti",
    "stay fit gym popesti leordeni": "Popesti Leordeni",
    "stay fit gym supernova alexandriei": "Bucuresti",
    "stay fit gym targoviste": "Targoviste",
    "stay fit gym targu jiu": "Targu Jiu",
    "stay fit gym": "Bucuresti",
    "stay fit otopeni": "Otopeni",
    "supernova alexandriei": "Bucuresti",
    "supernova constanta": "Constanta",
    "targoviste": "Targoviste",
    "targu jiu": "Targu Jiu",
    "timisoara bega central": "Timisoara",
    "timisoara": "Timisoara",
    "titulescu": "Bucuresti",
    "tractorul": "Brasov",
    "urbano cluj": "Cluj-Napoca",
    "urbano floresti": "Floresti",
    "urbano": "Cluj-Napoca",
    "valea adanca": "Valea Adanca",
    "valea lupului": "Valea Lupului",
    "vaslui": "Vaslui",
    "vitan": "Bucuresti",
    "vladimirescu": "Vladimirescu",
    "voluntari": "Voluntari",
}

county_overrides = {
    "Balotesti": "Ilfov",
    "Floresti": "Cluj",
    "Iasi": "Iasi",
    "Valea Lupului": "Iasi",
}


def normalize_city(location):
    normalized_location = remove_diacritics(location).lower().replace(".", " ")
    normalized_location = " ".join(normalized_location.split())

    for alias, city in sorted(city_aliases.items(), key=lambda item: len(item[0]), reverse=True):
        if alias in normalized_location:
            return city

    return None


jobs_heading = scraper.find("h2", string="Joburi disponibile:")
current_role = None

for element in jobs_heading.find_all_next():
    if element.name == "h2":
        break

    if element.name == "h3":
        current_role = element.get_text(" ", strip=True)
        continue

    if element.name != "li" or current_role is None:
        continue

    location = element.get_text(" ", strip=True)
    city = normalize_city(location)
    if city is None:
        continue

    county = county_overrides.get(city, get_county(city))
    country = "Romania"
    job_link = f"{url}#{job_no}"
    job_no += 1

    jobs.append(
        create_job(
            job_title=current_role,
            job_link=job_link,
            city=city,
            county=county,
            country=country,
            company=company,
        )
    )

publish(company, jobs)

publish_logo(company, 'https://stayfit.ro/wp-content/uploads/2020/12/Logo-SFG-v2026-black.webp')

show_jobs(jobs)
