import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_chart():
    # Buat objek Figure dari Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    # Tambahkan subplot
    plot = fig.add_subplot(1, 1, 1)
    # Gambar grafik atau plot disini, contoh:
    plot.plot([1, 2, 3, 4], [10, 20, 25, 30], marker="o")

    # Buat objek FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Tempatkan objek canvas di widget Tkinter
    canvas.get_tk_widget().pack()


# Buat jendela Tkinter
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Buat tombol untuk memanggil fungsi plot_chart
button = tk.Button(root, text="Plot Chart", command=plot_chart)
button.pack()

root.mainloop()
