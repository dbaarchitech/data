
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

        try:
            tickerSymbol = (input().strip()).upper()
            return ListOfStockObjs[tickerSymbol].data.groupby(['date_ym'])['ticker','close','open'].mean()
        except:
            return "Unable to find stock ticker symbol in table"



    def max_daily_profit(self):
        StockMaxDict = {}
        ListOfStockObjs=self.ListStockObjs

        for stock in ListOfStockObjs.items():
            MaxValue = stock[1].data['high'][0]-stock[1].data['low'][0]
            stock[1].data['high']-stock[1].data['low']

            for index, row in stock[1].data.iterrows():
                #if the current delta between the high and low price
                #greater than the max value then this will replace it
                if MaxValue < row['high']- row['low']:
                    MaxValue =row['high']- row['low']
            StockMaxDict[stock[0]] = {'TickerSymbol':stock[0],'Date':row['date'],'MaxProfit':MaxValue}
        return StockMaxDict


    def busy_day(self):
        BusyDayDict = {}
        ListOfStockObjs=self.ListStockObjs
        for stock in ListOfStockObjs.items():
            AvgValue = stock[1].data['volume'].mean()
            Count = 0
            for index,row in stock[1].data.iterrows():
                if AvgValue*1.10 <row['volume']:
                    Count += 1
            BusyDayDict[stock[0]] = {'TotalAboveAverage':Count,'AvgValue':AvgValue}
        return BusyDayDict

    def biggest_loser(self):
        ListOfStockObjs=self.ListStockObjs
        LossesDict = {}
        LossLeaderDict ={}
        rn = 0
        for stock in ListOfStockObjs.items():
            Count = 0
            for index,row in stock[1].data.iterrows():
                TotalLosses = row['open'] - row['close']
                if TotalLosses < 0:
                    Count +=1
            LossesDict[rn] = {'TickerSymbol':stock[0],'Count':Count}
            rn +=1

        lowest_loss = LossesDict[0]['Count']
        LossLeaderDict['0'] = {'Symbol':LossesDict[0]['TickerSymbol'],'Count':LossesDict[0]['Count']}
        for key,value in LossesDict.items():

            if lowest_loss > value['Count']:
                print(lowest_loss)
                LossLeaderDict[value['TickerSymbol']] = {'Symbol':value['TickerSymbol'],'Count':value['Count']}
                lowest_loss = value['Count']
        return LossLeaderDict
