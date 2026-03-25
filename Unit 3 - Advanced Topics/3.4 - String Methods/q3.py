"""
Author: Dinesh Sinnathamby
Date: March 24th, 2026
Description: Simple program converting 10-character telephone numbers with letters into their numerical equivalents.
"""

number = input("Enter a 10-character telephone number: ")
new = ""

for i in range(len(number)):
    if number[i].isdigit():
        new += number[i]
    else:
        if number[i].upper() in "ABC":
            new += '2'
        elif number[i].upper() in "DEF":
            new += '3'
        elif number[i].upper() in "GHI":
            new += '4'
        elif number[i].upper() in "JKL":
            new += '5'
        elif number[i].upper() in "MNO":
            new += '6'
        elif number[i].upper() in "PQRS":
            new += '7'
        elif number[i].upper() in "TUV":
            new += '8'
        else:
            new += '9'
        
print("Your converted number is:", new)