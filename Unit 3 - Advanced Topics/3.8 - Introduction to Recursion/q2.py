"""
Author: Dinesh Sinnathamby
Date: March 31st, 2026
Description: Recursive function that computes the product of two numbers using repeated addition.
"""

def multiply(x, y):
    if y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)

def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x, "x", y, "=", multiply(x, y))

main()
