from services.game import Game
from entities.AiPlayer import AiPlayer
from entities.HumanPlayer import HumanPlayer
from services.gameboard import GameBoard


class GameLoop:
    def __init__(self):
        self.game = Game()
        self.ai = AiPlayer()
        self.human = HumanPlayer()
        self.gameboard = GameBoard()

    def run(self):
        print()
        print('Welcome to play TicTacToe. Try to get 5 X-letters side by side!')
        print(self.gameboard.print_grid())
        while True:
            self.human.make_move(self.game)