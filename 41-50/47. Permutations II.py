'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

def permuteUnique(nums):
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return [nums[:]]
        return nums[:], nums[::-1]
    elif len(nums) == 1:
        return [nums]
    
    answer = []
    for i in range(len(nums)):
        head = nums.pop(i)
        bodies = permuteUnique(nums)
        nums.insert(i, head)
        for body in bodies:
            if [head]+body not in answer:
                answer.append([head]+body)
    return answer


nums = [1,1,2]
print(permuteUnique(nums))