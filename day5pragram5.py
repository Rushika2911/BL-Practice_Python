# PROG 5: Transpose Matrix

# Transpose a matrix: Given a 3 X 3 matrix of numbers as two dimensional list of numbers, develop a function which does transpose this matrix

# Input =>Original Matrix :
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Output =>
# ```
# Transpose matrix
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

# ```

# PROG 5: Transpose Matrix
def transpose_matrix(matrix):
    ROW= len(matrix)
    COLS= len(matrix[0])
    transposed_matrix= [[0,0,0],[0,0,0],[0,0,0]]
    for row in range(ROW):
        for col in range(COLS):
            transposed_matrix[row][col]= matrix[col][row]
    
    return transposed_matrix

matrix= [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    print(row)

transposed= transpose_matrix(matrix)

for row in transposed:
    print(row)