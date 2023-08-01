'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4] (sorted [-4, -1, 1, 2]), target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

def threeSumClosest(nums, target):
    nums.sort()
    targetLeft = target
    targetRight = target
    sum = 0
    while True:                                                # runs forever
        for left in range(0, len(nums)-2):
            for mid in range(left+1, len(nums)-1):
                for right in range(mid+1, len(nums)):           # brute force 3 forloops 
                    sum = nums[left] + nums[mid] + nums[right]  # sum for all numbers
                    if sum == targetLeft:
                        return targetLeft
                    elif sum == targetRight:
                        return targetRight
        targetLeft -= 1                                         # if no match, move left and right 1 from target
        targetRight += 1

nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))
