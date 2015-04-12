def number_to_list_of_powers_of_two(number):
    binary = bin(number)
    result = []
    power = len(binary[2:]) - 1
    for digit in binary[2:]:
        if digit == '1':
            result.append(2 ** power)
        power -= 1
    return result


def powers_of_two_remain(numbers):
    powers_two = []
    for number in numbers:
        powers_two += number_to_list_of_powers_of_two(number)
    result = list(filter(lambda x: powers_two.count(x) % 2 != 0, powers_two))
    return bool(result)
