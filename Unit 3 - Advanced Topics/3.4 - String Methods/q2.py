"""
Author: Dinesh Sinnathamby
Date: March 24th, 2026
Description: Simple program that counts the amount of vowels within an inputted text or word.
"""

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for i in range(len(string)):
        if string.lower()[i] in vowels:
            count += 1
    return count
    
def main():
    string = input("Enter your desired text: ")
    count = count_vowels(string)
    print("There are", count, "vowels in the text!")
    
main()