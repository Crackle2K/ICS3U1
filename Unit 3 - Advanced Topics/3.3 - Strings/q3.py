"""
Author: Dinesh Sinnathamby
Date: March 23rd, 2026
Description: Simple program that displays the amount of words within your inputted text.
"""

def word_count(string):
    count = 1
    for character in string:
        if character == ' ':
            count += 1
    return count

def main():
    string = input("Enter your desired text: ")
    words = word_count(string)
    print("There are", words, "words in your text!")
    
main()