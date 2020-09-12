import requests
import json
from pprint import pprint

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"Chiba"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }

response = requests.get(url, headers=headers, params=querystring)


print("☆☆☆☆☆☆☆☆☆☆☆")
pprint(response.json())
print("☆☆☆☆☆☆☆☆☆☆☆")
print(response)