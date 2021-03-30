from SECRETS import FINNHUB_TOKEN
import requests


class APIRequest:
    def __init__(self):
        self.api_token = '&token=' + FINNHUB_TOKEN
        self.main_url = 'https://finnhub.io/api/v1/'

    def quote_build_and_send_api_request_returns_dict(self, ticker):
        req = f'{self.main_url}quote?symbol={ticker}{self.api_token}'
        api_data = requests.get(req)

        return api_data.json()


# testing purposes
#r = APIRequest('AAPL')
#print(r.quote_build_and_send_api_request().json())
