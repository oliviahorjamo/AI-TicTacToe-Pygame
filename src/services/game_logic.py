
class GameLogic:
    """A class that represents the game logics.

    Attributes:
            self.played_positions (list): keeps track of the cells
                                            where a player has inserted
                                            a move.
            self.strike (int): defines the amount of O's or X's has to be in strike position.
            self.grids (int) = amount of grids helps with the winning checks.
    """
    def __init__(self):
        """A constructor of the class that initializes the game logics."""
        self.played_positions = []
        self.strike = 5
        self.grids = 14

    def check_for_space(self, row, col, board):
        """a method that checks if a player can insert a move into the game board.

        Args:
            row (int): a row number
            col (int): a column number
            board (matrix): game board

        Returns:
            True (boolean): if the cell is free,
            False (boolean): if the cell is not free.
        """
        if board[row][col] == 0:
            return True
        return False

    def insert_move(self, player, row, col, board):
        """A method that inserts a move into the game board and played_positions list.
        Args:
            player (int): player value
            row (int): a row number
            col (int): a column number
            board (matrix): game board
        """
        board[row][col] = player
        self.played_positions.append((row, col))

    def remove_move(self, row, col, board):
        """A method that removes a move from the played_positions list.
        Args:
            row (int): a row number
            col (int): a column number
            board (matrix): the game board
        """
        board[row][col] = 0
        self.played_positions.remove((row, col))

    def empty_spaces(self, board):
        """a method that checks if there are no moves left in the game board.

        Args:
            board (matrix): the game board

        Returns:
            numbers (list): a list of the unplayed cells.
        """
        numbers = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 0:
                    numbers.append([row, col])
        return numbers

    def check_for_tie(self, board):
        """A method that checks if there is a tie in the game.

        Args:
            board (matrix): the game board

        Returns:
            True (boolean): if there is a tie in the game.
            False (boolean): if there is no tie in the game.
        """
        if len(self.empty_spaces(board)) == 0:
            return True
        return False

    def neighbors(self, latest_row, latest_col):
        """A method that checks the neighbors of a played position.

        Args:
            latest_row (int): previously inserted row position
            latest_col (int): previously inserted column position.

        Returns:
            neighbors (list): a list of all the neighbors.
        """
        possible_neighbors = [(latest_row-1, latest_col-1),
                             (latest_row-1, latest_col),
                             (latest_row-1, latest_col+1),
                             (latest_row, latest_col+1),
                             (latest_row, latest_col-1),
                             (latest_row+1, latest_col-1),
                             (latest_row+1, latest_col),
                             (latest_row+1, latest_col+1)]
        neighbors = []
        for position in possible_neighbors:
            neighbors.append(position)
        return neighbors

    def check_for_horizontal_win(self, row, col, board):
        """A method that checks if there is a horizontal win.

        Args:
            row (int): a row position
            col (int): a column position
            board (matrix): the game board.

        Returns:
            True (boolean): if there is a horizontal win.
            False (boolean): if there is no horizontal win.
        """
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if col + number > self.grids:
                return False
            if board[row][col + number] != board[row][col]:
                return False
        return True

    def check_for_vertical_win(self, row, col, board):
        """A method that checks if there is a vertical win.

        Args:
            row (int): a row position
            col (int): a column position
            board (matrix): the game board.

        Returns:
            True (boolean): if there is a vertical win.
            False (boolean): if there is no vertical win.
        """
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if row + number > self.grids:
                return False
            if board[row + number][col] != board[row][col]:
                return False
        return True

    def check_for_asc_diagonal_win(self, row, col, board):
        """A method that checks if there is a descending diagonal win.

        Args:
            row (int): a row position
            col (int): a column position
            board (matrix): the game board.

        Returns:
            True (boolean): if there is an ascending diagonal win.
            False (boolean): if there is no ascending diagonal win.
        """
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if row - number < 0 or  col + number > self.grids:
                return False
            if board[row- number][col + number] != board[row][col]:
                return False
        return True

    def check_for_desc_diagonal_win(self, row, col, board):
        """A method that checks if there is an descending diagonal win.

        Args:
            row (int): a row position
            col (int): a column position
            board (matrix): the game board.

        Returns:
            True (boolean): if there is a descending diagonal win.
            False (boolean): if there is no descending diagonal win.
        """
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if row + number > self.grids or col + number > self.grids:
                return False
            if board[row + number ][col + number] != board[row][col]:
                return False
        return True

    def check_for_win(self, board):
        """A method that checks if there is a win.

        Args:
            board (matrix): the game board.

        Returns:
            True (boolean): if there is a win.
            False (boolean): if there is no win.
        """
        for position in self.played_positions:
            row = position[0]
            col = position[1]
            if self.check_for_horizontal_win(row, col, board):
                return True, board[row][col]
            if self.check_for_vertical_win(row, col, board):
                return True, board[row][col]
            if self.check_for_asc_diagonal_win(row, col, board):
                return True, board[row][col]
            if self.check_for_desc_diagonal_win(row, col, board):
                return True, board[row][col]
        return False, None
