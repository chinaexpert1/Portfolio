import numpy as np
from board import Board
from conditional_player import ConditionalPlayer
from argmax import argmax
import random

class UtilityPlayer(ConditionalPlayer):
    # initiaize the player
    def __init__(self, number):
        self.number = number
        self.mark = "X" if self.number == 1 else "O"
        self.opponent_mark = "O" if self.number == 1 else "X"
        self.lines = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6))

    # this is the heart of the agent
    def get_next_move(self, board):
        # simple reassignment
        util_board = board

        # it checks for a win
        winning_move = self._get_winning_move(util_board, self.mark)
        if winning_move is not None:
            return winning_move

        # it checks for a block
        opponent_mark = 'O' if self.mark == 'X' else 'X'
        blocking_move = self._get_winning_move(util_board, opponent_mark)
        if blocking_move is not None:
            return blocking_move

        # it uses the utility methods to play according to the evaluation function
        util_lines = self.get_utility_of_lines(util_board)   # this runs get_line_utility inside
        util_spaces = self.get_utility_of_spaces(board, util_lines)
        best_move = np.argmax(util_spaces)

        return best_move

    # this checks for winning moves using a model
    def _get_winning_move(self, util_board, mark):
        available_moves = util_board.get_open_spaces()
        for move in available_moves:
            temp_board = util_board.copy()
            temp_board.mark_space(move, mark)
            if temp_board.has_win(mark) == True:
                return move
            else:
                temp_board.spaces[move] = '-'
        return None

    # a required method to find the max utility
    #def get_utility_of_spaces(self, board, util_lines):
        # begin planning with a model
        # Cost: c1 + c3 + c4*n + c3 + c7*n + c1 + c3 + (2n - 1)c2 + c3 + (2n - 1)c1 + c3 + (n - 1)c2
        #util_board = board
       # available_moves = util_board.get_open_spaces()

        # finds the max utility
       # max_index = np.argmax(util_lines)
        # tiebreaker logic (secondary evaluation)
        #if 0 > 1:
           # bestmove = self._break_ties(max_index)
          #  for move in self.lines[bestmove]:
          #      if move in available_moves:
           #         return move
        #else:
       # for move in self.lines[max_index]:      # it takes the max utility space
          #  if move in available_moves:
           #     return move

       # return

    # I decided to break ties randomly so as not to upstage the evaluation function
    def _break_ties(self, best_moves):
        return random.choice(best_moves)

    # copy of board function to make it available inside the class
    def mark_space(self, space: int, mark: str):
        if not self.is_open_space(space):
            raise Exception("Move is not valid.")
        self.spaces[space] = mark

    # another required function to get the utility of a line or diagonal
    def get_line_utility(self, board, line):
        # Cost: 3c1 + 2c3 + 8c2 + 2c5 + c1 = 4c1 + 2c3 + 8c2 + 2c5
        agentMarks = 0
        opponentMarks = 0

        # tally the marks in the line
        for space in line:
            if board.spaces[space] == self.mark:
                agentMarks += 1
            elif board.spaces[space] == self.opponent_mark:
                opponentMarks += 1

        # conditionals used to set the values of the variables in the evaluation function
        x1 = 0
        x2 = 0
        o1 = 0
        o2 = 0
        if agentMarks == 2:
            if self.mark == 'O':
                o1 = 0
                o2 = 2
            else:
                x1 = 0
                x2 = 2
        elif agentMarks == 1:
            if self.mark == 'O':
                o1 = 1
                o2 = 0
            else:
                x1 = 1
                x2 = 0
        if opponentMarks == 2:
            if self.opponent_mark == 'X':
                x1 = 0
                x2 = 2
            else:
                o1 = 0
                o2 = 2
        elif opponentMarks == 1:
            if self.opponent_mark == 'X':
                x1 = 1
                x2 = 0
            else:
                o1 = 1
                o2 = 0

            # evaluation function here
        if self.number == 2:
            SpaceUtility = 3*o2+o1-(3*x2+x1)
        elif self.number == 1:
            SpaceUtility = 3 * x2 + x1 - (3 * o2 + o1)
        return SpaceUtility

    # required function to get the utility of all lines
    def get_utility_of_lines(self, board):
        # Cost: c1 + n * (c1 + 3c2 + c3 + c8) = (n + 1)c1 + 3nc2 + nc3 + nc8
        lineUtilities = []
        for i, line in enumerate(self.lines):
            if board.spaces[line[0]] == "-" and board.spaces[line[1]] == "-" and board.spaces[line[2]] == "-":
                utility = 0
            elif board.spaces[line[0]] != "-" and board.spaces[line[1]] != "-" and board.spaces[line[2]] != "-":
                utility = -10
            else:
                utility = self.get_line_utility(board, line)
            lineUtilities.append(utility)
        return lineUtilities

    def is_line_full(self, board_string, line):
        for index in line:
            if board_string.spaces[index] == '-':
                return False
        return True

    def is_line_empty(self, board_string, line):
        for index in line:
            if board_string.spaces[index] != '-':
                return False
        return True

    def get_utility_of_spaces(self, board, util_lines):
        # Cost: c1 + n * (c1 + 3c2 + c3 + c8) = (n + 1)c1 + 3nc2 + nc3 + nc8
        lineUtilities = []
        for i, line in enumerate(self.lines):
            if board.spaces[line[0]] == "-" and board.spaces[line[1]] == "-" and board.spaces[line[2]] == "-":
                utility = 0
            elif board.spaces[line[0]] != "-" and board.spaces[line[1]] != "-" and board.spaces[line[2]] != "-":
                utility = -10
            else:
                utility = self.get_line_utility(board, line)
            lineUtilities.append(utility)
        return lineUtilities

