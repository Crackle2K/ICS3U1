"""
Author: Dinesh Sinnathamby
Date: March 3rd, 2026
Description: This program implements a simple Rock-Paper-Scissors game where the user plays against the computer.
"""

import random

def main():
    ranChoice = random.randint(1, 3)
    if ranChoice == 1:
        compChoice = "Rock"
    if ranChoice == 2:
        compChoice = "Paper"
    if ranChoice == 3:
        compChoice = "Scissors"

    print("Select your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    userChoice = int(input("Enter the number corresponding to your move: "))

    if userChoice == 1:
        userChoice = "Rock"
    if userChoice == 2:
        userChoice = "Paper"
    if userChoice == 3:
        userChoice = "Scissors"

    print("You chose", userChoice + '!')
    print("Computer chose", compChoice + '!')

    if userChoice == compChoice:
        print("It's a tie!")
    elif (userChoice == "Rock" and compChoice == "Scissors") or \
        (userChoice == "Paper" and compChoice == "Rock") or \
        (userChoice == "Scissors" and compChoice == "Paper"):
        print("You win!")
    else:
        print("You lost!")

main()