"""
Author: Dinesh Sinnathamby
Date: March 26th, 2026
Description: This program corrects a previously broken program, where each value in a new list is double the previous value in a user's list, then displayed.
"""

def double_preceeding(values):
    new = [0]
    for i in range(len(values) - 1):
        new.append(int(values[i]) * 2)
    return new
            
def main():
    userValues = [int(i) for i in input("Enter your values: ").split()]
    newValues = double_preceeding(userValues)
    print("Here are your new values:", newValues)
    
main()