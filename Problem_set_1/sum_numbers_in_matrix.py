def sum_matrix(m):
    sum = 0
    for row in m:
        for item in row:
            sum += item
    return sum
print(sum_matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
