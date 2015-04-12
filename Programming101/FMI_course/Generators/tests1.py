import unittest
from itertools import islice
from itertools import cycle
from math import factorial
import solution


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        fibonacci = solution.fibonacci()
        first_five = list(islice(fibonacci, 5))
        self.assertEqual(first_five, [1, 1, 2, 3, 5])
        self.assertTrue(hasattr(fibonacci, '__iter__'))
        self.assertTrue(hasattr(fibonacci, '__next__'))
        self.assertFalse(hasattr(fibonacci, '__getitem__'))
        self.assertFalse(hasattr(fibonacci, '__len__'))

    def test_fibonacci_ten(self):
        fibonacci = solution.fibonacci()
        first_ten = list(islice(fibonacci, 10))
        result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(first_ten, result)

    def test_fibonacci_twenty(self):
        fibonacci = solution.fibonacci()
        first_twenty = list(islice(fibonacci, 20))
        result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                  610, 987, 1597, 2584, 4181, 6765]
        self.assertEqual(first_twenty, result)


class TestPrimes(unittest.TestCase):

    def test_primes(self):
        primes = solution.primes()
        first_five = list(islice(primes, 5))
        self.assertEqual(first_five, [2, 3, 5, 7, 11])
        self.assertTrue(hasattr(primes, '__iter__'))
        self.assertTrue(hasattr(primes, '__next__'))
        self.assertFalse(hasattr(primes, '__getitem__'))
        self.assertFalse(hasattr(primes, '__len__'))

    def test_primes_ten(self):
        primes = solution.primes()
        first_ten = list(islice(primes, 10))
        result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(first_ten, result)


class TestAlphabet(unittest.TestCase):

    def test_alphabet(self):
        alphabet = solution.alphabet(code='lat')
        first_five = list(islice(alphabet, 5))
        self.assertEqual(first_five, ['a', 'b', 'c', 'd', 'e'])
        self.assertTrue(hasattr(alphabet, '__iter__'))
        self.assertTrue(hasattr(alphabet, '__next__'))
        self.assertFalse(hasattr(alphabet, '__getitem__'))
        self.assertFalse(hasattr(alphabet, '__len__'))

    def test_bg_alphabet(self):
        alphabet = solution.alphabet(code='bg')
        all_bg_letters = list('абвгдежзийклмнопрстуфхцчшщъьюя')
        solution_letters = list(alphabet)
        self.assertEqual(all_bg_letters, solution_letters)
        self.assertTrue(hasattr(alphabet, '__iter__'))
        self.assertTrue(hasattr(alphabet, '__next__'))
        self.assertFalse(hasattr(alphabet, '__getitem__'))
        self.assertFalse(hasattr(alphabet, '__len__'))

    def test_letters_argument(self):
        input_letters = '蜙跣鉌鳭蟷蠉蟼踸躽輷輴郺暲釂鱞鸄緀綡蒚曋橪'
        result = list(input_letters[:5])
        alphabet = solution.alphabet(letters=input_letters)
        first_five = list(islice(alphabet, 5))
        self.assertEqual(first_five, result)
        self.assertTrue(hasattr(alphabet, '__iter__'))
        self.assertTrue(hasattr(alphabet, '__next__'))
        self.assertFalse(hasattr(alphabet, '__getitem__'))
        self.assertFalse(hasattr(alphabet, '__len__'))


