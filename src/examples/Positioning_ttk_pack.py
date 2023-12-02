"""
# Sumber website
ActiveState

Penulis: -
Tanggal: 29 Oktober 2020

# Note
Importing tkinter.ttk after importing tkinter causes Ttk widgets to automatically replace
the standard Tk widgets of Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow,
Radiobutton, Scale and Scrollbar. 

Important:
The basic idea is to separate as much as possible the code implementing a widget's behavior
from the code implementing its appearance (Style()).

Keep in mind that while Ttk widgets have a Style()padding option, it does not affect widget positioning.
"""
from tkinter import *
from tkinter.ttk import *


root = Tk()

# Style() padding adds pixels inside the Button. The widget’s position is not changed.
Style().configure("TButton", padding=5, relief="flat")
button1 = Button(text="Button Example")

# pack() padding adds pixels outside the TButton. The widget’s position is changed.
button1.pack(side = BOTTOM, padx=50, pady=50)

root.mainloop()
