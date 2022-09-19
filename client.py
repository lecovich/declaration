import http.client
import json

HOST = 'nbg.gov.ge'
PATH = 'gw/api/ct/monetarypolicy/currencies/en/json/?date=2022-09-19'


def get_data():
    connection = http.client.HTTPSConnection(HOST)
    connection.request('GET', PATH)
    response = connection.getresponse()
    connection.close()

    if response.status != 200:
        return response.status, None

    raw_data = response.read()
    data = json.loads(raw_data)

    return response.status, data
