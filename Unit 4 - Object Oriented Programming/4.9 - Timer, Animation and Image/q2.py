"""
Author: Dinesh Sinnathamby
Date: April 28th, 2026
Description: A simple stopwatch using Tkinter that tracks elapsed time in tenths of a second.
"""

import tkinter as tk

class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stopwatch")
        self.label = tk.Label(self.root, text="0.0", font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)
        self.display_counter(0.0)
        self.root.mainloop()

    def display_counter(self, count):
        self.label.config(text=f"{count:.1f}")
        self.root.after(100, self.display_counter, count + 0.1)

Stopwatch()