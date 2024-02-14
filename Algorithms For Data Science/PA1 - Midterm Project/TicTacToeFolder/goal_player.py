'''by Andrew Taylor
    atayl136
    This is a goal-based agent that is based on the following premise: that the center is the most valuable space in the game \
    and otherwise the corners are most valuable. The agent looks to take the center whenever available, and it tries to win \
    and block first, or choose a corner otherwise. If none of these considerations are relevant, the move can be chosen randomly.'''

from board import Board
from conditional_player import ConditionalPlayer
from argmax import argmax
import random

class GoalPlayer(ConditionalPlayer):
    # initialize the player
    def __init__(self, number):
        self.number = number
        self.mark = "X" if number == 1 else "O"
        self.opponent_mark = "O" if number == 1 else "X"

    # the heart of the agent
    def get_next_move(self, board):
        # it makes a copy of the board to plan with
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

        # Built-in strategy to favor the center
        if util_board.spaces[4] == '-':
            return 4
        else:
            available_moves = util_board.get_open_spaces()
            # it Checks the opponents corners if the center is taken
            if util_board.spaces[2] or util_board.spaces[8] == self.opponent_mark:
                for block in available_moves:
                    if block in [2, 6]:
                        return block
            if util_board.spaces[6] == self.opponent_mark:
                for block in available_moves:
                    if block in [2, 6, 8]:
                        return block

        # it replans
        available_moves = util_board.get_open_spaces()

        # then it Checks the corners if it has the center
        if util_board.spaces[0] and util_board.spaces[8] == self.opponent_mark:
            for block in available_moves:
                if block in [3, 1, 5, 7]:
                    return block
        if util_board.spaces[2] and util_board.spaces[6] == self.opponent_mark:
            for block in available_moves:
                if block in [1, 3, 5, 7]:
                    return block

        # then it favors the corners if open
        for corner in [0, 6, 2, 8]:
            if corner in available_moves:
                return corner

        # the move is random otherwise
        available_moves = util_board.get_open_spaces()
        best_move = random.choice(available_moves)

        return best_move

    def _get_winning_move(self, util_board, mark):
        # c1 + c3 + c7*n
        available_moves = util_board.get_open_spaces()
        # c1 + n * (c2 + c3 + c4*n + c5 + c3 + c6*n + c1 + c5)
        for move in available_moves:
            # c1 + c3 + c4*n
            temp_board = util_board.copy()
            # c3 + c5
            temp_board.mark_space(move, mark)
            # c3 + c6*n
            if temp_board.has_win(mark) == True:
                # c1
                return move
            else:
                # c1 + c5
                temp_board.spaces[move] = '-'
        # c1
        return None




