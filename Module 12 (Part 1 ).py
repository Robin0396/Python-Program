import requests
import json


server = "https://api.chucknorris.io/"
request = server + "jokes/random"

try:
    response = requests.get(request).json()
    print(response["value"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed", e)