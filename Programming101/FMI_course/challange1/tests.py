import unittest
import solution


class TestPowers(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(solution.powers_of_two_remain([]), False)
        self.assertEqual(solution.powers_of_two_remain([7, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8, 12]), False)
        self.assertEqual(solution.powers_of_two_remain([10, 10]), False)
        self.assertEqual(solution.powers_of_two_remain([10, 10, 10]), True)

    def test_powers_of_two(self):
        self.assertEqual(solution.powers_of_two_remain([4]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8, 16]), True)
        self.assertEqual(solution.powers_of_two_remain([32, 16, 2]), True)

    def test_true(self):
        self.assertEqual(solution.powers_of_two_remain([10, 1, 3, 5, 6]), True)
        self.assertEqual(solution.powers_of_two_remain([6, 12, 24]), True)
        self.assertEqual(solution.powers_of_two_remain([4, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([6, 12, 8]), True)
        self.assertEqual(solution.powers_of_two_remain([10, 12, 6, 2]), True)
        self.assertEqual(solution.powers_of_two_remain([14, 6]), True)
        self.assertEqual(solution.powers_of_two_remain([6, 10, 8, 3, 3]), True)

    def test_false(self):
        self.assertEqual(solution.powers_of_two_remain([10, 12, 6, 10, 12, 6]),
                         False)
        self.assertEqual(solution.powers_of_two_remain([10, 12, 6]), False)
        self.assertEqual(solution.powers_of_two_remain([16, 18, 2]), False)
        self.assertEqual(solution.powers_of_two_remain([14, 6, 8]), False)

if __name__ == '__main__':
    unittest.main()
