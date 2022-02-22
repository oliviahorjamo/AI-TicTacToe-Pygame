import unittest
from services.game_logic import GameLogic
from services.game_board import GameBoard


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        self.game_board = GameBoard()
        self.board = self.game_board.board
        self.board_size = self.game_board.board_size

    def test_check_for_space(self):
        self.assertTrue(self.game.check_for_space(0, 0, self.board))
        self.game.insert_move('X', 0, 0, self.game_board.board)
        self.assertFalse(self.game.check_for_space(0, 0, self.board))

    def test_check_for_horizontal_win(self):
        self.game.insert_move(0, 0, 0, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 0, 0, self.board)
        self.game.insert_move('X', 0, 24, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 0, 1, self.board)
        self.game.insert_move('X', 0, 2, self.board)
        self.game.insert_move('X', 0, 3, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 0, 4, self.board)
        self.assertEqual(self.game.check_for_win(self.board), True)

    def test_check_for_vertical_win(self):
        self.game.insert_move(0, 0, 0, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 0, 0, self.board)
        self.game.insert_move('X', 24, 24, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 1, 0, self.board)
        self.game.insert_move('X', 2, 0, self.board)
        self.game.insert_move('X', 3, 0, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 4, 0, self.board)
        self.assertEqual(self.game.check_for_win(self.board), True, 'X')

    def test_check_for_desc_diagonal_win(self):
        self.game.insert_move(0, 0, 0, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 0, 0, self.board)
        self.game.insert_move('X', 14, 0, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 1, 1, self.board)
        self.game.insert_move('X', 2, 2, self.board)
        self.game.insert_move('X', 3, 3, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 4, 4, self.board)
        self.assertEqual(self.game.check_for_win(self.board), True)

    def test_check_for_asc_diagonal_win(self):
        self.game.insert_move(0, 0, 0, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 6, 0, self.board)
        self.game.insert_move('X', 24, 24, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.insert_move('X', 5, 1, self.board)
        self.game.insert_move('X', 4, 2, self.board)
        self.game.insert_move('X', 3, 3, self.board)
        self.assertEqual(self.game.check_for_win(self.board), False)
        self.game.remove_move(3, 3, self.board)
        self.game.insert_move('X', 2, 4, self.board)
        self.game.insert_move('X', 3, 3, self.board)
        self.assertEqual(self.game.check_for_win(self.board), True)

    def test_empty_spaces_and_tie(self):
        self.board = [[0 for _ in range(self.board_size)]
                      for _ in range(self.board_size)]
        self.assertEqual(self.game.check_for_tie(self.board), 625)
        self.board = [[1 for _ in range(self.board_size)]
                      for _ in range(self.board_size)]
        self.assertEqual(self.game.check_for_tie(self.board), 0)

    def test_neighbors(self):
        n = [(4, 4), (4, 5), (4, 6), (5, 6), (5, 4), (6, 4), (6, 5), (6, 6)]
        self.assertEqual(self.game.neighbors(5, 5), n)
        n = []
        self.assertEqual(self.game.neighbors(30, -1), n)
