'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

def setZeroes(matrix):
    row_mem = []
    col_mem = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                row_mem.append(row)
                col_mem.append(col)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in row_mem:
                matrix[row][col] = 0
            if col in col_mem:
                matrix[row][col] = 0
    print(matrix)
    return 


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)