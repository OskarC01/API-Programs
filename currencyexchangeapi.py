import requests
import json
import pprint

'https://api.currencyapi.com/v3/latest?apikey=4x38E752ESF6LWuGzzzAAE4JMyoONWJ7ZdmLS9KF&currencies=EUR%2CUSD%2CCAD'

apikey = '4x38E752ESF6LWuGzzzAAE4JMyoONWJ7ZdmLS9KF'
base = input('Input the base currency designation you want to use: ')
currency = input(
    'Input currency designation you want to convert to (leave blank of you want to see all available currencies): ')
amount = int(input('Input amount of money you want to convert: '))
url = f'https://api.currencyapi.com/v3/latest?apikey={apikey}&base_currency={base}&currencies={currency}'


response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    pprint.pprint(data['data'])
    converter = (data['data'][currency]['value'])
    print(f'Amount of converted money is equal to: {converter * amount} {currency}')
elif response.status_code == 429:
    print('You have reached your monthly request limit')
else:
    print('Error occurred')
