class GameBoard:
    """A class that represents the game board."""
    def __init__(self):
        """A constructor of the class that initializes the game board."""
        self.grid_size = 30
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def print_grid(self):
        """A method that updates the game board while playing."""
        for i in self.grid:
            print(i)
