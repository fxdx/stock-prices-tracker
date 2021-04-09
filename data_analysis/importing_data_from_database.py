import pandas
import sqlite3

class SQLitePandasImports:
    def connect_to_database(self):
        self.sqliteConnection = sqlite3.connect('stock_database/stock_database.db')

    def close_connection(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()

    def read_database_to_pandas_dataframe(self, database_ticker_name):
        self.connect_to_database()

        df = pandas.read_sql_query("SELECT * from '{}'".format(database_ticker_name), self.sqliteConnection)
        del df['id']

        self.close_connection()
        return df

# testing purposes
#if __name__ == '__main__':
#    app = SQLitePandasImports()
#    df = app.read_database_to_pandas_dataframe('AAPL')
#    print(df.head())