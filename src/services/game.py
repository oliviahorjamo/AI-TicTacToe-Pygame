from services.gameboard import GameBoard


class Game:
    def __init__(self):
        self.game_board = GameBoard()

    def check_for_space(self, position):
        if self.game_board.board[position] == ' ':
            return True
        return False

    def check_for_win(self, board):
        pass

    def insert_letter(self, letter, position):
        if self.check_for_space(position):
            self.game_board.board[position] = letter
        else:
            print('Cannot insert letter in this spot!')
            new_position = int(input('Enter new position for X: '))
            self.insert_letter(letter, new_position)
            return
        print(self.game_board.print_board())
