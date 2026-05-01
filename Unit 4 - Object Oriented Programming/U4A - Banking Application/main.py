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
    
class BankingApplication:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Banking System")
        self.main_window.geometry("600x600")
        self.init_login_frames()
        self.init_login_labels()
        self.init_login_buttons()
        tk.mainloop()
        
    def init_login_page(self):
        self.init_login_frames()
        self.init_login_labels()
        self.init_login_buttons()
        
    def init_login_frames(self):
        self.top_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        self.top_frame.pack()
        self.bottom_frame.pack()
        
    def init_login_buttons(self):
        self.sign_up_button = tk.Button(self.bottom_frame, text="Sign Up", command=self.sign_up)
        self.login_button = tk.Button(self.bottom_frame, text="Login", command=self.login)
        
        self.sign_up_button.pack(side="left")
        self.login_button.pack(side="left")
        
    def init_login_labels(self):
        self.title = tk.Label(self.top_frame, text="Banking Application")
        self.prompt_username = tk.Label(self.top_frame, text="Enter your username: ")
        self.username_entry = tk.Entry(self.top_frame, width=15)
        self.prompt_password = tk.Label(self.top_frame, text="Enter your password: ")
        self.password_entry = tk.Entry(self.top_frame, width=15)
        self.prompt_balance = tk.Label(self.top_frame, text="Initial Deposit, if signing up ($): ")
        self.balance_entry = tk.Entry(self.top_frame, width=15)
        self.title.pack()
        self.prompt_username.pack()
        self.username_entry.pack()
        self.prompt_password.pack()
        self.password_entry.pack()
        self.prompt_balance.pack()
        self.balance_entry.pack()
        

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        accountnum = "INSERT"
        try: 
            database = open(self.encrypt(username) + ".txt", 'r')
            lines = database.readlines()
            database.close()
            stored_username = self.decrypt(lines[0].strip())
            stored_password = self.decrypt(lines[1].strip())
            stored_bal = self.decrypt(lines[2].strip())
            if username == stored_username and password == stored_password:
                self.current_password = password
                self.top_frame.destroy()
                self.bottom_frame.destroy()

                self.user_checking = Checking(float(stored_bal), accountnum, username)
                self.user_savings = Savings(0 ,accountnum, username, 2.0)
                self.show_dashboard(username)
            else:
                messagebox.showerror("Error", "Incorrect Username or Password")
        except FileNotFoundError:
            messagebox.showerror("Error", "No users registered yet!") 

    def show_dashboard(self, username):
        self.main_window.title("Banking Dashboard")
        self.main_window.geometry("400x400")

        self.dash_frame = tk.Frame(self.main_window)
        self.dash_frame.pack(padx=20, pady=20)

        tk.Label(self.dash_frame, text="Banking Dashboard").pack(pady = 10)
        tk.Label(self.dash_frame, text="Account belongs to: " + username).pack()

        self.checking = tk.Button(self.dash_frame, text = "Checking Account", width=20, command=self.open_checking)
        self.savings = tk.Button(self.dash_frame, text= "Savings Account", width=20, command=self.open_savings)
        self.button_logout = tk.Button(self.dash_frame, text="Logout", command=self.logout)

        self.checking.pack()
        self.savings.pack()
        self.button_logout.pack()

    def open_savings(self):
        pass
    def add_savings(self):
        pass
    def open_checking(self):
        self.dash_frame.destroy()

        self.checking_frame = tk.Frame(self.main_window)
        self.checking_frame.pack(pady=20)

        tk.Label(self.checking_frame, text="Checking Account").pack()
        self.balance_label = tk.Label(self.checking_frame, text="Balance: " + str(self.user_checking.get_balance()))
        self.balance_label.pack(pady=10)
        
        tk.Button(self.checking_frame, text="Deposit", command= self.deposit_money).pack(side='left', padx=5)
        tk.Button(self.checking_frame, text="Withdraw", command=self.withdraw_money).pack(side='left', padx=5)
        tk.Button(self.checking_frame, text="Transaction to savings", command=self.add_savings).pack(side='left', padx=5)
        tk.Button(self.checking_frame, text="Back to Dashboard", command=self.back_to_dash).pack(pady=10)
        self.prompt_amount = tk.Label(self.checking_frame, text="Enter amount: ").pack(padx=5)
        self.amount_entry = tk.Entry(self.checking_frame, width=15)
        self.amount_entry.pack(padx=5)

    def deposit_money(self):
        try:
            amount = float(self.amount_entry.get())
            self.user_checking.deposit(amount)
            new_bal = str(self.user_checking.get_balance())
            self.balance_label.config(text="Balance: $" + new_bal)
            messagebox.showinfo("Success", "Deposited $" + str(amount))
        except ValueError:
            messagebox.showerror("Errof", "Please enter a valid numeric amount.")

    def withdraw_money(self):
        try:
            amount = float(self.amount_entry.get())
            current_bal = self.user_checking.get_balance()
            if amount > current_bal:
                messagebox.showwarning("Denied", "Not enough moeny!")
            elif amount <= 0:
                messagebox.showwarning("Denied", "Amount must be positive!")
            else:
                self.user_checking.withdraw(amount)
                new_bal = str(self.user_checking.get_balance())
                self.balance_label.config(text="Balance: $" + new_bal)
                messagebox.showinfo("Success", "Withdrew $" + str(amount))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")   

    def back_to_dash(self):
        username = self.user_checking.get_name()
        balance = str(self.user_checking.get_balance())
        password = self.current_password
        file = self.encrypt(username) + ".txt"
        database = open(file, 'w')
        database.write(self.encrypt(username) + '\n')
        database.write(self.encrypt(password) + '\n')
        database.write(self.encrypt(balance) + '\n')
        database.close()

        self.checking_frame.destroy()
        self.show_dashboard(username)        
        
    def logout(self):
        self.dash_frame.destroy()
        self.init_login_frames()
        self.init_login_labels()
        self.init_login_buttons()
    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + 3) % 26 + base)
            else:
                result += char
        return result

    def decrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - 3) % 26 + base)
            else:
                result += char
        return result
        
    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        balance = self.balance_entry.get()
        if (username == '' or password == '' or balance == ''):
            messagebox.showinfo("Error", "Everything is required")
        else:
            try:
                float(balance)
                filename = self.encrypt(username) + ".txt"
                database = open(filename, 'w')
                database.write(self.encrypt(username) + '\n')
                database.write(self.encrypt(password) + '\n')
                database.write(self.encrypt(balance) +'\n')
                database.close()
                messagebox.showinfo("Sucess", "Signed Up!")
                self.top_frame.destroy()
                self.bottom_frame.destroy() 
                self.user_checking = Checking(balance, accountnum, username)
                self.user_savings = Savings(0, accountnum, username, 2.0)
                self.show_dashboard(username)
            except ValueError:
                messagebox.showerror("Error", "Balance must be a number")
    def close(self):
        self.main_window.quit()
        self.main_window.destroy()
        
application = BankingApplication()
