"""
Author: Dinesh Sinnathamby
Date: March 26th, 2026
Description: This program takes in a list of positive and negative numbers, then displays the list without any negative numbers.
"""

def remove_negs(userList):
    modified = []
    for value in userList:
        if value > 0:
            modified.append(value)
    return modified
    
def main():
    userList = [1, 2, 3, -3, 6, -1, -3, 1]
    modifiedList = remove_negs(userList)
    print("The new list is: ", modifiedList)
    
main()

"""
The problem is when you remove a value from a list in Python, the numbers shift down, skipping the second negative number. We can see proof of this as after removing the -1 from the list, the -3 is skipped, hiding in the original list.
"""
