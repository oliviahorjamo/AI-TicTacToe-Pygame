import unittest
from services.game_board import GameBoard
from services.game_logic import Game

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.game_board = GameBoard()
        self.game = Game()

    def test_game_board(self):
        self.assertEqual(self.game_board.board, [[0 for _ in range(self.game_board.board_size)]
                                                for _ in range(self.game_board.board_size)])
    def test_reset_game_board(self):
        self.game.insert_move('X', 0, 0, self.game_board.board)
        self.game.insert_move('X', 0, 1, self.game_board.board)
        self.assertNotEqual(self.game_board.board, [[0 for _ in range(self.game_board.board_size)]
                                                for _ in range(self.game_board.board_size)])
        self.game_board.reset_game_board()
        self.assertNotEqual(self.game_board.board, [[0 for _ in range(self.game_board.board_size)]
                                                for _ in range(self.game_board.board_size)])


    def test_print_board(self):
        self.game_board.print_game_board()
        self.assertEqual(self.game_board.board, [[0 for _ in range(self.game_board.board_size)]
                                                for _ in range(self.game_board.board_size)])