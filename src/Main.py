import tkinter as tk
from tkinter import ttk


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
        self.mainframe = Main_Frame(self).tk_setPalette(background="yellow")

        # # Widget Menu (File, Edit, Setting, Help, dsb.)
        # Widget ini harus menempel ke master Root
        self.menubar = Menubar(self)
        self.config(menu=self.menubar)

        self.sidebar = Sidebar(self).tk_setPalette(background="green")
        
        # # Function untuk menampilkan window aplikasi
        self.mainloop()


class Main_Frame(ttk.Frame):
    """Frame utama satu tingkat diatas Root widget."""
    def __init__(self, parent):
        super().__init__()
        ttk.Label(self, text="Disini letak mainframe", background="red").pack()

        # # Widget Frame sebagai sidebar
        # Posisi di samping kiri aplikasi
        # self.sidebar = Sidebar(self).tk_setPalette(background="green")

        # # Positioning widget mainframe
        self.grid(row=0, column=1, sticky=tk.NSEW)


class Menubar(tk.Menu):
    """Widget Menubar untuk pilihan perintah aplikasi"""
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widget()

    def create_widget(self):
        """Function untuk membuat komponen Menu bar."""
        # Menu file
        menu_file = tk.Menu(self, tearoff=0)
        menu_file.add_command(label="Open File...")
        menu_file.add_command(label="Save")
        menu_file.add_command(label="Preference")
        menu_file.add_command(label="Exit", command=self.quit)

        # Menu edit
        menu_edit = tk.Menu(self, tearoff=0)
        menu_edit.add_command(label="Terserah")
        menu_edit.add_command(label="Mau Ngapain")

        # Menu selection
        menu_selection = tk.Menu(self, tearoff=0)
        menu_selection.add_command(label="Terserah")
        menu_selection.add_command(label="Mau Ngapain")

        # Menu view
        menu_view = tk.Menu(self, tearoff=0)
        menu_view.add_command(label="Terserah")
        menu_view.add_command(label="Mau Ngapain")

        # Menu help
        menu_help = tk.Menu(self, tearoff=0)
        menu_help.add_command(label="Terserah")
        menu_help.add_command(label="Mau Ngapain")

        # Menambahkan cascading menu
        self.add_cascade(label="File", menu=menu_file)
        self.add_cascade(label="Edit", menu=menu_edit)
        self.add_cascade(label="Selection", menu=menu_selection)
        self.add_cascade(label="View", menu=menu_view)
        self.add_cascade(label="Help", menu=menu_help)


class Sidebar(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        ttk.Label(self, text="Disini letak frame sidebar", background="blue").pack()
        self.grid(row=0, column=0, rowspan=6, sticky=tk.NSEW)


# # Panggil interface aplikasi pada kode program dibawah
App("Prediksi Harga Saham USA", (640, 480))
