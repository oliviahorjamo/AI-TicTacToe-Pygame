import unittest
from services.game_board import GameBoard
from services.game_logic import GameLogic
from entities.ai_player import AiPlayer


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        self.played_positions = []
        self.board = GameBoard()
        self.ai = AiPlayer(self.board, self.game)

    def test_find_best_move_1(self):
        self.game.insert_move(1, 0, 0, self.board.board)
        self.played_positions.append([0, 0])
        self.game.insert_move(2, 0, 1, self.board.board)
        self.played_positions.append([0, 1])
        self.assertEqual(self.ai.find_best_move(), (1, 2))
        self.game.insert_move(1, 1, 2, self.board.board)
        self.assertEqual(self.ai.find_best_move(), (1, 1))
        self.game.insert_move(2, 1, 1, self.board.board)
        self.assertEqual(self.ai.find_best_move(), (2, 2))
    
    def test_find_best_move_2(self):
        self.game.insert_move(1, 0, 0, self.board.board)
        self.played_positions.append([0, 0])
        self.game.insert_move(2, 1, 0, self.board.board)
        self.played_positions.append([0, 1])
        self.assertEqual(self.ai.find_best_move(), (2, 1))
        self.game.insert_move(1, 1, 1, self.board.board)
        self.assertEqual(self.ai.find_best_move(), (2, 1))
        self.game.insert_move(2, 3, 1, self.board.board)
        self.assertEqual(self.ai.find_best_move(), (4, 2))

    def test_tie(self):
        board = [[1 for _ in range(25)]
                      for _ in range(25)]
        self.assertEqual(self.ai.minimax(board, 3, -10000, 10000, True, 0, 0), 0)
