from tkinter import messagebox
import tkinter as tk


class Searchbar(tk.Frame):
    """
    Searchbar merupakan frame untuk menempatkan widget Entry dan Button.
    Berfungsi untuk menerima input berupa ticker saham. Keyword pencarian akan
    diproses oleh modul `yfinance`.
    """
    __background_color = "#d0efb1"
    __font_settings = ("Arial", 15)

    @property
    def background_color(self):
        pass

    @property
    def font_settings(self):
        pass

    @property
    def searching(self):
        pass

    @classmethod
    def get_background_color(cls):
        return cls.__background_color

    @classmethod
    def get_font_settings(cls):
        return cls.__font_settings

    def __init__(self, parent):

        tk.Frame.__init__(self, background=self.get_background_color())

        # EntryBox -> Kolom pencarian ticker saham
        self.kolom_pencarian = EntryBox(self, 50, self.get_font_settings())
        self.kolom_pencarian.place(x=200, y=25, in_=self, height=30)

        # Button -> Tombol untuk memulai proses pencarian ticker
        self.tombol_pencarian = SubmitButton(
            self, width=10, fontset=("Arial", 14), text="Temukan", command=self.pencarian)
        self.tombol_pencarian.place(x=770, y=23, in_=self)

    def pencarian(self):
        q = self.kolom_pencarian.get().upper()
        if q == "":
            messagebox.showerror(
                "Error", "Kolom pencarian tidak boleh kosong.")
        else:
            mylabel = tk.Label(
                self, text=f"Keyword yang anda masukkan: {q}", font=self.get_font_settings())
            mylabel.pack()


class EntryBox(tk.Entry):
    def __init__(self, parent, width: int, fontset: tuple):
        tk.Entry.__init__(self, width=width, font=fontset)


class SubmitButton(tk.Button):
    def __init__(self, parent, width: int, fontset: tuple, text: str, command):
        tk.Button.__init__(self, width=width, font=fontset, text=text, command=command,
                           background="#4daa57", foreground="#ffffff",
                           activebackground="#4daa57", activeforeground="#ffffff")
