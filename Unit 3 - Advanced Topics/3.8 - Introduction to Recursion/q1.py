"""
Author: Dinesh Sinnathamby
Date: March 31st, 2026
Description: Recursive function that computes the greatest common denominator between all numbers.
"""

def gcd(m, n):
    remainder = m % n
    if remainder == 0:
        return n
    else:
        return gcd(n, remainder)

def main():
    first_num = int(input("Enter your first number: "))
    second_num = int(input("Enter your second number: "))
    print("The GCD is", str(gcd(first_num, second_num)) + '.')
    
main()