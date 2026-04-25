"""
Author: Dinesh Sinnathamby
Date: April 25th, 2026
Description: Simple program demonstrating a celcius to fahrenheit convertor, using a tkinter GUI.
"""

import tkinter as tk

def convert_temperature():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (9/5) * celsius + 32
        label_result.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        label_result.config(text="Please enter a valid number")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("250x150")

tk.Label(root, text="Enter Celsius:").pack(pady=5)
entry_celsius = tk.Entry(root)
entry_celsius.pack()

btn_convert = tk.Button(root, text="Convert to Fahrenheit", command=convert_temperature)
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="Result will appear here")
label_result.pack()

root.mainloop()