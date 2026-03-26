"""
Author: Dinesh Sinnathamby
Date: March 26th, 2026
Description: Simple program that adds up all of the numerical values in a user's list, and ignores any other values.
"""

def total(userList):
    sum = 0
    for value in userList:
        try:
            sum += int(value)
        except ValueError:
            pass
    return sum

def main():
    userList = list(input("Enter your list: "))
    count = total(userList)
    print("The sum of all the values in the list is", str(count) + '.')
    
main()