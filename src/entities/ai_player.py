from services.game import Game

class AiPlayer:
    def __init__(self):
        self.game = Game()

    def evaluate(self, board):
        if self.game.check_win(board, 2):
            return 100
        if self.game.check_win(board, 1):
            return -100
        if self.game.check_for_tie(board):
            return 1
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
            return 100
        if score == -10: # minimazer has won
            return -100
        if depth == 0:
            return self.evaluate(board)

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

    def find_best_move(self, board):
        board_size = len(board)
        best_value = -1000
        best_move = (0, 0)
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == 0:
                    board[row][col] = 2
                    checked_value = self.minimax(board, 5, -1000, 1000, True)
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