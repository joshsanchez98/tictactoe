# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable. 

# OOP-injection occurs through the class Board.

# For empty_space_coords function.
import random
import pandas as pd
games_filename = "records.csv"

class Board:

    # Creates the row of the board.
    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    # Creates the strings constituting the board.
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

    def empty_space_coords(self):
        """ Returns the empty spaces of the board w/ dict. """
        new_dict = {}
        counter = 0
        for i in range(3): 
            for j in range(3):
                if self._rows[i][j] == None:
                    counter = counter + 1
                    new_dict[counter] = [i, j]
        return random.choice(list(new_dict.values()))

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
                    return 'O'
                elif self._rows[ct[i][0]][ct[i][1]] == 'X': 
                    print('X Wins!')
                    return "X"
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

def update_stats(winner, p1_name, p2_name):
    """Given a game's conclusion, update the stats on the CSV file."""
    if winner == 'O':
        winner_name = p1_name
    elif winner == 'X':
        winner_name = p2_name
    
    # Read from the file name.
    games = read_games()

    # Update the games dataframe.
    games.loc[len(games)] = {
        "Game ID": len(games) + 1,
        "Player 1": p1_name,
        "Player 2": p2_name,
        "Winner": winner_name,
    }   

    games.to_csv(games_filename)

def display_end_stats(p1_name, p2_name):
    """Given a game's conclusion, display 3 key items."""

    # Read from the file name.
    games = read_games()

    # Get and define the stats: 
    ratio_1 = get_ratio(p1_name)
    ratio_2 = get_ratio(p2_name)
    total_num = len(games)

    print('')
    print('The win ratio of', p1_name, 'is', ratio_1, '!')
    print('')
    print('The win ratio of', p2_name, 'is', ratio_2, '!')
    print('')
    print('The total number of games played on this program is', total_num, '!')

def read_games(): 
    """Reading games from a CSV file."""
    try: 
        return pd.read_csv(games_filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "Game ID",
            "Player 1",
            "Player 2",
            "Winner"
        ])

def get_ratio(name):
    """Get the ratio of a given person."""

    # Read from the file name.
    games = read_games()

    # Calculate the ratio.
    num_total = len(games[games["Player 1"] == name]) + len(games[games["Player 2"] == name])
    num_wins = len(games[games["Winner"] == name])
    return num_wins / num_total