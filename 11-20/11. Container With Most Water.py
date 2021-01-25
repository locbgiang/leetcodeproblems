'''
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
'''

# Solution:
def maxArea (height):
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])     # area of current left and right
        result = max(area, result)                                  # asign result to the higher of the two between current and new area
        if height[left] < height[right]:                           # move left right if left is lower
            left += 1
        else:                                                       # move right left if right is lower
            right -= 1
    return result

# Solution
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))