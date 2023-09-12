'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1
'''
def maximalRectangle(matrix):
    n = len(matrix[0])+1
    heights = [0] * (n)     # heights of current row, end with extra [0] 
    max_area = 0            # answer
    for row in matrix:      # loop through every row in matrix
        for i in range(len(matrix[0])):     # for every num in col
            if row[i] == '1':               # if '1', add 1 into height at [i]
                heights[i] = heights[i] + 1  
            else:
                heights[i] = 0
        # heights ex = [3, 1, 3, 2, 2, 0] where each number represent how many '1' in that col on top
        # now it is essentially prolem 84, we find the biggest square
        stack = [-1]    # set a -1 before index 0
        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]        # set h using last index from stack
                w = i - stack[-1] - 1           # w is the length until the next index of stack 
                max_area = max(max_area, h*w)
            stack.append(i)             # save the index since it can still extend
    return max_area


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
maximalRectangle(matrix)
'''
[   ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
'''