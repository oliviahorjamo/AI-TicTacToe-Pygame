import unittest
import sys
from services.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.grid_size = 15
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def test_insert_letter_and_check_for_space(self):
        self.game.insert_letter('X', 0, 0)
        self.assertEqual(self.game.check_for_space(0, 0), False)
        self.assertEqual(self.game.check_for_space(0, 1), True)
  
     
    def test_check_for_win_horizontal(self):
        self.assertFalse(self.game.check_for_win_horizontal(self.grid, self.grid_size))
        self.game.insert_letter('X', 0, 1)
        self.game.insert_letter('X', 0, 2)
        self.game.insert_letter('X', 0, 3)
        self.game.insert_letter('X', 0, 4)
        self.assertFalse(self.game.check_for_win_horizontal(self.grid, self.grid_size))
        self.game.insert_letter('X', 0, 5)
        # self.assertTrue(self.game.check_for_win_horizontal(self.grid, self.grid_size))


    def test_check_for_win_vertical(self):
        self.assertFalse(self.game.check_for_win_vertical(self.grid, self.grid_size))
        
    def test_check_for_win_diagonal(self):
        self.assertFalse(self.game.check_for_win_diagonal(self.grid, self.grid_size))
        
