#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def remind():
    messagebox.showinfo("Break", "Take a break! Look into the distance for 20 seconds.")
    # Reschedule the reminder in 20 minutes (20 minutes * 60 seconds * 1000 milliseconds)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Break! Next break in 20 minutes.")

    root.after(20 * 60 * 1000, remind)

root = tk.Tk()
root.withdraw()

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - The break reminder has started. A notification will appear every 20 minutes.")

# Schedule the first reminder in 20 minutes
root.after(20 * 60 * 1000, remind)
root.mainloop()
