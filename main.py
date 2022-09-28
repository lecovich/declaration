import json
from datetime import date

from client import get_data


def get_user_input_as_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid number, try again')


def main():
    result = []

    while True:
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

        for currency in currencies:
            if currency['code'] == 'USD':
                result.append({
                    'date': currency['date'],
                    'rate': currency['rate'],
                    'resultAmount': amount * currency['rate'],
                })

        user_prompt = input('Do you want to add one more date? [Y/n]')
        if user_prompt == 'n':
            break

    with open('output.json', 'w') as fp:
        json.dump(result, fp)


if __name__ == '__main__':
    main()
