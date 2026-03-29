"""
Author: Dinesh Sinnathamby
Date: March 27th, 2026
Description: This programs prompts the user for five different numbers, checks if each number has already been added, then displays the five numbers.
"""

numbers = []

while len(numbers) != 5:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        
print(numbers)