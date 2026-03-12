"""
Author: Dinesh Sinnathamby
Date: March 10th, 2026
Description: Simple program that checks if a user's desired fruit is on the groceries list.
"""

groceries = open("Unit 3 - Advanced Topics/3.1 - Files/groceries.txt", 'r')
items = groceries.read()
groceries.close()

fruit = input("What's your favourite fruit? : ").strip().lower()

if fruit in items:
    print("The fruit", fruit, "is on the groceries list!")
else:
    print("The fruit", fruit, "is not on the groceries list!")