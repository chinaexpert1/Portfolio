
from player import Player
from board import Board

# Represents a brute-force minimax agent
class MinimaxPlayer(Player):

    def __init__(self, number):
        self.number = number
        self.mark = "X" if number == 1 else "O"
        self.opponent_mark = "O" if number == 1 else "X"

    # Gets the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        player = self.mark  # Current player to move
        value, move = self.MaxValue(board, player)
        return move

    def MaxValue(self, board: Board, player: str) -> (int, int):
        if self.is_terminal(board):
            return self.get_score(board, player), None
        v = float('-inf')
        move = None
        for action in board.get_open_spaces():
            result_board = self.result(board, action, player)
            v2, a2 = self.MinValue(result_board, player)  # Recursive call to MinValue
            if v2 > v:
                v, move = v2, action
        return v, move

    def MinValue(self, board: Board, player: str) -> (int, int):
        if self.is_terminal(board):
            return self.get_score(board, player), None
        v = float('inf')
        move = None
        for action in board.get_open_spaces():
            result_board = self.result(board, action, player)
            v2, a2 = self.MaxValue(result_board, player)  # Recursive call to MaxValue
            if v2 < v:
                v, move = v2, action
        return v, move

    def is_terminal(self, board: Board) -> bool:
        return board.is_full() or board.has_win("X") or board.has_win("O")

    def result(self, board: Board, action: int, player: str) -> Board:
        new_board = board.copy()
        new_board.mark_space(action, player)
        return new_board

    def get_score(self, board: Board, player: str) -> int:
        if board.has_win(player):
            return 1
        elif board.has_win(self.opponent_mark):
            return -1
        else:
            return 0
