import requests
import pprint

from security import currencyapikey

'https://api.currencyapi.com/v3/latest?apikey=4x38E752ESF6LWuGzzzAAE4JMyoONWJ7ZdmLS9KF&currencies=EUR%2CUSD%2CCAD'

apikey = currencyapikey
base = input('Input the base currency designation you want to use: ').upper()
currency = input(
    'Input currency designation you want to convert to (leave blank of you want to see all available currencies): ').upper()
amount = int(input('Input amount of money you want to convert: '))
url = f'https://api.currencyapi.com/v3/latest?apikey={apikey}&base_currency={base}&currencies={currency}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint.pprint(data['data'])
    converter = (data['data'][currency]['value'])
    print(f'Converting {amount} {base} is equal {round(converter * amount, 2)} {currency}, with conversion rate of {round(converter, 2)}.')
elif response.status_code == 429:
    print('This apiKey has reached monthly request limit. Sorry.')
else:
    print('Error occurred')
