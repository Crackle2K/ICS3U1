"""
Author: Dinesh Sinnathamby
Date: April 25th, 2026
Description: Simple program that displays a variety of different welcome messages, each rotating after 1 second.
"""

import tkinter as tk
import random

messages = [
    "Welcome to the program!",
    "Hello, great to see you!",
    "Greetings, user!"
]

def change_message():
    new_message = random.choice(messages)
    label_welcome.config(text=new_message)
    
    root.after(1000, change_message)

root = tk.Tk()
root.title("Random Greeter")
root.geometry("300x100")

label_welcome = tk.Label(root, text="Starting...", font=("Arial", 14))
label_welcome.pack(expand=True)

change_message()

root.mainloop()