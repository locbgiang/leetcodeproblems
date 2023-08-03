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

[start] [?] [?] [?] [?] [?] [1]
    [?] [?] [?] [?] [?] [?] [1]
    [1] [1] [1] [1] [1] [1] [end] 
when the robot is at right most column there is only one path to end
same thing with bottom most row

we can see that the position top left of end has two different path to end
this is because the robot can go right or down.  mathematically, we can say that bottom + right = current
[start] [?] [?] [?] [?] [?] [1]
    [?] [?] [?] [?] [?] [2] [1]
    [1] [1] [1] [1] [1] [1] [end] 

the position to the left of 2 has 3 different unique paths toward end, going down, going right and then right or down
we can see that 2 + 1 = 3
[start] [?] [?] [?] [?] [?] [1]
    [?] [?] [?] [?] [3] [2] [1]
    [1] [1] [1] [1] [1] [1] [end] 

repeating this process we can find the number of paths the start position will have
'''



def uniquePaths(m, n):
    row = [1]*n

    for i in range(m-1):    
        newRow = [1]*n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    print(row)


m = 3
n = 7
uniquePaths(m, n)