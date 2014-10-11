from fibonacci_lists import nth_fib_lists


def fib_random_numbers(a, b):
    result = []
    for index in range(0, 10):
        if index == 0:
            result.append(a)
        elif index == 1:
            result.append(b)
        else:
            result.append(result[index - 1] + result[index - 2])
    return result
#print(fib_random_numbers(3, 2))


def member_of_nth_fib_lists(listA, listB, needle):
    lst = fib_random_numbers(len(listA), len(listB))
    print(lst)
    if len(needle) not in lst:
        return False
    else:
        for item in needle:
            if (item not in listA) and (item not in listB):
                return False
        return needle == nth_fib_lists(listA, listB, lst.index(len(needle)) + 1)
print(member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
