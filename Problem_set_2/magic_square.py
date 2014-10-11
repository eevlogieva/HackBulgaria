def magic_square(matrix):
    sum = 0
    sum1 = 0
    sum2 = 0
    for item in matrix[0]:
        sum += item
    for row in matrix[1:]:
        for item in row:
            sum1 += item
        if sum != sum1:
            return False
        sum1 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sum1 += matrix[j][i]
        if sum1 != sum:
            return False
        sum1 = 0
    for i in range(len(matrix)):
        sum1 += matrix[i][i]
        sum2 += matrix[i][len(matrix) - 1 - i]
    if sum1 != sum or sum2 != sum:
        return False
    return True
print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
