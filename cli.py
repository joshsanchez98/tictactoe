# This file contains the Command Line Interface (CLI) for 
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Board
from logic import other_player

if __name__ == '__main__':

    # Define variables outside loop:
    board = Board()
    winner = None
    player = 'O'

    # TODO: Determine whether 1-person or 2-person game:
    game_mode = input("Press '1' for 1-person game, or press '2' for 2-person game: ")
    
    # Game Mode: Human plays bot.
    if game_mode == 1:

        print('Not fixed, buddy.')
        winner = True

    # Game Mode: Human plays human. 
    elif game_mode == 2:

        while winner == None:
            # TODO: Update who's turn it is. 
            print('')
            print("It's your turn, Player...")
            print('')
            print(player)
            print('')
            print("Here's the current map:")

            # TODO: Show the board to the user.
            print('')
            print(board)
            print('')

            # TODO: Input a move from the player.
            # Take the values from the user:
            y_coord = input("Enter the horizontal position of your move (Position 1-3): ")
            print('')
            x_coord = input("Enter the vertical position of your move (Position 1-3): ")

            # TODO: Display the value you inputted: 
            print('')
            print('Your coordinates are: ')
            print(x_coord, y_coord)
            print('')
            print('The board now looks like this: ')
            print('')

            # TODO: Update the board. 
            board.set_board(x_coord, y_coord, player)
            print(board)
            print('')

            # TODO: Check for win/update. 
            print('Which means...')
            # print(board.get_winner())

            if board.get_winner() == True: 
                winner = True
            else: 
                player = other_player(player)

    else:

        print('Run this thing again. Did not input 1 or 2.')
        winner = True