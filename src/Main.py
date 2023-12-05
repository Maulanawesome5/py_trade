import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image


selectionbar_color = "#EFF5F6"
sidebar_color = "#F5E1FD"
header_color = "#53366B"

class App(tk.Tk):
    """Root widget, widget yang paling dasar pada aplikasi"""
    image_resolution = (50,50)

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
        self.menubar = Menubar(self)
        self.config(menu=self.menubar)

        # # Widget Sidebar (Tools dan Indikator trading)
        # Membuat frame untuk sidebar
        self.sidebar = tk.Frame(self, background=sidebar_color)
        self.sidebar.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        
        # Logo aplikasi
        self.brand_frame = tk.Frame(self.sidebar, bg=sidebar_color)
        self.brand_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        self.logo_kampus = ImageTk.PhotoImage(
            Image.open(f".\\static\\icon\\unnamed.png").resize(self.image_resolution)
            )
        logo = tk.Label(self.brand_frame, image=self.logo_kampus, bg=sidebar_color)
        logo.place(x=50, y=20)

        # Tools dan Trading Indikator di Sidebar
        self.submenu_frame = tk.Frame(self.sidebar, background=sidebar_color)
        self.submenu_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.85)

        att_submenu = Sidebar(self.submenu_frame,
                              sub_menu_heading="TRADE INDICATOR",
                              sub_menu_options=["Indikator 1", "Indikator 2"])

        att_submenu.options["Indikator 1"].config(command=lambda: self.show_frame(Frame1))
        att_submenu.options["Indikator 2"].config(command=lambda: self.show_frame(Frame2))
        att_submenu.place(relx=0, rely=0.025, relwidth=1, relheight=0.3)

        # Multipage
        container = tk.Frame(self)
        container.config(highlightbackground="#808080", highlightthickness=0.5)
        container.place(relx=0.3, rely=0.1, relwidth=0.7, relheight=0.9)

        self.frames = {}

        for F in (Frame1, Frame2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame(Frame1)

        # # Function untuk menampilkan window aplikasi
        self.mainloop()
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


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

    def openfile(self):
        """
        Function untuk mengakses dataframe di local computer. Support file `.xlsx` `.csv`
        * 2023/11/26 : Belum dibuatkan proses
        """
        path = r".\\data\\"
        self.filename = filedialog.askopenfilename(initialdir=path,
                                                   title="Open DataFrame...",
                                                   filetypes=(("Excel Workbook", ".xlsx"), ("CSV", ".csv"))
                                                   )
    
    def popup(self):
        """
        Function untuk menampilkan interaksi berupa messagebox / dialogbox.
        * 2023/11/26 : Belum dibuatkan proses
        """
        info_title = "Perhatian"
        info_message = "Maaf. Menu masih dalam tahap konstruksi, kembali lain waktu."
        response = messagebox.showinfo(info_title, info_message)

    def create_widget(self):
        """Function untuk membuat komponen Menu bar."""
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


class Frame1(tk.Frame):
    """
    Frame ini akan muncul ketika user menekan tulisan "Indikator 1"
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CHART SAHAM", font=("Arial", 15))
        label.pack()


class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="INI FRAME 2", font=("Arial", 15))
        label.pack()


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
