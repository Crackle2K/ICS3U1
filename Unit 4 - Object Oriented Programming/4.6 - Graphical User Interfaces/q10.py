"""
Author: Dinesh Sinnathamby
Date: April 23rd, 2026
Description: A GUI application that randomly selects one of three welcome messages to display in a Label widget upon startup.
"""

import tkinter
import random

class WelcomeGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Welcome')

        messages = ["Hello there!", "Welcome to the app!", "Greetings, traveler!"]
        
        chosen_text = random.choice(messages)

        self.label = tkinter.Label(self.main_window, text=chosen_text)
        
        self.label.pack(padx=20, pady=20)

        tkinter.mainloop()

WelcomeGUI()