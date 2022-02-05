import unittest
from services.game import Game
from services.game_board import GameBoard
from entities.human_player import HumanPlayer

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game_board = GameBoard()
        self.human_player = HumanPlayer(self.game_board, self.game)

    def test_make_move(self):
        self.game.check_for_space(2, 2, self.game_board.board)
        self.assertEqual(self.human_player.make_move(2, 2), self.game.insert_move(1, 2, 2, self.game_board.board))
        self.game.insert_move(1, 1, 1, self.game_board.board)
        self.assertEqual(self.human_player.make_move(1, 1), None)