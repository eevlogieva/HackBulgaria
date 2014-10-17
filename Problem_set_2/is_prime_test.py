import unittest

from is_prime import is_prime


class isPrimeTest(unittest.TestCase):
    def test_is_prime_prime(self):
        self.assertTrue(is_prime(23))

    def test_is_prime_nonprime(self):
        self.assertFalse(is_prime(49))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()
