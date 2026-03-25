"""
Author: Dinesh Sinnathamby
Date: March 23rd, 2026
Description: Simple program that randomizes the characters in a word, and returns a scrambled product.
"""

import random

def word_jumble(word):
    
    new = ""
    current_word = word
    
    while len(current_word) > 0:
        randomIndex = random.randint(0, len(current_word) - 1)
        char = current_word[randomIndex]
        new += char
        current_word = current_word[:randomIndex] + current_word[randomIndex + 1:]

    return new

def main():
    word = input("Enter a word to get scrambled: ")
    new = word_jumble(word)
    print("The word scrambled up is", new)
    
main()