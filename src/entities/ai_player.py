import math

class AiPlayer:
    def __init__(self, game_board, game):
        self.game_board = game_board
        self.game = game

    def minimax(self, node, depth, alpha, beta, maximizingPlayer):

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
        for row in range(len(self.game_board.board)):
            for col in range(len(self.game_board.board)):
                node = (row, col)
                if self.game.check_for_space(row, col, self.game_board.board):
                    self.game.insert_move(2, row, col, self.game_board.board)
                    value = self.minimax(node, 3, -math.inf, math.inf, True)
                    self.game.insert_move(0, row, col, self.game_board.board)
                    if value < best_value:
                        best_move = (row, col)
                        best_value = value
        return best_move

