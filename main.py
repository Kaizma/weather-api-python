import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "2833f9039e7bc5e9d64a5402eaae0c34"
CITY = "Colombo"


def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15

    return celcius 


url = BASE_URL + "appid="+ API_KEY + "&q=" + CITY

response = requests.get(url).json()
print(response)

temp_kelvin = response['main']['temp']
temp_celcius = kelvin_to_celcius(temp_kelvin)
print(temp_celcius)

feels_like_kelvin = response['main']['feels_like']
feels_like_celcius = kelvin_to_celcius(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']

description = response['weather'][0]['description']

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print(f"Temperature in {CITY}: {temp_celcius:.2f}°C")
print(f"Temperature in {CITY} feels like: {feels_like_celcius:.2f}°C")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Windspeed in {CITY}: {wind_speed}m/s")

print(f"Sun rises in the city {CITY} at {sunrise_time} local time")
print(f"Sun sets in the city {CITY} at {sunset_time} local time")
print(f"General weather in {CITY}: {description}")


