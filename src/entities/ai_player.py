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
        return cells

    def minimax(self, board, depth, ai_player, alpha, beta):

        if ai_player:
            best_value = -math.inf
            for cell in self.empty_cells(board):
                row = cell[0]
                col = cell[1]
                board[row][col] = 2
                value = self.minimax(board, depth + 1, False, alpha, beta)
                board[row][col] = 0
                best_value = max(best_value, value)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = math.inf
            for cell in self.empty_cells(board):
                row = cell[0]
                col = cell[1]
                board[row][col] = 1
                value = self.minimax(board, depth + 1, True, alpha, beta)
                board[row][col] = 0
                best_value = min(best_value, value)
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value

    def make_move(self, board):
        max_value = math.inf
        arvo = (0, 0)

        for cell in board:
            row = cell[0]
            col = cell[1]
            if board[row][col] == 0:
                value = self.minimax(board, 0, True, -math.inf, math.inf)
                board[row][col] == 2
                if value < max_value:
                    arvo = (row, col)
        return arvo
