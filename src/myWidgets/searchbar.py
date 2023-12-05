import tkinter as tk


class Searchbar(tk.Frame):
    """
    Searchbar merupakan frame untuk menempatkan widget Entry dan Button.
    Berfungsi untuk menerima input berupa ticker saham. Keyword pencarian akan
    diproses oleh modul `yfinance`.
    """
    # searchbar_bg = "#F5E1FD"
    searchbar_bg = "red"
    font_settings = ("Arial", 15)

    def __init__(self, parent):
        tk.Frame.__init__(self, background=self.searchbar_bg)
        myLabel = tk.Label(self, text="Kolom Pencarian", font=self.font_settings)
        myLabel.pack()

