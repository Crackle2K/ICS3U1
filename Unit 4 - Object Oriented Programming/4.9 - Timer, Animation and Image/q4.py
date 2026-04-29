"""
Author: Dinesh Sinnathamby
Date: April 28th, 2026
Description: A program that animates a ball bouncing within a canvas window triggered by a mouse click.
"""

import tkinter as tk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.dx, self.dy = 2, 2
        self.ball = self.canvas.create_oval(50, 50, 70, 70, fill='blue')
        
        self.root.bind("<Button-1>", self.start_animation)
        self.running = False
        self.root.mainloop()

    def start_animation(self, event):
        if not self.running:
            self.running = True
            self.animate()

    def animate(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        
        pos = self.canvas.coords(self.ball)
        
        if pos[0] <= 0 or pos[2] >= 300:
            self.dx = -self.dx
        if pos[1] <= 0 or pos[3] >= 300:
            self.dy = -self.dy
            
        self.root.after(10, self.animate)

Main()