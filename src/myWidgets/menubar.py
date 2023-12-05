import tkinter as tk
from tkinter import filedialog, messagebox


class Menubar(tk.Menu):
    """
    Widget Menubar untuk pilihan perintah pada aplikasi.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widget()
    
    def openfile(self):
        """
        Function untuk mengakses dataframe di local computer. Support terhadap ekstensi file `.xlsx` dan `.csv`
        * 2023/11/26 : Belum dibuatkan proses.
        """
        path = r".\\data\\"
        self.filename = filedialog.askopenfilename(initialdir=path,
                                                   title="Open DataFrame...",
                                                   filetypes=(("Excel Workbook", ".xlsx"), ("CSV", ".csv"))
                                                   )
    
    def popup(self):
        """
        Function untuk menampilkan interaksi berupa messagebox / dialogbox.
        * 2023/11/26 : Belum dibuatkan proses.
        """
        info_title = "Perhatian"
        info_message = "Maaf. Menu masih dalam tahap konstruksi, kembali lain waktu."
        response = messagebox.showinfo(info_title, info_message)

    def create_widget(self):
        """
        Function untuk membuat komponen widget menubar. Beberapa menu saja yang berfungsi.
        Lainnya hanya dummy.
        """
        # Menu file
        menu_file = tk.Menu(self, tearoff=0)
        menu_file.add_command(label="Open File...", command=self.openfile)
        menu_file.add_command(label="Save", command=self.popup)
        menu_file.add_command(label="Preference", command=self.popup)
        menu_file.add_command(label="Exit", command=self.quit)

        # Menu edit
        menu_edit = tk.Menu(self, tearoff=0)
        menu_edit.add_command(label="Terserah", command=self.popup)
        menu_edit.add_command(label="Mau Ngapain", command=self.popup)

        # Menu selection
        menu_selection = tk.Menu(self, tearoff=0)
        menu_selection.add_command(label="Terserah", command=self.popup)
        menu_selection.add_command(label="Mau Ngapain", command=self.popup)

        # Menu view
        menu_view = tk.Menu(self, tearoff=0)
        menu_view.add_command(label="Terserah", command=self.popup)
        menu_view.add_command(label="Mau Ngapain", command=self.popup)

        # Menu help
        menu_help = tk.Menu(self, tearoff=0)
        menu_help.add_command(label="Terserah", command=self.popup)
        menu_help.add_command(label="Mau Ngapain", command=self.popup)

        # Menambahkan cascading menu
        self.add_cascade(label="File", menu=menu_file)
        self.add_cascade(label="Edit", menu=menu_edit)
        self.add_cascade(label="Selection", menu=menu_selection)
        self.add_cascade(label="View", menu=menu_view)
        self.add_cascade(label="Help", menu=menu_help)

