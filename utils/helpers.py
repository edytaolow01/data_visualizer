import tkinter as tk
from tkinter import ttk

def popup_msg(msg):
    """Display a message after pressing a button"""
    popup = tk.Tk()
    popup.wm_title("Notification")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Ok", command=popup.destroy)
    B1.pack()
    popup.mainloop()

def validate_numeric_input(value):
    """Validate if the input is numeric"""
    try:
        float(value)
        return True
    except ValueError:
        return False 