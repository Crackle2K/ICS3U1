"""
Author: Dinesh Sinnathamby
Date: March 10th, 2026
Description: Simple program that checks if a user's least favourite fruit is on the groceries list. If so, it will remove the fruit from the list.
"""

fruit = input("What fruit do you dislike? : ").strip().lower()

groceries = open("Unit 3 - Advanced Topics/3.1 - Files/groceries.txt", 'r')
new_groceries = open("Unit 3 - Advanced Topics/3.1 - Files/groceries.new", 'w')

for line in groceries:
    if line.strip().lower() != fruit:
        new_groceries.write(line)

groceries.close()
new_groceries.close()

print("groceries.new has been created with", fruit, "removed.")
