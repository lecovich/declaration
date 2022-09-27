import requests
#2022-09-21
HOST = 'nbg.gov.ge'
PATH = 'gw/api/ct/monetarypolicy/currencies/en/json/?date='


def get_data(current_date):

    url = f'https://{HOST}/{PATH}{current_date.isoformat()}'
    print(url)
    response = requests.get(url)

    if response.status_code != 200:
        return response.status_code, None

    data = response.json()

    return response.status_code, data


def foo():
    pass