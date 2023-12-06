import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MatplotlibTkinterApp:
    def __init__(self, master):
        self.master = master
        master.title("Matplotlib in Tkinter")

        # Buat object Figure dari Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        # Tambahkan subplot
        self.plot = self.fig.add_subplot(1, 1, 1)

        # Buat object FigureCanvasTkagg
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()

        # Tempatkan object canvas di widget Tkinter
        self.canvas.get_tk_widget().pack()

        # Buat tombol untuk memanggil fungsi plot_chart
        self.button = tk.Button(
            self.master, text="Plot Chart", command=self.plot_chart)
        self.button.pack()

    def plot_chart(self):
        # Gambar plot atau grafik di sini, contoh:
        self.plot.plot([1, 2, 3, 4], [10, 20, 25, 30])
        self.canvas.draw()


# Buat jendela tkinter
root = tk.Tk()

# Inisialisasi aplikasi dengan objek
app = MatplotlibTkinterApp(root)

# Jalankan aplikasi
root.mainloop()
