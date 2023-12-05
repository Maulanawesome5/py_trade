import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


class MyApp(tk.Tk):
    house_prices = np.random.normal(200000, 250000, 5000)

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Tutorial from freecodecamp.org')
        self.iconbitmap(
            '.\\static\\icon\\business-color_stock_icon-icons.com_53431.ico')
        self.geometry("400x200")

        my_button = tk.Button(self, text="Graph It !", command=self.graph)
        my_button.pack()

    @staticmethod
    def graph():
        plt.hist(MyApp.house_prices, 50)
        plt.show()


app = MyApp()
app.mainloop()
