import tkinter as tk


def on_resize(event):
    width = root.winfo_width()
    height = root.winfo_height()
    print(f"Ukuran aktual: {width}x{height}")


root = tk.Tk()
root.geometry("640x480")
root.minsize(640, 480)

root.bind("<Configure>", on_resize)
root.mainloop()
