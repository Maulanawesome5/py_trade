"""
# Sumber website
https://python-course.eu/

Penulis: Bernd Klein
Tanggal: 01 Februari 2022
"""
import tkinter as tk


root = tk.Tk()

w = tk.Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=tk.X, padx=10, pady=10)
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(padx=10, pady=10, ipadx=10)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=tk.X, padx=10, pady=10, ipady=10)

x = tk.Label(root, text="Yellow Light", bg="yellow", fg="black")
x.pack(padx=5, pady=10, side=tk.LEFT)
x = tk.Label(root, text="Purple Grape", bg="purple", fg="white")
x.pack(padx=5, pady=20, side=tk.LEFT)
x = tk.Label(root, text="Dark Gray", bg="gray", fg="black")
x.pack(padx=5, pady=20, side=tk.LEFT)

root.mainloop()
