"""
Author: Dinesh Sinnathamby
Date: April 7th, 2026
Description: This program checks whether the characters of a word appear in order inside a second string.
"""

def main():
    word = input("Enter the word to search for: ")
    text = input("Enter the string to search in: ")

    pos = 0
    found = True

    for letter in word:
        pos = text.find(letter, pos)
        if pos == -1:
            found = False
            break
        pos += 1

    if found:
        print("Yes")
    else:
        print("No")

main()
