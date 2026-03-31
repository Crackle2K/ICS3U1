"""
Author: Dinesh Sinnathamby
Date: March 31st, 2026
Description: This is a simple program that adds up as well as multiplies every single value in a predetermined list.
"""

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
    
def rec_product(lst):
    if len(lst)==1:
        return lst[0]
    return lst[0] * rec_product(lst[1:])

def main():
    my_list = [1, 2, 3, 4]
    print(rec_product(my_list))

main()