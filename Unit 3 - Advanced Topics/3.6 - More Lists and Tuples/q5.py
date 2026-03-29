"""
Author: Dinesh Sinnathamby
Date: March 29th, 2026
Description: This is a simple program that selects a random word from a predefined list and displays a scrambled version of that word.
"""

import random

words = [
    "Strawberry", "Pear", "Apple", "Banana", "Orange", "Grape", "Pineapple", "Peach", "Raspberry"
]

while len(words) > 0:
    randomIndex = random.randint(0, len(words) - 1)
    currentWord = words[randomIndex]
    words.remove(currentWord)

    temp_word = currentWord
    scrambled = ""
    while len(temp_word) > 0:
        charIndex = random.randint(0, len(temp_word) - 1)
        scrambled += temp_word[charIndex]
        temp_word = temp_word[:charIndex] + temp_word[charIndex + 1:]

    print("Scrambled word: " + scrambled)
    
    guess = ""
    while guess.lower() != currentWord.lower():
        guess = input("Guess the word: ")
        if guess.lower() == currentWord.lower():
            print("Correct!")
        else:
            print("Try again.")

print("All words have been used!")