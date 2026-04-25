import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        self.init_buttons()
        # Enter the tkinter main loop.
        tkinter.mainloop()
        
    def init_buttons(self):
        # Create a Button widget. The text 'Click Me!' should appear on the face of the Button.
        # The do_something method should be executed when the user clicks the Button.
        self.my_button = tkinter.Button(self.main_window, text='Click Me!', command=self.displayMessage)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.close)
        # Pack the Button.
        self.my_button.pack()
        self.quit_button.pack()
        # The do_something method is a callback function for the Button widget.
        
    def displayMessage(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')
        
    def close(self):
        self.main_window.quit()
        self.main_window.destroy()
        
# Create an instance of the MyGUI class.
my_gui = MyGUI()