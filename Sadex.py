import os, time, tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()
root.title("Sadex Beta - Non-VT Emulator Engine")
root.geometry("700x500")
root.configure(bg="#11111b")

status_label = tk.Label(root, text="Click START to initialize engine...", font=("Arial", 11, "italic"), fg="#f5e0dc", bg="#11111b")
status_label.pack(pady=(20, 5))

progress = ttk.Progressbar(root, orient="horizontal", length=520, mode="determinate")
progress.pack(pady=10)

def start_loading():
    for val in range(0, 101, 20):
        progress["value"] = val
        root.update()
        time.sleep(0.5)
    messagebox.showinfo("Sadex Engine", "Sadex Engine Ready!")

start_btn = tk.Button(root, text="START SADEX ENGINE", font=("Arial", 11, "bold"), bg="#89b4fa", fg="#11111b", command=start_loading)
start_btn.pack(pady=20)
root.mainloop()
