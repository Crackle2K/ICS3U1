"""
Author: Dinesh Sinnathamby
Date: April 7th, 2026
Description: This program calculates the Digit of Life from a user's birthday.
"""

def main():
    date = input("Enter your birthday date (in YYYYMMDD): ")

    while len(date) > 1:
        date = str(sum(int(digit) for digit in date))

    print("Your Digit of Life is: " + date)

main()
