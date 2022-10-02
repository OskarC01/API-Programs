import requests
import json

location = int(input("""What location do you want to search: 
            1 - World
            2 - Poland
"""))


if location == 1:
    api_key_world = '9d6fdd10c6c3aced84b9bb07e8e78aa3'
    base_url_world = 'http://api.openweathermap.org/data/2.5/weather'

    city = input('Enter a city name: ')
    request_url = f'{base_url_world}?appid={api_key_world}&q={city}'
    response = requests.get(request_url)

    if response.status_code == 200:
        data_world = response.json()
        weather = data_world['weather']
        temperature = round(data_world['main']['temp'] - 273.15, 1)
        country = data_world['sys']['country']

        print(f"Weather: {weather[0]['main']},  {weather[0]['description']}")
        print(f"Temperature: {temperature} degrees Celsius")
        print(f"Country: {country}")

    else:
        print('An error occurred')
elif location == 2:
    city_poland = input('Enter city you want to check: ')
    response = requests.get(
        f'https://danepubliczne.imgw.pl/api/data/synop/station/{city_poland}')

    if response.status_code == 200:
        data_poland = response.json()
        station_id = data_poland['id_stacji']
        station = data_poland['stacja']
        date = data_poland['data_pomiaru']
        time = data_poland['godzina_pomiaru']
        temp = data_poland['temperatura']
        pressure = data_poland['cisnienie']

        print(f'Station ID: {station_id}, station city: {station}.')
        print(f'Date of measurement: {date}, {time}.')
        print(f'Temperature - {temp}°C, Pressure - {pressure}')

    else:
        print('City not found')
