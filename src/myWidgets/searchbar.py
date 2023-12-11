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

        self.kolom_pencarian = EntryBox(self, 50, self.font_settings)
        self.kolom_pencarian.place(x=200, y=25, in_=self, height=30)

        self.tombol_pencarian = SubmitButton(
            self, width=10, fontset=("Arial", 14), text="Temukan")
        self.tombol_pencarian.place(x=770, y=23, in_=self)


class EntryBox(tk.Entry):
    def __init__(self, parent, width: int, fontset: tuple):
        tk.Entry.__init__(self, width=width, font=fontset)


class SubmitButton(tk.Button):
    def __init__(self, parent, width: int, fontset: tuple, text: str):
        tk.Button.__init__(self, width=width, font=fontset, text=text)
