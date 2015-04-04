import json

def countries():
	jsonFile = open('countries.json', 'r')
	lines = jsonFile.read()
	
	print lines[0][0]

if __name__ == "__main__":
	countries()

'''from requests import *

query = get("http://api.openweathermap.org/data/2.5/weather?q=San+Francisco,us")

query.json()
query.text'''