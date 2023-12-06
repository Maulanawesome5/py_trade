import tkinter as tk


class ScrollableApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Scrollable App")

        # Buat widget canvas sebagai wadah konten
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Buat scrollbar untuk widget Canvas (vertikal)
        self.scrollbar = tk.Scrollbar(root, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Konfigurasi widget Canvas untuk menggunakan scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Buat frame sebagai konten yang akan diisi ke dalam widget Canvas
        self.content_frame = tk.Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.content_frame, anchor=tk.NW)

        # Isi konten frame dengan elemen-elemen. Misalnya Label
        for i in range(20):
            label = tk.Label(self.content_frame, text=f"Label {i}")
            label.pack(pady=10)

        # Atur agar scrollbar muncul secara otomatis saat isi konten melebihi jendela
        self.content_frame.bind("<Configure>", self.on_content_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def on_content_configure(self, event):
        """Perbarui ukuran area tampilan widget Canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

    def on_canvas_configure(self, event):
        """Perbarui ukuran area tampilan widget Canvas saat ukuran jendela berubah"""
        self.canvas.itemconfig(self.content_frame_window, width=event.width)


# Buat jendela tkinter
root = tk.Tk()
app = ScrollableApp(root)

root.mainloop()