class TestIntertwine(unittest.TestCase):

    def test_with_empty_arguments(self):
        generator = solution.intertwined_sequences(())
        self.assertTrue(hasattr(generator, '__iter__'))
        self.assertTrue(hasattr(generator, '__next__'))
        self.assertFalse(hasattr(generator, '__getitem__'))
        self.assertFalse(hasattr(generator, '__len__'))
        self.assertEqual([], list(generator))

    def test_intertwine(self):
        fibonacci_3_prime_3_bg_3 = solution.intertwined_sequences([
            {'sequence': 'fibonacci', 'length': 3},
            {'sequence': 'primes', 'length': 3},
            {'sequence': 'alphabet', 'code': 'bg', 'length': 3}
        ])

        self.assertEqual(
            list(fibonacci_3_prime_3_bg_3),
            [1, 1, 2, 2, 3, 5, 'а', 'б', 'в']
        )

    def test_all_same(self):
        fibonacci_3_times = solution.intertwined_sequences([
            {'sequence': 'fibonacci', 'length': 3},
            {'sequence': 'fibonacci', 'length': 3},
            {'sequence': 'fibonacci', 'length': 4}])

        result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertTrue(hasattr(fibonacci_3_times, '__iter__'))
        self.assertTrue(hasattr(fibonacci_3_times, '__next__'))
        self.assertFalse(hasattr(fibonacci_3_times, '__getitem__'))
        self.assertFalse(hasattr(fibonacci_3_times, '__len__'))

        solution_result = list(fibonacci_3_times)
        self.assertEqual(solution_result, result)

    def test_alphabet_3_times_with_diff_args(self):
        chinese_letters = '蜙跣鉌鳭蟷蠉蟼踸躽輷輴郺暲釂鱞鸄緀綡蒚曋橪'
        alphabet_3_times_diff_args = solution.intertwined_sequences([
            {'sequence': 'alphabet', 'code': 'bg', 'length': 3},
            {'sequence': 'alphabet', 'letters': chinese_letters, 'length': 3},
            {'sequence': 'alphabet', 'code': 'lat', 'length': 3}])
        self.assertTrue(hasattr(alphabet_3_times_diff_args, '__iter__'))
        self.assertTrue(hasattr(alphabet_3_times_diff_args, '__next__'))
        self.assertFalse(hasattr(alphabet_3_times_diff_args, '__getitem__'))
        self.assertFalse(hasattr(alphabet_3_times_diff_args, '__len__'))

        result = list('абвгдежзи')
        solution_result = list(alphabet_3_times_diff_args)
        self.assertEqual(solution_result, result)

    def test_for_endless_argument(self):
        def endless_sequences():
            for key in cycle(['fibonacci', 'primes', 'alphabet']):
                if key == 'alphabet':
                    yield {'sequence': key, 'length': 1, 'code': 'bg'}
                else:
                    yield {'sequence': key, 'length': 1}

        generator = solution.intertwined_sequences(endless_sequences())
        self.assertTrue(hasattr(generator, '__iter__'))
        self.assertTrue(hasattr(generator, '__next__'))
        self.assertFalse(hasattr(generator, '__getitem__'))
        self.assertFalse(hasattr(generator, '__len__'))

        solution_result = list(islice(generator, 6))
        self.assertEqual(solution_result, [1, 2, 'а', 1, 3, 'б'])

    def test_with_other_generators(self):
        input_ = [{'sequence': 'square', 'length': 3},
                  {'sequence': 'pentagonal', 'length': 3},
                  {'sequence': 'catalan', 'length': 3}]

        input_definitions = {'square': square,
                             'pentagonal': pentagonal,
                             'catalan': catalan}

        result = [1, 4, 9, 1, 5, 12, 1, 1, 2]
        generator = solution.intertwined_sequences(input_,
                                    generator_definitions=input_definitions)
        self.assertTrue(hasattr(generator, '__iter__'))
        self.assertTrue(hasattr(generator, '__next__'))
        self.assertFalse(hasattr(generator, '__getitem__'))
        self.assertFalse(hasattr(generator, '__len__'))

        solution_result = list(generator)
        self.assertEqual(solution_result, result)

    def test_with_other_generators_and_args(self):
        input_ = [{'sequence': 'square_from_to', 'length': 2,
                   'from_': 1, 'to_': 3},
                  {'sequence': 'pentagonal_from_to', 'length': 2,
                   'from_': 1, 'to_': 3},
                  {'sequence': 'catalan_from_to', 'length': 2,
                   'from_': 0, 'to_': 3}]

        input_definitions = {'square_from_to': square_from_to,
                             'pentagonal_from_to': pentagonal_from_to,
                             'catalan_from_to': catalan_from_to}

        result = [1, 4, 1, 5, 1, 1]
        generator = solution.intertwined_sequences(input_,
                                    generator_definitions=input_definitions)
        self.assertTrue(hasattr(generator, '__iter__'))
        self.assertTrue(hasattr(generator, '__next__'))
        self.assertFalse(hasattr(generator, '__getitem__'))
        self.assertFalse(hasattr(generator, '__len__'))

        solution_result = list(generator)
        self.assertEqual(solution_result, result)

    def test_with_same_generator_but_diff_args(self):
        input_ = [{'sequence': 'square_from_to', 'length': 2,
                   'from_': 1, 'to_': 6},
                  {'sequence': 'square_from_to', 'length': 2,
                   'from_': 5, 'to_': 10},
                  {'sequence': 'square_from_to', 'length': 2,
                   'from_': 10, 'to_': 13}]

        input_definitions = {'square_from_to': square_from_to}

        generator = solution.intertwined_sequences(input_,
                                    generator_definitions=input_definitions)
        self.assertTrue(hasattr(generator, '__iter__'))
        self.assertTrue(hasattr(generator, '__next__'))
        self.assertFalse(hasattr(generator, '__getitem__'))
        self.assertFalse(hasattr(generator, '__len__'))

        result = [1, 4, 9, 16, 25, 36]
        solution_result = list(generator)
        self.assertEqual(solution_result, result)


def square():
    n = 1
    while True:
        yield n * n
        n += 1


def square_from_to(from_=5, to_=10):
    for n in range(from_, to_ + 1):
        yield n * n


def pentagonal():
    n = 1
    while True:
        yield int((3 * n * n - n) / 2)
        n += 1


def pentagonal_from_to(from_=5, to_=10):
    for n in range(from_, to_ + 1):
        yield int((3 * n * n - n) / 2)


def catalan():
    n = 0
    while True:
        yield int(factorial(2 * n) / factorial(n + 1) / factorial(n))
        n += 1


def catalan_from_to(from_=5, to_=10):
    for n in range(from_, to_ + 1):
        yield int(factorial(2 * n) / factorial(n + 1) / factorial(n))

if __name__ == '__main__':
    unittest.main()
