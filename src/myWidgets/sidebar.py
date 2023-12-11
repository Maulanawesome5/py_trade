import tkinter as tk
from tkinter import ttk


class Sidebar(tk.Frame):
    """
    Sidebar widget, terletak di sebelah kiri mainframe.
    Sidebar akan digunakan untuk menampung tombol indikator trading.
    """
    __background_color = "#7deb7e"
    __foreground_color = "#000000"
    __font_settings = ("Arial", 14)

    def __init__(self, parent, fontset: tuple):
        tk.Frame.__init__(self, parent)
        self.config(background=self.get_background_color())

        # # Group Button

        # Label button separator
        indicator_group_label = tk.Label(self,
                                         text="Moving Average",
                                         font=self.get_font_settings(),
                                         background=self.get_background_color()
                                         )
        indicator_group_label.place(in_=self, x=75, y=50, anchor=tk.NW)

        # Button separator
        button_separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        button_separator.place(in_=self, x=25, y=80, relwidth=0.8, anchor=tk.W)

        # Button trading indicator
        self.simple_MA = IndicatorButton(self, "Simple Moving Average")
        self.simple_MA.place(in_=self, x=55, y=100)

        self.weighted_MA = IndicatorButton(self, "Weighted Moving Average")
        self.weighted_MA.place(in_=self, x=55, y=150)

        self.exp_MA = IndicatorButton(self, "Exponential Moving Average")
        self.exp_MA.place(in_=self, x=55, y=200)

    @classmethod
    def get_background_color(cls):
        return cls.__background_color

    @classmethod
    def get_foreground_color(cls):
        return cls.__foreground_color

    @classmethod
    def get_font_settings(cls):
        return cls.__font_settings


class IndicatorButton(tk.Button):
    """
    Indikator Trading berupa widget button. Nantinya ada 1 indikator yaitu Moving Average (MA).
    Terdapat 3 jenis MA yaitu:
    * Simple Moving Average
    * Weighted Moving Average
    * Exponential Moving Average
    """
    __font_settings = ("Arial", 12)

    def __init__(self, parent, buttonName: str):
        tk.Button.__init__(self, parent, text=buttonName,
                           font=self.get_font_settings())

    @classmethod
    def get_font_settings(cls):
        return cls.__font_settings
