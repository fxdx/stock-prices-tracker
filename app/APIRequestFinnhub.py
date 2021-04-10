from app.SECRETS import FINNHUB_TOKEN
import requests


class APIRequest:
    def __init__(self):
        self.api_token = '&token=' + FINNHUB_TOKEN
        self.main_url = 'https://finnhub.io/api/v1/'

    def quote_build_and_send_api_request_returns_dict(self, ticker):
        req = f'{self.main_url}quote?symbol={ticker}{self.api_token}'
        quote_api_data = requests.get(req)

        return quote_api_data.json()

    def reported_financials_build_and_send_api_request_returns_dict(self, ticker):
        req = f'{self.main_url}stock/financials-reported?symbol={ticker}{self.api_token}'
        reported_financials_api_data = requests.get(req)

        return reported_financials_api_data.json()

# testing purposes
# r = APIRequest()
# print(r.reported_financials_build_and_send_api_request_returns_dict('AAPL'))
