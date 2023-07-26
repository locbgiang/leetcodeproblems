'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''
def trap(height):
    answer = 0          # total water
    tallest_index = height.index(max(height))       # find tallest index

    pillar = 0                  # pillar to trap water
    for i in range(0, tallest_index):       # interate through height array stopping at tallest index
        if height[i] > pillar:              # if current height is greater than pillar
            pillar = height[i]              # set pillar at current height
        answer += pillar - height[i]        # pillar will trap water if current height is lower than pillar

    # same idea as above, iterate through height backward until tallest index
    pillar = 0                  # reset pillar
    for i in range(len(height)-1, tallest_index, -1):       
        if height[i] > pillar:
            pillar = height[i]
        answer += pillar - height[i]

    return answer



height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,3]
height3 = [4,2,0,3,2,5]
print(trap(height1))