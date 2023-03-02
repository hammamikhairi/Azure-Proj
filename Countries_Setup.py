
import requests
import json

OUT_PATH = "countries.json"

data = requests.get('https://countriesnow.space/api/v0.1/countries').json()
countries_dict = {}
countries = data['data']  # first we access the data
for country in countries: # now we loop the countries
  countries_dict[country['country']] = country['cities']


with open(OUT_PATH, "w") as f:
    json.dump(countries_dict, f)


print(OUT_PATH)