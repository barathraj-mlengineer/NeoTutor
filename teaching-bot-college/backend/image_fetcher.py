import requests
from utils.config import load_api_key

def fetch_diagram_image(topic):
    serp_key = load_api_key("SERPAPI_KEY")
    url = f"https://serpapi.com/search.json?q={topic} diagram&tbm=isch&api_key={serp_key}"
    res = requests.get(url).json()
    return res['images_results'][0]['original']
