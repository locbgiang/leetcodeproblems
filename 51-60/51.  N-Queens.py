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
    column = set()
    diagonalPos = set() # col - row
    diagonalNeg = set() # row + col

    board = [['.']*n for i in range(n)]

    def callback(row):
        if row == n:
            copy = ["".join(row) for row in board]
            answer.append(copy)
            return 

        for col in range(n):
            if col in column or (row+col) in diagonalNeg or (col-row) in diagonalPos:
                continue
            board[row][col] = 'Q'
            column.add(col)
            diagonalNeg.add(col+row)
            diagonalPos.add(col-row)
            callback(row+1)

            column.remove(col)
            diagonalNeg.remove(col+row)
            diagonalPos.remove(col-row)
            board[row][col] = '.'
        print('here', board)
    
    callback(0)
    print(answer)
    print(board)
    return answer 

n = 3
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