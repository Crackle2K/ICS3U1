"""
Author: Dinesh Sinnathamby
Date: April 1st, 2026
Description: A single-player Tic-Tac-Toe game where the user plays as X and the computer plays as O by making random moves.
"""

import random

def winner(board):
    """This function accepts the Tic-Tac-Toe board as a parameter.
    If there is no winner, the function will return the empty string "".
    If the user has won, it will return "X", and if the computer has
    won it will return "O"."""
    
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
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will print the Tic-Tac-Toe board grid (using ASCII characters)
    and show the positions of any X's and O's. It also displays
    the column and row numbers on top and beside the board to help
    the user figure out the coordinates of their next move.
    This function does not return anything."""
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
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will ask the user for a row and column. If the row and
    column are each within the range of 1 and 3, and that square
    is not already occupied, then it will place an "X" in that square."""
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
    """This function accepts the Tic-Tac-Toe board as a parameter.
    It will randomly pick row and column values between 0 and 2.
    If that square is not already occupied, it will place an "O"
    in that square. Otherwise, another random row and column
    will be generated."""
    # Code needed here...

    valid_move = False
    while not valid_move:
        random_row = random.randint(0, 2)
        random_column = random.randint(0, 2)
        if (0 <= random_row <= 2) and (0 <= random_column <= 2) and (board[random_row][random_column] == " "):
            board[random_row][random_column] = 'O'
            valid_move = True
        else:
            print("Sorry, invalid square. Please try again!\n")

def main():
    """Our Main Game Loop:"""
    free_cells = 9
    users_turn = True
    ttt_board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
            free_cells -= 1
        display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print ("Y O U W O N !")
    elif (winner(ttt_board) == 'O'):
        print ("I W O N !")
    else:
        print ("S T A L E M A T E !")
        print ("\n*** GAME OVER ***\n")

# Start the game!
main()