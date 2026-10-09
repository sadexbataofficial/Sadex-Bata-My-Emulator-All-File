import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Sadex Beta v1.0.0 - Multi-Instance Manager")
root.geometry("750x520")
root.configure(bg="#11111b")

header = tk.Label(root, text="SADEX BETA MULTI-INSTANCE MANAGER", font=("Arial", 16, "bold"), fg="#89b4fa", bg="#11111b")
header.pack(pady=15)

frame_list = tk.Frame(root, bg="#1e1e2e")
frame_list.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("name", "android_ver", "status", "ram", "cpu")
tree = ttk.Treeview(frame_list, columns=columns, show="headings")
tree.heading("name", text="Instance Name")
tree.heading("android_ver", text="Android Version")
tree.heading("status", text="Status")
tree.heading("ram", text="RAM (MB)")
tree.heading("cpu", text="CPU Cores")

tree.insert("", "end", values=("Sadex-Instance-1", "Nougat 64-bit (Android 7)", "Stopped", "2048", "2"))
tree.insert("", "end", values=("Sadex-Instance-2 (Glory)", "Android 11", "Stopped", "4096", "4"))
tree.pack(fill="both", expand=True)

root.mainloop()
