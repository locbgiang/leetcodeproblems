'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
'''

def generateMatrix(n):
    matrix = [['.']*n for i in range(n)]
    
    left, right = 0, len(matrix[0])
    top, bot = 0, len(matrix)
    count = 1

    while left<right and top<bot:

        for i in range(left,right):         # fill out top row
            matrix[top][i] = count
            count += 1
        top += 1                            # top row is filled, move top pointer down

        for i in range(top, bot):           # fill out right column
            matrix[i][right-1] = count
            count += 1
        right -= 1                          # right column filled, move right pointer left

        for i in range(right-1, left-1, -1):    # fill out bottom row
            matrix[bot-1][i] = count
            count += 1 
        bot -= 1                            # move bot pointer up

        for i in range(bot-1, top-1, -1):   # fill out left column
            matrix[i][left] = count
            count += 1
        left += 1                           # move left pointer right

    return matrix

n = 3
generateMatrix(n)