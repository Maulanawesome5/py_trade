import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf


yf.pdr_override()
Tickers = "AMZN"

data = pdr.DataReader(Tickers, start="1997-05-15", end="2023-02-06")

df = pd.DataFrame(data)

print(df)

# Menulis file excel dari dataframe
saveToExcel = pd.ExcelWriter(
    f"D:/py_trade/data/{Tickers}.xlsx",
    engine="openpyxl",
    date_format="YYYY-MM-DD"
)

df.to_excel(saveToExcel, sheet_name=f"{Tickers}")
saveToExcel.close()
