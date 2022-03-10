from services.game_logic import GameLogic

class Evaluate:
    """A class that represents the evaluation of the squares in the game.
    """
    def __init__(self):
        """A constructor of the class that initializes the evaluation.
        """
        self.result = 0
        self.game = GameLogic()
        self.grids = self.game.grids

    def evaluate_horizontal(self, row, col, direction, strike, depth, board):
        """A method that evaluates the horizontal positions.

        Args:
            row (int): row in the game board
            col (int_): col in the game board
            direction (int): direction of the evaluation
            strike (int): the sequence
            depth (int): _description_
            board (matrix): _description_

        Returns:
            the result of the horizontal position evaluation.
        """
        result = 0
        score = 1

        if depth == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if col + calculation > self.game.grids or col + calculation < 0:
                return 0

            if board[row][col + calculation] == 1:
                result += score * 1000
                score += 1

            else:
                best_value = self.evaluate_horizontal(row, col, -direction,
                                                            (self.game.strike - number),
                                                            (depth - 1), board)
                return best_value
            result += 1
        return result

    def evaluate_vertical(self, row, col, direction, strike, depth, board):
        result = 0
        score = 1
        if depth == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if row + calculation > self.game.grids or row + calculation < 0:
                return 0
            if board[row + calculation][col] == 1:
                result += score * 1000
                score += 1
            else:
                best_value = self.evaluate_vertical(row, col, -direction,
                                                        (self.game.strike - number),
                                                        (depth - 1), board)
                return best_value
            result += 1
        return result

    def evaluate_asc_diagonal(self, row, col, direction, strike, depth, board):
        result = 0
        score = 1

        if depth == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if row + calculation < 0 \
                or row + calculation > self.game.grids \
                    or col + calculation < 0 \
                        or col + calculation > self.game.grids:
                return 0
            if board[row + calculation][col + calculation] == 1:
                result += score * 1000
                score += 1
            else:
                best_value = self.evaluate_asc_diagonal(row, col, -direction,
                                                            (self.game.strike - number),
                                                            (depth - 1), board)
                return best_value
            result += 1
        return result

    def evaluate_desc_diagonal(self, row, col, direction, strike, depth, board):
        result = 0
        score = 1

        if depth == 0:
            return 0

        for number in range(1, strike):
            calculation = direction * number
            if row + calculation < 0 \
                or row + calculation > self.game.grids \
                    or col - calculation < 0 \
                        or col - calculation > self.game.grids:
                return 0
            if board[row + calculation][col - calculation] == 1:
                result += score * 1000
                score += 1
            else:
                best_value = self.evaluate_desc_diagonal(row, col, -direction,
                                                            (self.game.strike - number),
                                                            (depth - 1), board)
                return best_value
            result += 1
        return result

    def evaluate_movement(self, row, col, board):
        result = 0
        direction = 1
        depth = 2
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
