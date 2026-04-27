"""
Author: Dinesh Sinnathamby
Date: April 27th, 2026
Description: Simple GUI application that lets the user select a rate category via Radiobuttons and input an energy consumption value in Watts and time in hours into two Entry widgets. When they click the “OK” button, a dialog box should display their total electricity cost.
"""

import tkinter as tk
from tkinter import messagebox

class ElectricityBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ontario Electricity Billing")
        self.root.geometry("300x350")

        self.rate_var = tk.DoubleVar(value=0.051)

        tk.Label(self.root, text="Select Rate Category:", font=('Arial', 10, 'bold')).pack(pady=5)

        tk.Radiobutton(self.root, text="Off-Peak ($0.051/kWh)", variable=self.rate_var, value=0.051).pack(anchor="w", padx=20)
        tk.Radiobutton(self.root, text="Mid-Peak ($0.081/kWh)", variable=self.rate_var, value=0.081).pack(anchor="w", padx=20)
        tk.Radiobutton(self.root, text="On-Peak ($0.099/kWh)", variable=self.rate_var, value=0.099).pack(anchor="w", padx=20)

        tk.Label(self.root, text="Enter Power (Watts):").pack(pady=(15, 0))
        self.entry_watts = tk.Entry(self.root)
        self.entry_watts.pack()

        tk.Label(self.root, text="Enter Time (Hours):").pack(pady=(10, 0))
        self.entry_hours = tk.Entry(self.root)
        self.entry_hours.pack()

        tk.Button(self.root, text="OK", command=self.calculate_cost, width=10).pack(pady=20)

    def calculate_cost(self):
        try:
            watts = float(self.entry_watts.get())
            hours = float(self.entry_hours.get())
            kwh = (watts * hours) / 1000
            rate = self.rate_var.get()
            total_cost = kwh * rate
            messagebox.showinfo("Total Cost", f"Total Electricity Cost: ${total_cost:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

root = tk.Tk()
app = ElectricityBillingApp(root)
root.mainloop()