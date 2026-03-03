"""
Author: Dinesh Sinnathamby
Date: March 3rd, 2026
Description: This program implements a number guessing game where the user thinks of a number between 1 and 1000, and the computer tries to guess it using a binary search algorithm.
"""

def game():
    print("Think of a number from 1 to 1000, and I will try to guess it.")
    print("After each guess, please respond with 'too high', 'too low', or 'correct'.")
    min, max = 1, 1000
    while True:
        guess = (min + max) // 2
        print(f"My guess is: {guess}")
        response = input("Is my guess too high, too low, or correct? ").lower()
        if response == "too high":
            max = guess - 1
        elif response == "too low":
            min = guess + 1
        elif response == "correct":
            print("Yay! I guessed your number!")
            break
        else:
            print("Please respond with 'too high', 'too low', or 'correct'.")
            
def main():
    while True:
        game()
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again != "Y":
            print("Thanks for playing! Goodbye!")
            break
        
main()