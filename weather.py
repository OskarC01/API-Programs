import requests

from security import weatherapikey

api_key_world = weatherapikey
base_url_world = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f'{base_url_world}?appid={api_key_world}&q={city}'
response = requests.get(request_url)
if response.status_code == 200:
    data_world = response.json()
    weather = data_world['weather']
    temperature = round(data_world['main']['temp'] - 273.15, 1)
    country = data_world['sys']['country']
    print(f"\nWeather: {weather[0]['main']},  {weather[0]['description']}")
    print(f"Temperature: {temperature} degrees Celsius")
    print(f"Country: {country}\n")
else:
    print('An error occurred')
