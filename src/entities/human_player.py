from services.game import Game


class HumanPlayer:
    def __init__(self):
        self.game = Game()

    def make_move(self, letter, position_row, position_col):
        self.game.insert_letter(letter, position_row, position_col)
