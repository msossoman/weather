import json
import requests

def countries():
	jsonFile = open('countries.json')
	jsonOutput = json.loads(jsonFile.read())
	
	x = 0
	while x < 34:	
		for country in jsonOutput[1][x]:
			if country == 'name':
				print "We are visiting " + jsonOutput[1][x]['name'] + "."
		for capital in jsonOutput[1][x]:
			if capital == 'capitalCity':
				city = jsonOutput[1][x]['capitalCity']
				countryCode = jsonOutput[1][x]['iso2Code']
				query = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + countryCode)
				info = query.json()
				cityTemp = int(info['main']['temp'])
				centigrade = int(cityTemp - 273.15)
				fahrenheit = int((cityTemp * 9/5) - 459.67) 
				print "In the capital city of " + jsonOutput[1][x]['capitalCity'] + ", the current temperature is:\n" + str(centigrade) + " degrees Centigrade, or " + str(fahrenheit) + " degrees Fahrenheit.\n"
		x += 1
	
	jsonFile.close()



if __name__ == "__main__":
	countries()