"""
Authors: Dinesh Sinnathamby, Dhani Shah
Date: April 8th, 2026
Description: This program creates a moveable Tic-Tac-Toe game,
where once both the user and the computer have completed three moves
without anyone winning, the oppurtunity to move a previous piece will appear,
creating a more fun and complex twist on standard Tic-Tac-Toe.
"""

import random

def go_first_check():
    """ This is a function that asks if the player would like to go first, and returns True or False. """
    check = input("Would you like to go first? (Y/N): ")
    if check.lower() == 'y': # Checks if the user responded with yes
        return True
    elif check.lower() == 'n': # Checks if the user responded with no
        return False
    else: # Checks if the user responded with neither yes or no
        return go_first_check()

def winner(board):
    """ This is a function that checks if someone has currently won the game, and if so it will return the winner's symbol. """

    # Horizontal win check
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != " "):
            return board[row][0]

    # Vertical win check
    for column in range(3):
        if (board[0][column] == board[1][column] == board[2][column]) and (board[0][column] != " "):
            return board[0][column]

    return ""

def check_player_moves(board):
    """ This is a function that checks the amount of moves the player has done through the game. """

    player_moves = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] == 'X':
                player_moves += 1

    return player_moves

def check_computer_moves(board):
    """ This is a function that checks the amount of moves the computer has done through the game. """

    computer_moves = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] == 'O':
                computer_moves += 1
    return computer_moves

def user_remove_tile(board):
    """ This is a function that allows the user to remove a previous tile and select a new one, after they have done three moves."""

    occupiedTile = False
    while not occupiedTile:
        try:
            remove_row = int(input("What row would you like to remove from (1-3): "))
            remove_col = int(input("What col would you like to remove from (1-3): "))
        except ValueError:
            print("Sorry, please enter a number.\n")
            continue
        if (1 <= remove_row <= 3) and (1 <= remove_col <= 3) and (board[remove_row - 1][remove_col - 1] == 'X'):
            board[remove_row - 1][remove_col - 1] = ' '
            occupiedTile = True
        else:
            print("Sorry, you cannot remove your symbol from this tile. Please try again!\n")

def computer_remove_tile(board):
    """ This is a function that allows the computer to remove a previous tile and select a new one, after they have done three moves. """

    o_positions = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'O':
                o_positions.append((r, c))

    best_to_remove = None
    min_alignment = 3

    for pos in o_positions:
        r, c = pos
        alignment = 0
        for other_pos in o_positions:
            if other_pos != pos:
                other_r, other_c = other_pos
                if other_r == r or other_c == c:
                    alignment += 1
        if alignment < min_alignment:
            min_alignment = alignment
            best_to_remove = pos

    if best_to_remove:
        board[best_to_remove[0]][best_to_remove[1]] = ' '

def display_board(board):
    """ This is a function that displays the current state of the board, returning nothing. """

    print("   ".join(['   1', '2', '3']))
    for row in range(3):
        row_str = str(row + 1) + ": "
        for col in range(3):
            row_str += board[row][col]
            if col < 2:
                row_str += " | "
        print(row_str)
        if row < 2:
            print("  ---+---+---")

def make_user_move(board):
    """ This is a function that allows the user to input a move, to then fill in a spot on the board. """

    valid_move = False
    while not valid_move: # Loop runs until the user makes a valid move
        try:
            row = int(input("What row would you like to move to (1-3): "))
            col = int(input("What col would you like to move to (1-3): "))
        except ValueError:
            print("Sorry, please enter a number.\n")
            continue
        if (1 <= row <= 3) and (1 <= col <= 3) and (board[row - 1][col - 1] == " "): # Checks if the row and colum are valid
            board[row - 1][col - 1] = 'X'
            valid_move = True
        else:
            print("Sorry, invalid square. Please try again!\n")

def make_computer_move(board):
    """ This is a function that allows the computer to make a move, first checks if computer can win and takes that spot
    then checks if user can win and takes that spot, then if nothing is winable it goes to a random spot. """

    for r in range(3):
        for c in range(3):
            if board[r][c] == " " and winner_comp_move(board, r, c, 'O'):
                board[r][c] = 'O'
                return

    for r in range(3):
        for c in range(3):
            if board[r][c] == " " and winner_comp_move(board, r, c, 'X'):
                board[r][c] = 'O'
                return

    valid_move = False
    while not valid_move: # Loop runs until the computer's move is finally valid
        random_row = random.randint(0, 2)
        random_column = random.randint(0, 2)
        if board[random_row][random_column] == " ": # Checks if tile is empty
            board[random_row][random_column] = 'O'
            valid_move = True

def winner_comp_move(board, r, c, symbol):
    """ Check if move results in a win. """

    board[r][c] = symbol
    is_winner = winner(board) == symbol
    board[r][c] = " "
    return is_winner

def add_hall_of_fame():
    """ This function adds the user to the Hall of Fame if they won the game. """

    name = input("What is your name? : ")
    with open("HallOfFame.txt", 'a') as file:
        file.write("\n" + name)

def display_hall_of_fame():
    """ This function displays all users that have made it onto the Hall of Fame. """

    try:
        with open("HallOfFame.txt", 'r') as file:
            content = file.read()
            words = content.split()
            print("Hall of Fame")
            index = 0
            for word in words:
                index += 1
                print(str(index) + '.', word)
    except FileNotFoundError:
        print("No Human Has Ever Beat Me... mwah-ha-ha-ha!")

def turn(ttt_board, users_turn):
    """ This function navigates between users turn and computers turn. """

    while not winner(ttt_board):
        display_board(ttt_board)

        free_cells = sum(1 for r in range(3) for c in range(3) if ttt_board[r][c] == ' ')
        if free_cells == 0:
            break

        player_moves = check_player_moves(ttt_board)
        computer_moves = check_computer_moves(ttt_board)

        if users_turn: # Checks if it is currently the user's turn
            print("Your turn!")
            if player_moves >= 3: # Checks if the player has already done more than 3 moves
                print("You already have 3 tiles on the board. Remove one before placing a new one.")
                user_remove_tile(ttt_board)
                display_board(ttt_board)
            make_user_move(ttt_board)
        else: # Checks if it is currently the player's turn
            print("Computer's turn!")
            if computer_moves >= 3: # Checks if the computer has already done more than 3 moves
                computer_remove_tile(ttt_board)
            make_computer_move(ttt_board)

        if winner(ttt_board): # If there is a winner, the game loop should stop
            break

        users_turn = not users_turn

def main():
    """ This is the mainline logic of our program, putting together all the various functions to have the program finally work. """

    display_hall_of_fame()
    ttt_board = [[" ", " ", " "],[" ", "*", " "],[" ", " ", " "]]
    users_turn = go_first_check()

    turn(ttt_board, users_turn)

    display_board(ttt_board)
    if (winner(ttt_board) == 'X'): # Checks if the winner was the player
        print ("You won!")
        add_hall_of_fame()
    elif (winner(ttt_board) == 'O'): # Checks if the winner was the computer
        print ("I won!")
    else:
        print ("Stalemate!")
        print ("GAME OVER!")

main()
