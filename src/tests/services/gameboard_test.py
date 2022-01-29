import unittest
from services.game_board import GameBoard
from services.game import Game

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.game_board = GameBoard()
        self.game = Game()

    def test_game_board(self):
        self.assertEqual(self.game_board.grid, [[0 for _ in range(self.game_board.grid_size)]
                                                for _ in range(self.game_board.grid_size)])
    def test_reset_game_board(self):
        self.game.insert_letter('X', 0, 0, self.game_board.grid)
        self.game.insert_letter('X', 0, 1, self.game_board.grid)
        self.assertNotEqual(self.game_board.grid, [[0 for _ in range(self.game_board.grid_size)]
                                                for _ in range(self.game_board.grid_size)])
        self.game_board.reset_game_board()
        self.assertEqual(self.game_board.grid, [[0 for _ in range(self.game_board.grid_size)]
                                                for _ in range(self.game_board.grid_size)])
    def test_print_grid(self):
        self.game_board.print_grid()
        self.assertEqual(self.game_board.grid, [[0 for _ in range(self.game_board.grid_size)]
                                                for _ in range(self.game_board.grid_size)])