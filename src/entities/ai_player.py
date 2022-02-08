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

        if depth == 0:
            return 0

        if self.game.check_for_win(self.game_board.board, self.game_board.board_size):
            if maximizingPlayer:
                return -math.inf
            return math.inf

        if maximizingPlayer:
            value = -math.inf

            for node in self.game_board.board:
                row = node[0]
                col = node[1]
                if self.game_board.board[row][col] == 0:
                    self.game_board.board[row][col] = 2
                    value = max(value, self.minimax(node, depth - 1, alpha, beta, False))
                    self.game_board.board[row][col] = 0
                    alpha = max(alpha, value)
                    if value >= beta:
                        break
            return value

        else:
            value = math.inf
            for node in self.game_board.board:
                row = node[0]
                col = node[1]
                if self.game_board.board[row][col] == 0:
                    self.game_board.board[row][col] = 1
                    value = min(value, self.minimax(node, depth - 1, alpha, beta, True))
                    self.game_board.board[row][col] = 0
                    beta = min(beta, value)
                    if value <= alpha:
                        break
            return value

    def find_best_move(self):
        best_value = math.inf
        best_move = (0, 0)
        for row in range(len(self.game_board.board)):
            for col in range(len(self.game_board.board)):
                if self.game.check_for_space(row, col, self.game_board.board):
                    self.game.insert_move(2, row, col, self.game_board.board)
                    value = self.minimax(self.game_board.board, 10, -math.inf, math.inf, True)
                    print(self.game_board.print_game_board())
                    self.game.insert_move(0, row, col, self.game_board.board)
                    if value < best_value:
                        best_move = (row, col)
                        best_value = value
        return best_move