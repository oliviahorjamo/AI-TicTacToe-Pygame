
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


    def check_for_tie(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 0:
                    return False
        return True

    def check_for_win(self, board, player):

        for col in range(len(board)):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player and board[3][col] == player and board[4][col] == player :
                return True
        for row in range(len(board)):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player and board[row][3] == player and board[row][4] == player:
                return True

        if board[4][0] == player and board[3][1] == player and board[2][2] == player and board[1][3] == player and board[0][4] == player:
            return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3] == player and board[4][4] == player:
            return True

        return False