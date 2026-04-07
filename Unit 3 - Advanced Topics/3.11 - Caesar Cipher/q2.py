"""
Author: Dinesh Sinnathamby
Date: April 7th, 2026
Description: This program checks whether two entered strings are anagrams of each other.
"""

def main():
    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")

    first_string = first_string.replace(" ", "").upper()
    second_string = second_string.replace(" ", "").upper()

    if first_string == "" and second_string == "":
        print("Not anagrams")
    elif sorted(first_string) == sorted(second_string):
        print("Anagrams")
    else:
        print("Not anagrams")

main()
