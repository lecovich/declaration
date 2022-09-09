import json
from datetime import datetime

with open('input.json', 'r') as fp:
    d = json.load(fp)

currencies = d[0]['currencies']
currency_date = datetime.fromisoformat(d[0]['date'].replace('Z', ''))

for currency in currencies:
    if currency['code'] == 'USD':
        rate = currency['rate']
        print(f'{currency_date.date()}: {rate}')
