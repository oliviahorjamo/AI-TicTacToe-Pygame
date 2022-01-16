
class HumanPlayer:
    def __init__(self):
        pass

    def make_move(self, game):
        position = int(input("Enter the position for 'X':  "))
        game.insert_letter('X', position)
        return
