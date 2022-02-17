from services.game_logic import GameLogic

class AiPlayer:
    def __init__(self, game_board, played_position):
        self.game = GameLogic()
        self.played_positions = played_position.played_positions
        self.game_board = game_board
        self.board = game_board.board

    def minimax(self, board, depth, alpha, beta, maximizingPlayer, row, col):
        if self.game.check_for_win(board)[0]:
            if self.game.check_for_win(board)[1] == 2:
                return 10000
            return -10000
        if len(self.game.check_for_tie(board)) == 0:
            return 0
        if depth == 0:
            return 0

        if maximizingPlayer:
            value = -10000

            for pos in self.played_positions:
                for cell in self.game.neighbors(pos[0], pos[1]):
                    if self.game.check_for_space(cell[0], cell[1], board):
                        self.game.insert_move(2, cell[0], cell[1], board)
                        value = max(value, self.minimax(board, depth - 1, alpha, beta, False, row, col))
                        self.game.remove_move(cell[0], cell[1], board)
                        alpha = max(alpha, value)
                        if value >= beta:
                            break
            return value - depth

        else:
            value = 10000
            for pos in self.played_positions:
                for cell in self.game.neighbors(pos[0], pos[1]):
                    if self.game.check_for_space(cell[0], cell[1], board):
                        self.game.insert_move(1, cell[0], cell[1], board)
                        value = min(value, self.minimax(board, depth - 1, alpha, beta, False, row, col))
                        self.game.remove_move(cell[0], cell[1], board)
                        beta = min(beta, value)
                        if value <= alpha:
                            break
            return value + depth

    def find_best_move(self):
        board = self.board
        best_value = -10000
        best_move = (-1, -1)
        for pos in self.played_positions:
            for cell in self.game.neighbors(pos[0], pos[1]):
                if self.game.check_for_space(cell[0], cell[1], board):
                    self.game.insert_move(2, cell[0], cell[1], board)
                    checked_value = self.minimax(board, 3, -10000, 10000, False, cell[0], cell[1])
                    print(self.game_board.print_game_board())
                    print(checked_value)
                    self.game.remove_move(cell[0], cell[1], board)
                    if checked_value >= best_value:
                        best_move = (cell[0], cell[1])
                        best_value = checked_value
        return best_move