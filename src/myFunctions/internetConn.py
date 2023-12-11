from tkinter import messagebox
import socket


def is_internet_connected():
    """Function untuk menguji koneksi internet.\n
    Jika perangkat sedang online atau offline, akan memberikan respon.
    """
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        messagebox.showinfo("Info", "Perangkat terhubung ke internet.")
        return True
    except OSError:
        messagebox.showerror("Error", "Perangkat tidak terhubung ke internet.")
    return False


# Memanggil function
is_internet_connected()
