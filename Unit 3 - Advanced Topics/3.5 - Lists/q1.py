"""
Author: Dinesh Sinnathamby
Date: March 26th, 2026
Description: This program takes in a group of numbers as a list, then doubles each value in the list before finally displaying the result.
"""

def double_it(userList):
    doubledList = []
    for value in userList:
        newValue = value * 2
        doubledList.append(newValue)
    return doubledList
    
def main():
    numbers = [int(i) for i in input("Enter your numbers seperated by spaces: ").split()]
    result = double_it(numbers)
    print("Your doubled list is", str(result) + "!")
    
main()