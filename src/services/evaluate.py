from services.game_logic import GameLogic


# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/?ref=lbp
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-2-evaluation-function/

class Evaluate:
    def __init__(self):
        self.result = 0
        self.game = GameLogic()
        self.grids = self.game.grids

    def evaluate_horizontal(self, row, col, direction, strike, depth, board):
        result = 0
        score = 1

        if depth == 0 or self.game.strike == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if col + calculation > self.game.grids or col + calculation < 0:
                return 0

            if board[row][col + calculation] == 1:
                result += score * 2
                score += 1
            if board[row][col + calculation] == 2:
                best_value = self.evaluate_horizontal(row, col, -direction,
                                                            (self.game.strike - number),
                                                            depth - 1, board)
                return best_value
            result += 1
        return result

    def evaluate_vertical(self, row, col, direction, strike, depth, board):
        result = 0
        score = 1
        if depth == 0 or self.game.strike == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if row + calculation > self.game.grids or row + calculation < 0:
                return 0
            if board[row + calculation][col] == 1:
                result += score * 2
                score += 1
            if board[row + calculation][col] == 2:
                best_value = self.evaluate_vertical(row, col, -direction,
                                                        (self.game.strike - number),
                                                        (depth - 1), board)
                return best_value
            result += 1
        return result

    def evaluate_asc_diagonal(self, row, col, direction, strike, depth, board):
        result = 0
        score = 1

        if depth == 0 or self.game.strike == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if row + calculation < 0 \
                or row + calculation > self.game.grids \
                    or col + calculation < 0 \
                        or col + calculation > self.game.grids:
                return 0
            if board[row + calculation][col + calculation] == 1:
                result += score * 2
                score += 1
            if board[row + calculation][col + calculation] == 2:
                best_value = self.evaluate_asc_diagonal(row, col, -direction,
                                                            (self.game.strike - number),
                                                            (depth - 1), board)
                return best_value
            result += 1
        return result

    def evaluate_desc_diagonal(self, row, col, direction, strike, depth, board):
        result = 0
        score = 1

        if depth == 0 or self.game.strike == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if row + calculation < 0 \
                or row + calculation > self.game.grids \
                    or col - calculation < 0 \
                        or col - calculation > self.game.grids:
                return 0
            if board[row + calculation][col - calculation] == 1:
                result += score * 2
                score += 1
            if board[row + calculation][col - calculation] == 2:
                best_value = self.evaluate_desc_diagonal(row, col, -direction,
                                                            (self.game.strike - number),
                                                            (depth - 1), board)
                return best_value
            result += 1
        return result

    def evaluate_movement(self, row, col, board):
        result = 0
        direction = 1
        depth = 3
        strike = self.game.strike

        result += self.evaluate_horizontal(row, col, direction, strike, depth, board)
        result += self.evaluate_horizontal(row, col, -direction, strike, depth, board)

        result += self.evaluate_vertical(row, col, direction, strike, depth, board)
        result += self.evaluate_vertical(row, col, -direction, strike, depth, board)

        result += self.evaluate_asc_diagonal(row, col, direction, strike, depth, board)
        result += self.evaluate_asc_diagonal(row, col, -direction, strike, depth, board)

        result += self.evaluate_desc_diagonal(row, col, direction, strike, depth, board)
        result += self.evaluate_desc_diagonal(row, col, -direction, strike, depth, board)

        return result
