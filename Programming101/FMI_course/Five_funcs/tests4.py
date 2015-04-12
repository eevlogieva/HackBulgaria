import unittest
import solution


class ExtractTypeTest(unittest.TestCase):
    def test_snake(self):
        input = [('s', 1), ('n', 1), ('a', 1),
                 ('k', 1), ('e', 1), (55, 1)]
        self.assertEqual("snake", solution.extract_type(input, str))

    def test_monty_python(self):
        input = [('m', 1), (8, 108), ('o', 1), ('n', 1), ('t', 1), ('y', 1), (55, 1),
                 ('p', 1), ('y', 1), (114, 22), ('t', 1), ('h', 1), ('o', 1), ('n', 1)]
        self.assertEqual("montypython", solution.extract_type(input, str))

    def test_cheese(self):
        input = [('c', 1), ('h', 1), (1, 1), ('e', 2), ('s', 1), (5, 0),
                 (12, 1), (55, 1), (1, 2), ('e', 1), (1, 1)]
        self.assertEqual("cheese", solution.extract_type(input, str))

    def test_america(self):
        input = [('A', 1), ('m', 1), ('e', 1), ('r', 1), ('i', 1),
                 (33, 1), (453, 1), (2, 1), ('c', 1), (4, 3),
                 ('a', 1), (3, 1)]
        self.assertEqual("America", solution.extract_type(input, str))

    def test_number(self):
        input = [('hg', 19), ('h', 15), (1, 4), ('kk', 4), ('yu', 1),
                 ('a', 1), ('k', 1), ('qqw', 1), (1, 2), (4, 3),
                 ('kl', 1), (3, 10)]
        self.assertEqual("1111114443333333333", solution.extract_type(input, int))

class ReversedDictTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual({}, solution.reversed_dict({}))

    def test_food(self):
        input = {'Cake': '11', 'Rice': '312', 'Noodle': 'yuck!',
                 'Bread': '24', 'Eggs': '21', 'Cheese': 'yummy'}
        output = {'11': 'Cake', '21': 'Eggs', '312': 'Rice',
                  'yuck!': 'Noodle', '24': 'Bread', 'yummy': 'Cheese'}
        self.assertEqual(solution.reversed_dict(input), output)

    def test_champions(self):
        input = {'adc': 'ashe', 'mid': 'veigar',
                'top': 'fiora', 'support': 'braum', 'jungle': 'fizz'}
        output = {'ashe': 'adc', 'veigar': 'mid', 'fiora': 'top',
                    'braum': 'support', 'fizz': 'jungle'}
        self.assertEqual(solution.reversed_dict(input), output)

    def test_gender(self):
        result = solution.reversed_dict({'ivan': 'M', 'jodie': 'F', 'jack': 'M',
                                            'jessy': 'F', 'bianca': 'F'})
        self.assertIn('F', result.keys())
        self.assertIn(result['M'], ['ivan', 'jack'])
        self.assertIn(result['F'], ['jessy', 'bianca', 'jodie'])

    def test_animals(self):
        input_ = {"cat": 2, "dog": 1, "monkey": 1, "gopher": 3}
        input_ = {'minh': 'cat', 'ivan': 'dog', 'jess': 'parrot',
                    'plamen': 'rabbit', 'stoqn': 'cat', 'dari': 'cat'}
        output = solution.reversed_dict(input_)
        self.assertEqual(output['dog'], 'ivan')
        self.assertEqual(output['rabbit'], 'plamen')
        self.assertEqual(output['parrot'], "jess")
        self.assertIn(output['cat'], ['minh', 'stoqn', 'dari'])

