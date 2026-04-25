"""
Author: Dinesh Sinnathamby
Date: April 25th, 2026
Description: Simple program using a tkinter GUI, displaying the average of three user inputted grades.
"""

import tkinter as tk

def calculate_average():
    try:
        score1 = float(entry1.get())
        score2 = float(entry2.get())
        score3 = float(entry3.get())
        average = (score1 + score2 + score3) / 3
        
        label_result.config(text=f"Average: {average:.2f}")
    except ValueError:
        label_result.config(text="Error: Enter numeric values.")

root = tk.Tk()
root.title("Grade Calculator")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)

frame1.pack(pady=5)
frame2.pack(pady=5)
frame3.pack(pady=5)
frame4.pack(pady=5)
frame5.pack(pady=5)

tk.Label(frame1, text="Test Score 1:").pack(side=tk.LEFT)
entry1 = tk.Entry(frame1)
entry1.pack(side=tk.LEFT)

tk.Label(frame2, text="Test Score 2:").pack(side=tk.LEFT)
entry2 = tk.Entry(frame2)
entry2.pack(side=tk.LEFT)

tk.Label(frame3, text="Test Score 3:").pack(side=tk.LEFT)
entry3 = tk.Entry(frame3)
entry3.pack(side=tk.LEFT)

btn_calc = tk.Button(frame4, text="Calculate Average", command=calculate_average)
btn_calc.pack()

label_result = tk.Label(frame5, text="Average: ")
label_result.pack()

root.mainloop()