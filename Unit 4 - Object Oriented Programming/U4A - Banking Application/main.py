"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: April 29th, 2026
Description: This is a secure online banking system program, built with Python's tkinter library. 
This program features a login system, banking dashboards, as well as a variety of different account features.
"""

import tkinter as tk
import datetime
from tkinter import messagebox
import time
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
            self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)

class Savings(Account):
    def __init__(self, balance, accountnum, name, interest_rate):
        Account.__init__(self, balance, accountnum, name)
        self.__interest_rate = interest_rate / 100
        self.__interest_earned = 0.0

    def get_interest_rate(self):
        return self.__interest_rate

    def get_interest_earned(self):
        return self.__interest_earned

    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.set_balance(self.get_balance() + interest)
        self.__interest_earned += interest

class BankingApplication:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Banking System")
        self.main_window.geometry("600x650")
        self.coin_frames = [
            tk.PhotoImage(file=r"C:\Users\dhani\OneDrive\Documents\GitHub\ICS3U1\Unit 4 - Object Oriented Programming\U4A - Banking Application\coin1.png"), 
            tk.PhotoImage(file=r"C:\Users\dhani\OneDrive\Documents\GitHub\ICS3U1\Unit 4 - Object Oriented Programming\U4A - Banking Application\coin2.png")
        ]
        self.coin_index = 0
        self.interest_job = None
        self.logo_job = None
        self.init_login_page()
        tk.mainloop()

    def init_login_page(self):
        self.init_login_frames()
        self.init_logo_animation()
        self.init_login_labels()
        self.init_login_buttons()

    def init_login_frames(self):
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        self.top_frame.pack()
        self.bottom_frame.pack()

    def flipping_coin(self):
        current_frame = self.coin_frames[self.coin_index]
        self.anim_label.config(image=current_frame)
                
        self.coin_index = (self.coin_index + 1) % 2
                
        self.main_window.after(500, self.flipping_coin)
    

    def init_logo_animation(self):
        self.logo_canvas = tk.Canvas(self.top_frame, width=80, height=80, bg="white", highlightthickness=0)
        self.logo_canvas.pack(pady=5)
        self.logo_state = 0
        self.animate_logo()

    def animate_logo(self): #will improve this later this was fully copied
        self.logo_canvas.delete("all")
        text_color = "#FFD700" if self.logo_state == 0 else "#228B22"
        self.logo_canvas.create_text(40, 40, text="$", font=("Arial", 36, "bold"), fill=text_color)
        self.logo_state = (self.logo_state + 1) % 2
        self.logo_job = self.main_window.after(500, self.animate_logo)

    def cancel_logo_animation(self):
        if self.logo_job is not None:
            self.main_window.after_cancel(self.logo_job) #MUST fix this later
            self.logo_job = None 

    def init_login_labels(self):
        self.anim_label = tk.Label(self.top_frame, height=300, width=200)
        self.anim_label.place(height=300, width=200)
        self.anim_label.pack(pady=10)
        self.flipping_coin()
        self.title_label = tk.Label(self.top_frame, text="Banking Application", font=("Arial", 14, "bold"))
        self.full_name_label = tk.Label(self.top_frame, text="Full Name (sign up only):")
        self.fullname_entry = tk.Entry(self.top_frame, width=20)
        self.prompt_username = tk.Label(self.top_frame, text="Username:")
        self.username_entry = tk.Entry(self.top_frame, width=20)
        self.prompt_password = tk.Label(self.top_frame, text="Password:")
        self.password_entry = tk.Entry(self.top_frame, width=20, show="*")
        self.prompt_balance = tk.Label(self.top_frame, text="Initial Deposit, if signing up ($):")
        self.balance_entry = tk.Entry(self.top_frame, width=20)

        self.title_label.pack(pady=5)
        self.full_name_label.pack()
        self.fullname_entry.pack()
        self.prompt_username.pack()
        self.username_entry.pack()
        self.prompt_password.pack()
        self.password_entry.pack()
        self.prompt_balance.pack()
        self.balance_entry.pack()

    def init_login_buttons(self):
        self.sign_up_button = tk.Button(self.bottom_frame, text="Sign Up", width=12, command=self.sign_up)
        self.login_button = tk.Button(self.bottom_frame, text="Login", width=12, command=self.login)
        self.sign_up_button.pack(side="left", padx=5, pady=10)
        self.login_button.pack(side="left", padx=5, pady=10)

    def sign_up(self):
        fullname = self.fullname_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        balance = self.balance_entry.get().strip()

        if fullname == '' or username == '' or password == '' or balance == '':
            messagebox.showerror("Error", "All fields are required for sign up.")
            return

        try:
            float(balance)
        except ValueError:
            messagebox.showerror("Error", "Balance must be a number.")
            return

        try:
            users = open("userdata.txt", 'r+')
            lines = users.readlines()
            if not lines:
                users.write(str(0))
                accountnum = "0"
            else:
                count = int(lines[0]) + 1
                users.seek(0)
                users.write(str(count))
                users.truncate()
                accountnum = str(count)
            users.close()

        except FileNotFoundError:
            users = open("userdata.txt", 'w')
            users.write(str(0))
            users.close()
            accountnum = "0"

        filename = self.encrypt(username) + ".txt"
        database = open(filename, 'w')
        database.write(self.encrypt(fullname) + '\n')
        database.write(self.encrypt(username) + '\n')
        database.write(self.encrypt(password) + '\n')
        database.write(self.encrypt(balance) + '\n')
        database.write(self.encrypt("0.0") + '\n')
        database.write(self.encrypt(accountnum) + '\n')
        database.close()

        messagebox.showinfo("Success", "Signed up successfully!")
        self.cancel_logo_animation()
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        self.current_fullname = fullname
        self.current_password = password
        self.user_checking = Checking(float(balance), accountnum, username)
        self.user_savings = Savings(0.0, accountnum, username, 2.0)
        self.show_dashboard(username, accountnum)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        try:
            database = open(self.encrypt(username) + ".txt", 'r')
            lines = database.readlines()
            database.close()

            stored_fullname = self.decrypt(lines[0].strip())
            stored_username = self.decrypt(lines[1].strip())
            stored_password = self.decrypt(lines[2].strip())
            stored_checking = self.decrypt(lines[3].strip())
            stored_savings = self.decrypt(lines[4].strip())
            stored_accountnum = self.decrypt(lines[5].strip())

            if username == stored_username and password == stored_password:
                self.current_password = password
                self.current_fullname = stored_fullname
                self.cancel_logo_animation()
                self.top_frame.destroy()
                self.bottom_frame.destroy()
                self.user_checking = Checking(float(stored_checking), stored_accountnum, username)
                self.user_savings = Savings(float(stored_savings), stored_accountnum, username, 2.0)
                self.show_dashboard(username, stored_accountnum)
            else:
                messagebox.showerror("Error", "Incorrect username or password.")

        except FileNotFoundError:
            messagebox.showerror("Error", "Account not found.")
        except (IndexError, ValueError):
            messagebox.showerror("Error", "User data is corrupted. Please sign up again.")

    def show_dashboard(self, username, accountnum):
        self.main_window.title("Banking Dashboard")
        self.main_window.geometry("400x400")

        try:
            self.dash_frame.destroy()
        except AttributeError:
            pass

        self.dash_frame = tk.Frame(self.main_window)
        self.dash_frame.pack(padx=20, pady=20)

        tk.Label(self.dash_frame, text="Banking Dashboard", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.dash_frame, text="Account holder: " + username).pack()
        tk.Label(self.dash_frame, text="Account Number: " + accountnum).pack()
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        tk.Label(self.dash_frame, text="Date: " + current_date).pack(pady=5)

        tk.Button(self.dash_frame, text="Checking Account", width=20, command=self.open_checking).pack(pady=3)
        tk.Button(self.dash_frame, text="Savings Account", width=20, command=self.open_savings).pack(pady=3)
        tk.Button(self.dash_frame, text="Change Password", width=20, command=self.change_password).pack(pady=3)
        tk.Button(self.dash_frame, text="Logout", width=20, command=self.logout).pack(pady=3)
        tk.Button(self.dash_frame, text="Exit", width=20, command=self.close).pack(pady=3)

    def change_password(self):
        self.dash_frame.destroy()
        self.change_pass_frame = tk.Frame(self.main_window)
        self.change_pass_frame.pack(padx=20, pady=20)

        tk.Label(self.change_pass_frame, text="Change Password", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self.change_pass_frame, text="Current Password:").pack()
        self.old_pass_entry = tk.Entry(self.change_pass_frame, width=20, show="*")
        self.old_pass_entry.pack()
        tk.Label(self.change_pass_frame, text="New Password:").pack()
        self.new_pass_entry = tk.Entry(self.change_pass_frame, width=20, show="*")
        self.new_pass_entry.pack()
        tk.Label(self.change_pass_frame, text="Confirm New Password:").pack()
        self.confirm_pass_entry = tk.Entry(self.change_pass_frame, width=20, show="*")
        self.confirm_pass_entry.pack(pady=5)

        tk.Button(self.change_pass_frame, text="Confirm", command=self.confirm_change_password).pack(pady=5)
        tk.Button(self.change_pass_frame, text="Back", command=self.back_from_change_pass).pack()

    def confirm_change_password(self):
        old = self.old_pass_entry.get()
        new = self.new_pass_entry.get()
        confirm = self.confirm_pass_entry.get()

        if old != self.current_password:
            messagebox.showerror("Error", "Current password is incorrect.")
        elif new == '':
            messagebox.showerror("Error", "New password cannot be empty.")
        elif new != confirm:
            messagebox.showerror("Error", "New passwords do not match.")
        else:
            self.current_password = new
            self.save_user_data()
            messagebox.showinfo("Success", "Password changed successfully!")
            self.back_from_change_pass()

    def back_from_change_pass(self):
        self.change_pass_frame.destroy()
        self.show_dashboard(self.user_checking.get_name(), self.user_checking.get_accountnum())

    def open_checking(self):
        self.dash_frame.destroy()
        self.checking_frame = tk.Frame(self.main_window)
        self.checking_frame.pack(pady=20)

        tk.Label(self.checking_frame, text="Checking Account", font=("Arial", 12, "bold")).pack()
        tk.Label(self.checking_frame, text="Account holder: " + self.current_fullname).pack()
        self.balance_label = tk.Label(self.checking_frame, text="Balance: $" + str(round(self.user_checking.get_balance(), 2)))
        self.balance_label.pack(pady=10)

        tk.Label(self.checking_frame, text="Enter amount ($):").pack()
        self.amount_entry = tk.Entry(self.checking_frame, width=15)
        self.amount_entry.pack(pady=5)

        btn_frame = tk.Frame(self.checking_frame)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Deposit", command=self.deposit_money).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Withdraw", command=self.withdraw_money).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Transfer to Savings", command=self.add_savings).pack(side='left', padx=5)

        tk.Button(self.checking_frame, text="Back to Dashboard", command=self.back_to_dash).pack(pady=5)
        tk.Button(self.checking_frame, text="Exit", command=self.close).pack()

    def deposit_money(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showwarning("Denied", "Amount must be positive.")
                return
            self.user_checking.deposit(amount)
            self.balance_label.config(text="Balance: $" + str(round(self.user_checking.get_balance(), 2)))
            self.save_user_data()
            messagebox.showinfo("Success", "Deposited $" + str(round(amount, 2)))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

    def withdraw_money(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showwarning("Denied", "Amount must be positive.")
            elif amount > self.user_checking.get_balance():
                messagebox.showwarning("Denied", "Insufficient funds.")
            else:
                self.user_checking.withdraw(amount)
                self.balance_label.config(text="Balance: $" + str(round(self.user_checking.get_balance(), 2)))
                self.save_user_data()
                messagebox.showinfo("Success", "Withdrew $" + str(round(amount, 2)))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

    def add_savings(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showwarning("Denied", "Amount must be positive.")
            elif amount > self.user_checking.get_balance():
                messagebox.showwarning("Denied", "Insufficient funds in checking.")
            else:
                self.user_checking.withdraw(amount)
                self.user_savings.set_balance(self.user_savings.get_balance() + amount)
                self.balance_label.config(text="Balance: $" + str(round(self.user_checking.get_balance(), 2)))
                self.save_user_data()
                messagebox.showinfo("Success", "Transferred $" + str(round(amount, 2)) + " to savings.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

    def back_to_dash(self):
        self.save_user_data()
        self.checking_frame.destroy()
        self.show_dashboard(self.user_checking.get_name(), self.user_checking.get_accountnum())

    def open_savings(self):
        self.dash_frame.destroy()
        self.cancel_interest_job()

        self.savings_frame = tk.Frame(self.main_window)
        self.savings_frame.pack(pady=20)

        tk.Label(self.savings_frame, text="Savings Account", font=("Arial", 12, "bold")).pack()
        tk.Label(self.savings_frame, text="Account holder: " + self.current_fullname).pack()

        self.savings_balance_label = tk.Label(self.savings_frame, text="Balance: $" + str(round(self.user_savings.get_balance(), 2)))
        self.savings_balance_label.pack(pady=5)

        self.savings_interest_label = tk.Label(self.savings_frame, text="Total Interest Earned: $" + str(round(self.user_savings.get_interest_earned(), 2)))
        self.savings_interest_label.pack()

        tk.Label(self.savings_frame, text="Transfer amount to checking ($):").pack(pady=5)
        self.savings_transfer_entry = tk.Entry(self.savings_frame, width=15)
        self.savings_transfer_entry.pack()

        tk.Button(self.savings_frame, text="Transfer to Checking", command=self.transfer_to_checking).pack(pady=5)
        tk.Button(self.savings_frame, text="Back to Dashboard", command=self.back_from_savings).pack(pady=3)
        tk.Button(self.savings_frame, text="Exit", command=self.close).pack(pady=3)

        self.schedule_interest()

    def schedule_interest(self):
        self.interest_job = self.main_window.after(1000, self.update_interest)

    def update_interest(self):
        self.user_savings.calculate_interest()
        self.save_user_data()
        self.savings_balance_label.config(text="Balance: $" + str(round(self.user_savings.get_balance(), 2)))
        self.savings_interest_label.config(text="Total Interest Earned: $" + str(round(self.user_savings.get_interest_earned(), 2)))
        self.interest_job = self.main_window.after(1000, self.update_interest)

    def cancel_interest_job(self):
        if self.interest_job is not None:
            self.main_window.after_cancel(self.interest_job)
            self.interest_job = None

    def transfer_to_checking(self):
        try:
            amount = float(self.savings_transfer_entry.get())
            if amount <= 0:
                messagebox.showwarning("Denied", "Amount must be positive.")
            elif amount > self.user_savings.get_balance():
                messagebox.showwarning("Denied", "Insufficient funds in savings.")
            else:
                self.user_savings.set_balance(self.user_savings.get_balance() - amount)
                self.user_checking.deposit(amount)
                self.savings_balance_label.config(text="Balance: $" + str(round(self.user_savings.get_balance(), 2)))
                self.save_user_data()
                messagebox.showinfo("Success", "Transferred $" + str(round(amount, 2)) + " to checking.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

    def back_from_savings(self):
        self.cancel_interest_job()
        self.savings_frame.destroy()
        self.show_dashboard(self.user_checking.get_name(), self.user_checking.get_accountnum())

    def save_user_data(self):
        username = self.user_checking.get_name()
        filename = self.encrypt(username) + ".txt"
        database = open(filename, 'w')
        database.write(self.encrypt(self.current_fullname) + '\n')
        database.write(self.encrypt(username) + '\n')
        database.write(self.encrypt(self.current_password) + '\n')
        database.write(self.encrypt(str(self.user_checking.get_balance())) + '\n')
        database.write(self.encrypt(str(self.user_savings.get_balance())) + '\n')
        database.write(self.encrypt(self.user_checking.get_accountnum()) + '\n')
        database.close()

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

    def logout(self):
        self.cancel_interest_job()
        self.dash_frame.destroy()
        self.main_window.geometry("600x650")
        self.init_login_frames()
        self.init_logo_animation()
        self.init_login_labels()
        self.init_login_buttons()

    def close(self):
        self.cancel_interest_job()
        self.cancel_logo_animation()
        self.main_window.quit()
        self.main_window.destroy()

application = BankingApplication()
