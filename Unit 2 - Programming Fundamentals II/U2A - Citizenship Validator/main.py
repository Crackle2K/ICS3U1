"""
Author: Dinesh Sinnathamby
Date: March 9th, 2026
Description: The main project file for the citizenship validator assignment in Python.
"""

import check_CIN # This imports my other Python file, check_CIN.py

def main(): # Mainline logic
    while True:
        first_letter = input("Enter starting letter (X or K), or -1 to quit: ").strip().upper()

        if first_letter == "-1":
            break # exits the program

        if first_letter not in ("X", "K"):
            print("Invalid letter. CIN must start with X or K.")
            continue

        number_text = input("Enter the 8-digit number part of the CIN: ").strip()

        if number_text == "-1":
            break # exits the program

        if not (number_text.isdigit() and len(number_text) == 8):
            print("Invalid number. Please enter exactly 8 digits.")
            continue

        number_value = int(number_text)
        cin_display = first_letter + number_text

        if check_CIN.is_valid(number_value):
            print(cin_display, "is valid.")
        else:
            print(cin_display, "is invalid.")


main()