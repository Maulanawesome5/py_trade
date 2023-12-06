import tkinter as tk
import yfinance as yf
import mplfinance as mpf
from mpl_finance import candlestick_ohlc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates


class StockVisualizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Stock Visualizer")

        self.ticker_entry = tk.Entry(master)
        self.ticker_entry.pack()

        self.button = tk.Button(
            master, text="Visualizer Stock", command=self.visualize_stock)
        self.button.pack()

        self.button = tk.Button(
            master, text="Candlestick Old", command=self.visualize_candlestick)
        self.button.pack()

        # Upgrade latest mplfinace
        self.button = tk.Button(
            master, text="Candlestick New", command=self.visualize_candlestick_new)
        self.button.pack()

        # Buatlah object figure dari Matplotlib
        self.fig = Figure(figsize=(8, 6), dpi=100)
        # Tambahkan subplot
        self.plot = self.fig.add_subplot(1, 1, 1)

        # Buat object FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def visualize_stock(self):
        ticker_symbol = self.ticker_entry.get()

        # Dapatkan data saham menggunakan yfinance
        stock_data = yf.download(
            ticker_symbol, start="2022-01-01", end="2023-01-01")

        # Gambar grafik harga penutup saham
        self.plot.clear()
        self.plot.plot(stock_data["Close"])
        self.plot.set_title(f"Stock Price for {ticker_symbol}")
        self.plot.set_xlabel("Date")
        self.plot.set_ylabel("Closing Price")

        self.canvas.draw()

    def visualize_candlestick(self):
        """
        Function ini untuk membuat visualisasi grafik harga saham menjadi Candlestick.\n
        Mekanisme function ini adalah:
        1. Menerima input berupa string ticker dari widget Entry `tkinter`.
        2. Input yang diterima akan diproses oleh modul `yfinance`.
        3. Modul `yfinance` akan memperoleh data harga saham dengan metode web scrapping.
        4. Selanjutnya proses pembuatan figure dan plot akan ditangani oleh `matplotlib`.
        5. Candlestick chart di bentuk dengan modul `mpl-finance`.
        \nWarning:\n
        Modul `mpl-finance` sudah deprecated. Sebaiknya diganti dengan modul `mplfinance`.
        """
        ticker_symbol = self.ticker_entry.get()

        # Dapatkan data saham menggunakan yfinance
        stock_data = yf.download(
            ticker_symbol, start="2022-01-01", end="2023-01-01")

        # Ubah indeks tanggal ke dalam format matplotlib dates
        stock_data.reset_index(inplace=True)
        stock_data["Date"] = stock_data["Date"].map(mdates.date2num)

        # Gambar candlestick harga saham
        self.plot.clear()
        candlestick_ohlc(self.plot, stock_data.values, width=0.6,
                         colorup="g", colordown="r", alpha=0.8)

        self.plot.set_title(f"Stock Price for {ticker_symbol}")
        self.plot.set_xlabel("Date")
        self.plot.set_ylabel("Price")

        # Format tanggal di sumbu x (horizontal)
        self.plot.xaxis_date()
        self.plot.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

        self.canvas.draw()

    def visualize_candlestick_new(self):
        """
        Function ini untuk membuat visualisasi grafik harga saham menjadi Candlestick.\n
        Mekanisme function ini adalah:
        1. Menerima input berupa string ticker dari widget Entry `tkinter`.
        2. Input yang diterima akan diproses oleh modul `yfinance`.
        3. Modul `yfinance` akan memperoleh data harga saham dengan metode web scrapping.
        4. Selanjutnya proses pembuatan figure dan plot akan ditangani oleh `matplotlib`.
        5. Candlestick chart di bentuk dengan modul `mplfinance`.
        """
        ticker_symbol = self.ticker_entry.get()

        # Dapatkan data saham menggunakan yfinance
        stock_data = yf.download(
            ticker_symbol, start="2022-01-01", end="2023-01-01")

        # Gambar candlestick harga saham
        self.plot.clear()
        mpf.plot(stock_data, type="candle", style="yahoo",
                 mav=(20, 200), volume=True)

        self.plot.set_title(f"Stock Price for {ticker_symbol}")
        self.plot.set_xlabel("Date")
        self.plot.set_ylabel("Price")

        self.canvas.draw()


# Buat jendela Tkinter
root = tk.Tk()
# Inisialisasi aplikasi dengan object StockVisualizerApp
app = StockVisualizerApp(root)
# Jalankan loop Tkinter
root.mainloop()
