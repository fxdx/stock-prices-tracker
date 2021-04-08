import app.APIRequestFinnhub
import stock_database.database_operators


class EventManager:
    def __init__(self):
        self.database_handler = stock_database.database_operators.SQLDatabaseOperator()
        self.api_handler = app.APIRequestFinnhub.APIRequest()

    def convert_tuple_to_string(self, tup):
        string = ''.join(tup)
        return string

    def get_tickers_from_database(self):
        # t contains TUPLES so it needs to be converted
        t = self.database_handler.sqlite_select_and_return_tickers()

        tickers = []
        for tick in t:
            tickers.append(self.convert_tuple_to_string(tick))
        return tickers

    def send_and_return_quote_request(self, company_ticker):
        quote_data = self.api_handler.quote_build_and_send_api_request_returns_dict(company_ticker)
        return quote_data

    def insert_stock_data_from_quote_api_to_database(self, c_ticker, data_dict):
        self.database_handler.insert_data_to_database(c_ticker, data_dict)

    def insert_new_stock_company_to_database(self, company_name, company_ticker):
        self.database_handler.insert_new_company_to_stock_data(company_name, company_ticker)

    def create_tables_for_tickers(self, t_list):
        self.database_handler.sqlite_creating_tables_for_tickers(t_list)


if __name__ == '__main__':
    app = EventManager()
    tickers = app.get_tickers_from_database()
    app.create_tables_for_tickers(tickers)

    for c_t in tickers:
        quote_data_dict = app.send_and_return_quote_request(c_t)
        app.insert_stock_data_from_quote_api_to_database(c_t, quote_data_dict)
