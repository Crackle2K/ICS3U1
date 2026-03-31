"""
Author: Dinesh Sinnathamby
Date: March 31st, 2026
Description: This is a simple program that works by calculating the factorial of a number the user inputs.
"""

def main():
    number = int(input("Enter a non-negative integer: "))
    fact = factorial(number)
    print("The factorial of", number, "is", str(fact) + '.')

def factorial(num):
    retrieve = 1
    while num != 1:
        retrieve *= num
        num -= 1
    return retrieve
    
main()