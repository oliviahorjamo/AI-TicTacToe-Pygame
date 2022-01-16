from services.game import Game
from entities.AiPlayer import AiPlayer
from entities.HumanPlayer import HumanPlayer


class GameLoop:
    def __init__(self):
        self.game = Game()
        self.ai = AiPlayer()
        self.human = HumanPlayer()

    def run(self):
        while True:
            self.human.make_move(self.game)
            self.ai.make_move(self.game)
