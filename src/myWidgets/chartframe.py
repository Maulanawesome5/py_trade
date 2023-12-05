import tkinter as tk


class ChartFrame(tk.Frame):
    chartframe_bg = "#FFFF00"
    font_settings = ("Arial", 15)

    def __init__(self, parent):
        tk.Frame.__init__(self, background=self.chartframe_bg, width=300, height=300, border=2, borderwidth=2)
        
        # Dummy Label
        tk.Label(self, text="TRADING CHART", font=self.font_settings).pack()

