import requests

HOST = 'nbg.gov.ge'
PATH = 'gw/api/ct/monetarypolicy/currencies/en/json/?date=2022-09-20'


def get_data():
    response = requests.get(f'https://{HOST}/{PATH}')

    if response.status_code != 200:
        return response.status_code, None

    data = response.json()

    return response.status_code, data
