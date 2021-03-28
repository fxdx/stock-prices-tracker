from SECRETS import FINNHUB_TOKEN
import requests


class APIRequest:
    def __init__(self, c_ticker):
        self.api_token = '&token=' + FINNHUB_TOKEN
        self.main_url = 'https://finnhub.io/api/v1/'
        self.company_ticker = c_ticker

    def quote_build_and_send_api_request(self):
        req = f'{self.main_url}quote?symbol={self.company_ticker}{self.api_token}'
        api_data = requests.get(req)

        return api_data


# testing purposes
#r = APIRequest('AAPL')
#print(r.quote_build_and_send_api_request().json())
