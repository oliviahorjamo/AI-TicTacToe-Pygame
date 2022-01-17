
class HumanPlayer:
    def __init__(self):
        pass

    def make_move(self, game):
        position_row = int(input("Enter a row position for 'X':  "))
        position_col = int(input("Enter a column position for 'X':  "))
        game.insert_letter('X', position_row, position_col)
        return
