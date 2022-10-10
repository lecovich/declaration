import json
from datetime import date

from client import get_data


def get_user_input_as_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid number, try again')


def print_result(value):
    overall_amount = 0
    overall_result_amount = 0

    print('\nDate\t\t\tAmount, USD\t\tRate\t\t\tAmount, GEL')

    for item in value:
        current_date = item['date'].split('T')[0]
        print(f'{current_date}\t\t{item["amount"]}\t\t\t\t{item["rate"]}\t\t\t{item["resultAmount"]}')

        overall_amount += item['amount']
        overall_result_amount += item['resultAmount']

    print('\n')
    print(f'{"Overall amount"}\t{round(overall_amount, 2)}\t\t\t\t\t\t\t\t{round(overall_result_amount, 2)}')


def main():
    new_add_user_prompt = input('Do you want to read file with result? [Y/n] ')
    if new_add_user_prompt in ('Y', ''):
        try:
            with open('output.json', 'r') as fp:
                result = json.load(fp)
        except FileNotFoundError:
            result = []
    else:
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
                    'amount': amount,
                })

        user_prompt = input('Do you want to add one more date? [Y/n] ')
        if user_prompt == 'n':
            break

    print_result(result)

    user_prompt = input('Do you want to add result in file?  [Y/n] ')
    if user_prompt in ('Y', ''):
        with open('output.json', 'w') as fp:
            json.dump(result, fp)


if __name__ == '__main__':
    main()
