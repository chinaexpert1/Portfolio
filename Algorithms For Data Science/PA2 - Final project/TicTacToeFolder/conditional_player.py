# Import libraries
from player import Player
from board import Board


# Represents a tic-tac-toe agent that evaluates moves using conditional logic
class ConditionalPlayer(Player):
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
        # then it checks for a winning move
        winning_move = self._get_winning_move(util_board, self.mark)
        if winning_move is not None:
            return winning_move

        # then it checks for a blocking move
        util_board = board.copy()
        blocking_move = self._get_winning_move(util_board, self.opponent_mark)
        if blocking_move is not None:
            return blocking_move

        # it replans
        available_moves = util_board.get_open_spaces()

        # the move is random otherwise
        available_moves = util_board.get_open_spaces()
        best_move = random.choice(available_moves)

        return best_move