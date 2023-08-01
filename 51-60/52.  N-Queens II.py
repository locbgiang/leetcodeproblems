'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1
'''

def totalNQueens(n):
    answer = 0
    
    column = set()
    negDiag = set() # col + row
    posDiag = set() # col - row

    def callback(row):
        if row == n:
            nonlocal answer
            answer += 1
            return
        for col in range(n):
            if col in column or (col+row) in negDiag or (col-row) in posDiag:
                continue
            else:
                column.add(col)
                negDiag.add(col+row)
                posDiag.add(col-row)
                callback(row+1)

                column.remove(col)
                negDiag.remove(col+row)
                posDiag.remove(col-row)
        return

    callback(0)
    print(answer)
    return answer



n = 4
totalNQueens(n)