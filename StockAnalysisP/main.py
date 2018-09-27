
import sys,subprocess
dependencies = ['pandas','quandl']
subprocess.call([sys.executable,'-m','pip','install'] + dependencies)
import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path,"Classes"))
sys.path.append(os.path.join(dir_path,"Util"))

from StockAnalyticalPackage import StockAnalyticalPackage
from Stockobj import Stockobj
from json_parser import json_parser
from SystemScanner import getCurrentSystem





def main():

    #Since I don't have access to a database I am using xml to configure the actions
    #of this script.
    TickerSymbolConfig = os.path.join(dir_path,'config','TickerSymbolConfig.json')
    FunctionListConfig =os.path.join(dir_path,'config','FunctionListConfig.json')

    #ListOfTickerSymbols is used to get the ticker symbols and date
    #ranges for each symbol required to run
    #This way you don't have to change the code to run
    #new ticker symbols
    ListOfTickerSymbols = json_parser(TickerSymbolConfig)

    #The FunctionListJson variable contains all the functions
    #from the requirements document
    #Now if more functions are added, there does not need to be new
    #logic added for each new function in the main script. Instead you
    #can add the functions to the json file
    FunctionListJson = json_parser(FunctionListConfig)

    #This list will hold all of the stock objects and the price history info
    ListOfStockObjs ={}

    for TickerSymbol in ListOfTickerSymbols.items():

        #This creates a new stock object which will be put into a list
        #in order to run all of the functions on later
        new_StockObj = Stockobj(TickerSymbol[1]['TickerSymbol']
                                        ,TickerSymbol[1]['Start_Date']
                                        ,TickerSymbol[1]['End_Date'])
        ListOfStockObjs[TickerSymbol[1]['TickerSymbol']]=(new_StockObj)
        #end for loop

    StockAnalyticalTool = StockAnalyticalPackage(ListOfStockObjs)
    print('Please enter the value 1 - ' +str(len(FunctionListJson)) +' to call one of functions or enter "x" to escape')
    command = "1"
    while(command != 'x'):

        #
        for functionName in FunctionListJson.items():
            print (functionName[0]+': '+functionName[1]['Desc'])
        command = input().strip()
        if command.isdigit():

            if int(command) <= len(FunctionListJson) and int(command) >=1:


                method_to_call = getattr(StockAnalyticalTool, FunctionListJson[command]['functionName'])
                result = method_to_call()
                print(FunctionListJson[command]['DictName'])
                print(result)
            else:
                print('Incorrect input. Please select a numeric option that is between 1 - ' +str(len(FunctionListJson)))
        else:
            print('Incorrect input. Please select one of the numeric options')
        print('Please enter the value 1 - ' +str(len(FunctionListJson)) +' to call one of functions or enter "x" to escape')
    #End while loop



if __name__== "__main__":
  main()
