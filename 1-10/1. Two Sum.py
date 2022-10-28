'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

'''
nums = [2, 7, 11, 15]
target = 9

# Solution:
def twoSum(nums, target):
    memory = {}        
    answer = []

    for i in range(0, len(nums)):                     # create a dictionary of the array
        memory[i] = nums[i]

    for i in range(0, len(nums)):
        value = memory.pop(i, -1)                     # pop the memory at i
        lookingFor = target - value
        if lookingFor in memory.values():
            for j in memory:
                if memory[j] == lookingFor:         # look for number that add with the popped to get target
                    answer.append(i)
                    answer.append(j)
                    return answer
# Solution
print(twoSum(nums, target))
'''

import enum


nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):                       # this new way has O(n) coefficient 
    memory = {} # val : index
    for i, n in enumerate(nums):
        find = target - n
        if find in memory:                      # if find is in memory 
            return [memory[find], i]            # return index of find
        memory[nums[i]] = i                     # add value :  index to memory
    return


print(twoSum(nums, target))