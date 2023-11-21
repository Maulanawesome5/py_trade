import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("640x480")
root.title("Prediksi Harga Saham USA")

menu_bar = tk.Menu(root)

menu_1 = tk.Menu(menu_bar, tearoff=0)
menu_1.add_command(label="Open File...")
menu_1.add_command(label="Save")
menu_1.add_command(label="Preference")
menu_1.add_command(label="Exit")

menu_2 = tk.Menu(menu_bar, tearoff=0)
menu_2.add_command(label="Terserah")
menu_2.add_command(label="Mau Ngapain Saja")

menu_3 = tk.Menu(menu_bar, tearoff=0)
menu_3.add_command(label="Terserah")
menu_3.add_command(label="Mau Ngapain Saja")

menu_4 = tk.Menu(menu_bar, tearoff=0)
menu_4.add_command(label="Terserah")
menu_4.add_command(label="Mau Ngapain Saja")

menu_5 = tk.Menu(menu_bar, tearoff=0)
menu_5.add_command(label="Terserah")
menu_5.add_command(label="Mau Ngapain Saja")

menu_bar.add_cascade(label="File", menu=menu_1)
menu_bar.add_cascade(label="Edit", menu=menu_2)
menu_bar.add_cascade(label="Selection", menu=menu_3)
menu_bar.add_cascade(label="View", menu=menu_4)
menu_bar.add_cascade(label="Help", menu=menu_5)

# Secondary frame, satu level di atas root
mainframe = tk.Frame(root)
mainframe.grid(row=0, column=1)

# Third frame, sebagai sidebar
toolbar = tk.Frame(mainframe, relief=tk.SUNKEN, height=480, border=2, padx=25, pady=450, width=480)
toolbar.grid(row=0, column=0, ipady=10)

indikator_trade_label = tk.Label(toolbar, text="Trade Indicator")
indikator_trade_label.grid(row=0, column=0)




root.config(menu=menu_bar)
root.mainloop()
