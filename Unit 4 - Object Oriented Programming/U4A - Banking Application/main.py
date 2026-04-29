"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: April 29th, 2026
Description: This is a secure online banking system program, built with Python's tkinter library. This program features a login system, banking dashboards, as well as a variety of different account features.
"""

import tkinter as tk

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
    