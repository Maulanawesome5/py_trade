import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox


width_app = 640  # ukuran lebar
height_app = 480  # ukuran tinggi

# # Root Widget
root = tk.Tk()
root.geometry(f"{width_app}x{height_app}")
root.title("Prediksi Harga Saham USA")
root.iconbitmap(f".\\static\\icon\\business-color_stock_icon-icons.com_53431.ico")
root.minsize(width_app, height_app)

# # Frame Widget
#   Mainframe -> Secondary frame satu level di atas root. Menempel ke root frame.
mainframe = tk.Frame(root, background="yellow")
mainframe.pack(expand=True, fill=tk.BOTH)

#   Sidebar   -> Third frame, sebagai sidebar. Menempel ke mainframe (secondary frame)
toolbar = tk.Frame(mainframe, relief=tk.SUNKEN, background="blue", border=2, padx=30)
toolbar.grid(row=0, column=0, sticky=tk.W, ipady=height_app,
            rowspan=width_app, in_=mainframe)

#   Searchbar -> Fourth frame, sebagai searchbar.
searchFrame = tk.Frame(mainframe, background="red")
searchFrame.grid(row=0, column=1, sticky=tk.NSEW, in_=mainframe,
                pady=0, padx=0, ipady=5, ipadx=width_app, columnspan=width_app)

#   Chart     -> Fifth frame, untuk menempatkan jendela chart saham
stockChartFrame = tk.Frame(mainframe, background="green")
stockChartFrame.grid(row=1, column=1, sticky=tk.NSEW, in_=mainframe,
                    pady=0, padx=0, ipadx=width_app, ipady=height_app,
                    columnspan=height_app, rowspan=width_app)

# # Menu Widget
menu_bar = tk.Menu(root)

def openfile():
    """
    Function untuk mengakses dataframe di local computer. Support file `.xlsx` `.csv`
    * 2023/11/26 : Belum dibuatkan proses
    """
    path = r".\\data\\"
    root.filename = filedialog.askopenfilename(initialdir=path,
                                               title="Open DataFrame...",
                                               filetypes=(("Excel Workbook", ".xlsx"),("CSV", ".csv"))
                                               )

def popup():
    """
    Function untuk menampilkan interaksi berupa messagebox / dialogbox.
    * 2023/11/26 : Belum dibuatkan proses
    """
    info_title = "Perhatian"
    info_message = "Maaf. Menu masih dalam tahap konstruksi, kembali lain kali"
    response = messagebox.showinfo(info_title, info_message)

#   Menu File
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Open File...", command=openfile)
menu_file.add_command(label="Save", command=popup)
menu_file.add_command(label="Preference", command=popup)
menu_file.add_command(label="Exit", command=quit)

#   Menu Edit
menu_edit = tk.Menu(menu_bar, tearoff=0)
menu_edit.add_command(label="Terserah", command=popup)
menu_edit.add_command(label="Mau Ngapain Saja", command=popup)

#   Menu Select
menu_selection = tk.Menu(menu_bar, tearoff=0)
menu_selection.add_command(label="Terserah", command=popup)
menu_selection.add_command(label="Mau Ngapain Saja", command=popup)

#   Menu View
menu_view = tk.Menu(menu_bar, tearoff=0)
menu_view.add_command(label="Terserah", command=popup)
menu_view.add_command(label="Mau Ngapain Saja", command=popup)

#   Menu Help
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="Terserah", command=popup)
menu_help.add_command(label="Mau Ngapain Saja", command=popup)

#   Menambahkan cascading menu
menu_bar.add_cascade(label="File", menu=menu_file)
menu_bar.add_cascade(label="Edit", menu=menu_edit)
menu_bar.add_cascade(label="Selection", menu=menu_selection)
menu_bar.add_cascade(label="View", menu=menu_view)
menu_bar.add_cascade(label="Help", menu=menu_help)

# Dummy text untuk frame sidebar
indikator_trade_label = ttk.Label(toolbar, background="#9c2300", text="Trade Indicator")
indikator_trade_label.grid(row=0, column=0)

# # Search Widget
#   Entry -> Kolom pencarian untuk mencari kode saham. Widget ini menempel di searchFrame.
searchBox = ttk.Entry(searchFrame, width=40)
searchBox.insert(0, "Ticker")
searchBox.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10, in_=searchFrame)

#   Button -> Tombol untuk memulai proses pencarian. Widget ini menempel di searchFrame.
searchButton = tk.Button(searchFrame, text="Cari Saham", command=None)
searchButton.grid(row=0, column=1, sticky=tk.EW)


# Label dummy 5 frame
dummyLabel = tk.Label(stockChartFrame, text="Grafik Harga Saham")
dummyLabel.pack()

root.config(menu=menu_bar)
root.mainloop()
