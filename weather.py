#This will be the module for the lecture 49 assignment using the weather API.

import json

jsonFile = open('countries.json', 'r')
jsonOutput = json.loads(jsonFile)

from requests import *

query = get("http://api.openweathermap.org/data/2.5/weather?q=San+Francisco,us")

query.json()
query.text