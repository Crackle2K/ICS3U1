"""
Author: Dinesh Sinnathamby
Date: March 23rd, 2026
Description: Simple program that takes a string, reverses it, and displays it to the user.
"""


def string_reverse(string):
    reversed = ""
    for i in range(len(string)):
        reversed += string[-(i + 1)]
    return reversed
    
def main():
    string = input("Enter your desired text: ")
    reversed = string_reverse(string)
    print(reversed)
    
main()