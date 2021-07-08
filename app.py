import requests
import config

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
    'x-rapidapi-key': config.apiFootballKey,
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)