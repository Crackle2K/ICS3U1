"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: April 8th, 2026
Description: This program creating a moveable Tic-Tac-Toe game, 
where once both the user and the computer have completed three moves 
\without anyone winning, the oppurtunity to move a previous piece will appear, 
creating a more fun and complex twist on standard Tic-Tac-Toe.
"""

import random

def go_first_check():
    """ This is a function that asks if the player would like to go first, and returns True or False. """
    go_first = False
    check = input("Would you like to go first? (Y/N): ")
    if check.lower() == 'y':
        go_first = True
    elif check.lower() == 'n':
        go_first = False
    else:
        go_first_check()
    return go_first

def winner(board):
    """ This is a function that checks if someone has currently won the game, and if so it will return the winner's symbol. """
    
    # Horizontal win check
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != " "):
            return board[row][0]
        
    # Vertical win check
    for column in range(3):
        if (board[0][column] == board[1][column] == board[2][column]) and (board[0][column] != " "):
            return board[column][0]
        
    # Diagonal win check
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != " "):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != " "):
        return board[0][2]    
        
    return ""

def display_board(board):
    """ This is a function that displays the current state of the board, returning nothing. """
    
    print("   1   2   3")
    for row in range(3):
        row_str = str(row + 1) + ": "
        for col in range(3):
            row_str += board[row][col]
            if col < 2:
                row_str += " | "
        print(row_str)
        if row < 2:
            print(" ---+---+---")
    
def make_user_move(board):
    """ This is a function that allows the user to input a move, to then fill in a spot on the board. """
    
    valid_move = False
    while not valid_move:
        try:
            row = int(input("What row would you like to move to (1-3): "))
            col = int(input("What col would you like to move to (1-3): "))
        except ValueError:
            print("Sorry, please enter a number.\n")
            continue
        if (1 <= row <= 3) and (1 <= col <= 3) and (board[row - 1][col - 1] == " "):
            board[row - 1][col - 1] = 'X'
            valid_move = True
        else:
            print("Sorry, invalid square. Please try again!\n")

def make_computer_move(board):
    """ This is a function that allows the computer to make a move, checking if a random spot is occupied then filling it in."""
    # We need to make this smarter
    
    valid_move = False
    while not valid_move:
        random_row = random.randint(0, 2)
        random_column = random.randint(0, 2)
        if (0 <= random_row <= 2) and (0 <= random_column <= 2) and (board[random_row][random_column] == " "):
            board[random_row][random_column] = 'O'
            valid_move = True
        else:
            print("Sorry, invalid square. Please try again!\n")
            
def add_hall_of_fame():
    """ This function adds the user to the Hall of Fame if they won the game. """
    name = input("What is your name? : ")
    with open("HallOfFame.txt", 'a') as file:
        file.write(name)
        
def display_hall_of_fame():
    """ This function displays all users that have made it onto the Hall of Fame. """
    try:
        with open("HallOfFame.txt", 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("No Human Has Ever Beat Me... mwah-ha-ha-ha!")

def main():
    """ This is the mainline logic of our program, putting together all the various functions to have the program finally work. """
    display_hall_of_fame()
    ttt_board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    users_turn = go_first_check()
    free_cells = 9
    
    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            print("Your turn!")
            make_user_move(ttt_board)
            if winner(ttt_board):
                break
        else:
            print("Computers turn!")
            make_computer_move(ttt_board)
            free_cells -= 1
        users_turn = not users_turn
        
    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print ("You won!")
        add_hall_of_fame()
    elif (winner(ttt_board) == 'O'):
        print ("I won!")
    else:
        print ("Stalemate!")
        print ("\n*** GAME OVER ***\n")

main()