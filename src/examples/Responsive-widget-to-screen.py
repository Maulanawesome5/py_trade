import tkinter as tk


class ResponsiveApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Tampilan Responsif")

        # Menambahkan widget
        self.label = tk.Label(root, text="Ini adalah label")
        self.label.pack(pady=20)

        # Menanggapi perubahan ukuran
        root.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        # Mendapatkan ukuran jendela baru
        self.root.after(200, self.adjust_widget_properties)

    def adjust_widget_properties(self):
        # Mendapatkan ukuran jendela baru
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Menyesuaikan properti widget berdasarkan ukuran jendela baru
        label_font_size = int(min(width, height) / 20)
        self.label.config(font=("Arial", label_font_size))

        print(f"Ukuran jendela: {width}x{height}")


# Buat jendela Tkinter
root = tk.Tk()
app = ResponsiveApp(root)

# Jalankan aplikasi
root.mainloop()
