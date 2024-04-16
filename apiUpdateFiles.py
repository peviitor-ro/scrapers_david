import requests
from utils import get_token
from dotenv import load_dotenv

load_dotenv()

url = "https://api.laurentiumarian.ro/scraper/scrapers_david/"
token = get_token()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

r = requests.post(url, json={"update": "true"}, headers=headers)

response = r.json()

if response.get("succes"):
    print(response.get("succes"))
else:
    print(response.get("error"))
