import math

class AiPlayer:
    def __init__(self, game_board, game):
        self.game_board = game_board
        self.game = game

    def minimax(self, node, depth, alpha, beta, maximizingPlayer):

        """Pseudocode: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
        function alphabeta(node, depth, α, β, maximizingPlayer) is
            if depth = 0 or node is a terminal node then
                return the heuristic value of node
            if maximizingPlayer then
                value := −∞
                for each child of node do
                    value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
                    α := max(α, value)
                    if value ≥ β then
                        break (* β cutoff *)
                return value
            else
                value := +∞
                for each child of node do
                    value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
                    β := min(β, value)
                    if value ≤ α then
                        break (* α cutoff *)
                return value

        (* Initial call *)
        alphabeta(origin, depth, −∞, +∞, TRUE)
        """

        if depth == 0 or self.game.check_for_win(self.game_board.board, self.game_board.board_size):
            return 0

        if maximizingPlayer:
            value = -math.inf

            for node in self.game_board.board:
                if self.game.check_for_space(node[0], node[1], self.game_board.board):
                    self.game.insert_move(2, node[0], node[1], self.game_board.board)
                    value = max(value, self.minimax(node, depth - 1, alpha, beta, False))
                    self.game.insert_move(0, node[0], node[1], self.game_board.board)
                    alpha = max(alpha, value)
                    if value >= beta:
                        break
            return value

        else:
            value = math.inf
            for node in self.game_board.board:
                if self.game.check_for_space(node[0], node[1], self.game_board.board):
                    self.game.insert_move(1, node[0], node[1], self.game_board.board)
                    value = min(value, self.minimax(node, depth - 1, alpha, beta, True))
                    self.game.insert_move(0, node[0], node[1], self.game_board.board)
                    alpha = max(alpha, value)
                    if value <= alpha:
                        break
                    beta = min(beta, value)
            return value

    def find_best_move(self):
        best_value = math.inf
        best_move = (0, 0)
        for row in range(self.game_board.board_size):
            for col in range(self.game_board.board_size):
                node = (row, col)
                if self.game.check_for_space(row, col, self.game_board.board):
                    self.game.insert_move(2, row, col, self.game_board.board)
                    value = self.minimax(node, 0, -math.inf, math.inf, True)
                    self.game.insert_move(0, row, col, self.game_board.board)
                    if value < best_value:
                        best_move = (row, col)
                        best_value = value
        return best_move