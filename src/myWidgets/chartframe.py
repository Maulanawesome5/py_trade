import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .searchbar import Searchbar


class ChartFrame(tk.Frame):
    # Class variable
    __background_color = "#426a5a"
    __font_settings = ("Arial", 15)

    @property
    def background_color(self):
        pass

    @property
    def font_settings(self):
        pass

    @classmethod
    def get_background_color(cls):
        return cls.__background_color

    @classmethod
    def get_font_settings(cls):
        return cls.__font_settings

    @Searchbar.searching.getter
    def searching(self):
        # q = self.kolom_pencarian.get().upper()
        # if q == "":
        #     messagebox.showerror(
        #         "Error", "Kolom pencarian tidak boleh kosong.")
        # else:
        #     myLabel = tk.Label(
        #         self, text=f"Keyword yang anda masukkan: {q}", font=self.get_font_settings())
        #     myLabel.place()
        pass

    @background_color.getter
    def background_color(self):
        return self.__background_color

    @font_settings.getter
    def font_settings(self):
        return self.__font_settings

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background=self.get_background_color(),
                          width=300, height=300, border=2, borderwidth=2)

        # Dummy Label
        tk.Label(self, text="TRADING CHART",
                 font=self.get_font_settings()).pack()
