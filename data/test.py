import yfinance as yf
import pandas as pd
import datetime as dt


tickers = ["AAPL", "AMZN", "CSCO", "GOOG", "META", "MSFT", "NFLX", "NVDA", "PYPL", "TSLA"]
start_date = dt.datetime(year=2022, month=6, day=15)
end_date = dt.datetime(year=2023, month=4, day=1)

newStock = yf.download(
    tickers=tickers,
    start=start_date,
    end=end_date,
    ignore_tz=True,
    interval="1d"
    ).drop(["Open","High","Low","Volume", "Adj Close"], axis=1)

newStock = pd.DataFrame(newStock)
save2excel = pd.ExcelWriter(r"D:/py_trade/data/[Join].xlsx", engine="openpyxl")
newStock.to_excel(save2excel)
save2excel.close()
