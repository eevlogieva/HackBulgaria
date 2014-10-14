def sum_of_divisors(n):
    result = 1 + n
    for i in range(2, n):
        if n % i == 0:
            result += i
    return result
#print(sum_of_divisors(1000))
