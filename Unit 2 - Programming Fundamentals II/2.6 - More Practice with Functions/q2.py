"""
Author: Dinesh Sinnathamby
Date: March 3rd, 2026
Description: This program implements a number guessing game where the computer randomly selects a number between 1 and 1000, and the user tries to guess it.
"""

import random

def game():
    number = random.randint(1, 1000)
    guess = int(input("Guess a number between 1 and 1000: "))
    
    while guess != number:
        if guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        guess = int(input("Guess a number between 1 and 1000: "))
        
    print("Congratulations! You guessed the number.")
    

def main():
    while True:
        game()
        choice = input("Would you like to play again? (Y/N): ")
        if choice.upper() != "Y":
            break
    
main()