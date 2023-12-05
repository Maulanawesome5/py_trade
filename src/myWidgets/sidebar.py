import tkinter as tk
from tkinter import ttk


class Sidebar(tk.Frame):
    """
    Sidebar widget, terletak di sebelah kiri mainframe.
    Sidebar akan digunakan untuk menampung tombol indikator trading.
    """
    sidebar_color = "#ABABAB"
    sidebar_text_color = "#000000"
    button_font_settings = ("Arial", 12)
    label_button_font_settings = ("Arial", 14)

    def __init__(self, parent, fontset: tuple):
        tk.Frame.__init__(self, parent)
        self.config(background=self.sidebar_color)

        # # Group Button

        # Label button separator
        indicator_group_label = tk.Label(self,
                                         text="Moving Average",
                                         font=self.label_button_font_settings,
                                         background=self.sidebar_color
                                         )
        indicator_group_label.place(in_=self, x=75, y=50, anchor=tk.NW)

        # Button separator
        button_separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        button_separator.place(in_=self, x=25, y=80, relwidth=0.8, anchor=tk.W)

        # Button trading indicator
        self.simple_MA = IndicatorButton(
            self, "Simple Moving Average", self.button_font_settings)
        self.simple_MA.place(in_=self, x=55, y=100)

        self.weighted_MA = IndicatorButton(
            self, "Weighted Moving Average", self.button_font_settings)
        self.weighted_MA.place(in_=self, x=55, y=150)

        self.exp_MA = IndicatorButton(
            self, "Exponential Moving Average", self.button_font_settings)
        self.exp_MA.place(in_=self, x=55, y=200)


class IndicatorButton(tk.Button):
    """
    Indikator Trading berupa widget button. Nantinya ada 1 indikator yaitu Moving Average (MA).
    Terdapat 3 jenis MA yaitu:
    * Simple Moving Average
    * Weighted Moving Average
    * Exponential Moving Average
    """

    def __init__(self, parent, buttonName: str, fontSet: tuple):
        tk.Button.__init__(self, parent, text=buttonName, font=fontSet)
