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
    def backtrack(row, col, counter, path):
        if board[row][col] == word[counter] and counter == len(word)-1:
            return True
        path.append([row, col])
        print(path)
        counter += 1
        if col > 0 and board[row][col-1] == word[counter] and [row,col-1] not in path:
            if backtrack(row, col-1, counter, path):
                return True
        if col < len(board[0])-1 and board[row][col+1] == word[counter] and [row,col+1] not in path:
            if backtrack(row, col+1, counter, path):
                return True
        if row > 0 and board[row-1][col] == word[counter] and [row-1,col] not in path:
            if backtrack(row-1, col, counter, path):
                return True
        if row < len(board)-1 and board[row+1][col] == word[counter] and [row+1,col] not in path:
            if backtrack(row+1, col, counter, path):
                return True
        path.pop()
        return False

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if backtrack(row, col, 0, []):
                    return True
            
    return False

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(exist(board, word))