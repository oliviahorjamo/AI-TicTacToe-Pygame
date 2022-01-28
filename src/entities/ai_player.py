from services.game import Game

class AiPlayer:

    def __init__(self):
        self.game = Game()

    def make_move(self, letter, position_row, position_col):
        self.game.insert_letter(letter, position_row, position_col)

    def min_max(self):
        pass
