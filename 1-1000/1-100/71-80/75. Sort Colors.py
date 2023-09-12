'''
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
 
'''

def sortColors(nums):
    red = 0
    white = 0
    blue = 0
    for num in nums:
        if num == 0:
            red += 1
        elif num == 1:
            white += 1
        else:
            blue += 1
    for i in range(len(nums)):
        if red > 0:
            nums[i] = 0
            red -= 1
        elif white > 0:
            nums[i] = 1
            white -= 1
        else:
            nums[i] = 2
            blue -= 1
    return

nums = [2,0,2,1,1,0]
sortColors(nums)