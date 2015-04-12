def prepare_meal(number):
    result = ''
    if number % 3 != 0 and number % 5 == 0:
        result += 'eggs'
    else:
        for item in range(0, int(number ** (1 / 3.0))):
            if 3 ** item // number == 0:
                result += item * 'spam '
        if number % 5 == 0:
            result += 'and eggs'
    return result
print(prepare_meal(45))
