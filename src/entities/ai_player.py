from services.game import Game

class AiPlayer:
    def __init__(self, game_board):
        self.game = Game()
        self.game_board = game_board
        self.board = game_board.board

    def empty_cells(self,board):
        board_size = len(board)
        cells = []
        for i in range(board_size):
            for j in range(board_size) :
                if board[i][j] == 0:
                    cells.append([i, j])
        return cells


    def minimax(self, node, depth, alpha, beta, maximizingPlayer):
        board_size = len(self.board)
        board = self.board

        if self.game.check_for_win(board, 2):
            return 1000
        if self.game.check_for_win(board, 1):
            return -1000
        if len(self.game.check_for_tie(board)) == 0:
            return 0
        if depth == 0:
            return 0

        if maximizingPlayer:
            value = -1000

            for row in range(board_size):
                for col in range(board_size):
                    if board[row][col] == 0:
                        board[row][col] = 2
                        node = (row, col)
                        value = max(value, self.minimax(node, depth - 1, alpha, beta, False))
                        board[row][col] = 0
                        alpha = max(alpha, value)
                        if value >= beta:
                            break
            return value - depth

        else:
            value = 1000
            for row in range(board_size):
                for col in range(board_size):
                    if board[row][col] == 0:
                        node = (row, col)
                        board[row][col] = 1
                        value = min(value, self.minimax(node, depth - 1, alpha, beta, False))
                        board[row][col] = 0
                        beta = min(beta, value)
                        if value <= alpha:
                            break
            return value + depth

    def find_best_move(self, board):
        board_size = len(board)
        best_value = -1000
        best_move = (-1, -1)
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == 0:
                    board[row][col] = 2
                    node = (row, col)
                    checked_value = self.minimax(node, 3, -1000, 1000, False)
                    print(board)
                    print(checked_value)
                    board[row][col] = 0
                    if checked_value >= best_value:
                        best_move = (row, col)
                        best_value = checked_value
        print("The value of the best Move is :", best_value)
        print("ROW:", best_move[0], " COL:", best_move[1])
        return best_move

#if __name__ == '__main__':
 #   board = [
 #       [ 0, 0, 0, 0, 0 ],
  #      [ 0, 0, 0, 0, 0 ],
 #       [ 1, 1, 1, 1, 0 ],
#        [ 0, 0, 0, 2, 1 ],
 #       [ 2, 2, 1, 2, 2 ]
 #   ]