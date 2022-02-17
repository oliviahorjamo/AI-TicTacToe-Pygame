
class GameLogic:
    def __init__(self):
        self.played_positions = []
        self.strike = 5
        self.grids = 14

    def check_for_space(self, row, col, board):
        if board[row][col] == 0:
            return True
        return False

    def insert_move(self, player, row, col, board):
        board[row][col] = player
        self.played_positions.append((row, col))

    def remove_move(self, row, col, board):
        board[row][col] = 0
        self.played_positions.remove((row, col))

    def check_for_tie(self, board):
        numbers = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != 0:
                    numbers.append([row, col])
        return numbers

    def neighbors(self, latest_row, latest_col):
        possible_neighbors = [(latest_row-1, latest_col-1),
                             (latest_row-1, latest_col),
                             (latest_row-1, latest_col+1),
                             (latest_row, latest_col+1),
                             (latest_row, latest_col-1),
                             (latest_row+1, latest_col-1),
                             (latest_row+1, latest_col),
                             (latest_row+1, latest_col+1)]
        neighbors = []
        for position in possible_neighbors:
            neighbors.append(position)
        return neighbors

    def check_for_horizontal_win(self, row, col, board):
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if col + number > self.grids:
                return False
            if board[row][col + number] != board[row][col]:
                return False
        return True

    def check_for_vertical_win(self, row, col, board):
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if row + number > self.grids:
                return False
            if board[row + number][col] != board[row][col]:
                return False
        return True

    def check_for_desc_diagonal_win(self, row, col, board):
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if row - number < 0 or  col + number > self.grids:
                return False
            if board[row- number][col + number] != board[row][col]:
                return False
        return True

    def check_for_asc_diagonal_win(self, row, col, board):
        if board[row][col] == 0:
            return False
        for number in range(1, self.strike):
            if row + number > self.grids or col + number > self.grids:
                return False
            if board[row + number ][col + number] != board[row][col]:
                return False
        return True

    def check_for_win(self, board):
        for position in self.played_positions:
            row = position[0]
            col = position[1]
            if self.check_for_horizontal_win(row, col, board):
                print('horizontal win')
                return True, board[row][col]
            if self.check_for_vertical_win(row, col, board):
                print('vertical win')
                return True, board[row][col]
            if self.check_for_asc_diagonal_win(row, col, board):
                print('asc')
                return True, board[row][col]
            if self.check_for_desc_diagonal_win(row, col, board):
                print('desc')
                return True, board[row][col]
        return False, None
