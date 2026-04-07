"""
Author: Dinesh Sinnathamby
Date: April 7th, 2026
Description: This is a simple program that encrypts your desired message using the Caeser Cipher method, with a right shift of 1.
"""

text = input("Enter your message: ")

cipher = ''
for ch in text:
    if not ch.isalpha():
        cipher +=" "
        continue
    
    ch = ch.upper()
    code = ord(ch) + 1
    print(code)
    
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
    
print(cipher)