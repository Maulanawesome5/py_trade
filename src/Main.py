import tkinter as tk
from tkinter import ttk
from myWidgets import menubar


selectionbar_color = "#EFF5F6"
sidebar_color = "#F5E1FD"
header_color = "#53366B"

class App(tk.Tk):
    """Root widget, widget yang paling dasar pada aplikasi"""

    def __init__(self, title:str, resolution:tuple):
        
        # # Setup utama root aplikasi
        super().__init__()
        self.title(title)
        self.geometry(f"{resolution[0]}x{resolution[1]}")
        self.minsize(resolution[0], resolution[1])
        self.iconbitmap(f".\\static\\icon\\business-color_stock_icon-icons.com_53431.ico")

        # # Widget Frame sebagai container seluruh elemen
        # Frame ini satu tingkat di atas Root
        self.mainframe = Main_Frame(self)

        # # Widget Menu (File, Edit, Setting, Help, dsb.)
        # Widget ini harus menempel ke master Root
        self.menubar = menubar.Menubar(self)
        self.config(menu=self.menubar)

        # # Widget Sidebar (Tools dan Indikator trading)
        

        # # Function untuk menampilkan window aplikasi
        self.mainloop()


class Main_Frame(ttk.Frame):
    """Frame utama satu tingkat diatas Root widget."""
    def __init__(self, parent):
        super().__init__()
        ttk.Label(self, text="Disini letak mainframe", background="red").pack()


class Sidebar(tk.Frame):
    def __init__(self, parent:tk.Frame, sub_menu_heading:str, sub_menu_options:list):
        tk.Frame.__init__(self, parent)
        self.config(bg=sidebar_color)
        self.sub_menu_heading_label = ttk.Label(self,
                                                text=sub_menu_heading,
                                                background=sidebar_color,
                                                foreground="#333333",
                                                font=("Arial", 10)) 
        self.sub_menu_heading_label.place(x=30, y=10, anchor=tk.W)

        sub_menu_sep = ttk.Separator(self, orient=tk.HORIZONTAL)
        sub_menu_sep.place(x=30, y=30, relwidth=0.8, anchor=tk.W)

        self.options = {}
        for n, x in enumerate(sub_menu_options):
            self.options[x] = tk.Button(self, text=x, background=sidebar_color,
                                        font=("Arial", 9, "bold"),
                                        border=0,
                                        cursor="hand2",
                                        activebackground="#FFFFFF")
            self.options[x].place(x=30, y=45*(n+1), anchor=tk.W)


# # Panggil interface aplikasi pada kode program dibawah
App("Prediksi Harga Saham USA", (640, 480))
