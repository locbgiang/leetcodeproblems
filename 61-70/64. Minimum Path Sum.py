'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''
def minPathSum(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 and col == 0:                   # start position, set it as itself
                grid[row][col] = grid[row][col]
            elif row == 0:                              # for the rest of the top row, add itself and the number to the left
                grid[row][col] += grid[row][col-1]      # there is only one path, right therefore this new number represent the lowest
            elif col == 0:                              # same idea but for the first column
                grid[row][col] += grid[row-1][col]
            else:                                       # otherwise add the current number and the minimum of either top or left number
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
    return grid[-1][-1]                                 # return the last number


grid = [[1,3,1],[1,5,1],[4,2,1]]
minPathSum(grid)