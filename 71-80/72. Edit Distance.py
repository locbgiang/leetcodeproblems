'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

def minDistance(word1, word2):
    board = [ [0]*(len(word2)+1) for i in range(len(word1)+1)]

    for w2 in range(len(word2)+1):
        board[len(word1)][w2] = len(word2) - w2
    for w1 in range(len(word1)+1):
        board[w1][len(word2)] = len(word1) - w1
    
    for y in range(len(word1)-1, -1, -1):
        for x in range(len(word2)-1,-1,-1):
            if word1[y] == word2[x]:
                board[y][x] = board[y+1][x+1]
            else:
                board[y][x] = 1 + min(board[y][x+1], board[y+1][x], board[y+1][x+1])
    return board[0][0]

word1 = 'horse'
word2 = 'ros'
minDistance(word1, word2)