# Import libraries
from random_player import RandomPlayer
# from conditional_player import ConditionalPlayer
from utility_player import UtilityPlayer
from goal_player import GoalPlayer
from minimax_player import MinimaxPlayer
# from alpha_beta_player import AlphaBetaPlayer
from human_player import HumanPlayer
from game import Game

# Set the players for the game
player1 = HumanPlayer(1)

difficulty = input('Enter 1 for easy, 2 for Medium, 3 for Hard:')

if difficulty == '1':
    player2 = RandomPlayer(2)
elif difficulty == '2':
    playerchoice = input('Enter 1 for Goal Based and 2 for Utility Player:')
    if playerchoice == '1':
        player2 = GoalPlayer(2)
    elif playerchoice == '2':
        player2 = UtilityPlayer(2)
    else:
        print('Invalid Selection.')
elif difficulty == '3':
    player2 = MinimaxPlayer(2)
else:
    print('Invalid Selection.')




# Loop until the user chooses to exit the program
while True:

    # Create a new game using the two players
    game = Game(player1, player2)

    # Play the game to it's conclusion
    game.play()

    # Ask the user if they want to continue
    choice = input("Play another game? Y/N: ")

    # Exit the program if the user doesn't want to play anymore
    if choice != "Y":
        break




