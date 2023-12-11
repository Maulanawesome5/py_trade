import tkinter as tk


class ChartFrame(tk.Frame):
    # Class variable
    __background_color = "#426a5a"
    __font_settings = ("Arial", 15)

    def __init__(self, parent):
        tk.Frame.__init__(self, background=self.get_background_color(),
                          width=300, height=300, border=2, borderwidth=2)

        # Dummy Label
        tk.Label(self, text="TRADING CHART",
                 font=self.get_font_settings()).pack()

    @classmethod
    def get_background_color(cls):
        return cls.__background_color

    @classmethod
    def get_font_settings(cls):
        return cls.__font_settings
