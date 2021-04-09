import sqlite3


class SQLDatabaseOperator:
    def connect_to_database(self):
        self.sqliteConnection = sqlite3.connect('stock_database/stock_database.db')

    def close_connection(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()

    def sqlite_select_and_return_tickers(self):
        self.connect_to_database()

        sqlite_select_ticker_query = '''SELECT ticker from Stock_data'''
        cursor = self.sqliteConnection.cursor()
        cursor.execute('SELECT ticker from Stock_data')
        # IT GETS LIST OF TUPLES, SO IT NEEDS TO BE CONVERTED
        tickers = cursor.fetchall()
        cursor.close()
        self.close_connection()

        return tickers

    def insert_new_company_to_stock_data(self, c_name, ticker_name):
        self.connect_to_database()

        cursor = self.sqliteConnection.cursor()
        cursor.execute('INSERT INTO Stock_data(company_name, ticker) VALUES (?, ?);', (c_name, ticker_name))
        self.sqliteConnection.commit()
        cursor.close()
        self.close_connection()

    def insert_data_to_database(self, ticker_name, api_data_dict):
        self.connect_to_database()

        sqlite_insert_data_query = '''INSERT INTO {}(open_price, high_price, low_price, previous_close_price, date)\
                                      VALUES ({}, {}, {}, {}, datetime('now', '+2 hours'));'''.format(ticker_name,\
                                                                                               api_data_dict['o'],\
                                                                                               api_data_dict['h'],\
                                                                                               api_data_dict['l'],\
                                                                                               api_data_dict['pc'])
        cursor = self.sqliteConnection.cursor()
        cursor.execute(sqlite_insert_data_query)
        self.sqliteConnection.commit()
        cursor.close()
        self.close_connection()

    def sqlite_creating_tables_for_tickers(self, tickers_list):
        self.connect_to_database()
        cursor = self.sqliteConnection.cursor()

        for ticker in tickers_list:
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS {}(
                                    id INTEGER PRIMARY KEY,
                                    open_price FLOAT,
                                    high_price FLOAT,
                                    low_price FLOAT,
                                    previous_close_price FLOAT,
                                    date TEXT);'''.format(ticker)
            cursor.execute(sqlite_create_table_query)
            self.sqliteConnection.commit()

        cursor.close()
        self.close_connection()


# if __name__ == '__main__':
    #name = 'ATT'
    #ticker = 'T'
    #app = SQLDatabaseOperator()
    #app.insert_new_company_to_stock_data(name, ticker)
