"""
# Sumber website
ActiveState

Penulis: -
Tanggal: 29 Oktober 2020
"""
import tkinter as tk

root = tk.Tk()

# # Vertical Position
a = tk.Label(root, text="Red", bg="red", fg="white")
a.pack(side=tk.BOTTOM)
a = tk.Label(root, text="Green", bg="green", fg="white")
a.pack(side=tk.BOTTOM)
a = tk.Label(root, text="Purple", bg="purple", fg="white")
a.pack(side=tk.BOTTOM)

# # Side-by-Side Position
b = tk.Label(root, text="blue", bg="blue", fg="white")
b.pack(padx=5, pady=15, side=tk.LEFT)
b = tk.Label(root, text="gray", bg="gray", fg="black")
b.pack(padx=5, pady=20, side=tk.LEFT)
b = tk.Label(root, text="yellow", bg="yellow", fg="black")
b.pack(padx=5, pady=20, side=tk.LEFT)


tk.mainloop()
