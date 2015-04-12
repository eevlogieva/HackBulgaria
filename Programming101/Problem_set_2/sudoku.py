def sudoku_solved(sudoku):
    lst = []
    for row in sudoku:
        for item in range(1, 9):
            if item not in row:
                return False
    for i in range(0, 9):
        for j in range(0, 9):
            lst.append(sudoku[j][i])
            lst.sort()
        if lst != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        lst = []
    for item1 in [0, 3, 6]:
        for i in range(0 + item1, 3 + item1):
            for item in [0, 3, 6]:
                for j in range(0 + item, 3 + item):
                    lst.append(sudoku[i][j])
                    lst.sort()
            if lst != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            lst = []

    return True
print(sudoku_solved([[4, 5, 2, 3, 8, 9, 7, 1, 6], 
	                 [3, 8, 7, 4, 6, 1, 2, 9, 5], 
	                 [6, 1, 9, 2, 5, 7, 3, 4, 8],
	                 [9, 3, 5, 1, 2, 6, 8, 7, 4], 
	                 [7, 6, 4, 9, 3, 8, 5, 2, 1], 
	                 [1, 2, 8, 5, 7, 4, 6, 3, 9],
	                 [5, 7, 1, 8, 9, 2, 4, 6, 3], 
	                 [8, 9, 6, 7, 4, 3, 1, 5, 2], 
	                 [2, 4, 3, 6, 1, 5, 9, 8, 7]]))

