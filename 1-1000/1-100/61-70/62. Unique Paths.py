'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

'''
example: 
m = 3, n = 7

let ?s represent the number of paths the robot can take towards "end"
[start] [?] [?] [?] [?] [?] [?]
    [?] [?] [?] [?] [?] [?] [?]
    [?] [?] [?] [?] [?] [?] [end] 

when the robot is at right most column there is only one path to end: down
same thing when the robot is at the bottom row, it can only go right
[start] [?] [?] [?] [?] [?] [1]
    [?] [?] [?] [?] [?] [?] [1]
    [1] [1] [1] [1] [1] [1] [end] 

we can see that the position top left of end has two different paths to end
this is because the robot can go right or down.  mathematically, we can say that bottom + right = current
[start] [?] [?] [?] [?] [?] [1]
    [?] [?] [?] [?] [?] [2] [1]
    [1] [1] [1] [1] [1] [1] [end] 

the position to the left of 2 has 3 different unique paths toward end, going down or going right, which will have two paths
1(down) + 2(right) = 3
[start] [?] [?] [?] [?] [?] [1]
    [?] [?] [?] [?] [3] [2] [1]
    [1] [1] [1] [1] [1] [1] [end] 

repeating this process we can find the number of paths the start position will have
'''



def uniquePaths(m, n):
    row = [1]*n                 # this represent the bottomn row
    for i in range(m-1):        # repeating for however many rows there are above the bottom row
        newRow = [1]*n          # this is the row above the bottom row
        for j in range(n-2, -1, -1):    # starting from 2nd to last column, we will go backward 
            newRow[j] = newRow[j+1] + row[j]        # the number of paths we can take at the current 
            # number of paths at current position = paths of right + paths of bottom
        row = newRow            # move the bottom row up
    # currently row represents the top row, we can return the first value to find the number of paths at start
    return row[0]


m = 3
n = 7
uniquePaths(m, n)