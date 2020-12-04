'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

nums = [2, 7, 11, 15]
target = 9

# solution:
def twoSum(nums, target):
    memory = {}
    answer = []

    for i in range(0, len(nums)):
        memory[i] = nums[i]

    for i in range(0, len(nums)):
        value = memory.pop(i, -1)
        lookingFor = target - value
        if lookingFor in memory.values():
            for j in memory:
                if memory[j] == lookingFor:
                    answer.append(i)
                    answer.append(j)
                    return answer

answer = twoSum(nums, target)
print(answer)