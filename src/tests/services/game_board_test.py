import unittest
from services.game_board import GameBoard
from services.game_logic import GameLogic


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.game_board = GameBoard()
        self.game = GameLogic()

    def test_game_board(self):
        self.assertEqual(self.game_board.board, [[0 for _ in range(self.game_board.board_size)]
                                                 for _ in range(self.game_board.board_size)])
