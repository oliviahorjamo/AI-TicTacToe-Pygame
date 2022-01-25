from services.game_board import GameBoard


class Game:

    """A class that represents the game functionalities.

    Attributes:
                self.game_board: An object that imports the game board methods."""

    def __init__(self):
        """A constructor of the class that initializes the game functionalities."""

        self.game_board = GameBoard()

    def check_for_space(self, row, col):
        """A method that checks whether the player can insert letter to the game board.

        Args:
            row (index): row position on the game board.
            col (index): col position on the game board.

        Returns:
            (boolean): returns True if the index of the game board is 0, else False.
        """
        if self.game_board.grid[row][col] == 0:
            return True
        return False

    def insert_letter(self, player, position_row, position_col):
        """A method to insert a letter to a given position on the gameboard.

        Args:
            player (str): letter of the player to be inserted.
            position_row (int): a row position to insert the letter.
            position_col (int): a column position to insert the letter.
        """

        self.game_board.grid[position_row][position_col] = player

    def check_for_win_horizontal(self, grid, grid_size):
        """A method to check if there is a horizontal win.

        Args:
            grid (matrix): game board.
            grid_size (int): a size of the game board.

        Returns:
            (boolean): returns True if there is a horizontal win, else False.
        """
        for row in range(grid_size):
            for col in range(grid_size):
                if row + 4 < grid_size and grid[row][col] != 0:
                    if grid[row][col] == grid[row][col + 1] \
                        and grid[row][col + 1] == grid[row][col + 2] \
                            and grid[row][col + 2] == grid[row][col + 3] \
                                and grid[row][col + 3] == grid[row][col + 4]:
                        return True
        return False

    def check_for_win_vertical(self, grid, grid_size):
        """A method to check if there is a vertical win.

        Args:
            grid (matrix): game board.
            grid_size (int): a size of the game board.

        Returns:
            (boolean): returns True if there is a vertical win, else False.
        """
        for row in range(grid_size):
            for col in range(grid_size):
                if col + 4 < grid_size and grid[row][col] != 0:
                    if grid[row][col] == grid[row + 1][col] \
                        and grid[row + 1][col] == grid[row + 2][col] \
                            and grid[row + 2][col] == grid[row + 3][col] \
                                and grid[row + 3][col] == grid[row + 4][col]:
                        return True
        return False

    def check_for_win_desc_diagonal(self, grid, grid_size):
        """A method to check if there is a descending diagonal win.

        Args:
            grid (matrix): game board.
            grid_size (int): a size of the game board.

        Returns:
            (boolean): returns True if there is a  descending diagonal win, else False.
        """
        for row in range(grid_size):
            for col in range(grid_size):
                if row + 4 < grid_size and col + 4 < grid_size and grid[row][col] != 0:
                    if grid[row][col] == grid[row + 1][col + 1] \
                        and grid[row + 1][col + 1] == grid[row + 2][col + 2] \
                            and grid[row + 2][col + 2] == grid[row + 3][col + 3] \
                                and grid[row + 3][col + 3] == grid[row + 4][col + 4]:
                        return True
        return False

    def check_for_win_asc_diagonal(self, grid, grid_size):
        """A method to check if there is a ascending diagonal win.

        Args:
            grid (matrix): game board.
            grid_size (int): a size of the game board.

        Returns:
            (boolean): returns True if there is a  ascending diagonal win, else False."""

        for row in range(grid_size):
            for col in range(grid_size):
                if row + 4 < grid_size <= col - 4 and grid[row][col] != 0:
                    if grid[row][col] == grid[row + 1][col - 1] \
                        and grid[row + 1][col - 1] == grid[row + 2][col - 2] \
                            and grid[row + 2][col - 2] == grid[row + 3][col - 3] \
                                and grid[row + 3][col - 3] == grid[row + 4][col - 4]:
                        return True
        return False

    def check_win(self):

        if self.check_for_win_horizontal(self.game_board.grid, self.game_board.grid_size):
            return True
        if self.check_for_win_vertical(self.game_board.grid, self.game_board.grid_size):
            return True
        if self.check_for_win_asc_diagonal(self.game_board.grid, self.game_board.grid_size):
            return True
        if self.check_for_win_desc_diagonal(self.game_board.grid, self.game_board.grid_size):
            return True
        return False

    def restart_game(self):
        pass