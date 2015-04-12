def magic_square(matrix):
    if check_rows[0] and check_columns[0] and check_diagonals[0]:
        return check_diagonals[1] == check_columns[1] == check_rows[1]


def check_rows(matrix):
    sum = 0
    sum1 = 0
    for item in matrix[0]:
        sum += item
    for row in matrix[1:]:
        sum1 = 0
        for item in row:
            sum1 += item
        if sum != sum1:
            return (False, sum)
    return (True, sum)


def check_columns(matrix):
    sum = 0
    sum1 = 0
    for i in range(len(matrix)):
        sum += matrix[i][0]
    for i in range(len(matrix)):
        sum1 = 0
        for j in range(len(matrix)):
            sum1 += matrix[j][i]
        if sum1 != sum:
            return (False, sum)
    return (True, sum)


def check_diagonals(matrix):
    sum1, sum2 = 0, 0
    for i in range(len(matrix)):
        sum1 += matrix[i][i]
        sum2 += matrix[i][len(matrix) - 1 - i]
    if sum1 != sum2:
        return (False, sum1)
    return (True, sum1)
