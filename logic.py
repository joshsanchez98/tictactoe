# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable. 

# OOP-injection occurs through the class Board.

class Board:

    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self):
        s = '-------\n'
        for row in self._rows: 
            for cell in row:
                s = s + '|'
                if cell == None:
                    s = s + ' '
                else:
                    s = s + cell
            s = s + '|\n-------\n'
        return s

    

    def set_board(self, x_coord, y_coord, variable):
        """ Returns the edited board given the input. """
        self._rows[x_coord-1][y_coord-1] = variable

    def get_winner(self):
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
            if self._rows[ct[i][0]][ct[i][1]] == self._rows[ct[i][2]][ct[i][3]] == self._rows[ct[i][4]][ct[i][5]]:
                if self._rows[ct[i][0]][ct[i][1]] == 'O': 
                    print('O Wins!')
                    return True
                elif self._rows[ct[i][0]][ct[i][1]] == 'X': 
                    print('X Wins!')
                    return True
            else:
                if i != 7:
                    continue
                else:
                    if any(None in sub for sub in self._rows):
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