import pandas as pd
import quandl
class Stockobj():
    """
        By Ben Rogojan
        Date: 2018-09-25
        A class used to represent a stock and the data for
        its stock prices in a set data range

        Attributes
        ----------
        StockTicker : str
            Represents the 1-5 character ticker symbol

        Start_Date : date
            Represents the starting date the price data was pulled from

        End_Date : date
            Represents the ending date the price data was pulled from

        price_data : data frame
            Represents a data frame that contains price data on the Stock
                ticker - the ticker symbol for the stock
                date - the date the prices and volumes were recorded
                volume - the number of shares that exchanged traders
                close - the closing price of the stock
                open - the opening price of the Stock
                high - the highest price the stock got during the day
                low - the lowest price the stock got during the day
                date_ym - This is added in and represents the day variable in the YYYY-MM format
        Methods
        -------

        get_price_dict
            Gets data from the WIKIP API using the quandl library

        """
    StockTicker =""
    Start_Date=""
    End_Date=""
    price_data  = pd.DataFrame()


    def __init__(self, p_StockTicker,p_Start_Date,p_EndDate):
        self.Start_Date = p_Start_Date
        self.End_Date = p_EndDate
        self.StockTicker = p_StockTicker
        self.get_price_dict()

    def get_price_dict(self):
        quandl.ApiConfig.api_key = "s-GMZ_xkw6CrkGYUWs1p"
        data = quandl.get_table('WIKI/PRICES'
                            , qopts = { 'columns': ['ticker', 'date', 'volume','close','open','high','low'] }
                            , ticker =self.StockTicker
                            , date = { 'gte': self.Start_Date, 'lte': self.End_Date })
        #We are adding a column to the data frame that contains YYYYMM
        data['date_ym'] = pd.to_datetime(data['date']).dt.to_period('M')
        self.price_data = data
