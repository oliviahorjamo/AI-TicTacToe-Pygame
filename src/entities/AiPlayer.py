class AiPlayer:
    def __init__(self):
        pass

    def make_move(self, game):
        position = int(input("Enter the position for '0':  "))
        game.insert_letter('0', position)
        return

    def min_max(self):
        pass
