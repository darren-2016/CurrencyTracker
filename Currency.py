# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Request
    # GET http://api.openrates.io/latest

    try:
        response = requests.get(
            url="http://api.openrates.io/latest",
            params={
                "base": "USD",
                "symbols": "USD,GBP,EUR,AUD",
            },
            headers={
                "Cookie": "__cfduid=d5894e0107eff1eb12d8eb5af2c7292bf1538645249",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request()
