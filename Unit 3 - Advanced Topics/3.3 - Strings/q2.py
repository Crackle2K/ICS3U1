"""
Author: Dinesh Sinnathamby
Date: March 23rd, 2026
Description: Simple program that checks if a selected string contains any whitespace.
"""

def contains_whitespace(string):
    if (' ' or '\t' or '\n') in string:
        return True
    else:
        return False
    
def main():
    string = input("Enter your text: ")
    if contains_whitespace(string):
        print("This text has whitespace!")
    else:
        print("This string doesn't have any whitespace!")
    
main()