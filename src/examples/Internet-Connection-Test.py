import socket
from tkinter import messagebox


def is_internet_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        # messagebox bisa ditempatkan disini
        # tidak perlu membuat if statement di luar function.
        return True
    except OSError:
        pass
    return False


# Contoh pemakaian
if is_internet_connected():
    messagebox.showinfo("Info", "Perangkat terhubung ke internet.")
    print("Perangkat terhubung ke internet.")
else:
    messagebox.showerror("Error", "Perangkat tidak terhubung ke internet.")
    print("Perangkat tidak terhubung ke internet.")
