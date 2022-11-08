# This file contains the Command Line Interface (CLI) for 
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board

if __name__ == '__main__':

    # Define variables outside loop:
    board = make_empty_board()
    winner = None
    
    # While there is no winner:
    while winner == None:
        print('')
        print("It's your turn! The ")
        print("Here's the current map:")

        # TODO: Show the board to the user.
        print('')
        print(board[0])
        print(board[1])
        print(board[2])
        print('')

        # TODO: Input a move from the player.
        # Take the values from the user:
        x_axis = input("Enter the horizontal position of your move (Position 1-3): ")
        print('')
        y_axis = input("Enter the vertical position of your move (Position 1-3): ")

        # TODO: Display the value you inputted: 
        print('')
        print('Your coordinates are: ')
        print(x_axis, y_axis)
        print('')
        print('The board will look like this: ')
        print('')

        # TODO: Update the board. 
        # update the board that you have:
        

        # TODO: Update who's turn it is. 
        # update the variable: 


        winner = 'X' # FIXME