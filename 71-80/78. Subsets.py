'''
Given an integer array nums of unique elements, return all possible 
subsets
(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''
def subsets(nums):
    answer = []
    def backtrack(start, combine):
        answer.append(combine.copy())
        for i in range(start, len(nums)):
            combine.append(nums[i])
            backtrack(i+1, combine)
            combine.pop()
    backtrack(0, [])
    return answer


nums = [1,2,3]
print(subsets(nums))