import matplotlib.pyplot as plt
import pandas as pd


folder = "D:/py_trade/data/AMZN.xlsx"

df = pd.read_excel(folder).drop(["Adj Close", "Volume"], axis=1)
df = pd.DataFrame(df).set_index("Date")

print(df) # Jumlah / len data = 6474

def SimpleMovingAverage(len_days=1):
    """Function untuk menghitung indikator Simple MA harga saham"""
    pass


def ExponentialMovingAverage():
    pass

