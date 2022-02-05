

class HumanPlayer:
    def __init__(self, game_board, game):
        self.game_board = game_board
        self.game = game

    def make_move(self, pos_row, pos_col):
        if self.game.check_for_space(pos_row, pos_col, self.game_board.board):
            self.game.insert_move(1, pos_row, pos_col, self.game_board.board)