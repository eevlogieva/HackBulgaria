import unittest

from fibonacci_lists import nth_fib_lists


class FibListsTests(unittest.TestCase):
    def test_fib_list_for_n_1(self):
        self.assertEqual(nth_fib_lists([2, 3, 4], [1, 2], 1), [2, 3, 4])

    def test_fib_list_for_n_2(self):
        self.assertEqual(nth_fib_lists([2, 3, 5], [1], 2), [1])

    def test_fib_list_n_greater_than_2(self):
        self.assertEqual(nth_fib_lists([3, 4], [1, 2, 3], 3), [3, 4, 1, 2, 3])

    def test_fib_list_empty_list(self):
        self. assertEqual(nth_fib_lists([], [], 35), [])

if __name__ == '__main__':
    unittest.main()
