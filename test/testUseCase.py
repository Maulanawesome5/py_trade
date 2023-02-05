import pandas as pd
import pandas_datareader as pdr
import yfinance


Tickers = ["AMZN", "GOOGL", "META", "MSFT", "TSLA"]

dfs = []

for ticker in Tickers:
    df = yfinance.Ticker(ticker)
    df = df.history(period="max")
    dfs.append(df)

# print(dfs)

dfs = pd.DataFrame(dfs, columns=Tickers)
print(dfs)
