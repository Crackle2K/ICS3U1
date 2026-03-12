"""
Author: Dinesh Sinnathamby
Date: March 12th, 2026
Description: This program reads the file numbers.txt, and displays the largest and smallest numbers in the file.
"""

numbersFile = open("Unit 3 - Advanced Topics/3.1 - Files/numbers.txt", 'r')
numbers = numbersFile.readlines()
numbersFile.close()

largest = 9
smallest = 9999999999999999

for number in numbers:
    num = int(number.strip())
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
        
print("The largest number is", str(largest) + ".")
print("The smallest number is", str(smallest) + ".")
