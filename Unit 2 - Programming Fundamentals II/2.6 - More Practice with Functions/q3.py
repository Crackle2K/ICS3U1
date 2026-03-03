"""
Author: Dinesh Sinnathamby
Date: March 3rd, 2026
Description: This program implements a number guessing game where the computer randomly selects a number between 1 and 1000, and the user tries to guess it.
"""

import random

def game():
    guesses = 10
    number = random.randint(1, 1000)
    guess = int(input("Guess a number between 1 and 1000: "))
    
    while guess != number and guesses > 1:
        if guess < number:
            print("Too low! Try again.")
            print(f"You have {guesses - 1} guesses left.")
        else:
            print("Too high! Try again.")
            print(f"You have {guesses - 1} guesses left.")
        guess = int(input("Guess a number between 1 and 1000: "))
        guesses -= 1
        
    if guess > 0 and guess == number:
        print("Congratulations! You guessed the number.")
    else:
        print(f"Game over! The number was {number}.")

def main():
    while True:
        game()
        choice = input("Would you like to play again? (Y/N): ")
        if choice.upper() != "Y":
            break
    
main()