import math

class AiPlayer:
    def __init__(self, game):
        self.game = game

    def empty_cells(self, board):
        cells = []
        for cell in board:
            row = cell[0]
            col = cell[1]
            if board[row][col] == 0:
                cells.append([row, col])
            else:
                continue
        return cells

    def min_alpha_beta(self, board, depth, alpha, beta):
        best_value = math.inf
        for cell in self.empty_cells(board):
            row = cell[0]
            col = cell[1]
            board[row][col] = 1
            value = self.max_alpha_beta(board, depth + 1, alpha, beta)
            board[row][col] = 0
            best_value = min(best_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_value

    def max_alpha_beta(self, board, depth, alpha, beta):
        best_value = -math.inf
        for cell in self.empty_cells(board):
            row = cell[0]
            col = cell[1]
            board[row][col] = 2
            value = self.min_alpha_beta(board, depth + 1, alpha, beta)
            board[row][col] = 0
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value

    def minimax(self, board, ai_player, depth, alpha, beta):
        if ai_player:
            return self.max_alpha_beta(board, depth, alpha, beta)
        return self.min_alpha_beta(board, depth, alpha, beta)

    def make_move(self, board):
        best_value = math.inf
        coordinates = (0, 0)
        for cell in self.empty_cells(board):
            row = cell[0]
            col = cell[1]
            if board[row][col] == 0:
                value = self.minimax(board, False, 0, -math.inf, math.inf)
                board[row][col] == 2
                if value <= best_value:
                    coordinates = (row, col)
        return coordinates
