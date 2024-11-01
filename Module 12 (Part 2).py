from ctypes import c_int

import requests
from datetime import datetime
import json

from Ex12_apikey import open_weather_key

def open_weathermap(city):
    srv = "https://api.openweathermap.org"
    req = srv + "/data/2.5/weather" + "?q=" + city + "&appid" + open_weather_key()

    resp = requests.get(req)
    return resp.status_code, requests.get(req).json()

def temp_in_celsius(kelvin):
    return kelvin - 273.15

city = input("Which city's weather you want to know?")
try:
    (result, date) = open_weathermap(city)
    if result == 200:
        print(f"Current weather: {data, ['weather'] [0] ['description']},"
              f"Temperature: {temp_in_celsius(data['main']['temp']):.1f}")

    elif result == 401:
        print("Not valid API key")
    elif result == 404:
        print("Not weather information for " + city)
    else:
        print("Unknown response code" + str(result))

except requests.exceptions.RequestException as e:
    print("Request could not be completed")
