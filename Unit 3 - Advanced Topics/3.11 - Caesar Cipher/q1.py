"""
Author: Dinesh Sinnathamby
Date: April 7th, 2026
Description: This is a simple program that encrypts your desired message using the Caeser Cipher method, with a right shift of 1.
"""

def caesar_cipher(text, shift):
    cipher = ""

    for character in text:
        if not character.isalpha():
            cipher += character
        elif character.isupper():
            cipher += chr((ord(character) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher += chr((ord(character) - ord('a') + shift) % 26 + ord('a'))

    return cipher

def main():
    text = input("Enter your message: ")
    while True:
        shift = int(input("Enter the amount to shift by: "))
        if 1 <= shift <= 25:
            break
        print("Invalid shift value. Please enter a number between 1 and 25.")
    cipher = caesar_cipher(text, shift)
    print(cipher)
    
main()