class GameBoard:
    def __init__(self,):
        self.board = {1: ' ', 2: ' ', 3: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}

    def print_board(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-----')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-----')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
