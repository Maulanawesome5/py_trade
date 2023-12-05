import tkinter as tk
from myWidgets.sidebar import Sidebar
from myWidgets.searchbar import Searchbar


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

        self.test = tk.Label(self, text="MainFrame", background="blue", font=self.font_settings)
        self.test.place(x=100, y=100)

