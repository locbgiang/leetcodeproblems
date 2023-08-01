'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''
def permute(nums):
    if len(nums) == 2:
        return nums[:], nums[::-1]
    elif len(nums) == 1:
        return [nums]
    
    answer = []
    for i in range(len(nums)):
        head = nums.pop(i)          # pop head out
        bodies = permute(nums)      # recursion call with body until length of body == 2
        nums.insert(i, head)        # add head back in
        for body in bodies:         
            answer.append([head]+body)          # add head to new bodies, then append to answer

    return answer


nums = [1,2,3,4]
print(permute(nums))