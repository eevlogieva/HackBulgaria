def groupby(func, seq):
    tuple_keys = (func)
    result = {}
    for index in range(len(tuple_keys)):
        result[(tuple_keys[index])] = seq[index]
    return result
print(groupby([x for x in range(0, 3)], [1, 2, 3, 4]))
