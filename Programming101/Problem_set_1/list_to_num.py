def list_to_numbers(digits):
    number = 0
    for item in digits:
        number += item
        digits.remove(item)
        number *= 10
    return number
print(list_to_numbers([1, 2, 3]))
# I know it doesn't work properly, I just don't know why :(
