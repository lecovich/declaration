import json
from datetime import datetime

with open('input.json', 'r') as fp:
    d = json.load(fp)

currencies = d[0]['currencies']
currency_date = datetime.fromisoformat(d[0]['date'].replace('Z', ''))

result = {}

for currency in currencies:
    if currency['code'] == 'USD':
        rate = currency['rate']
        result = {
            'date': currency_date.isoformat(),
            'rate': rate,
        }

with open('output.json', 'w') as fp:
    json.dump(result, fp)
