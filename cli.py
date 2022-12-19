# This file contains the Command Line Interface (CLI) for 
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Board
from logic import other_player
import time

if __name__ == '__main__':

    # Define variables outside loop:
    board = Board()
    winner = None
    player = 'O'

    # TODO: Determine whether 1-person or 2-person game:
    while True: 
        try:
            print('')
            game_mode = int(input("Type '1' for 1-person game, or type '2' for 2-person game, then press 'Enter': "))
            print('')
        except ValueError: 
            print('')
            print("Sorry, I didn't understand that! Type '1' for 1-person game, or type '2' for 2-person game, then press 'Enter': ")
            print('')
        if (game_mode != 1) & (game_mode != 2):
            print('')
            print("Try again! Type '1' for 1-person game, or type '2' for 2-person game, then press 'Enter': ")
            print('')
        else:
            break
    
    # Game Mode: Human plays bot.
    if game_mode == 1:
        
        # TODO: Show the board to the user.
        print('')
        print("Okay! Remember: You are Player 'O' and the Bot is Player 'X'!")
        print('')
        time.sleep(3) # Pause for 3 second.
        print("The current map is blank:")
        print(board)

        # TODO: Start the loop.
        while winner == None:

            # TODO: Update whose turn it is. 
            time.sleep(3) # Pause for 3 second.
            print('')
            print("It's your turn, Player...")
            print('')
            print(player)
            print('')

            # TODO: Input the move. (If bot...)
            if player == 'X':
                
                # Search for possible random spaces
                coords = board.empty_space_coords()
                y_coord = coords[0] + 1
                x_coord = coords[1] + 1

            # TODO: Input the move. (If human...)
            else: 
                # Take the values from the user:
                y_coord = input("Enter the horizontal position of your move (Position 1-3): ")
                print('')
                x_coord = input("Enter the vertical position of your move (Position 1-3): ")

            # TODO: Display the value inputted. 
            print('')
            print('The coordinates inputted are: ')
            print(y_coord, x_coord)
            print('')
            print('The board now looks like this: ')
            print('')

            # TODO: Update the board. 
            time.sleep(3) # Pause for 3 second.
            board.set_board(x_coord, y_coord, player)
            print(board)
            print('')

            # TODO: Check for win/update.
            print('Which means...')

            if board.get_winner() == True: 
                winner = True
            else: 
                player = other_player(player)

    # Game Mode: Human plays human. 
    else:

        # TODO: Show the board to the user.
        print('')
        print("Okay! This is a 2-player game! Good luck of both of you!")
        print('')
        time.sleep(3) # Pause for 3 second.
        print("The current map is blank:")
        print(board)

        # Start the loop.
        while winner == None:

            # TODO: Update whose turn it is. 
            print('')
            print("It's your turn, Player...")
            print('')
            print(player)
            print('')

            # TODO: Input a move from the player.
            # Take the values from the user:
            y_coord = input("Enter the horizontal position of your move (Position 1-3): ")
            print('')
            x_coord = input("Enter the vertical position of your move (Position 1-3): ")

            # TODO: Display the value you inputted: 
            print('')
            print('Your coordinates are: ')
            print(y_coord, x_coord)
            print('')
            print('The board now looks like this: ')
            print('')

            # TODO: Update the board. 
            time.sleep(3) # Pause for 3 second.
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