class FlattenDictTest(unittest.TestCase):

    def test_names(self):
        input_ = {'steve': 12,
                  'jack': {'jess': 21,
                            'karry': 31,
                            'molly': {'peny': 33,
                                      'john': 44}},
                  'lily': 3}

        output = {'steve': 12, 'jack.jess': 21, 'jack.karry': 31,
                  'jack.molly.peny': 33, 'jack.molly.john': 44,
                  'lily': 3}
        self.assertEqual(solution.flatten_dict(input_), output)

    def test_ab(self):
        input_ = {'a': 123,
                  'b': {'a': 212,
                        'b': {'a': 777}
                       }}

        output = {'a': 123, 'b.a': 212, 'b.b.a': 777}
        self.assertEqual(output, solution.flatten_dict(input_))

    def test_games_type(self):
        input_ = {'moba': 'league_of_legends',
                  'fps': {'dota': 12,
                          'call_of_duty': {'battlefield': 777}
                         }}

        output = {'moba': 'league_of_legends', 'fps.dota': 12, 'fps.call_of_duty.battlefield': 777}
        self.assertEqual(output, solution.flatten_dict(input_))

class UnflattenDictTest(unittest.TestCase):

    def test_names(self):
        input_ = {'steve': 12, 'jack.jess': 21, 'jack.karry': 31,
                  'jack.molly.peny': 33, 'jack.molly.john': 44,
                  'lily': 3}

        output = {'steve': 12,
                  'jack': {'jess': 21,
                            'karry': 31,
                            'molly': {'peny': 33,
                                      'john': 44}},
                  'lily': 3}
        self.assertEqual(solution.unflatten_dict(input_), output)

    def test_ab(self):
        input_ = {'a': 123, 'b.a': 212, 'b.b.a': 777}

        output = {'a': 123,
                  'b': {'a': 212,
                        'b': {'a': 777}
                       }}
        self.assertEqual(output, solution.unflatten_dict(input_))

    def test_games_type(self):
        input_ = {'moba': 'league_of_legends', 'fps.dota': 12, 'fps.call_of_duty.battlefield': 777}

        output = {'moba': 'league_of_legends',
                  'fps': {'dota': 12,
                          'call_of_duty': {'battlefield': 777}
                         }}

        self.assertEqual(output, solution.unflatten_dict(input_))

class RepsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual((), solution.reps((1, 2, 7, 43, 52, 61)) )
        self.assertEqual((), solution.reps(()) )
        self.assertEqual((), solution.reps([]) )
        self.assertEqual((), solution.reps([2]) )
        self.assertEqual((), solution.reps((1,)) )

    def test_ones(self):
        self.assertEqual((1, 1, 1, 1, 1, 1, 1, 1), solution.reps((1, 1, 1, 1, 1, 1, 1, 1)))
        self.assertEqual((1, 1, 1, 1, 1, 1, 1, 1), solution.reps([1, 1, 1, 1, 1, 1, 1, 1]))


    def test_non_empty(self):
        self.assertEqual((1, 1, 2, 2, 3, 3), solution.reps([1, 1, 2, 2, 3, 3]))
        self.assertEqual((6, 5, 6, 5), solution.reps([6, 1, 5, 6, 2, 3, 4, 5]))
        self.assertEqual((1, 2, 7, 1, 2, 7, 1, 9, 2, 9), solution.reps((1, 2, 7, 1, 2, 7, 1, 9, 2, 9)))

    def test_example_case(self):
        self.assertEqual(
            (1, 5, 2, 2, 1, 2, 5, 1),
            solution.reps([1, 5, 2, 6, 90, 2, 4, 11, 1, 9, 0, 2, 5, 3, 1])
        )

    def test_letters(self):
        input_ = ['f', 's', 's', 'w', 'b', 'l', 'f',
                  'a', 'z', 'z', 'i', 't', 'm', 'd', 'x', 's', 't']
        output = ('f', 's', 's', 'f',
                  'z', 'z', 't', 's', 't')
        self.assertEqual(solution.reps(input_), output)

    def test_bool(self):
        input_ = [False, True, False, False]
        output = (False, False, False)
        self.assertEqual(solution.reps(input_), output)

if __name__ == '__main__':
    unittest.main()
