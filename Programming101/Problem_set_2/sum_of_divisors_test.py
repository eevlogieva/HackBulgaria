import unittest

from sum_of_devisiors import sum_of_divisors


class SumDivisorsTest(unittest.TestCase):
    def test_sum_of_divisors_one(self):
        self.assertEqual(sum_of_divisors(1), 1)

    def test_sum_of_divisors_prime(self):
        self.assertEqual(sum_of_divisors(23), 24)

    def test_sum_of_divisors_nonprime(self):
        self.assertEqual(sum_of_divisors(1000), 2340)

    def test_sum_of_divisors_zero(self):
        self.assertEqual(sum_of_divisors(0), 0)

    def test_sum_of_divisors_negative(self):
        self.assertEqual(sum_of_divisors(-7), 0)

if __name__ == '__main__':
    unittest.main()
