'''Andrew Taylor
    atayl136
    These are some simple tests to make sure the goal-based player is working.'''


from board import Board
from goal_player import GoalPlayer


def test_get_next_move_empty_board():
    player = GoalPlayer(1)
    board = Board('---------')  # An empty board
    assert player.get_next_move(board) == 4, "Expected the player to choose the center space on an empty board"


def test_get_next_move_winning_move_available():
    player = GoalPlayer(1)
    board = Board('XX-O-----')  # Player 'X' can win by choosing space 2
    assert player.get_next_move(board) == 2, "Expected the player to choose the winning move"

def test_get_next_move_blocking_move_available():
    player = GoalPlayer(1)
    board = Board('OO-X-----')  # Player 'O' can win by choosing space 2, so player 'X' should block
    assert player.get_next_move(board) == 2, "Expected the player to block the opponent's winning move"

def test_get_next_move_corner_available():
    player = GoalPlayer(1)
    board = Board('O--XO----')  # Center (4) is taken by 'X', no immediate win or block, so player 'X' should take a corner
    assert player.get_next_move(board) in [0, 2, 6, 8], "Expected the player to take a corner space"


def main():
    # List of test functions
    tests = [test_get_next_move_empty_board,
             test_get_next_move_winning_move_available,
             test_get_next_move_blocking_move_available,
             test_get_next_move_corner_available]

    # Run each test
    for test in tests:
        try:
            test()
            print(f"{test.__name__}: Pass")
        except AssertionError as e:
            print(f"{test.__name__}: Fail\n\t{e}")

if __name__ == "__main__":
    main()
