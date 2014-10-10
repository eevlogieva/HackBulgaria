def sum_matrix(m):
    sum = 0
    for row in m:
        for index in row:
            sum += row[index]
    return sum
    