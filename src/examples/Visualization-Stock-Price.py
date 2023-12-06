import tkinter as tk
import yfinance as yf
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StockVisualizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Stock Visualizer")

        self.ticker_entry = tk.Entry(master)
        self.ticker_entry.pack()

        self.button = tk.Button(
            master, text="Visualizer Stock", command=self.visualize_stock)
        self.button.pack()

        # Buatlah object figure dari Matplotlib
        self.fig = Figure(figsize=(8, 6), dpi=100)
        # Tambahkan subplot
        self.plot = self.fig.add_subplot(1, 1, 1)

        # Buat object FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

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


# Buat jendela Tkinter
root = tk.Tk()
# Inisialisasi aplikasi dengan object StockVisualizerApp
app = StockVisualizerApp(root)
# Jalankan loop Tkinter
root.mainloop()
