import unittest

from goldbach_conjecture import goldbach


class GoldbachTest(unittest.TestCase):
    def test_goldback_small_number(self):
        self.assertEqual(goldbach(6), [(3, 3)])

    def test_goldbach_big_number(self):
        self.assertEqual(goldbach(100), [(3, 97), (11, 89), (17, 83),
                                 (29, 71), (41, 59), (47, 53)])

if __name__ == '__main__':
    unittest.main()
