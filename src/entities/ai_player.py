import math


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
                            and board[row + 2][col] == player:
                               # and board[row + 3][col] == player \
                                    #and board[row + 4][col] == player:
                    return True
        return False

    def check_for_win_vertical(self, board, player):
        board_size = len(board)

        for row in range(board_size):
            for col in range(board_size):
                if col + 4 < board_size \
                    and board[row][col] == player \
                        and board[row][col + 1] == player \
                            and board[row][col + 2] == player:
                                #and board[row][col + 3] == player \
                                   # and board[row][col + 4] == player:
                    return True
        return False

    def check_for_win_desc_diagonal(self, board, player):
        board_size = len(board)

        for row in range(board_size):
            for col in range(board_size):
                if row + 4 < board_size and col - 4 >= 0 \
                    and board[row][col] == player \
                        and board[row + 1][col - 1] == player \
                            and board[row + 2][col - 2] == player:
                                #and board[row + 3][col- 3] == player \
                                    #and board[row + 4][col - 4] == player:
                    return True
        return False

    def check_for_win_asc_diagonal(self, board, player):
        """A method to check if there is a ascending diagonal win.
        Args:
            board (matrix): game board.
            board_size (int): a size of the game board.
        Returns:
            (boolean): returns True if there is a ascending diagonal win, else False.
        """

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
        """A method that checks if a player has won the game.
        Args:
            board (matrix): the game board
            board_size (int): the board size
        Returns:
            [boolean]: returns True if a player has won the game, else False
        """

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


class AiPlayer:
    def __init__(self):
        self.ai = 2
        self.human = 1
        self.game = Game()

    def evaluate(self, board):
        if self.game.check_for_win(board, self.ai):
            return 10
        if self.game.check_for_win(board, self.human):
            return -10
        return 0

    def isMovesLeft(self,board):
        board_size = len(board)
        for i in range(board_size):
            for j in range(board_size) :
                if board[i][j] == 0:
                    return True
        return False

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        board_size = len(board)
        score = self.evaluate(board)

        if score == 10: # maximazer has won
            return score
        if score == -10: # minimazer has won
            return score

        if self.isMovesLeft(board) == False: # tie / no moves left
            return 0

        if maximizingPlayer:
            value = -1000

            for row in range(board_size):
                for col in range(board_size):
                    if board[row][col] == 0:
                        board[row][col] = 2
                        value = max(value, self.minimax(board, depth - 1, alpha, beta, False))
                        board[row][col] = 0
                        alpha = max(alpha, value)
                        if value >= beta:
                            break
            return value

        else:
            value = 1000
            for row in range(board_size):
                for col in range(board_size):
                    if board[row][col] == 0:
                        board[row][col] = 1
                        value = min(value, self.minimax(board, depth - 1, alpha, beta, True))
                        board[row][col] = 0
                        beta = min(beta, value)
                        if value <= alpha:
                            break
            return value

    def find_best_move(self, player, board):
        board_size = len(board)
        best_value = -1000
        best_move = (0, 0)
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == 0:
                    board[row][col] = player
                    checked_value = self.minimax(board, 0, -1000, 1000,True)
                    print(board)
                    print(checked_value)
                    board[row][col] = 0

                    if (checked_value >= best_value):
                        best_move = (row, col)
                        best_value = checked_value
        print("The value of the best Move is :", best_value)
        print()
        return best_move

if __name__ == '__main__':
    board = [
        [ 0, 0, 0 ],
        [ 0, 2, 0 ],
        [ 0, 1, 1 ]
    ]
    ai = AiPlayer()

    best_move = ai.find_best_move(2, board)
    print("The Optimal Move is :")
    print("ROW:", best_move[0], " COL:", best_move[1])