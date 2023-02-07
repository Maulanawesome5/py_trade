import pandas as pd
from pandas_datareader import data as pdr
import yfinance


Tickers = ["AMZN", "GOOGL", "META", "MSFT", "TSLA"]

joined_data = {
    "AMZN": yfinance.Ticker(Tickers[0]).history(period="max"),
    "GOOGL" : yfinance.Ticker(Tickers[1]).history(period="max"),
    "META" : yfinance.Ticker(Tickers[2]).history(period="max"),
    "MSFT" : yfinance.Ticker(Tickers[3]).history(period="max"),
    "TSLA" : yfinance.Ticker(Tickers[4]).history(period="max")
}

print(joined_data)
