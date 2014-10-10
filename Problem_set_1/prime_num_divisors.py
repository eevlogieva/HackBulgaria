from is_prime import is_prime


def prime_num_divisors(n):
    divisors = [1, n]
    for index in range(2, n-1):
        if n % index == 0:
            divisors.append(index)
    return is_prime(len(divisors))
print(prime_num_divisors(9))
