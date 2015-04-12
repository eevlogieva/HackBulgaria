def contains_digits(number, digits):
    count = 0
    for digit in digits:
        if str(digit) in str(number):
            count += 1
    if count == len(digits):
            return True
    else:
        return False
print (contains_digits(2307, [2, 3, 0, 8]))
