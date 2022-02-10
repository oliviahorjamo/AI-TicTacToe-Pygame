import unittest
from services.game import Game
from services.game_board import GameBoard

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game_board = GameBoard()

    def test_check_for_space(self):
        self.assertTrue(self.game.check_for_space(0, 0, self.game_board.board))
        self.game.insert_move('X', 0, 0, self.game_board.board)
        self.assertFalse(self.game.check_for_space(0, 0, self.game_board.board))

