LAT_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
BG_ALPHABET = 'абвгдежзийклмнопрстуфхцчшщъьюя'


def fibonacci():
    prev_prev_fib = 0
    prev_fib = 1
    yield 1
    while True:
        result = prev_fib + prev_prev_fib
        prev_prev_fib = prev_fib
        prev_fib = result
        yield result


def is_prime(number):
    if number < 2:
        return False
    for elem in range(2, number//2):
        if number % elem == 0:
            return False
    return True


def primes():
    yield 2
    yield 3
    prev_prime = 3
    current = prev_prime
    while True:
        found = False
        while not found:
            current += 2
            if(is_prime(current)):
                found = True
                prev_prime = current
                yield current


def alphabet(*, code='lat', letters=''):
    if letters:
        for letter in letters:
            yield letter
    elif code == 'bg':
        for letter in BG_ALPHABET:
            yield letter
    else:
        for letter in LAT_ALPHABET:
            yield letter


def intertwined_sequences(sequences, *, generator_definitions={}):
    generators = {'fibonacci': fibonacci,
                  'primes': primes,
                  'alphabet': alphabet
                  }
    generator_instances = {}
    for current in sequences:
        seq = current['sequence']
        if seq not in generator_instances:
            kwargs = current.copy()
            del kwargs['sequence']
            del kwargs['length']
            if seq in ['fibonacci', 'primes', 'alphabet']:
                generator_instances[seq] = iter(generators[seq](**kwargs))
            else:
                generator_instances[seq] = iter(
                    generator_definitions[seq](**kwargs))
        for value in range(current['length']):
                yield next(generator_instances[seq])
