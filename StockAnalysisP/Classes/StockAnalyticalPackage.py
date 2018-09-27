
class StockAnalyticalPackage():

    """
        By Ben Rogojan
        Date: 2018-09-25
        A class used to represent an analytical package used
        to return specific transformations on the stock data

        Attributes
        ----------
        ListStockObjs : dict
            Represents each stock that is pulled in and the information
            pulled from the daily stock prices

        Methods
        -------
        average_month_price()
            Calculates the averge price for a stock per
            Month

        max_daily_profit()
            Calculates the max daily profit in the selected month range
            per stock

        busy_day()
            Calculates the days where the volume of trading is 10% higher than
            average

        biggest_loser()
            Calculates the stock that is pulled that had the biggest
            loss between its open and close price

        """
    ListStockObjs={}

    def __init__(self,p_ListObjs ):
        self.ListStockObjs=p_ListObjs


    def average_month_price(self):
        ListOfStockObjs=self.ListStockObjs
        print('Please type in which ticker symbol you are interested in: ')
        for ticker in ListOfStockObjs.items():
            print(ticker[1].StockTicker)
        #end for loop
        try:
            tickerSymbol = (input().strip()).upper()
            return ListOfStockObjs[tickerSymbol].price_data.groupby(['date_ym'])['ticker','close','open'].mean()
        except:
            return "Unable to find stock ticker symbol in table"

    """
        max_daily_profit() returns
            a dict that contains the max stock price
            that the stocks were sold at
    """

    def max_daily_profit(self):
        StockMaxDict = {}
        ListOfStockObjs=self.ListStockObjs

        for stock in ListOfStockObjs.items():
            MaxValue = stock[1].price_data['high'][0]-stock[1].price_data['low'][0]
            stock[1].price_data['high']-stock[1].price_data['low']

            for index, row in stock[1].price_data.iterrows():
                #if the current delta between the high and low price
                #greater than the max value then this will replace it
                if MaxValue < row['high']- row['low']:
                    MaxValue =row['high']- row['low']
            #end for loop

            StockMaxDict[stock[0]] = {'TickerSymbol':stock[0],'Date':row['date'],'MaxProfit':round(MaxValue,4)}
        #end for loop
        return StockMaxDict

    """
    busy_day() returns
        a dict with a list of the busy days
        for each ticker
    """
    def busy_day(self):
        BusyDayDict = {}
        ListOfStockObjs=self.ListStockObjs
        for stock in ListOfStockObjs.items():
            AvgValue = stock[1].price_data['volume'].mean()
            Count = 0
            for index,row in stock[1].price_data.iterrows():
                if AvgValue*1.10 <row['volume']:
                    Count += 1
            #end for loop
            BusyDayDict[stock[0]] = {'TotalAboveAverage':Count,'AvgValue':AvgValue}
        #end for loop
        return BusyDayDict

    """
        biggest_loser() returns
            a dict with the stock that had the
            most days where teh open price was less than the cloe price
    """

    def biggest_loser(self):

        ListOfStockObjs=self.ListStockObjs
        LossesDict = {}
        LossLeaderDict ={}
        ticker_row_number = 0
        for stock in ListOfStockObjs.items():
            count_of_losses = 0
            for index,row in stock[1].price_data.iterrows():
                total_losses = row['open'] - row['close']
                if total_losses < 0:
                    count_of_losses +=1
            #end for loop
            LossesDict[ticker_row_number] = {'TickerSymbol':stock[0],'Count':count_of_losses}
            ticker_row_number +=1
        #end for loop

        lowest_loss = LossesDict[0]['Count']
        LossLeaderDict['0'] = {'Symbol':LossesDict[0]['TickerSymbol'],'Count':LossesDict[0]['Count']}
        for key,value in LossesDict.items():
            if lowest_loss < value['Count']:
                print(lowest_loss)
                LossLeaderDict['0'] = {'Symbol':value['TickerSymbol'],'Count':value['Count']}
                lowest_loss = value['Count']
        #end for loop
        return LossLeaderDict
