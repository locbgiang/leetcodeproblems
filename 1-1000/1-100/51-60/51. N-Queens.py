'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
'''

def solveNQueens(n):
    answer = []
    # create 3 sets to keep track queens, queens can not be in the same column and diagonal.
    column = set()
    diagonalPos = set() # col - row
    diagonalNeg = set() # row + col

    board = [['.']*n for i in range(n)]

    def callback(row):
        if row == n:
            copy = ["".join(row) for row in board]
            answer.append(copy)
            return 

        for col in range(n):                # loop through the row
            if col in column or (row+col) in diagonalNeg or (col-row) in diagonalPos:       # if position is invalid move on
                continue
            board[row][col] = 'Q'           # try queen
            column.add(col)                 # add queen col 
            diagonalNeg.add(col+row)        # add diagonal
            diagonalPos.add(col-row)
            callback(row+1)                 # move on to next row

            board[row][col] = '.'           # after that try '.'
            column.remove(col)              # remove added set
            diagonalNeg.remove(col+row)
            diagonalPos.remove(col-row)

    
    callback(0)
    return answer 

n = 3
solveNQueens(n)