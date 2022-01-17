from services.gameboard import GameBoard


class Game:
    def __init__(self):
        self.game_board = GameBoard()

    def check_for_space(self, position_row, position_col):
        if self.game_board.grid[(position_row, position_col)] == ' ':
            return True
        return False

    def check_for_win(self, grid):
        pass

    def insert_letter(self, letter, position_row, position_col):
        if self.check_for_space(position_row, position_col):
            self.game_board.grid[(position_row, position_col)] = letter
        else:
            print('Cannot insert letter in this spot!')
            new_row_position = int(input('Enter new row position for X: '))
            new_col_position = int(input('Enter new column position for X: '))
            self.insert_letter(letter, new_row_position, new_col_position)
            return
        print(self.game_board.print_grid())