'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''
def exist(board, word):
    def dfs(row, col, counter):
        if counter == len(word):
            return True
        elif (row < 0) or (col<0) or (row >= m) or (col >= n) or (board[row][col] != word[counter]):
            return False

        save, board[row][col] = board[row][col], 'used'
        if dfs(row+1, col, counter+1) or dfs(row-1, col, counter+1) or dfs(row, col-1, counter+1) or dfs(row, col+1, counter+1):
            return True
        else:
            board[row][col] = save
            return False
    m, n = len(board), len(board[0])
    for row in range(m):
        for col in range(n):
            if board[row][col] == word[0]:
                if dfs(row, col, 0):
                    return True
    return False
'''
[   ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]]
    "ABCESEEEFS"

'''

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))