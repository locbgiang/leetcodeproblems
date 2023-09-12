'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
def twoSum(nums, target):
    mem = {}
    for i, n in enumerate(nums):
        if n in mem:
            return [mem[n], i]
        else:
            mem[target-n] = i

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

'''
for i in range(len(nums)-1):                            # loop throught nums
    leftover = target - nums[i]                         # find leftover
    if leftover in nums[i+1:]:                          # if leftover is in the remaining list after i
        return [i, nums[i+1:].index(leftover)+i+1]      # return index i and index of leftover
return 
'''