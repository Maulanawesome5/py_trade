import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np
import pandas as pd
import socket
import tkinter as tk
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, messagebox, ttk


class AbstractClass:
    """ # ABSTRACT
    \nMerupakan class untuk menyatukan function atau properties yang diwarisi oleh
    \nclass lain.
    """
    __background_color = ""
    __foreground_color = ""
    __font_settings = ("Bahnschrift", 12)

    def background(self):
        return self.__background_color

    def foreground(self):
        return self.__foreground_color

    def font(self):
        return self.__font_settings

    def is_internet_connected(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            # messagebox.showinfo("Info", "Perangkat terhubung ke internet.")
            return True
        except OSError:
            # messagebox.showerror(
            #     "Error", "Perangkat tidak terhubung ke internet")
            return False

    def openfile(self):
        path = r".\\data\\"
        filename = filedialog.askopenfilename(
            initialdir=path, title="Open DataFrame...",
            filetypes=(("Excel Workbook", ".xlsx"),
                       ("Comma Separated Value", ".csv"))
        )
        return filename


class Menubar(tk.Menu, AbstractClass):
    """ # Menubar
    \nMerupakan widget berisi menu perintah yang selalu ada pada setiap aplikasi desktop.
    \nPositioning menubar di atur di dalam Root Widget.
    """

    def __init__(self, master):
        super().__init__(master)
        self.create_widget()

    def popup(self):
        info_title = "Perhatian"
        info_message = "Maaf. Menu masih dalam tahap konstruksi, kembali lain waktu."
        response = messagebox.showinfo(info_title, info_message)

    def create_widget(self):
        """Function untuk membuat bundling widget."""

        # Menu File
        menu_file = tk.Menu(self, tearoff=0)
        menu_file.add_command(label="Open File...", command=self.openfile)
        menu_file.add_command(label="Save", command=self.popup)
        menu_file.add_command(label="Preference", command=self.popup)
        menu_file.add_command(label="Exit", command=self.quit)

        # Menu Edit
        menu_edit = tk.Menu(self, tearoff=0)
        menu_edit.add_command(label="Undo", command=self.popup)
        menu_edit.add_command(label="Redo", command=self.popup)
        menu_edit.add_command(label="Cut", command=self.popup)
        menu_edit.add_command(label="Copy", command=self.popup)
        menu_edit.add_command(label="Paste", command=self.popup)

        # Menu Selection
        menu_select = tk.Menu(self, tearoff=0)

        # Menu View
        menu_view = tk.Menu(self, tearoff=0)
        menu_view.add_command(label="Zoom In", command=self.popup)
        menu_view.add_command(label="Zoom Out", command=self.popup)
        menu_view.add_command(label="Timeframe", command=self.popup)
        menu_view.add_command(label="Economic Calendar", command=self.popup)
        menu_view.add_command(label="Market Outlook", command=self.popup)

        # Menu Help
        menu_help = tk.Menu(self, tearoff=0)
        menu_help.add_command(label="Documentation", command=self.popup)
        menu_help.add_command(label="License", command=self.popup)
        menu_help.add_command(label="Privacy Policy", command=self.popup)
        menu_help.add_command(label="Check for Updates", command=self.popup)
        menu_help.add_command(label="About", command=self.popup)

        # Menambahkan cascading menu
        self.add_cascade(label="File", menu=menu_file)
        self.add_cascade(label="Edit", menu=menu_edit)
        self.add_cascade(label="Selection", menu=menu_select)
        self.add_cascade(label="View", menu=menu_view)
        self.add_cascade(label="Help", menu=menu_help)


class Sidebar(tk.Frame):
    """ # Sidebar
    \nMerupakan widget frame yang berfungsi menampung elemen seperti tombol indikator trading.
    \nSidebar seperti pada aplikasi web, selalu terletak di samping.
    """
    __background_color = "#7deb7e"
    __foreground_color = "#000000"
    __font_settings = ("Bahnschrift", 12)

    @classmethod
    def background(cls):
        return cls.__background_color

    @classmethod
    def foreground(cls):
        return cls.__foreground_color

    @classmethod
    def font(cls):
        return cls.__font_settings

    def __init__(self, master):
        super().__init__(master)
        self["background"] = self.background()
        self.create_widget()

    def create_widget(self):
        """Function untuk membuat bundling widget, sama seperti menubar"""

        # # Group Button Moving Averages
        # Label button separator
        moving_average_group_label = tk.Label(
            self, text="MOVING AVERAGE", font=self.font(), background=self.background()
        )
        moving_average_group_label.place(in_=self, x=75, y=50, anchor=tk.NW)

        # Button Separator
        button_separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        button_separator.place(in_=self, x=30, y=80, relwidth=0.8, anchor=tk.W)

        # Trading indicator button
        SMA_Button = tk.Button(self, text="Simple Moving Average", width=30)
        SMA_Button.place(in_=self, x=45, y=100)

        WMA_Button = tk.Button(self, text="Weighted Moving Average", width=30)
        WMA_Button.place(in_=self, x=45, y=150)

        EMA_Button = tk.Button(
            self, width=30, text="Exponential Moving Average")
        EMA_Button.place(in_=self, x=45, y=200)

        # # Group Button Oscillator
        # Label button separator
        oscillator_group_label = tk.Label(
            self, text="OSCILLATOR", font=self.font(), background=self.background()
        )
        oscillator_group_label.place(in_=self, x=100, y=290, anchor=tk.NW)

        # Button Separator
        button_separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        button_separator.place(in_=self, x=30, y=320,
                               relwidth=0.8, anchor=tk.W)

        # Trading indicator button
        RSI_Button = tk.Button(self, text="Relative Strength Index", width=30)
        RSI_Button.place(in_=self, x=45, y=340)

        # # Group Button Action
        # Label button separator
        action_group_label = tk.Label(
            self, text="PREDICTION", font=self.font(), background=self.background()
        )
        action_group_label.place(in_=self, x=100, y=430, anchor=tk.NW)

        # Button Separator
        button_separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        button_separator.place(in_=self, x=30, y=460,
                               relwidth=0.8, anchor=tk.W)

        # Prediction and accuration button
        prediction_button = tk.Button(self, text="Price Prediction", width=30)
        prediction_button.place(in_=self, x=45, y=480)

        accuration_button = tk.Button(
            self, text="Accuration of Prediction", width=30)
        accuration_button.place(in_=self, x=45, y=530)


class SearchbarFrame(tk.Frame):
    """ # SearchbarFrame
    \nMerupakan widget frame untuk mengorganisir elemen pencarian data.
    \nWidget yang tergabung dalam frame ini seperti kolom dan tombol pencarian.
    """
    __font_settings = ("Bahnschrift", 12)
    __background_color = "#d0efb1"
    __foreground_color = "#9C2500"

    @classmethod
    def font(cls):
        return cls.__font_settings

    @classmethod
    def background(cls):
        return cls.__background_color

    @classmethod
    def foreground(cls):
        return cls.__foreground_color

    def __init__(self, master):
        super().__init__()
        self["background"] = self.background()


class TradingChartFrame(tk.Frame):
    """ # TradingChartFrame
    \nMerupakan widget frame untuk menempatkan grafik harga saham.
    """
    __background_color = "#4DAA57"

    @classmethod
    def background(cls):
        return cls.__background_color

    def __init__(self, master):
        super().__init__()
        self["background"] = self.background()


class FooterFrame(tk.LabelFrame):
    """ # FooterFrame
    \nMerupakan widget LabelFrame yang menempel pada MainFrame. Digunakan untuk menaruh
    \ninformasi seperti hasil prediksi, nilai akurasi prediksi, dan sebagaimana fungsi dari
    \nelemen footer dalam aplikasi web.
    """
    __font_settings = ("Bahnschrift", 10)
    __background_color = "#4daa57"
    __foreground_color = "#ffffff"

    @classmethod
    def font(cls):
        return cls.__font_settings

    @classmethod
    def background(cls):
        return cls.__background_color

    @classmethod
    def foreground(cls):
        return cls.__foreground_color

    def __init__(self, master):
        super().__init__()
        self["text"] = "Hasil Prediksi"
        self["background"] = self.background()
        self["foreground"] = self.foreground()
        self["font"] = self.font()

        # Menampilkan hasil prediksi

        self.ema5_prediction_result = tk.Label(
            self, text="EMA-5 : {}", justify=tk.LEFT,
            font=self.font(), background=self.background(),
            foreground=self.foreground(), activebackground=self.background(),
            activeforeground=self.foreground()
        )
        self.ema5_prediction_result.grid(column=0, row=0, padx=5, pady=5)

        self.ema20_prediction_result = tk.Label(
            self, text="EMA-20: {}", justify=tk.LEFT,
            font=self.font(), background=self.background(),
            foreground=self.foreground(), activebackground=self.background(),
            activeforeground=self.foreground()
        )
        self.ema20_prediction_result.grid(column=1, row=0, padx=5, pady=5)

        self.sma200_prediction_result = tk.Label(
            self, text="SMA-200: {}", justify=tk.LEFT,
            font=self.font(), background=self.background(),
            foreground=self.foreground(), activebackground=self.background(),
            activeforeground=self.foreground()
        )
        self.sma200_prediction_result.grid(column=2, row=0, padx=5, pady=5)

        self.accuracy_prediction_result = tk.Label(
            self, justify=tk.LEFT, font=self.font(),
            background=self.background(), text="Akurasi prediksi menunjukkan hasil: {}",
            foreground=self.foreground(), activebackground=self.background(),
            activeforeground=self.foreground()
        )
        self.accuracy_prediction_result.grid(column=0, row=1, columnspan=3)


class MainFrame(tk.Frame, AbstractClass):
    """ # MainFrame
    \nMerupakan widget frame satu tingkat di atas Root Widget dan menjadi container semua elemen.
    \nMemiliki banyak parameter bawaan seperti ubah warna, ukuran, indentasi, dll.
    """

    __background_color = "#d0efb1"
    __font_settings = ("Bahnschrift", 12)

    def call_dataframe(self, ticker_symbol: str | None):
        """ # CALL DATAFRAME
        \nFunction untuk memanggil data harga saham yang dicari pada kolom pencarian.
        """
        price = yf.Ticker(ticker_symbol).history(period="max")
        price = pd.DataFrame(price)
        del price["Dividends"]
        del price["Stock Splits"]

        return price

    def clear_canvas(self):
        """function untuk Hapus canvas jika ada."""
        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().destroy()

    def visualize(self, parent, ticker: str, data: pd.DataFrame):
        """ # VISUALIZE
        \nFunction untuk menampilkan visualisasi data harga yang dipanggil.
        """

        # Buat figure dan axis baru
        fig, ax = plt.subplots(1, 1)
        mpf.plot(data, type="candle", style="charles", ax=ax,
                 warn_too_much_data=5000)

        # Bersihkan canvas yang lama
        self.clear_canvas()

        # 3. Buat object FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(fig, master=parent)
        self.canvas.draw()
        self.canvas
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

    def search(self):
        """ # SEARCH
        \nMerupakan function untuk melakukan pencarian data harga saham
        \nberdasarkan kode/ticker yang dimasukkan pada entrybox oleh user.
        \nHasil pencarian ditampilkan pada widget `tradingCanvas`.
        """
        stock_code = self.entrybox.get().upper()

        if stock_code:
            try:
                # Setelah user memasukkan kode saham
                df = self.call_dataframe(ticker_symbol=stock_code)

                # Periksa koneksi internet.
                if self.is_internet_connected():
                    # Jika online, visualisasi dilakukan
                    self.visualize(parent=self.tradingCanvas,
                                   ticker=stock_code, data=df)
                else:
                    # Jika tidak terkoneksi internet, tampilkan popup
                    messagebox.showerror(
                        "Error", "Perangkat Anda tidak terhubung internet.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to retrieve data: {e}")
        else:
            messagebox.showwarning(
                "Peringatan", "Kolom pencarian tidak boleh kosong")

    def __init__(self, master: tk.Tk):
        super().__init__(master)
        # # Widget Frame Sidebar bergantung pada MainFrame
        # Instansiasi & method positioning menggunakan `.place` pada mainframe
        self.sidebar = Sidebar(self)
        self.sidebar.place(x=0, y=0, width=300, height=720, relx=0, rely=0)

        # # Widget Frame Searchbar bergantung pada MainFrame
        # Instansiasi & method positioning menggunakan `.place` pada mainframe
        self.searchbar = SearchbarFrame(self)
        self.searchbar.place(x=300, y=0, width=1280, height=80, relx=0, rely=0)

        # Kolom dan tombol pencarian
        self.entrybox = tk.Entry(self.searchbar, width=50, font=self.font())
        self.entrybox.place(x=270, y=25, height=30)

        self.submit = tk.Button(self.searchbar, width=15, text="Search",
                                font=self.font(), command=self.search,
                                background="#4daa57", foreground="#ffffff",
                                activebackground="#4daa57", activeforeground="#ffffff")
        self.submit.place(x=730, y=25)

        # # Widget Frame Trading Chart bergantung pada MainFrame
        # Instansiasi & method positioning menggunakan `.place` pada mainframe
        self.tradingframe = TradingChartFrame(self)
        self.tradingframe.place(x=320, y=100, width=1025, height=480)

        # Membuat trading canvas untuk menempatkan grafik matplotlib
        self.tradingCanvas = tk.Canvas(self.tradingframe, background="#2E2E2E")
        self.tradingCanvas.pack(expand=True, fill=tk.BOTH)

        # # Widget Frame Footer bergantung pada MainFrame
        # Instansiasi & method positioning menggunakan `.place` pada mainframe
        self.footerframe = FooterFrame(self)
        self.footerframe.place(x=300, y=600, width=1280, height=80)


class MainApps(tk.Tk):
    """Root Widget. Layer aplikasi yang paling bawah."""

    def __init__(self, title: str, resolution: tuple):
        super().__init__()

        # # Konfigurasi Root Widget
        # Root Widget = Layer paling dasar pada aplikasi
        self.title(title)
        self.geometry(f"{resolution[0]}x{resolution[1]}")
        self.minsize(resolution[0], resolution[1])
        self.iconbitmap(
            f".\\static\\icon\\business-color_stock_icon-icons.com_53431.ico")

        # # Widget Menubar (File, Edit, Setting, Help, dsb.)
        # Widget ini harus menempel ke layer root
        menubar = Menubar(self)
        self.config(menu=menubar)

        # # Widget MainFrame sebagai container seluruh elemen
        # Instansiasi & method positioning MainFrame ditaruh disini
        mainframe = MainFrame(self)
        mainframe.pack(expand=True, fill=tk.BOTH)

        self.mainloop()


MainApps("Prediksi Harga Saham USA", (1280, 720))
