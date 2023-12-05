import tkinter as tk
from myWidgets import menubar, mainframe


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
        self.mainframe = mainframe.MainFrame(self)
        self.mainframe.pack(expand=True, fill=tk.BOTH)

        # # Widget Menu (File, Edit, Setting, Help, dsb.)
        # Widget ini harus menempel ke master Root
        self.menubar = menubar.Menubar(self)
        self.config(menu=self.menubar)

        # # Widget Sidebar
        # Pengaturan Layout sidebar saya taruh sini supaya bisa mendeteksi 
        # secara otomatis tinggi (height) resolusi layar
        self.mainframe.sidebar.place(x=0, y=0, width=300, height=self.winfo_height())

        # # Function untuk menampilkan window aplikasi
        self.mainloop()


# # Panggil interface aplikasi pada kode program dibawah
App("Prediksi Harga Saham USA", (1280, 720))
