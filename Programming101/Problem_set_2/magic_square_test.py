import unittest

from magic_square import magic_square, check_rows, check_diagonals, check_columns


class MagicSquare(unittest.TestCase):
    def test_rows(self):
        self.assertEqual(check_rows([[1, 2, 3], [4, 2, 0], [6, 0, 0]]), (True, 6))

    def test_columns(self):
        self.assertEqual(check_columns([[1, 2, 3], [2, 1, 3], [3, 3, 0]]), (True, 6))

    def test_diagonals(self):
        self.assertEqual(check_diagonals([[1, 2, 3], [1, 1, 1], [1, 2, 3]]), (True, 5))

if __name__ == '__main__':
    unittest.main()
