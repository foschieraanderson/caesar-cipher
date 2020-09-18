import requests
from utils.config import Token

def postUrl(url, file):
  post_url = url+Token
  data = {'answer': open(file,'rb')}
  response = requests.post(post_url, files=data)
  return response