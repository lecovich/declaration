import json
from datetime import datetime, date

from client import get_data


def get_user_input_as_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid number, try again')


def main():
    while True:
        year = get_user_input_as_int('Enter year: ')
        month = get_user_input_as_int('Enter month: ')
        day = get_user_input_as_int('Ender day: ')

        try:
            current_date = date(year, month, day)
        except ValueError:
            print('Invalid date, try again from the very beginning')
        else:
            break

    amount = get_user_input_as_int('Enter amount: ')

    status, d = get_data(current_date)
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
