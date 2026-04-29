"""
Author: Dinesh Sinnathamby
Date: April 28th, 2026
Description: A Tkinter application that displays a numerical countdown from 10 to 0.
"""

import tkinter as tk

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.label = tk.Label(self.root, text="Starting timer...", font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)
        self.countdown(10)
        self.root.mainloop()

    def countdown(self, timer):
        if timer > 0:
            message = "Time left: %d" % timer
            self.label.config(text=message)
            timer -= 1
            self.root.after(1000, self.countdown, timer)
        else:
            self.label.config(text="Time's up!", fg="red")

CountdownTimer()