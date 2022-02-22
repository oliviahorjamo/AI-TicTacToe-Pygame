from services.game_logic import GameLogic
from services.evaluate import Evaluate

class AiPlayer:
    """A class that represents the minimax algorithm with alpha beta pruning.
    Attributes:
            self.game = an object that brings the game logic to the class
            self.board = the game board
    """
    def __init__(self, game_board, played_position):
        """A constructor of the class that initializes the algorithm.
        Args:
            game_board (object): brings the game_board to the class
            played_position (object): _brings the played positions to the class.
        """
        self.game = GameLogic()
        self.played_positions = played_position.played_positions
        self.game_board = game_board
        self.board = game_board.board
        self.eval = Evaluate()

    def minimax(self, board, depth, alpha, beta, is_maximizing_player, row, col):
        """A method that represents the minimax algorithm with alpha beta pruning.
        Args:
            board (matrix): the game board
            depth (int): _the depth of the minimax algorithm.
            alpha (int): the best value that the maximizer currently
                         can guarantee at that level or above.
            beta (int): the best value that the minimizer currently
                        can guarantee at that level or above.
            is_maximizing_player (boolean): if the player is maximazer.
            row (int): row position
            col (int): row positions
        Returns:
            (int): returns th best value of the current player
        """
        if self.game.check_for_win(board):
            if is_maximizing_player:
                return self.eval.evaluate_movement(row, col, board)
            return -10000

        if self.game.check_for_tie(board) == 0:
            return 0

        if depth == 0:
            return self.eval.evaluate_movement(row, col, board)

        if is_maximizing_player:
            value = -10000

            for pos in reversed(self.played_positions):
                for cell in self.game.neighbors(pos[0], pos[1]):
                    if self.game.check_for_space(cell[0], cell[1], board):
                        self.game.insert_move(2, cell[0], cell[1], board)
                        value = max(value, self.minimax(board, depth - 1,
                                                        alpha, beta, False,
                                                        row, col))
                        self.game.remove_move(cell[0], cell[1], board)
                        alpha = max(alpha, value)
                        if value >= beta:
                            break
            return value - depth

        value = 10000
        for pos in reversed(self.played_positions):
            for cell in self.game.neighbors(pos[0], pos[1]):
                if self.game.check_for_space(cell[0], cell[1], board):
                    self.game.insert_move(1, cell[0], cell[1], board)
                    value = min(value, self.minimax(board, depth - 1,
                                                        alpha, beta, True,
                                                        row, col))
                    self.game.remove_move(cell[0], cell[1], board)
                    beta = min(beta, value)
                    if value <= alpha:
                        break
        return value + depth

    def find_best_move(self):
        """A method that evaluates all the available moves using the minimax() method.
        Returns:
            best_move (tuple): the best move the the maximizer can make.
        """
        best_value = -10000
        best_move = (-1, -1)
        visited = set()
        for pos in reversed(self.played_positions):
            for cell in self.game.neighbors(pos[0], pos[1]):
                if cell in visited:
                    continue
                visited.add(cell)
                if self.game.check_for_space(cell[0], cell[1], self.board):
                    self.game.insert_move(2, cell[0], cell[1], self.board)
                    checked_value = self.minimax(self.board, 3,
                                                -10000, 10000, True,
                                                cell[0], cell[1])
                    self.game.remove_move(cell[0], cell[1], self.board)
                    if checked_value > best_value:
                        best_move = (cell[0], cell[1])
                        best_value = checked_value
        return best_move
