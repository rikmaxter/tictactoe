import random
import unittest
from main import TicTacToe, neg_symbol 

class TestNegSymbol(unittest.TestCase):
 
    def test_neg_of_x_is_o(self):
        self.assertEqual(neg_symbol("X"), "O")
 
    def test_neg_of_o_is_x(self):
        self.assertEqual(neg_symbol("O"), "X")
 
 
class TestGameLogic(unittest.TestCase):
 
    def test_board_starts_empty(self):
        game = TicTacToe(n=3)
        for i in range(3):
            for j in range(3):
                self.assertEqual(game.get_symbol(i, j), "")

    def test_set_and_get_symbol(self):
        game = TicTacToe(n=3)
        i, j = random.randint(0,2), random.randint(0,2)
        game.set_symbol(i, j, "X")
        self.assertEqual(game.get_symbol(i, j), "X")
    
    def test_check_winner_row(self):
        game = TicTacToe(n=3)
        row = random.randint(0, 2)
        for j in range(3):
            game.set_symbol(row, j, "X")
        self.assertTrue(game.check_winner("X"))
    
    def test_check_winner_col(self):
        game = TicTacToe(n=3)
        col = random.randint(0, 2)
        for i in range(3):
            game.set_symbol(i, col, "O")
        self.assertTrue(game.check_winner("O"))
    
    def test_check_winner_diag(self):
        game = TicTacToe(n=3)
        for i in range(3):
            game.set_symbol(i, i, "X")
        self.assertTrue(game.check_winner("X"))

    def test_check_winner_anti_diag(self):
        game = TicTacToe(n=3)
        for i in range(3):
            game.set_symbol(i, 2-i, "O")
        self.assertTrue(game.check_winner("O"))

    def test_check_winner_false_when_no_line(self):
        game = TicTacToe(n=3)
        game.set_symbol(0, 0, "X")
        game.set_symbol(0, 1, "X")
        self.assertFalse(game.check_winner("X"))

    def test_turns_increment(self):
        game = TicTacToe(n=3)
        game.set_symbol(0, 0, "X")
        game.set_symbol(1, 1, "O")
        self.assertEqual(game.turns, 2)

    def test_is_board_full_false(self):
        game = TicTacToe(n=3)
        game.set_symbol(0, 0, "X")
        self.assertFalse(game.is_board_full())

    def test_is_board_full_true(self):
        game = TicTacToe(n=3)
        for i in range(3):
            for j in range(3):
                game.set_symbol(i, j, "X")
        self.assertTrue(game.is_board_full())

 
if __name__ == "__main__":
    unittest.main()
