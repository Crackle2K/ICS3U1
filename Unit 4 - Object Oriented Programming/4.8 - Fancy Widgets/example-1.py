import tkinter
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        """ Create the main window."""
        self.main_window = tkinter.Tk()
        self.init_frames()
        self.init_radios()
        self.init_buttons()
        # Start the mainloop.
        tkinter.mainloop()
        
    def init_buttons(self):
        """ Create an OK button and a Quit button."""
        self.ok_button = tkinter.Button(self.bottom_frame,text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
    def init_radios(self):
        """ Create an IntVar object to use with the Radiobuttons. """
        self.radio_var = tkinter.IntVar()
        # Set the intVar object to 1, default
        self.radio_var.set(True)
        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Option 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text='Option 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text='Option 3', variable=self.radio_var, value=3)
        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
    def init_frames(self):
        """ Create two frames. One for the Radiobuttons
        and another for the regular Button widgets. """
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
def show_choice(self):
    """ The show_choice method is the callback function for the OK button. """
    tkinter.messagebox.showinfo('Selection', 'You selected option ' + str(self.radio_var.get()))
    
# Create an instance of the MyGUI class.
my_gui = MyGUI()