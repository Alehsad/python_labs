def col_sums(matrix):

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            return "ValueError"
    
    return [sum(col) for col in zip(*matrix)]


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))