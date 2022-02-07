
class Game:

    """A class that represents the game functionalities.

    Attributes:
                self.game_board: An object that imports the game board methods."""

    def __init__(self):
        """A constructor of the class that initializes the game functionalities."""

    def check_for_space(self, row, col, board):
        """A method that checks whether the player can insert letter to the game board.

        Args:
            row (index): row position on the game board.
            col (index): col position on the game board.

        Returns:
            (boolean): returns True if the index of the game board is 0, else False.
        """
        if board[row][col] == 0:
            return True
        return False

    def insert_move(self, player, row, col, board):
        """A method to insert a letter to a given position on the gameboard.

        Args:
            player (str): letter of the player to be inserted.
            position_row (int): a row position to insert the letter.
            position_col (int): a column position to insert the letter.
        """
        board[row][col] = player


    def check_for_win_horizontal(self, board, board_size):
        """A method to check if there is a horizontal win.
        Args:
            board (matrix): game board.
            board_size (int): a size of the game board.
        Returns:
            (boolean): returns True if there is a horizontal win, else False.
        """
        for row in range(board_size):
            for col in range(board_size):
                if 0 <= col < 14 and board[row][col] != 0:
                    if board[row][col] == board[row][col + 1] \
                        and board[row][col + 1] == board[row][col + 2] \
                            and board[row][col + 2] == board[row][col + 3] \
                                and board[row][col + 3] == board[row][col + 4]:
                        return True
                if 19 >= col > 4 and board[row][col] != 0:
                    if board[row][col] == board[row][col - 1] \
                        and board[row][col - 1] == board[row][col - 2] \
                            and board[row][col - 2] == board[row][col - 3] \
                                and board[row][col - 3] == board[row][col - 4]:
                        return True
        return False

    def check_for_win_vertical(self, board, board_size):
        """A method to check if there is a vertical win.
        Args:
            board (matrix): game board.
            board_size (int): a size of the game board.
        Returns:
            (boolean): returns True if there is a vertical win, else False.
        """
        for row in range(board_size):
            for col in range(board_size):
                if col + 4 <= board_size and board[row][col] != 0:
                    if board[row][col] == board[row + 1][col] \
                        and board[row + 1][col] == board[row + 2][col] \
                            and board[row + 2][col] == board[row + 3][col] \
                                and board[row + 3][col] == board[row + 4][col]:
                        return True
        return False

    def check_for_win_desc_diagonal(self, board, board_size):
        """A method to check if there is a descending diagonal win.
        Args:
            board (matrix): game board.
            board_size (int): a size of the game board.
        Returns:
            (boolean): returns True if there is a  descending diagonal win, else False.
        """
        for row in range(board_size):
            for col in range(board_size):
                if row + 4 < board_size and col + 4 < board_size and board[row][col] != 0:
                    if board[row][col] == board[row + 1][col + 1] \
                        and board[row + 1][col + 1] == board[row + 2][col + 2] \
                            and board[row + 2][col + 2] == board[row + 3][col + 3] \
                                and board[row + 3][col + 3] == board[row + 4][col + 4]:
                        return True
        return False

    def check_for_win_asc_diagonal(self, board, board_size):
        """A method to check if there is a ascending diagonal win.
        Args:
            board (matrix): game board.
            board_size (int): a size of the game board.
        Returns:
            (boolean): returns True if there is a ascending diagonal win, else False.
        """

        for row in range(board_size):
            for col in range(board_size):
                if row + 4 < board_size and col - 4 < board_size and board[row][col] != 0:
                    if board[row][col] == board[row + 1][col - 1] \
                        and board[row + 1][col - 1] == board[row + 2][col - 2] \
                            and board[row + 2][col - 2] == board[row + 3][col - 3] \
                                and board[row + 3][col - 3] == board[row + 4][col - 4]:
                        return True
        return False

    def check_for_win(self, board, board_size):
        """A method that checks if a player has won the game.
        Args:
            board (matrix): the game board
            board_size (int): the board size
        Returns:
            [boolean]: returns True if a player has won the game, else False
        """

        if self.check_for_win_horizontal(board, board_size):
            return True
        if self.check_for_win_vertical(board, board_size):
            return True
        #if self.check_for_win_asc_diagonal(board, board_size):
            #return True
        #if self.check_for_win_desc_diagonal(board, board_size):
            #return True
        return False

    def check_for_tie(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    return False
        return True