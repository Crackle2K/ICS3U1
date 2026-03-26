"""
Author: Dinesh Sinnathamby
Date: March 26th, 2026
Description: Simple program that takes in a user's list and reverses the order, before finally displaying the reversed list.
"""

def list_reverse(userList):
    userList.reverse()
    return userList

def main():
    userList = list(input("Enter your list: "))
    reversed = list_reverse(userList)
    print("Your reversed list is", str(reversed) + '.')
    
main()