# Import libraries
from player import Player
from board import Board
import random


# Represents a tic-tak-toe player using purely random moves
class RandomPlayer(Player):
    def __init__(self, number):
        self.number = number
        self.mark = "X" if number == 1 else "O"
        self.opponent_mark = "O" if number == 1 else "X"
        self.lines = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6))

    def get_next_move(self, board):
        util_board = board.copy()

        # the move is random otherwise
        available_moves = util_board.get_open_spaces()
        best_move = random.choice(available_moves)

        return best_move
