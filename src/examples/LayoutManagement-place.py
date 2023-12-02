"""
# Sumber website
https://python-course.eu/

Penulis: Bernd Klein
Tanggal: 01 Februari 2022
"""
import tkinter as tk
import random


root = tk.Tk()
root.geometry("170x200+30+30")  # Width x Height + x_offset + x_offset

languages = ["C++", "Java", "Perl", "Python", "Tcl/Tk"]
labels = range(5)

for i in range(5):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    l = tk.Label(root, 
                text=languages[i], 
                fg='White' if brightness < 120 else 'Black', 
                bg=bg_colour)
    l.place(x = 20, y = 30 + i*30, width=120, height=25)

root.mainloop()
