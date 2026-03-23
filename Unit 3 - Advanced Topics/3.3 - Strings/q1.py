"""
Author: Dinesh Sinnathamby
Date: March 23rd, 2026
Description: Simple program converting a single word from English to Pig Latin.
"""

word = input()
modified = word + word[0] + "ay"
final = modified[1:]

print(final)