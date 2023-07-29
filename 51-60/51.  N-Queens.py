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

from turtle import right


def solveNQueens(n):
    def checkValid(row, col): 
        if 'Q' in board[row]:
            return False
        for i in range(row):
            if board[i][col]=='Q':
                return False

            leftDiagonal = col - (i + 1)
            rightDiagonal = col + (i + 1)
            if leftDiagonal >= 0:
                if board[row-(i+1)][leftDiagonal]=='Q':
                    return False
            if rightDiagonal < len(board):
                if board[row-(i+1)][rightDiagonal]=='Q':
                    return False
        return True

    def solver(col):
        strArr = []
        for x in range(n):
            if x == col:
                board[0][x] = 'Q'
        strArr.append("".join(board[0]))
        queenCount = 1

        for i in range(1, n):
            for j in range(0, n):
                if checkValid(i, j):
                    board[i][j] = 'Q'
                    queenCount += 1
            strArr.append("".join(board[i]))
        if queenCount == n:
            return strArr
        else:
            return False

    answer = []
    board = [['.']*n for i in range(n)]
    for y in range(n):
        x = solver(y)
        if x:
            answer.append(x)
        board = [['.']*n for i in range(n)]
    print(answer)
    return answer

n = 5
solveNQueens(n)



'''
    for row in range(len(board)):
        for col in range(len(board[row])):
            if checkValid(row, col, queenCount):
                board[row][col] = 'Q'
            else:
                board[row][col] = '.'

    def solver(row, col, queenCount):
        if row == n:
            if queenCount == n:
                return True
            else:
                return False
        if col == n:
            return solver(row+1, 0, queenCount)

        option = ['Q', '.']
        for i in option:
            if i == 'Q':
                if checkValid(row, col):
                    board[row][col] = 'Q'
                    if solver(row, col+1, queenCount+1):
                        return True
                    else: 
                        board[row][col] = '.'
                        return solver(row, col+1, queenCount)
                else:
                    board[row][col] == '.'
                    return solver(row, col+1, queenCount)
            else:
                return solver(row, col+1, queenCount)
    '''