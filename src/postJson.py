import requests
from utils.config import Token

def postJson(url, file):
  url = url+Token
  data = {'answer': open(file,'rb')}
  response = requests.post(url, files=data)
  return response