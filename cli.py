# This file contains the Command Line Interface (CLI) for 
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import return_edited_board

if __name__ == '__main__':

    # Define variables outside loop:
    board = make_empty_board()
    winner = None
    player = 'O'
    
    # While there is no winner:
    while winner == None:
        print('')
        print("It's your turn!")
        print("Here's the current map:")

        # TODO: Show the board to the user.
        print('')
        print(board[0])
        print(board[1])
        print(board[2])
        print('')

        # TODO: Input a move from the player.
        # Take the values from the user:
        x_coord = input("Enter the horizontal position of your move (Position 1-3): ")
        print('')
        y_coord = input("Enter the vertical position of your move (Position 1-3): ")

        # TODO: Display the value you inputted: 
        print('')
        print('Your coordinates are: ')
        print(x_coord, y_coord)
        print('')
        print('The board will look like this: ')
        print('')

        # TODO: Update the board. 
        board = return_edited_board(board, x_coord, y_coord, variable)

        # TODO: Update who's turn it is. 
        # update the variable: 


        winner = True # FIXME