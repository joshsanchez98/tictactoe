# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable. 

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def return_edited_board(board, x_axis, y_axis, variable):
    """ Returns the edited board given the input. """
    board[x_axis][y_axis] = variable
    return board

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None. """
    
    return None # FIXME

def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'O' # FIXME