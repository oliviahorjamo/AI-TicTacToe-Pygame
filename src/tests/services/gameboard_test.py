import unittest
from services.game_board import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.gameboard = GameBoard()

    def test_gameboard(self):
        self.assertEqual(self.gameboard.grid, [[0 for _ in range(self.gameboard.grid_size)]
                                                for _ in range(self.gameboard.grid_size)])