'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
Explanation: The input board is shown above and the only valid solution is shown below:

'''

def solveSudoku(board):
    def validChecker(row, col, val):
        boxRow = (row//3) * 3
        boxCol = (col//3) * 3
        for i in range(9):
            if board[row][i] == val:
                return False

            if board[i][col] == val:
                return False

            iBoxRow = i//3              # ex: 0 0 0 1 1 1 2 2 2 
            iBoxCol = i%3               # ex: 0 1 2 0 1 2 0 1 2
            if board[boxRow+iBoxRow][boxCol+iBoxCol] == val:
                return False
        return True

    def solver(row, col):
        if row == 9:                # end, return true for line 64
            return True
        if col == 9:                # move on to next row
            return solver(row+1, 0)

        if board[row][col] == '.':      # if . 
            for i in range(1, 10):      # try out everything from 1 to 9
                if validChecker(row, col, str(i)):      # current i is valid
                    board[row][col] = str(i)            # set current spot to str(i)
                    if solver(row, col + 1):            # call next spot
                        return True                     # if next spot is valid return true for the previous spot
                    else:
                        board[row][col] = '.'           # otherwise change back to '.' and try a new number in validchecker 
        else:
            return solver(row, col+1)           # not a '.' move on to next spot
    solver(0, 0)


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
boardanswer=[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)
print(board)