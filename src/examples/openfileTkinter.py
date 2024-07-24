# # Tutorial untuk membuka file melalui aplikasi Tkinter
# # https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import filedialog as fd


def openfile():
    """Function ini akan mengembalikan nilai berupa string alamat folder dan nama file yang diakses."""
    path = r".\\.\\data\\"
    supported_types = (("Comma Separated Value", ".csv"),
                       ("Excel Workbook", ".xlsx")
                       )
    filename = fd.askopenfilename(
        initialdir=path, title="Open DataFrame", filetypes=supported_types)

    return filename


def dataframe(file_location: str):
    try:
        if file_location.endswith(".csv"):
            df = pd.read_csv(file_location)
            return df
        if file_location.endswith(".xlsx"):
            df = pd.read_excel(file_location)
            return df
    except:
        return False


print(dataframe(openfile()))


# # root window
# root = tk.Tk()
# root.title("My Aplikasi")
# root.resizable(False, False)
# root.geometry("550x250")

# # Text Editor
# text = tk.Text(root, height=12)
# text.grid(column=0, row=0, sticky="nsew")


# def open_text_file():
#     filetypes = (("text file", "*.txt"), ("All files", "*.*"))
#     f = fd.askopenfile(filetypes=filetypes)
#     text.insert('1.0', f.readlines())


# # open file button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=open_text_file
# )

# open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)


# root.mainloop()


# directory = "D:/py_trade/data/AAPL.csv"
# print("Apakah file berformat .csv? {}".format(directory.endswith(".csv")))

# directory = "D:/py_trade/data/AAPL.xlsx"
# print("Apakah file berformat .xlsx? {}".format(directory.endswith(".xlsx")))
