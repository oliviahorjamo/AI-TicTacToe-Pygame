class GameBoard:
    """A class that represents the game board.

    Attributes:
                self.grid_size: The size of the game board
                self.grid: the game board
    """
    def __init__(self):
        """A constructor of the class that initializes the game board."""
        self.grid_size = 3
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def print_grid(self):
        """A method that prints the game_board on terminal"""
        for i in self.grid:
            print(i)

    def reset_game_board(self):
        """A method that resets the game board"""
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

g = GameBoard()
print(g.print_grid())