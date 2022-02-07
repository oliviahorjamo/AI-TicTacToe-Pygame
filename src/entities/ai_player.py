
class AiPlayer:
    def __init__(self, game_board, game):
        self.game_board = game_board
        self.game = game

    def minimax(self, board, depth, ai_player, alpha, beta):
        if ai_player:
            best_value = -1000
            for cell in board:
                row = cell[0]
                col = cell[1]
                if self.game.check_for_space(row, col, board):
                    self.game.insert_move(2, row, col, board)
                    value = self.minimax(board, depth + 1, False, alpha, beta)
                    self.game.insert_move(0, row, col, board)
                    best_value = max(best_value, value)
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break
            return best_value
        else:
            best_value = 1000
            for cell in board:
                row = cell[0]
                col = cell[1]
                if self.game.check_for_space(row, col, board):
                    self.game.insert_move(1, row, col, board)
                    value = self.minimax(board, depth + 1, True, alpha, beta)
                    self.game.insert_move(0, row, col, board)
                    best_value = min(best_value, value)
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            return best_value

    def make_move(self):
        best_value = 1000
        best_move = (0, 0)
        for row in range(len(self.game_board.board)):
            for col in range(len(self.game_board.board[0])):
                if self.game.check_for_space(row, col, self.game_board.board):
                    self.game.insert_move(2, row, col, self.game_board.board)
                    value = self.minimax(self.game_board.board, 0, True, -1000, 1000)
                    self.game.insert_move(0, row, col, self.game_board.board)
                    if value < best_value:
                        best_move = (row, col)
                        best_value = value
        return best_move


