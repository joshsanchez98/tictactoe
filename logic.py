# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable. 

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def return_edited_board(board, x_coord, y_coord, variable):
    """ Returns the edited board given the input. """
    board[x_coord-1][y_coord-1] = variable
    return board

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None. """

    # Combinations which work. 
    ct = [[0, 0, 0, 1, 0, 2],
      [1, 0, 1, 1, 1, 2],
      [2, 0, 2, 1, 2, 2],
      [0, 0, 1, 0, 2, 0],
      [0, 1, 1, 1, 2, 1],
      [0, 2, 1, 2, 2, 2],
      [0, 0, 1, 1, 2, 2],
      [2, 0, 1, 1, 0, 2]]

    # Loop which checks for all possible combinations.
    for i in range(0,8):
        if board[ct[i][0]][ct[i][1]] == board[ct[i][2]][ct[i][3]] == board[ct[i][4]][ct[i][5]]:
            if board[ct[i][0]][ct[i][1]] == 'O': 
                print('O Wins!')
                return True
            elif board[ct[i][0]][ct[i][1]] == 'X': 
                print('X Wins!')
                return True
        else:
            if i != 7:
                continue
            else:
                if any(None in sub for sub in board):
                    print('The game can keep going!')
                    return False
                else:
                    print('A draw!')
                    return True

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'O': 
        return 'X'
    elif player == 'X':
        return 'O'