def sum_of_digits(n):
    result = 0
    if n < 0:
        n = abs(n)
    while n:
        result += n % 10
        n //= 10
    return result
print(sum_of_digits(-10))
