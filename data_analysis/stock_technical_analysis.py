import pandas
import numpy


class TechnicalAnalysis:
    def __init__(self, stock_df):
        self.stock_dataframe = stock_df

    def return_moving_average(self, days_number):
        return self.stock_dataframe.previous_close_price.rolling(days_number).mean()

    def return_close_prices(self, days_number):
        return self.stock_dataframe.previous_close_price.rolling(days_number)
