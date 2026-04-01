"""
Author: Dinesh Sinnathamby
Date: March 31st, 2026
Description: Recursive function that returns the sum of all integers from 1 up to n.
"""

def sum_to(n):
    if n == 1:
        return 1
    else:
        return n + sum_to(n - 1)

def main():
    n = int(input("Enter a positive integer: "))
    print("The sum of all integers from 1 to", n, "is", sum_to(n))

main()
