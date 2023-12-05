import tkinter as tk


class Sidebar(tk.Frame):
    """
    Sidebar widget, terletak di sebelah kiri mainframe.
    Sidebar akan digunakan untuk menampung tombol indikator trading.
    """
    sidebar_color = "#ABABAB"
    sidebar_text_color = "#000000"

    def __init__(self, parent, fontset=tuple):
        tk.Frame.__init__(self, parent, background=self.sidebar_color)
        self.config(background=self.sidebar_color)

        # Dummy text
        tk.Label(self, text="TEMPAT SIDEBAR", font=fontset).pack(expand=True, fill="both", in_=self)

