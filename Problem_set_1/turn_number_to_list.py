def number_to_list(num):
    lst = []
    while(num):
        lst.append(num % 10)
        num //= 10
    return lst
print(number_to_list(123))
