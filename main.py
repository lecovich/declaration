import json
from datetime import datetime, date

from client import get_data


def main():

    while True:
        try:
            year = int(input('введите год: '))
            month = int(input('введите месяц: '))
            day = int(input('введите день: '))
            amount = int(input('введите количество денег: '))
            s = date(year, month, day)
        except ValueError:
            print('введена  неправильная дата ')
        else:
            print('введена корректная дата')
            break

    status, d = get_data(s)
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
                'resultAmount': amount * rate,
            }

    with open('output.json', 'w') as fp:
        json.dump(result, fp)


if __name__ == '__main__':
    main()
