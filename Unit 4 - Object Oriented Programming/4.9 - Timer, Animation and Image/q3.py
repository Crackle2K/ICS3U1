"""
Author: Dinesh Sinnathamby
Date: April 28th, 2026
Description: An automated traffic light simulation that cycles through Green, Yellow, and Red.
"""

import tkinter as tk

class TrafficLight:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=100, height=300)
        self.canvas.pack()
        self.red_light = self.canvas.create_oval(20, 20, 80, 80, fill="grey")
        self.yellow_light = self.canvas.create_oval(20, 110, 80, 170, fill="grey")
        self.green_light = self.canvas.create_oval(20, 200, 80, 260, fill="grey")
        self.state = 0
        self.display()
        self.root.mainloop()

    def display(self):
        self.canvas.itemconfig(self.red_light, fill="grey")
        self.canvas.itemconfig(self.yellow_light, fill="grey")
        self.canvas.itemconfig(self.green_light, fill="grey")
        
        if self.state == 0:
            self.canvas.itemconfig(self.green_light, fill="green")
            delay = 3000
        elif self.state == 1:
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            delay = 1000
        else:
            self.canvas.itemconfig(self.red_light, fill="red")
            delay = 3000
            
        self.state = (self.state + 1) % 3
        self.root.after(delay, self.display)

TrafficLight()