"""
Author: Dinesh Sinnathamby
Date: March 31st, 2026
Description: Recursive function that computes the power of a number given a non-negative integer exponent.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

def main():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    print(base, "^", exponent, "=", power(base, exponent))

main()
