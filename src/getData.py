import requests
from utils.config import Token

def getData(url):
    url = url+Token
    response = requests.get(url)
    response_json = response.json()
    return response_json