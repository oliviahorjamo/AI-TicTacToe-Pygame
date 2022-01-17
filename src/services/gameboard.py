class GameBoard:
    def __init__(self):
        self.grid = {}
        self.grid_size = 25

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.grid[(row, col)] = ' '

    def print_grid(self):
        print()
        print('--' * self.grid_size + '-')
        for row in range(self.grid_size):
            print('|' + '|'.join(self.grid[(row, col)] for col in range(self.grid_size)) + '|')
            print('--' * self.grid_size + '-')
