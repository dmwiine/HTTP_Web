import requests
import json

CityIDs = [7873249, 2761999, 2762000, 25113449, 5815020]
Key = "56f7ffa37dff76b634f101927adcd288"

def get_weather_data(get_url, city_id):
	try:
		isinstance(int(city_id), int)
		if int(city_id) in CityIDs:
			response = requests.get(get_url)

			if response.status_code == 401:
				return "Please check your api key"
			elif response.status_code == 200:
				weather_data = json.loads(response.text)
				return weather_data
		else:
			print("Please enter a valid City ID")
	except ValueError as e:
		print("You need to enter an integer value")
		raise(e)
	return "----No Weather data to show----"

def main():
	print("\n\t*** Python HTTP API APP***\n\t%s\n" %("-"*31))
	print("Welcome to this simple Python Console App")
	print()
	print("Let us retrieve weather data for select cities around the world and display it")
	print()
	print(CityIDs)
	print()
	city_id = input("Please input a city ID from the id's printed above  ")

	API_Url = "http://api.openweathermap.org/data/2.5/forecast?id=%d&appid=%s" % (int(city_id), Key)
	print()
	print("-------------Procesing your request--------------")
	print()
	print()
	print(get_weather_data(API_Url,city_id))

if __name__ == '__main__':
	main()
