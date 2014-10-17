def sum_of_divisors(n):
    if n == 1:
        return 1
    result = 1 + n
    if n > 0:
        for i in range(2, n):
            if n % i == 0:
                result += i
    else:
        return 0
    return result
