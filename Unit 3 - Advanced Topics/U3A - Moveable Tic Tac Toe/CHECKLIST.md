
# Program Requirements

1. Your program should start by asking the user whether they want to go first. Then, it
would be best if you used proper input validation so that only “y”, “Y”, “n”, or “N”
are accepted as valid responses. 🟨 (Slightly broken, need to fix the auto defaulting to computers move if first response to prompt was a random character)

2. The Tic-Tac-toe board should be neatly displayed as three separate 3x3 grids (side-byside) using ASCII characters to divide the cells. Include numbers for each grid level,
column, and row to assist the user in selecting where to put their next “X”. Hint:
consider using the string function join() to make your code as efficient as possible
and avoid the need for repetitive code or nested loops.

3. The game should alternate turns between the user (“X”) and the computer (“O”).
After each player makes a move, check if there is a winner or a stalemate. To win,
the user or the computer must have 3 in a row -- horizontally, vertically, or
diagonally-- on the same layer or between layers. A stalemate occurs when all the
cells are filled, but no one has won. ✅

4. Once a player has all three marks placed on the grid, the player has to move a piece
when it’s their turn.

5. When getting the user’s move (i.e., layer, row, and column), use input validation and
exception handling techniques. For example, if a grid cell is already full, the user
should not be allowed to put their “X” into it. ✅

6. Use random number generation to make the computer move. For example, the
computer should randomly pick another location if a grid cell is already full. ✅

7. When a winner or stalemate is detected, the game should display an appropriate
message and end the program. ✅

8. Your program should use effective mainline logic. In addition to a main() function,
create other functions to make your code as easily read as possible. ✅

9. Your program should demonstrate mastery of the style rules we have discussed this
year, including docstrings, code comments, and good variable names. ✅

10. After you have completed requirements 1 through 9, enhance your game so that
whenever the user wins, the game asks for their name and appends it to a text file
called “HallOfFame.txt”. Before requirement #1, your program should display the
names stored in the Hall of Fame, and number each name starting with 1. If the
“HallOfFame.txt” file does not exist, the message “No Human Has Ever Beat Me..
mwah-ha-ha-ha!” should be displayed instead. ✅

11. In Tic-Tac-Toe (and Tic-Tactics), the first player can always win (or at least stalemate)
by selecting the center grid cell and mirroring their opponent’s moves. After you have
completed requirements 1 through 10, enhance your game so that the center cell of
the middle layer is reserved; that is, neither the user nor the computer can put an
“X” or “O” into it. This will make the game more challenging. Also, indicate that the
center grid cell in the middle layer is not selectable when the layers are displayed.

12. Create a level 1 smart move computer: The computer should foresee the apparent
path to win for itself and to prevent the obvious potential winner from their opponent
from playing a bet to prevent it. 