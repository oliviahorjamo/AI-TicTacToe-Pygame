class GameBoard:
    """A class that represents the game board.

    Attributes:
                self.board_size: The size of the game board
                self.board: the game board
    """
    def __init__(self):
        """A constructor of the class that initializes the game board."""
        self.board_size = 15
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]

    def print_game_board(self):
        """A method that prints the game_board on terminal"""
        for i in self.board:
            print(i)

    def reset_game_board(self):
        """A method that resets the game board"""
        board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board = board
        return self.board
