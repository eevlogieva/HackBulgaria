from is_prime import is_prime


def goldbach(n):
    result = []
    for item in range(2, n // 2 + 1):
        if is_prime(item) and is_prime(n - item):
            result.append((item, n - item))
    return result
