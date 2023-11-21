import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    """Root aplikasi yang akan ditampilkan pertama kali."""
    def __init__(self, title:str, resolution:tuple):
        super().__init__()
        self.title(title)
        self.geometry(f"{resolution[0]}x{resolution[1]}")
        self.minsize(resolution[0], resolution[1])
        self.iconbitmap(f"..\\static\\icon\\business-color_stock_icon-icons.com_53431.ico")

        # Widget (seperti Button, Menu, dsb.)
        self.mainframe = Main_Frame(self)
        self.mainframe.grid(row=0, column=1)

        self.menubar = Menubar(self)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=2)

        self.tombol = None
        
        # Function untuk menampilkan window aplikasi
        self.mainloop()


class Main_Frame(ttk.Frame):
    """Frame utama satu tingkat diatas Root widget."""
    def __init__(self, parent):
        super().__init__()
        ttk.Label(self, text="Disini letak mainframe", background="red").pack()


class Menubar(tk.Menu):
    def __init__(self, parent):
        pass


class Sidebar(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        ttk.Label(self, text="Disini letak frame sidebar", background="blue").pack()


# # Panggil interface aplikasi pada kode program dibawah
App("Prediksi Harga Saham USA", (640, 480))
