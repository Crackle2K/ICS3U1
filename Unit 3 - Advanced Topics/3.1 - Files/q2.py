"""
Author: Dinesh Sinnathamby
Date: March 10th, 2026
Description: Simple program that checks if a user's desired fruit is on the groceries list. If not, it will append the fruit to the list.
"""

groceries = open("Unit 3 - Advanced Topics/3.1 - Files/groceries.txt", 'r')
items = groceries.read()
groceries.close()

fruit = input("What's your favourite fruit? : ").strip().lower()

if fruit in items:
    print("The fruit", fruit, "is on the groceries list!")
else:
    groceries = open("Unit 3 - Advanced Topics/3.1 - Files/groceries.txt", 'a')
    groceries.write(fruit + "\n")
    print("The fruit", fruit, "has been added to the groceries list!")
    groceries.close()