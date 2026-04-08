
        random_column = random.randint(0, 2)
        if (0 <= random_row <= 2) and (0 <= random_column <= 2) and (board[random_row][random_column] == " "):
            board[random_row][random_column] = 'O'
            valid_move = True
        else:
            print("Sorry, invalid square. Please try again!\n")

def main():
    free_cells = 9
    if go_first_check() == True: