def is_number_balanced(n):
    left_sum = 0
    right_sum = 0
    digits = len(str(n))
    if digits % 2 == 0:
        for index in range(digits // 2):
            right_sum += n % 10
            n //= 10
        while(n):
            left_sum += n % 10
            n //= 10
    elif digits == 1:
        return True
    else:
        for digit in range(digits // 2):
            right_sum += n % 10
            n //= 10
        n //= 10
        while(n):
            left_sum += n % 10
            n //= 10
    return left_sum == right_sum
print(is_number_balanced(28471))
