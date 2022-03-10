class GameBoard:
    """A class that represents the game board.

    Attributes:
             self.board_size: The size of the game board
             self.board: the game board
    """

    def __init__(self):
        """A constructor of the class that initializes the game board."""
        self.board_size = 25
        self.board = [[0 for _ in range(self.board_size)]
                      for _ in range(self.board_size)]
