"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: April 29th, 2026
Description: This is a secure online banking system program, built with Python's tkinter library. 
This program features a login system, banking dashboards, as well as a variety of different account features.
"""

import tkinter as tk
from tkinter import messagebox

class Account(object):
    def __init__(self, balance, accountnum, name):
        self.__balance = float(balance)
        self.__accountnum = accountnum
        self.__name = name
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        self.__balance = new_balance
        
    def get_accountnum(self):
        return self.__accountnum
    
    def get_name(self):
        return self.__name
    
class Checking(Account):
    def __init__(self, balance, accountnum, name):
        Account.__init__(self, balance, accountnum, name)

    def deposit(self, amount):
        if amount > 0:
            current = self.get_balance()
            self.set_balance(current + amount)

    def withdraw(self, amount):
        current = self.get_balance()
        if 0 < amount <= current:
            self.set_balance(current - amount)   
        
        
class Savings(Account):
    def __init__(self, balance, accountnum, name, interest_rate):
        Account.__init__(self, balance, accountnum, name)
        self.__interest_rate = (interest_rate/100)
        self.__interest_earned = 0

    def calculate_interest(self):
        
        interest = self.get_balance() * self.__interest_rate
        new_balance = self.get_balance() + interest
        self.set_balance(new_balance)
        self.__interest_earned += interest
        
    def get_interest_earned(self):
        return self.__interest_earned
    
class LoginPage:
    def __init__(self):
        self.main_window = tk.Tk()
        self.init_frames()
        self.init_labels()
        self.init_buttons()
        
        tk.mainloop()
        
    def init_frames(self):
        self.top_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
    def init_buttons(self):
        self.login_button = tk.Button(self.bottom_frame, text="Login", command=self.login)
        
        self.login_button.pack()
        
    def init_labels(self):
        self.title = tk.Label(self.top_frame, text="Banking Application")
        self.prompt_username = tk.Label(self.top_frame, text="Enter your username: ")
        self.username_entry = tk.Entry(self.top_frame, width=10)
        self.prompt_password = tk.Label(self.top_frame, text="Enter your password: ")
        self.password_entry = tk.Entry(self.top_frame, width=10)
        
        self.title.pack()
        self.prompt_username.pack()
        self.username_entry.pack()
        self.prompt_password.pack()
        self.password_entry.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        messagebox.showinfo("Success", "You username is " + username + " and your password is " + password + '.')
        
application = LoginPage()
