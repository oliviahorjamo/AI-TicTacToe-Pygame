import unittest
from services.game_board import GameBoard
from services.game_logic import GameLogic
from entities.ai_player import AiPlayer


class TestAiPlayer(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        self.played_positions = []
        self.board = GameBoard()
        self.ai = AiPlayer(self.board, self.game)

    def test_find_best_move_1(self):
        self.game.insert_move(1, 6, 1, self.board.board)
        self.played_positions.append([6, 1])
        self.assertEqual(self.ai.find_best_move()[0], (5, 0))
        self.game.insert_move(2, 5, 0, self.board.board)
        self.played_positions.append([5, 0])
        self.game.insert_move(1, 7, 1, self.board.board)
        self.played_positions.append([7, 1])
        self.assertEqual(self.ai.find_best_move()[0], (5, 1))
        self.game.insert_move(2, 5, 1, self.board.board)
        self.played_positions.append([5, 1])
        self.game.insert_move(1, 8, 1, self.board.board)
        self.played_positions.append([8, 1])
        self.assertEqual(self.ai.find_best_move()[0], (9, 1))
        self.game.insert_move(2, 9, 1, self.board.board)
        self.played_positions.append([9, 1])

    def test_find_best_move_2(self):
        self.game.insert_move(1, 2, 2, self.board.board)
        self.played_positions.append([2, 2])
        self.assertEqual(self.ai.find_best_move()[0], (1, 1))
        self.game.insert_move(2, 1, 1, self.board.board)
        self.played_positions.append([1, 1])
        self.game.insert_move(1, 3, 3, self.board.board)
        self.played_positions.append([3, 2])
        self.assertEqual(self.ai.find_best_move()[0], (1, 2))
        self.game.insert_move(2, 1, 2, self.board.board)
        self.played_positions.append([1, 2])
        self.game.insert_move(1, 4, 4, self.board.board)
        self.played_positions.append([4, 3])
        self.assertEqual(self.ai.find_best_move()[0], (5, 5))

    def test_find_best_move_3(self):
        self.game.insert_move(1, 1, 6, self.board.board)
        self.played_positions.append([1, 6])
        self.assertEqual(self.ai.find_best_move()[0], (0, 5))
        self.game.insert_move(2, 0, 5, self.board.board)
        self.played_positions.append([0, 5])
        self.game.insert_move(1, 1, 7, self.board.board)
        self.played_positions.append([1, 7])
        self.assertEqual(self.ai.find_best_move()[0], (0, 6))
        self.game.insert_move(2, 0, 6, self.board.board)
        self.played_positions.append([0, 6])
        self.game.insert_move(1, 1, 8, self.board.board)
        self.played_positions.append([1, 8])
        self.assertEqual(self.ai.find_best_move()[0], (1, 5))
        self.game.insert_move(2, 1, 5, self.board.board)
        self.played_positions.append([1, 5])

    def test_find_best_move_4(self):
        self.game.insert_move(1, 10, 9, self.board.board)
        self.played_positions.append([10, 10])
        self.assertEqual(self.ai.find_best_move()[0], (9, 8))
        self.game.insert_move(2, 9, 8, self.board.board)
        self.played_positions.append([9, 8])
        self.game.insert_move(1, 11, 8, self.board.board)
        self.played_positions.append([11, 8])
        self.assertEqual(self.ai.find_best_move()[0], (9, 9))
        self.game.insert_move(2, 9, 9, self.board.board)
        self.played_positions.append([9, 9])
        self.game.insert_move(1, 12, 7, self.board.board)
        self.played_positions.append([12, 7])
        self.assertEqual(self.ai.find_best_move()[0], (9, 10))
        self.game.insert_move(2, 9, 10, self.board.board)
        self.played_positions.append([9, 10])
        self.game.insert_move(1, 13, 8, self.board.board)
        self.played_positions.append([13, 8])
        self.assertEqual(self.ai.find_best_move()[0], (13, 6))


    def test_tie(self):
        board = [[1 for _ in range(25)]
                      for _ in range(25)]
        self.assertEqual(self.ai.minimax(board, 3, -10000, 10000, True, 0, 0), 0)

    def test_win(self):
        self.game.insert_move(2, 7, 8, self.board.board)
        self.game.insert_move(2, 6, 8, self.board.board)
        self.game.insert_move(2, 5, 8, self.board.board)
        self.game.insert_move(2, 4, 8, self.board.board)
        self.game.insert_move(2, 3, 8, self.board.board)
        self.assertEqual(self.ai.find_best_move()[0], (2, 8))
        self.assertEqual(self.ai.find_best_move(), ((2, 8), 100000))
