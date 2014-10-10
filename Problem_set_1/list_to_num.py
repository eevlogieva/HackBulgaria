def list_to_numbers(digits):
    number = 0
    for index in range(0,len(digits)-1):
        number += digits[index]
        print(number)
        digits.pop(index)
        print(number)
        number *= 10
        print(number)
    return number
print(list_to_numbers([1, 2]))
