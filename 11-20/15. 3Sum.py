'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''

def threeSum (nums):
    if len(nums) < 3:                                   # if less than 3 numbers, return empty list
        return []
    answer = []
    nums.sort()                                         # sort the list
    for i in range(1, len(nums)-1):
         left = 0                                       # left at the start, right at the end
         right = len(nums)-1
         while left < i and right > i:                  # while left and right are not i
            total = nums[left] + nums[right] + nums[i]  # add left right i together
            if total > 0:                               # if total greater than 0, move right left (decrease)
                right -= 1
            elif total < 0:                             # if total less than 0, move left right (increase)
                left += 1
            else:                                       # if total = 0
                bundle = [nums[left],nums[i],nums[right]]       # bundle the 3 numbers together
                if bundle not in answer:                        # check if this answer already exist or not
                    answer.append(bundle)                       # if not then add to the answer list
                right -= 1                              # move left and right
                left += 1
    return answer
#nums = [-1, 0, 1, 2, -1, 4]
nums = [3,0,-2,-1,1,2]
print(threeSum(nums))