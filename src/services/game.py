class Game:

    """A class that represents the game functionalities.

    Attributes:
                game_board: An object that imports the game board methods."""

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


    def check_for_win_horizontal(self, board, player):
        board_size = len(board)

        for row in range(board_size):
            for col in range(board_size):
                if row + 4 < board_size \
                    and board[row][col] == player \
                        and board[row + 1][col] == player \
                            and board[row + 2][col] == player \
                               and board[row + 3][col] == player \
                                    and board[row + 4][col] == player:
                    return True
        return False

    def check_for_win_vertical(self, board, player):
        board_size = len(board)

        for row in range(board_size):
            for col in range(board_size):
                if col + 4 < board_size \
                    and board[row][col] == player \
                        and board[row][col + 1] == player \
                            and board[row][col + 2] == player \
                                and board[row][col + 3] == player \
                                    and board[row][col + 4] == player:
                    return True
        return False

    def check_for_win_desc_diagonal(self, board, player):
        board_size = len(board)

        for row in range(board_size):
            for col in range(board_size):
                if row + 4 < board_size and col - 4 >= 0 \
                    and board[row][col] == player \
                        and board[row + 1][col - 1] == player \
                            and board[row + 2][col - 2] == player \
                                and board[row + 3][col- 3] == player \
                                    and board[row + 4][col - 4] == player:
                    return True
        return False

    def check_for_win_asc_diagonal(self, board, player):
        board_size = len(board)

        for row in range(board_size):
            for col in range(board_size):
                if row + 4 < board_size and col + 4 < board_size \
                    and board[row][col] == player \
                        and board[row + 1][col + 1] == player \
                            and board[row + 2][col + 2] == player \
                                and board[row + 3][col + 3] == player \
                                    and board[row + 4][col + 4] == player:
                    return True
        return False

    def check_for_win(self, board, player):
        if self.check_for_win_horizontal(board, player):
            return True
        if self.check_for_win_vertical(board, player):
            return True
        if self.check_for_win_asc_diagonal(board, player):
            return True
        if self.check_for_win_desc_diagonal(board, player):
            return True
        return False

    def check_for_tie(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 0:
                    return False
        return True
