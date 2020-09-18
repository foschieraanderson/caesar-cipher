import requests
from utils.config import Token

def getResponse(url):
    get_url = url+Token
    response = requests.get(get_url)
    response_json = response.json()
    return response_json