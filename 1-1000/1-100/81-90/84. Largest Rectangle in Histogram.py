'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
'''
def largestRectangleArea(heights):
    answer = 0
    heights = heights + [0]
    stack = [-1]
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            answer = max(answer, heights[stack.pop()]*(i - stack[-1] - 1))
        stack.append(i)
    return answer



heights = [1,2]
largestRectangleArea(heights)