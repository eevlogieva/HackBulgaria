from sum_of_devisiors import sum_of_divisors


def is_prime(n):
    if n == sum_of_divisors(n) - 1:
        return True
    else:
        return False
print(is_prime(7))
