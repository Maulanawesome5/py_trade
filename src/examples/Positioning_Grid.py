"""
# Sumber website
ActiveState

Penulis: -
Tanggal: 29 Oktober 2020
"""
import tkinter as tk

root = tk.Tk()

tk.Label(text="Position 1", width=10).grid(row=0, column=0)
tk.Label(text="Position 2", width=10).grid(row=0, column=1)
tk.Label(text="Position 3", width=10).grid(row=1, column=0)
tk.Label(text="Position 4", width=10).grid(row=1, column=1)


tk.mainloop()
