import json
from datetime import datetime

from client import get_data


def main():
    status, d = get_data()
    if status != 200:
        print('Error', status)
        return

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


if __name__ == '__main__':
    main()
