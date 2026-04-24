"""
Author: Dinesh Sinnathamby
Date: April 23rd, 2026
Description: This is another simple program that creates an organized GUI, displaying various labels, as well as using frame objects."""


import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        # Create two frames
        self.init_frames()
        self.init_labels()
        # Enter the tkinter main loop.
        tkinter.mainloop()
        
    def init_frames(self):
        """ Create two frames, one for the top of the
        window, and one for the bottom."""
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # Yes, we have to pack the frames too!
        self.top_frame.pack()
        self.bottom_frame.pack()
        
    def init_labels(self):
        # Create three Label widgets for the top Frame.
        self.label1 = tkinter.Label(self.top_frame, text='Brown')
        self.label2 = tkinter.Label(self.top_frame, text='Pouline')
        self.label3 = tkinter.Label(self.top_frame, text='Huynh')
        # Create three Label widgets for the bottom Frame.
        self.label4 = tkinter.Label(self.bottom_frame, text='Brown')
        self.label5 = tkinter.Label(self.bottom_frame, text='Huynh')
        self.label6 = tkinter.Label(self.bottom_frame, text='Pouline')
        # Pack the labels that are in the top Frame.
        # Use the side='top' argument to stack them under each other
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        # Pack the labels that are in the bottom Frame.
        # Use the side='left' argument to arrange them

        # horizontally from the left of the Frame.
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

# Create an instance of the MyGUI class.
my_gui = MyGUI()