import tkinter as tk
from myWidgets.sidebar import Sidebar
from myWidgets.searchbar import Searchbar
from myWidgets.chartframe import ChartFrame


class MainFrame(tk.Frame):
    """
    MainFrame merupakan frame utama satu tingkat di atas root widget.
    """
    mainframe_bg = "#53366B"
    font_settings = ("Arial", 15)

    def __init__(self, parent):
        tk.Frame.__init__(self, background=self.mainframe_bg)

        # # Sidebar depends on mainframe
        self.sidebar = Sidebar(self, fontset=self.font_settings)

        # # Searchbar
        self.searchbar = Searchbar(self)

        # # Trading Chart Frame
        self.trading_chart_frame = ChartFrame(self)
        self.trading_chart_frame.place(
            x=350, y=100, width=980, height=500, bordermode="outside")
